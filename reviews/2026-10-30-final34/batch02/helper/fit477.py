import numpy as np, json, hashlib
from astropy.io import fits
from scipy.optimize import least_squares
from pathlib import Path
D=Path('.');p=16.601566756396096;t0=2210.2689715821157
for path in D.glob('47719859_s*.fits'):
 with fits.open(path) as h:
  a=h[1].data;t=np.array(a['TIME'],float);y=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY']);m=np.isfinite(t)&np.isfinite(y)&(q==0)&(y>0);t=t[m];y=y[m]
 print(path.name,hashlib.sha256(path.read_bytes()).hexdigest(),'time',t.min(),t.max())
 for n in range(int(np.floor((t.min()-t0)/p)),int(np.ceil((t.max()-t0)/p))+1):
  tp=t0+n*p;x=t-tp;m=abs(x)<1.5
  if m.sum()<15: continue
  xx=x[m];z=y[m]/np.median(y[m]);
  def f(a):return a[0]+a[1]*xx+a[2]*xx**2-a[3]*np.clip((a[5]/2-abs(xx-a[4]))/(a[5]*a[6]),0,1)
  a=least_squares(lambda a:f(a)-z,[1,0,0,.2,0,.586,.38],bounds=([.3,-1,-1,0,-1,.3,.05],[1.7,1,1,.99,1,1,.5]),max_nfev=3000).x
  print(n,'tc',tp+a[4],'delta',a[4],'depth',a[3],'dur',a[5],'n',len(xx),'rms',np.std(z-f(a)))
