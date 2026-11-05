import csv,json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;D=B/'295743311';q=next(x for x in csv.DictReader((B/'queue.csv').open()) if x['tic']=='295743311')
fold=json.loads((D/'fold-inspection.json').read_text())['fold_trials'];out={}
for sector in (87,108):
 p=D/f's{sector}-tesscut.fits';rec=json.loads((D/f's{sector}-tesscut-receipt.json').read_text());assert hashlib.sha256(p.read_bytes()).hexdigest()==rec['fits_sha256']
 with fits.open(p,memmap=False) as h:
  a=h[1].data;w=WCS(h[2].header);x,y=w.all_world2pix(float(q['ra_deg']),float(q['dec_deg']),0)
  t=np.asarray(a['TIME'],float);cube=np.asarray(a['FLUX'],float);quality=np.asarray(a['QUALITY'],int)
 good=np.isfinite(t)&(quality==0)&np.isfinite(cube).all(axis=(1,2));t=t[good];cube=cube[good]
 yy,xx=np.indices(cube.shape[1:]);bg=np.median(np.sort(cube.reshape(len(cube),-1),axis=1)[:,:12],axis=1)
 f={}
 for radius in (1,2):
  mask=(abs(xx-x)<=radius)&(abs(yy-y)<=radius)
  v=np.sum(cube[:,mask]-bg[:,None],axis=1);f[f'ap{radius}']=v/np.median(v)
 fig,axes=plt.subplots(3,1,figsize=(10,7),sharex=False)
 for ax,(k,v) in zip(axes[:2],f.items()):
  ax.plot(t,v,'.',ms=2);ax.set_ylabel(k)
  for typ,color in [('P','red'),('P2','purple')]:
   tr=fold[typ];n=np.arange(-200,300);pred=tr['t0']+n*tr['P']
   for m in pred[(pred>t.min())&(pred<t.max())]:ax.axvline(m,color=color,lw=.7)
 axes[2].imshow(np.median(cube,axis=0),origin='lower');axes[2].plot(x,y,'r+',ms=15)
 axes[2].set_title(f'target WCS ({x:.2f}, {y:.2f})');fig.suptitle(f'TIC 295743311 s{sector} TESSCut')
 fig.tight_layout();fig.savefig(D/f's{sector}-aperture.png',dpi=120);plt.close(fig)
 preds=[]
 for typ in ('P','P2'):
  tr=fold[typ];n=np.arange(-200,300);ps=tr['t0']+n*tr['P']
  for pred in ps[(ps>t.min())&(ps<t.max())]:
   m=abs(t-pred)<.16;side=(abs(t-pred)>.6)&(abs(t-pred)<1.2)
   preds.append({'trial':typ,'predicted_btjd':float(pred),'n_core':int(m.sum()),'n_side':int(side.sum()),'ap1_core_delta_ppt':float(1000*(np.median(f['ap1'][m])/np.median(f['ap1'][side])-1)) if m.sum() and side.sum() else None,'ap2_core_delta_ppt':float(1000*(np.median(f['ap2'][m])/np.median(f['ap2'][side])-1)) if m.sum() and side.sum() else None})
 out[str(sector)]={'fits_sha256':rec['fits_sha256'],'wcs_target_xy':[float(x),float(y)],'n_quality0':len(t),'time_span':[float(t.min()),float(t.max())],'predictions':preds}
(D/'cutout-check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
