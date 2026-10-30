from pathlib import Path
import csv,json,shutil,os,hashlib
D=Path('[local working path omitted]');B=D/'batch06';R=B/'raw-evidence';R.mkdir(exist_ok=True)
rows=[r for r in csv.DictReader((D/'queue.csv').open()) if r['batch']=='batch06'];ids=[r['tic'] for r in rows];T=json.loads((D/'targets-selected.json').read_text());(B/'targets-selected.json').write_text(json.dumps({x:T[x] for x in ids},indent=2))
cache=Path(os.environ['TEMP'])/'hunt-sb1-scale';search=[json.loads(l) for l in (cache/'search.jsonl').open() if str(json.loads(l)['tic']) in ids];assert len(search)==5;(R/'search-receipts.json').write_text(json.dumps(search,indent=2));manifest=[]
for tic in ids:
 dst=R/tic;dst.mkdir(exist_ok=True);files=sorted(cache.glob(tic+'_s*.fits'));chosen=files if len(files)<=3 else [files[0],files[len(files)//2],files[-1]]
 for p in chosen:
  dest=dst/('qlp_s'+p.stem.split('_s')[1]+'.fits');shutil.copy2(p,dest);manifest.append(dict(tic=tic,path=str(dest.relative_to(B)),origin=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
for name in ['measure.py','plot_events.py','inventory.py','independent.py','tesscut_fetch.py','pixel_independent.py','plot_pixels.py','verify_identity.py']:
 shutil.copy2(D/'batch01/raw-evidence'/name,R/name)
(R/'cache-manifest.json').write_text(json.dumps(manifest,indent=2));print(ids,len(manifest))



