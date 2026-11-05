"""Check T028 current/older cutout target flux, aperture light curves and coverage."""
import json,csv,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;row=next(r for r in csv.DictReader((B/'queue.csv').open()) if r['sample_id']=='T025');out=[]
for sector in (86,):
    p=B/row['tic']/f'lead-tesscut-s{sector}.fits';sha=hashlib.sha256(p.read_bytes()).hexdigest()
    with fits.open(p,memmap=False) as h:
        d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['FLUX'],float);q=np.asarray(d['QUALITY'],int);w=WCS(h[2].header)
    tx,ty=w.all_world2pix(float(row['ra_deg']),float(row['dec_deg']),0);yy,xx=np.indices(f.shape[1:]);dist=np.hypot(xx-tx,yy-ty);mask=(np.abs(xx-tx)<=1.5)&(np.abs(yy-ty)<=1.5);bgmask=dist>3
    bg=np.nanmedian(f[:,bgmask],axis=1);a=np.nansum(f[:,mask]-bg[:,None],axis=1);good=np.isfinite(t)&np.isfinite(a)&(a>0)&(q==0)
    base=np.nanmedian(f[good],axis=0)-np.median(bg[good]);target_counts=float(np.sum(base[mask]));total_pos=float(np.sum(np.maximum(base,0)));med=np.median(a[good]);tt=t[good];aa=a[good]/med
    rec=dict(tic=row['tic'],sector=sector,sha256=sha,target_pixel=[float(tx),float(ty)],target_3x3_counts=target_counts,positive_cutout_counts=total_pos,target_fraction_positive=target_counts/total_pos,n_quality0=int(good.sum()),start_btjd=float(tt.min()),end_btjd=float(tt.max()),relative_p1_p50_p99=list(map(float,np.percentile(aa,[1,50,99]))))
    out.append(rec)
    fig,axs=plt.subplots(2,1,figsize=(12,5),gridspec_kw={'height_ratios':[1,2]});axs[0].imshow(base,origin='lower');axs[0].plot(tx,ty,'r+',ms=12);axs[0].set_title(f's{sector} target pixel and baseline');axs[1].plot(tt,aa,'.',ms=1);axs[1].set_ylim(.9,1.1);axs[1].set_xlabel('BTJD');axs[1].set_ylabel('background-subtracted target 3x3');fig.tight_layout();fig.savefig(B/row['tic']/f'lead-cutout-s{sector}.png',dpi=130);plt.close(fig)
    print(rec)
(B/'lead-t025-cutout.json').write_text(json.dumps(out,indent=2)+'\n')

