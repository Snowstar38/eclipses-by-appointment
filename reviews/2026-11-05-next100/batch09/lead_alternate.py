import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
spec=[('210963066',11,1619.39,2.5),('191416124',57,2872.53,6),('191416124',84,3604.94,5),('316880689',1,1335.27,7),('74352282',39,2381.,3),('243276811',74,3326.76,3),('243276811',82,3546.87,3)]
out=[];fig,axs=plt.subplots(len(spec),1,figsize=(12,2.4*len(spec)))
for ax,(tic,sec,c,rad) in zip(axs,spec):
 ctx=json.loads((B/tic/'lead-context.json').read_text());s=next(x for x in ctx['sectors'] if x['sector']==sec)
 with fits.open(s['source_path'],memmap=False) as h:
  a=h[1].data;t=np.array(a['TIME'],float);q=np.array(a['QUALITY'],int);names=h[1].columns.names
  mask=np.isfinite(t)&(q==0)&(abs(t-c)<=rad)
  for name in ['SAP_FLUX','DET_FLUX','DET_FLUX_SML','SYS_RM_FLUX','KSPSAP_FLUX']:
   if name not in names:continue
   f=np.array(a[name],float);g=mask&np.isfinite(f)&(f>0)
   if np.count_nonzero(g)<10:continue
   tt=t[g];ff=f[g]/np.median(f[g]);ax.plot(tt,ff,'.',ms=1,alpha=.5,label=name)
   out.append(dict(tic=tic,sector=sec,center_btjd=c,flux_column=name,points=int(g.sum()),raw_positive_median=float(np.median(f[g])),normalized_p05_p95_ppt=(np.percentile(ff,[5,95])*1000).tolist(),source_sha256=s['source_sha256']))
 ax.axvline(c,color='k',lw=.5);ax.set_title(f'{tic} S{sec} at {c:.2f}',fontsize=9);ax.set_ylabel('f/median',fontsize=8)
axs[0].legend(ncol=5,fontsize=6);fig.tight_layout();fig.savefig(B/'lead-alternate.png',dpi=120)
(B/'lead-alternate.json').write_text(json.dumps(out,indent=2)+'\n')
