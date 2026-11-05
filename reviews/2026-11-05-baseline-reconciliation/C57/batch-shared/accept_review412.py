"""Root acceptance of completed, excluded R688; preserve all existing locks."""
from pathlib import Path
import csv, hashlib, json
W=Path(__file__).resolve().parent
H=W/'review412'; A=W/'accounting'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((H/'SHA256SUMS.json').read_text(encoding='utf-8'))
for path,digest in manifest.items():
    assert sha(Path(path))==digest,path
q=list(csv.DictReader((H/'queue.csv').open(encoding='utf-8-sig')))
r=list(csv.DictReader((H/'RESULTS.csv').open(encoding='utf-8-sig')))
assert len(q)==len(r)==1 and q[0]['tic']==r[0]['tic']=='412639100'
assert q[0]['gaia_dr3_source_id']=='2204160934098817280'
assert sha(H/'queue.csv')==json.loads((H/'queue-seal.json').read_text())['queue_sha256']
m=json.loads((H/'412639100/measurements.json').read_text(encoding='utf-8'))
assert r[0]['physical_verdict']==m['physical_verdict']=='PLAUSIBLE'
assert r[0]['full_review_completion']=='COMPLETE' and not m['counted_eb']
assert all(r[0][k]=='' for k in ('period_days','period_error_days','primary_epoch_btjd','depth_ppt'))
assert m['raw_sap']==json.loads((H/'sap-measurements.json').read_text())
receipt={'review_id':'R688','tic':'412639100','decision':'accepted completed plausible; excluded from physical and claim counts','manifest_files_verified':len(manifest),'manifest_sha256':sha(H/'SHA256SUMS.json'),'results_sha256':sha(H/'RESULTS.csv'),'queue_sha256':sha(H/'queue.csv'),'counts_unchanged':910}
(H/'ROOT-ACCEPTANCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
decision={'review_id':'R688','tic':'412639100','gaia_dr3':'2204160934098817280','physical_tier':'plausible','novelty':'not_claim_eligible','accepted_by':'root explicit decision 2026-11-04','rationale':'Bounded lead/helper review complete. Broad shallow recurrent trough lacks secure eclipse contacts, measured timings, or localized source; alternative periastron variability unresolved. No physical or new-claim membership.','queue_file':str(H/'queue.csv'),'results_file':str(H/'RESULTS.csv'),'evidence':[str(H/x) for x in ('SHA256SUMS.json','ROOT-ACCEPTANCE.json','helper-audit.md','412639100/REPORT.md','412639100/measurements.json')]}
lock=json.loads((A/'input-lock.json').read_text(encoding='utf-8'))
for path,digest in lock.items():assert sha(Path(path))==digest,path
for path in [decision['queue_file'],decision['results_file']]+decision['evidence']:
    assert path not in lock or lock[path]==sha(Path(path))
    lock[path]=sha(Path(path))
(A/'input-lock.json').write_text(json.dumps(lock,indent=2)+'\n',encoding='utf-8')
ds=json.loads((A/'root-decisions.json').read_text(encoding='utf-8'))
assert not any(d['review_id']=='R688' for d in ds['decisions'])
ds['decisions'].append(decision)
(A/'root-decisions.json').write_text(json.dumps(ds,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
