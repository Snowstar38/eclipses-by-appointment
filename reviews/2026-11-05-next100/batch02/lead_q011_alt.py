"""Independent fixed WCS aperture on Tesscut cubes for Q011 representative dips/nulls."""
import hashlib,io,json,zipfile
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent; O=B/'246892556'; cut=O/'cutouts'
receipts=json.loads((cut/'receipts.json').read_text(encoding='utf-8'))
ra,dec=9.002209629788853,-28.267882554400508
events={29:[2089.5918,2096.1545,2109.2588],69:[3184.6399,3191.2002,3197.7466,3204.3092]}
nulls={29:[2092.8707,2105.9851],69:[3201.0311]}
results=[]
for rec in receipts:
    fp=Path(rec['path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==rec['sha256']
    with zipfile.ZipFile(fp) as z:raw=z.read(z.namelist()[0])
    with fits.open(io.BytesIO(raw),memmap=False) as h:
        a=h[1].data;t=np.asarray(a['TIME'],float);cube=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY'],int);w=WCS(h[2].header)
    tx,ty=w.world_to_pixel_values(ra,dec);tx=float(np.asarray(tx).item());ty=float(np.asarray(ty).item())
    xi,yi=round(tx),round(ty);ym,xm=np.indices(cube.shape[1:]);mask=(abs(xm-xi)<=1)&(abs(ym-yi)<=1)
    sky=(xm<2)|(xm>8)|(ym<2)|(ym>8)
    background=np.nanmedian(cube[:,sky],axis=1);flux=np.nansum(cube[:,mask]-background[:,None],axis=1)
    valid=(q==0)&np.isfinite(t)&np.isfinite(flux)&(flux>0);t=t[valid];flux=flux[valid]
    obj=dict(sector=rec['sector'],zip_sha256=rec['sha256'],target_wcs_xy=[tx,ty],aperture_center_xy=[xi,yi],aperture_pixels=int(mask.sum()),median_positive_aperture_e_per_s=float(np.median(flux)),measurements=[])
    for kind,centers in [('event',events[rec['sector']]),('half_step_null',nulls[rec['sector']])]:
        for c in centers:
            x=t-c;core=np.abs(x)<.06;side=(np.abs(x)>.18)&(np.abs(x)<.5);pre=(x>-.5)&(x<-.18);post=(x>.18)&(x<.5)
            coverage=dict(core=int(core.sum()),pre=int(pre.sum()),post=int(post.sum()))
            if min(coverage.values())<4:obj['measurements'].append(dict(kind=kind,center_btjd=c,covered=False,coverage=coverage));continue
            fit=np.polyfit(x[side],flux[side],1);base=np.polyval(fit,x)
            depth=float(np.median((base[core]-flux[core]))/np.median(base[side])*1000)
            scatter=float(1.4826*np.median(abs(flux[side]-base[side]-np.median(flux[side]-base[side])))/np.median(base[side])*1000)
            obj['measurements'].append(dict(kind=kind,center_btjd=c,covered=True,coverage=coverage,loss_ppt=depth,side_mad_ppt=scatter))
    fig,ax=plt.subplots(figsize=(12,3));ax.plot(t,flux/np.median(flux),'.',ms=1)
    for c in events[rec['sector']]:ax.axvline(c,color='C3',lw=.8)
    for c in nulls[rec['sector']]:ax.axvline(c,color='C0',lw=.8)
    ax.set_title(f"Q011 S{rec['sector']} 3x3 sky-subtracted target aperture");ax.set_xlabel('BTJD');ax.set_ylabel('flux / median');fig.tight_layout();fig.savefig(cut/f"s{rec['sector']:03d}-lead-alt-aperture.png",dpi=140);plt.close(fig)
    results.append(obj)
    print(rec['sector'],[(m['kind'],round(m['center_btjd'],3),round(m.get('loss_ppt',float('nan')),2)) for m in obj['measurements']],flush=True)
(cut/'lead-alt-evidence.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
