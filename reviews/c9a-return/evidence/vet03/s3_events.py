import numpy as np, sys, json
from scipy.optimize import least_squares
from scipy.ndimage import median_filter
from lcio import load, trap
cfg={'70665829':dict(P=3.46588776746830707,win=0.30,T14=0.13,medwin=0.8),
     '331293467':dict(P=5.25654668202362618,win=0.55,T14=0.24,medwin=1.5)}
def blind(t,f,medwin,nsig=5):
    # running median in time (approx via index window using cadence)
    cad=np.median(np.diff(t)); n=int(medwin/cad)|1
    base=median_filter(f,size=n,mode='nearest'); r=f-base
    mad=1.4826*np.median(np.abs(r-np.median(r)))
    low=r<-nsig*mad
    ev=[]; i=0
    while i<len(t):
        if low[i]:
            j=i
            while j+1<len(t) and low[j+1] and t[j+1]-t[j]<5*cad: j+=1
            if j-i+1>=3: k=i+np.argmin(r[i:j+1]); ev.append((t[k],-r[k],j-i+1))
            i=j+1
        else: i+=1
    return ev,mad
def fit_event(t,f,cad,tc,win,T14g):
    m=np.abs(t-tc)<win; tt=t[m]; ff=f[m]
    if m.sum()<15: return None
    # coverage: require points on both sides of eclipse
    def model(p): t0,D,T14,r,a0,a1,a2=p; x=tt-tc; return (a0+a1*x+a2*x*x)*trap(tt,t0,D,T14,r,cad)
    p0=[tt[np.argmin(ff)],1-ff.min()/np.median(ff),T14g,0.2,np.median(ff),0,0]
    lb=[tc-win/2,0,0.02,0,0.5,-1,-10]; ub=[tc+win/2,1,win*1.6,0.95,1.5,1,10]
    p0=np.clip(p0,np.array(lb)+1e-6,np.array(ub)-1e-6)
    best=None
    for r0 in (0.05,0.4,0.8):
        p0[3]=r0
        s=least_squares(lambda p: model(p)-ff,p0,bounds=(lb,ub))
        if best is None or s.cost<best.cost: best=s
    s=best; res=s.fun; rms=np.std(res); J=s.jac
    try: cov=np.linalg.inv(J.T@J)*rms**2; err=np.sqrt(np.diag(cov))
    except Exception: err=np.full(len(s.x),np.nan)
    t0,D,T14,r=s.x[:4]
    pre=np.sum((tt>tc-win)&(tt<t0-T14/2)); post=np.sum((tt<tc+win)&(tt>t0+T14/2)); inn=np.sum(np.abs(tt-t0)<T14/2)
    expected_in=T14/cad
    return dict(t0=t0,et0=err[0],D=D,eD=err[1],T14=T14*24,eT14=err[2]*24,T23=r*T14*24,rms=rms,npre=int(pre),npost=int(post),nin=int(inn),fill=inn/expected_in)
tic=sys.argv[1]; c=cfg[tic]; P=c['P']
lcs=load(tic); rows=[]
for lc in lcs:
    ev,mad=blind(lc['t'],lc['f'],c['medwin'])
    print(f"# {lc['pipe']} s{lc['sector']} cad={lc['cad']*1440:.1f}min good={lc['ngood']}/{lc['ntot']} span {lc['tstart']:.2f}-{lc['tend']:.2f} mad={mad*1e3:.2f}ppt blind dips: "+', '.join(f'{e[0]:.3f}({e[1]*1e3:.0f}ppt,n{e[2]})' for e in ev))
    for e in ev:
        r=fit_event(lc['t'],lc['f'],lc['cad'],e[0],c['win'],c['T14'])
        if r: r.update(pipe=lc['pipe'],sector=lc['sector'],blind_amp=e[1]); rows.append(r)
# dedupe blind detections within 0.1 d per pipeline
rows.sort(key=lambda r:(r['pipe'],r['t0']))
ded=[]
for r in rows:
    if ded and ded[-1]['pipe']==r['pipe'] and abs(ded[-1]['t0']-r['t0'])<0.1: 
        if r['D']>ded[-1]['D']: ded[-1]=r
        continue
    ded.append(r)
json.dump(ded,open(f's3_events_{tic}.json','w'),indent=1,default=float)
print('pipe sec  t0  et0  depth(ppt) eD  T14h eT14 T23h rms_ppt npre nin npost fill')
for r in ded:
    print(f"{r['pipe']:4s} {r['sector']:4d} {r['t0']:.5f} {r['et0']:.5f} {r['D']*1e3:7.2f} {r['eD']*1e3:5.2f} {r['T14']:5.2f} {r['eT14']:4.2f} {r['T23']:5.2f} {r['rms']*1e3:5.2f} {r['npre']:4d} {r['nin']:4d} {r['npost']:4d} {r['fill']:.2f}")
