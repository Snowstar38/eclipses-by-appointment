import json, hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
b=Path(__file__).parent; out=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for p in sorted(b.glob('*/fresh-pixels/diff_fresh.json')):
 d=json.loads(p.read_text()); tic=d['tic']; m=json.loads((b/tic/'measurements.json').read_text()); g=json.loads((p.parent/'gaia.json').read_text()); sec=d['sector']; cut=Path(f'local-source/sky/data/sb1-scale-c3/vet{tic}/tesscut_s{sec:03}.fits')
 with fits.open(cut,memmap=False) as h:
  t=np.array(h[1].data['TIME'],float); f=np.array(h[1].data['FLUX'],float); q=np.array(h[1].data['QUALITY'],int); w=WCS(h[2].header)
 ok=np.isfinite(t)&np.all(np.isfinite(f.reshape(len(t),-1)),axis=1)&(q==0); t=t[ok];f=f[ok]; flat=f.reshape(len(t),-1); f-=np.array([np.median(np.sort(r)[:int(.4*len(r))]) for r in flat])[:,None,None]
 dur=np.median([e['duration_days'] for e in m['events'] if e.get('timing_usable')]); ds=[]
 for e in d['events']:
  dt=np.abs(t-e['t']); mi=dt<.3*dur; pre=(dt>.75*dur)&(dt<1.75*dur)&(t<e['t']); post=(dt>.75*dur)&(dt<1.75*dur)&(t>e['t']); ds.append(.5*(np.median(f[pre],axis=0)+np.median(f[post],axis=0))-np.median(f[mi],axis=0))
 D=np.mean(ds,axis=0); x,y=d['target_pixel']; targ=float(D[y,x]); n=[]
 for z in d['neighbours_60']:
  if not z['possible']:continue
  x,y=map(lambda a:int(round(a)),z['px']); deficit=float(D[y,x]) if 0<=y<D.shape[0] and 0<=x<D.shape[1] else None
  n.append(dict(source_id=z['source_id'],sep_arcsec=z['sep'],G=z['G'],px=z['px'],pixel_xy=[x,y],deficit_e_per_s=deficit,ratio_to_target_pixel=deficit/targ if deficit is not None else None,required_intrinsic_depth_proxy=z['depth_needed']))
 out.append(dict(tic=tic,sector=sec,target_gaia_source_id=str(g['src'][0]['source_id']),cutout=str(cut),cutout_sha256=sha(cut),gaia_sha256=sha(p.parent/'gaia.json'),fresh_json_sha256=sha(p),target_pixel_xy=d['target_pixel'],target_pixel_deficit_e_per_s=targ,neighbors=n,notes='Pixel values are background-subtracted out-minus-in flux in identical e-/s units; neighboring PSFs overlap and no centroid threshold defines exclusion. Required intrinsic depth is a Gaia G-band flux-ratio proxy only.'))
(b/'terra-pixel-audit.json').write_text(json.dumps(out,indent=2));
for a in out:print(a['tic'],round(a['target_pixel_deficit_e_per_s'],2),[(x['source_id'],round(x['sep_arcsec'],1),round(x['deficit_e_per_s'],2),round(x['ratio_to_target_pixel'],2)) for x in a['neighbors']])
