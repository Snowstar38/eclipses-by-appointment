# Fit every individual eclipse event (raw SAP, QUALITY==0) with a supersampled trapezoid on a local
# quadratic baseline. Errors: max(scaled covariance, prayer-bead). Output: events_<tic>.csv
import numpy as np, csv, warnings
from scipy.optimize import curve_fit
warnings.filterwarnings('ignore')
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet02'
CFG={ # P, T0(primary guess), {kind: (phase offset, T14 guess d, half-window d)}
 '470235665':(10.3262,1795.742,{'pri':(0.0,0.27,0.65),'sec':(0.5235,0.355,0.75)}),
 '379251709':(12.3239,1961.237,{'pri':(0.0,0.145,0.40),'sec':(0.5,0.145,0.40)}),
}
def trap(t,tc,d,T14,f23):
    T23=f23*T14; x=np.abs(t-tc); y=np.zeros_like(t)
    full=x<=T23/2; y[full]=d
    ing=(x>T23/2)&(x<T14/2); y[ing]=d*(T14/2-x[ing])/((T14-T23)/2)
    return y
def model(t,cad,tc,d,T14,f23,c0,c1,c2):
    ns=7 if cad>0.004 else 1
    off=(np.arange(ns)-(ns-1)/2)/ns*cad
    tt=t[:,None]+off[None,:]
    tr=trap(tt.ravel(),tc,d,T14,f23).reshape(tt.shape).mean(1)
    dt=t-tc
    return (c0+c1*dt+c2*dt**2)*(1-tr)
rows=[]
for tic,(P,T0,kinds) in CFG.items():
    z=np.load(f'{D}/{tic}/lc_sap_q0.npz')
    for kind,(ph,T14g,W) in kinds.items():
        for pipe in ['QLP','SPOC']:
            for sec in np.unique(z['s'][z['p']==pipe]):
                m=(z['p']==pipe)&(z['s']==sec); t=z['t'][m]; f=z['f'][m]
                cad=np.median(np.diff(t))
                n0=int(np.floor((t.min()-T0)/P))-1; n1=int(np.ceil((t.max()-T0)/P))+1
                for n in range(n0,n1+1):
                    tp=T0+(n+ph)*P
                    if tp<t.min()-W or tp>t.max()+W: continue
                    w=np.abs(t-tp)<W; tw=t[w]; fw=f[w]
                    inn=np.abs(tw-tp)<T14g/2
                    pre=(tw<tp-T14g/2).sum()*cad; post=(tw>tp+T14g/2).sum()*cad
                    cov=inn.sum()*cad/T14g
                    status='full' if (cov>0.7 and pre>0.1 and post>0.1) else 'partial'
                    if cov<0.3 or (pre<0.05 and post<0.05):
                        rows.append(dict(tic=tic,kind=kind,epoch=n,pipe=pipe,sector=sec,status='lost',pred=round(tp,4),cov=round(cov,2)));continue
                    p0=[tp,0.1 if tic=='470235665' else 0.03,T14g,0.3,np.median(fw[~inn]) if (~inn).sum()>3 else 1,0,0]
                    lo=[tp-0.15,0,0.3*T14g,0,0.5,-1,-5]; hi=[tp+0.15,0.5,2.0*T14g,0.95,1.5,1,5]
                    if kind=='sec' and tic=='379251709': lo[0]=tp-0.6*P/12.3239*0.5; hi[0]=tp+0.6*0.5; p0[1]=0.002
                    try:
                        fn=lambda tt,*p: model(tt,cad,*p)
                        best=None
                        for f23 in [0.0,0.3,0.6]:
                            p0[3]=f23
                            try:
                                popt,pcov=curve_fit(fn,tw,fw,p0=p0,bounds=(lo,hi),maxfev=20000)
                                chi=np.sum((fw-fn(tw,*popt))**2)
                                if best is None or chi<best[2]: best=(popt,pcov,chi)
                            except Exception: pass
                        popt,pcov,chi=best
                        res=fw-fn(tw,*popt); dof=max(1,len(tw)-7); s=np.std(res)
                        # covariance with sigma=s
                        popt2,pcov2=curve_fit(fn,tw,fw,p0=popt,sigma=np.full(len(tw),s),absolute_sigma=True,bounds=(lo,hi),maxfev=20000)
                        etc=np.sqrt(pcov2[0,0]); ed=np.sqrt(pcov2[1,1])
                        # prayer bead
                        mod=fn(tw,*popt); pb_tc=[];pb_d=[]
                        for k in np.linspace(0,len(tw)-1,15).astype(int)[1:]:
                            try:
                                pp,_=curve_fit(fn,tw,mod+np.roll(res,k),p0=popt,bounds=(lo,hi),maxfev=5000)
                                pb_tc.append(pp[0]);pb_d.append(pp[1])
                            except Exception: pass
                        etc=max(etc,np.std(pb_tc)) if pb_tc else etc; ed=max(ed,np.std(pb_d)) if pb_d else ed
                        rows.append(dict(tic=tic,kind=kind,epoch=n,pipe=pipe,sector=sec,status=status,pred=round(tp,4),cov=round(cov,2),
                            tc=round(popt[0],5),e_tc=round(etc,5),depth_ppt=round(1e3*popt[1],2),e_depth_ppt=round(1e3*ed,2),
                            T14_h=round(24*popt[2],2),T23_h=round(24*popt[2]*popt[3],2),rms_ppt=round(1e3*s,2),npts=len(tw),cad_min=round(cad*1440,1)))
                    except Exception as ex:
                        rows.append(dict(tic=tic,kind=kind,epoch=n,pipe=pipe,sector=sec,status='fitfail',pred=round(tp,4),cov=round(cov,2)))
keys=['tic','kind','epoch','pipe','sector','status','pred','cov','tc','e_tc','depth_ppt','e_depth_ppt','T14_h','T23_h','rms_ppt','npts','cad_min']
for tic in CFG:
    with open(f'events_{tic}.csv','w',newline='') as fo:
        w=csv.DictWriter(fo,fieldnames=keys); w.writeheader()
        for r in sorted([r for r in rows if r['tic']==tic],key=lambda r:(r['kind'],r['epoch'],r['pipe'])): w.writerow(r)
print('done')
