"""Per-pixel eclipse template fits in one bounded TESScut sector per target."""
import csv,hashlib,json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

here=Path(__file__).resolve().parent
rows=list(csv.DictReader((here/'queue.csv').open()))
sectors={'24668377':98,'150465032':61,'331650047':79,
         '384744604':101,'109560492':88}
for row in rows:
    tic=row['tic'];sector=sectors[tic];d=here/tic/'pixels'
    fits_path=d/f'tesscut_s{sector:03d}.fits'
    receipts=json.loads((here/'pixel-download-receipts.json').read_text())
    retries=json.loads((here/'pixel-retries.json').read_text())
    known=[v['tesscut_fits_sha256'] for v in receipts if v['tic']==tic and v.get('tesscut_fits_sha256')]
    known += [a['fits_sha256'] for v in retries if v['tic']==tic for a in v['attempts'] if a.get('ok')]
    assert hashlib.sha256(fits_path.read_bytes()).hexdigest() in known
    events=json.loads((here/tic/'measurements.json').read_text())['events']
    ev=next(e for e in events if e.get('timing_usable') and e['sector']==sector and
            e['kind']==('B' if tic=='109560492' else 'A'))
    stars=json.loads((d/'gaia-stars.json').read_text())
    target=next(v for v in stars if str(v['source_id'])==row['gaia_dr3_source_id'])
    center=ev['mid_btjd'];p=ev['fit_parameters'];width=p[4];ingress=p[5]
    with fits.open(fits_path,memmap=False) as h:
        a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['FLUX'],float)
        q=np.array(a['QUALITY'],int);wcs=WCS(h[2].header)
    valid=np.isfinite(t)&(q==0)&np.all(np.isfinite(f),axis=(1,2))&(abs(t-center)<max(1.,3*width))
    t=t[valid];f=f[valid];x=t-center
    assert len(t)>50
    # Integrate the fitted eclipse template across the FFI exposure.
    cadence=float(np.median(np.diff(t)));offsets=np.linspace(-cadence/2,cadence/2,21)
    z=abs(x[:,None]+offsets)
    shape=np.clip((width/2-z)/ingress,0,1).mean(axis=1)
    flat=f.reshape(len(f),-1);ncorner=max(1,int(.4*flat.shape[1]))
    background=np.median(np.sort(flat,axis=1)[:,:ncorner],axis=1)
    corrected=f-background[:,None,None]
    design=np.column_stack((np.ones(len(x)),x,x*x,-shape))
    coef=np.linalg.lstsq(design,corrected.reshape(len(x),-1),rcond=None)[0]
    baseline=coef[0].reshape(f.shape[1:]);deficit=coef[3].reshape(f.shape[1:])
    residual=corrected.reshape(len(x),-1)-design@coef
    err=(residual.std(axis=0)*math.sqrt(np.linalg.inv(design.T@design)[3,3])).reshape(f.shape[1:])
    tx,ty=[float(v) for v in wcs.all_world2pix(float(target['ra']),float(target['dec']),0)]
    ny,nx=baseline.shape;yy,xx=np.mgrid[:ny,:nx]
    # Compare the eclipse deficit and out-of-eclipse light in the same
    # 5x5 target region; distant neighbors are assessed at their own pixels.
    region=(abs(xx-tx)<=2.5)&(abs(yy-ty)<=2.5)
    def cent(img):
        v=np.clip(img,0,None)*region
        return [float((v*xx).sum()/v.sum()),float((v*yy).sum()/v.sum())]
    dc=cent(deficit);lc=cent(baseline)
    neighbor=[]
    for star in stars:
        if str(star['source_id'])==row['gaia_dr3_source_id']:continue
        ra=float(star['ra']);dec=float(star['dec']);sep=3600*math.hypot((ra-float(target['ra']))*math.cos(math.radians(dec)),dec-float(target['dec']))
        px,py=[float(v) for v in wcs.all_world2pix(ra,dec,0)];ix,iy=round(px),round(py)
        gm=star.get('phot_g_mean_mag');g=float(gm) if gm is not None else None
        dg=g-float(target['phot_g_mean_mag']) if g is not None else None
        required=ev['depth_ppt']/1000*(1+10**(.4*dg)) if dg is not None else None
        pix_loss=float(deficit[iy,ix]/baseline[iy,ix]) if 0<=ix<nx and 0<=iy<ny and baseline[iy,ix]>0 else None
        neighbor.append(dict(source_id=str(star['source_id']),sep_arcsec=sep,G=g,
                             delta_G=dg,xy=[float(px),float(py)],
                             target_plus_neighbor_required_intrinsic_depth=required,
                             feasible_under_two_star_G_approximation=bool(required is not None and required<=1),
                             local_pixel_fractional_loss=pix_loss))
    neighbor.sort(key=lambda v:v['sep_arcsec'])
    result=dict(tic=tic,sector=sector,event_kind=ev['kind'],center_btjd=center,n_cadences=len(t),
        cutout_sha256=hashlib.sha256(fits_path.read_bytes()).hexdigest(),
        target_xy=[float(tx),float(ty)],deficit_centroid_xy=dc,light_centroid_xy=lc,
        deficit_light_offset_arcsec=float(math.dist(dc,lc)*21),
        deficit_target_offset_arcsec=float(math.dist(dc,[float(tx),float(ty)])*21),
        target_center_pixel_fractional_loss=float(deficit[round(ty),round(tx)]/baseline[round(ty),round(tx)]),
        neighbor_60arcsec=neighbor,
        limitation='Single-sector pixel template from same TESS FFI photons. G-band two-star depth feasibility is approximate; compare PSF/centroid and each capable neighbor, not its intrinsic fraction with diluted target pixel loss.')
    (d/'pixel-difference.json').write_text(json.dumps(result,indent=2))
    fig,axs=plt.subplots(1,3,figsize=(13,4))
    for ax,img,title in zip(axs,[baseline,deficit,deficit/np.where(err>0,err,np.nan)],['baseline','eclipse deficit','deficit S/N']):
        im=ax.imshow(img,origin='lower',interpolation='nearest');fig.colorbar(im,ax=ax,fraction=.05)
        ax.plot(tx,ty,'r+',ms=15,mew=2,label='Gaia target')
        for v in neighbor:
            if v['G'] is not None and (v['G']<16 or v['feasible_under_two_star_G_approximation']):
                px,py=v['xy'];ax.plot(px,py,'wx',ms=6);ax.annotate(f"{v['G']:.1f}",(px,py),xytext=(2,2),textcoords='offset points',color='white',fontsize=6)
        ax.set_title(title)
    axs[1].plot(*dc,'mo',mfc='none',ms=12,label='deficit centroid')
    axs[1].plot(*lc,'cs',mfc='none',ms=9,label='light centroid')
    axs[1].legend(fontsize=7)
    fig.suptitle(f'TIC {tic} s{sector} {ev["kind"]}; deficit-light offset {result["deficit_light_offset_arcsec"]:.1f} arcsec')
    fig.tight_layout();fig.savefig(d/'pixel-difference.png',dpi=130);plt.close(fig)
    print(tic,len(t),round(result['deficit_light_offset_arcsec'],2),round(result['deficit_target_offset_arcsec'],2),
          sum(v['feasible_under_two_star_G_approximation'] for v in neighbor),flush=True)
