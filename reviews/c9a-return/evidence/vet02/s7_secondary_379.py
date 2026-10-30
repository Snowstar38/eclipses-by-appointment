# TIC 379251709: search for and measure the shallow secondary. Raw SAP QUALITY==0, primaries masked,
# 1.5-d running-median detrend, fold on the eclipse ephemeris (s6), box scan over phase, trapezoid fit,
# then per-event depths at the fold-fixed shape.
import numpy as np, warnings
from scipy.optimize import curve_fit
warnings.filterwarnings('ignore')
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet02'
P=12.323912; T0=1961.25375
z=np.load(f'{D}/379251709/lc_sap_q0.npz')
def runmed(t,f,w,mask):
    out=np.empty_like(f)
    for i in range(len(t)):
        m=(np.abs(t-t[i])<w/2)&mask; out[i]=np.median(f[m]) if m.sum()>5 else np.nan
    return out
def detrended(pipe,exclude=()):
    T=[];F=[];S=[]
    for sec in np.unique(z['s'][z['p']==pipe]):
        if sec in exclude: continue
        m=(z['p']==pipe)&(z['s']==sec); t=z['t'][m]; f=z['f'][m]
        if np.median(np.diff(t))<0.005:  # bin 200-s data to 10 min for speed
            tb=np.floor((t-t[0])/0.006944); u=np.unique(tb)
            t=np.array([t[tb==k].mean() for k in u]); f=np.array([f[tb==k].mean() for k in u])
        ph=((t-T0)/P+0.5)%1-0.5
        mask=np.abs(ph*P)>0.15   # primary masked
        # trim 0.3 d after the start of every segment (segments split at gaps > 0.3 d): thermal/scattered-light ramps
        seg=np.r_[0,np.cumsum(np.diff(t)>0.3)]
        for g in np.unique(seg):
            st=t[seg==g].min(); mask&=~((seg==g)&(t<st+0.3))
        tr=runmed(t,f,1.5,mask)
        r=f/tr-1; ok=np.isfinite(r)&mask
        T.append(t[ok]);F.append(r[ok]);S.append(np.full(ok.sum(),sec))
    return np.concatenate(T),np.concatenate(F),np.concatenate(S)
def trap(x,c,d,w,f23):
    a=np.abs(x-c); y=np.zeros_like(x); T23=f23*w
    y[a<=T23/2]=d; i=(a>T23/2)&(a<w/2); y[i]=d*(w/2-a[i])/((w-T23)/2); return -y
out=open('s7_secondary_379.txt','w')
def pr(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
for pipe,excl in [('SPOC',()),('QLP',(24,25)),('QLP',())]:
    t,r,s=detrended(pipe,excl)
    ph=((t-T0)/P)%1
    sig=1.4826*np.median(np.abs(r-np.median(r)))
    # box scan, width 4.1 h
    wph=4.1/24/P; grid=np.arange(0.05,0.95,0.0005); snr=[]
    for g in grid:
        inb=np.abs(ph-g)<wph/2; n=inb.sum()
        snr.append(-np.mean(r[inb])/(np.std(r)/np.sqrt(n)) if n>5 else 0)
    snr=np.array(snr); k=np.argmax(snr)
    top=np.argsort(snr)[::-1]; peaks=[]
    for j in top:
        if all(abs(grid[j]-p)>0.02 for p in peaks): peaks.append(grid[j])
        if len(peaks)==4: break
    pr(f'{pipe} excl{excl}: N={len(t)} rms={1e3*np.std(r):.2f}ppt; box-scan best phase={grid[k]:.4f} S/N={snr[k]:.1f}; next peaks: '+', '.join(f'{p:.3f}(S/N {snr[np.argmin(abs(grid-p))]:.1f})' for p in peaks[1:]))
    sel=np.abs(ph-0.5)<0.1
    x=(ph[sel]-0.5)*P; y=r[sel]
    best=None
    for f23 in [0.1,0.5]:
        try:
            p,c=curve_fit(lambda x,c0,cc,d,w,f: c0+trap(x,cc,d,w,f),x,y,p0=[0,(grid[k]-0.5)*P if abs(grid[k]-0.5)<0.045 else 0.0,0.002,0.17,f23],bounds=([-0.01,-0.6,0,0.05,0],[0.01,0.6,0.02,0.4,0.95]))
            chi=np.sum((y-p[0]-trap(x,*p[1:]))**2)
            if best is None or chi<best[2]: best=(p,c,chi)
        except Exception as ex: pr('fitfail',ex)
    p,c,chi=best; rs=y-p[0]-trap(x,*p[1:]); sc=np.std(rs)
    _,c2=curve_fit(lambda x,c0,cc,d,w,f: c0+trap(x,cc,d,w,f),x,y,p0=p,sigma=np.full(len(y),sc),absolute_sigma=True,bounds=([-0.01,-0.6,0,0.05,0],[0.01,0.6,0.02,0.4,0.95]))
    e=np.sqrt(np.diag(c2))
    # bootstrap over events (resample sectors) for phase error
    pr(f'   trapezoid fit (phase 0.4-0.6): phase={0.5+p[1]/P:.5f}+-{e[1]/P:.5f} depth={1e3*p[2]:.2f}+-{1e3*e[2]:.2f}ppt T14={24*p[3]:.2f}+-{24*e[3]:.2f}h T23={24*p[3]*p[4]:.2f}h  depth S/N={p[2]/e[2]:.1f}')
    if pipe=='QLP' and excl==(24,25): ref=p
    if pipe=='SPOC': refS=p
# per-event depths, shape fixed at the QLP(excl 24,25) fold fit, local linear baseline
pr('Per-event secondary depths at fixed fold shape (center, T14, T23 from QLP fold), local linear baseline over +-0.5 d:')
for pipe in ['SPOC','QLP']:
    t,r,s=detrended(pipe,())
    n0=int(np.floor((t.min()-T0)/P))-1; n1=int(np.ceil((t.max()-T0)/P))+1
    for n in range(n0,n1+1):
        tc=T0+(n+0.5)*P+ref[1]
        w=np.abs(t-tc)<0.5
        if w.sum()<10: continue
        inn=np.abs(t[w]-tc)<ref[3]/2
        if inn.sum()< (0.6*ref[3]/np.median(np.diff(t[w]))): pr(f'  {pipe} s{int(s[w][0])} E{n} tc={tc:.3f} incomplete coverage ({inn.sum()} in-eclipse pts)'); continue
        tmpl=trap(t[w]-tc,0,1.0,ref[3],ref[4])
        A=np.vstack([np.ones(w.sum()),t[w]-tc,tmpl]).T
        coef,res,_,_=np.linalg.lstsq(A,r[w],rcond=None)
        rr=r[w]-A@coef; sc=np.std(rr); C=np.linalg.inv(A.T@A)*sc**2
        pr(f'  {pipe} s{int(s[w][0])} E{n} tc={tc:.3f} depth={1e3*coef[2]:.2f}+-{1e3*np.sqrt(C[2,2]):.2f} ppt (S/N {coef[2]/np.sqrt(C[2,2]):.1f})')
out.close()
