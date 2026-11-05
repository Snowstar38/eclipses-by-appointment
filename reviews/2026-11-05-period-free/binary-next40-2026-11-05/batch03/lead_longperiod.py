"""Bounded photometric clock diagnostic from raw SAP for F022/F023."""
from pathlib import Path
import json,hashlib
import numpy as np
from astropy.io import fits
from astropy.timeseries import BoxLeastSquares
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
for sid,tic,lo,hi in [('F022','324424395',27.6,28.0),('F023','286094277',27.3,27.5)]:
    src=json.loads((B/tic/'lead-measurements.json').read_text(encoding='utf8'))
    tt=[];ff=[]
    for r in src['source_receipts']:
        p=Path(r['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
        with fits.open(p,memmap=False) as h:
            a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
        good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[good];f=f[good]
        if len(t)<30:continue
        tt.append(t);ff.append(f/np.median(f))
    t=np.concatenate(tt);f=np.concatenate(ff);grid=np.linspace(lo,hi,20000)
    pow=BoxLeastSquares(t,f).power(grid,[.2,.4,.8,1.6,2.4],objective='snr')
    i=int(np.argmax(pow.power));best=dict(period_days=float(grid[i]),epoch_btjd=float(pow.transit_time[i]),duration_days=float(pow.duration[i]),depth=float(pow.depth[i]),statistic=float(pow.power[i]))
    (B/tic/'lead-longperiod.json').write_text(json.dumps(dict(sample_id=sid,tic=tic,best=best,source_receipts=src['source_receipts'],method='Raw SAP sector-normalized BLS diagnostic; period resolution and event kinds require actual timing and alias checks'),indent=2)+'\n',encoding='utf8')
    fig,ax=plt.subplots(2,1,figsize=(10,6));ax[0].plot(grid,pow.power,lw=.5);ax[0].axvline(float(src['gaia']['period']),color='r',lw=.7);ax[0].set_ylabel('BLS statistic');ax[1].plot(((t-best['epoch_btjd']+best['period_days']/2)%best['period_days']-best['period_days']/2),f,'.',ms=1,alpha=.15);ax[1].set_xlim(-3,3);ax[1].set_xlabel('Phase days');fig.tight_layout();fig.savefig(B/tic/'lead-longperiod.png',dpi=140);plt.close(fig)
    print(sid,best,flush=True)
