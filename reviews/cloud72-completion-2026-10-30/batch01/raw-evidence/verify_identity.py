from pathlib import Path
from astropy.io import fits
import json,hashlib
r=Path('.'); out=[]
for f in r.glob('*/qlp*.fits'):
 with fits.open(f) as h:
  H=h[0].header; tic=f.parent.name; sec=int(f.stem[-3:]);out.append(dict(path=str(f),sha256=hashlib.sha256(f.read_bytes()).hexdigest(),tic_expected=tic,sector_expected=sec,TICID=H.get('TICID'),OBJECT=H.get('OBJECT'),SECTOR=H.get('SECTOR'),tic_matches=str(H.get('TICID','')).strip()==tic,sector_matches=H.get('SECTOR')==sec))
json.dump(out,open('identity-checks.json','w'),indent=2)
print([(x['path'],x['TICID'],x['OBJECT'],x['SECTOR']) for x in out if not x['tic_matches'] or not x['sector_matches']])
