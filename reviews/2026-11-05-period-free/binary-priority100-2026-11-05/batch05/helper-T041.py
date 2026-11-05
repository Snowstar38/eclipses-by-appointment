import json,hashlib,numpy as np
from pathlib import Path
from astropy.io import fits
from astropy.timeseries import LombScargle
B=Path(__file__).parent;p=Path(r'[local-path-redacted]')
with fits.open(p) as h:
 d=h[1].data;t=np.array(d['TIME']);f=np.array(d['SAP_FLUX']);q=np.array(d['QUALITY'])
m=np.isfinite(t)&np.isfinite(f)&(q==0)&(abs(t-2948.188321)<2);t=t[m];f=f[m];freq=np.linspace(2,10,10000);ls=LombScargle(t,f/np.median(f)-1);power=ls.power(freq);i=np.argmax(power);out=dict(source=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),window_btjd=[float(t.min()),float(t.max())],n=len(t),frequency_search_cycles_per_day=[2,10],period_days=float(1/freq[i]),peak_power=float(power[i]),note='Local quality-zero raw SAP sinusoid frequency scan; describes oscillation, not an orbital period or precision fit.')
(B/'helper-T041-numeric.json').write_text(json.dumps(out,indent=2));print(out)
