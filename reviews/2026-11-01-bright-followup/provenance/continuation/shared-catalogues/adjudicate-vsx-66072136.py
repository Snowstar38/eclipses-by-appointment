import csv
import hashlib
import io
import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

p = Path(__file__).parent
t = json.loads((p / 'targets-selected.json').read_text())['66072136']
ra, dec = t['ra'], t['dec']
query = ("SELECT source_id,ra,dec,phot_g_mean_mag,pmra,pmdec,"
         "DISTANCE(POINT('ICRS',ra,dec),POINT('ICRS',"
         f"{ra},{dec})) AS distance_deg FROM gaiadr3.gaia_source "
         "WHERE 1=CONTAINS(POINT('ICRS',ra,dec),"
         f"CIRCLE('ICRS',{ra},{dec},0.001388888889)) ORDER BY distance_deg")
url = 'http[local path omitted]'
receipt = {'query': query, 'url': url, 'queried_at_utc': datetime.now(timezone.utc).isoformat()}
try:
    data = urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':query}).encode()
    raw = urllib.request.urlopen(url,data,timeout=30).read()
    rows = list(csv.DictReader(io.StringIO(raw.decode())))
    assert rows and 'source_id' in rows[0]
    (p/'gaia-neighbours-66072136.csv').write_bytes(raw)
    receipt.update(status='success',rows=rows,sha256=hashlib.sha256(raw).hexdigest())
except Exception as exc:
    receipt.update(status='unavailable',error=repr(exc))
(p/'gaia-neighbours-66072136-receipt.json').write_text(json.dumps(receipt,indent=2))
print(json.dumps(receipt,indent=2))
