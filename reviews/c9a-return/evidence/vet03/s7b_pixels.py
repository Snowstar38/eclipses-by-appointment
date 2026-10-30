import numpy as np, json, sys, glob, csv
from astropy.io import fits
from astropy.wcs import WCS
from scipy.optimize import least_squares
from lcio import trap
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet03'
tic=sys.argv[1]
SECS=[int(x) for x in sys.argv[2:]]  # s7b: optional sector filter (resume after crash)
E={'70665829':dict(T0=2576.73361,P=3.4657658,phi2=0.46049,T14=2.83/24,r=0.19,Tt=12.2939,ra=155.384788090706,dec=17.2035145893056),
   '331293467':dict(T0=4066.68168,P=5.2568187,phi2=0.5002,T14=4.07/24,r=0.20,Tt=12.3131,ra=212.403511923353,dec=-60.1143106920448)}[tic]
def Tmag(G,bprp):  # Stassun+2019 TIC-8 relation (dwarfs/giants, -0.2<BP-RP<3)
    x=bprp; return G-0.00522555*x**3+0.0891337*x**2-0.633923*x+0.0324473
stars=[]
for r in csv.DictReader(open('../neighbours_90as.csv')):
    if r['tic']!=tic: continue
    sep=float(r['sep_arcsec'])
    stars.append(dict(id=r['source_id'],ra=float(r['ra']),dec=float(r['dec']),G=float(r['Gmag']),bprp=float(r['BP_RP']),sep=sep,T=(E['Tt'] if sep<1 else Tmag(float(r['Gmag']),min(float(r['BP_RP']),3.5)))))
stars.sort(key=lambda s:s['sep'])
def gauss(xx,yy,x0,y0,s): 
    # pixel-integrated gaussian
    from scipy.special import erf
    k=np.sqrt(2)*s
    return 0.25*(erf((xx+0.5-x0)/k)-erf((xx-0.5-x0)/k))*(erf((yy+0.5-y0)/k)-erf((yy-0.5-y0)/k))
out={}
for fn in sorted(glob.glob(f'{D}/{tic}/tesscut/*.fits')):
    h=fits.open(fn); sec=h[0].header['SECTOR']
    if SECS and sec not in SECS: h.close(); continue
    d=h[1].data; w=WCS(h[2].header)
    t=d['TIME']; F=np.array(d['FLUX'],float); q=d['QUALITY']
    good=(q==0)&np.isfinite(t)&np.all(np.isfinite(F.reshape(len(t),-1)),axis=1)
    t=t[good]; F=F[good]
    bkg=np.percentile(F.reshape(len(t),-1),20,axis=1); F=F-bkg[:,None,None]
    ny,nx=F.shape[1:]; yy,xx=np.mgrid[0:ny,0:nx]
    for s in stars: s['x'],s['y']=[float(v) for v in w.all_world2pix(s['ra'],s['dec'],0)]
    tgt=stars[0]
    inst=[s for s in stars if -2<s['x']<nx+1 and -2<s['y']<ny+1]
    cad=np.median(np.diff(t))
    res={}
    for kind,ph in [('primary',0.0),('secondary',E['phi2'])]:
        n0=int(np.floor((t.min()-E['T0'])/E['P']))-1; n1=int(np.ceil((t.max()-E['T0'])/E['P']))+1
        diffs=[]; ooti=[]; evt=[]
        for n in range(n0,n1+1):
            tc=E['T0']+(n+ph)*E['P']; dt=t-tc
            ii=np.abs(dt)<0.25*E['T14']; oo=(np.abs(dt)>0.7*E['T14'])&(np.abs(dt)<0.7*E['T14']+0.25)
            if ii.sum()<max(3,0.3*0.5*E['T14']/cad) or (oo&(dt<0)).sum()<5 or (oo&(dt>0)).sum()<5: continue
            O=np.median(F[oo],0); I=np.median(F[ii],0); diffs.append(O-I); ooti.append(O); evt.append(tc)
        if not diffs: continue
        diffs=np.array(diffs); Dm=diffs.mean(0); Om=np.median(F,0)
        # scene fit to OOT image: target flux A, neighbour scale B, shift, sigma, bkg
        def scene(p,which=None):
            A,B,dx,dy,sg,b=p; m=np.full((ny,nx),b)
            for s in inst:
                fl=A if s is tgt else A*B*10**(-0.4*(s['T']-tgt['T']))
                m=m+fl*gauss(xx,yy,s['x']+dx,s['y']+dy,sg)
            return m
        p0=[Om.max()*3,1,0,0,0.8,0]
        sf=least_squares(lambda p:(scene(p)-Om).ravel(),p0,bounds=([0,0,-2,-2,0.3,-1e4],[1e8,10,2,2,3,1e4]))
        A,B,dx,dy,sg,b=sf.x
        # diff-image single-source fit
        def one(p): a,x0,y0,c=p; return a*gauss(xx,yy,x0,y0,sg)+c
        xt,yt=tgt['x']+dx,tgt['y']+dy
        def fitD(Dimg):
            s=least_squares(lambda p:(one(p)-Dimg).ravel(),[Dimg.max()*3,xt,yt,0]); return s.x
        pd=fitD(Dm)
        rng=np.random.default_rng(1); bs=[]
        for k in range(300):
            idx=rng.integers(0,len(diffs),len(diffs)); bs.append(fitD(diffs[idx].mean(0))[1:3])
        bs=np.array(bs); ex,ey=bs.std(0)
        offx,offy=pd[1]-xt,pd[2]-yt; off=np.hypot(offx,offy)*21.0; eoff=np.hypot(ex*abs(offx),ey*abs(offy))/max(np.hypot(offx,offy),1e-9)*21.0
        # flux-weighted centroids
        cO=(np.sum(Om*xx)/Om.sum(),np.sum(Om*yy)/Om.sum())
        # candidate test
        cand=[]
        for s in stars:
            if s['sep']>90: continue
            x0,y0=s['x']+dx,s['y']+dy
            G0=gauss(xx,yy,x0,y0,sg); M=np.vstack([G0.ravel(),np.ones(G0.size)]).T
            coef,*_=np.linalg.lstsq(M,Dm.ravel(),rcond=None); chi=np.sum((M@coef-Dm.ravel())**2)
            cand.append((s,chi,coef[0]))
        chi_t=cand[0][1]
        # aperture: 3x3 around target model position + flux fractions
        ix,iy=int(round(xt)),int(round(yt)); ap=np.zeros((ny,nx),bool); ap[max(iy-1,0):iy+2,max(ix-1,0):ix+2]=True
        flux_ap_meas=Om[ap].sum()
        dep_ap=Dm[ap].sum()/np.median([o[ap].sum() for o in ooti])
        fr={}
        for s in stars:
            fl=A if s is tgt else A*B*10**(-0.4*(s['T']-tgt['T']))
            fr[s['id']]=fl*gauss(xx,yy,s['x']+dx,s['y']+dy,sg)[ap].sum()/flux_ap_meas
        lines=[]
        lines.append(f"s{sec} {kind}: N_events={len(diffs)} scene fit A={A:.0f} B(neigh scale)={B:.2f} shift=({dx:+.2f},{dy:+.2f}) px sigma={sg:.2f} px bkg={b:.1f}; target model pos=({xt:.2f},{yt:.2f})")
        lines.append(f"  diff-image source fit at ({pd[1]:.2f},{pd[2]:.2f}) +- ({ex:.2f},{ey:.2f}) px; offset from target = ({offx*21:+.1f},{offy*21:+.1f})\" |off|={off:.1f}\" +- {eoff:.1f}\"; deficit amplitude {pd[0]:.1f} e/s")
        lines.append(f"  OOT flux-weighted centroid ({cO[0]:.2f},{cO[1]:.2f}); diff-image peak pixel {np.unravel_index(np.argmax(Dm),Dm.shape)[::-1]}; target pixel ({ix},{iy})")
        lines.append(f"  3x3 aperture: measured OOT flux {flux_ap_meas:.0f} e/s, diff-image depth in aperture {dep_ap*1e3:.1f} ppt; target model share of aperture = {fr[tgt['id']]:.3f} -> undiluted target depth {dep_ap/fr[tgt['id']]*1e3:.1f} ppt")
        fracD=Dm/np.clip(Om,Om.max()*0.05,None); pk=np.unravel_index(np.argmax(fracD),fracD.shape)[::-1]
        lines.append(f"  fractional-deficit peak pixel {pk} value {fracD.max()*1e3:.1f} ppt (pixels with OOT flux > 5% of max)")
        for s in stars:
            if s is tgt or s['sep']>40: continue
            vx,vy=(s['x']-tgt['x'])*21,(s['y']-tgt['y'])*21; L=np.hypot(vx,vy)
            proj=(offx*21*vx+offy*21*vy)/L
            lines.append(f"  vector check vs {s['id']} (G {s['G']:.2f}, {s['sep']:.1f}\"): neighbour at ({vx:+.1f},{vy:+.1f})\" from target; measured offset projected on that direction {proj:+.1f}\" = {proj/L:.2f} of the way")
        lines.append("  candidate | sep\" | G | T(est) | share of ap | needed intrinsic depth | chi2/chi2_target | fitted amp")
        for s,chi,a in cand:
            f=fr[s['id']]; need=dep_ap/f if f>0 else np.inf
            lines.append(f"   {s['id']} | {s['sep']:5.1f} | {s['G']:.2f} | {s['T']:.2f} | {f:.4f} | {need*100:8.1f}% | {chi/chi_t:7.2f} | {a:.1f}")
        print('\n'.join(lines),flush=True); res[kind]=dict(lines=lines,off=off,eoff=eoff,dep_ap=dep_ap)
        if kind=='primary':
            fig,ax=plt.subplots(1,3,figsize=(9,3))
            for a_,img,tl in zip(ax,[Om,Dm,Dm/np.clip(Om,Om.max()*0.02,None)],['OOT median','in-out deficit','fractional deficit']):
                a_.imshow(img,origin='lower',cmap='viridis'); a_.set_title(f'{tl} s{sec}',fontsize=8)
                for s in stars:
                    if s['sep']<=60: a_.plot(s['x']+dx,s['y']+dy,'r+' if s is not tgt else 'wx',ms=6 if s['G']<16 else 3)
                a_.plot(pd[1],pd[2],'o',mfc='none',mec='orange')
            plt.tight_layout(); plt.savefig(f'pix_{tic}_s{sec}.png',dpi=90); plt.close()
    # own aperture photometry light curve (3x3) for this sector
    xt,yt=float(tgt['x']),float(tgt['y']); ix,iy=int(round(xt)),int(round(yt)); ap=np.zeros((ny,nx),bool); ap[max(iy-1,0):iy+2,max(ix-1,0):ix+2]=True
    lc=F[:,ap].sum(1); lc=lc/np.median(lc)
    np.savetxt(f'tesscut_ap3x3_{tic}_s{sec}.txt',np.c_[t,lc],fmt='%.6f',header='BTJD  norm_flux (3x3 aperture, bkg = 20th pct pixel, QUALITY==0)')
    out[sec]=res
    del F,d; h.close()
