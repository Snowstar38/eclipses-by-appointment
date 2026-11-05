import csv,json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).parent; bulk=Path('[local-path-redacted]')
res={}
for row in csv.DictReader((B/'queue.csv').open()):
 tic=row['tic']; d=json.loads((bulk/(tic+'.json')).read_text()); flags=[(f,w) for f in d['files'] for w in f['windows'] if w['flag'] and w['kind']=='dip']; res[tic]=[]
 fig,axs=plt.subplots(max(1,len(flags)),1,figsize=(9,max(2.4,2.2*len(flags))),squeeze=False)
 for ax,(f,w) in zip(axs[:,0],flags):
  p=Path(f['path']); sha=hashlib.sha256(p.read_bytes()).hexdigest()
  with fits.open(p,memmap=False) as h:
   hdr=h[0].header; a=h[1].data; t=np.array(a['TIME']); flux=np.array(a['SAP_FLUX']); q=np.array(a['QUALITY']); ok=np.isfinite(t)&np.isfinite(flux)&(flux>0)&(q==0); x=t[ok]; y=flux[ok]; sel=abs(x-w['time'])<3; x=x[sel];y=y[sel]; med=np.median(y); y=y/med
   ax.plot(x,y,'.',ms=1); ax.axvline(w['time'],color='red'); ax.set_title(f"{tic} s{f['sector']} {w['time']:.3f} hdr TIC {hdr.get('TICID',hdr.get('OBJECT'))} hash {sha==f['sha256']}"); ax.grid()
   res[tic].append(dict(sector=f['sector'],time=w['time'],sha256=sha,expected_sha256=f['sha256'],header_tic=str(hdr.get('TICID',hdr.get('OBJECT'))),finite_positive_median=float(med),n=len(x),first=float(x.min()),last=float(x.max()),maxgap=float(np.max(np.diff(x)))))
 fig.tight_layout(); fig.savefig(B/('helper-'+tic+'.png'),dpi=100);plt.close(fig)
(B/'helper-flags.json').write_text(json.dumps(res,indent=2))
