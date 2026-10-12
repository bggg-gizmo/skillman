#!/usr/bin/env python3
"""Verify 40-specialty routing coverage and selection-cost structure offline."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent

def main():
    skill=ROOT/'skills'/'codemaster'
    route=json.loads((skill/'references/module-routing.json').read_text('utf8'))
    modules=route['modules']
    names=[item['name'] for item in modules]
    assert len(names)==40 and len(names)==len(set(names)), 'Routing must consider all 40 modules'
    assert 'codeman-core' in route['mandatory_for_all_tasks']
    assert set(route['mandatory_for_code_modification'])=={'codeman-guardian','codeman-tester'}
    assert set(names)=={p.name for p in (ROOT/'skills').glob('codeman-*') if p.is_dir()}
    for entry in modules:
        assert entry['description'] and entry['signals']
        assert (skill/entry['guide']).exists(),entry
    router_size=(skill/'references/module-routing.json').stat().st_size
    full_bytes=sum((skill/m['guide']).stat().st_size for m in modules)
    assert router_size < full_bytes/6, f'Routing file excessive: {router_size} bytes of {full_bytes}'
    print(f'Routing PASS: all {len(modules)} specialties assessed by {router_size} byte index; {full_bytes} bytes of full playbooks loaded only when relevant')

if __name__=='__main__':main()
