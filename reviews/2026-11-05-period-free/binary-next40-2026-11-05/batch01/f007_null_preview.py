"""Representative measured F007 eclipse and fully covered shorter-alias nulls."""
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;H=B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results';bulk=json.loads((H/'238855958.json').read_text())
pick=[(67,3132.851,'eclipse'),(94,3858.534,'eclipse'),(94,3877.615,'P/2 null'),(67,3145.582,'P/3 null')]
fig,axs=plt.subplots(len(pick),1,figsize=(9,8),sharex=True)
for a,(sec,mid,label) in zip(axs,pick):
 rec=next(z for z in bulk['files'] if int(z['sector'])==sec)
 with fits.open(rec['path'],memmap=False) as hd:
  d=hd[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int)
 ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok];x=t-mid
 near=abs(x)<.8;side=near&(abs(x)>.35);base=np.median(f[side]);y=f/base
 a.plot(x[near],y[near],'.',ms=2);a.axvspan(-.13,.13,color='r',alpha=.12);a.set_ylabel(f'S{sec} {label}')
 a.set_xlim(-.8,.8);a.set_ylim(.988,1.006)
axs[-1].set_xlabel('BTJD offset from measured/predicted center (d)');fig.tight_layout();fig.savefig(B/'f007-null-preview.png',dpi=140)
