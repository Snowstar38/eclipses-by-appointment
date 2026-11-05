import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;tic='280051953';ss={s['sector']:s for s in json.loads((B/tic/'lead-context.json').read_text())['sectors']};fig,axs=plt.subplots(3,2,figsize=(12,10))
for row,(sec,half,primary) in enumerate([(94,3859.82,3874.08),(95,3888.17,3902.37),(96,3916.51,3930.69)]):
 s=ss[sec]
 with fits.open(s['source_path'],memmap=False) as h:
  a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
 g=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[g];f=f[g]
 for j,(c,label) in enumerate([(half,'half phase'),(primary,'primary')]):
  ax=axs[row,j];sel=abs(t-c)<=2.4;tt=t[sel];ff=f[sel];base=(abs(tt-c)>=1.4)&(abs(tt-c)<=2.4)
  if base.sum()>10:line=np.polyfit(tt[base]-c,ff[base],1);v=1000*(ff/np.polyval(line,tt-c)-1)
  else:v=1000*(ff/np.median(ff)-1)
  ax.plot(tt-c,v,'.',ms=1);ax.set_title(f'S{sec} {label} {c:.2f}');ax.set_xlim(-2.2,2.2);ax.set_ylim(-55,20);ax.set_ylabel('ppt');ax.axvline(0,color='k',lw=.5)
fig.tight_layout();fig.savefig(B/tic/'lead-primary-vs-halfphase.png',dpi=160)
