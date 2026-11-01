"""Fetch historical cutout sectors for targeted timing contradictions."""
import hashlib, json, requests
from pathlib import Path
from astropy.io import fits
B=Path(__file__).parent; ROOT=B.parent
T=json.loads((ROOT/'targets-selected.json').read_text())
jobs=[('30770290',39),('306980055',39),('457272901',65),('403410574',39)]
out=[]
for tic,sec in jobs:
    uri=next(u for s,u in T[tic]['qlp'] if s==sec)
    p=ROOT/'shared-qlp'/f'{tic}_s{sec:03}.fits'
    if not p.exists():
        r=requests.get('http[local path omitted]',params={'uri':uri},timeout=120)
        r.raise_for_status();p.write_bytes(r.content)
    with fits.open(p) as f:
        assert len(f[1].data)>0
        cols=f[1].columns.names
    rec=dict(tic=tic,sector=sec,uri=uri,file=str(p),columns=cols,status='ok',bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
    out.append(rec);print(tic,sec,rec['bytes'],flush=True)
(B/'targeted-download-receipts.json').write_text(json.dumps(out,indent=2)+'\n')
