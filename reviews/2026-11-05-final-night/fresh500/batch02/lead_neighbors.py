import csv,json,requests,hashlib,io
from pathlib import Path
from astropy.io import fits
from astropy.wcs import WCS
import numpy as np
b=Path(__file__).resolve().parent
for row in csv.DictReader((b/'queue.csv').open()):
 tic=row['tic'];d=b/tic;
 if not (d/'helper-localization.json').exists():continue
 l=json.loads((d/'helper-localization.json').read_text());ra=l['ra'];dec=l['dec'];query=f"SELECT source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.035))"
 try:
  r=requests.post('https://gaia.ari.uni-heidelberg.de/tap/sync',data={'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':query},timeout=30);r.raise_for_status();r.content.decode();(d/'lead-gaia-neighbors.csv').write_bytes(r.content);ns=list(csv.DictReader(io.StringIO(r.text)))
  with fits.open(d/'helper-tesscut.fits') as h:w=WCS(h[2].header)
  for n in ns:
   x,y=w.world_to_pixel_values(float(n['ra']),float(n['dec']));n['pixel_xy']=[float(x),float(y)];n['relative_G_flux']=10**(-.4*(float(n['phot_g_mean_mag'])-float(row['gaia_G']))) if n['phot_g_mean_mag'] else None
  out={'url':r.url,'sha256':hashlib.sha256(r.content).hexdigest(),'neighbors':ns};(d/'lead-neighbors.json').write_text(json.dumps(out,indent=2));print(tic,len(ns),flush=True)
 except Exception as e: print(tic,repr(e),flush=True);(d/'lead-neighbors.json').write_text(json.dumps({'error':repr(e)}))




