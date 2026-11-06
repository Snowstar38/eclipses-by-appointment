import csv,io,json,requests,hashlib,concurrent.futures
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
B=Path(__file__).resolve().parent;rows=list(csv.DictReader((B/'queue.csv').open()))
def task(row):
 D=B/row['tic'];j=json.loads((D/'helper-localization.json').read_text());ra,dec=j['ra'],j['dec'];q=f"SELECT TOP 1000 source_id,ra,dec,phot_g_mean_mag,DISTANCE(POINT('ICRS',ra,dec),POINT('ICRS',{ra},{dec}))*3600 AS sep FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.0166667))";r=requests.get('https://gea.esac.esa.int/tap-server/tap/sync',params={'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q},timeout=20);r.raise_for_status();(D/'helper-gaia-cone.csv').write_bytes(r.content); stars=list(csv.DictReader(io.StringIO(r.text))); target=next((s for s in stars if s['source_id']==row['gaia_dr3']),None)
 if not target:raise ValueError('target absent')
 with fits.open(D/'helper-tesscut.fits') as f:w=WCS(f[2].header)
 g=float(target['phot_g_mean_mag']); res=[]
 for s in stars:
  if s['source_id']==row['gaia_dr3'] or not s['phot_g_mean_mag']:continue
  x,y=w.world_to_pixel_values(float(s['ra']),float(s['dec']));ratio=10**(-.4*(float(s['phot_g_mean_mag'])-g));required=j['aperture_loss']*(1+ratio)/ratio
  if required<2 or float(s['sep'])<5:res.append(dict(source_id=s['source_id'],sep_arcsec=float(s['sep']),G=float(s['phot_g_mean_mag']),relative_G_flux=ratio,idealized_required_intrinsic_loss=required,wcs_xy=[float(x),float(y)]))
 out=dict(request_url=r.url,response_sha256=hashlib.sha256(r.content).hexdigest(),target_G=g,target_gaia=row['gaia_dr3'],neighbors_sorted=sorted(res,key=lambda s:s['idealized_required_intrinsic_loss']),note='Idealized required intrinsic loss uses Gaia G flux ratio and observed aperture loss assuming target and neighbor fully captured and no other flux. Approximate only: Gaia G differs from TESS band, aperture throughput and additional stars change budget. Missing Gaia sources or unresolved companions not excluded.')
 (D/'helper-gaia-neighbors.json').write_text(json.dumps(out,indent=2));return row['sample_id'],[(s['source_id'],round(s['sep_arcsec'],1),round(s['idealized_required_intrinsic_loss'],2)) for s in out['neighbors_sorted'][:5]]

for row in rows:
 if row['sample_id'] in ('Z001','Z006','Z007','Z008'):
  try: print(task(row),flush=True)
  except Exception as e: print(row['sample_id'],repr(e),flush=True)

