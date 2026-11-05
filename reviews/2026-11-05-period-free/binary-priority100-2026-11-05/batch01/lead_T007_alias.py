"""Test the shared middle prediction of competing T007 shallow-event integer aliases."""
import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;m=json.loads((B/'142761762'/'lead-numeric.json').read_text())
src=next(x for x in m['sources'] if x['sector']==61);fp=Path(src['path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==src['sha256']
with fits.open(fp,memmap=False) as h:
 a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
sel=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[sel];f=f[sel];cad=float(np.median(np.diff(t)))
first=1499.5882;last=3715.7806; pred=first+(last-first)*2/3
dt=t-pred;core=np.abs(dt)<.8;left=(dt>=-3)&(dt< -1.5);right=(dt>1.5)&(dt<=3);local=np.abs(dt)<5
base=np.median(np.r_[f[left],f[right]]);noise=1.4826*np.median(abs(np.r_[f[left],f[right]]/base-1))*1000
rec=dict(tic='142761762',source_sha256=src['sha256'],first_shallow_btjd=first,last_shallow_btjd=last,predicted_s61_btjd=pred,assumption='If S7 and S88 broad shallow dips are same kind and S34 is approximately one-third baseline, all 18/19/20-cycle assignments predict this S61 occasion at two-thirds baseline.',quality0_core_n=int(sum(core)),quality0_left_n=int(sum(left)),quality0_right_n=int(sum(right)),expected_core_n=1.6/cad,core_first_btjd=float(t[core].min()),core_last_btjd=float(t[core].max()),core_max_gap_days=float(np.max(np.diff(t[core]))),core_median_deficit_ppt=float((1-np.median(f[core])/base)*1000),side_scatter_ppt=float(noise))
(B/'142761762'/'lead-alias.json').write_text(json.dumps(rec,indent=2)+'\n')
plt.figure(figsize=(9,4));plt.plot(dt[local],f[local]/base,'.',ms=2);plt.axvspan(-.8,.8,color='orange',alpha=.2);plt.xlabel('days from predicted S61 shallow event');plt.ylabel('raw SAP / side');plt.title(f'T007 S61 predicted {pred:.3f}, core deficit {rec["core_median_deficit_ppt"]:.2f} ppt');plt.tight_layout();plt.savefig(B/'142761762'/'lead-alias.png',dpi=125)
print(json.dumps(rec,indent=2))
