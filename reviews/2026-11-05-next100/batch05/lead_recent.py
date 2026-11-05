"""Check later TESSCut sectors omitted from the original QLP cache."""
import csv,hashlib,io,json,zipfile
from pathlib import Path
import numpy as np
import requests
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
Q={r['sample_id']:r for r in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf8'))}
EVENTS=[('Q046',103),('Q047',104),('Q050',109)]
out=[]
for sid,sector in EVENTS:
 r=Q[sid];args=dict(ra=float(r['ra_deg']),dec=float(r['dec_deg']),x=11,y=11,sector=sector)
 response=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=args,timeout=120);response.raise_for_status();z=response.content
 zp=B/f'lead-{sid}-s{sector:03d}-recent.zip';zp.write_bytes(z)
 with zipfile.ZipFile(io.BytesIO(z)) as arc:raw=arc.read(arc.namelist()[0])
 with fits.open(io.BytesIO(raw),memmap=False) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);F=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY'],int);w=WCS(h[2].header)
 tx,ty=w.world_to_pixel_values(float(r['ra_deg']),float(r['dec_deg']))
 tx=float(np.asarray(tx).reshape(-1)[0]);ty=float(np.asarray(ty).reshape(-1)[0])
 yy,xx=np.indices(F.shape[1:]);ap=(np.abs(xx-round(tx))<=1)&(np.abs(yy-round(ty))<=1)
 border=(xx<2)|(xx>8)|(yy<2)|(yy>8)
 sky=np.nanmedian(np.where(F[:,border]>0,F[:,border],np.nan),axis=1)
 flux=np.sum(F[:,ap],axis=1)-sky*ap.sum();target=F[:,round(ty),round(tx)]-sky
 good=np.isfinite(t)&(q==0)&np.isfinite(flux)&(flux>0)&np.isfinite(sky)&np.isfinite(target)&(target>0)
 t=t[good];flux=flux[good]
 rec=dict(sample_id=sid,tic=r['tic'],sector=sector,url=response.url,zip_sha256=hashlib.sha256(z).hexdigest(),zip_bytes=len(z),target_xy=[float(tx),float(ty)],good_count=len(t),time_start_btjd=float(t.min()) if len(t) else None,time_end_btjd=float(t.max()) if len(t) else None,median_flux=float(np.median(flux)) if len(t) else None)
 if len(t):
  bins=np.floor((t-t.min())/.05).astype(int);ids,inv=np.unique(bins,return_inverse=True)
  bt=np.array([np.median(t[inv==i]) for i in range(len(ids))]);bf=np.array([np.median(flux[inv==i]) for i in range(len(ids))]);
  fig,ax=plt.subplots(figsize=(13,3));ax.plot(bt,bf/np.median(bf),'.',ms=2);ax.set(xlabel='BTJD',ylabel='3x3 sky-subtracted flux / median',title=f'{sid} TESSCut S{sector}');fig.tight_layout();fig.savefig(B/f'lead-{sid}-s{sector:03d}-recent.png',dpi=130);plt.close(fig)
  np.savez_compressed(B/f'lead-{sid}-s{sector:03d}-recent.npz',time_btjd=t,ap3_sky_subtracted_flux=flux)
 out.append(rec);print(sid,sector,rec['good_count'],rec['time_start_btjd'],rec['time_end_btjd'],flush=True)
(B/'lead-recent.json').write_text(json.dumps(out,indent=2)+'\n')
