"""Compare the S32 opening with same-camera/CCD cached controls."""
import hashlib,json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;D=B/'373314632'
sources=['373314632','373105227','396934213']
fig,axs=plt.subplots(3,1,figsize=(10,7),sharex=True);out=[]
for ax,tic in zip(axs,sources):
    p=Path(r'[local-path-redacted]')/f'{tic}_s032.fits';sha=hashlib.sha256(p.read_bytes()).hexdigest()
    with fits.open(p,memmap=False) as h:
        a=h[1].data;t=np.asarray(a['TIME'],float);q=np.asarray(a['QUALITY'],int);raw=np.asarray(a['SAP_FLUX'],float)
        cam=int(h[0].header['CAMERA']);ccd=int(h[0].header['CCD'])
        good=np.isfinite(t)&np.isfinite(raw)&(raw>0)&(q==0); m=good&(t>=2174.25)&(t<=2175.25)
        v=raw[m];tt=t[m]; norm=np.median(v[tt>2175]) if np.any(tt>2175) else np.median(v)
        ax.plot(tt,v/norm,'.',ms=3,label='SAP')
        if 'KSPSAP_FLUX' in h[1].columns.names:
            alt=np.asarray(a['KSPSAP_FLUX'],float)[m];valid=np.isfinite(alt)&(alt>0)
            if valid.any():ax.plot(tt[valid],alt[valid]/np.median(alt[valid]),'.',ms=3,label='KSPSAP')
        out.append(dict(tic=tic,sector=32,camera=cam,ccd=ccd,source_path=str(p),source_sha256=sha,
                        first_quality0_btjd=float(t[good].min()),window_points=int(m.sum()),
                        first_raw_over_late_median=float(v[0]/norm),
                        first_halfday_raw_min_over_late_median=float(np.min(v[tt<2174.75])/norm)))
        ax.set_ylabel(f'TIC {tic} C{cam}/{ccd}');ax.legend(fontsize=7)
axs[-1].set_xlabel('BTJD');fig.tight_layout();fig.savefig(D/'lead-startup-controls.png',dpi=150);plt.close(fig)
(D/'lead-startup-controls.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print([(x['tic'],x['camera'],x['ccd'],x['first_raw_over_late_median']) for x in out])
