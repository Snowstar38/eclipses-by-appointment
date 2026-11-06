"""Gaia-period diagnostic only; per-sector 3-day median detrend of raw SAP."""
from pathlib import Path
import csv,json,hashlib
import numpy as np
from astropy.io import fits
from scipy.ndimage import median_filter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
H=B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'
for row in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf8')):
    tic=row['tic']; p=float(row['gaia_period_days']); out=B/tic
    bulk=json.loads((H/f'{tic}.json').read_text()); allph=[]; allfl=[]; sect=[]
    for rec in bulk['files']:
        fp=Path(rec['path']); assert hashlib.sha256(fp.read_bytes()).hexdigest()==rec['sha256']
        with fits.open(fp,memmap=False) as h:
            d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int)
        good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[good];f=f[good]
        if len(t)<50:continue
        dt=np.median(np.diff(t)); n=int(round(3/dt))|1
        trend=median_filter(f,size=n,mode='nearest'); norm=f/trend
        ph=(t/p)%1;allph.extend(ph);allfl.extend(norm);sect.extend([rec['sector']]*len(ph))
    ph=np.asarray(allph);fl=np.asarray(allfl); ss=np.asarray(sect)
    bins=np.linspace(0,1,201);med=[];count=[]
    for lo,hi in zip(bins[:-1],bins[1:]):
        v=fl[(ph>=lo)&(ph<hi)];med.append(float(np.median(v)) if len(v) else None);count.append(len(v))
    (out/'fold-gaia.json').write_text(json.dumps({'gaia_period_days':p,'method':'raw SAP q0 per-sector 3-day median detrend; diagnostic, no eclipse period adoption','phase_bin_centers':((bins[:-1]+bins[1:])/2).tolist(),'median':med,'n':count},indent=2)+'\n')
    fig,ax=plt.subplots(1,1,figsize=(11,3));ax.plot(ph,fl,'.',ms=.35,alpha=.1);ax.plot((bins[:-1]+bins[1:])/2,med,'r-',lw=1);ax.set_ylim(np.quantile(fl,[.002,.998]));ax.set_title(f'{row["sample_id"]} TIC {tic}, Gaia P={p:.5f} d (diagnostic)');ax.set_xlabel('Gaia phase');ax.set_ylabel('raw SAP / 3d median');fig.tight_layout();fig.savefig(out/'fold-gaia.png',dpi=140);plt.close(fig)
    print(tic,round(float(np.nanmin(med)),5),round(float(np.nanmax(med)),5),flush=True)
