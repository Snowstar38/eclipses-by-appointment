"""Fold-screen local raw SAP stacks; diagnostic, not event timing."""
import csv,json,sys
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
q=list(csv.DictReader((B/'queue.csv').open(encoding='utf-8',newline='')))
for row in q:
    if len(sys.argv)>1 and row['sample_id'] not in sys.argv[1:]:continue
    o=B/row['tic'];d=json.loads((o/'lead-numeric.json').read_text());fold=json.loads((o/'lead-fold-windows.json').read_text())
    occ=[]
    for s in d['sources']:
        wins=[w for w in fold['windows'] if w['sector']==s['sector'] and w['core_n']>=3 and w['side_n']>=12]
        if not wins:continue
        with fits.open(s['path'],memmap=False) as hd:
            a=hd[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);qu=np.asarray(a['QUALITY'],int)
        good=np.isfinite(t)&np.isfinite(f)&(f>0)&(qu==0);t=t[good];f=f[good]
        for w in wins:
            pred=w['pred_btjd'];span=max(.6,3*fold['screen_duration_days']);sel=abs(t-pred)<span
            z=t[sel]-pred;v=f[sel];side=(abs(z)>max(.2,fold['screen_duration_days']))&(abs(z)<span)
            if sum(side)<12:continue
            med=np.median(v[side]);occ.append((w,z,v/med))
    fig,axs=plt.subplots(1,2,figsize=(12,4))
    for w,z,v in occ:axs[0].plot(z,v,'.',ms=1,alpha=.15)
    zall=np.concatenate([x for w,x,v in occ]) if occ else np.array([]);vall=np.concatenate([v for w,x,v in occ]) if occ else np.array([])
    bins=np.linspace(-.6,.6,61);cent=(bins[1:]+bins[:-1])/2
    means=[float(np.median(vall[(zall>=a)&(zall<b)])) if np.any((zall>=a)&(zall<b)) else np.nan for a,b in zip(bins[:-1],bins[1:])]
    axs[1].plot(cent,np.asarray(means)*1000-1000,'o-',ms=2)
    axs[0].set(xlim=(-.6,.6),xlabel='days from fold prediction',ylabel='SAP / local median',title=f'{row["sample_id"]}: {len(occ)} covered occasions')
    axs[1].set(xlim=(-.6,.6),xlabel='days from fold prediction',ylabel='median residual ppt',title=f'P={fold["screen_period_days"]:.5f} d; not fitted')
    fig.tight_layout();fig.savefig(o/'lead-fold-stack.png',dpi=140);plt.close(fig)
    (o/'lead-fold-stack.json').write_text(json.dumps(dict(covered_occasions=len(occ),bin_center_days=cent.tolist(),median_residual_ppt=(np.asarray(means)*1000-1000).tolist()),indent=2)+'\n')
    print(row['sample_id'],len(occ),flush=True)
