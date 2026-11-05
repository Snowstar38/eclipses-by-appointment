"""Plot actual raw and corrected flux at Gaia-period predicted windows."""
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
allrows=json.loads((B/'lead-fold-coverage.json').read_text())
for sample in ('T061','T069','T070'):
    r=next(x for x in allrows if x['sample_id']==sample)
    selected=[w for w in r['records'] if w['core_time_bin_coverage']>.5]
    if sample=='T061': selected=[w for w in selected if w['sector'] in (16,17,57,84)]
    cols=2; nr=(len(selected)+cols-1)//cols
    fig,axs=plt.subplots(nr,cols,figsize=(12,nr*2.7),squeeze=False)
    src={x['sector']:x for x in json.loads((B/r['tic']/'lead-numeric.json').read_text())['sources']}
    for ax,w in zip(axs.flat,selected):
        with fits.open(src[w['sector']]['path'],memmap=False) as h:
            d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int)
            alt=np.asarray(d['KSPSAP_FLUX'],float) if 'KSPSAP_FLUX' in d.names else None
        center=w['pred_btjd'];span=max(3*r['core_half_width_days'],2)
        ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(np.abs(t-center)<span)
        t=t[ok];f=f[ok]
        if len(t)==0:continue
        base=np.median(f)
        ax.plot(t-center,f/base,'.',ms=1,label='SAP')
        if alt is not None:
            alt=alt[ok]; good=np.isfinite(alt)&(alt>0)
            ax.plot(t[good]-center,alt[good]/np.median(alt[good]),'.',ms=.8,alpha=.5,label='KSPSAP')
        ax.axvspan(-r['core_half_width_days'],r['core_half_width_days'],alpha=.08,color='red')
        ax.set_title(f"s{w['sector']} n={w['cycle']} pred {center:.2f} cov {w['core_time_bin_coverage']:.2f} D {w.get('raw_core_minus_baseline_ppt',float('nan')):.1f} ppt",fontsize=9)
        ax.set_xlabel('days from predicted');ax.set_ylabel('relative flux')
    for ax in list(axs.flat)[len(selected):]:ax.axis('off')
    axs[0,0].legend();fig.tight_layout();fig.savefig(B/r['tic']/'lead-deciding-windows.png',dpi=120);plt.close(fig)
