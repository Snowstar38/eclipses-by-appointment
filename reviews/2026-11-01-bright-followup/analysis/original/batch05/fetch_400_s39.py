"""Targeted raw QLP sector-39 check of TIC 40076679's cycle alias."""
import hashlib,json,requests
from pathlib import Path
from astropy.io import fits
B=Path(__file__).parent;tic='40076679';sec=39
uri=next(uri for s,uri in json.loads((B.parent/'targets-selected.json').read_text())[tic]['qlp'] if int(s)==sec)
p=B.parent/'shared-qlp'/f'{tic}_s{sec:03d}.fits'
if not p.exists():
 r=requests.get('http[local path omitted]',params={'uri':uri},timeout=120);r.raise_for_status();p.write_bytes(r.content)
with fits.open(p) as h:
 assert str(h[0].header['TICID'])==tic and int(h[0].header['SECTOR'])==sec
 print(tic,sec,len(h[1].data),hashlib.sha256(p.read_bytes()).hexdigest())
