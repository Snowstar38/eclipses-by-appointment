"""Targeted sector-62 check for T097, absent from cached QLP set."""
import requests,io,zipfile,hashlib,json
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;p=B/'29510249';url='https://mast.stsci.edu/tesscut/api/v0.1/astrocut'
r=requests.get(url,params=dict(ra=133.1574694589157,dec=-44.566114197668405,x=9,y=9,units='px',sector=62),timeout=150);r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));name=z.namelist()[0];dat=z.read(name);f=p/'lead-s62-tesscut.fits';f.write_bytes(dat)
with fits.open(f,memmap=False) as h:
 d=h[1].data;t=np.array(d['TIME'],float);q=np.array(d['QUALITY'],int);flux=np.array(d['FLUX'],float);w=WCS(h[2].header);x,y=w.all_world2pix(133.1574694589157,-44.566114197668405,0)
x,y=float(np.asarray(x).item()),float(np.asarray(y).item());ix,iy=round(x),round(y);med=np.nanmedian(flux[q==0],axis=0)
if not np.isfinite(med[iy,ix]) or med[iy,ix]<=0:
 out=dict(request_url=r.url,zip_sha256=hashlib.sha256(r.content).hexdigest(),member=name,fits_sha256=hashlib.sha256(dat).hexdigest(),target_xy=[x,y],target_pixel_median=float(med[iy,ix]),quality0_n=int(sum(q==0)),time_range_btjd=[float(np.nanmin(t[q==0])),float(np.nanmax(t[q==0]))],status='UNUSABLE_TARGET_PIXEL',note='Target WCS pixel has nonpositive median flux in the sector-62 cutout. No valid source aperture or sensitive alias null can be derived from this footprint.')
 (p/'lead-s62-audit.json').write_text(json.dumps(out,indent=2)+'\n');print(out);raise SystemExit
yy,xx=np.indices(med.shape);sky=(np.hypot(xx-x,yy-y)>3)&(med>0)&np.isfinite(med);bg=np.nanmedian(np.where(flux[:,sky]>0,flux[:,sky],np.nan),axis=1);ap=flux[:,iy-1:iy+2,ix-1:ix+2].sum(axis=(1,2))-9*bg;good=(q==0)&np.isfinite(t)&np.isfinite(ap)&(ap>0)
cad=float(np.median(np.diff(t[good])));spec=[]
for n in (11,12,13,24,36):
 P=(2275.4556-1559.4177)/n;checks=[]
 for k in range(-100,100):
  c=1559.4177+k*P
  if c<t[good].min()+3 or c>t[good].max()-3:continue
  dur=1.5;core=good&(abs(t-c)<dur/2);left=good&(t>c-2*dur)&(t<c-dur);right=good&(t>c+dur)&(t<c+2*dur)
  def cover(mask):
   v=t[mask];return dict(n=int(len(v)),fraction=float(min(1,len(v)*cad/dur)),max_gap_days=float(np.max(np.diff(v))) if len(v)>1 else None)
  cc,lc,rc=cover(core),cover(left),cover(right);sensitive=all(z['fraction']>.75 and z['max_gap_days'] is not None and z['max_gap_days']<dur/4 for z in (cc,lc,rc))
  obs=float(1-np.median(ap[core])/((np.median(ap[left])+np.median(ap[right]))/2)) if sensitive else None
  checks.append(dict(cycle=k,center_btjd=c,core=cc,left=lc,right=rc,sensitive=sensitive,observed_depth=obs))
 spec.append(dict(cycles_between=n,period_days=P,checks=checks))
fig,axs=plt.subplots(len(spec),1,figsize=(9,2.3*len(spec)))
for ax,z in zip(axs,spec):
 ax.plot(t[good],ap[good]/np.median(ap[good]),'.',ms=1);ax.set_title(f's62 n={z["cycles_between"]} P={z["period_days"]:.4f}, predicted={[(round(v["center_btjd"],2),v["sensitive"]) for v in z["checks"]]}');
 for a in z['checks']:ax.axvspan(a['center_btjd']-.75,a['center_btjd']+.75,color='salmon',alpha=.2)
 ax.set_ylabel('ap / median')
axs[-1].set_xlabel('BTJD');fig.tight_layout();fig.savefig(p/'lead-s62-alias.png',dpi=125);plt.close(fig)
out=dict(request_url=r.url,zip_sha256=hashlib.sha256(r.content).hexdigest(),member=name,fits_sha256=hashlib.sha256(dat).hexdigest(),target_xy=[float(x),float(y)],target_pixel_median=float(med[iy,ix]),valid_sky_pixels=int(sky.sum()),quality0_good_n=int(good.sum()),time_range_btjd=[float(t[good].min()),float(t[good].max())],cadence_days=cad,alias_trials=spec,note='Sector 62 was absent from the cached QLP target files but present in current Tesscut footprint. Background-corrected target-centered 3x3, same TESS photons as other TESS reductions. Numeric nulls require actual full core and baseline cadence; plotted for inspection.')
(p/'lead-s62-audit.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_range_btjd'],[(z['cycles_between'],[(round(x['center_btjd'],3),x['sensitive'],x['observed_depth']) for x in z['checks']]) for z in spec])
