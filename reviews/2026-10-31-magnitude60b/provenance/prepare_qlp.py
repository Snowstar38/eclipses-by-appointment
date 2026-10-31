"""Fetch up to three widely separated archived QLP sectors per queued target."""
import csv, json, hashlib, os, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
from astropy.io import fits
W = Path(__file__).resolve().parent
targets = json.loads((W/'targets-selected.json').read_text())
queue = list(csv.DictReader((W/'queue.csv').open()))
dest = W/'shared-qlp'; dest.mkdir(exist_ok=True)
jobs=[]
for r in queue:
    arr=sorted(targets[r['tic']]['qlp'])
    for i in sorted({0,len(arr)//2,len(arr)-1}) if arr else []:
        sec,uri=arr[i]; jobs.append((r['tic'],sec,uri))
def fetch(job):
    tic,sec,uri=job
    p=dest/f'{tic}_s{sec:03d}.fits'
    url='http[local path omitted]'
    result={'tic':tic,'sector':sec,'uri':uri,'file':p.name}
    try:
        if not p.exists():
            for attempt in range(3):
                try:
                    r=requests.get(url,params={'uri':uri},timeout=90);r.raise_for_status()
                    p.write_bytes(r.content)
                    break
                except Exception:
                    if attempt==2: raise
                    time.sleep(2)
        with fits.open(p) as f:
            result['rows']=len(f[1].data)
            result['columns']=f[1].columns.names
        result.update(status='ok',bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
    except Exception as e: result.update(status='error',error=str(e))
    print(tic,sec,result['status'],flush=True)
    return result
with ThreadPoolExecutor(max_workers=3) as pool:
    results=list(pool.map(fetch,jobs))
(dest/'manifest.json').write_text(json.dumps({'selection':'Up to three archived sectors at first/middle/last indices; availability not re-queried by this downloader','results':results},indent=2))
print('DONE',len(results),sum(r['status']=='ok' for r in results),flush=True)
