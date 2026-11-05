from pathlib import Path
import hashlib,json
import numpy as np
from astropy.io import fits
from astropy.timeseries import LombScargle
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;p=Path('[local-path-redacted]')
with fits.open(p,memmap=False) as h:
 d=h[1].data;t=np.array(d['TIME']);f=np.array(d['SAP_FLUX']);q=np.array(d['QUALITY']);s=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[s];f=f[s];freq,power=LombScargle(t,f/np.median(f)).autopower(minimum_frequency=.2,maximum_frequency=10,samples_per_peak=10);k=np.argmax(power);period=float(1/freq[k]);ph=((t-1554.91)/period+.5)%1-.5
 fig,ax=plt.subplots(figsize=(8,4));ax.plot(ph,f,'.',ms=2);ax.set_ylim(.985,1.01);ax.set_xlabel(f'Phase from 1554.91 at {period:.5f} d');ax.set_ylabel('SAP');ax.grid();fig.tight_layout();fig.savefig(B/'helper-T057-shortfold.png',dpi=150)
 (B/'helper-T057-numerics.json').write_text(json.dumps({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'n':len(t),'start':float(t.min()),'end':float(t.max()),'grid_frequency_min':.2,'grid_frequency_max':10,'samples_per_peak':10,'grid_peak_period_days':period,'power':float(power[k])},indent=2)+'\n',encoding='utf-8')
