import json,pathlib,numpy as np,hashlib
from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
import astropy.units as u
r=pathlib.Path(__file__).parent; T=json.load(open(r.parent/'targets-selected.json'));rows=json.load(open(r/'pixel-results.json'));dl=json.load(open(r/'tesscut-downloads.json'));out=[];ind=[]
for row in rows:
 tic=row['tic'];sec=row['sector']; d=next(z for z in dl if z['tic']==tic and z['sector']==sec);p=r/tic/d['members'][0];target=T[tic]
 with fits.open(p,memmap=False) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);F=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY']);w=WCS(h[2].header);tx,ty=w.all_world2pix(target['ra'],target['dec'],0)
 good=np.isfinite(t)&(q==0)&np.all(np.isfinite(F.reshape(len(t),-1)),axis=1);t=t[good];F=F[good];back=np.median(np.sort(F.reshape(len(t),-1),axis=1)[:,:48],axis=1);yy,xx=np.mgrid[:11,:11]; mask=(abs(xx-tx)<=1)&(abs(yy-ty)<=1);flux=F[:,mask].sum(axis=1)-mask.sum()*back; np.savez_compressed(r/tic/f'independent_s{sec:03d}.npz',time=t,flux=flux,background=back,quality_filter='QUALITY=0',aperture=mask)
 ind.append(dict(tic=tic,sector=sec,file=f'{tic}/independent_s{sec:03d}.npz',n=len(t),note='Custom 3x3-like target-centred aperture, per-cadence median faintest 48 pixels background; independent reduction using same TESS FFI photons, not independent observations.'))
 cone=json.load(open(r/tic/'tic-cone.json'))['data']; tr=next((x for x in cone if str(x['ID'])==tic),None);tm=tr.get('Tmag') if tr else None;depth=abs(row.get('depth_3x3',0));c=[]
 for x in cone:
  if str(x['ID'])==tic or not all(x.get(k) is not None for k in ('ra','dec','Tmag')) or tm is None:continue
  sep=SkyCoord(target['ra']*u.deg,target['dec']*u.deg).separation(SkyCoord(x['ra']*u.deg,x['dec']*u.deg)).arcsec; ratio=10**(-.4*(x['Tmag']-tm));need=depth*(1+ratio)/ratio
  if need<=1 and sep<=60:
   px=w.all_world2pix(x['ra'],x['dec'],0);c.append(dict(tic=x['ID'],Tmag=x['Tmag'],separation_arcsec=float(sep),depth_needed=float(need),px=[float(v) for v in px]))
 out.append(dict(tic=tic,sector=sec,depth_3x3=depth,capable_neighbours=c,note='TIC cone within 60 arcsec; ideal brightness-based limit neglects aperture throughput, uncatalogued sources and bandpass uncertainty; zero depth means no valid event and does not imply capability.'))
json.dump(out,open(r/'neighbour-results.json','w'),indent=2);json.dump(ind,open(r/'independent-extraction.json','w'),indent=2)
