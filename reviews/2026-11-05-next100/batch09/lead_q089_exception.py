import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
spec=[('382040915',67,3147.,2.5),('74352282',39,2381.,2.5),('382040915',39,2381.,2.5)]
fig,axs=plt.subplots(3,1,figsize=(11,8));out=[]
for ax,(tic,sec,c,rad) in zip(axs,spec):
 ctx=json.loads((B/tic/'lead-context.json').read_text());s=next(x for x in ctx['sectors'] if x['sector']==sec)
 with fits.open(s['source_path'],memmap=False) as h:
  a=h[1].data;t=np.array(a['TIME'],float);q=np.array(a['QUALITY'],int)
  for name in ['SAP_FLUX','DET_FLUX','SYS_RM_FLUX','KSPSAP_FLUX']:
   if name not in h[1].columns.names:continue
   f=np.array(a[name],float);g=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-c)<=rad)
   if np.count_nonzero(g)<10:continue
   ax.plot(t[g],f[g]/np.median(f[g]),'.',ms=1.5,alpha=.5,label=name)
   out.append(dict(tic=tic,sector=sec,flux_column=name,points=int(g.sum()),time_start=float(t[g].min()),time_end=float(t[g].max()),source_sha256=s['source_sha256']))
 ax.set_title(f'{tic} S{sec} around {c:.1f}',fontsize=10);ax.legend(fontsize=6,ncol=4)
fig.tight_layout();fig.savefig(B/'lead-q089-exception.png',dpi=130)
(B/'lead-q089-exception.json').write_text(json.dumps(out,indent=2)+'\n')
