import zipfile,hashlib,json,csv,io
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
stars=list(csv.DictReader(open(B/'helper-q029-gaia.csv')))
timing=json.loads((B/'168657537/lead-timing.json').read_text())['aliases_by_late_epoch_cycle_offset']['0']; p=timing['period_days']; ep=timing['epoch_btjd']
fig,axs=plt.subplots(1,3,figsize=(15,5)); out={}
for ax,s in zip(axs,[4,5,31]):
 path=B/f'helper-q029-s{s}.zip'; z=zipfile.ZipFile(path); h=fits.open(io.BytesIO(z.read(z.namelist()[0]))); a=h[1].data; t=np.array(a['TIME']); f=np.array(a['FLUX']); q=np.array(a['QUALITY']); w=WCS(h[2].header)
 phase=(t-ep+p/2)%p-p/2; cyc=np.rint((t-ep)/p).astype(int); ok=np.isfinite(t)&(q==0); on=ok&(abs(phase)<.045); off=ok&(abs(phase)>.09)&(abs(phase)<.20)
 # local per-cycle median baseline minimizes slow variation
 diffs=[]; parity=[]
 for c in np.unique(cyc[on]):
  i=on&(cyc==c); o=off&(cyc==c)
  if i.sum()>=2 and o.sum()>=2:
   diffs.append(np.nanmedian(f[o],axis=0)-np.nanmedian(f[i],axis=0)); parity.append(int(c%2))
 d=np.nanmedian(diffs,axis=0); xy=w.all_world2pix([[float(x['ra']),float(x['dec'])] for x in stars],0); target=xy[0]; yy,xx=np.indices(d.shape); win=(xx-target[0])**2+(yy-target[1])**2<16; pos=np.clip(d,0,None)*win; cent=[float((pos*xx).sum()/pos.sum()),float((pos*yy).sum()/pos.sum())]; peak=np.unravel_index(np.nanargmax(np.where(win,d,np.nan)),d.shape)
 ax.imshow(d,origin='lower',cmap='RdBu_r',vmin=-np.nanmax(abs(d[win])),vmax=np.nanmax(abs(d[win]))); ax.scatter(xy[:,0],xy[:,1],s=[max(15,180*10**(-.4*(float(x['phot_g_mean_mag'])-8.728))) for x in stars],facecolors='none',edgecolors='lime'); ax.scatter(*cent,c='yellow',marker='+'); ax.set_title(f'S{s} loss; {len(diffs)} cycles'); ax.set_xlim(2,12);ax.set_ylim(2,12)
 nearest=[]
 for st,pt in zip(stars,xy):
  dist=float(np.linalg.norm(pt-target));
  if dist<5: nearest.append(dict(id=st['source_id'],g=float(st['phot_g_mean_mag']),xy=list(map(float,pt)),separation_pixels=dist))
 out[str(s)]=dict(zip_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),n_cycles=len(diffs),target_xy=list(map(float,target)),positive_loss_centroid_xy=cent,peak_xy=[int(peak[1]),int(peak[0])],nearest=nearest,parity_count=[parity.count(0),parity.count(1)])
fig.tight_layout();fig.savefig(B/'helper-q029-difference.png',dpi=180)
(B/'helper-q029-difference.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
