import json,csv
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;Q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())}
for e in json.loads((B/'helper-fetch.json').read_text()):
 t0=e['time'];tic=e['tic'];fp=B/f'helper-{tic}-tesscut.fits'
 if not fp.exists():continue
 with fits.open(fp,memmap=False) as h:
  t=np.asarray(h[1].data['TIME'],float);f=np.asarray(h[1].data['FLUX'],float);q=np.asarray(h[1].data['QUALITY'],int);w=WCS(h[2].header)
 tx,ty=w.all_world2pix(float(Q[tic]['ra_deg']),float(Q[tic]['dec_deg']),0);yy,xx=np.indices(f.shape[1:]);mask=(abs(xx-round(float(tx)))<=1)&(abs(yy-round(float(ty)))<=1);sky=(xx<2)|(xx>8)|(yy<2)|(yy>8);v=np.sum(f[:,mask],axis=1)-9*np.median(f[:,sky],axis=1);g=(q==0)&np.isfinite(t)&np.isfinite(v)&(v>0)&(abs(t-t0)<max(3*e['duration'],1));
 fig,ax=plt.subplots(figsize=(9,3));ax.plot(t[g],v[g]/np.median(v[g]),'.',ms=1);ax.axvline(t0,c='r',lw=.7);ax.set_title(f'{Q[tic]["sample_id"]} S{e["sector"]} 3x3 minus sky, quality 0');ax.set_xlabel('BTJD');fig.tight_layout();fig.savefig(B/f'helper-{tic}-time.png',dpi=100);plt.close(fig)

