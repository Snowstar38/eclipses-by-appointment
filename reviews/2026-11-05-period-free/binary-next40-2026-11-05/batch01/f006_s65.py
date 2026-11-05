"""Bounded newer S65 target-centered TESSCut check for F006 conditional repeat."""
import csv,hashlib,io,json,zipfile
from pathlib import Path
import requests,numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;r=next(x for x in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf8')) if x['sample_id']=='F006')
p=B/'f006-s65-tesscut.fits';receipt={'sample_id':'F006','sector':65,'prediction_btjd':3057.805+39.44,'note':'Conditional P from S64/S100/S101; same TESS photons as any other S65 extraction.'}
if not p.exists():
 v=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':r['ra_deg'],'dec':r['dec_deg'],'x':11,'y':11,'units':'px','sector':65},timeout=180);receipt.update(url=v.url,status=v.status_code,raw_sha256=hashlib.sha256(v.content).hexdigest());v.raise_for_status();z=zipfile.ZipFile(io.BytesIO(v.content));p.write_bytes(z.read(z.namelist()[0]))
receipt['fits_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
with fits.open(p,memmap=False) as hd:
 a=hd[1].data;t=np.asarray(a['TIME'],float);q=np.asarray(a['QUALITY'],int);cube=np.asarray(a['FLUX'],float)
 # Explicit centered 3x3, constant border sky; require positive finite target sum.
 target=np.nansum(cube[:,4:7,4:7],axis=(1,2));border=np.ones((11,11),bool);border[2:9,2:9]=False;sky=np.nanmedian(cube[:,border],axis=1);f=target-9*sky
ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok];f=f/np.median(f)
receipt.update(n_quality0_positive=int(len(t)),first_btjd=float(t.min()),last_btjd=float(t.max()),median_target_sum=float(np.median(target)),median_sky=float(np.median(sky)))
mid=receipt['prediction_btjd'];m=abs(t-mid)<4;core=abs(t-mid)<.8;left=(t>mid-3)&(t<mid-1.5);right=(t>mid+1.5)&(t<mid+3)
receipt.update(prediction_core_n=int(core.sum()),left_n=int(left.sum()),right_n=int(right.sum()),first_core_btjd=float(t[core].min()) if core.any() else None,last_core_btjd=float(t[core].max()) if core.any() else None,max_core_gap_days=float(np.diff(t[core]).max()) if core.sum()>1 else None)
if left.sum()>10 and right.sum()>10 and core.any():
 base=np.median(np.r_[f[left],f[right]]);receipt['core_depth_ppt']=float((base-np.median(f[core]))/base*1000)
fig,ax=plt.subplots(2,1,figsize=(11,6));ax[0].plot(t,f,'.',ms=1);ax[0].axvline(mid,color='r');ax[1].plot(t[m]-mid,f[m],'.',ms=2);ax[1].axvspan(-.8,.8,color='r',alpha=.1);fig.tight_layout();fig.savefig(B/'f006-s65.png',dpi=140)
(B/'f006-s65.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf8');print(receipt)
