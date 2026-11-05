import hashlib,json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

here=Path(__file__).resolve().parent
tic='155346713';sec=7
receipt=json.loads((here/'pixel-download-155346713.json').read_text())
path=Path(receipt['fits_path']); assert hashlib.sha256(path.read_bytes()).hexdigest()==receipt['tesscut_fits_sha256']
old=next(r for r in json.loads((here/'downloads-155346713.json').read_text())['products'] if r['sector']==7)
with fits.open(old['path']) as h:
    a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(t>1502.18)&(t<1502.82)
x=t[good];y=f[good]/np.median(f[good])
def model(t,b,s,amp,c,w,k):return b+s*(t-c)-amp*np.clip((w/2-abs(t-c))/k,0,1)
p,cov=curve_fit(model,x,y,p0=[1,0,.06,1502.50,.24,.045],
                bounds=([.8,-.2,0,1502.43,.13,.01],[1.2,.2,.3,1502.56,.4,.12]),maxfev=20000)
center,width,ingress=p[3],p[4],p[5]
with fits.open(path,memmap=False) as h:
    a=h[1].data;tt=np.asarray(a['TIME'],float);ff=np.asarray(a['FLUX'],float);qq=np.asarray(a['QUALITY'],int)
    wcs=WCS(h[2].header)
valid=np.isfinite(tt)&(qq==0)&np.all(np.isfinite(ff),axis=(1,2))&(tt>1502.1)&(tt<1502.9)
tt=tt[valid];ff=ff[valid];xx=tt-center
cadence=float(np.median(np.diff(tt)));offsets=np.linspace(-cadence/2,cadence/2,21)
shape=np.clip((width/2-abs(xx[:,None]+offsets))/ingress,0,1).mean(axis=1)
flat=ff.reshape(len(ff),-1);ncorner=max(1,int(.4*flat.shape[1]))
background=np.median(np.sort(flat,axis=1)[:,:ncorner],axis=1)
corrected=ff-background[:,None,None]
design=np.column_stack((np.ones(len(xx)),xx,xx*xx,-shape))
coef=np.linalg.lstsq(design,corrected.reshape(len(xx),-1),rcond=None)[0]
baseline=coef[0].reshape(ff.shape[1:]);deficit=coef[3].reshape(ff.shape[1:])
resid=corrected.reshape(len(xx),-1)-design@coef
err=(resid.std(axis=0)*math.sqrt(np.linalg.inv(design.T@design)[3,3])).reshape(ff.shape[1:])
stars=json.loads((here/'gaia-stars-155346713.json').read_text())
target=next(v for v in stars if str(v['source_id'])==receipt['gaia_source_id'])
tx,ty=[float(v) for v in wcs.all_world2pix(float(target['ra']),float(target['dec']),0)]
ny,nx=baseline.shape;yy,px=np.mgrid[:ny,:nx];region=(abs(px-tx)<=2.5)&(abs(yy-ty)<=2.5)
def cent(img):
    v=np.clip(img,0,None)*region
    return [float((v*px).sum()/v.sum()),float((v*yy).sum()/v.sum())]
dc=cent(deficit);lc=cent(baseline)
neighbor=[]
for star in stars:
    if str(star['source_id'])==receipt['gaia_source_id']:continue
    ra,dec=float(star['ra']),float(star['dec'])
    sep=3600*math.hypot((ra-float(target['ra']))*math.cos(math.radians(dec)),dec-float(target['dec']))
    sx,sy=[float(v) for v in wcs.all_world2pix(ra,dec,0)]
    g=star.get('phot_g_mean_mag');g=float(g) if g is not None else None
    neighbor.append({'source_id':str(star['source_id']),'sep_arcsec':sep,'G':g,'xy':[sx,sy]})
neighbor.sort(key=lambda r:r['sep_arcsec'])
result={'tic':tic,'sector':sec,'event':'B-like full dip','center_btjd':center,'width_days':width,
        'ingress_days':ingress,'qlp_model_amplitude_ppt':float(p[2]*1000),
        'qlp_realized_depth_ppt':float(p[2]*min(1,width/(2*ingress))*1000),
        'qlp_fit_parameter_covariance':cov.tolist(),'n_cutout_cadences':len(tt),
        'cutout_sha256':receipt['tesscut_fits_sha256'],'target_xy':[tx,ty],
        'deficit_centroid_xy':dc,'light_centroid_xy':lc,
        'deficit_target_offset_arcsec':math.dist(dc,[tx,ty])*21,
        'deficit_light_offset_arcsec':math.dist(dc,lc)*21,
        'neighbor_60arcsec':neighbor,
        'limitation':'Single-sector 30-minute FFI pixel fit. Offset is exploratory, without calibrated localization uncertainty.'}
(here/'pixel-difference-155346713.json').write_text(json.dumps(result,indent=2))
fig,axs=plt.subplots(1,3,figsize=(13,4))
for ax,img,title in zip(axs,(baseline,deficit,deficit/np.where(err>0,err,np.nan)),('baseline','B-like deficit','deficit S/N')):
    im=ax.imshow(img,origin='lower',interpolation='nearest');fig.colorbar(im,ax=ax,fraction=.05)
    ax.plot(tx,ty,'r+',ms=15,mew=2,label='Gaia target')
    for v in neighbor:
        if v['G'] is not None and v['G']<15:
            sx,sy=v['xy'];ax.plot(sx,sy,'wx',ms=6);ax.annotate(f"{v['G']:.1f}",(sx,sy),xytext=(2,2),textcoords='offset points',color='white',fontsize=6)
    ax.set_title(title)
axs[1].plot(*dc,'mo',mfc='none',ms=12,label='deficit centroid');axs[1].plot(*lc,'cs',mfc='none',ms=9,label='light centroid');axs[1].legend(fontsize=7)
fig.suptitle(f'TIC {tic} s7 B-like deficit, target offset {result["deficit_target_offset_arcsec"]:.1f} arcsec')
fig.tight_layout();fig.savefig(here/'pixel-difference-155346713.png',dpi=140)
print(json.dumps({k:result[k] for k in ('center_btjd','qlp_realized_depth_ppt','n_cutout_cadences','deficit_target_offset_arcsec','deficit_light_offset_arcsec')},indent=2))
