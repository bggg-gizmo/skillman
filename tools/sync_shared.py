#!/usr/bin/env python3
"""Copy the canonical contract to all standalone skills and master snapshots."""
from pathlib import Path
import argparse

ROOT=Path(__file__).resolve().parent.parent
SOURCE=ROOT/'shared'/'operating-contract.md'

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true',help='fail if a skill copy is out of date')
    args=parser.parse_args()
    contract=SOURCE.read_bytes()
    targets=sorted((ROOT/'skills').glob('*/references/operating-contract.md'))
    targets+=sorted((ROOT/'skills'/'codemaster'/'references'/'modules').glob('*/references/operating-contract.md'))
    if len(targets)!=81: raise SystemExit(f'Expected 81 copies (41+40), found {len(targets)}')
    dirty=[p for p in targets if p.read_bytes()!=contract]
    if args.check and dirty: raise SystemExit('Outdated shared contract: '+', '.join(str(p) for p in dirty))
    if not args.check:
        for path in dirty:path.write_bytes(contract)
    print(f'Shared contract: {len(targets)} copies, {len(dirty)} '+('out of sync' if args.check else 'synchronized'))

if __name__=='__main__':main()
