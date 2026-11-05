"""Bounded newest-sector check for N008; target-centered cutout, actual footprint/coverage."""
from pathlib import Path
import requests,zipfile,io,csv,json,hashlib
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent; r=next(x for x in csv.DictReader((B/'queue.csv').open()) if x['sample_id']=='N008')
p=B/r['tic']/'s105-tesscut.fits'; url='https://mast.stsci.edu/tesscut/api/v0.1/astrocut';params={'ra':r['ra_deg'],'dec':r['dec_deg'],'x':11,'y':11,'units':'px','sector':105}
rec={'tic':r['tic'],'sector':105,'request_url':requests.Request('GET',url,params=params).prepare().url}
if not p.exists():
 v=requests.get(url,params=params,timeout=120);rec['http_status']=v.status_code;v.raise_for_status();z=zipfile.ZipFile(io.BytesIO(v.content));p.write_bytes(z.read(z.namelist()[0]))
rec['fits_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
with fits.open(p,memmap=False) as h:
 d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['FLUX'],float);q=np.asarray(d['QUALITY'],int);w=WCS(h[2].header)
tx,ty=map(float,w.all_world2pix(float(r['ra_deg']),float(r['dec_deg']),0));yy,xx=np.indices(f.shape[1:]);mask=(abs(xx-round(tx))<=1)&(abs(yy-round(ty))<=1)
good=np.isfinite(t)&(q==0)&np.isfinite(f).all(axis=(1,2))
t=t[good];f=f[good];q=q[good]
bg=np.median(np.sort(f.reshape(len(f),-1),axis=1)[:,:40],axis=1)
flux=(f-bg[:,None,None])[:,mask].sum(axis=1)
rec.update(target_pixel=[float(tx),float(ty)],mask_pixels=int(mask.sum()),time_min=float(t.min()),time_max=float(t.max()),n=len(t),positive_fraction=float(np.mean(flux>0)),median_target_flux=float(np.median(flux)),max_gap_days=float(np.max(np.diff(t))))
fig,ax=plt.subplots(figsize=(12,4));ax.plot(t,flux,'.',ms=1);ax.set_title('N008 S105 target-centered 3x3 raw TESSCut, q0');ax.set_xlabel('BTJD');fig.tight_layout();fig.savefig(B/r['tic']/'s105-raw.png',dpi=150);plt.close(fig)
fig,ax=plt.subplots(figsize=(10,4));sel=abs(t-4217.35)<2.5;ax.plot(t[sel],flux[sel],'.',ms=2);ax.set_title('N008 S105 dip detail, target-centered 3x3 raw TESSCut q0');ax.set_xlabel('BTJD');fig.tight_layout();fig.savefig(B/r['tic']/'s105-event.png',dpi=150);plt.close(fig)
for k in range(16,25):
 P=(3131.710-2046.070)/k; n=round((np.median(t)-2046.070)/P); mid=2046.070+n*P;core=abs(t-mid)<.48;pre=(t>mid-1.8)&(t<mid-.75);post=(t>mid+.75)&(t<mid+1.8)
 if sum(core):
  baseline=np.median(np.r_[flux[pre],flux[post]]) if sum(pre)+sum(post)>10 else None
  depth=1000*(1-np.median(flux[core])/baseline) if baseline and baseline>0 else None
 else:depth=None
 rec.setdefault('aliases',[]).append({'k':k,'period_days':P,'cycle':int(n),'predicted_mid':mid,'core_n':int(sum(core)),'pre_n':int(sum(pre)),'post_n':int(sum(post)),'core_depth_ppt':depth})
(B/r['tic']/'s105-check.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec,indent=2))
