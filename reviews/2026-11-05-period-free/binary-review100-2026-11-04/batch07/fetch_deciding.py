"""Bounded MAST cutout fetch for potentially deciding uncached sectors."""
import csv
import hashlib
import io
import json
import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

B = Path(__file__).resolve().parent
Q = {r['tic']: r for r in csv.DictReader((B / 'queue.csv').open())}
REQUESTS = [('368903210', 59), ('321154190', 66)]


def fetch(item):
    tic, sector = item
    q = Q[tic]
    dest = B / tic
    rec = {'tic': tic, 'sector': sector, 'purpose': 'uncached-sector check for possible real-event alternative'}
    try:
        response = requests.get(
            'https://mast.stsci.edu/tesscut/api/v0.1/astrocut',
            params={'ra': q['ra_deg'], 'dec': q['dec_deg'], 'y': 5, 'x': 5,
                    'units': 'px', 'sector': sector}, timeout=90)
        raw = response.content
        (dest / f's{sector}-tesscut.raw').write_bytes(raw)
        rec.update(url=response.url, http_status=response.status_code,
                   response_sha256=hashlib.sha256(raw).hexdigest())
        response.raise_for_status()
        archive = zipfile.ZipFile(io.BytesIO(raw))
        data = archive.read(archive.namelist()[0])
        (dest / f's{sector}-tesscut.fits').write_bytes(data)
        rec['fits_sha256'] = hashlib.sha256(data).hexdigest()
    except Exception as exc:
        rec['error'] = repr(exc)
    (dest / f's{sector}-tesscut-receipt.json').write_text(json.dumps(rec, indent=2) + '\n')
    print(tic, sector, rec.get('http_status'), rec.get('error'), flush=True)


with ThreadPoolExecutor(max_workers=2) as pool:
    list(pool.map(fetch, REQUESTS))
