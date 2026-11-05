import json,math
from pathlib import Path
import numpy as np
from astropy.io.votable import parse_single_table
from astropy.coordinates import SkyCoord
from astropy import units as u
B=Path(__file__).resolve().parent;H=B/'helper-pixels';D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf8'));R=json.loads((H/'results.json').read_text(encoding='utf8'));t=__import__('astropy.table',fromlist=['Table']).Table.read(H/'gaia-all.raw',format='ascii.csv');C=SkyCoord(np.array(t['ra'],float)*u.deg,np.array(t['dec'],float)*u.deg)
for o in R:
 g=D[o['tic']]['target']['gaia'];p=SkyCoord(float(g['ra'])*u.deg,float(g['dec'])*u.deg);sep=C.separation(p).arcsec;v=[o['test_depth_ppt']]+[x for x in o['qlp_alternative_aperture_ppt'].values() if x is not None and x>0];
 if o.get('cutout',{}).get('ap5_depth_ppt',0)>0:v.append(o['cutout']['ap5_depth_ppt'])
 dep=min(v)/1000;ns=[]
 for i in np.where(sep<=60)[0]:
  x=t[i];sid=str(x['source_id']);
  if sid==g['source_id'] or np.ma.is_masked(x['phot_g_mean_mag']):continue
  ratio=10**(-.4*(float(x['phot_g_mean_mag'])-float(g['phot_g_mean_mag'])));need=dep*(1+ratio)/ratio
  if need<=1:ns.append({'source_id':sid,'sep_arcsec':float(sep[i]),'G':float(x['phot_g_mean_mag']),'flux_ratio_G':ratio,'intrinsic_eclipse_fraction':need})
 o['conservative_depth_ppt']=dep*1000;o['capable_at_conservative_depth']=ns;print(o['tic'],len(ns))
(H/'conservative-neighbors.json').write_text(json.dumps(R,indent=2,allow_nan=False)+'\n',encoding='utf8')

