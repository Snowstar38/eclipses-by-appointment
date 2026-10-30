# TESScut pixel test: per-pixel amplitude of the dominant photometric frequency; which source does it sit on?
# usage: s4_pixels.py <tic> <sector> <period_of_signal_days>
import sys, os, numpy as np, csv, glob, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,'[local path omitted]')
from common import *
from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
import astropy.units as u
from scipy.optimize import least_squares
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
tic,sector,Psig=sys.argv[1],int(sys.argv[2]),float(sys.argv[3])
T=targets()[tic]; ra,dec=float(T['tic_ra']),float(T['tic_dec'])
d=f'{D}/{tic}/tesscut'; os.makedirs(d,exist_ok=True)
fn=glob.glob(f'{d}/*s{sector:04d}*.fits')
if not fn:
    from astroquery.mast import Tesscut
    Tesscut.download_cutouts(coordinates=SkyCoord(ra,dec,unit='deg'),size=11,sector=sector,path=d)
    fn=glob.glob(f'{d}/**/*s{sector:04d}*.fits',recursive=True)
fn=fn[0] if isinstance(fn,list) else fn
h=fits.open(fn); dat=h[1].data; w=WCS(h[2].header)
tt=dat['TIME']; fl=dat['FLUX']; q=dat['QUALITY']
m=(q==0)&np.isfinite(tt)&np.all(np.isfinite(fl.reshape(len(tt),-1)),axis=1)
tt=tt[m]; fl=fl[m]
# segments
br=np.where(np.diff(tt)>0.5)[0]+1; seg=np.zeros(len(tt),int)
for j,b in enumerate(br): seg[b:]=j+1
med_img=np.median(fl,axis=0); lowpix=med_img<=np.percentile(med_img,25)
bgts=np.median(fl[:,lowpix],axis=1)   # common-mode (scattered light) from the faintest 25% pixels
bgc=[]
for sgi in np.unique(seg):
    c_=np.zeros(len(tt)); c_[seg==sgi]=bgts[seg==sgi]-np.median(bgts[seg==sgi]); bgc.append(c_)
A=np.hstack([poly_cols(tt,seg,3),np.array(bgc).T,harm_cols(tt,Psig,0.0,1)])
ny,nx=fl.shape[1:]; amp=np.zeros((ny,nx)); eamp=np.zeros((ny,nx)); cc=np.zeros((ny,nx)); ss=np.zeros((ny,nx))
for y in range(ny):
    for x in range(nx):
        f=fl[:,y,x]; c,*_=np.linalg.lstsq(A,f,rcond=None); r=f-A@c; s=1.4826*np.median(np.abs(r))
        cov=np.linalg.inv(A.T@A)*s**2; cc[y,x],ss[y,x]=c[-2],c[-1]; eamp[y,x]=np.sqrt(cov[-1,-1])
mean=np.median(fl,axis=0)
# reference phase = brightest-amplitude pixel; signed amplitude
amp=np.hypot(cc,ss); iy,ix=np.unravel_index(np.argmax(amp),amp.shape)
REF=sys.argv[4] if len(sys.argv)>4 else 'target'
if REF=='target':
    tx0,ty0=w.all_world2pix([[ra,dec]],0)[0]; jx,jy=int(round(tx0)),int(round(ty0))
else: jx,jy=ix,iy
ph0=np.arctan2(ss[jy,jx],cc[jy,jx])
sa=amp*np.cos(np.arctan2(ss,cc)-ph0)
# sources: target + Gaia neighbours G<17 within 90" (+ beyond-90" bright stars are not in the file)
src=[('target',ra,dec,float(T['gaia_Gmag']),0.0)]
for n in csv.DictReader(open(f'{VET}/neighbours_90as.csv')):
    if n['tic']==tic and float(n['sep_arcsec'])>0.5 and float(n['Gmag'])<17: src.append((n['source_id'],float(n['ra']),float(n['dec']),float(n['Gmag']),float(n['sep_arcsec'])))
px=np.array([w.all_world2pix([[s[1],s[2]]],0)[0] for s in src])
G=np.array([s[3] for s in src]); yy,xx=np.mgrid[0:ny,0:nx]
def psf(x0,y0,sig): return np.exp(-((xx-x0)**2+(yy-y0)**2)/(2*sig**2))/(2*np.pi*sig**2)
# 1) mean-image model: all sources, fluxes ~10^-0.4G with free scale, common shift and sigma, + bg
def resm(p):
    dx,dy,sig,sc,bg=p; mod=bg+sum(sc*10**(-0.4*(g-12))*psf(x+dx,y+dy,sig) for (x,y),g in zip(px,G)); return (mod-mean).ravel()/np.sqrt(np.abs(mean.ravel())+50)
pm=least_squares(resm,[0,0,0.8,mean.max()*2,np.percentile(mean,5)]).x
dx,dy,sig=pm[:3]
fr_t=10**(-0.4*G); 
# flux fractions in a 3x3 aperture around the target pixel
tx,ty=px[0][0]+dx,px[0][1]+dy; ap=(np.abs(xx-np.round(tx))<=1)&(np.abs(yy-np.round(ty))<=1)
ff=np.array([np.sum(psf(x+dx,y+dy,sig)[ap])*fr for (x,y),fr in zip(px,fr_t)]); ffrac=ff/ff.sum()
# 2) amplitude map: single-source fits (signed amplitude = c*PSF(source) + const)
out=open(f's4_{tic}_s{sector}.txt','w')
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
P(f'TIC {tic} sector {sector}: {len(tt)} cadences; signal period {Psig} d; mean-image model shift dx={dx:.2f} dy={dy:.2f} px, PSF sigma {sig:.2f} px')
P(f'peak |amplitude| pixel (x,y)=({ix},{iy}) amp {amp[iy,ix]:.2f} +- {eamp[iy,ix]:.2f} e/s; target at ({tx:.2f},{ty:.2f}); median pixel amp err {np.median(eamp):.3f}')
e2=np.median(eamp)
res=[]
for k,((x,y),s) in enumerate(zip(px,src)):
    Pm=psf(x+dx,y+dy,sig).ravel(); B=np.vstack([Pm,np.ones_like(Pm)]).T; c,*_=np.linalg.lstsq(B,sa.ravel(),rcond=None)
    chi2=np.sum(((sa.ravel()-B@c)/eamp.ravel())**2); res.append((chi2,k,c[0]))
res.sort()
# free-position fit
def resa(p): return ((p[2]*psf(p[0],p[1],sig)+p[3]-sa)/eamp).ravel()
pf=least_squares(resa,[ix,iy,sa[iy,ix]*2*np.pi*sig**2,0]).x
cf=w.all_pix2world([[pf[0]-dx,pf[1]-dy]],0)[0]; off=SkyCoord(cf[0],cf[1],unit='deg').separation(SkyCoord(ra,dec,unit='deg')).arcsec
P(f'free-position PSF fit to signed amplitude map: (x,y)=({pf[0]:.2f},{pf[1]:.2f}); offset from target {off:.1f} arcsec ({off/21:.2f} px); total signal flux {pf[2]:.1f} e/s')
amp_frac=pf[2]  # e/s semi-amplitude total
tot_t=np.sum(psf(tx,ty,sig)[ap])  # fraction
P('single-source fits (chi2 rank): source, G, sep", chi2, dchi2 vs best, fitted semi-amp e/s, flux frac in 3x3 ap')
for chi2,k,c in res[:6]:
    s=src[k]; P(f'   {s[0]:>20s} G={s[3]:.2f} sep={s[4]:.1f} chi2={chi2:.1f} dchi2={chi2-res[0][0]:.1f} amp={c:.1f} frac3x3={ffrac[k]:.4f}')
kb=res[0][1]; fl_b=pm[3]*10**(-0.4*(G[kb]-12))
P(f'best single source {src[kb][0]} (G {G[kb]:.2f}): fitted signal {res[0][2]:.2f} e/s / model total flux {fl_b:.0f} e/s = intrinsic semi-amplitude {res[0][2]/fl_b*1e3:.2f} ppt (Gaussian-PSF flux model; approximate)')
# dilution arithmetic: fractional semi-amplitude in 3x3 aperture; intrinsic needed if from each source
apsum=np.sum(mean[ap])-ap.sum()*pm[4]; P(f'3x3 aperture background from mean-image model: {pm[4]:.1f} e/s/pix (subtracted)'); apsig=np.sum(sa[ap])-ap.sum()*pf[3]; fa=apsig/apsum
P(f'3x3 aperture: signal semi-amp {apsig:.1f} e/s of {apsum:.0f} e/s = {fa*1e3:.2f} ppt; required intrinsic semi-amplitude if from source (= fa/fraction): '+'; '.join(f'{src[k][0][-6:]}(G{src[k][3]:.1f},{src[k][4]:.0f}"): {fa/ffrac[k]*1e3:.1f} ppt' for k in np.argsort(-ffrac)[:6]))
fig,ax=plt.subplots(1,2,figsize=(7,3.3))
ax[0].imshow(np.log10(np.clip(mean,1,None)),origin='lower',cmap='gray'); ax[0].set_title('median image (log)',fontsize=8)
im=ax[1].imshow(sa,origin='lower',cmap='RdBu_r',vmin=-np.abs(sa).max(),vmax=np.abs(sa).max()); ax[1].set_title(f'signed amp at P={Psig:.4f} d (e/s)',fontsize=8); plt.colorbar(im,ax=ax[1],fraction=0.046)
for a in ax:
    a.plot(px[1:,0]+dx,px[1:,1]+dy,'y+',ms=6); a.plot(tx,ty,'gx',ms=8)
    for (x,y),g in zip(px[1:],G[1:]):
        if g<15: a.text(x+dx+0.2,y+dy+0.2,f'{g:.1f}',color='y',fontsize=6)
ax[1].plot(pf[0],pf[1],'ko',mfc='none',ms=8)
plt.suptitle(f'TIC {tic} s{sector}',fontsize=8); plt.tight_layout(); plt.savefig(f'pix_{tic}_s{sector}.png',dpi=100)
np.savez(f's4_{tic}_s{sector}.npz',amp=amp,sa=sa,eamp=eamp,mean=mean)
