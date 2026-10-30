from pathlib import Path
import json,numpy as np,urllib.request,urllib.parse,hashlib
from astropy.io import fits
from astropy.wcs import WCS
B=Path(__file__).parent;R=B/'raw-evidence';targets=json.loads((B/'targets-selected.json').read_text());raw=json.loads((R/'raw-events.json').read_text());pixels={x['tic']:x for x in json.loads((R/'pixel-independent-results.json').read_text())}
for tic in ['417917895','162075402']:
 rec=pixels[tic];sec=rec['sector'];T=targets[tic];ep=raw[tic]['representative_ephemeris'];dur=np.median([x['duration_d'] for x in raw[tic]['events'] if 'tc'in x]);uri=next(x[1] for x in T['qlp'] if x[0]==sec);p=R/tic/f'qlp_s{sec:03}.fits'
 if not p.exists():p.write_bytes(urllib.request.urlopen('https://mast.stsci.edu/api/v0.1/Download/file?'+urllib.parse.urlencode({'uri':uri}),timeout=60).read())
 def measure(t,f):
  out=[]
  for e in rec['measurements']:
   dt=t-e['tc'];mi=abs(dt)<.3*dur;pre=(dt<-.75*dur)&(dt>-1.75*dur);post=(dt>.75*dur)&(dt<1.75*dur);base=(np.median(f[pre])+np.median(f[post]))/2
   out.append(dict(tc=e['tc'],depth_core=float(1-np.median(f[mi])/base),depth_deepest3=float(1-np.median(np.sort(f[mi])[:3])/base),core_samples=int(mi.sum()),pre_samples=int(pre.sum()),post_samples=int(post.sum())))
  return out
 with fits.open(p) as h:
  assert str(h[0].header['TICID'])==tic and h[0].header['SECTOR']==sec
  a=h[1].data;m=(a['QUALITY']==0)&np.isfinite(a['SAP_FLUX'])&np.isfinite(a['TIME']);qlp=measure(a['TIME'][m],a['SAP_FLUX'][m])
 with fits.open(rec['source_path']) as h:
  a=h[1].data;F=np.array(a['FLUX']);t=np.array(a['TIME']);m=(a['QUALITY']==0)&np.isfinite(t)&np.all(np.isfinite(F.reshape(len(t),-1)),axis=1);F=F[m];t=t[m];bg=np.median(np.sort(F.reshape(len(t),-1),axis=1)[:,:int(.4*F.shape[1]*F.shape[2])],axis=1);x,y=WCS(h[2].header).all_world2pix(float(T['gaia']['ra']),float(T['gaia']['dec']),0);ix,iy=round(float(x)),round(float(y));aps={}
  for half in [0,1,2]:
   f=F[:,iy-half:iy+half+1,ix-half:ix+half+1].sum(axis=(1,2))-(2*half+1)**2*bg;aps[f'{2*half+1}x{2*half+1}']=measure(t,f)
 result=dict(tic=tic,sector=sec,qlp_uri=uri,qlp_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),pixel_source_path=rec['source_path'],pixel_sha256=rec['sha256'],qlp_same_epoch=qlp,pixel_same_epoch=aps,primary_period=ep['period_d'],duration_d=float(dur),note='Same event epochs and core-median estimator; background lower40percent pixels; apertures vary. Descriptive depth sanity, no uncertainty or dilution model.')
 (B/f'depth-sanity-{tic}.json').write_text(json.dumps(result,indent=2));print(tic,qlp,aps)
