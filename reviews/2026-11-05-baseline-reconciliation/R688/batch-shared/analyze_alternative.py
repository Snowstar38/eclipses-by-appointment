import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
H=Path(__file__).parent
s=json.load(open(H/'sap-measurements.json'));P=s['screening_period_days'];T0=s['screening_epoch_btjd'];dur=s['screening_width_days']
fig,ax=plt.subplots(2,2,figsize=(11,7),layout='constrained')
out=[]
for i,sec in enumerate((56,84)):
    ep=T0+({56:53,84:90}[sec])*P
    for j,col in enumerate(('SAP_FLUX','PDCSAP_FLUX')):
        path=H/f'tess-spoc-s{sec:03d}.fits'
        with fits.open(path) as h:
            assert h[0].header['TICID']==412639100 and h[0].header['SECTOR']==sec
            d=h[1].data;t=np.array(d['TIME'],float);y=np.array(d[col],float);q=np.array(d['QUALITY'],int)
        x=t-ep;ok=np.isfinite(x)&np.isfinite(y)&(y>0)&(q==0)&(abs(x)<.85);x=x[ok];y=y[ok]
        oot=(abs(x)>.35)&(abs(x)<.8);coef=np.polyfit(x[oot],y[oot],1);yn=y/np.polyval(coef,x)
        core=abs(x)<dur/2;depth=(1-np.median(yn[core]))*1e6
        off=abs(x)>.3;noise=1.4826*np.median(abs(yn[off]-np.median(yn[off])))*1e6
        out.append(dict(sector=sec,column=col,quality='QUALITY==0',n_window=len(x),n_core=int(core.sum()),fixed_window_depth_ppm=depth,off_window_scatter_ppm=noise,baseline='linear fit to 0.35-0.8 d shoulders on each side of screening prediction',predicted_btjd=ep))
        a=ax[i,j];a.plot(x*24,(yn-1)*1e6,'.',ms=2,alpha=.55);a.axvspan(-dur*12,dur*12,color='salmon',alpha=.2);a.set(xlim=(-18,18),ylim=(-1200,1200),title=f'TESS-SPOC s{sec} {col}: fixed {depth:.0f} ppm')
fig.supxlabel('hours from QLP screening prediction');fig.supylabel('locally detrended flux residual (ppm)')
fig.savefig(H/'alternative-events.png',dpi=150);plt.close(fig)
(H/'alternative-measurements.json').write_text(json.dumps(dict(provenance='TESS-SPOC independently extracts same TESS FFI photons as QLP; not independent observation',measurements=out),indent=2)+'\n')
print(json.dumps(out,indent=2))
