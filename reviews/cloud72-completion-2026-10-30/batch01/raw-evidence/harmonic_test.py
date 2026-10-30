import json,numpy as np,pathlib
from astropy.io import fits
R=pathlib.Path(__file__).parent;raw=json.load(open(R/'raw-events.json'))['10790605'];P=raw['search_period'];t0=raw['search_epoch'];out=[]
for f in sorted((R/'10790605').glob('qlp*.fits')):
 with fits.open(f) as h:a=h[1].data;t=np.asarray(a['TIME'],float);y=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY']);m=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[m];y=y[m];y/=np.median(y)
 ph=(t-t0)/P;cols=[np.ones(len(t)),(t-np.mean(t))/np.ptp(t)]
 for k in range(1,5):cols.extend([np.sin(2*np.pi*k*ph),np.cos(2*np.pi*k*ph)])
 A=np.column_stack(cols);fit=np.linalg.lstsq(A,y,rcond=None)[0];z=y-A@fit;phase=(ph+.5)%1-.5
 for center in [0,.5]:
  dp=(phase-center+.5)%1-.5; inside=abs(dp)<.025;outside=(abs(dp)>.04)&(abs(dp)<.12); depth=float(np.mean(z[outside])-np.mean(z[inside]));se=float(np.sqrt(np.var(z[inside])/inside.sum()+np.var(z[outside])/outside.sum()));out.append(dict(sector=int(f.stem[-3:]),phase=center,depth=depth,formal_se=se,n_in=int(inside.sum()),n_out=int(outside.sum()),residual_rms=float(np.std(z))))
json.dump(dict(tic='10790605',period=P,epoch=t0,results=out,note='Four harmonics fitted across all cadences including eclipse; can absorb broad eclipses. IID standard errors ignore correlated noise; box width .05 cycle and local comparison .04-.12. Diagnostic only.'),open(R/'10790605/harmonic-test.json','w'),indent=2);print(out)
