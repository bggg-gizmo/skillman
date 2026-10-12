#!/usr/bin/env python3
"""Verify every standalone source skill and its packaged ZIP, preserving all content."""
from __future__ import annotations
import hashlib,json,re,zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent

def main()->None:
    manifest=json.loads((ROOT/'MANIFEST.json').read_text('utf8'))
    dirs=sorted(p for p in (ROOT/'skills').iterdir() if p.is_dir())
    assert len(dirs)==manifest['skill_count']==41
    assert [p.name for p in dirs]==manifest['skills']
    archive_files=sorted((ROOT/'upload-zips').glob('*.zip'))
    assert len(archive_files)==41
    contracts=set()
    for folder in dirs:
        skill=(folder/'SKILL.md').read_text('utf8')
        assert re.search(r'^name: '+re.escape(folder.name)+r'$',skill,re.M),folder
        assert re.search(r'^description:\s+\S',skill,re.M),folder
        assert skill.startswith('---\n') and '\n---\n' in skill,folder
        refs=re.findall(r'`(references/[a-z0-9-]+\.md)`',skill)
        assert 'references/operating-contract.md' in refs
        assert 'references/local-configuration.md' in refs
        assert all((folder/ref).is_file() for ref in refs),(folder,refs)
        contracts.add((folder/'references/operating-contract.md').read_bytes())
        package=ROOT/'upload-zips'/(folder.name+'.zip')
        assert package.exists(),package
        with zipfile.ZipFile(package) as z:
            assert z.testzip() is None,package
            names=z.namelist()
            assert f'{folder.name}/SKILL.md' in names,package
            assert [x for x in names if x.endswith('/SKILL.md')]==[f'{folder.name}/SKILL.md'],package
            files={p.relative_to(ROOT/'skills').as_posix():p.read_bytes() for p in folder.rglob('*') if p.is_file()}
            assert set(names)==set(files),(package,'paths mismatch')
            for n,b in files.items(): assert z.read(n)==b,(package,n)
    assert len(contracts)==1,'Contracts differ across packages'
    assert next(iter(contracts))==(ROOT/'shared/operating-contract.md').read_bytes(), 'Canonical operating contract differs'
    assert (ROOT/'LICENSE').is_file() and 'MIT License' in (ROOT/'LICENSE').read_text('utf8'), 'MIT license missing'
    master=ROOT/'skills'/'codemaster'/'references'/'modules'
    standalone={p.name:p for p in dirs if p.name!='codemaster'}
    assert len(standalone)==40
    for skill_name,folder in standalone.items():
        original={p.relative_to(folder):p.read_bytes() for p in folder.rglob('*') if p.is_file()}
        snapshot=master/skill_name
        copied={p.relative_to(snapshot):p.read_bytes() for p in snapshot.rglob('*') if p.is_file()}
        normalized={Path('module-guide.md') if str(k)=='SKILL.md' else k:v for k,v in original.items()}
        assert normalized==copied, f'Codemaster embedded {skill_name} differs from public original (except entry-point filename)'
    bundle=ROOT/'bundles'/'skillman-all-public-skills.zip'
    with zipfile.ZipFile(bundle) as zipped:
        assert zipped.testzip() is None
        members=set(zipped.namelist())
        assert 'skillman/SKILLMANUAL.md' in members
        for folder in dirs:
            assert 'skillman/skills/'+folder.name+'/SKILL.md' in members
            archived_zip='skillman/upload-zips/'+folder.name+'.zip'
            assert archived_zip in members
            assert zipped.read(archived_zip)==(ROOT/'upload-zips'/(folder.name+'.zip')).read_bytes(), f'Bundle contains a stale standalone ZIP: {folder.name}'
            assert len([x for x in members if x.startswith('skillman/skills/'+folder.name+'/') and x.endswith('/SKILL.md')])==1
    assert len([p for p in master.rglob('SKILL.md')])==0
    assert b'For any application or programming startup montage' in next(iter(contracts))
    for path,info in manifest['files'].items():
        f=ROOT/path
        assert f.is_file(),f
        assert f.stat().st_size==info['bytes'],f
        assert hashlib.sha256(f.read_bytes()).hexdigest()==info['sha256'],f
    expected=''.join(f"{data['sha256']}  {path}\n" for path,data in sorted(manifest['files'].items()))
    assert (ROOT/'SHA256SUMS').read_text('utf8')==expected
    route=json.loads((ROOT/'skills/codemaster/references/module-routing.json').read_text('utf8'))
    assert len(route['modules'])==40
    assert {x['name'] for x in route['modules']}==set(standalone), 'Codemaster routing coverage differs'
    for extra in ('skillman/LICENSE','skillman/README.md','skillman/SKILLMANUAL.md','skillman/evals/README.md'):
        assert extra in members, f'Bundle missing {extra}'
    print('Integrity + consistency: PASS; MIT license, shared contract, 40-module routing, 41 source skills and ZIPs, codemaster snapshots, evaluation fixtures, 1 bundle')

if __name__=='__main__':main()
