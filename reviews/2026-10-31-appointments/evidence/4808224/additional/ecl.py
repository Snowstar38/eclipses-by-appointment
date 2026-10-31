"""Trapezoid + quadratic baseline fit to each eclipse from raw SAP_FLUX (all finite cadences, quality reported).
Nelder-Mead in numpy; errors from residual bootstrap (prayer-bead-free: resample residual blocks)."""
import numpy as np, json
from astropy.io import fits
D='[local path omitted]'
EV=[('008',1526.84),('009',1551.91),('035',2279.34),('062',3006.76),('089',3734.18)]
def trap(t,tc,dep,T14,T12,cad):
    # supersample to cadence
    ns=7; off=(np.arange(ns)-(ns-1)/2)/ns*cad
    tt=(t[:,None]+off[None,:]); x=np.abs(tt-tc); T12=min(max(T12,1e-4),T14/2)
    m=np.where(x<=T14/2-T12,dep,np.where(x<T14/2,dep*(T14/2-x)/T12,0.))
    return 1-m.mean(1)
def nm(f,x0,st,it=3000):
    n=len(x0); S=[np.array(x0,float)]+[np.array(x0,float)+np.eye(n)[i]*st[i] for i in range(n)]; F=[f(s) for s in S]
    for _ in range(it):
        o=np.argsort(F); S=[S[i] for i in o]; F=[F[i] for i in o]; c=np.mean(S[:-1],0)
        xr=c+(c-S[-1]); fr=f(xr)
        if fr<F[0]:
            xe=c+2*(c-S[-1]); fe=f(xe); S[-1],F[-1]=(xe,fe) if fe<fr else (xr,fr)
        elif fr<F[-2]: S[-1],F[-1]=xr,fr
        else:
            xc=c+0.5*(S[-1]-c); fc=f(xc)
            if fc<F[-1]: S[-1],F[-1]=xc,fc
            else: S=[S[0]+0.5*(s-S[0]) for s in S]; F=[f(s) for s in S]
    return S[int(np.argmin(F))]
res=[]
for s,tg in EV:
    d=fits.open(D+f'4808224_s{s}.fits')[1].data; t=d['TIME'];f=d['SAP_FLUX'];q=d['QUALITY']
    g=np.isfinite(t)&np.isfinite(f)&(np.abs(t-tg)<1.0)
    t,f,q=t[g],f[g],q[g]; bkg=d['SAP_BKG'][g]; x=d['SAP_X'][g]; y=d['SAP_Y'][g]
    cad=np.median(np.diff(t)); f=f/np.median(f[np.abs(t-tg)>0.4])
    def model(p,t=t): tc,dep,T14,T12,a0,a1,a2=p; u=t-tg; return trap(t,tc,dep,T14,T12,cad)*(a0+a1*u+a2*u*u)
    def chi(p,t=t,f=f):
        if p[2]<0.02 or p[2]>1.5 or p[1]<0 or p[3]<0.002 or p[3]>p[2]/2: return 1e9
        return np.sum((f-model(p,t))**2)
    p=nm(chi,[tg,0.05,0.25,0.1,1,0,0],[0.02,0.005,0.05,0.03,0.002,0.002,0.002])
    p=nm(chi,p,[0.005,0.002,0.02,0.01,0.001,0.001,0.001])
    r=f-model(p); sd=np.std(r)
    # bootstrap by cyclic residual shift (keeps red noise)
    B=[]; rng=np.random.default_rng(1)
    for k in range(60):
        fb=model(p)+np.roll(r,rng.integers(len(r)))
        B.append(nm(lambda pp:chi(pp,t,fb),p,[0.003,0.002,0.01,0.005,0.001,0.001,0.001],800))
    B=np.array(B); e=B.std(0)
    inn=np.abs(t-p[0])<p[2]/2; out=(np.abs(t-p[0])>p[2]/2+0.05)
    r1=dict(sector=s,tc=p[0],tc_err=e[0],depth=p[1],depth_err=e[1],T14_h=p[2]*24,T14_err_h=e[2]*24,T12_h=p[3]*24,T12_err_h=e[3]*24,
            flat_h=(p[2]-2*p[3])*24,rms=sd,cad_min=cad*1440,n_in=int(inn.sum()),n_in_flag=int((inn&(q!=0)).sum()),
            flags_in=sorted(set(int(v) for v in q[inn&(q!=0)])),
            bkg_in_minus_out=float(np.median(bkg[inn])-np.median(bkg[out])),bkg_out_sd=float(np.std(bkg[out])),
            dx=float(np.median(x[inn])-np.median(x[out])),dy=float(np.median(y[inn])-np.median(y[out])),
            xsd=float(np.std(x[out])/np.sqrt(max(inn.sum(),1))),ysd=float(np.std(y[out])/np.sqrt(max(inn.sum(),1))))
    res.append(r1); print({k:(round(v,5) if isinstance(v,float) else v) for k,v in r1.items()})
json.dump(res,open('ecl.json','w'),indent=1)
