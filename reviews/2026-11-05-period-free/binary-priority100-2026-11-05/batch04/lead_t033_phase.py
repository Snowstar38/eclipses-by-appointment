import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
tic='362778566'
m=json.loads((B/tic/'lead-numeric.json').read_text())
P=m['gaia_period_days']; epoch=m['events'][0]['fit_mid_btjd']
fig,axs=plt.subplots(3,1,figsize=(10,8))
out=[]
for ax,s in zip(axs,m['sources']):
 p=Path(s['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256']
 with fits.open(p,memmap=False) as h:
  d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int)
  alt=np.asarray(d['KSPSAP_FLUX'],float) if 'KSPSAP_FLUX' in d.names else None
 ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
 if alt is not None:alt=alt[ok]
 near=epoch+round((np.median(t)-epoch)/P)*P
 sel=np.abs(t-near)<5
 baseline=(np.abs(t-near)>2)&(np.abs(t-near)<5)
 norm=np.median(f[baseline]) if sum(baseline)>20 else np.median(f)
 ax.plot(t[sel]-near,f[sel]/norm,'.',ms=2,label='SAP')
 if alt is not None:
  aok=sel&np.isfinite(alt)&(alt>0)
  ax.plot(t[aok]-near,alt[aok]/np.median(alt[baseline&np.isfinite(alt)&(alt>0)]),'.',ms=1,alpha=.5,label='KSPSAP')
 ax.axvline(0,color='r',lw=1);ax.set_ylim(.97,1.03);ax.set_title(f"s{s['sector']} predicted BTJD {near:.3f}");ax.legend()
 out.append(dict(sector=s['sector'],pred_btjd=float(near),data_start=float(t.min()),data_end=float(t.max()),pred_minus_start=float(near-t.min()),core_n=int(sum(np.abs(t-near)<1)),baseline_n=int(sum(baseline)),core_median_ppt=float(1000*(np.median(f[np.abs(t-near)<1])/norm-1)) if sum(np.abs(t-near)<1)>0 else None))
fig.tight_layout();fig.savefig(B/tic/'lead-phase.png',dpi=130)
(B/tic/'lead-phase.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
