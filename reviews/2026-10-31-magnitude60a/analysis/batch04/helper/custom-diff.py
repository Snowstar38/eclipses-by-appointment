from astropy.io import fits
import numpy as np,json,hashlib
from pathlib import Path
B=Path('[local path omitted]'); O=B/'helper'
for tic,sector in [('314047448',24),('48108063',62)]:
 m=json.load(open(B/tic/'measurements.json')); hist=Path('[local path omitted] 5/made/sb1-scale/diffimg')/tic/f'diff_s{sector}.json'; j=json.load(open(hist)); p=Path(f'[local path omitted]')
 with fits.open(p) as h: a=h[1].data; t=np.array(a['TIME']); q=np.array(a['QUALITY']); flux=np.array(a['FLUX'],float); bkg=np.array(a['FLUX_BKG'],float)
 phase=((t-m['primary_epoch_btjd']+m['period_days']/2)%m['period_days'])-m['period_days']/2
 dur=np.median([e['duration_days'] for e in m['events'] if e.get('timing_usable')]); valid=np.isfinite(t)&(q==0); inside=valid&(abs(phase)<dur*.22); outside=valid&(abs(phase)>dur*.8)&(abs(phase)<dur*1.8)
 # subtract modeled background as supplied, estimate local out-in pixel medians
 a=flux; diff=np.nanmedian(a[outside],axis=0)-np.nanmedian(a[inside],axis=0); base=np.nanmedian(a[outside],axis=0); xx,yy=j['target_px']; ix,iy=round(xx),round(yy)
 sums={}
 for r in [0,1,2]:
  sl=np.s_[iy-r:iy+r+1,ix-r:ix+r+1]; sums[str(2*r+1)]=float(np.nansum(diff[sl])/np.nansum(base[sl]))
 output={'tic':tic,'sector':sector,'n_in':int(inside.sum()),'n_out':int(outside.sum()),'duration_days':dur,'aperture_fractional_losses':sums,'target_px':j['target_px'],'target_pixel_deficit':float(diff[iy,ix]),'peak_deficit_xy':list(map(int,np.unravel_index(np.nanargmax(diff),diff.shape)[::-1])),'fits_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'historical_diff_sha256':hashlib.sha256(hist.read_bytes()).hexdigest()}
 np.savetxt(O/f'{tic}-measured-diff.csv',diff,delimiter=','); json.dump(output,open(O/f'{tic}-measured-diff.json','w'),indent=2);print(json.dumps(output))

