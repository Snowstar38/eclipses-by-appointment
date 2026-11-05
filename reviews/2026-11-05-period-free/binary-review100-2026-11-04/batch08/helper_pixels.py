from pathlib import Path
import json,csv
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
jobs=[('423569223',101),('393487481',46),('393487481',72),('41859748',104),('41859748',105),('41859748',106),('41859748',107)]
Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())}; out=[]
for tic,s in jobs:
 p=B/tic/f'helper-cutout-s{s:03d}.fits'; h=fits.open(p,memmap=False); a=h[1].data; t=np.array(a['TIME']);q=np.array(a['QUALITY']);f=np.array(a['FLUX'])-np.array(a['FLUX_BKG']);good=np.isfinite(t)&(q==0);t=t[good];f=f[good]; x,y=WCS(h[2].header).all_world2pix(float(Q[tic]['ra_deg']),float(Q[tic]['dec_deg']),0);x,y=float(x),float(y)
 yy,xx=np.indices((11,11)); r=np.sqrt((xx-x)**2+(yy-y)**2); masks=[r<1.5,r<2.5,(r>=3.5)&(r<5)]; labs=['central r<1.5','central r<2.5','outer annulus']
 fig,axs=plt.subplots(3,1,figsize=(12,7),sharex=True); rec={'tic':tic,'sector':s,'target_xy':[x,y],'n':len(t),'start':float(t.min()),'end':float(t.max()),'max_gap':float(np.diff(t).max())}
 for ax,m,label in zip(axs,masks,labs):
  v=np.nansum(f[:,m],axis=1)-np.nanmedian(f[:,r>4],axis=1)*m.sum(); med=np.nanmedian(v); ax.plot(t,v/med,'.',ms=1); ax.set_ylim(.95,1.05); ax.set_ylabel(label); ax.grid();
 axs[-1].set_xlabel('BTJD');fig.suptitle(f'{tic} sector {s} quality=0, tesscut background-subtracted summed flux; target WCS {x:.2f},{y:.2f}');fig.tight_layout();fig.savefig(B/tic/f'helper-pixel-s{s:03d}.png',dpi=110);plt.close(fig);out.append(rec)
(B/'helper-pixel-summary.json').write_text(json.dumps(out,indent=2)+'\n')
