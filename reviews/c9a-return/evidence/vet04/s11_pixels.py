# TESScut pixel analysis: background-subtracted cube, Gaia-scene Gaussian-PSF model of the direct image (fits PSF width + WCS offset),
# per-event difference images (median out - median in), deficit centroid, single-source hypothesis fits for target and every Gaia neighbour,
# dilution arithmetic, and own aperture photometry depths (fixed eclipse shape from s08).
import sys, glob, json, numpy as np, csv
from astropy.io import fits; from astropy.wcs import WCS
from scipy.optimize import least_squares
sys.path.insert(0,'.'); from common import GAIA, D; from fitlib import fit_event
tic=sys.argv[1]
eph=json.load(open(f's05_ephem_{tic}.json')); sh=json.load(open('s08_shape_oddeven.json'))[tic]['shape']
P=eph['P']; T0={'P':eph['T0P'],'S':eph['T0S']}
tgt=[r for r in csv.DictReader(open('../targets.csv')) if r['tic']==tic][0]
nb=[r for r in csv.DictReader(open('../neighbours_90as.csv')) if r['tic']==tic]
def tmag(G,br): return G-0.00522555*br**3+0.0891337*br**2-0.633923*br+0.0324473
stars=[dict(id=r['source_id'],ra=float(r['ra']),dec=float(r['dec']),G=float(r['Gmag']),T=tmag(float(r['Gmag']),float(r['BP_RP'])),sep=float(r['sep_arcsec'])) for r in nb]
stars.sort(key=lambda s:s['sep']); assert stars[0]['sep']<1
def gauss_img(x0,y0,sig,ny,nx):
    # pixel-integrated gaussian via erf
    from scipy.special import erf
    xe=np.arange(nx+1)-0.5; ye=np.arange(ny+1)-0.5
    gx=0.5*(erf((xe[1:]-x0)/(np.sqrt(2)*sig))-erf((xe[:-1]-x0)/(np.sqrt(2)*sig)))
    gy=0.5*(erf((ye[1:]-y0)/(np.sqrt(2)*sig))-erf((ye[:-1]-y0)/(np.sqrt(2)*sig)))
    return np.outer(gy,gx)
summary=[]
for fn in sorted(glob.glob(f'{D}/{tic}/tesscut/*astrocut.fits')):
    h=fits.open(fn); d=h[1].data; w=WCS(h[2].header); sec=int(h[0].header['SECTOR'])
    t=d['TIME']; F=np.array(d['FLUX'],float); q=d['QUALITY']
    ok=(q==0)&np.isfinite(t)&np.all(np.isfinite(F.reshape(len(t),-1)),1)
    t=t[ok]; F=F[ok]
    med=np.nanmedian(F,0); ny,nx=med.shape
    bpix=med<=np.percentile(med,30)
    bkg=np.array([np.median(f[bpix]) for f in F]); F=F-bkg[:,None,None]
    med=np.nanmedian(F,0)
    # scene: pixel positions of all Gaia stars
    for s in stars: s['x'],s['y']=w.all_world2pix([[s['ra'],s['dec']]],0)[0]
    fl=np.array([10**(-0.4*(s['T']-10)) for s in stars])
    X=np.array([s['x'] for s in stars]); Y=np.array([s['y'] for s in stars])
    def scene(p,ret=False):
        dx,dy,sig,A,b=p
        m=b+A*sum(fl[i]*gauss_img(X[i]+dx,Y[i]+dy,sig,ny,nx) for i in range(len(stars)))
        return m
    r=least_squares(lambda p:(scene(p)-med).ravel(),[0,0,0.8,med.max()/fl[0],0],bounds=([-2,-2,0.3,0,-500],[2,2,3,1e9,500]))
    dx,dy,sig,A,b=r.x
    comp=[A*fl[i]*gauss_img(X[i]+dx,Y[i]+dy,sig,ny,nx) for i in range(len(stars))]
    model=b+sum(comp)
    # aperture: pixels where target component >= 30% of model and target comp > 5% of its peak... simple: top pixels of target comp holding ~target light
    tc=comp[0]
    ap=(tc/model>0.5)&(tc>0.08*tc.max())
    frac=np.array([c[ap].sum() for c in comp])/model[ap].sum()
    lc=F[:,ap].sum(1); lc=lc/np.median(lc)
    te=float(np.median(np.diff(t)))
    print(f'=== {tic} s{sec} cadence {te*86400:.0f}s  scene fit: WCS offset dx={dx:+.2f} dy={dy:+.2f} pix, sigma={sig:.2f} pix, resid rms/peak={np.std(r.fun)/med.max():.3f}; aperture {ap.sum()} pix; target flux fraction in aperture {frac[0]:.3f}')
    # events
    for kind in ('P','S'):
        s_=sh[kind]; T14=s_['T14']
        ks=range(int((t.min()-T0[kind])/P)-1,int((t.max()-T0[kind])/P)+2)
        evs=[]
        for k in ks:
            tcen=T0[kind]+k*P
            inn=np.abs(t-tcen)<0.5*s_['r23']*T14+0.25*(1-s_['r23'])*T14   # inner part of the eclipse
            out=(np.abs(t-tcen)>T14/2+0.05)&(np.abs(t-tcen)<T14/2+0.6)
            pre=np.sum(out&(t<tcen)); post=np.sum(out&(t>tcen))
            if inn.sum()*te<0.4*T14*0.5 or pre*te<0.15 or post*te<0.15: continue
            # own aperture photometry depth with fixed shape
            fr=fit_event(t,lc,te if te>0.003 else 0.0,tcen,s_['d'],T14,0.7 if tic=='283532878' else 0.8,fix={'T14':T14,'r23':s_['r23']})
            diff=np.median(F[out],0)-np.median(F[inn],0)
            evs.append((k,tcen,diff,np.median(F[out],0),fr,inn.sum(),out.sum()))
        for k,tcen,diff,oot,fr,nin,nout in evs:
            pix_frac=diff/np.where(oot>0,oot,np.nan)
            # noise per pixel from out-of-eclipse scatter
            # centroid of the deficit (flux-weighted, positive part, 5x5 box around the target model position)
            x0,y0=X[0]+dx,Y[0]+dy
            yy,xx=np.mgrid[0:ny,0:nx]; box=(np.abs(xx-x0)<=2.5)&(np.abs(yy-y0)<=2.5)
            wgt=np.clip(diff,0,None)*box
            cx=(wgt*xx).sum()/wgt.sum(); cy=(wgt*yy).sum()/wgt.sum()
            # direct-image centroid in same box (light-weighted, for comparison)
            wd=np.clip(oot,0,None)*box; dcx=(wd*xx).sum()/wd.sum(); dcy=(wd*yy).sum()/wd.sum()
            # hypothesis fits: diff = a * PSF(star i) + c
            chis=[]
            for i in range(len(stars)):
                g=gauss_img(X[i]+dx,Y[i]+dy,sig,ny,nx)
                Am=np.vstack([g.ravel(),np.ones(g.size)]).T
                cc,res,_,_=np.linalg.lstsq(Am,diff.ravel(),rcond=None)
                chis.append((np.sum((Am@cc-diff.ravel())**2),cc[0]))
            # free-position PSF fit
            def rr(p): return (p[2]*gauss_img(p[0],p[1],sig,ny,nx)+p[3]-diff).ravel()
            pf=least_squares(rr,[x0,y0,diff.max()*2*np.pi*sig**2,0]).x
            # convert pixel offsets to arcsec using WCS
            def sky(xp,yp): return w.all_pix2world([[xp-dx,yp-dy]],0)[0]
            ra_c,de_c=sky(pf[0],pf[1]); 
            off=lambda ra,de: 3600*np.hypot((ra-stars[0]['ra'])*np.cos(np.radians(de)),de-stars[0]['dec'])
            ra_w,de_w=sky(cx,cy)
            best=np.argmin([c[0] for c in chis]); chi0=chis[0][0]
            # observed depth in aperture, dilution: depth needed on star i
            dep=fr['p']['d']; edep=fr['e']['d']
            print(f'  {kind} n={k} mid~{tcen:.3f} N_in={nin} N_out={nout} | own-aperture depth {1e3*dep:.2f}±{1e3*edep:.2f} ppt (t0 {fr["p"]["t0"]:.4f}±{fr["e"]["t0"]:.4f}) | '
                  f'max per-pixel frac depth {1e3*np.nanmax(np.where(box,pix_frac,np.nan)):.1f} ppt at pix ({np.nanargmax(np.where(box,pix_frac,-1))%nx},{np.nanargmax(np.where(box,pix_frac,-1))//nx}); target model pix ({x0:.2f},{y0:.2f})')
            print(f'     deficit PSF-fit position offset from target {off(ra_c,de_c):.1f}" (dpix {pf[0]-x0:+.2f},{pf[1]-y0:+.2f}); weighted-centroid offset {off(ra_w,de_w):.1f}"; direct-image centroid shift (diff-centroid minus direct-centroid) {np.hypot(cx-dcx,cy-dcy)*21:.1f}"')
            print(f'     single-source fits: best = star {best} (sep {stars[best]["sep"]:.1f}", G {stars[best]["G"]:.2f}); chi2(target)={chi0:.4g}; ' +
                  '; '.join(f'{stars[i]["sep"]:.0f}"/G{stars[i]["G"]:.1f}: dchi2={chis[i][0]-chi0:+.3g}' for i in range(1,len(stars)) if stars[i]['sep']<65))
            summary.append(dict(sector=sec,kind=kind,n=k,depth=dep,edep=edep,t0=fr['p']['t0'],et0=fr['e']['t0'],psf_off=off(ra_c,de_c),wc_off=off(ra_w,de_w),best=int(best),
                                dchi=[chis[i][0]-chi0 for i in range(len(stars))]))
            if kind=='P' and k==evs[0][0] and sec in (17,56,12,100):
                np.save(f's11_diff_{tic}_s{sec}_{kind}{k}.npy',dict(diff=diff,oot=oot,x0=x0,y0=y0,X=X+dx,Y=Y+dy,G=[s['G'] for s in stars]),allow_pickle=True)
    # dilution arithmetic for this sector's aperture (primary and secondary depth from stack)
    print('  dilution (aperture flux fraction f_i; required intrinsic depth = observed/f_i, observed from s08 stack: P %.1f ppt, S %.1f ppt):'%(1e3*sh['P']['d'],1e3*sh['S']['d']))
    for i,s in enumerate(stars):
        if i==0: continue
        if frac[i]<1e-4: print(f'     {s["sep"]:.1f}" G{s["G"]:.2f} T{s["T"]:.2f}: f<1e-4 -> excluded'); continue
        print(f'     {s["sep"]:.1f}" G{s["G"]:.2f} T{s["T"]:.2f}: f={frac[i]:.4f}  needs P {100*sh["P"]["d"]/frac[i]:.0f}%  S {100*sh["S"]["d"]/frac[i]:.1f}%')
json.dump(summary,open(f's11_pixels_{tic}.json','w'),indent=1)
