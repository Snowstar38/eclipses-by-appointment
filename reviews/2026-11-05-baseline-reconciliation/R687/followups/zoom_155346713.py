import hashlib
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

here=Path(__file__).resolve().parent
receipts=json.loads((here/'downloads-155346713.json').read_text())['products']
panels=[]
for r in receipts:
    p=Path(r['path']); assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
    with fits.open(p) as h:
        a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
    ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
    panels.append((r['sector'],t,f))
fig,axs=plt.subplots(2,1,figsize=(11,7))
for ax,(sec,t,f) in zip(axs,panels):
    if sec==7: lo,hi=1513.6,1516.1
    else: lo,hi=1517.9,1521.0
    ix=(t>=lo)&(t<=hi);x=t[ix];y=f[ix]/np.median(f[(t>=lo)&(t<=hi)])
    ax.plot(x,y,'ko-',ms=2,lw=.4)
    ax.set_xlim(lo,hi);ax.grid(alpha=.2);ax.set_ylabel('local normalized SAP');ax.set_title(f's{sec}: {len(x)} Q0 points')
    if sec==7:
        ax.axvline(3702.3228-65*33.63348396287843,color='green',ls=':',label='s88 - 65 Gaia P')
        ax.legend()
axs[-1].set_xlabel('BTJD');fig.tight_layout();fig.savefig(here/'155346713-s7-edge.png',dpi=170)
