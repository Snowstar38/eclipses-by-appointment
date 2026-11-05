import json,zipfile,io,hashlib,math
from pathlib import Path
from astropy.io import fits
from astropy.wcs import WCS
B=Path(__file__).resolve().parent;cones=json.loads((B/'lead-neighbors.json').read_text());out={}
for tic in ('280051953','295351347','72497715'):
 p=next((B/tic).glob('helper-tesscut*.zip'));z=zipfile.ZipFile(p);h=fits.open(io.BytesIO(z.read(z.namelist()[0])));w=WCS(h[2].header);stars=[]
 for s in cones[tic]['stars']:
  x,y=w.all_world2pix(float(s['ra_deg']),float(s['dec_deg']),0);x=float(x);y=float(y)
  if 0<=x<=10 and 0<=y<=10:
   stars.append(dict(tic=s['tic'],sep_arcsec=s['separation_arcsec'],tmag=s['tmag'],approx_t_flux_ratio=s.get('approx_t_flux_ratio_to_target'),x=x,y=y))
 out[tic]=dict(cutout_zip=str(p),cutout_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),mast_cone_response_sha256=cones[tic]['response_sha256'],sources=stars)
(B/'lead-neighbor-wcs.json').write_text(json.dumps(out,indent=2)+'\n')
for tic,x in out.items():print(tic,len(x['sources']))
