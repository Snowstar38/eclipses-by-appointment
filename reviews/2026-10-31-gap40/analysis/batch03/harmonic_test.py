import json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from astropy.io import fits
from scipy.optimize import least_squares
b=Path('[local path omitted]');m=json.load(open(b/'314041837/measurements.json'));P=m['period_days'];ep=m['primary_epoch_btjd']
with fits.open(b.parent/'shared-qlp/314041837_s077.fits') as h:
 d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=d['QUALITY']
ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]/np.median(f[ok]);ph=((t-ep+P/2)%P-P/2)
# per continuous segment baseline plus first 2 orbital harmonics, excluding central +/-0.3d
X=np.column_stack([np.ones(len(t)),t-np.mean(t)]+[a(2*np.pi*k*ph/P) for k in (1,2) for a in (np.sin,np.cos)])
mask=abs(ph)>.35;coef=np.linalg.lstsq(X[mask],f[mask],rcond=None)[0];res=f-X@coef
bins=np.arange(-P/2,P/2,.025);xx=[];yy=[]
for x in bins:
 z=abs(ph-x)<.0125
 if z.sum()>3:xx.append(x);yy.append(np.median(res[z]))
fig,ax=plt.subplots(2,1,figsize=(10,7));ax[0].plot(ph,f,'.',ms=1);ix=np.argsort(ph);ax[0].plot(ph[ix],(X@coef)[ix],'r.',ms=1);ax[1].plot(xx,np.array(yy)*1000,'.');ax[1].axhline(0,color='k');ax[1].set(xlabel='Days from measured broad minimum',ylabel='Residual ppt');fig.tight_layout();fig.savefig(b/'314041837/harmonic-test.png',dpi=130)
summary=dict(sector=77,model='linear time baseline plus sine/cosine first two orbital harmonics, fit excluding +/-0.35d from primary minimum',central_residual_ppt=float(np.median(res[abs(ph)<.08])*1000),outer_residual_scatter_ppt=float(1.4826*np.median(abs(res[mask]-np.median(res[mask])))*1000),note='Descriptive exclusion test, not calibrated model selection. Harmonics can absorb broad eclipses; a residual core tests whether smooth low-order modulation suffices.')
json.dump(summary,open(b/'314041837/harmonic-test.json','w'),indent=2);print(summary)
