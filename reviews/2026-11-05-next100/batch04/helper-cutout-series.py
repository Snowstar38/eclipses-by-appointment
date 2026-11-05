"""Same-photon TESSCut sky-corrected aperture curves, preserving Q036 source ambiguity."""
import io,json,zipfile
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
pix=json.loads((B/'helper-pixels.json').read_text())
out=[]
for r in pix:
    if r['sample_id']!='Q036':continue
    sec=r['sector'];center=r['center_btjd'];sid=r['sample_id']
    with zipfile.ZipFile(B/f'helper-{sid}-s{sec:03d}.zip') as z:raw=z.read(z.namelist()[0])
    with fits.open(io.BytesIO(raw),memmap=False) as h:
        a=h[1].data;t=np.asarray(a['TIME'],float);F=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY'],int);w=WCS(h[2].header)
    valid=(q==0)&np.isfinite(t)&np.all(np.isfinite(F),axis=(1,2))
    yy,xx=np.indices(F.shape[1:]); sky=((xx<2)|(xx>8))&((yy<2)|(yy>8))
    bg=np.median(F[:,sky],axis=1);S=F-bg[:,None,None]
    sources=[s for s in r['sources'] if s['is_target'] or (s['G_flux_ratio']>.01 and s['distance_arcsec']<45)]
    side=valid&(np.abs(t-center)>.25)&(np.abs(t-center)<.7)
    core=valid&(np.abs(t-center)<(.05 if sec==18 else .045))
    # Fit every pixel's local time trend; spatial difference on sky-corrected frames.
    side_x=t[side]-center
    pixel_slope=np.tensordot(side_x-side_x.mean(),S[side]-S[side].mean(axis=0),axes=(0,0))/np.sum((side_x-side_x.mean())**2)
    pixel_at_center=S[side].mean(axis=0)-pixel_slope*side_x.mean()
    diff=pixel_at_center-np.median(S[core],axis=0)
    target=next(s for s in sources if s['is_target'])
    local=(xx-target['x'])**2+(yy-target['y'])**2<3**2
    weights=np.maximum(diff,0)*local
    spatial=dict(peak_yx=list(map(int,np.unravel_index(np.argmax(diff),diff.shape))),
                 difference_centroid_xy=[float((weights*xx).sum()/weights.sum()),float((weights*yy).sum()/weights.sum())] if weights.sum()>0 else None,
                 target_pixel_difference=float(diff[round(target['y']),round(target['x'])]),
                 peak_difference=float(np.max(diff)))
    neighbor=next(s for s in sources if abs(s['G']-15.339438)<.001)
    # Disjoint rows along the target-neighbor axis, using a common x stripe.
    xstripe=np.abs(xx-round(target['x']))<=1
    target_only=xstripe&(yy>=round(target['y'])-1)&(yy<=round(target['y']))
    neighbor_only=xstripe&(yy>=round(neighbor['y']))&(yy<=round(neighbor['y'])+1)
    spatial['disjoint_masks']={'target_side_yx':np.argwhere(target_only).tolist(),
                               'neighbor_side_yx':np.argwhere(neighbor_only).tolist(),
                               'target_side_difference_e_s':float(diff[target_only].sum()),
                               'neighbor_side_difference_e_s':float(diff[neighbor_only].sum()),
                               'target_side_baseline_e_s':float(pixel_at_center[target_only].sum()),
                               'neighbor_side_baseline_e_s':float(pixel_at_center[neighbor_only].sum())}
    fig2,ax2=plt.subplots(figsize=(5,4));im=ax2.imshow(diff,origin='lower',cmap='RdBu_r');fig2.colorbar(im,ax=ax2)
    for s in sources: ax2.plot(s['x'],s['y'],'r+' if s['is_target'] else 'cx',ms=9)
    ax2.set_title(f'{sid} S{sec} local sky+trend difference');fig2.tight_layout();fig2.savefig(B/f'helper-Q036-s{sec:03d}-local-difference.png',dpi=130);plt.close(fig2)
    curves=[];fig,ax=plt.subplots(figsize=(10,4))
    for s in sources:
        x,y=s['x'],s['y'];mask=(np.abs(xx-round(x))<=1)&(np.abs(yy-round(y))<=1)
        flux=S[:,mask].sum(axis=1)
        # Local linear baseline from both sides of event, with full actual time retained.
        if side.sum()<6 or core.sum()<2: continue
        coef=np.polyfit(t[side]-center,flux[side],1)
        pred=np.polyval(coef,t-center)
        loss=1000*np.median((pred[core]-flux[core])/np.median(pred[side]))
        curves.append(dict(source_id=s['source_id'],is_target=s['is_target'],G=s['G'],xy=[x,y],
                           median_sky_corrected_ap3=float(np.median(flux[valid])),loss_ppt=float(loss),
                           n_core=int(core.sum()),n_side=int(side.sum()),baseline_slope_e_s_day=float(coef[0])))
        local=valid&(np.abs(t-center)<.7)
        ax.plot(t[local]-center,1000*(flux[local]/pred[local]-1),'.',ms=2,label=f"G{s['G']:.1f} {'target' if s['is_target'] else 'neighbor'}")
    ax.axvline(0,color='k',lw=.5);ax.legend(fontsize=7);ax.set_xlabel('BTJD minus QLP screen center');ax.set_ylabel('local detrended aperture ppt');fig.tight_layout()
    fig.savefig(B/f'helper-Q036-s{sec:03d}-apertures.png',dpi=130);plt.close(fig)
    out.append(dict(sector=sec,center_btjd=center,method='3x3 integer-centered sky-subtracted, linear sideband trend, core |dt|<0.05 S18/<0.045 S85; same TESS photons',curves=curves,spatial=spatial))
    print(sec,[(x['G'],x['is_target'],round(x['loss_ppt'],2)) for x in curves])
(B/'helper-Q036-cutout-series.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
