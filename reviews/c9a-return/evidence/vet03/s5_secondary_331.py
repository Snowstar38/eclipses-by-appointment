import numpy as np, json
from scipy.optimize import least_squares
from lcio import load, trap
eph=dict(T0=4066.68168,P=5.2568187)
T14=4.07/24; r=0.83/4.07; win=0.55
lcs=load('331293467')
def fitone(t,f,cad,tc,free_t0=True):
    m=np.abs(t-tc)<win; tt=t[m]; ff=f[m]
    if m.sum()<15: return None
    inn=np.sum(np.abs(tt-tc)<T14/2); 
    if inn< 0.5*T14/cad: return None
    if free_t0:
        mod=lambda p:(p[2]+p[3]*(tt-tc)+p[4]*(tt-tc)**2)*trap(tt,p[0],p[1],T14,r,cad)
        p0=[tc,0.01,1,0,0]; lb=[tc-0.15,-0.1,0.5,-1,-10]; ub=[tc+0.15,0.2,1.5,1,10]
        best=None
        for dt in (-0.08,0,0.08):
            p0[0]=tc+dt; s=least_squares(lambda p:mod(p)-ff,p0,bounds=(lb,ub))
            if best is None or s.cost<best.cost: best=s
        s=best
    else:
        mod=lambda p:(p[1]+p[2]*(tt-tc)+p[3]*(tt-tc)**2)*trap(tt,tc,p[0],T14,r,cad)
        s=least_squares(lambda p:mod(p)-ff,[0.01,1,0,0])
    rms=np.std(s.fun); C=np.linalg.inv(s.jac.T@s.jac)*rms**2; e=np.sqrt(np.diag(C))
    return s.x,e,inn
rows=[]
for lc in lcs:
    t,f,cad=lc['t'],lc['f'],lc['cad']
    n0=int(np.floor((t.min()-eph['T0'])/eph['P']))-1; n1=int(np.ceil((t.max()-eph['T0'])/eph['P']))+1
    for n in range(n0,n1+1):
        for ph,lab in [(0.5,'sec'),(0.25,'null25'),(0.75,'null75')]:
            tc=eph['T0']+(n+ph)*eph['P']
            if tc<t.min()-0.1 or tc>t.max()+0.1: continue
            a=fitone(t,f,cad,tc, free_t0=(lab=='sec'))
            if a is None: continue
            x,e,inn=a
            if lab=='sec': rows.append(dict(kind=lab,sector=lc['sector'],n=n,tpred=tc,t0=x[0],et0=e[0],D=x[1],eD=e[1],nin=int(inn)))
            else: rows.append(dict(kind=lab,sector=lc['sector'],n=n,tpred=tc,t0=tc,et0=0,D=x[0],eD=e[0],nin=int(inn)))
print('kind sector cycle t_pred t0 et0 depth_ppt eD_ppt n_in')
for R in rows: print(f"{R['kind']:7s} {R['sector']:4d} {R['n']:4d} {R['tpred']:.4f} {R['t0']:.4f} {R['et0']:.4f} {R['D']*1e3:6.2f} {R['eD']*1e3:5.2f} {R['nin']}")
for k in ['sec','null25','null75']:
    D=np.array([R['D'] for R in rows if R['kind']==k]); eD=np.array([R['eD'] for R in rows if R['kind']==k]); w=1/eD**2
    print(f"{k}: N={len(D)} weighted mean depth {np.sum(D*w)/w.sum()*1e3:.2f} +- {np.sqrt(1/w.sum())*1e3:.2f} ppt; median {np.median(D)*1e3:.2f}; scatter {np.std(D)*1e3:.2f}")
# secondary timing: linear fit with P free and phase
S=[R for R in rows if R['kind']=='sec' and R['D']>3*R['eD'] and R['et0']<0.05]
ts=np.array([R['t0'] for R in S]); es=np.array([R['et0'] for R in S])
ph=((ts-eph['T0'])/eph['P'])%1; w=1/es**2; m=np.sum(ph*w)/w.sum(); sc=np.sqrt(max(1,np.sum((ph-m)**2*w)/(len(ph)-1)))
em=np.sqrt(1/w.sum())/eph['P']*sc
print(f"individually significant secondaries (D>3sig): {len(S)}; mean phase {m:.4f} +- {em:.4f} (P,T0 fixed from primaries; T0/P errors add <0.0001)")
print(f"implied e cos w ~ pi/2*(phi-0.5) = {np.pi/2*(m-0.5):+.4f} +- {np.pi/2*em:.4f}")
A=np.vstack([np.ones(len(ts)),np.floor((ts-eph['T0'])/eph['P'])]).T; C=np.linalg.inv(A.T@(A*w[:,None])); p=C@(A.T@(w*ts)); res=ts-A@p; rc=np.sum(res**2*w)/(len(ts)-2)
print(f"secondary-only linear ephemeris: P={p[1]:.6f}+-{np.sqrt(C[1,1]*max(1,rc)):.6f} chi2r={rc:.2f}")
json.dump(rows,open('s5_secondary_331293467.json','w'),indent=1,default=float)
