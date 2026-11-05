"""Lossless pointers plus compact scores for all attempted science targets."""
from pathlib import Path
import csv,json,hashlib
W=Path(__file__).resolve().parent
read=lambda p:list(csv.DictReader(p.open(encoding='utf-8-sig')))
ledger={r['tic']:r for r in read(W/'accounting/accepted-proposal-ledger.csv')}
rows=[];sources={}
for cohort in ('pilot48','next256','remaining_cached','resolved125','unmatched512'):
 S=W/cohort;pilot=json.loads((S/'pilot.json').read_text())['targets'];tp=S/'triage/triage.csv'
 tri={r['tic']:r for r in read(tp)} if tp.exists() else {}
 for p in (S/'pilot.json',S/'screening.jsonl',S/'triage/REPORT.md',tp):
  if p.exists():sources[str(p.relative_to(W))]=hashlib.sha256(p.read_bytes()).hexdigest()
 for line_no,line in enumerate((S/'screening.jsonl').read_text().splitlines(),1):
  r=json.loads(line)
  if r['control']:continue
  tic=r['tic'];t=pilot[tic];tr=tri.get(tic,{});lr=ledger.get(tic,{})
  disposition=tr.get('physical_disposition') or tr.get('triage_disposition') or tr.get('disposition') or ''
  if cohort=='pilot48' and r.get('flag'):disposition='known_recovery' if tic in ('367017335','456163318') else 'full_review_proposed'
  row=dict(cohort=cohort,tic=tic,gaia_dr3=t['gaia']['source_id'],screen_status=r['status'],screen_flag=bool(r.get('flag')),screen_line=line_no,screen_file=str((S/'screening.jsonl').relative_to(W)),source_receipts=str((S/'pilot.json').relative_to(W)),triage_disposition=disposition,triage_report=str((S/'triage/REPORT.md').relative_to(W)) if r.get('flag') else '',review_id=lr.get('review_id',''),physical_tier=lr.get('physical_tier',''),novelty=lr.get('novelty',''),claim_member=lr.get('claim_member',''),review_report=lr.get('source_report',''))
  for branch in ('P','P2'):
   for key in ('P','snr','depth','dur','t0','z','flag'):row[branch+'_'+key]=r.get(branch,{}).get(key,'')
  for key in ('sig_ppm','n','base','null_med','null_mad','null_max','null_count'):row[key]=r.get(key,'')
  rows.append(row)
assert len(rows)==1674 and len({r['tic'] for r in rows})==1674
assert sum(r['screen_flag'] for r in rows)==169
missing=[r['tic'] for r in rows if r['screen_flag'] and not r['triage_disposition']]
assert not missing,missing
p=W/'REVISIT-REGISTER.csv'
with p.open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
sources['accounting/accepted-proposal-ledger.csv']=hashlib.sha256((W/'accounting/accepted-proposal-ledger.csv').read_bytes()).hexdigest()
(W/'REVISIT-REGISTER.json').write_text(json.dumps(dict(rows=len(rows),flags=169,no_data=sum(r['screen_status']=='no_usable_data' for r in rows),source_hashes=sources,register_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),interpretation='All attempted science retained, including nonflags and no data. Screening periods/epochs are predictions, not measured timings. z is a within-star null score, not Gaussian significance. Blank physical review fields mean no root-accepted full review. Full null periods, grid parameters and per-sector flux columns remain in linked JSONL rows. Not an occurrence-rate denominator.'),indent=2)+'\n',encoding='utf-8')
print('Verified 1674 unique science rows,169 flags, all flagged triage dispositions linked.')
