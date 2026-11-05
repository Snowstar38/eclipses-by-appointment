import json,hashlib,csv
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent; neigh=json.loads((B/'../shared-catalogues/gaia-neighbors.json').read_text())['targets']; out=[]
for sid,tid,s,c in [('T026','341688154',48,2633.8706),('T025','219765764',79,3464.7),('T025','219765764',77,None)]:
 p=B/tid/f'helper-tesscut-s{s}.fits'; row=next(r for r in csv.DictReader((B/'queue.csv').open()) if r['tic']==tid)
 with fits.open(p,memmap=False) as h:
  d=h[1].data;t=np.array(d['TIME'],float);f=np.array(d['FLUX'],float);q=np.array(d['QUALITY'],int);w=WCS(h[2].header)
 x,y=w.all_world2pix(float(row['ra_deg']),float(row['dec_deg']),0);x=float(x);y=float(y); yy,xx=np.indices(f.shape[1:]);mask=(abs(xx-round(x))<=1)&(abs(yy-round(y))<=1); bgmask=np.hypot(xx-x,yy-y)>4
 bg=np.nanmedian(f[:,bgmask],axis=1);lc=np.nansum(f[:,mask]-bg[:,None],axis=1); ok=np.isfinite(t)&np.isfinite(lc)&(q==0);t=t[ok];f=f[ok];lc=lc[ok];bg=bg[ok];base=np.nanmedian(f,axis=0)-np.nanmedian(bg); med=np.median(lc)
 rec={'sample':sid,'sector':s,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'target_pixel':[float(x),float(y)],'aperture_median_counts':float(med),'start':float(t.min()),'end':float(t.max()),'cadences':len(t),'positions':[]}
 for n in neigh[sid][:4]:
  nx,ny=w.all_world2pix(float(n['ra']),float(n['dec']),0);rec['positions'].append({'source_id':n['source_id'],'g':n['phot_g_mean_mag'],'pixel':[float(nx),float(ny)]})
 fig,axs=plt.subplots(2,2,figsize=(12,8));axs[0,0].imshow(base,origin='lower');axs[0,0].plot(x,y,'r+');axs[0,0].set_title('median background-subtracted image');axs[0,1].plot(t,lc/med,'.',ms=1);axs[0,1].set_title('3x3 target aperture')
 if c:
  core=(abs(t-c)<(.065 if sid=='T026' else .22));left=(t>c-.4)&(t<c-.18) if sid=='T026' else (t>c-1.2)&(t<c-.6);right=(t>c+.18)&(t<c+.4) if sid=='T026' else (t>c+1)&(t<c+1.5); side=left|right
  diff=np.nanmedian(f[side],axis=0)-np.nanmedian(f[core],axis=0);axs[1,0].imshow(diff,origin='lower',cmap='coolwarm');axs[1,0].plot(x,y,'k+');
  for pos in rec['positions'][:3]:axs[1,0].plot(*pos['pixel'],'x')
  axs[1,0].set_title('side - event; crosses Gaia positions');win=(t>c-2)&(t<c+2);axs[1,1].plot(t[win]-c,lc[win]/med,'.',ms=2);axs[1,1].set_title('local aperture')
  rec.update(core_n=int(core.sum()),side_n=int(side.sum()),core_minus_side_ppt=float(1000*(1-np.median(lc[core])/np.median(lc[side]))),diff_aperture_counts=float(np.sum(diff[mask])),diff_pixels=np.round(diff,3).tolist())
  # Difference centroid within 5x5; background estimated in outer pixels.
  dif=diff-np.median(diff[bgmask]);m=(abs(xx-round(x))<=2)&(abs(yy-round(y))<=2);den=np.sum(dif[m]);rec['diff_centroid']=[float(np.sum(dif[m]*xx[m])/den),float(np.sum(dif[m]*yy[m])/den)]
 fig.tight_layout();fig.savefig(B/tid/f'helper-pixels-s{s}.png',dpi=130);plt.close(fig);out.append(rec);print(json.dumps(rec,indent=2),flush=True)
(B/'helper-pixels.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')

