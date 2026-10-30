# lcio: shared loaders and trapezoid fitter for vet01
import glob, numpy as np
from astropy.io import fits
from scipy.optimize import least_squares
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet01'
def load_qlp(tic, col='SAP_FLUX', q0=True):
    out={}
    for f in sorted(glob.glob(f'{D}/{tic}/**/hlsp_qlp*llc.fits',recursive=True)):
        h=fits.open(f); d=h[1].data; s=h[0].header['SECTOR']
        t=np.array(d['TIME'],float); y=np.array(d[col],float); q=np.array(d['QUALITY'])
        m=np.isfinite(t)&np.isfinite(y)
        if q0: m&=(q==0)
        texp=float(np.nanmedian(np.diff(t[np.isfinite(t)])))
        out[s]=dict(texp=texp,t=t[m],f=y[m]/np.nanmedian(y[m]),q=q[m],cam=h[0].header['CAMERA'],ccd=h[0].header['CCD'],
                    tall=t[np.isfinite(t)&np.isfinite(y)],qall=q[np.isfinite(t)&np.isfinite(y)],fall=y[np.isfinite(t)&np.isfinite(y)]/np.nanmedian(y[m]))
    return out
def trap(t,t0,d,T14,f23):
    T23=f23*T14; x=np.abs(t-t0); m=np.zeros_like(t)
    full=x<=T23/2; m[full]=d
    ing=(x>T23/2)&(x<T14/2)
    m[ing]=d*(T14/2-x[ing])/max((T14-T23)/2,1e-6)
    return m
def model(p,t,tref,texp=0.0):
    t0,d,T14,f23,a0,a1,a2=p
    u=t-tref
    if texp>0:
        k=np.linspace(-0.5,0.5,9)*texp
        tr=np.mean([trap(t+dk,t0,d,T14,f23) for dk in k],axis=0)
    else: tr=trap(t,t0,d,T14,f23)
    return (a0+a1*u+a2*u*u)*(1-tr)
def fit_event(t,f,t0g,dg,T14g,f23g=0.3,halfwin=None,fix_shape=None,texp=0.0):
    hw=halfwin or 1.5*T14g
    m=np.abs(t-t0g)<hw
    tt,ff=t[m],f[m]
    if len(tt)<10: return None
    # coverage: need points both sides and in centre
    pre=np.sum((tt<t0g-T14g/2)); post=np.sum(tt>t0g+T14g/2); cen=np.sum(np.abs(tt-t0g)<T14g/4)
    tref=t0g
    if fix_shape is None:
        p0=[t0g,dg,T14g,f23g,np.median(ff),0,0]
        lo=[t0g-T14g/3,0,T14g*0.4,0,0.5,-1,-1]; hi=[t0g+T14g/3,0.9,T14g*2.0,0.98,1.5,1,1]
        fun=lambda p: model(p,tt,tref,texp)-ff
    else:
        T14,f23=fix_shape
        p0=[t0g,dg,np.median(ff),0,0]
        lo=[t0g-T14/3,0,0.5,-1,-1]; hi=[t0g+T14/3,0.9,1.5,1,1]
        fun=lambda q: model([q[0],q[1],T14,f23,q[2],q[3],q[4]],tt,tref,texp)-ff
    r=least_squares(fun,p0,bounds=(lo,hi),x_scale='jac')
    res=r.fun; rms=np.std(res); J=r.jac
    try: cov=np.linalg.inv(J.T@J)*rms**2; err=np.sqrt(np.diag(cov))
    except Exception: err=np.full(len(r.x),np.nan)
    p=r.x if fix_shape is None else np.array([r.x[0],r.x[1],fix_shape[0],fix_shape[1],r.x[2],r.x[3],r.x[4]])
    e=err if fix_shape is None else np.array([err[0],err[1],np.nan,np.nan,err[2],err[3],err[4]])
    return dict(p=p,e=e,rms=rms,n=len(tt),pre=pre,post=post,cen=cen,tt=tt,ff=ff,tref=tref)
