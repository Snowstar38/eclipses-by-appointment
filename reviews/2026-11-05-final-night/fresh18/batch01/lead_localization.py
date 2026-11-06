import json,csv,numpy as np
from pathlib import Path
from astropy.io import fits
from astropy.wcs import WCS
b=Path('[workspace]/Astra/made/final-night-2026-11-05/fresh18/batch01');pop=json.loads((b.parent.parent/'fresh-band-next400/population.json').read_text())['targets'];rr=json.loads((b/'lead-pixels-results.json').read_text());out=[]
for r in rr:
 tic=r['tic'];p=pop[tic];path=b/tic/f"helper-cut-s{r['sector']}.fits"
 with fits.open(path) as h:w=WCS(h[2].header)
 diff=np.array(r['difference']);border=np.zeros(diff.shape,bool);border[[0,-1],:]=True;border[:,[0,-1]]=True;bg=float(np.median(diff[border]));dif=diff-bg;xy=np.array(r['target_xy']);yy,xx=np.indices(diff.shape);region=(abs(xx-xy[0])<1.8)&(abs(yy-xy[1])<1.8);weights=np.where(region,np.maximum(dif,0),0);cen=[float((weights*xx).sum()/weights.sum()),float((weights*yy).sum()/weights.sum())];nb=[]
 for n in csv.DictReader((b/tic/'gaia-neighbors.csv').open()):
  if n['source_id']==p['gaia']['source_id'] or not n['phot_g_mean_mag']:continue
  px=w.all_world2pix([[float(n['ra']),float(n['dec'])]],0)[0];sep=3600*np.hypot((float(n['ra'])-p['ra'])*np.cos(np.deg2rad(p['dec'])),float(n['dec'])-p['dec']);rel=10**(-.4*(float(n['phot_g_mean_mag'])-float(p['gaia']['phot_g_mean_mag'])))
  if sep<90:nb.append(dict(source_id=n['source_id'],separation_arcsec=float(sep),G=float(n['phot_g_mean_mag']),G_flux_relative=rel,xy=px.tolist(),centroid_distance_px=float(np.linalg.norm(px-cen))))
 out.append(dict(tic=tic,sector=r['sector'],background_difference=bg,difference_centroid_xy=cen,target_xy=xy.tolist(),target_offset_px=float(np.linalg.norm(xy-cen)),neighbors=sorted(nb,key=lambda n:n['separation_arcsec']),note='Median outer-border offset removed from difference frame, positive weights within1.8pixel target region. Descriptive centroid, not calibrated PSF fit. G flux ratios approximate dilution, not TESS-band exact exclusion.'))
(b/'lead-source-localization.json').write_text(json.dumps(out,indent=2));print([(r['tic'],r['target_offset_px'],r['background_difference']) for r in out])
