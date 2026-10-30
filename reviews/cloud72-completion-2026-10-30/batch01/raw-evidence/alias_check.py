import json,numpy as np,pathlib
from astropy.io import fits
R=pathlib.Path(__file__).parent;raw=json.load(open(R/'raw-events.json'))['465073693'];P=raw['representative_ephemeris']['period_d'];t0=raw['representative_ephemeris']['epoch_btjd'];o=[]
for f in sorted((R/'465073693').glob('qlp*.fits')):
 with fits.open(f) as h:a=h[1].data;t=np.asarray(a['TIME'],float);y=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY']);m=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[m];y=y[m];y/=np.median(y)
 for phase in [0,.5]:
  cy=np.arange(np.ceil((t.min()-t0-phase*P)/P),np.floor((t.max()-t0-phase*P)/P)+1)
  for n in cy:
   x=t-(t0+(n+phase)*P);m=abs(x)<.65;xx=x[m];z=y[m];inside=abs(xx)<.11;outside=(abs(xx)>.25)&(abs(xx)<.6)
   if inside.sum()<3 or outside.sum()<10:continue
   coef=np.polyfit(xx[outside],z[outside],1);dep=float(np.mean(np.polyval(coef,xx[inside])-z[inside]));o.append(dict(sector=int(f.stem[-3:]),phase=phase,cycle=int(n),depth=dep,n_in=int(inside.sum()),n_out=int(outside.sum())))
json.dump(dict(period_d=P,events=o,note='Fixed plus or minus 0.11 d core, linear local baseline; phase 0.5 is a diagnostic for equal spacing, eccentric secondary can occur elsewhere; exposure dilution and variability not modelled.'),open(R/'465073693/alias-check.json','w'),indent=2);print(o)

