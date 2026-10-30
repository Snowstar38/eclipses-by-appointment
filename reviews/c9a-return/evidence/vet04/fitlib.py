import numpy as np
from scipy.optimize import least_squares
def trap(t,t0,d,T14,r23):
    """trapezoid: depth d (fraction), total T14 (d), T23 = r23*T14"""
    T23=r23*T14; x=np.abs(t-t0); m=np.zeros_like(t)
    tin=(T14-T23)/2
    full=x<=T23/2; m[full]=d
    ing=(x>T23/2)&(x<T14/2)
    m[ing]=d*(T14/2-x[ing])/max(tin,1e-6)
    return m
def model(p,t,texp,tref,nsub=7):
    t0,d,T14,r23,c0,c1,c2=p
    if texp>0.003:
        off=(np.arange(nsub)-(nsub-1)/2)/nsub*texp
        tt=(t[:,None]+off[None,:]).ravel()
        m=trap(tt,t0,d,T14,r23).reshape(len(t),nsub).mean(1)
    else: m=trap(t,t0,d,T14,r23)
    x=t-tref
    return (c0+c1*x+c2*x*x)*(1-m)
def fit_event(t,f,texp,t0g,dg,T14g,win,fix=None,r23g=0.3):
    """fix: dict of params to fix among 'T14','r23','t0','d'"""
    sel=np.abs(t-t0g)<win; t=t[sel]; f=f[sel]
    if len(t)<10: return None
    names=['t0','d','T14','r23','c0','c1','c2']
    p0=dict(t0=t0g,d=dg,T14=T14g,r23=r23g,c0=np.median(f),c1=0,c2=0)
    lo=dict(t0=t0g-0.3,d=-0.5,T14=0.02,r23=0.0,c0=0.5,c1=-1,c2=-1)
    hi=dict(t0=t0g+0.3,d=0.9,T14=1.5,r23=0.98,c0=1.5,c1=1,c2=1)
    fix=fix or {}
    free=[n for n in names if n not in fix]
    def full(q):
        d=dict(fix); d.update(dict(zip(free,q))); return [d[n] for n in names]
    res=lambda q: model(full(q),t,texp,t0g)-f
    r=least_squares(res,[p0[n] for n in free],bounds=([lo[n] for n in free],[hi[n] for n in free]),x_scale='jac')
    resid=r.fun; rms=np.std(resid)
    J=r.jac
    try: cov=np.linalg.inv(J.T@J)*rms**2; err=np.sqrt(np.diag(cov))
    except Exception: err=np.full(len(free),np.nan)
    # red-noise beta from binned residuals (~1 h bins)
    nb=max(1,int(round(0.0417/max(np.median(np.diff(t)),1e-4))))
    if nb>1 and len(resid)>4*nb:
        k=len(resid)//nb; bres=resid[:k*nb].reshape(k,nb).mean(1)
        beta=max(1.0,np.std(bres)/(rms/np.sqrt(nb))*np.sqrt(k/(k-1)))
    else: beta=1.0
    pf=dict(zip(names,full(r.x))); pe={n:(err[free.index(n)]*beta if n in free else 0.0) for n in names}
    # coverage: fraction of in-eclipse span (T14) covered by data
    inn=np.abs(t-pf['t0'])<pf['T14']/2
    cov_frac=np.sum(inn)*np.median(np.diff(t))/pf['T14']
    pre=np.sum((t<pf['t0']-pf['T14']/2)); post=np.sum(t>pf['t0']+pf['T14']/2)
    return dict(p=pf,e=pe,rms=rms,beta=beta,n=len(t),cov=cov_frac,npre=pre,npost=post,t=t,f=f,res=resid)
