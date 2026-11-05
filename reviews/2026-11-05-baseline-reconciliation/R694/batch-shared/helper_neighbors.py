import json,math
from pathlib import Path
from astropy.io.votable import parse_single_table
B=Path(__file__).resolve().parent; H=B/'helper-pixels';D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf8'));res=json.loads((H/'results.json').read_text(encoding='utf8'))
for o in res:
 tic=o['tic'];g=D[tic]['target']['gaia']; gt=float(g['phot_g_mean_mag']); r=json.loads((H/tic/'receipt.json').read_text(encoding='utf8')); dep=min(r['event']['depth_ppt'],o['ap5_depth_ppt'])/1000; ns=[]
 for x in parse_single_table(H/tic/'gaia.xml').to_table():
  import numpy as np
  sid=str(x['datalinkID']);
  if sid==g['source_id'] or np.ma.is_masked(x['phot_g_mean_mag']):continue
  G=float(x['phot_g_mean_mag']);fr=10**(-.4*(G-gt));need=dep*(1+fr)/fr
  if need<=1:
   ra=float(x['ra']);dec=float(x['dec']);sep=math.hypot((ra-float(g['ra']))*math.cos(math.radians(float(g['dec']))),dec-float(g['dec']))*3600;ns.append(dict(id=sid,G=G,sep_arcsec=sep,required_fraction=need))
 o['conservative_test_depth_ppt']=dep*1000;o['capable_using_min_qlp_or_ap5']=ns
 print(tic,dep*1000,ns)
(H/'conservative-neighbors.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf8')
