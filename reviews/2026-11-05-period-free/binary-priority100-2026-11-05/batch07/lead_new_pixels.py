"""Inspect target-containing pixel flux in newly available sectors.

No low-pixel background estimator is used; zero edge pixels are counted and
the plotted 1x1 and 3x3 sums are deliberately uncorrected.
"""
import csv, hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
rows={r['sample_id']:r for r in csv.DictReader((B/'queue.csv').open())}
out=[]
for sample,sector in [('T064',109),('T070',107),('T070',108)]:
    row=rows[sample];tic=row['tic'];directory=B/tic
    rec=json.loads((directory/f'lead-s{sector}-receipt.json').read_text())
    fp=Path(rec['fits_path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==rec['fits_sha256']
    with fits.open(fp,memmap=False) as h:
        d=h[1].data;t=np.asarray(d['TIME'],float);flux=np.asarray(d['FLUX'],float);quality=np.asarray(d['QUALITY'],int)
        w=WCS(h[2].header)
        x,y=w.all_world2pix(float(row['ra_deg']),float(row['dec_deg']),0)
    ix,iy=int(round(float(x))),int(round(float(y)))
    good=np.isfinite(t)&(quality==0)
    med=np.nanmedian(flux[good],axis=0)
    positives=np.isfinite(med)&(med>0)
    zero_fraction=float(np.mean(med==0))
    ap=[]
    fig,axs=plt.subplots(2,1,figsize=(13,6),gridspec_kw={'height_ratios':[1,2.2]})
    im=axs[0].imshow(med,origin='lower');axs[0].plot(x,y,'rx');fig.colorbar(im,ax=axs[0]);axs[0].set_title(f'{sample} s{sector} median raw pixel map; WCS target x')
    for n in (0,1):
        cube=flux[:,max(0,iy-n):iy+n+1,max(0,ix-n):ix+n+1]
        vals=np.nansum(cube,axis=(1,2))
        ok=good&np.isfinite(vals)&(vals>0)
        if ok.sum()<10:continue
        ap.append(dict(size=2*n+1,median_counts=float(np.median(vals[ok])),min_counts=float(np.min(vals[ok])),max_counts=float(np.max(vals[ok]))))
        axs[1].plot(t[ok],vals[ok]/np.median(vals[ok]),'.',ms=.8,label=f'{2*n+1}x{2*n+1} raw')
    seed=float(row['best_window_btjd']);period=float(row['gaia_period_days'])
    preds=[]
    for n in range(int((np.nanmin(t)-seed)/period)-1,int((np.nanmax(t)-seed)/period)+2):
        p=seed+n*period
        if np.nanmin(t)<p<np.nanmax(t):preds.append(dict(cycle=n,pred_btjd=p));axs[1].axvline(p,color='red',alpha=.4)
    axs[1].legend();axs[1].set_title('Uncorrected target-containing sums; red: Gaia-period screen-phase prediction');axs[1].set_xlabel('BTJD');axs[1].set_ylabel('sum / sector median')
    fig.tight_layout();fig.savefig(directory/f'lead-s{sector}-new-pixels.png',dpi=120);plt.close(fig)
    out.append(dict(sample_id=sample,tic=tic,sector=sector,wcs_target_x=float(x),wcs_target_y=float(y),rounded_x=ix,rounded_y=iy,target_pixel_median=float(med[iy,ix]),median_positive_pixel_count=int(positives.sum()),zero_fraction=zero_fraction,start_btjd=float(np.nanmin(t[good])),end_btjd=float(np.nanmax(t[good])),q0_n=int(good.sum()),apertures=ap,predictions=preds,fits_sha256=rec['fits_sha256']))
    print(sample,sector,round(float(x),2),round(float(y),2),int(good.sum()),preds,flush=True)
(B/'lead-new-pixels.json').write_text(json.dumps(out,indent=2)+'\n')
