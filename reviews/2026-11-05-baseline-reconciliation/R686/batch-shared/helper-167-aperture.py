import numpy as np,json,hashlib
from astropy.io import fits
from scipy.optimize import least_squares
from pathlib import Path
W=Path(__file__).resolve().parent;p=W/'helper-167197264_tesscut_s076.fits'
with fits.open(p,memmap=False) as h:
 d=h[1].data;t=np.array(d['TIME'],float);f=np.array(d['FLUX'],float);q=np.array(d['QUALITY'])
# target (x,y) near (4.2,4.2), 3x3 centered on pixel 4,4; sky is median of outer border
border=np.ones((9,9),bool);border[1:-1,1:-1]=False
sky=np.nanmedian(f[:,border],axis=1); flux=np.nansum(f[:,3:6,3:6],axis=(1,2))-9*sky
m=np.isfinite(t)&np.isfinite(flux)&(flux>0)&(q==0)&(abs(t-3380.39)<2);x=t[m];y=flux[m]/np.median(flux[m][abs(x-3380.39)>1]);
def res(v):
 mid,amp,hw,ing,b,s=v;return b+s*(x-3380.39)-amp*np.clip((hw-abs(x-mid))/ing,0,1)-y
v=least_squares(res,[3380.39,.03,.75,.47,1,0],bounds=([3380.1,0,.3,.05,.8,-.1],[3380.7,.2,1.2,.9,1.2,.1]),loss='soft_l1',f_scale=.003).x
out={'method':'TESScut 3x3 pixels centered on target; subtract 9 times median of outer-border pixels each cadence; Q0, finite positive flux, +/-2d; trapezoid plus linear baseline','n':len(x),'mid_btjd':v[0],'depth_fraction':v[1],'width_days':2*v[2],'ingress_days':v[3],'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'limitation':'Different extraction of same TESS photons; not an independent observation; no calibrated dilution correction.'}
(W/'helper-167-aperture.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
