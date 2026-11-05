import hashlib
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

here=Path(__file__).resolve().parent
recs=json.loads((here/'alternative-downloads-155346713.json').read_text())
rows=[]
fig,axs=plt.subplots(2,1,figsize=(10,7))
for rec in recs:
    if rec['status']!='ok':continue
    p=Path(rec['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==rec['sha256']
    with fits.open(p) as h:a=h[1].data
    if rec['provenance']=='TESS-SPOC':
        t=np.asarray(a['TIME'],float);q=np.asarray(a['QUALITY'],int)
        choices=[('SAP_FLUX',np.asarray(a['SAP_FLUX'],float)),('PDCSAP_FLUX',np.asarray(a['PDCSAP_FLUX'],float))]
        good=q==0
    else:
        t=np.asarray(a['time'],float);q=np.asarray(a['TESS_flags'],int);q2=np.asarray(a['TGLC_flags'],int)
        choices=[('psf_flux',np.asarray(a['psf_flux'],float)),('aperture_flux',np.asarray(a['aperture_flux'],float)),
                 ('cal_psf_flux',np.asarray(a['cal_psf_flux'],float)),('cal_aper_flux',np.asarray(a['cal_aper_flux'],float))]
        good=(q==0)&(q2==0)
    for name,f in choices:
        ok=good&np.isfinite(t)&np.isfinite(f)&(f>0);x=t[ok];y=f[ok]
        if len(x)==0:continue
        baseline=(x>1501.8)&(x<1502.35)
        if baseline.sum()<5:continue
        y=y/np.median(y[baseline])
        dip=(x>1502.42)&(x<1502.58)
        ingress=(x>1515.85)&(x<1516.04)
        rows.append({'provenance':rec['provenance'],'column':name,'q0_n':len(x),'baseline_n':int(baseline.sum()),
                     'B_min':float(y[dip].min()) if dip.any() else None,
                     'A_ingress_min':float(y[ingress].min()) if ingress.any() else None,
                     'last_btjd':float(x.max())})
        for ax,lo,hi in zip(axs,(1502.2,1515.5),(1502.85,1516.1)):
            ix=(x>=lo)&(x<=hi);ax.plot(x[ix],y[ix],'.-',ms=3,lw=.7,label=rec['provenance']+' '+name)
for ax,(lo,hi) in zip(axs,((1502.2,1502.85),(1515.5,1516.1))):
    ax.set_xlim(lo,hi);ax.grid(alpha=.2);ax.set_ylabel('flux / pre-B baseline');ax.legend(fontsize=6)
axs[-1].set_xlabel('BTJD');fig.tight_layout();fig.savefig(here/'155346713-alternative-events.png',dpi=170)
(here/'alternative-comparison-155346713.json').write_text(json.dumps(rows,indent=2))
print(json.dumps(rows,indent=2))
