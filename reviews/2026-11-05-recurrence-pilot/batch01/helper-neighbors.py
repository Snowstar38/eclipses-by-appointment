from pathlib import Path
from astropy.io import fits
from astropy.wcs import WCS
import csv,json,math
B=Path(__file__).resolve().parent
out=[]
for tic,sec,g,depth in [('147413927',37,10.435455,.0025),('265066551',17,11.26689,.3)]:
 with fits.open(B/tic/f'helper-tesscut-s{sec:03}.fits') as h:w=WCS(h[2].header)
 rows=list(csv.DictReader((B/tic/'helper-gaia-cone.csv').open()));cap=[]
 for r in rows:
  if not r['phot_g_mean_mag'] or float(r['sep_arcsec'])<1:continue
  ratio=10**(-.4*(float(r['phot_g_mean_mag'])-g))
  if ratio<depth:continue
  x,y=w.world_to_pixel_values(float(r['ra']),float(r['dec'])); cap.append(dict(source_id=r['source_id'],sep_arcsec=float(r['sep_arcsec']),G=float(r['phot_g_mean_mag']),approx_flux_ratio=ratio,x=float(x),y=float(y)))
 out.append(dict(tic=tic,sector=sec,threshold_flux_ratio=depth,assumption='100% intrinsic loss at full throughput; approximate Gaia G, actual aperture throughput and TESS band differ',candidates=cap))
(B/'helper-capable-neighbors.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
