import json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
from pathlib import Path
B=Path(__file__).parent;m=json.loads((B/'241089793'/'measurements.json').read_text());p=m['historical_period_days'];t0=m['historical_epoch_btjd']
with fits.open(B.parent/'shared-qlp'/'241089793_s018.fits') as h:
 a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
fig,axs=plt.subplots(5,1,figsize=(9,11))
for ax,cyc in zip(axs,range(-1,4)):
 c=t0+cyc*p;z=np.isfinite(t)&np.isfinite(f)&(f>0)&(np.abs(t-c)<.4)
 oot=z&(np.abs(t-c)>.14)&(np.abs(t-c)<.34)&(q==0);base=np.median(f[oot])
 ax.plot(t[z&(q==0)]-c,f[z&(q==0)]/base,'.-',ms=4);ax.plot(t[z&(q!=0)]-c,f[z&(q!=0)]/base,'rx',ms=5)
 ax.axvspan(-.045,.045,color='orange',alpha=.1);ax.set_title(f'S18 cycle {cyc}, predicted {c:.5f} (guide only)');ax.set_ylim(.97,1.03)
fig.tight_layout();fig.savefig(B/'241089793'/'s18-cycle-check.png',dpi=150)
