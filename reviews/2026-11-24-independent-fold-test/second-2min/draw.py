import csv,hashlib
from pathlib import Path
import numpy as np
from astropy.coordinates import SkyCoord
from astropy import units as u
D=Path(__file__).resolve().parent;P=D.parent;S=P.parent
def rows(f):
 with f.open(encoding='utf-8-sig') as q:return list(csv.DictReader(q))
def save(f,data):
 with (D/f).open('w',encoding='utf8',newline='') as q:
  w=csv.DictWriter(q,data[0],lineterminator='\n');w.writeheader();w.writerows(data)
omit=rows(P/'batch.csv')+rows(P/'ffi/batch.csv')+rows(S/'fable52-ffi-tce-2026-11-24/batch.csv')+[v for v in rows(S/'fable52-2026-11-22/tce-graveyard/candidates-ffi.csv') if v['validation']=='TCE only']+rows(S.parent/'tmp/astra-credit-nov24/accepted-systems.csv')+rows(S/'fable52-changing-2026-11-24/ephem.csv')
ids={r['tic'] for r in omit}; pos=SkyCoord([float(r.get('ra') or r['ra_deg']) for r in omit],[float(r.get('dec') or r['dec_deg']) for r in omit],unit='deg')
r=[]
for v in rows(P/'eligible.csv'):
 if v['stream']!='2min' or v['tic'] in ids:continue
 sep=SkyCoord(float(v['ra_deg']),float(v['dec_deg']),unit='deg').separation(pos).min().arcsec
 if sep<=30:continue
 r.append(dict(**v,min_excluded_sep_arcsec=round(float(sep),2)))
r.sort(key=lambda x:(-int(x['flag']),-int('|' in x['sectors']),-float(x['paired_bin_depth_ppt']),int(x['tic'])))
s=r[:10]
save('selection.csv',s); save('batch.csv',[dict(**{k:x[k] for k in ('tic','stream','sectors','ra_deg','dec_deg')},owner='Astra Sol-Terra') for x in sorted(s,key=lambda x:int(x['tic']))])
print('available',len(r),'selected',[x['tic'] for x in s])
