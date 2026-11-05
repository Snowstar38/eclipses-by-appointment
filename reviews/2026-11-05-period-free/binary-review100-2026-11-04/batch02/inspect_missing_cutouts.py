"""Inspect available missing-sector TESSCut pixels using a local aperture."""
import csv, hashlib, json, math
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS

B=Path(__file__).resolve().parent
rows={r['tic']:r for r in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8'))}
seeds={'231694897':(3875.114,57.96837228122208),'323818250':(1603.95,58.65080398491257)}
for tic in seeds:
    output=[]
    for fp in sorted((B/tic).glob('missing-cutout-s*.fits')):
        with fits.open(fp,memmap=False) as h:
            a=h[1].data;w=WCS(h[2].header)
            x0,y0=w.world_to_pixel_values(float(rows[tic]['ra_deg']),float(rows[tic]['dec_deg']))
            flux=np.asarray(a['FLUX'],float)
            time=np.asarray(a['TIME'],float);q=np.asarray(a['QUALITY'],int)
        yy,xx=np.indices(flux.shape[1:]); aperture=(abs(xx-x0)<=1.5)&(abs(yy-y0)<=1.5)
        outer=((xx-x0)**2+(yy-y0)**2>=16)
        # TESSCut FLUX_BKG is identically zero in these files. Use a local
        # outer-pixel median; several sectors contain only near-zero noise
        # at the nominal WCS target and cannot form a meaningful light curve.
        phot=np.nansum(flux[:,aperture]-np.nanmedian(flux[:,outer],axis=1)[:,None],axis=1)
        good=np.isfinite(time)&np.isfinite(phot)&(q==0)
        t=time[good];counts=phot[good];baseline=float(np.median(counts));usable=baseline>100
        f=counts/baseline if usable else counts
        seed,period=seeds[tic];n0=math.floor((min(t)-seed)/period)-1;n1=math.ceil((max(t)-seed)/period)+1
        predictions=[seed+n*period for n in range(n0,n1+1) if min(t)-1<=seed+n*period<=max(t)+1]
        near=[]
        for center in predictions:
            core=abs(t-center)<.3;side=(abs(t-center)>.7)&(abs(t-center)<1.8)
            near.append({'predicted_btjd':center,'n_core':int(sum(core)),'n_side':int(sum(side)),
                         'core_side_delta_ppt':float(1000*(np.median(f[core])-np.median(f[side]))) if usable and sum(core)>3 and sum(side)>8 else None,
                         'closest_cadence_days':float(min(abs(t-center)))})
        fig,ax=plt.subplots(figsize=(10,3));ax.scatter(t,f,s=1,alpha=.55)
        for x in predictions:ax.axvline(x,color='r',lw=.8)
        ax.set_title(f'TIC {tic} {fp.stem}: TESSCut 3x3 local-background aperture, quality 0')
        ax.set_xlabel('BTJD');ax.set_ylabel('relative flux' if usable else 'net counts (no target detected)');fig.tight_layout()
        plot=fp.with_suffix('.png');fig.savefig(plot,dpi=130);plt.close(fig)
        output.append({'path':str(fp),'sha256':hashlib.sha256(fp.read_bytes()).hexdigest(),
                       'target_pixel_0_based':[float(x0),float(y0)],'aperture_pixels':int(sum(aperture.ravel())),
                       'quality_zero_samples':len(t),'time_start':float(min(t)),'time_end':float(max(t)),
                       'median_net_counts':baseline,'target_measurable':usable,
                       'cadence_days':float(np.median(np.diff(t))),
                       'relative_flux_mad_ppt':float(1482.6*np.median(abs(f-np.median(f)))) if usable else None,
                       'predictions_from_screened_event_and_gaia_period':near,
                       'plot':str(plot)})
        print(tic,fp.name,'n',len(t),'pred',near)
    (B/tic/'missing-cutout-review.json').write_text(json.dumps({'tic':tic,'files':output,
        'caution':'Target-centered TESSCut aperture uses calibrated pixel FLUX minus a local outer-pixel median. Near-zero target net counts mark unusable sectors, not nulls. Predictions from one screened event and Gaia period are conditional and are not measured eclipse centers.'},indent=2)+'\n')
