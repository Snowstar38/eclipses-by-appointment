import json,numpy as np
from pathlib import Path
from astropy.io import fits
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;o=json.loads((B/'294257329/raw-inspection.json').read_text());f=next(x for x in o['sectors'] if x['sector']==62)
with fits.open(f['path']) as h:a=h[1].data;t=np.array(a['TIME'],float);y=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'])
ok=np.isfinite(t)&np.isfinite(y)&(q==0)&(t>2989)&(t<3009);t=t[ok];y=y[ok];y/=np.median(y);fig,ax=plt.subplots(figsize=(12,4));ax.plot(t,y,'.',ms=2);ax.axvline(2989.82,color='r');ax.axvline(3005.80,color='r');ax.set(xlabel='BTJD',ylabel='relative SAP',title='Sector 62: red = predicted midpoints');fig.tight_layout();fig.savefig(B/'helper-s62-check.png',dpi=150)
for lo,hi in [(2989,2992.5),(3003.8,3007.5)]:
 mask=(t>lo)&(t<hi);print(lo,hi,'time range',t[mask].min(),t[mask].max(),'n',sum(mask),'maxgap',np.max(np.diff(t[mask])))
(B/'helper-s62-check.json').write_text(json.dumps({'source_sha256':f['sha256'],'prediction_primary':2989.82,'prediction_secondary':3005.80,'note':'Sector 62 primary ingress missing because data begin in flat bottom; secondary centered on red prediction, egress reaches ~3007.2; the detector flag is on egress, not a measured midpoint.'},indent=2))
