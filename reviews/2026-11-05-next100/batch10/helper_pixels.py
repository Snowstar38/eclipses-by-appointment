"""Reproducible WCS difference images and simple positive-flux aperture checks."""
import csv, hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
rows={r['tic']:r for r in csv.DictReader((B/'queue.csv').open(encoding='utf8'))}
# In/out intervals are deliberately narrow local controls, not fitted eclipse centers.
jobs=[('3299934',62,(2999.96,3000.20),[(2999.40,2999.60),(3000.55,3000.75)]),
      ('3299934',89,(3735.92,3736.15),[(3735.36,3735.56),(3736.50,3736.70)]),
      ('311461544',101,(4112.08,4112.23),[(4111.40,4111.60),(4112.66,4112.86)]),
      ('47675509',86,(3637.48,3637.63),[(3636.95,3637.13),(3638.25,3638.43)]),
      ('447274265',93,(3849.78,3849.91),[(3849.42,3849.62),(3850.14,3850.34)])]
out=[]
for tic,sec,inside,outer in jobs:
    p=B/tic/f'helper-tesscut-s{sec}.fits'; hsh=hashlib.sha256(p.read_bytes()).hexdigest()
    with fits.open(p,memmap=False) as h:
        a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY'],int);w=WCS(h[2].header)
    x,y=w.all_world2pix(float(rows[tic]['ra_deg']),float(rows[tic]['dec_deg']),0);x=float(x);y=float(y)
    good=np.isfinite(t)&(q==0)
    ii=good&(t>=inside[0])&(t<=inside[1]);oo=good&np.logical_or.reduce([(t>=lo)&(t<=hi) for lo,hi in outer]);
    assert ii.sum()>=3 and oo.sum()>=3,(tic,sec,ii.sum(),oo.sum())
    fin=np.nanmedian(f[ii],axis=0);fout=np.nanmedian(f[oo],axis=0);diff=fout-fin
    yy,xx=np.indices(diff.shape);ap=(abs(xx-round(x))<=1)&(abs(yy-round(y))<=1)
    border=(xx<2)|(xx>8)|(yy<2)|(yy>8);bg=float(np.nanmedian(diff[border]));
    sky=float(np.nanmedian(fout[border]));raw_ap=float(np.nansum(fout[ap]-sky));
    deficit=float(np.nansum(diff[ap]-bg));depth=deficit/raw_ap if raw_ap>0 else None
    # Positive-difference centroid only over the central 7x7 pixels.
    pos=np.maximum(diff-bg,0);pos[border]=0
    cen=[float(np.nansum(pos*xx)/np.nansum(pos)),float(np.nansum(pos*yy)/np.nansum(pos))] if np.nansum(pos)>0 else None
    peak=np.unravel_index(np.nanargmax(diff[2:9,2:9]),(7,7));peakxy=[int(peak[1]+2),int(peak[0]+2)]
    np.savetxt(B/tic/f'helper-diff-s{sec}.csv',diff,delimiter=',')
    fig,ax=plt.subplots(figsize=(5,4.5)); im=ax.imshow(diff-bg,origin='lower',cmap='RdBu_r',vmin=-np.nanmax(abs(diff-bg)),vmax=np.nanmax(abs(diff-bg)))
    ax.plot(x,y,'kx',ms=10,label='target');ax.plot(cen[0],cen[1],'wo',mec='k',label='deficit centroid') if cen else None
    ax.plot(*peakxy,'y+',ms=11,label='peak');ax.legend(fontsize=7);fig.colorbar(im,ax=ax,label='outside - inside, e-/s');fig.tight_layout();fig.savefig(B/tic/f'helper-diff-s{sec}.png',dpi=150);plt.close(fig)
    rec=dict(tic=tic,sector=sec,source_sha256=hsh,target_xy=[float(x),float(y)],inside=inside,outer=outer,inside_cadences=int(ii.sum()),outer_cadences=int(oo.sum()),target_aperture_outside_sky_subtracted_flux=raw_ap,target_aperture_deficit=deficit,aperture_depth_fraction=depth,deficit_centroid_xy=cen,peak_xy=peakxy,peak_deficit=float(diff[peakxy[1],peakxy[0]]),background_difference=bg)
    out.append(rec);print(tic,sec,'depth',depth,'target',x,y,'centroid',cen,'peak',peakxy)
(B/'helper-pixels.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
