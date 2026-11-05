"""Compare independent F010 raw occasions after a local linear side-band baseline."""
from pathlib import Path
import json,hashlib
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;H=B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'
bulk=json.loads((H/'458324895.json').read_text());centers={12:1649.352,39:2377.495,66:3105.497,93:3833.891};out=[]
fig,ax=plt.subplots(figsize=(9,5))
for rec in bulk['files']:
 s=int(rec['sector'])
 if s not in centers:continue
 p=Path(rec['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==rec['sha256']
 with fits.open(p,memmap=False) as hd:
  a=hd[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
 ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok];x=t-centers[s]
 near=abs(x)<3;side=near&(abs(x)>1.4);core=near&(abs(x)<.45)
 assert side.sum()>30 and core.sum()>10
 co=np.polyfit(x[side],f[side],1);base=np.polyval(co,x);y=f/base
 depth=(1-np.median(y[core]))*1000
 left=near&(x<-1.4);right=near&(x>1.4)
 out.append({'sector':s,'center_btjd_provisional':centers[s],'source_sha256':rec['sha256'],'side_left_n':int(left.sum()),'side_right_n':int(right.sum()),'core_n':int(core.sum()),'core_depth_ppt_local_linear':float(depth),'core_first_btjd':float(t[core].min()),'core_last_btjd':float(t[core].max()),'max_core_gap_days':float(np.max(np.diff(t[core]))),'caveat':'Center and local baseline are provisional; broad asymmetric variability affects fitted depth.'})
 ax.plot(x[near],y[near],'.',ms=1,label=f'S{s} {depth:.1f} ppt')
ax.set(xlabel='BTJD offset from provisional center (d)',ylabel='SAP / local linear baseline',title='F010 separate broad raw occasions');ax.set_xlim(-3,3);ax.legend();fig.tight_layout();fig.savefig(B/'f010-overlay.png',dpi=140)
(B/'f010-overlay.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(out)
