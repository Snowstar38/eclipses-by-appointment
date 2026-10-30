import json,pathlib,hashlib,numpy as np
from astropy.io import fits
from astropy.wcs import WCS
R=pathlib.Path(__file__).parent; targets=json.load(open(R.parent/'targets-selected.json')); raw=json.load(open(R/'raw-events.json')); out=[]
for tic,r in raw.items():
 try:
  files=list(pathlib.Path(f'[local working path omitted; see provenance receipts]').glob('tesscut_s*.fits')); assert len(files)==1; p=files[0]; sec=int(p.stem[-3:]); T=targets[tic]; ep=r['representative_ephemeris']; dur=np.median([e['duration_d'] for e in r['events'] if 'tc' in e and not e['edge']]); assert ep
  with fits.open(p) as h:
   H=h[0].header;d=h[1].data;w=WCS(h[2].header); x,y=w.all_world2pix(float(T['gaia']['ra']),float(T['gaia']['dec']),0);t=np.array(d['TIME']);F=np.array(d['FLUX']);q=np.array(d['QUALITY']); assert H['SECTOR']==sec and 1<=x<F.shape[2]-1 and 1<=y<F.shape[1]-1;ix,iy=round(float(x)),round(float(y));valid=np.isfinite(t)&np.all(np.isfinite(F.reshape(len(t),-1)),axis=1)&(q==0);t=t[valid];F=F[valid];bg=np.median(np.sort(F.reshape(len(t),-1),axis=1)[:,:int(.4*F.shape[1]*F.shape[2])],axis=1);f=F[:,iy-1:iy+2,ix-1:ix+2].sum(axis=(1,2))-9*bg;rows=[]
   for n in range(int(np.ceil((t.min()-ep['epoch_btjd'])/ep['period_d'])),int(np.floor((t.max()-ep['epoch_btjd'])/ep['period_d']))+1):
    tc=ep['epoch_btjd']+n*ep['period_d']; dt=t-tc; mi=abs(dt)<.3*dur; pre=(dt<-.75*dur)&(dt>-1.75*dur);post=(dt>.75*dur)&(dt<1.75*dur)
    if min(mi.sum(),pre.sum(),post.sum())>=2:
     baseline=(np.median(f[pre])+np.median(f[post]))/2;rows.append(dict(tc=float(tc),depth=float(1-np.median(f[mi])/baseline),n_in=int(mi.sum()),n_pre=int(pre.sum()),n_post=int(post.sum())))
  result=dict(tic=tic,sector=sec,provenance='Independent TESScut pixel aperture extraction',source_path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),identity=dict(header_sector=H['SECTOR'],target_xy=[float(x),float(y)],target_coordinate_source='Gaia target coordinate projected through cutout WCS'),measurements=rows,note='3x3 target aperture, per-cadence faint-pixel background; core medians versus local pre/post baseline; same TESS images, independent extraction, depth not model corrected; event centers use QLP-derived period and cycle counts')
  if not rows: result['error']='No events with adequate in/out samples'
 except Exception as e: result=dict(tic=tic,error=str(e))
 out.append(result);print(tic,result,flush=True)
json.dump(out,open(R/'pixel-independent-results.json','w'),indent=2)
