"""Per-pixel regression on TESScut s089: flux_pix = quadratic trend + a * eclipse template (QLP-fit shape),
+-0.8 d around the primary (3734.1746) and the secondary (3724.368). Amplitude map vs star positions (WCS)."""
import numpy as np, glob, json, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits; from astropy.wcs import WCS
src=open('ecl.py').read(); exec(src[src.index('def trap'):src.index('def nm')])
fn=glob.glob('[local path omitted]')[0]; h=fits.open(fn)
d=h[1].data; t=d['TIME']; F=d['FLUX']; q=d['QUALITY']; w=WCS(h[2].header)
stars=[('target',141.4607833,-36.4630443,11.03),('G14.47',141.4724959,-36.4630394,14.47),('G14.96 31"',None,None,14.96),('G15.74 29"',None,None,15.74)]
gq=json.load(open('gaia.json')) if False else None
out={}
fig,ax=plt.subplots(1,3,figsize=(15,5))
for j,(lab,tc,dep,T14,T12) in enumerate((('pri',3734.1746,0.0505,7.7/24,2.9/24),('sec',3724.368,0.005,8.0/24,3.0/24))):
    g=np.isfinite(t)&(q==0)&(np.abs(t-tc)<0.8)&np.all(np.isfinite(F),axis=(1,2))
    tt=t[g]; FF=F[g]; u=tt-tc; tmpl=1-trap(tt,tc,1.0,T14,T12,200/86400)  # unit-depth dip
    X=np.vstack([np.ones_like(u),u,u*u,-tmpl]).T
    coef=np.linalg.lstsq(X,FF.reshape(len(tt),-1),rcond=None)[0]
    resid=FF.reshape(len(tt),-1)-X@coef; sig=resid.std(0)*np.sqrt(np.linalg.inv(X.T@X)[3,3])
    A=coef[3].reshape(11,11); S=(coef[3]/sig).reshape(11,11); med=np.median(FF,0)
    yy,xx=np.mgrid[:11,:11]; Ap=np.clip(A,0,None)
    cx,cy=(Ap*xx).sum()/Ap.sum(),(Ap*yy).sum()/Ap.sum()
    print(lab,'peak amp pixel',np.unravel_index(np.argmax(A),A.shape),'max S/N',S.max().round(1),'amp-centroid (x,y)',round(cx,2),round(cy,2),
          ' total dip / total flux in 3x3 at peak:', round(A[4:7,4:7].sum()/med[4:7,4:7].sum(),4))
    if j==0:
        im=ax[0].imshow(med,origin='lower'); ax[0].set_title('median image s089')
    ax[j+1].imshow(A,origin='lower'); ax[j+1].set_title(f'{lab} dip amplitude per pixel')
    for k,(nm_,ra,de,gm) in enumerate(stars):
        if ra is None: continue
        px,py=w.all_world2pix(ra,de,0)
        if j==0: print('  ',nm_,'pixel',round(float(px),2),round(float(py),2))
        for a in ax: a.plot(px,py,'r+' if k==0 else 'wx',ms=10)
plt.tight_layout(); plt.savefig('pix_s089.png',dpi=70)
mi=np.median(F[np.isfinite(t)&(q==0)],0); yy,xx=np.mgrid[:11,:11]
print('median-image peak',np.unravel_index(np.argmax(mi),mi.shape))
