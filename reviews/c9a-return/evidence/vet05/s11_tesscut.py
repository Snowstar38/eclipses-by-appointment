# Own TESScut photometry + difference images + neighbour dilution, one cube per call.
# usage: python s11_tesscut.py <tic> <cube.fits> [--delete]
# Outputs: s11_<tic>_s<sec>.json (events, depths, centroids, dilution), s11_<tic>_s<sec>_lc.npz (aperture LCs),
#          s11_<tic>_s<sec>_diff.npz (per-event in/out median images). Cube deleted only with --delete after outputs are written.
import sys, os, json, numpy as np, csv
from astropy.io import fits
from astropy.wcs import WCS
from scipy.optimize import least_squares
from scipy.special import erf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fitlib import fit_event
HERE=os.path.dirname(os.path.abspath(__file__))
tic, cube = sys.argv[1], sys.argv[2]
EXCL=[a.split('=')[1] for a in sys.argv if a.startswith('--exclude=')]
EXCL=EXCL[0].split(',') if EXCL else []   # e.g. P124: events left out of the difference-image stack
TAG=[a.split('=')[1] for a in sys.argv if a.startswith('--tag=')]
TAG=TAG[0] if TAG else ''
EPH=json.load(open(f'{HERE}/s7_ephem.json'))[f'{tic}_joint']
SH=json.load(open(f'{HERE}/s6_shape.json'))
P,T0,phS=EPH['P'],EPH['T0'],EPH['phaseS']
shape={k:(SH[f'{tic}_{k}']['depth'],SH[f'{tic}_{k}']['T14_d'],SH[f'{tic}_{k}']['T23_d']) for k in 'PS'}
# stars: target + neighbours (G<18, <90")
stars=[]
for r in csv.DictReader(open(f'{HERE}/../neighbours_90as.csv')):
    if r['tic']!=tic: continue
    G=float(r['Gmag']); br=float(r['BP_RP']) if r['BP_RP'] else 1.0
    Tm=G-0.00522555*br**3+0.0891337*br**2-0.633923*br+0.0324473   # Stassun+2019 Gaia->TESS
    stars.append(dict(source_id=r['source_id'],ra=float(r['ra']),dec=float(r['dec']),G=G,Tmag_est=Tm,sep=float(r['sep_arcsec'])))
stars.sort(key=lambda s:s['sep']); tgt=stars[0]
h=fits.open(cube); d=h[1].data; sec=int(h[0].header['SECTOR'])
wcs=WCS(h[2].header)
t=np.array(d['TIME'],float); F=np.array(d['FLUX'],float); q=np.array(d['QUALITY'])
good=np.isfinite(t)&(q==0)&np.all(np.isfinite(F.reshape(len(t),-1)),axis=1)
t=t[good]; F=F[good]
ny,nx=F.shape[1:]
for s in stars:
    x,y=wcs.all_world2pix(s['ra'],s['dec'],0); s['x']=float(x); s['y']=float(y)
xt,yt=tgt['x'],tgt['y']; ix,iy=int(round(xt)),int(round(yt))
med=np.median(F,axis=0)
# residual sky: pixels >3 px from target and below 40th percentile of the median image
YY,XX=np.mgrid[0:ny,0:nx]
far=np.hypot(XX-xt,YY-yt)>3
skym=far&(med<np.percentile(med[far],40))
sky=np.median(F[:,skym],axis=1)
Fs=F-sky[:,None,None]
medS=np.median(Fs,axis=0)
aps={'1px':(XX==ix)&(YY==iy),
     '3x3':(abs(XX-ix)<=1)&(abs(YY-iy)<=1),
     'r1.5':np.hypot(XX-xt,YY-yt)<=1.5,
     'r2.5':np.hypot(XX-xt,YY-yt)<=2.5}
lcs={k:Fs[:,m].sum(1) for k,m in aps.items()}
for s_ in stars[1:]:
    if s_['G']<16.5:
        jx,jy=int(round(s_['x'])),int(round(s_['y']))
        if 0<=jx<nx and 0<=jy<ny: lcs[f"nb_{s_['source_id']}_1px"]=Fs[:,jy,jx]
lcs={k:v/np.median(v) for k,v in lcs.items()}
texp=np.median(np.diff(t))
np.savez_compressed(f'{HERE}/s11_{tic}_s{sec}{TAG}_lc.npz',t=t,sky=sky,**lcs)
out=dict(tic=tic,sector=sec,excluded_from_diff=EXCL,camera=int(h[0].header['CAMERA']),ccd=int(h[0].header['CCD']),cube=os.path.basename(cube),
         n_good=int(good.sum()),cad_min=texp*1440,target_xy=[xt,yt],sky_npix=int(skym.sum()),
         rms_ppt={k:1e3*float(np.std(np.diff(v))/np.sqrt(2)) for k,v in lcs.items()},events=[])
# ---- per-event fits on each aperture (shape fixed from s6) ----
diffs=[]
for kind,off in [('P',0.0),('S',phS)]:
    dep0,T14,T23=shape[kind]
    n0=int(np.floor((t.min()-T0)/P-off))-1; n1=int(np.ceil((t.max()-T0)/P-off))+1
    for n in range(n0,n1+1):
        tc=T0+(n+off)*P
        if tc<t.min()-T14 or tc>t.max()+T14: continue
        win=np.abs(t-tc)<3*T14; inn=np.abs(t-tc)<T14/2
        pre=((t[win]-tc)<-T14/2).sum(); post=((t[win]-tc)>T14/2).sum()
        rec=dict(kind=kind,epoch=n,tpred=tc,n_in=int(inn.sum()),n_in_expected=float(T14/texp),pre=int(pre),post=int(post))
        if inn.sum()<0.5*T14/texp or pre<3 or post<3:
            rec['status']='LOST/PARTIAL (gap or flags)'; out['events'].append(rec); continue
        rec['status']='OK'
        for k,lc in lcs.items():
            if np.median(lc)<=0: continue
            p,ep,rms,beta=fit_event(t[win],lc[win],texp,tc,dep0,T14,T23,fix_shape=True)
            rec[k]=dict(tc=p[0],etc=ep[0],dep=p[1],edep=ep[1],rms=rms,beta=beta)
        # difference-image windows: centre of eclipse vs flanks
        cin=np.abs(t-tc)<max(0.3*T14/2*2,1.01*texp/2) if False else np.abs(t-tc)<max(0.30*T14,0.6*texp)
        cout=(np.abs(t-tc)>1.0*T14)&(np.abs(t-tc)<2.0*T14)
        if cin.sum()>=1 and cout.sum()>=4 and f'{kind}{n}' not in EXCL:
            Iin=np.median(Fs[cin],axis=0); Iout=np.median(Fs[cout],axis=0)
            diffs.append((kind,n,Iin,Iout,int(cin.sum()),int(cout.sum())))
        out['events'].append(rec)
# ---- difference images: stack per kind, fit PSF, compare with stars ----
def pixgauss(x0,y0,sig):
    gx=0.5*(erf((XX+0.5-x0)/(np.sqrt(2)*sig))-erf((XX-0.5-x0)/(np.sqrt(2)*sig)))
    gy=0.5*(erf((YY+0.5-y0)/(np.sqrt(2)*sig))-erf((YY-0.5-y0)/(np.sqrt(2)*sig)))
    return gx*gy
def fitpsf(img,x0,y0,w=None,fixpos=False,sig0=0.8):
    w=np.ones_like(img) if w is None else w
    if fixpos:
        def res(p): return ((img-(p[0]*pixgauss(x0,y0,p[1])+p[2]))*w).ravel()
        r=least_squares(res,[img.max()*2,sig0,0],bounds=([-np.inf,0.3,-np.inf],[np.inf,3,np.inf])); return r
    def res(p): return ((img-(p[0]*pixgauss(p[1],p[2],p[3])+p[4]))*w).ravel()
    r=least_squares(res,[img.max()*2,x0,y0,sig0,0],bounds=([-np.inf,x0-3,y0-3,0.3,-np.inf],[np.inf,x0+3,y0+3,3,np.inf]))
    return r
# direct image: fit target PSF within 5x5 box of the out-of-eclipse median (neighbours are faint/offset)
box=(abs(XX-ix)<=2)&(abs(YY-iy)<=2)
rd=fitpsf(np.where(box,medS,0),xt,yt,w=box.astype(float))
xd,yd,sigd=rd.x[1],rd.x[2],rd.x[3]
out['direct_fit']=dict(x=xd,y=yd,sigma_px=sigd,offset_from_wcs_arcsec=21*float(np.hypot(xd-xt,yd-yt)))
# fake-event noise: same windows at random out-of-eclipse epochs
rng=np.random.default_rng(int(tic)%1000+sec)
def ecl_mask(tt):
    m=np.zeros(len(tt),bool)
    for kind,off in [('P',0.0),('S',phS)]:
        ph=((tt-T0)/P-off+0.5)%1-0.5
        m|=np.abs(ph*P)<2.5*shape[kind][1]
    return m
okfake=~ecl_mask(t)
np.savez_compressed(f'{HERE}/s11_{tic}_s{sec}{TAG}_diff.npz',kinds=np.array([x[0] for x in diffs]),epochs=np.array([x[1] for x in diffs]),
                    Iin=np.array([x[2] for x in diffs]) if diffs else np.zeros((0,ny,nx)),Iout=np.array([x[3] for x in diffs]) if diffs else np.zeros((0,ny,nx)),
                    medS=medS,xy=np.array([[s['x'],s['y']] for s in stars]))
out['diff']={}
for kind in 'PS':
    D=[x for x in diffs if x[0]==kind]
    if not D: continue
    T14=shape[kind][1]
    dimg=np.mean([x[3]-x[2] for x in D],axis=0)        # out - in: positive where flux is lost
    oimg=np.mean([x[3] for x in D],axis=0)
    # noise: 200 fake stacks of len(D) fake events
    fk=[]
    cand=t[okfake]
    cand=cand[(cand>t.min()+2.5*T14)&(cand<t.max()-2.5*T14)]
    for k in range(200):
        acc=[]
        for tc in rng.choice(cand,len(D)):
            if not okfake[np.argmin(abs(t-tc))]: continue
            cin=np.abs(t-tc)<max(0.30*T14,0.6*texp); cout=(np.abs(t-tc)>1.0*T14)&(np.abs(t-tc)<2.0*T14)
            if cin.sum()<1 or cout.sum()<4 or ecl_mask(t[cin|cout]).any(): continue
            acc.append(np.median(Fs[cout],axis=0)-np.median(Fs[cin],axis=0))
        if acc: fk.append(np.mean(acc,axis=0))
    fk=np.array(fk); noise=np.std(fk,axis=0); w=1/np.maximum(noise,1e-6)
    r=fitpsf(dimg,xd,yd,w=w,sig0=sigd)
    J=r.jac; cov=np.linalg.pinv(J.T@J)*(np.sum(r.fun**2)/(r.fun.size-5)); e=np.sqrt(np.diag(cov))
    # empirical centroid error: fit fake stacks with injected scaled direct-image PSF
    inj=[]
    amp=r.x[0]
    for f_ in fk[:100]:
        rr=fitpsf(f_+amp*pixgauss(xd,yd,sigd),xd,yd,w=w,sig0=sigd); inj.append(rr.x[1:3])
    inj=np.array(inj); einj=np.std(inj,axis=0)
    ex=max(e[1],einj[0]); ey=max(e[2],einj[1])
    dx,dy=r.x[1]-xd,r.x[2]-yd
    res=dict(n_events=len(D),epochs=[int(x[1]) for x in D],amp=float(amp),x=float(r.x[1]),y=float(r.x[2]),sigma=float(r.x[3]),
             ex_px=float(ex),ey_px=float(ey),offset_arcsec=21*float(np.hypot(dx,dy)),
             offset_sigma=float(np.hypot(dx/ex,dy/ey)),frac_depth_peak_pixel=None,stars=[])
    fr=np.where(oimg>0.05*oimg.max(),dimg/np.maximum(oimg,1),np.nan)
    j=np.nanargmax(np.where(np.isfinite(fr)&(oimg>0.2*oimg.max()),fr,-np.inf))
    res['frac_depth_peak_pixel']=dict(x=int(XX.ravel()[j]),y=int(YY.ravel()[j]),frac=float(fr.ravel()[j]),
                                      target_pixel_frac=float(fr[iy,ix]))
    # chi2 of PSF fixed at each star position, amplitude/sigma/const free
    ox,oy=xd-xt,yd-yt   # WCS->PSF-frame offset measured on the target in the direct image; applied to all stars
    for s in stars:
        sx,sy=s['x']+ox,s['y']+oy
        rr=fitpsf(dimg,sx,sy,w=w,fixpos=True,sig0=sigd)
        dxs,dys=r.x[1]-sx,r.x[2]-sy
        res['stars'].append(dict(source_id=s['source_id'],G=s['G'],sep=s['sep'],chi2_fixed=float(np.sum(rr.fun**2)),
             centroid_dist_sigma=float(np.hypot(dxs/ex,dys/ey)),centroid_dist_arcsec=21*float(np.hypot(dxs,dys))))
    res['chi2_free']=float(np.sum(r.fun**2)); res['npix']=int(dimg.size)
    out['diff'][kind]=res
# ---- dilution arithmetic per aperture (Gaussian PSF with fitted sigma, and a 1.5x broader PSF) ----
dil={}
for k,m in aps.items():
    dil[k]={}
    for sigl,sg in [('sig',sigd),('sig1.5x',1.5*sigd)]:
        fl=[10**(-0.4*(s['Tmag_est']-10))*pixgauss(s['x']+xd-xt,s['y']+yd-yt,sg)[m].sum() for s in stars]
        tot=sum(fl)
        dil[k][sigl]=[dict(source_id=s['source_id'],G=s['G'],Tmag_est=s['Tmag_est'],sep=s['sep'],frac_in_ap=f_/tot) for s,f_ in zip(stars,fl)]
out['dilution']=dil
out['stars']=stars
json.dump(out,open(f'{HERE}/s11_{tic}_s{sec}{TAG}.json','w'),indent=1,default=float)
# ---- print summary ----
print(f'== TIC {tic} s{sec} cam{out["camera"]} ccd{out["ccd"]} N={len(t)} cad={texp*1440:.1f} min  target pix ({xt:.2f},{yt:.2f}); direct PSF fit ({xd:.2f},{yd:.2f}) sigma={sigd:.2f}px (offset from WCS {out["direct_fit"]["offset_from_wcs_arcsec"]:.1f}")')
print('   rms per point (ppt):',' '.join(f'{k}={v:.2f}' for k,v in out['rms_ppt'].items()))
for e in out['events']:
    if e['status']!='OK': print(f'   {e["kind"]} E{e["epoch"]} pred {e["tpred"]:.4f}: {e["status"]} (n_in={e["n_in"]}/{e["n_in_expected"]:.1f}, pre={e["pre"]}, post={e["post"]})'); continue
    print(f'   {e["kind"]} E{e["epoch"]} pred {e["tpred"]:.4f}: '+'  '.join(f'{k}: tc={e[k]["tc"]:.5f}±{e[k]["etc"]:.5f} d={1e3*e[k]["dep"]:.2f}±{1e3*e[k]["edep"]:.2f}ppt' for k in ['3x3','r2.5']))
for kind,res in out['diff'].items():
    print(f'   DIFF {kind}: {res["n_events"]} events {res["epochs"]}; deficit centroid ({res["x"]:.2f},{res["y"]:.2f}) ±({res["ex_px"]:.2f},{res["ey_px"]:.2f}) px; offset from target {res["offset_arcsec"]:.1f}" = {res["offset_sigma"]:.1f} sigma; peak frac-depth pixel ({res["frac_depth_peak_pixel"]["x"]},{res["frac_depth_peak_pixel"]["y"]}) {1e3*res["frac_depth_peak_pixel"]["frac"]:.1f} ppt (target pixel {1e3*res["frac_depth_peak_pixel"]["target_pixel_frac"]:.1f} ppt); chi2 free={res["chi2_free"]:.1f}/{res["npix"]} px')
    for s in res['stars']:
        print(f'      star (WCS pos + direct-image offset) G={s["G"]:.2f} sep={s["sep"]:5.1f}": PSF-fixed-there chi2={s["chi2_fixed"]:.1f}; centroid distance {s["centroid_dist_arcsec"]:.1f}" = {s["centroid_dist_sigma"]:.1f} sigma')
for e in out['events']:
    if e['status']=='OK':
        nbk=[k for k in e if k.startswith('nb_')]
        if nbk: print(f'   {e["kind"]} E{e["epoch"]} neighbour-pixel depths: '+' '.join(f'{k.split("_")[1][-6:]}: {1e3*e[k]["dep"]:.1f}±{1e3*e[k]["edep"]:.1f}ppt' for k in nbk)+f' | target 1px {1e3*e["1px"]["dep"]:.1f}±{1e3*e["1px"]["edep"]:.1f}')
for k in ['3x3','r2.5']:
    print(f'   dilution {k}:',' | '.join(f'G{s["G"]:.2f}@{s["sep"]:.0f}": {100*s["frac_in_ap"]:.2f}% ({100*s2["frac_in_ap"]:.2f}% broad)' for s,s2 in zip(dil[k]['sig'],dil[k]['sig1.5x'])))
if '--delete' in sys.argv:
    os.remove(cube); print('   deleted cube',os.path.basename(cube))
