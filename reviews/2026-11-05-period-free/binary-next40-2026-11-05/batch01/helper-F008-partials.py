import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent; H=B.parent.parent/'binary-exploration-2026-11-04';b=json.loads((H/'bulk-results/339023379.json').read_text()); fig,axs=plt.subplots(2,1,figsize=(10,6))
for a,s in zip(axs,[12,66]):
 rec=next(x for x in b['files'] if x['sector']==s)
 with fits.open(rec['path']) as h:t=np.array(h[1].data['TIME'],float);f=np.array(h[1].data['SAP_FLUX'],float);q=np.array(h[1].data['QUALITY'],int)
 g=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[g];f=f[g];a.plot(t,f/np.median(f),'.',ms=1);a.set_title('S'+str(s)+' raw QLP; quality 0');a.set_xlabel('BTJD')
fig.tight_layout();fig.savefig(B/'helper-F008-S12-S66.png',dpi=120)
