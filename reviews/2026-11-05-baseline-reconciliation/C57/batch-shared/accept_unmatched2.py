"""Root accepts completed bounded physical reviews, with novelty still pending."""
from pathlib import Path
import csv,json,hashlib
W=Path(__file__).resolve().parent;R=W/'review_unmatched2';A=W/'accounting';C=W/'unmatched512/catalogue-recovery-selected12'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:list(csv.DictReader(p.open(encoding='utf-8-sig')))
expected=['241479387','421331604'];q=read(R/'queue.csv');rs=read(R/'RESULTS.csv')
assert [r['tic'] for r in q]==[r['tic'] for r in rs]==expected
assert [r['physical_verdict'] for r in rs]==['PROBABLE','CONFIRMED'] and all(r['full_review_completion']=='COMPLETE' for r in rs)
s=json.loads((R/'queue-seal.json').read_text());assert sha(R/'queue.csv')==s['sha256'] and sha(R/'SOURCE-SNAPSHOT.json')==s['snapshot_sha256']
for p,d in s['source_hashes'].items():assert sha(W/p)==d,p
m=json.loads((R/'SHA256SUMS.json').read_text());m=m.get('files',m);verified={}
for p,d in m.items():
 f=Path(p);f=f if f.is_absolute() else R/f;assert sha(f)==d,str(f);verified[str(f)]=d
verified[str(R/'SHA256SUMS.json')]=sha(R/'SHA256SUMS.json')
for t in json.loads((R/'SOURCE-SNAPSHOT.json').read_text()).values():
 for rec in t['target']['file_receipts']:
  assert sha(Path(rec['path']))==rec['sha256'];verified[rec['path']]=rec['sha256']
h=json.loads((R/'helper-final-audit.json').read_text());assert all(h['checks'].values()) and h['results_sha256']==sha(R/'RESULTS.csv')
assert [r['tic'] for r in h['rows']]==expected
for r in h['rows']:
 assert all(r['checks'].values()) and sha(R/r['tic']/'REPORT.md')==r['report_sha256']
 assert sha(R/r['tic']/'measurements.json')==r['measurement_sha256']
matrix={r['tic']:r for r in read(C/'coverage-matrix.csv')};assert all(matrix[t]['coverage_complete']=='False' for t in expected)
ds=json.loads((A/'root-decisions.json').read_text());assert not set(expected)&{r['tic'] for r in ds['decisions']}
for i,(qr,rr) in enumerate(zip(q,rs)):
 rid=f'R{723+i}';assert qr['review_id']==rid
 reason=('Root accepts recurrent eclipses at probable tier with unresolved8.59arcsec neighbor and disclosed mild Gaia tension.' if i==0 else 'Root accepts confirmed repeated deep eclipses and separate recurrent shallow conjunction; alternate reduction, bounded source census and Gaia orbit support physical interpretation.')
 evidence=[str(R/p) for p in ('SHA256SUMS.json','LEAD-AUDIT.md','helper-audit.md','helper-final-audit.json',qr['tic']+'/REPORT.md',qr['tic']+'/measurements.json')]+[str(C/p) for p in ('coverage-matrix.csv','SHA256SUMS.json')]
 ds['decisions'].append(dict(review_id=rid,tic=qr['tic'],gaia_dr3=qr['gaia_dr3_source_id'],physical_tier=rr['physical_verdict'].lower(),novelty='pending_novelty',accepted_by='root explicit decision 2026-11-04',rationale=reason+' Missing catalogue scopes prevent a new-system claim. '+rr['limitations'],queue_file=str(R/'queue.csv'),results_file=str(R/'RESULTS.csv'),catalogue_matrix=str(C/'coverage-matrix.csv'),evidence=evidence))
lock=json.loads((A/'input-lock.json').read_text())
for p,d in lock.items():assert sha(Path(p))==d,p
for p,d in verified.items():
 assert p not in lock or lock[p]==d,p
 lock[p]=d
(A/'input-lock.json').write_text(json.dumps(lock,indent=2)+'\n',encoding='utf-8')
(A/'root-decisions.json').write_text(json.dumps(ds,indent=2)+'\n',encoding='utf-8')
receipt=dict(review_ids=['R723','R724'],new_claims=[],pending_novelty=expected,manifest_files_verified=len(m),results_sha256=sha(R/'RESULTS.csv'),expected_counts=dict(physical=959,claims=913,confirmed_claims=807,probable_claims=106,pending_novelty_physical=8))
(R/'ROOT-ACCEPTANCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print(json.dumps(receipt,indent=2))
