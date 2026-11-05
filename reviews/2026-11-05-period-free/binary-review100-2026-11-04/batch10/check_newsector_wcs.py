"""Check H094 TESScut target placement and aperture signal level."""
import zipfile,io,json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
B=Path(__file__).resolve().parent/'317718737';ra=89.14489068715288;dec=-17.64259204616499
out=[]
for s in (98,107,108,109):
 p=B/f'helper-tesscut-s{s}.zip'
 with zipfile.ZipFile(p) as z:
  with fits.open(io.BytesIO(z.read(z.namelist()[0]))) as h:
   x,y=WCS(h[2].header).world_to_pixel_values(ra,dec);a=h[1].data
   g=np.isfinite(a['TIME'])&(a['QUALITY']==0)
   flux=np.asarray(a['FLUX'][g],float);bg=np.asarray(a['FLUX_BKG'][g],float)
   med=np.nanmedian(flux,axis=0);bmed=np.nanmedian(bg,axis=0)
   net=med-bmed
   rec={'sector':s,'archive_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'wcs_target_x0':float(x),'wcs_target_y0':float(y),'quality0_cadences':int(g.sum()),'median_central_pixel_flux':float(med[2,2]),'median_central_pixel_background':float(bmed[2,2]),'median_3x3_total_flux':float(np.nansum(med[1:4,1:4])),'median_3x3_total_background':float(np.nansum(bmed[1:4,1:4])),'median_3x3_net_flux':float(np.nansum(net[1:4,1:4])),'brightest_net_pixel_yx0':list(map(int,np.unravel_index(np.nanargmax(net),net.shape))),'brightest_net_pixel_flux':float(np.nanmax(net))}
   out.append(rec)
(B/'wcs-placement.json').write_text(json.dumps(out,indent=2)+'\n')
for r in out:print(r)
