import json,requests,hashlib
from pathlib import Path
from astropy.io import fits
B=Path(__file__).parent;R=B.parent
T=json.loads((R/'targets-selected.json').read_text())
for tic,sec in [('325100028',38),('391340302',11),('195206508',55)]:
 u=next((u for s,u in T[tic]['qlp'] if int(s)==sec),None)
 if not u:print(tic,sec,'no archived QLP');continue
 p=R/'shared-qlp'/f'{tic}_s{sec:03d}.fits'
 if not p.exists():
  z=requests.get('http[local path omitted]',params={'uri':u},timeout=120);z.raise_for_status();p.write_bytes(z.content)
 with fits.open(p) as h:print(tic,sec,len(h[1].data),hashlib.sha256(p.read_bytes()).hexdigest())
