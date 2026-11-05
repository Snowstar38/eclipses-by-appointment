"""Root acceptance after reading lead/helper and deciding sparse/identity evidence.
Plausible novelty vocabulary corrected by repair_cached5_decisions.py.
"""
from pathlib import Path
import csv,json,hashlib
W=Path(__file__).resolve().parent;R=W/'review_cached5';A=W/'accounting';C=W/'remaining_cached/catalogue-recovery-late'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:list(csv.DictReader(p.open(encoding='utf-8-sig')))
expected=['257992903','70561926','380395732','280950412','188908998']
q=read(R/'queue.csv');rs=read(R/'RESULTS.csv')
assert [r['tic'] for r in q]==[r['tic'] for r in rs]==expected
assert [r['physical_verdict'] for r in rs]==['PROBABLE','CONFIRMED','PROBABLE','PLAUSIBLE','PLAUSIBLE']
assert all(r['full_review_completion']=='COMPLETE' for r in rs)
seal=json.loads((R/'queue-seal.json').read_text());assert sha(R/'queue.csv')==seal['sha256'] and sha(R/'SOURCE-SNAPSHOT.json')==seal['snapshot_sha256']
for p,d in seal['source_hashes'].items():assert sha(W/p)==d,p
verified={}
for p,d in json.loads((R/'SHA256SUMS.json').read_text())['files'].items():
 f=R/p;assert sha(f)==d,p;verified[str(f)]=d
verified[str(R/'SHA256SUMS.json')]=sha(R/'SHA256SUMS.json')
for t in json.loads((R/'SOURCE-SNAPSHOT.json').read_text()).values():
 for rec in t['target']['file_receipts']:
  assert sha(Path(rec['path']))==rec['sha256'];verified[rec['path']]=rec['sha256']
h=json.loads((R/'helper-final-audit.json').read_text());assert h['exact_queue'] and h['results_sha256']==sha(R/'RESULTS.csv')
assert [r['tic'] for r in h['rows']]==expected
for r in h['rows']:
 assert all(r['checks'].values()) and sha(R/r['tic']/'REPORT.md')==r['report_sha256']
 assert sha(R/r['tic']/'measurements.json')==r['measurements_sha256']
ds=json.loads((A/'root-decisions.json').read_text());assert not set(expected)&{r['tic'] for r in ds['decisions']}
for i,(qr,rr) in enumerate(zip(q,rs)):
 rid=f'R{708+i}';assert qr['review_id']==rid
 reason=('Known IJspeert exact identity; real repeats accepted probable with capable neighbors unresolved.' if i in (0,2) else 'Confirmed recurrent eclipses; four irregular event intervals constrain clock. Root resolves VSX EA association using 0.30 arcsec position, matching clock and no alternative Gaia source within 2 arcsec; known recovery.' if i==1 else 'Completed bounded review remains plausible; sparse or weak events do not resolve integer aliases. No new-system claim.')
 ds['decisions'].append(dict(review_id=rid,tic=qr['tic'],gaia_dr3=qr['gaia_dr3_source_id'],physical_tier=rr['physical_verdict'].lower(),novelty='known_prior_recovery' if i<3 else 'no_prior_eb_identified',accepted_by='root explicit decision 2026-11-04',rationale=reason+' '+rr['limitations'],queue_file=str(R/'queue.csv'),results_file=str(R/'RESULTS.csv'),catalogue_matrix=str(C/'coverage-matrix.csv'),evidence=[str(R/p) for p in ('SHA256SUMS.json','helper-audit.md','helper-final-audit.json',qr['tic']+'/REPORT.md',qr['tic']+'/measurements.json')]+[str(C/'coverage-matrix.csv')]))
lock=json.loads((A/'input-lock.json').read_text())
for p,d in lock.items():assert sha(Path(p))==d,p
for p,d in verified.items():
 assert p not in lock or lock[p]==d,p
 lock[p]=d
(A/'input-lock.json').write_text(json.dumps(lock,indent=2)+'\n',encoding='utf-8')
(A/'root-decisions.json').write_text(json.dumps(ds,indent=2)+'\n',encoding='utf-8')
receipt=dict(review_ids=[f'R{x}' for x in range(708,713)],known_recoveries=expected[:3],plausible=expected[3:],new_claims=[],verified_review_manifest_files=80,results_sha256=sha(R/'RESULTS.csv'),expected_counts=dict(physical=949,claims=913,confirmed_claims=807,probable_claims=106,pending_novelty_physical=0))
(R/'ROOT-ACCEPTANCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print(json.dumps(receipt))
