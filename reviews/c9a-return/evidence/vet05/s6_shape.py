# Joint shape fit per star & eclipse kind: shared depth,T14,T23; per-event tc + quadratic baseline.
# Uses only fast-cadence raw SAP Q==0 data (<=10 min), events with status OK.
import numpy as np, json
from scipy.optimize import least_squares
from common import *
from fitlib import model
ev=json.load(open('s5_events.json'))
fast={'15855794':[('QLP',70),('QLP',71),('TESS-SPOC',44)],'92881948':[('QLP',98),('TESS-SPOC',32)]}
init={('15855794','P'):(0.037,0.135,0.027),('15855794','S'):(0.005,0.135,0.027),
      ('92881948','P'):(0.017,0.07,0.008),('92881948','S'):(0.005,0.07,0.008)}
res_out={}
for (tic,kind),(d0,T140,T230) in init.items():
    segs=[]
    for r in ev:
        if r['tic']!=tic or r['kind']!=kind or r['status']!='OK': continue
        if (r['pipe'],r['sector']) not in fast[tic]: continue
        t,f,e,q=load(tic,r['pipe'],r['sector'])
        m=np.abs(t-r['tpred'])<3*T140
        segs.append((t[m],f[m],np.median(np.diff(t)),r['tc_fix'],r['pipe'],r['sector'],r['epoch']))
    nE=len(segs)
    def unpack(q):
        return q[0],q[1],q[2],q[3:].reshape(nE,4)
    def resid(q):
        dep,T14,T23,pe=unpack(q); out=[]
        for (t,f,texp,tc0,_,_,_),p in zip(segs,pe):
            out.append((f-model([p[0],dep,T14,T23,p[1],p[2],p[3]],t,texp,tc0))/np.std(f[np.abs(t-tc0)>T140]))
        return np.concatenate(out)
    q0=[d0,T140,T230]+sum([[s[3],1,0,0] for s in segs],[])
    lb=[0,0.02,0]+[-np.inf]*4*nE; ub=[0.2,0.3,0.3]+[np.inf]*4*nE
    r=least_squares(resid,q0,bounds=(lb,ub))
    J=r.jac; chi2=np.sum(r.fun**2)/(len(r.fun)-len(q0))
    cov=np.linalg.pinv(J.T@J)*chi2; e=np.sqrt(np.diag(cov))
    dep,T14,T23,pe=unpack(r.x)
    T23=min(T23,T14)
    res_out[f'{tic}_{kind}']=dict(depth=dep,edepth=e[0],T14_d=T14,eT14_d=e[1],T23_d=T23,eT23_d=e[2],nevents=nE,redchi2=chi2)
    print('%s %s n_events=%d depth=%.2f±%.2f ppt T14=%.3f±%.3f h T23=%.3f±%.3f h redchi2=%.2f'%(tic,kind,nE,1e3*dep,1e3*e[0],T14*24,e[1]*24,T23*24,e[2]*24,chi2))
json.dump(res_out,open('s6_shape.json','w'),indent=1)
