import json,math
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;d=json.loads((B/'SOURCE-SNAPSHOT.json').read_text())['280950412'];P=d['screen']['P']['P'];t0=d['screen']['P']['t0']
fig,axs=plt.subplots(8,1,figsize=(11,16))
for ax,r in zip(axs,d['target']['file_receipts']):
 with fits.open(r['path']) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
 ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
 phase=(t-t0+P/2)%P-P/2; sel=abs(phase)<1.2
 x=phase[sel];y=f[sel];base=np.median(y[abs(x)>.7]) if sum(abs(x)>.7) else np.median(y)
 ax.plot(x,(y/base-1)*1000,'.',ms=2);ax.set_xlim(-1.2,1.2);ax.set_ylim(-15,10);ax.set_title('s'+str(r['sector']))
fig.tight_layout();fig.savefig(B/'weak-phase-280950412.png',dpi=120)
