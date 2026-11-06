import json,numpy as np
from pathlib import Path
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
b=Path(__file__).resolve().parent;d=b/'347159772';c=json.loads((d/'lead-context.json').read_text());s=next(x for x in c['source'] if x['sector']==80);cl=json.loads((b/'lead-clocks.json').read_text())['347159772'];pred=cl['epoch_btjd']+29*cl['period_d']
with fits.open(s['path']) as h:a=h[1].data;t=np.array(a['TIME']);q=np.array(a['QUALITY']);y=np.array(a['SAP_FLUX'])
m=np.isfinite(t)&np.isfinite(y)&(abs(t-pred)<.5);core=m&(abs(t-pred)<.06);o=dict(predicted_btjd=pred,cycle=29,sector=80,source_sha256=s['sha256'],core_samples=int(core.sum()),quality0_core=int((core&(q==0)).sum()),core_quality_values=np.unique(q[core]).tolist(),core_min_flux=float(np.min(y[core])),note='Flagged primary-shape depression near predicted clock; not used as formal timing or clean null.')
(d/'lead-flagged-repeat.json').write_text(json.dumps(o,indent=2));fig,ax=plt.subplots(figsize=(8,3));ax.plot(t[m&(q!=0)]-pred,y[m&(q!=0)],'.',label='flagged');ax.plot(t[m&(q==0)]-pred,y[m&(q==0)],'.',label='quality0');ax.legend();ax.set_title('TIC347159772 S80 predicted primary; flagged core');ax.set_xlabel('BTJD minus predicted');fig.tight_layout();fig.savefig(d/'lead-flagged-repeat.png',dpi=130);print(o)
