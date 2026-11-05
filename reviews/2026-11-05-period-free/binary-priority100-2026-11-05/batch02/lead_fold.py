"""Independent raw SAP fold diagnostic for every fixed batch02 target.

Sector median normalization and an 8-day running median remove long trends;
the raw per-sector panel is retained by lead_measure.py. This is a visual
recurrence check, not a period or verdict estimator.
"""
import csv, json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.ndimage import median_filter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
for r in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')):
    p=float(r['gaia_period_days']); tic=r['tic']
    d=json.loads((B/tic/'lead-numeric.json').read_text());
    epoch=d['events'][0]['screen_btjd'] if d['events'] else 0
    xs=[]; ys=[]; ss=[]
    for src in d['sources']:
        with fits.open(src['path'],memmap=False) as hd:
            h=hd[1].data; t=np.asarray(h['TIME'],float); f=np.asarray(h['SAP_FLUX'],float); q=np.asarray(h['QUALITY'],int)
        m=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[m];f=f[m]
        if len(t)<30:continue
        cadence=np.median(np.diff(t)); width=max(11,int(8/cadence)//2*2+1)
        trend=median_filter(f,size=width,mode='nearest')
        y=f/trend-1; x=((t-epoch+p/2)%p-p/2)
        ok=np.isfinite(y)&(abs(y)<.5)
        xs.extend(x[ok]);ys.extend(y[ok]);ss.extend([int(src['sector'])]*sum(ok))
    x=np.asarray(xs);y=np.asarray(ys);s=np.asarray(ss)
    fig,ax=plt.subplots(figsize=(12,5))
    ax.plot(x,y,'.',ms=.65,alpha=.18,color='#2f628e')
    bins=np.linspace(-p/2,p/2,151);bc=(bins[:-1]+bins[1:])/2
    med=[np.median(y[(x>=a)&(x<b)]) if np.sum((x>=a)&(x<b))>=10 else np.nan for a,b in zip(bins[:-1],bins[1:])]
    ax.plot(bc,med,'r-',lw=1.4)
    ax.set(xlabel='Days from first screened window modulo Gaia SB1 period',ylabel='SAP / 8-day running median - 1',title=f"{r['sample_id']} TIC {tic}: raw fold at Gaia P={p:.5f} d; {len(d['sources'])} sectors")
    if len(y):ax.set_ylim(max(-.13,float(np.quantile(y,.001))*1.3),min(.13,float(np.quantile(y,.999))*1.3))
    fig.tight_layout();fig.savefig(B/tic/'lead-fold.png',dpi=120);plt.close(fig)
    print(r['sample_id'],tic,len(x),flush=True)
