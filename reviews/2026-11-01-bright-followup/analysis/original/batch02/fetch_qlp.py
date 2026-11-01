"""Fetch representative first/middle/last archived QLP sectors for batch01."""
import csv, json, hashlib, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
from astropy.io import fits
B=Path(__file__).resolve().parent
ROOT=B.parent
targets=json.loads((ROOT/'targets-selected.json').read_text())
queue=list(csv.DictReader((B/'queue.csv').open()))
dest=ROOT/'shared-qlp';dest.mkdir(exist_ok=True)
jobs=[]
for r in queue:
    arr=sorted(targets[r['tic']]['qlp'])
    pixel_sector={'37531624':61,'39768877':38,'288605754':65}.get(r['tic'])
    picks={0,len(arr)//2,len(arr)-1} if arr else set()
    picks.update(i for i,(sec,_) in enumerate(arr) if sec==pixel_sector)
    for i in sorted(picks):
        sec,uri=arr[i];jobs.append((r['tic'],sec,uri))
def fetch(job):
    tic,sec,uri=job;p=dest/f'{tic}_s{sec:03d}.fits';rec={'tic':tic,'sector':sec,'uri':uri,'file':str(p)}
    try:
        if not p.exists():
            url='http[local path omitted]'
            for attempt in range(3):
                try:
                    response=requests.get(url,params={'uri':uri},timeout=120)
                    response.raise_for_status();p.write_bytes(response.content);break
                except Exception:
                    if attempt==2:raise
                    time.sleep(2)
        with fits.open(p) as f:
            rec['rows']=len(f[1].data);rec['columns']=f[1].columns.names
        rec.update(status='ok',bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
    except Exception as e:rec.update(status='error',error=str(e))
    print(tic,sec,rec['status'],flush=True)
    return rec
with ThreadPoolExecutor(max_workers=4) as pool:recs=list(pool.map(fetch,jobs))
(B/'download-receipts.json').write_text(json.dumps(recs,indent=2))
print('DONE',len(recs),sum(r['status']=='ok' for r in recs),flush=True)
