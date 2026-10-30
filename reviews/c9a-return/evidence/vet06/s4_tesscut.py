# TESScut difference image for one star/sector (usage: s4_tesscut.py tic sector). Per primary event: median in-eclipse
# (|t-tc|<0.3 T14) minus median local out-of-eclipse (0.7-1.6 T14 from tc), averaged over events. Deficit centre =
# 2-D Gaussian fit to the difference image; compared with target WCS position and with out-of-eclipse centroid.
# Dilution: Gaussian PRF (sigma 0.75 px) fluxes from Gaia G for target + neighbours (neighbours_90as.csv); aperture r<=1.5 px.
# Required intrinsic depth for each neighbour = aperture depth * total aperture flux / neighbour aperture flux (PRF) and
# worst case (neighbour fully in aperture). Also simple aperture-photometry depth (independent pipeline). Cube deleted after.
import sys, os, glob, numpy as np, csv, warnings, shutil
from astropy.io import fits; from astropy.wcs import WCS; from scipy.optimize import curve_fit
from scipy.special import erf
warnings.filterwarnings('ignore')
tic=sys.argv[1]; sec=int(sys.argv[2])
D=f'/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet06/{tic}/tesscut_s{sec}'
os.makedirs(D,exist_ok=True)
RA,DEC={'468827621':(91.9386505142516,69.034466660429),'416285595':(287.318165074913,24.0684959972507)}[tic]
T14={'468827621':6.0/24,'416285595':3.6/24}[tic]
T0,eT0,P,eP,ph2,eph2=np.load(f's3_ephem_{tic}.npy')
fn=glob.glob(f'{D}/*.fits')
if not fn:
    from astroquery.mast import Tesscut; from astropy.coordinates import SkyCoord
    Tesscut.download_cutouts(coordinates=SkyCoord(RA,DEC,unit='deg'),size=11,sector=sec,path=D)
    fn=glob.glob(f'{D}/*.fits')
h=fits.open(fn[0]); d=h[1].data; w=WCS(h[2].header)
t=d['TIME']; fl=d['FLUX'].astype(float); q=d['QUALITY']
g=(q==0)&np.isfinite(t)&np.all(np.isfinite(fl.reshape(len(t),-1)),axis=1)
t=t[g]; fl=fl[g]; print(f'TIC {tic} s{sec} cam{h[0].header.get("CAMERA")} ccd{h[0].header.get("CCD")}: {g.sum()} good frames')
ny,nx=fl.shape[1:]; tx,ty=[float(v) for v in w.all_world2pix(RA,DEC,0)]; print(f'target pixel (x,y)=({tx:.2f},{ty:.2f})')
YY,XX=np.mgrid[0:ny,0:nx]
ev=[T0+n*P for n in range(int((t.min()-T0)/P)-1,int((t.max()-T0)/P)+2)]
diffs=[];oots=[];used=[]
for tc in ev:
    i=np.abs(t-tc)<0.3*T14; o=(np.abs(t-tc)>0.7*T14)&(np.abs(t-tc)<1.6*T14)
    if i.sum()<3 or (o&(t<tc)).sum()<3 or (o&(t>tc)).sum()<3: continue
    oo=np.median(fl[o],0); diffs.append(oo-np.median(fl[i],0)); oots.append(oo); used.append(tc)
print('events used:',' '.join(f'{x:.3f}' for x in used))
if not diffs: sys.exit('no events')
DI=np.mean(diffs,0); OO=np.mean(oots,0); FR=DI/OO
def g2(xy,a,x0,y0,s,b): x,y=xy; return (a*np.exp(-((x-x0)**2+(y-y0)**2)/(2*s*s))+b).ravel()
def fitc(img):
    j=np.unravel_index(np.nanargmax(img),img.shape)
    p,c=curve_fit(g2,(XX,YY),img.ravel(),p0=[img[j],j[1],j[0],0.8,0]); return p,np.sqrt(np.diag(c))
pd,ed=fitc(DI); po,eo=fitc(OO)
off_t=21*np.hypot(pd[1]-tx,pd[2]-ty); off_o=21*np.hypot(pd[1]-po[1],pd[2]-po[2]); eoff=21*np.hypot(ed[1],ed[2])
print(f'deficit centre (x,y)=({pd[1]:.3f},{pd[2]:.3f}) +-({ed[1]:.3f},{ed[2]:.3f}); OOT centre ({po[1]:.3f},{po[2]:.3f})')
print(f'offset deficit-target WCS = {off_t:.2f}"; deficit-OOT centroid = {off_o:.2f}" (+-{eoff:.2f}")')
iy,ix=int(round(ty)),int(round(tx)); print(f'fractional depth on target pixel = {1e3*FR[iy,ix]:.1f} ppt; max frac depth pixel {np.unravel_index(np.nanargmax(FR),FR.shape)} = {1e3*np.nanmax(FR):.1f} ppt')
# aperture photometry depth
ap=np.hypot(XX-tx,YY-ty)<=1.5; bk=np.hypot(XX-tx,YY-ty)>=4
lc=(fl*ap).sum((1,2))-ap.sum()*np.median(fl[:,bk],1)
deps=[]
for tc in used:
    i=np.abs(t-tc)<0.15*T14; o=(np.abs(t-tc)>0.7*T14)&(np.abs(t-tc)<1.6*T14)
    A=np.vstack([np.ones(o.sum()),t[o]-tc]).T; c=np.linalg.lstsq(A,lc[o],rcond=None)[0]
    deps.append(1-np.median(lc[i])/c[0])
print(f'TESScut aperture (r<=1.5px, {ap.sum()} px) central depth per event (ppt): '+' '.join(f'{1e3*x:.1f}' for x in deps)+f'; mean {1e3*np.mean(deps):.1f}')
dap=np.mean(deps)
# dilution
def frac(x0,y0,s=0.75):
    fx=lambda a,b: 0.5*(erf((b-x0)/(np.sqrt(2)*s))-erf((a-x0)/(np.sqrt(2)*s)))
    fy=lambda a,b: 0.5*(erf((b-y0)/(np.sqrt(2)*s))-erf((a-y0)/(np.sqrt(2)*s)))
    return sum(fx(x-0.5,x+0.5)*fy(y-0.5,y+0.5) for y,x in zip(*np.where(ap)))
rows=[r for r in csv.DictReader(open('[local path omitted]')) if r['tic']==tic]
stars=[]
for r in rows:
    x,y=[float(v) for v in w.all_world2pix(float(r["ra"]),float(r["dec"]),0)]; F=10**(-0.4*(float(r['Gmag'])-12.75)); stars.append((r,x,y,F,F*frac(x,y)))
Ftot=sum(s[4] for s in stars)
print(f'aperture flux share of target {[s[4] for s in stars if float(s[0]["sep_arcsec"])<1][0]/Ftot:.3f}')
print('neighbour: G sep" | PRF aperture share | required depth PRF / worst-case | frac depth at its pixel (ppt) | verdict')
for r,x,y,F,Fa in stars:
    if float(r['sep_arcsec'])<1: continue
    rp=dap*Ftot/Fa if Fa>0 else np.inf; rw=dap*Ftot/F
    jx,jy=int(round(x)),int(round(y)); fp=1e3*FR[jy,jx] if 0<=jx<nx and 0<=jy<ny else np.nan
    if rw<1.0 or rp<1.0: print(f'  G{float(r["Gmag"]):.2f} {float(r["sep_arcsec"]):.1f}" | {Fa/Ftot:.4f} | {100*rp:.0f}% / {100*rw:.0f}% | {fp:.1f} | arithmetically possible')
    else: pass
nex=sum(1 for r,x,y,F,Fa in stars if float(r['sep_arcsec'])>=1 and min(dap*Ftot/max(Fa,1e-30),dap*Ftot/F)>=1)
print(f'{nex} other neighbours need >100% even in the worst case (excluded)')
np.savez(f's4_tesscut_{tic}_s{sec}.npz',DI=DI,OO=OO,FR=FR,tx=tx,ty=ty)
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2,figsize=(7,3.3))
for a,img,ttl in [(ax[0],OO,'out-of-eclipse'),(ax[1],FR*1e3,'fractional deficit (ppt)')]:
    im=a.imshow(img,origin='lower',cmap='viridis'); plt.colorbar(im,ax=a,fraction=0.046); a.set_title(ttl,fontsize=9)
    a.plot(tx,ty,'r+',ms=12); a.plot(pd[1],pd[2],'wx')
    for r,x,y,F,Fa in stars:
        if float(r['sep_arcsec'])>1 and float(r['Gmag'])<16.5: a.plot(x,y,'o',mfc='none',mec='orange',ms=5)
fig.suptitle(f'TIC {tic} s{sec}',fontsize=10); fig.tight_layout(); fig.savefig(f's4_tesscut_{tic}_s{sec}.png',dpi=100)
shutil.rmtree(D); print('cube deleted')
