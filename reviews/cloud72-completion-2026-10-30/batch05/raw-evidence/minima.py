import numpy as np,json
from pathlib import Path
from astropy.io import fits
from scipy.signal import find_peaks
r=Path(__file__).parent;out={}
for tic in ['431762229','9396327','222498305','183994341','90542579']:
 rows=[]
 for f in sorted((r/tic).glob('qlp*.fits')):
  with fits.open(f) as h:
   a=h[1].data;t=np.array(a['TIME'],float);y=np.array(a['SAP_FLUX'],float);m=np.isfinite(t)&np.isfinite(y)&(y>0)&(a['QUALITY']==0);t=t[m];y=y[m]/np.median(y[m])
  # narrow low runs, retain minima separated by >0.3 days
  ii,_=find_peaks(-y,prominence=.025,distance=max(1,int(.3/np.median(np.diff(t)))))
  rows.append(dict(sector=int(f.stem[-3:]),minima=[dict(tc=float(t[i]),flux=float(y[i])) for i in ii],timespan=[float(t.min()),float(t.max())]))
 out[tic]=rows
(r/'minima-scan.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
