"""Inspect actual raw windows at likely repeats of one-off ambiguous troughs."""
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
for tic,anchor,P,cycles in [('268385893',3388.842,45.87634355,[-22,-21,-5,-4,-3,-2,-1,0,1,2,3,4]),('277891015',3875.088,34.18186296,[-73,-64,-54,-53,-22,-21,0,1])]:
    d=json.loads((B/tic/'raw-inspection.json').read_text())
    panels=[]; windows=[]
    for s in d['sectors']:
        if 'path' not in s:continue
        with fits.open(s['path'],memmap=False) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        valid=np.isfinite(t)&np.isfinite(f)&(f>0);t=t[valid];f=f[valid];q=q[valid]
        for n in cycles:
            c=anchor+n*P
            if c<min(t)-1.5 or c>max(t)+1.5:continue
            ix=(abs(t-c)<1.2)&(q==0)
            if sum(ix)<8:continue
            x=t[ix]-c;y=f[ix]/np.median(f[ix]);
            core=abs(x)<.2;side=(abs(x)>.4)&(abs(x)<1.2)
            w={'sector':s['sector'],'cycle':n,'predicted_btjd':c,'n_quality0_window':int(sum(ix)),
               'n_core':int(sum(core)),'n_side':int(sum(side)),
               'core_side_difference_ppt':float(1000*(np.median(y[core])-np.median(y[side]))) if sum(core)>3 and sum(side)>6 else None}
            windows.append(w);panels.append((w,x,y))
    fig,axes=plt.subplots(len(panels),1,figsize=(9,max(3,2.1*len(panels))),squeeze=False)
    for ax,(w,x,y) in zip(axes[:,0],panels):
        ax.scatter(x,y,s=5);ax.axvline(0,color='r',lw=.5);ax.set_title(f"s{w['sector']} n{w['cycle']} predicted {w['predicted_btjd']:.2f} core-side {w['core_side_difference_ppt']}",fontsize=9)
    fig.tight_layout();fig.savefig(B/tic/'repeat-windows.png',dpi=120);plt.close(fig)
    (B/tic/'repeat-windows.json').write_text(json.dumps({'tic':tic,'anchor_btjd':anchor,'period_days':P,'windows':windows,'caveat':'Predictions from one apparent trough and Gaia period; core-side difference diagnostic only.'},indent=2)+'\n')
    print(tic,[(w['sector'],w['cycle'],w['n_core'],round(w['core_side_difference_ppt'] or 0,1)) for w in windows])
