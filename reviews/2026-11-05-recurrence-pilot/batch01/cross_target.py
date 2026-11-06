"""Compare simultaneous candidate features in independently selected stars."""
from pathlib import Path
import json,hashlib
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
H=B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'
cases={94:['259900992','407622315','234302665'],96:['259900992','234302665']}
out={}
for sector,tics in cases.items():
 fig,ax=plt.subplots(len(tics),1,figsize=(10,2.2*len(tics)),sharex=True,squeeze=False)
 info=[];center=3874.95 if sector==94 else 3926.4
 for a,tic in zip(ax[:,0],tics):
  bulk=json.loads((H/f'{tic}.json').read_text());rec=next(r for r in bulk['files'] if r['sector']==sector)
  path=Path(rec['path']);sha=hashlib.sha256(path.read_bytes()).hexdigest();assert sha==rec['sha256']
  with fits.open(path,memmap=False) as h:
   assert str(int(h[0].header['TICID']))==tic
   d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int)
  z=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-center)<2.5)
  t=t[z];f=f[z];f=f/np.median(f)-1
  a.plot(t-center,f,'.',ms=2);a.set_ylabel(tic)
  info.append({'tic':tic,'sector':sector,'camera':rec['camera'],'ccd':rec['ccd'],'source_sha256':sha,'n_q0':len(t),'first_btjd':float(min(t)),'last_btjd':float(max(t)),'largest_gap_days':float(max(np.diff(t)))})
 ax[0,0].set_title(f'S{sector} raw q0 concurrent features, center {center:.3f} BTJD')
 ax[-1,0].set_xlabel('BTJD minus center (d)')
 fig.tight_layout();fig.savefig(B/f'cross-target-s{sector}.png',dpi=150);plt.close(fig)
 out[str(sector)]=info
(B/'cross-target.json').write_text(json.dumps(out,indent=2)+'\n')
