import json,numpy as np,matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
from pathlib import Path
B=Path('[workspace]/Astra/made/final-night-2026-11-05/visual10');tic='27681485';d=json.loads((B.parent.parent/'binary-exploration-2026-11-04/bulk-results'/f'{tic}.json').read_text());fig,ax=plt.subplots(5,1,figsize=(10,11))
for aa,r in zip(ax,d['files']):
 with fits.open(r['path']) as h:
  dd=h[1].data;t=np.array(dd['TIME']);y=np.array(dd['SAP_FLUX']);q=np.array(dd['QUALITY'])
 ok=(q==0)&np.isfinite(t)&np.isfinite(y)&(y>0);t=t[ok];y=y[ok]/np.median(y[ok]);phase=((t-2505.65+36.48222/2)%36.48222)-36.48222/2;aa.plot(phase,y,'.',ms=1);aa.set_title('S'+str(r['sector']));aa.set_xlim(-4,4);aa.axvline(0,c='r')
fig.suptitle('TIC27681485: primary windows at Gaia period, reference2505.65 (guide only)');fig.tight_layout();fig.savefig(B/tic/'lead-gaia-repeat-windows.png',dpi=130)
