import json,numpy as np
from pathlib import Path
from astropy.io import fits
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;o=json.loads((B/'113645244/raw-inspection.json').read_text());p=41.94565;t0=1676.36097;c=t0+105*p/2;f=next(x for x in o['sectors'] if x['sector']==94)
with fits.open(f['path']) as h:a=h[1].data;t=np.asarray(a['TIME'],float);y=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'])
ok=np.isfinite(t)&np.isfinite(y)&(q==0)&(abs(t-c)<.6);t=t[ok];y=y[ok];core=abs(t-c)<.07;side=(abs(t-c)>.15)&(abs(t-c)<.35);base=np.median(y[side]);fig,ax=plt.subplots(figsize=(8,3));ax.plot(t-c,y/base,'.',ms=2);ax.axvspan(-.07,.07,alpha=.2);ax.axhline(1,color='k');ax.set(xlabel='days from half-period prediction',ylabel='SAP / local median',title=f'TIC 113645244 S94 BTJD {c:.4f}');fig.tight_layout();fig.savefig(B/'helper-half-alias.png',dpi=150)
(B/'helper-half-alias.json').write_text(json.dumps({'predicted_center_btjd':c,'quality0_core_points':int(sum(core)),'core_span_days':float(np.ptp(t[core])),'core_deficit_ppt':float(1000*(1-np.median(y[core])/base)),'baseline_abs_time_days':[.15,.35],'source_sha256':f['sha256'],'method':'conditional half period test; inspect plotted actual data, not calibrated uncertainty'},indent=2)+'\n')
