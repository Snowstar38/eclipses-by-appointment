# Noise-calibrated difference-image test (fills a gap in s11, whose "chi2" values were unweighted sums of squares).
# Per sector and eclipse kind: average the per-event difference images (median out - median in) over all usable events;
# per-pixel noise from 300 pseudo-events at random out-of-eclipse times with the same in/out windows;
# then (a) weighted single-source PSF fits for the target and every Gaia neighbour G<18 within 90" -> proper chi2 and dchi2,
# (b) free-position PSF fit with a noise-ensemble error on the offset, (c) fitted amplitude -> depth on target.
import sys, glob, json, csv, numpy as np
from astropy.io import fits; from astropy.wcs import WCS
from scipy.optimize import least_squares
from scipy.special import erf
sys.path.insert(0,'.'); from common import D
tic=sys.argv[1]; secs=[int(x) for x in sys.argv[2].split(',')] if len(sys.argv)>2 else None
eph=json.load(open(f's05_ephem_{tic}.json')); sh=json.load(open('s08_shape_oddeven.json'))[tic]['shape']
P=eph['P']; T0={'P':eph['T0P'],'S':eph['T0S']}
nb=[r for r in csv.DictReader(open('../neighbours_90as.csv')) if r['tic']==tic]
def tmag(G,br): return G-0.00522555*br**3+0.0891337*br**2-0.633923*br+0.0324473
stars=sorted([dict(ra=float(r['ra']),dec=float(r['dec']),G=float(r['Gmag']),T=tmag(float(r['Gmag']),float(r['BP_RP'])),sep=float(r['sep_arcsec'])) for r in nb],key=lambda s:s['sep'])
def gimg(x0,y0,sig,ny,nx):
    xe=np.arange(nx+1)-0.5; ye=np.arange(ny+1)-0.5
    gx=0.5*(erf((xe[1:]-x0)/(np.sqrt(2)*sig))-erf((xe[:-1]-x0)/(np.sqrt(2)*sig)))
    gy=0.5*(erf((ye[1:]-y0)/(np.sqrt(2)*sig))-erf((ye[:-1]-y0)/(np.sqrt(2)*sig)))
    return np.outer(gy,gx)
rng=np.random.default_rng(1)
out=[]
for fn in sorted(glob.glob(f'{D}/{tic}/tesscut/*astrocut.fits')):
    h=fits.open(fn); sec=int(h[0].header['SECTOR'])
    if secs and sec not in secs: continue
    d=h[1].data; w=WCS(h[2].header)
    t=np.array(d['TIME'],float); F=np.array(d['FLUX'],float); q=d['QUALITY']
    ok=(q==0)&np.isfinite(t)&np.all(np.isfinite(F.reshape(len(t),-1)),1); t=t[ok]; F=F[ok]; h.close()
    med=np.nanmedian(F,0); ny,nx=med.shape
    bpix=med<=np.percentile(med,30); F=F-np.array([np.median(f[bpix]) for f in F])[:,None,None]
    med=np.nanmedian(F,0)
    X=np.array([w.all_world2pix([[s['ra'],s['dec']]],0)[0] for s in stars]); fl=np.array([10**(-0.4*(s['T']-10)) for s in stars])
    def scene(p): return p[4]+p[3]*sum(fl[i]*gimg(X[i,0]+p[0],X[i,1]+p[1],p[2],ny,nx) for i in range(len(stars)))
    r=least_squares(lambda p:(scene(p)-med).ravel(),[0,0,0.7,med.max()/fl[0],0],bounds=([-2,-2,0.3,0,-500],[2,2,3,1e9,500]))
    dx,dy,sig,A,b=r.x; XX=X+[dx,dy]
    te=float(np.median(np.diff(t)))
    # all eclipse windows (to exclude from pseudo-events)
    T14max=max(sh['P']['T14'],sh['S']['T14'])
    def in_any_ecl(tt):
        m=np.zeros_like(tt,bool)
        for k_ in 'PS':
            ph=((tt-T0[k_])/P+0.5)%1-0.5; m|=np.abs(ph*P)<T14max/2+0.65
        return m
    for kind in 'PS':
        s_=sh[kind]; T14=s_['T14']; hin=0.5*s_['r23']*T14+0.25*(1-s_['r23'])*T14
        def mk(tc):
            inn=np.abs(t-tc)<hin; o=(np.abs(t-tc)>T14/2+0.05)&(np.abs(t-tc)<T14/2+0.6)
            return inn,o
        diffs=[];oots=[];ks=[]
        for k in range(int((t.min()-T0[kind])/P)-1,int((t.max()-T0[kind])/P)+2):
            tc=T0[kind]+k*P; inn,o=mk(tc)
            pre=np.sum(o&(t<tc)); post=np.sum(o&(t>tc))
            if inn.sum()*te<0.2*T14 or pre*te<0.15 or post*te<0.15: continue
            diffs.append(np.median(F[o],0)-np.median(F[inn],0)); oots.append(np.median(F[o],0)); ks.append(k)
        if not diffs: continue
        diff=np.mean(diffs,0); oot=np.mean(oots,0); nev=len(diffs)
        # pseudo-events: same windows, random centres, none overlapping an eclipse window, combined nev at a time
        bad=in_any_ecl(t); cand=t[(~bad)&(t>t.min()+0.7)&(t<t.max()-0.7)]
        fakes=[]
        tries=0
        while len(fakes)<300 and tries<20000:
            tries+=1; acc=[]
            for j in range(nev):
                tc=rng.choice(cand); inn,o=mk(tc)
                if inn.sum()*te<0.2*T14 or np.sum(o&(t<tc))*te<0.15 or np.sum(o&(t>tc))*te<0.15 or bad[(np.abs(t-tc)<T14/2+0.6)].any(): break
                acc.append(np.median(F[o],0)-np.median(F[inn],0))
            if len(acc)==nev: fakes.append(np.mean(acc,0))
        fakes=np.array(fakes); sigp=np.std(fakes,0); sigp=np.where(sigp>0,sigp,np.nanmax(sigp))
        W=1/sigp.ravel()
        def single(i,img):
            g=gimg(XX[i,0],XX[i,1],sig,ny,nx).ravel(); Am=np.vstack([g,np.ones(g.size)]).T
            cc=np.linalg.lstsq(Am*W[:,None],img.ravel()*W,rcond=None)[0]; return np.sum(((Am@cc-img.ravel())*W)**2),cc[0]
        res=[single(i,diff) for i in range(len(stars))]; chi=np.array([c[0] for c in res]); amp=np.array([c[1] for c in res])
        # null: no source (constant only)
        chi_null=np.sum(((diff.ravel()-np.average(diff.ravel(),weights=W**2))*W)**2)
        def freefit(img,p0):
            return least_squares(lambda p:((p[2]*gimg(p[0],p[1],sig,ny,nx)+p[3]-img).ravel())*W,p0).x
        pf=freefit(diff,[XX[0,0],XX[0,1],max(amp[0],1e-3),0])
        # offset error: refit best-fit target model + each of 100 pseudo-event noise images
        mod=pf[2]*gimg(pf[0],pf[1],sig,ny,nx)+pf[3]
        pos=np.array([freefit(mod+fk-np.mean(fakes,0),pf)[:2] for fk in fakes[:100]])
        epos=np.std(pos,0)
        def sky(xp,yp): return w.all_pix2world([[xp-dx,yp-dy]],0)[0]
        rac,dec_=sky(pf[0],pf[1]); cd=np.cos(np.radians(stars[0]['dec']))
        offE=3600*(rac-stars[0]['ra'])*cd; offN=3600*(dec_-stars[0]['dec'])
        # pixel scale from WCS (arcsec/pix)
        r1=sky(XX[0,0],XX[0,1]); r2=sky(XX[0,0]+1,XX[0,1]); ps=3600*np.hypot((r2[0]-r1[0])*cd,r2[1]-r1[1])
        targflux=A*fl[0]  # total target flux in scene model units
        dep_t=amp[0]/targflux
        snr=np.sqrt(max(chi_null-chi[0],0))
        print(f'=== {tic} s{sec} {kind}: {nev} events {ks}; pseudo-events {len(fakes)}; PSF sigma {sig:.2f} pix; pixel scale {ps:.1f}"; diff-image S/N (sqrt(chi2_null-chi2_target)) {snr:.1f}')
        print(f'    chi2(target)={chi[0]:.1f} for {nx*ny-2} dof; chi2(no source)={chi_null:.1f}; depth on target from PSF amplitude = {1e3*dep_t:.1f} ppt (of modelled target flux)')
        print(f'    free PSF fit: offset from target E {offE:+.1f}" N {offN:+.1f}" (|off| {np.hypot(offE,offN):.1f}" ; 1-sigma {ps*epos[0]:.1f}"/{ps*epos[1]:.1f}" in x/y)')
        for i in range(1,len(stars)):
            s=stars[i]
            if s['sep']>90: continue
            print(f'    neighbour {s["sep"]:5.1f}" G{s["G"]:5.2f}: chi2={chi[i]:8.1f} dchi2={chi[i]-chi[0]:+8.1f}  implied intrinsic depth if source {100*amp[i]/(A*fl[i]):.0f}%')
        out.append(dict(sector=sec,kind=kind,nev=nev,ks=ks,snr=snr,chi_t=chi[0],chi_null=chi_null,dchi=[float(c-chi[0]) for c in chi],dep_t=dep_t,offE=offE,offN=offN,eoff=[float(ps*epos[0]),float(ps*epos[1])],
                        seps=[s['sep'] for s in stars],G=[s['G'] for s in stars]))
        np.savez(f's13_diff_{tic}_s{sec}_{kind}.npz',diff=diff,sigp=sigp,oot=oot,XX=XX,G=[s['G'] for s in stars],sep=[s['sep'] for s in stars],pf=pf)
    del F
json.dump(out,open(f's13_pixnoise_{tic}{"_"+sys.argv[2].replace(",","-") if secs else ""}.json','w'),indent=1)
