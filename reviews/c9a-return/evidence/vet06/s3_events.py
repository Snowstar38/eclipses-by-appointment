# Individual eclipse fits from raw SAP (QUALITY==0): locate primary & secondary in a coarse fold at the screen P,
# then fit each event with a supersampled trapezoid on a local quadratic baseline. Errors: covariance scaled
# to residual rms, inflated by a residual-shift (prayer-bead, 10 shifts) scatter. Then linear ephemerides,
# odd/even depths, secondary phase. Output: events_<tic>.csv + stdout.
import numpy as np, csv, sys, warnings
from scipy.optimize import curve_fit
warnings.filterwarnings('ignore')
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet06'
CFG={'468827621':(11.0411,0.30),'416285595':(4.6154,0.20)}   # screen P, T14 guess (d)
def trap(t,tc,d,T14,f23):
    T23=f23*T14; x=np.abs(t-tc); y=np.zeros_like(t)
    y[x<=T23/2]=d; ing=(x>T23/2)&(x<T14/2); y[ing]=d*(T14/2-x[ing])/max((T14-T23)/2,1e-6); return y
def model(t,cad,tc,d,T14,f23,c0,c1,c2):
    ns=max(1,int(round(cad/0.0023)));  off=(np.arange(ns)-(ns-1)/2)/ns*cad
    tt=t[:,None]+off[None,:]; tr=trap(tt.ravel(),tc,d,T14,f23).reshape(tt.shape).mean(1)
    dt=t-tc; return (c0+c1*dt+c2*dt**2)*(1-tr)
def fit_event(t,f,cad,tp,T14g,dg,W):
    w=np.abs(t-tp)<W; tw=t[w]; fw=f[w]
    if len(tw)<20: return None,'lost'
    inn=np.abs(tw-tp)<T14g/2; cov=inn.sum()*cad/T14g
    pre=(tw<tp-T14g/2).sum()*cad; post=(tw>tp+T14g/2).sum()*cad
    if cov<0.4 or pre<0.08 or post<0.08: return None,f'lost(cov={cov:.2f},pre={pre:.2f},post={post:.2f})'
    fn=lambda tt,*p: model(tt,cad,*p); best=None
    lo=[tp-0.1,0,0.4*T14g,0,0.5,-1,-5]; hi=[tp+0.1,0.6,2.0*T14g,0.95,1.5,1,5]
    for f23 in [0.0,0.3,0.6]:
        try:
            po,pc=curve_fit(fn,tw,fw,p0=[tp,dg,T14g,f23,np.median(fw[~inn]),0,0],bounds=(lo,hi),maxfev=20000)
            chi=np.sum((fw-fn(tw,*po))**2)
            if best is None or chi<best[2]: best=(po,pc,chi)
        except Exception: pass
    if best is None: return None,'fitfail'
    po,pc,chi=best; res=fw-fn(tw,*po); s=np.std(res); pc=pc*(s**2/(chi/max(1,len(tw)-7)))
    pb=[]
    for k in np.linspace(0,len(tw)-1,11).astype(int)[1:]:
        try: pb.append(curve_fit(fn,tw,fn(tw,*po)+np.roll(res,k),p0=po,bounds=(lo,hi),maxfev=4000)[0][:3])
        except Exception: pass
    pb=np.array(pb); e=np.sqrt(np.diag(pc))[:3]
    if len(pb)>3: e=np.maximum(e,pb.std(0))
    return dict(tc=po[0],e_tc=e[0],d=po[1],e_d=e[1],T14=po[2],T23=po[2]*po[3],rms=s,n=len(tw),cov=cov),'ok'
out=open('s3_events.out','w')
def pr(*a):
    print(*a); print(*a,file=out)
for tic,(P,T14g) in CFG.items():
    z=np.load(f'{D}/{tic}/lc_sap_q0.npz'); t,f,S,PP=z['t'],z['f'],z['s'],z['p']
    # per-sector 2-d running median for the coarse search only
    fd=f.copy()
    for k in set(zip(S,PP)):
        m=(S==k[0])&(PP==k[1]); tt=t[m]; ff=f[m]
        fd[m]=ff/np.array([np.median(ff[np.abs(tt-x)<1.0]) for x in tt])
    q=PP=='QLP'; ref=t[q][0]
    ph=np.mod((t[q]-ref)/P,1); bins=np.linspace(0,1,401); bm=np.array([np.median(fd[q][(ph>=a)&(ph<b)]) if ((ph>=a)&(ph<b)).sum()>3 else 1 for a,b in zip(bins[:-1],bins[1:])])
    i1=np.argmin(bm); T0=ref+(bins[i1]+0.00125)*P; d1=1-bm[i1]
    phr=np.mod(bins[:-1]+0.00125-bins[i1]-0.00125,1); mask=(phr>0.06)&(phr<0.94); i2=np.where(mask)[0][np.argmin(bm[mask])]
    ph2=phr[i2]; d2=1-bm[i2]
    pr(f'===== {tic}: coarse fold at P={P}: primary T0~{T0:.3f} depth~{1e3*d1:.0f} ppt; deepest other bin at phase {ph2:.4f} depth~{1e3*d2:.1f} ppt')
    rows=[]
    for kind,phk,dg in [('P',0.0,d1),('S',ph2,max(d2,0.002))]:
        for k in sorted(set(zip(S,PP))):
            m=(S==k[0])&(PP==k[1]); tt=t[m]; ff=f[m]; cad=np.median(np.diff(tt))
            for n in range(int(np.floor((tt.min()-T0)/P))-1,int(np.ceil((tt.max()-T0)/P))+1):
                tp=T0+(n+phk)*P
                if tp<tt.min()-0.2 or tp>tt.max()+0.2: continue
                r,st=fit_event(tt,ff,cad,tp,T14g,dg,max(0.6,1.6*T14g))
                rows.append(dict(kind=kind,epoch=n,pipe=k[1],sector=k[0],pred=round(tp,4),status=st,**({} if r is None else {kk:(round(v,6) if isinstance(v,float) else v) for kk,v in r.items()})))
    keys=['kind','epoch','pipe','sector','pred','status','tc','e_tc','d','e_d','T14','T23','rms','n','cov']
    with open(f'events_{tic}.csv','w',newline='') as fo:
        w=csv.DictWriter(fo,fieldnames=keys); w.writeheader(); [w.writerow(r) for r in rows]
    for r in rows:
        if r['status']=='ok': pr(f"  {r['kind']} E{r['epoch']:4d} {r['pipe']:4s} s{r['sector']}: tc={r['tc']:.5f}+-{r['e_tc']:.5f} depth={1e3*r['d']:.2f}+-{1e3*r['e_d']:.2f} ppt T14={24*r['T14']:.2f} h T23={24*r['T23']:.2f} h rms={1e3*r['rms']:.2f} ppt cov={r['cov']:.2f}")
        else: pr(f"  {r['kind']} E{r['epoch']:4d} {r['pipe']:4s} s{r['sector']}: pred {r['pred']} {r['status']}")
    # ephemerides
    ok=[r for r in rows if r['status']=='ok' and r['e_tc']<0.01]
    for kind in ['P','S']:
        R=[r for r in ok if r['kind']==kind]
        if len(R)<2: pr(f'  {kind}: <2 events'); continue
        # one value per epoch: prefer SPOC if both? take weighted mean of pipelines
        ep={}
        for r in R: ep.setdefault(r['epoch'],[]).append(r)
        E=np.array(sorted(ep)); tc=[];et=[]
        for e_ in E:
            a=np.array([x['tc'] for x in ep[e_]]); b=np.array([x['e_tc'] for x in ep[e_]]); wgt=1/b**2
            tc.append(np.sum(a*wgt)/wgt.sum()); et.append(max(1/np.sqrt(wgt.sum()), np.std(a) if len(a)>1 else 0))
        tc=np.array(tc); et=np.array(et)
        A=np.vstack([np.ones_like(E),E]).T; Wm=np.diag(1/et**2)
        cv=np.linalg.inv(A.T@Wm@A); p=cv@A.T@Wm@tc; res=tc-A@p; chi=np.sum(res**2/et**2)/max(1,len(E)-2)
        sc=max(1,np.sqrt(chi)); e0,eP=np.sqrt(np.diag(cv))*sc
        pr(f'  {kind} ephemeris: N_epochs={len(E)} T0={p[0]:.5f}+-{e0:.5f} P={p[1]:.6f}+-{eP:.6f} d; O-C rms={1440*np.std(res):.2f} min; red.chi2={chi:.2f}')
        pr(f'     O-C (min): '+' '.join(f'E{int(a)}:{1440*b:+.1f}' for a,b in zip(E,res)))
        if kind=='P': Tp0,Pp,eT0,ePp=p[0],p[1],e0,eP
        else: Ts0,Ps,eTs0,ePs=p[0],p[1],e0,eP
        # odd/even by pipeline
        for pipe in ['QLP','SPOC']:
            dd=[(x['epoch'],x['d'],x['e_d']) for x in R if x['pipe']==pipe]
            if len(dd)<2: continue
            dd=np.array(dd); o=dd[dd[:,0]%2==1]; ev=dd[dd[:,0]%2==0]
            def wm(a): 
                if len(a)==0: return np.nan,np.nan
                w_=1/a[:,2]**2; return np.sum(a[:,1]*w_)/w_.sum(), max(1/np.sqrt(w_.sum()), np.std(a[:,1])/np.sqrt(len(a)) if len(a)>1 else 0)
            mo,eo=wm(o); me,ee=wm(ev); mall=np.mean(dd[:,1]); sall=np.std(dd[:,1])
            pr(f'     {pipe} depth: mean {1e3*mall:.2f} ppt (sd {1e3*sall:.2f}, N={len(dd)}); odd {1e3*mo:.2f}+-{1e3*eo:.2f} even {1e3*me:.2f}+-{1e3*ee:.2f} -> {(mo-me)/np.hypot(eo,ee):+.2f} sigma')
    # joint: secondary phase with common P
    S_=[r for r in ok if r['kind']=='S']; P_=[r for r in ok if r['kind']=='P']
    if len(S_)>=1:
        phs=np.array([np.mod((r['tc']-Tp0)/Pp,1) for r in S_]); eph=np.array([np.hypot(r['e_tc'],np.hypot(eT0,ePp*abs((r['tc']-Tp0)/Pp)))/Pp for r in S_])
        w_=1/eph**2; m=np.sum(phs*w_)/w_.sum(); em=max(1/np.sqrt(w_.sum()), np.std(phs)/np.sqrt(len(phs)) if len(phs)>1 else 0)
        pr(f'  secondary phase from primary ephemeris: {m:.5f}+-{em:.5f} (N={len(phs)}, sd {np.std(phs):.5f})')
        np.save(f's3_ephem_{tic}.npy',np.array([Tp0,eT0,Pp,ePp,m,em]))
out.close()
