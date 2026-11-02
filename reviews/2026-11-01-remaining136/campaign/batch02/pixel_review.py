"""Fresh bounded TESScut reductions. Historical windows are guides, never timings."""
import csv,json,math,hashlib,shutil
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).parent;SB=Path('local-source/Fable 5/made/sb1-scale');TG=json.load(open(B.parent/'targets-selected.json'));out={};hashes={}
for r in csv.DictReader(open(B/'queue.csv')):
 tic=r['tic'];D=B/tic;src=next((SB/'diffimg'/tic).glob('diff_s*.json'));old=json.load(open(src));m=json.load(open(D/'measurements.json'));cut=Path(f'local-source/sky/data/sb1-scale-c3/vet{tic}/tesscut_s{old["sector"]:03}.fits');ga=src.parent/'gaia.json';hist=D/'historical';hist.mkdir(exist_ok=True)
 for p in [src,src.with_suffix('.png'),ga,cut]:
  hashes[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
  if p!=cut:shutil.copy2(p,hist/p.name)
 with fits.open(cut,memmap=False) as h:
  a=h[1].data;t=np.array(a['TIME'],float);F=np.array(a['FLUX'],float);q=np.array(a['QUALITY']);w=WCS(h[2].header);ra,dec=w.all_pix2world(*old['target_px'],0)
 target=json.load(open(ga))['src'][0];assert str(target['source_id'])==str(TG[tic]['gaia']['source_id'])
 coorderr=float(np.hypot((ra-float(target['ra']))*np.cos(np.deg2rad(dec)),dec-float(target['dec']))*3600);assert coorderr<1
 ok=np.isfinite(t)&np.all(np.isfinite(F.reshape(len(t),-1)),axis=1)&(q==0);t=t[ok];F=F[ok];flat=F.reshape(len(t),-1);bg=np.array([np.median(np.sort(z)[:int(.4*len(z))]) for z in flat]);F-=bg[:,None,None]
 yy,xx=np.mgrid[:F.shape[1],:F.shape[2]];tx,ty=old['target_px'];ix,iy=round(tx),round(ty);mask=(abs(xx-ix)<=2)&(abs(yy-iy)<=2);dur=float(np.median([e['duration_days'] for e in m['events'] if e.get('timing_usable')]));events=[];deficits=[]
 for e in old['events']:
  tp=e['t'];dt=abs(t-tp);mi=dt<.25*dur;pre=(t<tp-.75*dur)&(t>tp-1.75*dur);post=(t>tp+.75*dur)&(t<tp+1.75*dur)
  if min(sum(mi),sum(pre),sum(post))<3:continue
  fi=np.median(F[mi],axis=0);fo=(np.median(F[pre],axis=0)+np.median(F[post],axis=0))/2;dif=fo-fi;weight=np.clip(dif,0,None)*mask;cen=[float((weight*xx).sum()/weight.sum()),float((weight*yy).sum()/weight.sum())];ap={}
  for radius in [0,1,2]:
   am=(abs(xx-ix)<=radius)&(abs(yy-iy)<=radius);ap[str(2*radius+1)]=float(dif[am].sum()/fo[am].sum()*1000)
  events.append(dict(historical_cycle=e['cycle'],window_center_btjd=tp,n_in=int(sum(mi)),n_pre=int(sum(pre)),n_post=int(sum(post)),centroid_px=cen,target_distance_px=math.dist(cen,[tx,ty]),aperture_depths_ppt=ap));deficits.append(dif)
 assert events
 stack=np.mean(deficits,axis=0);fig,axs=plt.subplots(1,2,figsize=(10,4));axs[0].imshow(stack,origin='lower');axs[1].imshow(stack,origin='lower');axs[1].set_xlim(tx-3,tx+3);axs[1].set_ylim(ty-3,ty+3)
 capable=[n for n in old['neighbours_60'] if n['possible']]
 for ax in axs:
  ax.plot(tx,ty,'r+',ms=12)
  for n in capable:ax.plot(*n['px'],'wx');ax.annotate(n['source_id'][-5:],n['px'],color='white',fontsize=6)
 fig.suptitle(f'TIC {tic} S{old["sector"]}: recomputed deficits; red target, white capable neighbors');fig.tight_layout();fig.savefig(D/'pixel-recomputed.png',dpi=140);plt.close(fig)
 centers=np.array([e['centroid_px'] for e in events]);cen=centers.mean(axis=0)
 out[tic]=dict(identity=dict(gaia_source_id=str(target['source_id']),coordinate_error_arcsec=coorderr),sector=old['sector'],target_px=old['target_px'],duration_days=dur,events=events,mean_centroid_px=cen.tolist(),event_scatter_px=centers.std(axis=0,ddof=1).tolist() if len(events)>1 else None,target_distance_px=math.dist(cen,[tx,ty]),capable=[dict(source_id=n['source_id'],separation_arcsec=n['sep'],G=n['G'],intrinsic_required_fraction=n['depth_needed'],pixel_position=n['px'],distance_to_deficit_px=math.dist(cen,n['px'])) for n in capable],method='Quality-zero raw TESScut flux; per-cadence low40% median background; in |dt|<0.25 measured duration, separate symmetric out baselines0.75–1.75duration; positive-deficit centroid in target5x5; event scatter descriptive, not calibrated localization error. Aperture depths use signed deficit. Same TESS photons as QLP, independent extraction not independent observing occasions.')
 (D/'pixel-evidence.json').write_text(json.dumps(out[tic],indent=2));print(tic,'events',len(events),'target',round(out[tic]['target_distance_px'],3),'neighbors',[(round(n['separation_arcsec'],1),round(n['distance_to_deficit_px'],3)) for n in out[tic]['capable']],flush=True)
(B/'pixel-audit.json').write_text(json.dumps(out,indent=2));(B/'source-hashes.json').write_text(json.dumps(hashes,indent=2))
