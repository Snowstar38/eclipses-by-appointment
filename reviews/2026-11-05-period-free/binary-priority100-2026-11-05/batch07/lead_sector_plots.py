"""Plot raw and QLP alternate flux by sector for deciding candidates."""
import csv, json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
for row in csv.DictReader((B/'queue.csv').open(newline='')):
    tic=row['tic']; bulk=json.loads(Path(r'[local-path-redacted]',tic+'.json').read_text())
    files=[r for r in bulk['files'] if r['status']=='ok']
    for k in range(0,len(files),8):
        chunk=files[k:k+8]; fig,axs=plt.subplots(len(chunk),1,figsize=(12,2.2*len(chunk)),squeeze=False)
        for ax,r in zip(axs[:,0],chunk):
            with fits.open(r['path'],memmap=False) as hd:
                d=hd[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int)
                alt=np.asarray(d['KSPSAP_FLUX'],float) if 'KSPSAP_FLUX' in d.names else None
            ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)
            ax.plot(t[ok],f[ok]/np.median(f[ok]),'.',ms=.7,label='SAP')
            if alt is not None:
                ao=ok&np.isfinite(alt)&(alt>0)
                ax.plot(t[ao],alt[ao]/np.median(alt[ao]),'.',ms=.6,alpha=.4,label='KSPSAP')
            ax.set_title(f"{tic} s{r['sector']} raw/alternate q0",fontsize=9)
            ax.set_ylabel('relative flux')
            ax.set_ylim(.85,1.15)
        axs[0,0].legend(loc='upper right'); axs[-1,0].set_xlabel('BTJD')
        fig.tight_layout();fig.savefig(B/tic/f'lead-sector-{k//8+1:02d}.png',dpi=120);plt.close(fig)
