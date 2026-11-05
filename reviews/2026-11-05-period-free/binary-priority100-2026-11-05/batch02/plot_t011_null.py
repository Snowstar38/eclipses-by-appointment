"""Visual audit of T011 conditional Gaia-cycle null windows."""
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;tic='355493553';d=json.loads((B/tic/'lead-coverage.json').read_text());src=json.loads((B/tic/'lead-numeric.json').read_text())['sources'];src={x['sector']:x['path'] for x in src};wins=[x for x in d['windows'] if x['sector'] in (96,102,104)]
fig,axs=plt.subplots(3,1,figsize=(8,7.5))
for ax,w in zip(axs,wins):
    with fits.open(src[w['sector']],memmap=False) as hd:
        h=hd[1].data;t=np.asarray(h['TIME'],float);f=np.asarray(h['SAP_FLUX'],float);q=np.asarray(h['QUALITY'],int)
    x=t-w['pred_btjd'];m=np.isfinite(x)&np.isfinite(f)&(f>0)&(q==0)&(abs(x)<2);x=x[m];y=f[m];side=(abs(x)>1.0)&(abs(x)<1.8);y=y/np.median(y[side]);
    ax.plot(x,y,'.',ms=2);ax.axvspan(-.6,.6,color='orange',alpha=.15);ax.axhline(1,color='gray',lw=.5);ax.set(xlabel='days from conditional center',ylabel='raw SAP / side',title=f"S{w['sector']} cycle {w['cycle']}: deficit {w['raw_core_deficit_ppt']:.2f} ppt, core {w['core_quality0_n']} q0")
fig.tight_layout();fig.savefig(B/tic/'lead-conditional-nulls.png',dpi=150);plt.close(fig)
