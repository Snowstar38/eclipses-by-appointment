import numpy as np, glob, csv
from astropy.io import fits
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet11'
VET='[local path omitted]'
def targets():
    T={}
    for r in csv.DictReader(open(f'{VET}/targets.csv')): T.setdefault(r['tic'],r)
    return T
def load_qlp(tic, col='SAP_FLUX', binmin=10.0):
    """QLP light curve, QUALITY==0, finite; per-segment (gap>0.5 d) median-normalised; binned to binmin minutes.
    returns t, f, seg_id, sector"""
    out=[]
    for fn in sorted(glob.glob(f'{D}/{tic}/**/hlsp_qlp*llc.fits',recursive=True)):
        h=fits.open(fn); d=h[1].data; sec=h[0].header['SECTOR']
        names=d.columns.names
        c=col
        if col=='DET':
            c='KSPSAP_FLUX' if 'KSPSAP_FLUX' in names else 'DET_FLUX'
        t=np.array(d['TIME'],float); f=np.array(d[c],float); q=np.array(d['QUALITY'])
        m=(q==0)&np.isfinite(t)&np.isfinite(f)&(f>0)
        t,f=t[m],f[m]
        if len(t)<50: continue
        # bin
        bw=binmin/1440.
        k=np.floor((t-t[0])/bw).astype(int)
        u,inv,cnt=np.unique(k,return_inverse=True,return_counts=True)
        tb=np.bincount(inv,t)/cnt; fb=np.bincount(inv,f)/cnt
        good=cnt>=max(1,int(0.5*np.median(cnt)))
        tb,fb=tb[good],fb[good]
        # segments
        br=np.where(np.diff(tb)>0.5)[0]+1
        for j,(a,b) in enumerate(zip(np.r_[0,br],np.r_[br,len(tb)])):
            if b-a<30: continue
            out.append((tb[a:b],fb[a:b]/np.median(fb[a:b]),sec))
    t=np.concatenate([o[0] for o in out]); f=np.concatenate([o[1] for o in out])
    seg=np.concatenate([np.full(len(o[0]),i) for i,o in enumerate(out)])
    sec=np.concatenate([np.full(len(o[0]),o[2]) for o in out])
    return t,f,seg,sec
def poly_cols(t,seg,order=3):
    cols=[]
    for s in np.unique(seg):
        m=seg==s; ts=t[m]; x=np.zeros_like(t)
        span=ts.max()-ts.min(); o=order if span>5 else 1
        xx=2*(t-ts.min())/max(span,1e-3)-1
        for k in range(o+1):
            c=np.zeros_like(t); c[m]=np.polynomial.legendre.legval(xx[m],[0]*k+[1]); cols.append(c)
    return np.array(cols).T
def harm_cols(t,P,t0,K):
    ph=2*np.pi*(t-t0)/P; cols=[]
    for k in range(1,K+1): cols+= [np.cos(k*ph),np.sin(k*ph)]
    return np.array(cols).T
def fit(t,f,seg,P,t0,K,order=3,clip=4.0,niter=4):
    A=np.hstack([poly_cols(t,seg,order),harm_cols(t,P,t0,K)]); npoly=A.shape[1]-2*K
    m=np.ones(len(t),bool)
    for _ in range(niter):
        c,*_=np.linalg.lstsq(A[m],f[m],rcond=None); r=f-A@c; s=1.4826*np.median(np.abs(r[m]))
        m=np.abs(r)<clip*s
    chi2=np.sum((r[m]/s)**2)
    return dict(c=c,npoly=npoly,mask=m,resid=r,sig=s,chi2=chi2,A=A,poly=A[:,:npoly]@c[:npoly],harm=c[npoly:])
def harm_model(ph,hc):
    K=len(hc)//2; y=np.zeros_like(ph)
    for k in range(1,K+1): y+=hc[2*k-2]*np.cos(2*np.pi*k*ph)+hc[2*k-1]*np.sin(2*np.pi*k*ph)
    return y
def conj_times(P,Tp,e,w_deg):
    """times (within one cycle after Tp) of conjunction A (nu=90-w) and B (nu=270-w)"""
    res=[]
    for nu in (np.radians(90-w_deg),np.radians(270-w_deg)):
        E=2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2),np.sqrt(1+e)*np.cos(nu/2))
        M=E-e*np.sin(E); res.append(Tp+(M/(2*np.pi)%1)*P)
    return res
def extrema(hc,n=4000):
    """minima and maxima of harmonic curve: returns list of (phase,value) for minima and maxima"""
    ph=np.arange(n)/n; y=harm_model(ph,hc)
    yl=np.roll(y,1); yr=np.roll(y,-1)
    mins=[(ph[i],y[i]) for i in np.where((y<yl)&(y<=yr))[0]]
    maxs=[(ph[i],y[i]) for i in np.where((y>yl)&(y>=yr))[0]]
    return sorted(mins,key=lambda a:a[1]), sorted(maxs,key=lambda a:-a[1]), ph, y
