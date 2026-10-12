#!/usr/bin/env python3
"""Rebuild deterministic, self-contained skill ZIPs and SHA-256 manifest (offline)."""
from __future__ import annotations
import hashlib, json, zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
SKILLS=ROOT/'skills'
ARCHIVES=ROOT/'upload-zips'
BUNDLES=ROOT/'bundles'
FIXED_DATE=(2020,1,1,0,0,0)

def pack_one(skill_dir:Path, archive:Path)->None:
    skill_entries=[f for f in skill_dir.rglob('SKILL.md') if f.is_file()]
    if skill_entries != [skill_dir/'SKILL.md']:
        raise SystemExit(f'Skill archive must contain exactly one root SKILL.md: {skill_dir}: {skill_entries}')
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as output:
        for file in sorted(skill_dir.rglob('*')):
            if not file.is_file(): continue
            relative=file.relative_to(SKILLS).as_posix()
            info=zipfile.ZipInfo(relative,FIXED_DATE)
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=(0o100644 << 16)
            output.writestr(info,file.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)

def main()->None:
    contract=(ROOT/'shared/operating-contract.md').read_bytes()
    copies=list(SKILLS.glob('*/references/operating-contract.md'))
    copies+=list((SKILLS/'codemaster'/'references'/'modules').glob('*/references/operating-contract.md'))
    if len(copies)!=81 or any(f.read_bytes()!=contract for f in copies):
        raise SystemExit('Shared contract not synchronized; run python tools/sync_shared.py')
    ARCHIVES.mkdir(exist_ok=True)
    skill_dirs=sorted(p for p in SKILLS.iterdir() if p.is_dir() and (p.name.startswith('codeman-') or p.name=='codemaster'))
    if len(skill_dirs)!=41 or not (SKILLS/'codemaster').exists(): raise SystemExit(f'Expected 41 skills including codemaster, found {len(skill_dirs)}')
    expected={p.name+'.zip' for p in skill_dirs}
    for old in ARCHIVES.glob('*.zip'):
        if old.name not in expected: raise SystemExit('Unexpected archive; refusing to delete: '+old.name)
    for directory in skill_dirs:
        pack_one(directory,ARCHIVES/(directory.name+'.zip'))
    # One complete offline bundle with the public source, standalone packages and manuals;
    # bundle excludes itself, manifests, private archives, and VCS metadata.
    BUNDLES.mkdir(exist_ok=True)
    bundle=BUNDLES/'skillman-all-public-skills.zip'
    with zipfile.ZipFile(bundle,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as output:
        for f in sorted(ROOT.rglob('*')):
            if not f.is_file() or f==bundle or f.name in ('MANIFEST.json','SHA256SUMS'): continue
            if '.git' in f.parts or '__pycache__' in f.parts: continue
            name=f.relative_to(ROOT).as_posix()
            info=zipfile.ZipInfo('skillman/'+name,FIXED_DATE)
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=(0o100644 << 16)
            output.writestr(info,f.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
    paths=sorted(p for p in ROOT.rglob('*') if p.is_file() and p.name not in ('MANIFEST.json','SHA256SUMS') and not p.is_relative_to(ROOT/'.git'))
    files={p.relative_to(ROOT).as_posix(): {'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in paths}
    manifest={'schema_version':1,'skill_count':len(skill_dirs),'skills':[p.name for p in skill_dirs],'files':files}
    (ROOT/'MANIFEST.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n',encoding='utf8')
    (ROOT/'SHA256SUMS').write_text(''.join(f"{x['sha256']}  {p}\n" for p,x in files.items()),encoding='utf8')
    print('Built',len(skill_dirs),'archives, 1 complete bundle, and',len(files),'checksummed files')

if __name__=='__main__': main()
