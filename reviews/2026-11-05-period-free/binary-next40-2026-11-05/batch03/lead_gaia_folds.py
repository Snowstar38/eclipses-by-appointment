"""Check whether raw SAP dips form a coherent fold at each selection Gaia SB period."""
from pathlib import Path
import csv,json,hashlib
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
for row in csv.DictReader((B/'queue.csv').open(encoding='utf8')):
    if row['sample_id'] not in {'F021','F024','F025','F026','F027','F029'}:continue
    tic=row['tic'];P=float(row['gaia_period_days']);m=json.loads((B/tic/'lead-measurements.json').read_text(encoding='utf8'));phase=[];flux=[]
    for r in m['source_receipts']:
        p=Path(r['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
        with fits.open(p,memmap=False) as h:
            a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
        good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[good];f=f[good]
        if len(t)<30:continue
        phase.append((t%P)/P);flux.append(f/np.median(f))
    x=np.concatenate(phase);y=np.concatenate(flux);bins=np.linspace(0,1,121);idx=np.digitize(x,bins)-1
    med=[float(np.median(y[idx==j])) if sum(idx==j)>=5 else None for j in range(120)]
    d=dict(sample_id=row['sample_id'],tic=tic,gaia_period_days=P,phase_bin_centers=((bins[:-1]+bins[1:])/2).tolist(),median_normalized_raw_sap=med,points=len(y),source_receipts=m['source_receipts'],caveat='Gaia-period fold is a diagnostic only; a flat fold cannot exclude another orbit, transient, or eclipse below sensitivity. Sector normalization does not remove all trends.')
    (B/tic/'lead-gaia-fold.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf8')
    fig,ax=plt.subplots(figsize=(8,3));ax.plot(x,y,'.',ms=.6,alpha=.08);ax.plot(d['phase_bin_centers'],med,'r-',lw=1);ax.set(xlabel='Gaia SB phase',ylabel='SAP / sector median',title=f'{row["sample_id"]} Gaia P={P:.4f} d');fig.tight_layout();fig.savefig(B/tic/'lead-gaia-fold.png',dpi=140);plt.close(fig)
    print(row['sample_id'],len(y))
