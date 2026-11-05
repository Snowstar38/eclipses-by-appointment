"""Representative actually covered S16 F023 event and submultiple null windows."""
from pathlib import Path
import json,hashlib
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;tic='286094277';m=json.loads((B/tic/'lead-measurements.json').read_text(encoding='utf8'))
r=next(x for x in m['source_receipts'] if int(x['sector'])==16);p=Path(r['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
with fits.open(p,memmap=False) as h:
    a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[good];f=f[good]
centers=[('observed same-kind',1747.3806),('third-clock extra phase',1756.5045),('half-clock extra phase',1761.0664)]
fig,axs=plt.subplots(1,3,figsize=(12,3.5),sharey=True)
for ax,(label,c) in zip(axs,centers):
    x=t-c;sel=np.abs(x)<.8;side=(np.abs(x)>.3)&(np.abs(x)<.7);base=np.median(f[side]);ax.plot(x[sel],f[sel]/base,'.',ms=2);ax.axvspan(-.15,.15,color='orange',alpha=.2);ax.set_xlim(-.8,.8);ax.set_title(label);ax.set_xlabel('Days from prediction')
axs[0].set_ylabel('Raw SAP / local median');fig.tight_layout();fig.savefig(B/tic/'lead-null-windows.png',dpi=140);plt.close(fig)
