import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;cases=[('467963921',67,3144.7563),('467963921',93,3840.7808),('467963921',102,4139.0750),('467963921',104,4188.7909)]
fig,axs=plt.subplots(len(cases),1,figsize=(10,15),squeeze=False);out=[]
for ax,(tic,s,c) in zip(axs[:,0],cases):
 p=Path(f'[local-path-redacted]')
 with fits.open(p) as h:a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'])
 ok=np.isfinite(t)&np.isfinite(f)&(q==0)&(abs(t-c)<4);x=t[ok]-c;y=f[ok]/np.median(f[ok]);ax.plot(x,y,'.',ms=1.5);ax.axvline(0,color='r');ax.set_title(f'{tic} s{s} pred {c}',fontsize=9);out.append({'tic':tic,'sector':s,'predicted_btjd':c,'quality_zero_samples_within_4d':int(sum(ok))})
fig.tight_layout();fig.savefig(B/'helper-alias-audit.png',dpi=120)
(B/'helper-alias-audit.json').write_text(json.dumps({'windows':out,'note':'Visual raw SAP quality zero; predicted centers are conditional, not fitted events.'},indent=2)+'\n')

