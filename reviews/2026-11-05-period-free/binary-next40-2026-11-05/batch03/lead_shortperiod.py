"""Bounded short-clock diagnostic from quality-zero QLP corrected flux, same photons as SAP."""
from pathlib import Path
import json, csv, hashlib
import numpy as np
from astropy.io import fits
from astropy.timeseries import BoxLeastSquares
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
for row in csv.DictReader((B/'queue.csv').open(encoding='utf8')):
    if row['sample_id'] not in {'F027','F028','F030'}: continue
    tic=row['tic']; source=json.loads((B/tic/'lead-measurements.json').read_text(encoding='utf8'))
    tt=[];ff=[]; per=[]
    for r in source['source_receipts']:
        p=Path(r['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
        with fits.open(p,memmap=False) as h:
            a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['KSPSAP_FLUX'] if 'KSPSAP_FLUX' in h[1].columns.names else a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
        good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[good];f=f[good]
        if len(t)<30:continue
        ff.append(f/np.median(f));tt.append(t);per.append(int(r['sector']))
    t=np.concatenate(tt);f=np.concatenate(ff)
    lo,hi,n={'F027':(1.25,1.27,30000),'F028':(2.06,2.07,30000),'F030':(.5398,.5404,30000)}[row['sample_id']]
    grid=np.linspace(lo,hi,n)
    power=BoxLeastSquares(t,f).power(grid,[.05,.1,.2,.4],objective='snr')
    inds=np.argsort(power.power)[-10:][::-1]
    best=[]
    for i in inds:
        if all(abs(grid[i]-x['period_days'])>(hi-lo)/20 for x in best):
            best.append(dict(period_days=float(grid[i]),epoch_btjd=float(power.transit_time[i]),duration_days=float(power.duration[i]),depth=float(power.depth[i]),snr=float(power.power[i])))
    out=dict(sample_id=row['sample_id'],tic=tic,source_receipts=source['source_receipts'],method='BoxLeastSquares on QLP KSPSAP quality-zero data; diagnostic period search, same observing occasions as SAP',best=best)
    (B/tic/'lead-shortperiod.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
    fig,ax=plt.subplots(2,1,figsize=(10,6))
    ax[0].plot(grid,power.power,lw=.5);ax[0].set_xlim(lo,hi);ax[0].set_ylabel('BLS statistic')
    P=best[0]['period_days'];epoch=best[0]['epoch_btjd'];phase=((t-epoch+P/2)%P-P/2)
    ax[1].plot(phase,f,'.',ms=1,alpha=.2);ax[1].set_xlim(-P/2,P/2);ax[1].set_title(f'{row["sample_id"]} best {P:.6f} d');ax[1].set_xlabel('phase days')
    fig.tight_layout();fig.savefig(B/tic/'lead-shortperiod.png',dpi=140);plt.close(fig)
    print(row['sample_id'],best[:5],flush=True)
