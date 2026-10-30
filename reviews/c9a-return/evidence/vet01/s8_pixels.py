# s8: TESScut pixel analysis, one cube at a time:
#  (a) own background-subtracted aperture photometry (r=1.5 px) -> saved to pix/ap_<tic>_s<sec>.npz
#  (b) per-event and per-sector difference images (median out-of-eclipse minus median in-eclipse, primaries)
#  (c) Gaussian-PSF scene model of the out-of-eclipse image (TIC stars T<17 within 120", positions from WCS + one global shift)
#  (d) free-position PSF fit of the difference image -> offset from the target (arcsec, RA/Dec), bootstrap over events
#  (e) hypothesis test: chi2 of difference image = A x PSF(star k) for target and each neighbour
#  (f) flux fraction of each star in the aperture -> intrinsic depth it would need
import sys, glob, json, csv, numpy as np, warnings
from astropy.io import fits
from astropy.wcs import WCS
from scipy.optimize import least_squares
warnings.filterwarnings('ignore')
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet01'
tic=sys.argv[1]; secs=[int(x) for x in sys.argv[2].split(',')] if len(sys.argv)>2 else None
EP=json.load(open('ephem.json'))[tic]; P,T0=EP['P'],EP['T0']
R=[r for r in csv.DictReader(open('events_qlp.csv')) if r['tic']==tic and r['type']=='P' and r['status']=='ok']
T14=np.median([float(r['T14_h']) for r in R])/24
stars=[r for r in csv.DictReader(open(f'tic_neighbours_{tic}.csv')) if r['disposition']!='DUPLICATE' and float(r['Tmag'])<17.0]
sra=np.array([float(r['ra']) for r in stars]); sde=np.array([float(r['dec']) for r in stars]); sT=np.array([float(r['Tmag']) for r in stars])
sid=[r['ID'] for r in stars]; sG=[r['GAIA'] for r in stars]; sdist=np.array([float(r['dstArcSec']) for r in stars])
assert sid[0]==tic
def gpsf(X,Y,x0,y0,s):  # pixel-integrated Gaussian
    from scipy.special import erf
    a=lambda u,c:0.5*(erf((u+0.5-c)/(np.sqrt(2)*s))-erf((u-0.5-c)/(np.sqrt(2)*s)))
    return a(X,x0)*a(Y,y0)
out={}
for f in sorted(glob.glob(f'{D}/{tic}/tesscut/*astrocut.fits')):
    sec=int(f.split('tess-s')[1][:4])
    if secs and sec not in secs: continue
    h=fits.open(f); d=h[1].data; w=WCS(h[2].header)
    cam=f"{h[0].header['CAMERA']}-{h[0].header['CCD']}"; t=np.array(d['TIME'],float); F=np.array(d['FLUX'],float); q=np.array(d['QUALITY'])
    ok=np.isfinite(t)&(q==0)&np.all(np.isfinite(F.reshape(len(t),-1)),axis=1)
    t,F=t[ok],F[ok]; h.close(); del d
    ny,nx=F.shape[1:]; Y,X=np.mgrid[0:ny,0:nx]
    xs,ys=w.world_to_pixel_values(sra,sde)
    med=np.median(F,axis=0)
    bpix=med<=np.percentile(med,20)
    bkg=np.median(F[:,bpix],axis=1); Fb=F-bkg[:,None,None]
    xt,yt=xs[0],ys[0]
    ap=np.hypot(X-xt,Y-yt)<=1.5
    lc=Fb[:,ap].sum(1); 
    texp=np.median(np.diff(t))
    np.savez_compressed(f'pix/ap_{tic}_s{sec}.npz',t=t,flux=lc,bkg=bkg,ap=ap,texp=texp)
    # events
    n0=int(np.floor((t.min()-T0)/P))-1; n1=int(np.ceil((t.max()-T0)/P))+1
    diffs=[];outs=[];evs=[]
    for n in range(n0,n1+1):
        tc=T0+n*P
        din=np.abs(t-tc)<0.25*T14; dout=(np.abs(t-tc)>0.75*T14)&(np.abs(t-tc)<1.25*T14+0.1)
        pre=dout&(t<tc); post=dout&(t>tc)
        need=max(2,int(0.5*T14*0.5/texp))
        if din.sum()<max(2,int(0.5*T14/texp*0.6)) or pre.sum()<need or post.sum()<need: continue
        O=0.5*(np.median(Fb[pre],0)+np.median(Fb[post],0)); I=np.median(Fb[din],0)
        diffs.append(O-I); outs.append(O); evs.append(round(tc,4))
    if len(diffs)<1: print(tic,sec,'no full primary events'); continue
    diffs=np.array(diffs); Oim=np.median(np.array(outs),0); Dim=diffs.mean(0)
    # scene model of O: target + stars with T<15.5 free fluxes inside the cutout, fainter fixed ratio to target
    inside=(xs>-1.5)&(xs<nx+0.5)&(ys>-1.5)&(ys<ny+0.5)
    free=np.where(inside&(sT<15.5))[0]; fixd=np.where(inside&(sT>=15.5))[0]
    def scene(p,ret_comp=False):
        dx,dy,s,b=p[:4]; Fl=p[4:]
        comps={}
        m=np.full(X.shape,b,float)
        for j,k in enumerate(free):
            c=gpsf(X,Y,xs[k]+dx,ys[k]+dy,s); comps[k]=c; m+=Fl[j]*c
        for k in fixd:
            c=gpsf(X,Y,xs[k]+dx,ys[k]+dy,s); comps[k]=c; m+=Fl[0]*10**(-0.4*(sT[k]-sT[0]))*c
        return (m,comps) if ret_comp else m
    p0=[0,0,0.8,0]+[Oim[ap].sum()*10**(-0.4*(sT[k]-sT[0])) for k in free]
    rs=least_squares(lambda p:(scene(p)-Oim).ravel()/np.sqrt(np.abs(Oim).ravel()+10),p0,bounds=([-1.5,-1.5,0.3,-1e4]+[0]*len(free),[1.5,1.5,2.5,1e4]+[np.inf]*len(free)))
    dx,dy,s,b=rs.x[:4]; mod,comps=scene(rs.x,True)
    fluxes={k:(rs.x[4+list(free).index(k)] if k in free else rs.x[4]*10**(-0.4*(sT[k]-sT[0]))) for k in comps}
    tot_ap=sum(fluxes[k]*comps[k][ap].sum() for k in comps)
    frac={k:fluxes[k]*comps[k][ap].sum()/tot_ap for k in comps}
    xT,yT=xt+dx,yt+dy
    # diff image fit: free position Gaussian (sigma fixed) + const
    def dfit(Dm):
        sig=np.sqrt(np.abs(Oim)+10)*np.sqrt(1.0)  # weights ~ photon noise of O
        a0=max(Dm[ap].sum(),1e-3)
        r=least_squares(lambda p:(p[0]*gpsf(X,Y,p[1],p[2],s)+p[3]-Dm).ravel()/sig.ravel(),[a0,xT,yT,0],bounds=([-np.inf,-1,-1,-np.inf],[np.inf,nx,ny,np.inf]))
        return r.x
    pd=dfit(Dim)
    rng=np.random.default_rng(1)
    bs=np.array([dfit(diffs[rng.integers(0,len(diffs),len(diffs))].mean(0))[1:3] for _ in range(100)]) if len(diffs)>=3 else None
    # pixel->arcsec on sky (local Jacobian)
    def off_arcsec(x,y,x0,y0):
        r1,d1=w.pixel_to_world_values(x,y); r0,d0=w.pixel_to_world_values(x0,y0)
        return ((r1-r0)*np.cos(np.radians(d0))*3600,(d1-d0)*3600)
    oE,oN=off_arcsec(pd[1],pd[2],xT,yT)
    if bs is not None:
        bE,bN=np.array([off_arcsec(a,c,xT,yT) for a,c in bs]).T; eE,eN=np.std(bE),np.std(bN)
    else: eE=eN=np.nan
    # hypothesis chi2: D = A*psf_k + c
    sig=np.sqrt(np.abs(Oim)+10)
    if len(diffs)>=3:  # empirical per-pixel noise of the stacked diff
        sig=np.std(diffs,0,ddof=1)/np.sqrt(len(diffs)); sig=np.maximum(sig,np.median(sig)*0.3)
    hyp=[]
    for k in comps:
        A=np.c_[comps[k].ravel()/sig.ravel(),1/sig.ravel()]; c,*_=np.linalg.lstsq(A,Dim.ravel()/sig.ravel(),rcond=None)
        chi=np.sum((A@c-Dim.ravel()/sig.ravel())**2); hyp.append((chi,k,c[0]))
    hyp.sort()
    chiT=[hh[0] for hh in hyp if hh[1]==0][0]
    # fractional depth map
    fr=Dim/np.where(Oim>0,Oim,np.nan)
    iy,ix=np.unravel_index(np.nanargmax(np.where(np.hypot(X-xT,Y-yT)<4,Dim,-np.inf)),Dim.shape)
    # single events: first two full events
    single=[]
    for j in range(min(2,len(diffs))):
        pj=dfit(diffs[j]); single.append((evs[j],*off_arcsec(pj[1],pj[2],xT,yT)))
    print(f'=== TIC {tic} s{sec} cam{cam}  events used {len(diffs)} {evs}')
    print(f'  scene: global shift ({dx:+.3f},{dy:+.3f}) px, PSF sigma {s:.3f} px, bkg resid {b:.1f}; target at pixel ({xT:.2f},{yT:.2f}); aperture {ap.sum()} px r=1.5')
    print(f'  diff-image PSF centroid offset from target: dE={oE:+.2f}" dN={oN:+.2f}"  |off|={np.hypot(oE,oN):.2f}" (bootstrap err E {eE:.2f}" N {eN:.2f}")')
    print(f'  diff amplitude {pd[0]:.1f} e/s ; target-star flux model {fluxes[0]:.1f}; amp/target flux = {pd[0]/fluxes[0]*1e3:.1f} ppt')
    print(f'  brightest deficit pixel ({ix},{iy}) vs target pixel ({int(round(xT))},{int(round(yT))}); frac depth there {fr[iy,ix]*1e3:.1f} ppt; at target pixel {fr[int(round(yT)),int(round(xT))]*1e3:.1f} ppt')
    for (te,a,c) in single: print(f'  single event {te}: offset dE={a:+.2f}" dN={c:+.2f}"  |off|={np.hypot(a,c):.2f}"')
    print(f'  PSF hypotheses (chi2, lower=better; N pix {Dim.size}): best = {sid[hyp[0][1]]}; target chi2 {chiT:.1f}')
    for chi,k,A in hyp[:4]: print(f'     {sid[k]:>11s} sep {sdist[k]:5.1f}" T={sT[k]:.2f} chi2 {chi:9.1f}  dchi2 vs target {chi-chiT:+9.1f}')
    rows=[]
    for k in sorted(comps,key=lambda k:sdist[k]):
        sE,sN=off_arcsec(xs[k]+dx,ys[k]+dy,xT,yT); dd=np.hypot(oE-sE,oN-sN); ed=np.hypot(eE*(oE-sE),eN*(oN-sN))/max(dd,1e-9)
        rows.append(dict(id=sid[k],gaia=sG[k],sep=round(sdist[k],2),Tmag=sT[k],frac_ap=frac[k],dchi2=[hh[0] for hh in hyp if hh[1]==k][0]-chiT,
                         starE=sE,starN=sN,dist_from_centroid=dd,nsig=dd/ed if ed>0 else np.nan))
        if sdist[k]<40 and k!=0: print(f'     star {sid[k]} at dE={sE:+.2f}" dN={sN:+.2f}" : diff centroid is {dd:.2f}" away = {dd/ed if ed>0 else np.nan:.1f} sigma; flux frac in ap {frac[k]*100:.2f}%')
    out[sec]=dict(events=evs,offE=oE,offN=oN,eE=eE,eN=eN,sigma=s,stars=rows,single=single,frac_target=frac[0],nev=len(diffs))
    np.savez_compressed(f'pix/img_{tic}_s{sec}.npz',D=Dim,O=Oim,mod=mod,xT=xT,yT=yT,xs=xs+dx,ys=ys+dy,ap=ap)
    del F,Fb
json.dump(out,open(f'pix/pix_{tic}{"_"+sys.argv[2].replace(",","-") if secs else ""}.json','w'),indent=1,default=float)
