import json
from pathlib import Path
import numpy as np
from astropy.io.votable import parse_single_table
from astropy.coordinates import SkyCoord
from astropy import units as u
B=Path(__file__).resolve().parent;H=B/'helper-pixels';D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf8'));R=json.loads((H/'aperture-neighbors.json').read_text(encoding='utf8'));t=parse_single_table(H/'gaia-all.raw').to_table();C=SkyCoord(np.array(t['ra'],float)*u.deg,np.array(t['dec'],float)*u.deg)
for o in R:
 g=D[o['tic']]['target']['gaia'];p=SkyCoord(float(g['ra'])*u.deg,float(g['dec'])*u.deg);sep=C.separation(p).arcsec;dep=min([o['conservative_depth_ppt']]+[x for x in o['pixel_apertures_ppt'].values() if x>0])/1000;ns=[]
 for i in np.where(sep<=60)[0]:
  x=t[i];sid=str(x['datalinkID']);
  if sid==g['source_id'] or np.ma.is_masked(x['phot_g_mean_mag']):continue
  ratio=10**(-.4*(float(x['phot_g_mean_mag'])-float(g['phot_g_mean_mag'])));need=dep*(1+ratio)/ratio
  if need<=1:ns.append({'source_id':sid,'sep_arcsec':float(sep[i]),'separation_tess_pixels_approx':float(sep[i])/21,'G':float(x['phot_g_mean_mag']),'flux_ratio_G':ratio,'intrinsic_eclipse_fraction':need})
 o['minimum_all_apertures_ppt']=dep*1000;o['capable_at_minimum_all_apertures']=ns;print(o['tic'],len(ns))
(H/'final-neighbors.json').write_text(json.dumps(R,indent=2)+'\n',encoding='utf8')
