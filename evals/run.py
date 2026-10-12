#!/usr/bin/env python3
"""Prepare, score and compare reproducible agent coding evaluations (stdlib only)."""
from __future__ import annotations
import argparse,json,os,shutil,subprocess,sys,time
from datetime import datetime,timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parent
TASKS=ROOT/'tasks'

def taskpath(name):
    path=TASKS/name
    if not (path/'TASK.md').is_file() or not (path/'tests'/'test_solution.py').is_file():
        raise ValueError(f'Unknown task: {name}')
    return path

def prepare(name,output):
    source=taskpath(name)/'workspace'
    if output.exists():raise FileExistsError(f'Output already exists: {output}')
    output.mkdir(parents=True)
    shutil.copytree(source,output/'workspace')
    shutil.copy2(taskpath(name)/'TASK.md',output/'TASK.md')
    print(f'Prepared {name}: {output}')

def score(name,workspace,arm,run_id,timeout):
    # Only run in a disposable evaluation VM/container; candidate code is untrusted.
    workspace=workspace.resolve()
    work=workspace/'workspace'
    if not work.is_dir():raise FileNotFoundError(f'workspace missing: {work}')
    task=taskpath(name)
    env=os.environ.copy();env['PYTHONPATH']=str(work)
    started=time.monotonic()
    cmd=[sys.executable,'-m','unittest','discover','-s',str(task/'tests'),'-p','test_solution.py','-v']
    try:
        res=subprocess.run(cmd,cwd=work,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=timeout)
        status='passed' if res.returncode==0 else 'failed';code=res.returncode
        stdout=res.stdout;stderr=res.stderr
    except subprocess.TimeoutExpired as err:
        status='timeout';code=None
        stdout=(err.stdout or b'').decode('utf8','replace') if isinstance(err.stdout,bytes) else (err.stdout or '')
        stderr=(err.stderr or b'').decode('utf8','replace') if isinstance(err.stderr,bytes) else (err.stderr or '')
    return {'schema_version':1,'task':name,'arm':arm,'run_id':run_id,'status':status,
            'exit_code':code,'elapsed_seconds':round(time.monotonic()-started,3),
            'recorded_at':datetime.now(timezone.utc).isoformat(),'command':cmd,
            'stdout':stdout,'stderr':stderr,'workspace':str(workspace)}

def compare(paths):
    results=[json.loads(p.read_text('utf8')) for p in paths]
    arms={}
    for r in results:
        if r['arm'] not in ('baseline','codemaster'):
            raise ValueError('Expected arm baseline or codemaster')
        arms.setdefault((r['task'],r['arm']),[]).append(r)
    print('TASK | BASELINE | CODEMASTER')
    for task in sorted({r['task'] for r in results}):
        def pct(arm):
            xs=arms.get((task,arm),[])
            if not xs:return 'not run'
            return f"{sum(x['status']=='passed' for x in xs)}/{len(xs)} passed"
        print(f'{task} | {pct("baseline")} | {pct("codemaster")}')
    return results

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='action',required=True)
    sub.add_parser('list')
    p=sub.add_parser('prepare');p.add_argument('--task',required=True);p.add_argument('--output',type=Path,required=True)
    p=sub.add_parser('score');p.add_argument('--task',required=True);p.add_argument('--workspace',type=Path,required=True)
    p.add_argument('--arm',choices=['baseline','codemaster'],required=True);p.add_argument('--run-id',required=True)
    p.add_argument('--timeout',type=int,default=20);p.add_argument('--record',type=Path)
    p=sub.add_parser('compare');p.add_argument('records',type=Path,nargs='+')
    args=parser.parse_args()
    if args.action=='list':
        for item in sorted(TASKS.iterdir()):
            if item.is_dir():print(item.name)
    elif args.action=='prepare':prepare(args.task,args.output)
    elif args.action=='score':
        result=score(args.task,args.workspace,args.arm,args.run_id,args.timeout)
        print(json.dumps(result,indent=2))
        if args.record:
            args.record.parent.mkdir(parents=True,exist_ok=True)
            args.record.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
        return 0 if result['status']=='passed' else 1
    else:compare(args.records)
    return 0
if __name__=='__main__':sys.exit(main())
