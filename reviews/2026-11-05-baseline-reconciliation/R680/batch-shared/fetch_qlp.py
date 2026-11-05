"""Fetch bounded representative QLP SAP light curves from frozen selected metadata."""
import csv, hashlib, json, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import requests
from astropy.io import fits

B = Path(__file__).resolve().parent
R = B.parent
targets = json.loads((R / 'targets-selected.json').read_text())
queue = list(csv.DictReader((B / 'queue.csv').open()))
dest = R / 'shared-qlp'
dest.mkdir(exist_ok=True)
jobs = []
for row in queue:
    tic = row['tic']
    arr = sorted(targets[tic]['qlp'])
    picks = range(len(arr)) if tic == '187202091' else sorted({0, len(arr)//2, len(arr)-1})
    jobs.extend((tic, *arr[i]) for i in picks)

def fetch(job):
    tic, sec, uri = job
    p = dest / f'{tic}_s{sec:03d}.fits'
    rec = dict(tic=tic, sector=sec, uri=uri, file=str(p))
    try:
        if not p.exists():
            for attempt in range(3):
                try:
                    response = requests.get('https://mast.stsci.edu/api/v0.1/Download/file', params={'uri': uri}, timeout=120)
                    response.raise_for_status()
                    p.write_bytes(response.content)
                    break
                except Exception:
                    if attempt == 2: raise
                    time.sleep(2)
        with fits.open(p) as h:
            hdr = h[0].header
            rec['fits_ticid'] = str(hdr.get('TICID', hdr.get('TIC', '')))
            rec['fits_sector'] = hdr.get('SECTOR')
            rec['rows'] = len(h[1].data)
            rec['columns'] = h[1].columns.names
        if rec['fits_ticid'] != tic or int(rec['fits_sector']) != sec:
            raise ValueError(f"FITS identity mismatch: {rec['fits_ticid']} sector {rec['fits_sector']}")
        if 'SAP_FLUX' not in rec['columns']:
            raise ValueError('SAP_FLUX missing')
        rec.update(status='ok', bytes=p.stat().st_size, sha256=hashlib.sha256(p.read_bytes()).hexdigest())
    except Exception as exc:
        rec.update(status='error', error=str(exc))
    print(tic, sec, rec['status'], flush=True)
    return rec

with ThreadPoolExecutor(max_workers=4) as pool:
    receipts = list(pool.map(fetch, jobs))
(B / 'download-receipts.json').write_text(json.dumps(receipts, indent=2))
print('DONE', len(receipts), sum(r['status']=='ok' for r in receipts), flush=True)
