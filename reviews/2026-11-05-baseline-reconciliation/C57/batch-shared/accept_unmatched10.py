"""Explicit root decisions after independent alias/source/known-identity review."""
from pathlib import Path
import csv,json,hashlib
W=Path(__file__).resolve().parent;R=W/'review_unmatched10';A=W/'accounting';C=W/'unmatched512/catalogue-recovery-selected12'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:list(csv.DictReader(p.open(encoding='utf-8-sig')))
expected=['117930511','25320385','122557124','260797021','330664712','436013770','349527829','449012335','95836684','198358825']
tiers=['PROBABLE','PROBABLE','CONFIRMED','PROBABLE','PROBABLE','PROBABLE','PLAUSIBLE','PROBABLE','PLAUSIBLE','CONFIRMED']
q=read(R/'queue.csv');rs=read(R/'RESULTS.csv');assert [r['tic'] for r in q]==[r['tic'] for r in rs]==expected
assert [r['physical_verdict'] for r in rs]==tiers and all(r['full_review_completion']=='COMPLETE' for r in rs)
seal=json.loads((R/'queue-seal.json').read_text());assert sha(R/'queue.csv')==seal['sha256'] and sha(R/'SOURCE-SNAPSHOT.json')==seal['snapshot_sha256']
for p,d in seal['source_hashes'].items():assert sha(W/p)==d,p
verified={};counts={}
for O in (R,C):
 m=json.loads((O/'SHA256SUMS.json').read_text());m=m.get('files',m)
 for p,d in m.items():
  f=Path(p);f=f if f.is_absolute() else O/f;assert sha(f)==d,str(f);verified[str(f)]=d
 counts[O.name]=len(m);verified[str(O/'SHA256SUMS.json')]=sha(O/'SHA256SUMS.json')
for t in json.loads((R/'SOURCE-SNAPSHOT.json').read_text()).values():
 for rec in t['target']['file_receipts']:
  assert sha(Path(rec['path']))==rec['sha256'];verified[rec['path']]=rec['sha256']
h=json.loads((R/'helper-final-audit.json').read_text());assert h['exact_queue'] and h['results_sha256']==sha(R/'RESULTS.csv')
assert [r['tic'] for r in h['rows']]==expected
for r in h['rows']:
 assert all(r['checks'].values()) and sha(R/r['tic']/'REPORT.md')==r['report_sha256']
 assert sha(R/r['tic']/'measurements.json')==r['measurements_sha256']
for i in (1,6,8):assert all(not rs[i][k] for k in ('period_days','period_error_days','reference_epoch_btjd'))
matrix={r['tic']:r for r in read(C/'coverage-matrix.csv')};assert all(matrix[t]['coverage_complete']=='False' for t in expected)
ds=json.loads((A/'root-decisions.json').read_text());assert not set(expected)&{r['tic'] for r in ds['decisions']}
for i,(qr,rr) in enumerate(zip(q,rs)):
 rid=f'R{713+i}';assert qr['review_id']==rid
 known=i in (0,9);plausible=rr['physical_verdict']=='PLAUSIBLE'
 novelty='known_prior_recovery' if known else 'not_claim_eligible' if plausible else 'pending_novelty'
 reason=('Root accepts strongly supported positional prior VSX EA association, despite discrepant prior clock for117930511; no new-system claim.' if known else 'Root accepts completed physical tier, but unavailable catalogue scopes prevent any new-system claim.' if not plausible else 'Root accepts complete plausible review; sparse integer-cycle ambiguity prevents physical inclusion.')
 if i in (0,5):reason+=' Root required probable because the target-like broad deficit does not exclude the capable overlapping neighbor.'
 evidence=[str(R/p) for p in ('SHA256SUMS.json','LEAD-AUDIT.md','helper-audit.md','helper-final-audit.json',qr['tic']+'/REPORT.md',qr['tic']+'/measurements.json')]+[str(C/p) for p in ('coverage-matrix.csv','selected12-live-vsx-results.json','SHA256SUMS.json')]
 ds['decisions'].append(dict(review_id=rid,tic=qr['tic'],gaia_dr3=qr['gaia_dr3_source_id'],physical_tier=rr['physical_verdict'].lower(),novelty=novelty,accepted_by='root explicit decision 2026-11-04',rationale=reason+' '+rr['limitations'],queue_file=str(R/'queue.csv'),results_file=str(R/'RESULTS.csv'),catalogue_matrix=str(C/'coverage-matrix.csv'),evidence=evidence))
lock=json.loads((A/'input-lock.json').read_text())
for p,d in lock.items():assert sha(Path(p))==d,p
for p,d in verified.items():
 assert p not in lock or lock[p]==d,p
 lock[p]=d
(A/'input-lock.json').write_text(json.dumps(lock,indent=2)+'\n',encoding='utf-8')
(A/'root-decisions.json').write_text(json.dumps(ds,indent=2)+'\n',encoding='utf-8')
receipt=dict(review_ids=[f'R{x}' for x in range(713,723)],new_claims=[],known_recoveries=[expected[i] for i in (0,9)],pending_novelty=[expected[i] for i in (1,2,3,4,5,7)],plausible=[expected[i] for i in (6,8)],manifest_files_verified=counts,results_sha256=sha(R/'RESULTS.csv'),expected_counts=dict(physical=957,claims=913,confirmed_claims=807,probable_claims=106,pending_novelty_physical=6))
(R/'ROOT-ACCEPTANCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print(json.dumps(receipt,indent=2))
