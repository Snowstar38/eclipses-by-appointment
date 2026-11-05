from pathlib import Path
import numpy as np, hashlib,json
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent; figs,ax=plt.subplots(figsize=(10,6));out={}
for i,tic in enumerate([41531803,79154285,464656473,231636563,404162889]):
 p=Path(f'[local-path-redacted]');h=fits.open(p);a=h[1].data;t=np.asarray(a['TIME']);f=np.asarray(a['SAP_FLUX']);q=np.asarray(a['QUALITY']);ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(t>3872)&(t<3878);tt=t[ok];ff=f[ok]/np.median(f[ok]);ax.plot(tt,ff+i*.015,'.-',ms=2,lw=.6,label=str(tic));g=np.diff(tt);j=np.argmax(g);out[str(tic)]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'largest_gap_start_btjd':float(tt[j]),'largest_gap_end_btjd':float(tt[j+1]),'gap_days':float(g[j]),'pre_gap_median_normalized':float(np.median(ff[(tt>tt[j]-.3)&(tt<=tt[j])])),'post_gap_median_normalized':float(np.median(ff[(tt>=tt[j+1])&(tt<tt[j+1]+.3)]))}
ax.legend();ax.set_xlabel('BTJD');ax.set_ylabel('normalized SAP + vertical offset');figs.tight_layout();figs.savefig(B/'helper-s94-comparison.png',dpi=150);(B/'helper-s94-comparison.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
