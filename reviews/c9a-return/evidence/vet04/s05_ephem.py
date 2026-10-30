# (a) linear ephemerides from individual primary mid-times; (b) fold-shape (fixed T14,T23) refits of every event; (c) secondary phase; (d) odd/even
from common import *; from fitlib import *; import json
rows=json.load(open('s04_events.json'))
def linfit(n,t,e):
    w=1/e**2; A=np.vstack([np.ones_like(n),n]).T
    C=np.linalg.inv(A.T@(A*w[:,None])); p=C@(A.T@(w*t))
    res=t-A@p; chi2=np.sum(w*res**2); dof=len(t)-2
    s=np.sqrt(max(1,chi2/dof)) if dof>0 else 1
    return p, np.sqrt(np.diag(C))*s, res, chi2, dof, C*s*s
out={}
for tic in GAIA:
    print('=====',tic); g=GAIA[tic]
    R=[r for r in rows if r['tic']==tic and r['status'] in('ok','partial') and 't0' in r]
    # choose one measurement per event: TESS-SPOC where available and ok, else QLP ok
    best={}
    for r in R:
        k=(r['kind'],r['n'])
        if r['status']!='ok': continue
        if k not in best or r['author']=='TESS-SPOC': best[k]=r
    for kind in 'PS':
        E=sorted([v for k,v in best.items() if k[0]==kind],key=lambda r:r['n'])
        n=np.array([r['n'] for r in E],float); t=np.array([r['t0'] for r in E]); e=np.array([r['et0'] for r in E])
        p,pe,res,chi2,dof,C=linfit(n,t,e)
        print(kind,'N=%d'%len(E),'T0=%.5f±%.5f P=%.6f±%.6f chi2/dof=%.1f/%d'%(p[0],pe[0],p[1],pe[1],chi2,dof))
        for r,rr in zip(E,res): print('   n=%d %s s%d t0=%.4f±%.4f O-C=%+.1f min (%.1f sig)'%(r['n'],r['author'],r['sector'],r['t0'],r['et0'],rr*1440,rr/r['et0']))
        out[(tic,kind)]=dict(p=p,pe=pe,C=C)
        if kind=='P':
            print('   P vs Gaia: %.6f±%.6f vs %.6f±%.6f : diff %.6f d = %.2f sigma_gaia (%.2f sigma combined)'%(p[1],pe[1],g['P'],g['eP'],p[1]-g['P'],(p[1]-g['P'])/g['eP'],(p[1]-g['P'])/np.hypot(g['eP'],pe[1])))
    pP=out[(tic,'P')]; pS=out[(tic,'S')]
    print('P_sec - P_pri = %.6f ± %.6f d'%(pS['p'][1]-pP['p'][1],np.hypot(pS['pe'][1],pP['pe'][1])))
    # joint fit: common P, separate T0P,T0S
    E=sorted(best.values(),key=lambda r:(r['kind'],r['n']))
    A=np.array([[1 if r['kind']=='P' else 0, 1 if r['kind']=='S' else 0, r['n']] for r in E],float)
    tt=np.array([r['t0'] for r in E]); ee=np.array([r['et0'] for r in E]); w=1/ee**2
    C=np.linalg.inv(A.T@(A*w[:,None])); q=C@(A.T@(w*tt)); res=tt-A@q; chi2=np.sum(w*res**2); dof=len(tt)-3; s2=max(1,chi2/dof); C=C*s2
    pe=np.sqrt(np.diag(C))
    ph=(q[1]-q[0])/q[2]; # phase of secondary
    J=np.array([-1/q[2],1/q[2],-(q[1]-q[0])/q[2]**2]); eph=np.sqrt(J@C@J)
    print('JOINT: T0P=%.5f±%.5f T0S=%.5f±%.5f P=%.6f±%.6f chi2/dof=%.1f/%d'%(q[0],pe[0],q[1],pe[1],q[2],pe[2],chi2,dof))
    print('JOINT: secondary phase = %.5f ± %.5f'%(ph%1,eph))
    print('   P(joint) vs Gaia: diff %.6f d = %.2f sigma_gaia'%(q[2]-g['P'],(q[2]-g['P'])/g['eP']))
    json.dump(dict(T0P=q[0],eT0P=pe[0],T0S=q[1],eT0S=pe[1],P=q[2],eP=pe[2],ph2=ph%1,eph2=eph,C=C.tolist()),open(f's05_ephem_{tic}.json','w'),indent=1)
