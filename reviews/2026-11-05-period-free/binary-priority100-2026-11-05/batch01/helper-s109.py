import json,csv,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg');import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;q={r['tic']:r for r in csv.DictReader((B/'queue.csv').open())};out=[]
for tic in ['37647565','271782868']:
 p=B/f'helper-{tic}-s109.fits';row=q[tic]
 with fits.open(p,memmap=False) as h:
  t=np.asarray(h[1].data['TIME'],float);f=np.asarray(h[1].data['FLUX'],float);qual=np.asarray(h[1].data['QUALITY'],int);w=WCS(h[2].header)
 good=np.isfinite(t)&(qual==0);t=t[good];f=f[good];tx,ty=map(float,w.all_world2pix(float(row['ra_deg']),float(row['dec_deg']),0));yy,xx=np.indices(f.shape[1:]);mask=(abs(xx-round(tx))<=1)&(abs(yy-round(ty))<=1);bg=np.nanmedian(np.sort(f.reshape(len(f),-1),axis=1)[:,:40],axis=1);flux=np.nansum(f[:,mask],axis=1)-bg*np.isfinite(f[:,mask]).sum(axis=1);o={'tic':tic,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'target_pixel':[tx,ty],'n':len(t),'time_range':[float(t.min()),float(t.max())],'median_target_ap3_bgsub':float(np.median(flux)),'median_bg_pixel':float(np.median(bg)),'normalized_p01_p99':[float(z) for z in np.percentile(flux/np.median(flux),[1,99])],'max_gap_days':float(np.max(np.diff(t)))};out.append(o)
 fig,axs=plt.subplots(1,2,figsize=(12,4));axs[0].imshow(np.nanmedian(f,axis=0),origin='lower');axs[0].plot(tx,ty,'r+');axs[1].plot(t,flux,'.',ms=1);axs[1].set_title('background-subtracted target 3x3');fig.suptitle(f'{tic} sector 109');fig.tight_layout();fig.savefig(B/f'helper-{tic}-s109.png',dpi=130);plt.close(fig);print(o)
(B/'helper-s109.json').write_text(json.dumps(out,indent=2))

