import csv,json,zipfile,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent; root=B.parent; rows={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())}; out=[]; hashes={}
for tic in ['246892556','352610732']:
 row=rows[tic]; bulk=root.parent/'binary-exploration-2026-11-04'/'bulk-results'/f'{tic}.json'; d=json.loads(bulk.read_text()); hashes[str(bulk)]=hashlib.sha256(bulk.read_bytes()).hexdigest()
 for zpath in sorted((B/tic/'cutouts').glob('*.zip')):
  hashes[str(zpath)]=hashlib.sha256(zpath.read_bytes()).hexdigest(); sec=int(zpath.stem[1:]); item=next(x for x in d['files'] if x['sector']==sec); events=[w['time'] for w in item['windows'] if w['flag'] and w['kind']=='dip'];
  with zipfile.ZipFile(zpath) as z, z.open(z.namelist()[0]) as f, fits.open(f,memmap=False) as h:
   a=h[1].data;t=np.array(a['TIME']);q=np.array(a['QUALITY']);cube=np.array(a['FLUX'],float);x,y=map(float,WCS(h[2].header).world_to_pixel_values(float(row['ra_deg']),float(row['dec_deg'])))
  ok=np.isfinite(t)&(q==0); core=np.zeros(len(t),bool); side=core.copy(); width=.06 if tic=='246892556' else .20
  for e in events:
   core|=abs(t-e)<width;side|=(abs(t-e)>width*1.8)&(abs(t-e)<width*3.2)
  core &= ok;side &=ok; med=np.nanmedian(cube[side],axis=0); diff=med-np.nanmedian(cube[core],axis=0)
  yy,xx=np.indices(diff.shape); positive=np.maximum(diff,0); sel=(abs(xx-x)<=3)&(abs(yy-y)<=3); s=positive[sel].sum(); cx=(positive[sel]*xx[sel]).sum()/s;cy=(positive[sel]*yy[sel]).sum()/s
  ix,iy=round(x),round(y); m=(abs(xx-ix)<=1)&(abs(yy-iy)<=1); base=med[m].sum();delta=diff[m].sum(); entry=dict(tic=tic,sector=sec,events=events,core_count=int(core.sum()),side_count=int(side.sum()),target_xy=[x,y],positive_difference_centroid_xy=[cx,cy],centroid_offset_pixels=float(np.hypot(cx-x,cy-y)),center3x3_baseline=float(base),center3x3_difference=float(delta),center3x3_depth_ppt=float(1000*delta/base));out.append(entry)
  fig,axes=plt.subplots(1,2,figsize=(9,4));
  for ax,img,title in zip(axes,[med,diff],['side median','side minus event']):
   im=ax.imshow(img,origin='lower');ax.plot(x,y,'r+',ms=10);ax.set_title(title);fig.colorbar(im,ax=ax)
  fig.suptitle(f'TIC {tic} S{sec}  + target WCS');fig.tight_layout();fig.savefig(B/f'helper-{tic}-s{sec:03d}-pixels.png',dpi=130);plt.close(fig)
(B/'helper-numeric.json').write_text(json.dumps(out,indent=2)+'\n');(B/'helper-source-hashes.json').write_text(json.dumps(hashes,indent=2)+'\n');print(json.dumps(out,indent=2))
