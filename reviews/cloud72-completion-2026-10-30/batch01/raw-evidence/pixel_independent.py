import json,pathlib,hashlib,numpy as np
from astropy.io import fits
from astropy.wcs import WCS
r=pathlib.Path(__file__).parent;T=json.load(open(r.parent/'targets-selected.json'));raw=json.load(open(r/'raw-events.json'));DL=json.load(open(r/'tesscut-downloads.json'));out=[]
for d in DL:
 tic=d['tic'];sec=d['sector'];p=r/tic/d['members'][0];target=T[tic];ev=[e for e in raw[tic]['events'] if e['sector']==sec and 'tc' in e and not e['edge'] and e['depth']>3*e['residual_rms']];res=dict(tic=tic,sector=sec,file=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),events=[])
 try:
  with fits.open(p,memmap=False) as h:
   res['sector_header']=h[0].header.get('SECTOR'); a=h[1].data;t=np.asarray(a['TIME'],float);F=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY']); w=WCS(h[2].header);tx,ty=w.all_world2pix(target['ra'],target['dec'],0); res['target_px']=[float(tx),float(ty)];res['position_check_arcsec']=float(np.hypot(tx-5,ty-5)*21);res['sector_matches']=res['sector_header']==sec
  ok=np.isfinite(t)&np.all(np.isfinite(F.reshape(len(t),-1)),axis=1)&(q==0);t=t[ok];F=F[ok];F=F-np.median(np.sort(F.reshape(len(t),-1),axis=1)[:,:48],axis=1)[:,None,None];ds=[];os=[]
  for e in ev:
   x=t-e['tc'];D=e['duration_d'];i=abs(x)<.3*D;pre=(x<-.75*D)&(x> -1.75*D);post=(x>.75*D)&(x<1.75*D)
   if min(i.sum(),pre.sum(),post.sum())<2:continue
   O=(np.median(F[pre],axis=0)+np.median(F[post],axis=0))/2;Z=O-np.median(F[i],axis=0);os.append(O);ds.append(Z);res['events'].append(dict(tc=e['tc'],duration_d=D,n_in=int(i.sum()),n_pre=int(pre.sum()),n_post=int(post.sum())))
  if not ds:raise ValueError('insufficient in/out coverage')
  O=np.mean(os,axis=0);Z=np.mean(ds,axis=0);yy,xx=np.mgrid[:11,:11];ix=int(round(float(tx)));iy=int(round(float(ty)));m=(abs(xx-ix)<=2)&(abs(yy-iy)<=2);v=np.clip(Z,0,None)*m;dx=(v*xx).sum()/v.sum();dy=(v*yy).sum()/v.sum();res['deficit_centroid_px']=[float(dx),float(dy)];res['centroid_offset_arcsec']=float(np.hypot(dx-tx,dy-ty)*21);res['peak_px']=list(map(int,np.unravel_index(np.argmax(Z),Z.shape)[::-1]));res['depth_3x3']=float(Z[iy-1:iy+2,ix-1:ix+2].sum()/O[iy-1:iy+2,ix-1:ix+2].sum());res['note']='positive-clipped centroid within 5x5 biases noisy deficits toward center; no astrometric uncertainty; shared TESS photons, independent aperture extraction'
  np.savez_compressed(r/tic/f'pixel_s{sec:03d}.npz',out=O,deficit=Z)
 except Exception as e:res['error']=repr(e)
 out.append(res)
json.dump(out,open(r/'pixel-results.json','w'),indent=2);print([(x['tic'],x['sector'],round(x.get('centroid_offset_arcsec',0),1),round(x.get('depth_3x3',0),4),x.get('error')) for x in out])

