# Per-event measurement on raw SAP, QUALITY==0, local quadratic baseline, trapezoid (supersampled)
import numpy as np, json, sys
from common import *
from fitlib import *
from astropy.io import fits
cfg={'15855794':dict(P=5.89118,T0=2503.1195,phs=0.5015,secs=[44,70,71],
        prim=(0.036,0.14,0.02),sec=(0.0045,0.12,0.03)),
     '92881948':dict(P=8.80498,T0=1445.1987,phs=0.4835,secs=[5,6,32,98],
        prim=(0.017,0.075,0.01),sec=(0.0055,0.07,0.02))}
out=[]
for tic,c in cfg.items():
    P,T0=c['P'],c['T0']
    for kind,phoff,(d0,T14,T23) in [('P',0.0,c['prim']),('S',c['phs'],c['sec'])]:
        for a in ['QLP','TESS-SPOC']:
            for s in c['secs']:
                r=load(tic,a,s,q0=False)
                if r is None: continue
                tall,fall,eall,qall=r
                r=load(tic,a,s); t,f,e,q=r
                texp=np.median(np.diff(t))
                n0=int(np.ceil((tall.min()-T0)/P-phoff-0.1)); n1=int(np.floor((tall.max()-T0)/P-phoff+0.1))
                for n in range(n0,n1+1):
                    tc=T0+(n+phoff)*P
                    win=3.0*T14
                    m=np.abs(t-tc)<win; inn=np.abs(t-tc)<T14/2
                    ma=np.abs(tall-tc)<T14/2
                    rec=dict(tic=tic,kind=kind,pipe=a,sector=s,epoch=n,tpred=round(tc,4),
                             n_in_q0=int(inn.sum()),n_in_all=int(ma.sum()),n_win=int(m.sum()))
                    exp_in=T14/texp
                    if inn.sum()<0.5*exp_in or (np.abs(t[m]-tc)<-0).any():
                        rec['status']='LOST (gap/flags)'; out.append(rec); continue
                    # require some coverage both sides
                    pre=((t[m]-tc)<-T14/2).sum(); post=((t[m]-tc)>T14/2).sum()
                    if pre<3 or post<3:
                        rec['status']='PARTIAL (one-sided baseline)'
                    tt,ff=t[m],f[m]
                    p,ep,rms,beta=fit_event(tt,ff,texp,tc,d0,T14,T23,fix_shape=True)
                    rec.update(tc_fix=p[0],etc_fix=ep[0],dep_fix=p[1],edep_fix=ep[1],rms=rms,beta=beta)
                    try:
                        p2,ep2,rms2,beta2=fit_event(tt,ff,texp,tc,d0,T14,T23,fix_shape=False)
                        rec.update(tc_free=p2[0],etc_free=ep2[0],dep_free=p2[1],edep_free=ep2[1],
                                   T14_h=abs(p2[2])*24,eT14_h=ep2[2]*24,T23_h=min(abs(p2[3]),abs(p2[2]))*24,eT23_h=ep2[3]*24)
                    except Exception as ex: rec['free_err']=str(ex)
                    rec.setdefault('status','OK')
                    out.append(rec)
json.dump(out,open('s5_events.json','w'),indent=1,default=float)
for r in out:
    if 'dep_fix' in r:
        print('%s %s %-9s s%-3d E%-4d pred=%.4f tc=%.5f±%.5f dep=%.2f±%.2fppt | free: tc=%.5f±%.5f dep=%.2f±%.2f T14=%.2f±%.2fh T23=%.2fh rms=%.2fppt beta=%.2f nin=%d/%d %s'%(
          r['tic'],r['kind'],r['pipe'],r['sector'],r['epoch'],r['tpred'],r['tc_fix'],r['etc_fix'],1e3*r['dep_fix'],1e3*r['edep_fix'],
          r.get('tc_free',np.nan),r.get('etc_free',np.nan),1e3*r.get('dep_free',np.nan),1e3*r.get('edep_free',np.nan),r.get('T14_h',np.nan),r.get('eT14_h',np.nan),r.get('T23_h',np.nan),1e3*r['rms'],r['beta'],r['n_in_q0'],r['n_in_all'],r['status']))
    else:
        print('%s %s %-9s s%-3d E%-4d pred=%.4f %s nin=%d/%d'%(r['tic'],r['kind'],r['pipe'],r['sector'],r['epoch'],r['tpred'],r['status'],r['n_in_q0'],r['n_in_all']))
