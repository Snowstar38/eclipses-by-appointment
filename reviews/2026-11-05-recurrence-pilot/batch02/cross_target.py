"""Inspect simultaneous S94 raw SAP across separate queued targets."""
from pathlib import Path
import json,hashlib
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;H=B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'
out=[];fig,ax=plt.subplots(3,1,figsize=(11,7),sharex=True)
for a,(tic,label) in zip(ax,[('149252670','V011'),('344584786','V014'),('31531197','V018')]):
    bulk=json.loads((H/f'{tic}.json').read_text());r=next(r for r in bulk['files'] if r['sector']==94);p=Path(r['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
    with fits.open(p,memmap=False) as h:
        d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int)
    z=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-3874.9)<2);t=t[z];f=f[z]/np.median(f[z]);
    a.plot(t,f,'.',ms=1);a.set_ylabel(label);out.append({'tic':tic,'camera':r['camera'],'ccd':r['ccd'],'source_sha256':r['sha256'],'first_btjd':float(t.min()),'last_btjd':float(t.max()),'largest_gap_days':float(max(np.diff(t)))})
ax[-1].set_xlabel('BTJD');fig.suptitle('S94 same-time trough and gap context, independent CCDs');fig.tight_layout();fig.savefig(B/'cross-target-s94.png',dpi=150);plt.close(fig)
(B/'cross-target.json').write_text(json.dumps({'targets':out,'interpretation':'simultaneous structure is common-mode evidence, not an automatic artifact veto'},indent=2)+'\n')
print(out)
