"""Trapezoid fits (raw SAP, quadratic baseline) to each event in each available light curve.
python -X utf8 ecl.py  -> ecl.json, ecl_fits.png"""
import json, glob, os, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
from vetlib import fit_trap, model, t0_error
D='[local path omitted]'; V=D+'vet60583013/'
def find(pat):
    g=glob.glob(V+pat); return g[0] if g else None
F={'QLP6':D+'60583013_s006.fits','QLP33':D+'60583013_s033.fits',
   'TSPOC6':find('*tess-spoc*s0006*lc.fits'),'TSPOC33':find('*tess-spoc*s0033*lc.fits'),
   'TARS6':find('*tars*s0006*'),'TARS33':find('*tars*s0033*'),'TGLC6':find('*tglc*s0006*'),'ELE6':find('*eleanor*s0006*')}
def load(key, allq):
    with fits.open(F[key]) as h:
        d=h[1].data; c=d.columns.names
        t=np.array(d['TIME'],float)
        fc=[k for k in ('SAP_FLUX','RAW_FLUX','cal_aper_flux','aperture_flux','CORR_FLUX','FLUX') if k in c][0]
        f=np.array(d[fc],float)
        q=np.array(d['QUALITY'],int) if 'QUALITY' in c else np.zeros(len(t),int)
        bc=[k for k in ('SAP_BKG','FLUX_BKG','background','BKG') if k in c]
        bk=np.array(d[bc[0]],float) if bc else np.full(len(t),np.nan)
        xc=[k for k in ('MOM_CENTR1','SAP_X','centroid_x','X_CENTROID') if k in c]; yc=[k for k in ('MOM_CENTR2','SAP_Y','centroid_y','Y_CENTROID') if k in c]
        x=np.array(d[xc[0]],float) if xc else np.full(len(t),np.nan); y=np.array(d[yc[0]],float) if yc else np.full(len(t),np.nan)
    ok=np.isfinite(t)&np.isfinite(f)&(f>0)
    if not allq: ok&=q==0
    return t[ok],f[ok],q[ok],bk[ok],x[ok],y[ok],fc
JOBS=[('A',2210.97,k) for k in ('QLP33','QLP33all','TSPOC33','TARS33')]+[('B',2225.06,k) for k in ('QLP33','QLP33all','TSPOC33','TARS33')]+\
     [('B?',1478.9,k) for k in ('QLP6','QLP6all','TSPOC6','TARS6','TGLC6','ELE6')]
out=[]; fig,axs=plt.subplots(4,4,figsize=(20,14)); axs=axs.ravel()
for i,(kind,tc,key) in enumerate(JOBS):
    allq=key.endswith('all'); k=key[:-3] if allq else key
    if not F.get(k): print(kind,tc,key,'no file'); continue
    try: t,f,q,bk,x,y,fc=load(k,allq)
    except Exception as e: print(key,'load error',e); continue
    W=0.8 if kind=='A' else 0.7
    w=np.abs(t-tc)<W
    if w.sum()<15: print(kind,tc,key,'no data',w.sum()); continue
    t,f,q,bk,x,y=t[w],f[w],q[w],bk[w],x[w],y[w]; f=f/np.median(f)
    dep0=0.04 if kind=='A' else 0.004
    b,c2,s,tr=fit_trap(t,f,tc,dep0,0.36 if kind=='A' else 0.2,0.04)
    res=f-model(b,t,tr); dt=np.median(np.diff(t)); nb=max(1,int(round((1/24)/dt)))
    nn=len(res)//nb; beta=max(1.0,np.std(res[:nn*nb].reshape(nn,nb).mean(1))/(s/np.sqrt(nb))) if nn>5 else 1.0
    e=t0_error(t,f,b,tr,s,half=0.05 if kind=='A' else 0.2,n=401)*beta
    inn=np.abs(t-b[0])<max(b[2]/2-b[3],dt); outw=np.abs(t-b[0])>b[2]/2+0.05
    dbk=np.nanmedian(bk[inn])-np.nanmedian(bk[outw]) if inn.sum() else np.nan; sbk=np.nanstd(bk[outw])
    dx=np.nanmedian(x[inn])-np.nanmedian(x[outw]); dy=np.nanmedian(y[inn])-np.nanmedian(y[outw])
    sx=np.nanstd(x[outw])/np.sqrt(max(inn.sum(),1)); sy=np.nanstd(y[outw])/np.sqrt(max(inn.sum(),1))
    nfl=int((q[np.abs(t-b[0])<b[2]/2]!=0).sum())
    # chi2 improvement over baseline-only
    A=np.c_[np.ones_like(t),t-tr,(t-tr)**2]; cb,*_=np.linalg.lstsq(A,f,rcond=None); dchi=(np.sum((f-A@cb)**2)-c2)/s**2
    r=dict(kind=kind,tc=tc,key=key,col=fc,t0=b[0],et0=e,depth=b[1],T14_h=b[2]*24,T12_h=b[3]*24,flat_h=(b[2]-2*b[3])*24,rms=s,beta=beta,
           dbkg=dbk,bkg_sd=sbk,dx=dx,dy=dy,sx=sx,sy=sy,n=int(len(t)),span=[float(t.min()),float(t.max())],nflag_in=nfl,dchi2=dchi)
    out.append(r)
    print(f"{kind:2s} {key:9s} t0 {b[0]:.4f}+-{e*1440:5.1f}m dep {b[1]*100:6.3f}% T14 {b[2]*24:5.2f}h T12 {b[3]*24:4.2f}h flat {r['flat_h']:5.2f}h rms {s*1e6:5.0f} b {beta:.1f} dchi2 {dchi:7.0f} "
          f"dBKG {dbk:+.3g}(sd {sbk:.3g}) dxy {dx:+.4f}+-{sx:.4f},{dy:+.4f}+-{sy:.4f} nfl {nfl} span {t.min():.2f}-{t.max():.2f}")
    a=axs[i]; a.plot(t,f,'k.',ms=2); a.plot(t[q!=0],f[q!=0],'r.',ms=2); tt=np.linspace(t.min(),t.max(),800); a.plot(tt,model(b,tt,tr),'c-'); a.set_title(f'{kind} {key} {b[0]:.3f} {b[1]*100:.2f}%',fontsize=9)
plt.tight_layout(); plt.savefig('ecl_fits.png',dpi=55); json.dump(out,open('ecl.json','w'),indent=1)
