import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent; tic='341688154';m=json.loads((B/tic/'lead-numeric.json').read_text())
a=json.loads((B/'lead-t026-alias.json').read_text())
v=[x for x in a['windows'] if x['alias_cycles']==3 and x['full_sensitive_window']]
fig,axs=plt.subplots(len(v),1,figsize=(9,3*len(v)),squeeze=False)
for ax,x in zip(axs[:,0],v):
    s=next(z for z in m['sources'] if z['sector']==x['sector'])
    with fits.open(s['path'],memmap=False) as h:
        d=h[1].data;names=d.names;t=np.asarray(d['TIME'],float);q=np.asarray(d['QUALITY'],int)
        for name in ('SAP_FLUX','KSPSAP_FLUX_SML','KSPSAP_FLUX','KSPSAP_FLUX_LAG'):
            if name not in names:continue
            f=np.asarray(d[name],float);good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(np.abs(t-x['center_btjd'])<.5)
            if sum(good)<5:continue
            tx=t[good]-x['center_btjd'];fy=f[good]/np.median(f[good])
            ax.plot(tx,fy,'.',ms=3,alpha=.6,label=name)
    ax.set_xlim(-.5,.5);ax.set_ylim(.985,1.01);ax.set_title(f"s{x['sector']} predicted {x['center_btjd']:.4f}; raw deficit {x['raw_deficit_ppt']:.2f} ppt")
    ax.legend()
fig.tight_layout();fig.savefig(B/tic/'lead-alias-windows.png')
