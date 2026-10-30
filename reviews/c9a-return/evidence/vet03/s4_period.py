import numpy as np, json, sys
from scipy.optimize import least_squares
from lcio import load, trap
tic=sys.argv[1]
G={'70665829':dict(P=3.46588776746830707,eP=2.8460746e-04,thr=150e-3,win=0.30,T14=0.12),
   '331293467':dict(P=5.25654668202362618,eP=5.3649350e-04,thr=30e-3,win=0.55,T14=0.17)}[tic]
ev=json.load(open(f's3_events_{tic}.json'))
ev=[e for e in ev if e['D']>0.02 and e['eD']<0.01]
prim=[e for e in ev if e['D']>G['thr']]; sec=[e for e in ev if e['D']<=G['thr']]
def linfit(ts,es,P0):
    ts=np.array(ts); es=np.array(es); T0r=ts[np.argmin(np.abs(ts-np.median(ts)))]
    n=np.round((ts-T0r)/P0); A=np.vstack([np.ones_like(n),n]).T; W=1/es**2
    C=np.linalg.inv(A.T@(A*W[:,None])); p=C@(A.T@(W*ts)); res=ts-A@p
    chi2=np.sum(res**2*W); dof=len(ts)-2; s=max(1,np.sqrt(chi2/dof)) if dof>0 else 1
    return p, np.sqrt(np.diag(C))*s, res, n, chi2/dof if dof>0 else np.nan
out={}
def report(label,sel,P0):
    if len(sel)<2: print(label,'too few'); return None
    ts=[e['t0'] for e in sel]; es=[max(e['et0'],1e-4) for e in sel]
    p,pe,res,n,rc=linfit(ts,es,P0)
    print(f"{label}: N={len(sel)} T0={p[0]:.5f}+-{pe[0]:.5f} P={p[1]:.7f}+-{pe[1]:.7f} chi2r={rc:.2f} O-C rms={np.std(res)*1440:.2f} min  (P-Pgaia)/sig_comb={(p[1]-G['P'])/np.hypot(pe[1],G['eP']):+.2f}  (P-Pgaia)/eGaia={(p[1]-G['P'])/G['eP']:+.2f}")
    return p,pe
for pipe in ['SPOC','QLP']:
    pp=[e for e in prim if e['pipe']==pipe]; ss=[e for e in sec if e['pipe']==pipe]
    if not pp: continue
    print(f'== {pipe}')
    r1=report(f'{pipe} primaries',pp,G['P'])
    r2=report(f'{pipe} secondaries',ss,G['P']) if len(ss)>=2 else None
    if r1 and r2:
        P=r1[0][1]; T0p=r1[0][0]
        # secondary phase from joint-P: fit secondaries with P fixed at primary P
        ts=np.array([e['t0'] for e in ss]); es=np.array([max(e['et0'],1e-4) for e in ss])
        ph=((ts-T0p)/P)%1; W=1/es**2; m=np.sum(ph*W)/W.sum(); 
        sc=np.sqrt(max(1,np.sum((ph-m)**2*W)/(len(ph)-1)))
        em=np.sqrt(1/W.sum())/P*sc; em=np.hypot(em,np.hypot(r1[1][0]/P, r1[1][1]*np.mean(np.abs((ts-T0p)/P))/P))
        print(f"{pipe} secondary phase (P fixed to primaries) = {m:.5f} +- {em:.5f}; implied e cos w ~ pi/2*(phi-0.5) = {np.pi/2*(m-0.5):+.5f} +- {np.pi/2*em:.5f}")
        out[pipe]=dict(T0=T0p,eT0=r1[1][0],P=P,eP=r1[1][1],phi2=m,ephi2=em)
    for lab,sel in [('primary',pp),('secondary',ss)]:
        if len(sel)<4: continue
        P=r1[0][1]; T0=r1[0][0]
        n=np.round((np.array([e['t0'] for e in sel])-T0)/P).astype(int); D=np.array([e['D'] for e in sel]); eD=np.array([e['eD'] for e in sel]); sector=np.array([e['sector'] for e in sel])
        # odd/even within each sector to remove sector-dependent dilution
        diffs=[];errs=[]
        for s in np.unique(sector):
            m=sector==s; o=m&(n%2==1); ev_=m&(n%2==0)
            if o.sum() and ev_.sum():
                wo=1/eD[o]**2; we=1/eD[ev_]**2
                do=np.sum(D[o]*wo)/wo.sum(); de=np.sum(D[ev_]*we)/we.sum()
                sdo=max(np.sqrt(1/wo.sum()), np.std(D[o])/np.sqrt(o.sum()) if o.sum()>1 else 0); sde=max(np.sqrt(1/we.sum()), np.std(D[ev_])/np.sqrt(ev_.sum()) if ev_.sum()>1 else 0)
                diffs.append(do-de); errs.append(np.hypot(sdo,sde))
                print(f"  {pipe} {lab} s{s}: odd {do*1e3:.2f}+-{sdo*1e3:.2f} ppt (n={o.sum()}), even {de*1e3:.2f}+-{sde*1e3:.2f} ppt (n={ev_.sum()})")
        diffs=np.array(diffs); errs=np.array(errs); w=1/errs**2
        print(f"  {pipe} {lab} odd-even weighted mean = {np.sum(diffs*w)/w.sum()*1e3:+.2f} +- {np.sqrt(1/w.sum())*1e3:.2f} ppt")
    for lab,sel in [('primary',pp),('secondary',ss)]:
        if sel:
            print(f"  {pipe} {lab} T14 median {np.median([e['T14'] for e in sel]):.2f} h (range {min(e['T14'] for e in sel):.2f}-{max(e['T14'] for e in sel):.2f}); T23 median {np.median([e['T23'] for e in sel]):.2f} h; depth by sector: "+'; '.join(f"s{s}: {np.median([e['D'] for e in sel if e['sector']==s])*1e3:.1f} ppt (n={sum(1 for e in sel if e['sector']==s)})" for s in sorted(set(e['sector'] for e in sel))))
json.dump(out,open(f's4_ephem_{tic}.json','w'),indent=1)
