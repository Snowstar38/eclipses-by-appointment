import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;tic='280051953';ctx=json.loads((B/tic/'lead-context.json').read_text()); ss={s['sector']:s for s in ctx['sectors']};events=json.loads((B/tic/'lead-trapezoid-fits.json').read_text());fig,ax=plt.subplots(figsize=(10,6))
for x in events:
 s=ss[x['sector']];c=x['center_btjd']
 with fits.open(s['source_path'],memmap=False) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
 g=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-c)<2.5);t=t[g];f=f[g]
 if len(t)<30:continue
 b=(abs(t-c)>1.3)&(abs(t-c)<2.5)
 if b.sum()<15:continue
 line=np.polyfit(t[b]-c,f[b],1);v=1000*(f/np.polyval(line,t-c)-1)
 ax.plot(t-c,v,'.',ms=.8,alpha=.35,label=f"S{x['sector']}" )
ax.set_xlim(-2,2);ax.set_ylim(-65,35);ax.axvline(0,color='black',lw=.6);ax.set_xlabel('Days from fitted center');ax.set_ylabel('SAP residual (ppt)');ax.set_title('Q079 recurring primary eclipse, independent sectors');ax.legend(ncol=4,fontsize=8);fig.tight_layout();fig.savefig(B/tic/'lead-eclipse-overlay.png',dpi=180)
