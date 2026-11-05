"""Bounded sector-16 source-location check for the repeated F023 eclipse."""
from pathlib import Path
import hashlib,io,json,zipfile
import requests
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;O=B/'286094277';p=O/'lead-tesscut-s016.fits'
if not p.exists():
    r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=dict(ra=310.45886211210404,dec=48.028316545871625,x=11,y=11,units='px',sector=16),timeout=120)
    r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));p.write_bytes(z.read(z.namelist()[0]))
with fits.open(p,memmap=False) as h:
    a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['FLUX'],float);q=np.array(a['QUALITY'],int);w=WCS(h[2].header)
    good=np.isfinite(t)&np.isfinite(f).all(axis=(1,2))&(q==0);t=t[good];f=f[good]
bg=np.median(f[:,[0,0,-1,-1],[0,-1,0,-1]],axis=1);f=f-bg[:,None,None]
tx,ty=w.all_world2pix(310.45886211210404,48.028316545871625,0);tx=float(np.asarray(tx).ravel()[0]);ty=float(np.asarray(ty).ravel()[0])
neighbors=json.loads((B.parent/'shared-catalogues'/'gaia-neighbors.json').read_text(encoding='utf8'))['targets']['F023']
near=[]
for n in neighbors:
    if n['is_queue_gaia_source'] or n['separation_arcsec']>30:continue
    nx,ny=w.all_world2pix(float(n['ra']),float(n['dec']),0)
    near.append(dict(source_id=n['source_id'],g_mag=float(n['phot_g_mean_mag']),separation_arcsec=n['separation_arcsec'],x=float(nx),y=float(ny)))
inside=np.abs(t-1747.38)<.12;outside=(np.abs(t-1747.38)>.3)&(np.abs(t-1747.38)<.75)
o=np.median(f[outside],axis=0);d=o-np.median(f[inside],axis=0)
yy,xx=np.indices(d.shape);clip=np.clip(d,0,None);mask=(xx-tx)**2+(yy-ty)**2<3**2;clip[~mask]=0
cx=float((xx*clip).sum()/clip.sum());cy=float((yy*clip).sum()/clip.sum())
ap=(xx-tx)**2+(yy-ty)**2<1.8**2;flux=f[:,ap].sum(axis=1)
out=dict(sample_id='F023',tic='286094277',sector=16,tesscut_path=str(p.resolve()),tesscut_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),target_xy=[float(tx),float(ty)],nearest_gaia=near,difference_centroid_xy=[cx,cy],difference_offset_pixels=float(np.hypot(cx-tx,cy-ty)),n_inside=int(inside.sum()),n_outside=int(outside.sum()),target_pixel_sky_subtracted_median=float(np.median(f[:,round(ty),round(tx)])),sky_median=float(np.median(bg)),window_btjd=dict(inside=[1747.26,1747.5],outside=[[1746.63,1747.08],[1747.68,1748.13]]),caveat='Single-sector finite-difference location with empirical local baseline, same photons as QLP; centroid sensitive to crowded PSF and detrending.')
(O/'lead-pixels.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
fig,ax=plt.subplots(1,3,figsize=(13,4));ax[0].imshow(o,origin='lower');ax[1].imshow(d,origin='lower');ax[2].plot(t,flux/np.median(flux[outside]),'.',ms=1);ax[2].set_xlim(1746.5,1748.2)
for a in ax[:2]:
    a.plot(tx,ty,'r+',ms=12,label='target');a.plot(cx,cy,'wx',ms=8,label='difference')
    for n in near:
        if n['g_mag']<17:a.plot(n['x'],n['y'],'co',ms=4)
    a.legend(fontsize=7)
fig.tight_layout();fig.savefig(O/'lead-pixels.png',dpi=130);plt.close(fig)
print(json.dumps({k:v for k,v in out.items() if k not in ['nearest_gaia','tesscut_path']},indent=2))
