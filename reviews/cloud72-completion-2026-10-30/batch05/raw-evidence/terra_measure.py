import pathlib,json,numpy as np
from astropy.io import fits
R=pathlib.Path(__file__).parent
raw=json.load(open(R/'raw-events.json'))
rows=[]
for tic in ['431762229','9396327','222498305','183994341']:
 for e in raw[tic]['events']:
  if 'tc' not in e: continue
  sec=e['sector'];p=R/tic/f'independent_s{sec:03}.npz'
  if not p.exists():continue
  d=np.load(p);t=d['time'];y=d['flux'];T=e['duration_d'];x=t-e['tc'];m=np.isfinite(y)&(abs(x)<max(2*T,.3));x=x[m];y=y[m];y=y/np.median(y);shape=np.clip((T/2-abs(x))/(T*e['ingress_fraction']),0,1); A=np.column_stack((np.ones(len(x)),x,-shape)); c=np.linalg.lstsq(A,y,rcond=None)[0];res=y-A@c;err=np.sqrt(np.linalg.pinv(A.T@A)[2,2]*sum(res**2)/max(1,len(y)-3));rows.append(dict(tic=tic,sector=sec,tc=e['tc'],depth=float(c[2]),formal_error=float(err),n_in=int(sum(abs(x)<T/2)),rms=float(np.std(res))))
tic='90542579';sec=90;p=R/tic/f'qlp_s{sec:03}.fits'
with fits.open(p) as h:
 a=h[1].data;t=np.array(a['TIME']);y=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY']);m=np.isfinite(t)&np.isfinite(y)&(q==0)&(y>0);t=t[m];y=y[m]/np.median(y[m]);
d=np.load(R/tic/'independent_s090.npz');tt=d['time'];ff=d['flux']/np.median(d['flux']); edges=[]
for lo,hi in [(3757,3761),(3771,3775)]:
 z=(t>lo)&(t<hi);j=np.where(z)[0][np.argmin(y[z])];zz=(tt>lo)&(tt<hi);k=np.where(zz)[0][np.argmax(ff[zz])];edges.append(dict(window=[lo,hi],qlp_min_time=float(t[j]),qlp_min_relative_flux=float(y[j]),custom_max_time=float(tt[k]),custom_max_relative_flux=float(ff[k])))
out={'custom_aperture_fixed_template':rows,'sector90_edge_comparison':edges,'method':'Same TESS FFI photons reduced with target centred roughly 3x3 aperture, per-cadence faintest 48 pixel median background; independent of QLP reduction but not independent observations. QLP-derived event center, duration and ingress fraction held fixed; linear baseline and trapezoid depth fitted to custom flux within +/- max(2 duration, 0.3 d), uninflated formal errors; no exposure integration. Sector 90 ranges include boundary flags excluded by quality=0; flux scaled to sector median.'}
json.dump(out,open(R/'terra-helper-results.json','w'),indent=2)
print(json.dumps(out,indent=2))
