"""Visual audit of T014 deciding P/2 null windows."""
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;tic='313142904';d=json.loads((B/tic/'lead-half-alias.json').read_text());src=json.loads((B/tic/'lead-numeric.json').read_text())['sources'];src={x['sector']:x['path'] for x in src};windows=[x for x in d['windows'] if x['sector'] in (40,53,60)]
fig,axs=plt.subplots(3,1,figsize=(8,7.5))
for ax,w in zip(axs,windows):
    with fits.open(src[w['sector']],memmap=False) as hd:
        h=hd[1].data;t=np.asarray(h['TIME'],float);f=np.asarray(h['SAP_FLUX'],float);q=np.asarray(h['QUALITY'],int)
    x=t-w['pred_btjd'];m=np.isfinite(x)&np.isfinite(f)&(f>0)&(q==0)&(abs(x)<.5);x=x[m];y=f[m];side=((abs(x)>.2)&(abs(x)<.4));y=y/np.median(y[side]);
    ax.plot(x,y,'.',ms=3);ax.axvspan(-.1,.1,color='orange',alpha=.15);ax.axhline(1,color='gray',lw=.5);ax.set(xlabel='days from predicted half-cycle',ylabel='raw SAP / side',title=f"S{w['sector']} half cycle {w['half_cycle']}: deficit {w['core_deficit_ppt']:.2f} ppt, q0 core {w['core_q0_n']}")
fig.tight_layout();fig.savefig(B/tic/'lead-half-alias.png',dpi=150);plt.close(fig)
