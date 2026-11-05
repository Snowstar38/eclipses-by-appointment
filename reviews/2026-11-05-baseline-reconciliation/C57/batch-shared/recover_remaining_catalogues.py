"""Append-only recovery after a successful positive-control probe; cap new outage."""
from pathlib import Path
import concurrent.futures,csv,hashlib,importlib.util,json,os,shutil
W=Path(__file__).resolve().parent;S=W/'remaining_cached/shared-catalogues';B=W/'remaining_cached/catalogue-recovery-late'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
probe=json.loads((W/'catalogue-archives/harvard-late-control-receipt.json').read_text())
assert probe['status']=='control_returned_requires_parser_audit'
assert not B.exists();shutil.copytree(S,B,ignore=shutil.ignore_patterns('__pycache__'))
original={str(p.relative_to(S)):sha(p) for p in S.rglob('*') if p.is_file() and '__pycache__' not in str(p)}
(B/'original-manifest.json').write_text(json.dumps(original,indent=2)+'\n',encoding='utf-8')
shutil.copytree(S/'receipts',B/'pre-recovery-receipts')
spec=importlib.util.spec_from_file_location('recovery_catalogues',B/'run_catalogues.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
lock=json.loads((B/'queue-lock.json').read_text());c.QUEUE_HASH=lock['sha256'];assert sha(Path(lock['queue']))==c.QUEUE_HASH
priority=[r['tic'] for name in ('review_cached10','review_cached5') for r in csv.DictReader((W/name/'queue.csv').open())]
missing=[json.loads(p.read_text()) for p in (B/'receipts').glob('*.json') if json.loads(p.read_text()).get('status')=='unavailable']
missing.sort(key=lambda r:(priority.index(r['key'].split('-')[0]) if r['key'].split('-')[0] in priority else 999,r['key']))
assert len(missing)==450
def retry(old):
    rec,raw=c.cached_or_query(old['key'],old['url'],old.get('body'))
    return dict(key=old['key'],status=rec['status'])
out=[];todo=iter(missing);failures=0;stopped=False
with concurrent.futures.ThreadPoolExecutor(3) as ex:
    pending={ex.submit(retry,next(todo)) for _ in range(3)}
    while pending:
        done,pending=concurrent.futures.wait(pending,return_when=concurrent.futures.FIRST_COMPLETED)
        for future in done:
            result=future.result();out.append(result)
            failures=failures+1 if result['status']!='success' else 0
            if failures>=3:stopped=True
            if not stopped:
                item=next(todo,None)
                if item is not None:pending.add(ex.submit(retry,item))
        if len(out)%30==0:print('completed',len(out),'success',sum(r['status']=='success' for r in out),flush=True)
(B/'recovery-log.json').write_text(json.dumps(dict(max_concurrent_requests=3,priority_queue=priority,stopped_on_outage=stopped,results=out),indent=2)+'\n',encoding='utf-8')
os.environ['ASTRA_REUSE_FAILED_RECEIPTS']='1'
c.network(lock['targets'],json.loads((B/'heartbeat-overlaps.json').read_text()),json.loads((B/'chopard-overlaps.json').read_text()),json.loads((B/'tarrants-mendes-overlaps.json').read_text()))
assert all(sha(S/p)==digest for p,digest in original.items())
rows=list(csv.DictReader((B/'coverage-matrix.csv').open(encoding='utf-8-sig')))
assert len(rows)==75 and {r['tic'] for r in rows}=={r['tic'] for r in lock['targets']}
for p in (B/'receipts').glob('*.json'):
    rec=json.loads(p.read_text())
    if rec['status']=='success':assert sha(B/rec['file'])==rec['sha256']
summary=dict(attempted=len(out),recovered=sum(r['status']=='success' for r in out),complete_targets=sum(r['coverage_complete']=='True' for r in rows),known_prior_tics=[r['tic'] for r in rows if r['scoped_prior_eb_status']=='known prior EB in queried scope'],original_evidence_unchanged=True)
(B/'root-recovery-audit.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
# Replace the copied historical manifest with a new manifest; original stays in S.
files={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file() and '__pycache__' not in str(p) and p.name!='SHA256SUMS.json'}
(B/'SHA256SUMS.json').write_text(json.dumps(files,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,indent=2))
