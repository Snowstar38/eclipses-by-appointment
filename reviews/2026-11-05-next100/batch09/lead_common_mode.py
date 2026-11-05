import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
targets=['410117870','350091478','316880689','446548691','238195128','382040915']
fig,axs=plt.subplots(len(targets),1,figsize=(12,12),sharex=True)
rows=[]
for tic,ax in zip(targets,axs):
 ctx=json.loads((B/tic/'lead-context.json').read_text());s=next(x for x in ctx['sectors'] if x['sector']==94)
 with fits.open(s['source_path'],memmap=False) as h:
  a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
 g=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(t>=3873.2)&(t<=3876.3);t=t[g];f=f[g]
 baseline=(t>=3873.2)&(t<3873.7)
 f=f/np.median(f[baseline])
 ax.plot(t,f,'.',ms=1.5);ax.set_ylabel(tic,fontsize=9)
 rows.append(dict(tic=tic,sector=94,camera=next(x for x in json.loads((B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'/f'{tic}.json').read_text())['files'] if x['sector']==94)['camera'],ccd=next(x for x in json.loads((B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'/f'{tic}.json').read_text())['files'] if x['sector']==94)['ccd'],n=len(t),first=float(t.min()),last=float(t.max()),source_sha256=s['source_sha256']))
axs[-1].set_xlabel('BTJD');axs[0].set_title('S94 common-time raw SAP deficit and data gaps')
fig.tight_layout();fig.savefig(B/'lead-common-mode-s94.png',dpi=150)
(B/'lead-common-mode-s94.json').write_text(json.dumps(rows,indent=2)+'\n')
