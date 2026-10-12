#!/usr/bin/env python3
"""Fail on creator-specific references or secret-shaped material in public files."""
from __future__ import annotations
import hashlib,re,zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
# SHA-256 signatures of non-public identifiers from the original source.
# Store hashes rather than reintroducing the identifying terms into a public release.
BLOCKED_TOKEN_SHA256={
 'original shared asset repository': '43869e817ae7fd14fa3de7b0f7ff33ccc1ae9fd04386be454c0484d9ced26a80',
 'original repository account': '7c8b152232acb5782caf46fa0a53a7636b07639a7897d5febb92e5cf11fde6c5',
 'personal alias': 'f0dce5845962dc3700fff65ad30fbbe4241016fc70ef9e3970c53b3c975f084d'
}

PATTERNS={
 'email address':re.compile(r'(?<![\w.+-])[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}'),
 'local user home':re.compile(r'(?i)(?:/home/|/Users/)[a-zA-Z0-9_.-]+/'),
 'Windows user path':re.compile(r'(?i)[A-Z]:[\\]+Users[\\]+[a-z0-9_.-]+[\\]+'),
 'Github PAT':re.compile(r'gh[pousr]_[A-Za-z0-9_]{20,}'),
 'Github fine-grained PAT':re.compile(r'github_pat_[A-Za-z0-9_]{20,}'),
 'AWS access key':re.compile(r'AKIA[0-9A-Z]{16}'),
 'private key':re.compile(r'-----BEGIN (?:RSA|OPENSSH|EC|DSA|PGP) PRIVATE KEY-----'),
 'specific GitHub repository':re.compile(r'https?://(?:www\.)?github\.com/[^\s/`"<>]+/[^\s/`"<>]+'),
}

def inspect(name:str,data:bytes,failures:list[str])->None:
    try: text=data.decode('utf8')
    except UnicodeDecodeError: return
    # The audit script is excluded because it defines the detection patterns.
    if name.endswith('tools/audit_distribution.py'): return
    tokens=set(re.findall(r'[a-z0-9][a-z0-9_.-]{2,}',text.lower()))
    hashes={hashlib.sha256(token.encode('utf8')).hexdigest() for token in tokens}
    for label,digest in BLOCKED_TOKEN_SHA256.items():
        if digest in hashes: failures.append(f'{name}: {label}')
    for label,pattern in PATTERNS.items():
        if pattern.search(text): failures.append(f'{name}: {label}')

def main()->None:
    failures=[]
    for file in sorted(ROOT.rglob('*')):
        if not file.is_file() or file.name.endswith('.pyc'):continue
        rel=file.relative_to(ROOT).as_posix()
        if file.suffix=='.zip':
            with zipfile.ZipFile(file) as archive:
                for name in archive.namelist():
                    if name.endswith('/'):continue
                    inspect(rel+'!'+name,archive.read(name),failures)
        else: inspect(rel,file.read_bytes(),failures)
    if failures:
        print('PUBLIC SANITIZATION FAILED')
        print('\n'.join(failures))
        raise SystemExit(1)
    print('Public reference scan: PASS')

if __name__=='__main__':main()
