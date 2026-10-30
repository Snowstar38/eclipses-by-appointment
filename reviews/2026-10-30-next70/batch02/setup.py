from pathlib import Path
import csv,json,shutil,os,hashlib
D=Path('[local working path omitted; see provenance receipts]');B=D/'batch02';R=B/'raw-evidence';R.mkdir(exist_ok=True)
rows=[r for r in csv.DictReader((D/'queue.csv').open()) if r['batch']=='2'];ids=[r['tic'] for r in rows];T=json.loads((D/'targets-selected.json').read_text());(B/'targets-selected.json').write_text(json.dumps({x:T[x] for x in ids},indent=2))
search=[json.loads(l) for l in (Path(os.environ['TEMP'])/'hunt-sb1-scale/search.jsonl').open() if str(json.loads(l)['tic']) in ids];assert len(search)==10;(R/'search-receipts.json').write_text(json.dumps(search,indent=2));manifest=[]
for tic in ids:
 dst=R/tic;dst.mkdir(exist_ok=True)
 for p in (Path(os.environ['TEMP'])/'hunt-sb1-scale').glob(tic+'_s*.fits'):
  dest=dst/('qlp_s'+p.stem.split('_s')[1]+'.fits');shutil.copy2(p,dest);manifest.append(dict(tic=tic,path=str(dest.relative_to(B)),origin=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
 for p in (Path('[local working path omitted; see provenance receipts] 5/made/sb1-scale/diffimg')/tic).glob('*'):
  if p.is_file():shutil.copy2(p,dst/p.name)
for name in ['measure.py','plot_events.py','inventory.py','independent.py']:shutil.copy2(D/'batch01/raw-evidence'/name,R/name)
for name in ['source_review.py','gaia_geometry.py']:
 s=(D/'batch01'/name).read_text().replace("/batch01'","/batch02'").replace("B=D/'batch01'","B=D/'batch02'").replace('Lead personally inspected all ten cached three-panel images. ','')
 (B/name).write_text(s)
(R/'qlp-manifest.json').write_text(json.dumps(manifest,indent=2));print(ids,len(manifest))
