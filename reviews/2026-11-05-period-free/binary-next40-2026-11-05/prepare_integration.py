"""Stage exact retrospective catalogue-recovery scope; no old evidence mutations."""
from pathlib import Path
import csv,json,hashlib
W=Path(__file__).resolve().parent;O=W/'integration';O.mkdir(exist_ok=True)
read=lambda p:list(csv.DictReader(p.open(encoding='utf8')))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
campaigns=['binary-review100-2026-11-04','binary-priority100-2026-11-05','binary-next10-2026-11-05']
rows=[];locks={};counts={}
for name in campaigns:
 d=W.parent/name;source=d/'accepted-results.csv';q=d/'queue.csv';rs=read(source);qq={r['tic']:r for r in read(q)}
 locks[str(source)]=sha(source);locks[str(q)]=sha(q)
 subset=[r for r in rs if r['physical_verdict'] in ['CONFIRMED','PROBABLE'] and r['novelty_status']=='UNKNOWN']
 counts[name]={'reviewed':len(rs),'C_or_P':sum(r['physical_verdict'] in ['CONFIRMED','PROBABLE'] for r in rs),'unknown_C_or_P':len(subset)}
 for r in subset:
  x=qq[r['tic']]
  rows.append({k:x[k] for k in ['tic','gaia_dr3','ra_deg','dec_deg']}|{'sample_id':r['sample_id'],'source_campaign':name,'physical_verdict':r['physical_verdict'],'source_report':r['report']})
assert len(rows)==len({r['tic'] for r in rows})==41
with (O/'retrospective-queue.csv').open('w',encoding='utf8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
out={'scope':'41 physically confirmed/probable but noveltyUNKNOWN rows from three accepted campaigns. Catalogue recovery only; physical decisions remain frozen. Baseline eight pending novelty not included here.','campaigns':counts,'source_sha256':locks,'queue_sha256':sha(O/'retrospective-queue.csv'),'rows':len(rows)}
(O/'retrospective-queue-seal.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,indent=2))
