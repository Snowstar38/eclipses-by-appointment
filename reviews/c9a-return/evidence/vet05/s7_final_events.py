# Re-fit every event with the joint shape fixed (tc, depth, quadratic baseline free); then ephemerides, odd/even.
import numpy as np, json
from common import *
from fitlib import fit_event
ev=json.load(open('s5_events.json')); sh=json.load(open('s6_shape.json'))
gaia={'15855794':(5.89053844070554700,1.1329550e-03),'92881948':(8.80436043401770618,1.4405058e-03)}
rows=[]
for r in ev:
    if r['status'] not in ('OK','PARTIAL (one-sided baseline)'): rows.append(r); continue
    s=sh[f"{r['tic']}_{r['kind']}"]
    t,f,e,q=load(r['tic'],r['pipe'],r['sector'])
    m=np.abs(t-r['tpred'])<3*s['T14_d']
    texp=np.median(np.diff(t))
    p,ep,rms,beta=fit_event(t[m],f[m],texp,r['tc_fix'],s['depth'],s['T14_d'],s['T23_d'],fix_shape=True)
    r2=dict(r); r2.update(tc=p[0],etc=ep[0],dep=p[1],edep=ep[1],rms2=rms,beta2=beta,texp_min=texp*1440)
    rows.append(r2)
json.dump(rows,open('s7_events.json','w'),indent=1,default=float)
print('# Fixed-shape per-event fits (raw SAP, QUALITY==0, quadratic baseline over +-3 T14). depth in ppt.')
for r in rows:
    if 'tc' in r:
        print('%s %s %-9s s%-3d E%-4d tc=%.5f ± %.5f  depth=%5.2f ± %4.2f ppt  rms=%.2f ppt cad=%.1fmin %s'%(r['tic'],r['kind'],r['pipe'],r['sector'],r['epoch'],r['tc'],r['etc'],1e3*r['dep'],1e3*r['edep'],1e3*r['rms2'],r['texp_min'],r['status']))
    else:
        print('%s %s %-9s s%-3d E%-4d pred=%.4f %s (Q==0 pts in T14: %d of %d any-quality)'%(r['tic'],r['kind'],r['pipe'],r['sector'],r['epoch'],r['tpred'],r['status'],r['n_in_q0'],r['n_in_all']))
print()
def linfit(E,T,s):
    A=np.vstack([np.ones_like(E),E]).T; W=np.diag(1/s**2)
    C=np.linalg.inv(A.T@W@A); b=C@A.T@W@T
    res=T-A@b; chi2=np.sum((res/s)**2); dof=len(T)-2
    sc=max(1,np.sqrt(chi2/dof)) if dof>0 else 1
    return b,np.sqrt(np.diag(C))*sc,res,chi2,dof
out={}
for tic in ['15855794','92881948']:
    Pg,ePg=gaia[tic]
    sel={}
    for r in rows:
        if r['tic']!=tic or 'tc' not in r or r['status']!='OK': continue
        key=(r['kind'],r['epoch'])
        # one per event: prefer TESS-SPOC
        if key not in sel or r['pipe']=='TESS-SPOC': sel[key]=r
    for kind in ['P','S']:
        L=[v for k,v in sel.items() if k[0]==kind]; L.sort(key=lambda v:v['epoch'])
        E=np.array([v['epoch'] for v in L],float); T=np.array([v['tc'] for v in L]); s=np.array([v['etc'] for v in L])
        b,eb,res,chi2,dof=linfit(E,T,s)
        out[f'{tic}_{kind}']=dict(T0=b[0],eT0=eb[0],P=b[1],eP=eb[1],chi2=chi2,dof=dof,n=len(T))
        print('%s %s: n=%d T0=%.5f ± %.5f P=%.6f ± %.6f chi2/dof=%.1f/%d  (P-Pgaia)/sqrt(eP^2+ePg^2)=%+.2f sigma'%(tic,kind,len(T),b[0],eb[0],b[1],eb[1],chi2,dof,(b[1]-Pg)/np.hypot(eb[1],ePg)))
        print('   O-C (min):',' '.join('E%d:%+.1f±%.1f[%s]'%(e_,1440*o,1440*s_,v['pipe'][0]) for e_,o,s_,v in zip(E,res,s,L)))
    # joint: common P, T0, phase offset of S
    Ls=[v for v in sel.values()]
    E=np.array([v['epoch'] for v in Ls],float); T=np.array([v['tc'] for v in Ls]); s=np.array([v['etc'] for v in Ls]); isS=np.array([v['kind']=='S' for v in Ls],float)
    A=np.vstack([np.ones_like(E),E,isS]).T; W=np.diag(1/s**2)
    C=np.linalg.inv(A.T@W@A); b=C@A.T@W@T; res=T-A@b; chi2=np.sum((res/s)**2); dof=len(T)-3
    sc=max(1,np.sqrt(chi2/dof)); eb=np.sqrt(np.diag(C))*sc
    phS=b[2]/b[1]; ephS=np.hypot(eb[2]/b[1], b[2]*eb[1]/b[1]**2)
    out[f'{tic}_joint']=dict(T0=b[0],eT0=eb[0],P=b[1],eP=eb[1],dtS=b[2],edtS=eb[2],phaseS=phS,ephaseS=ephS,chi2=chi2,dof=dof)
    print('%s joint: T0=%.5f ± %.5f P=%.6f ± %.6f  secondary offset=%.5f ± %.5f d  phase_S=%.5f ± %.5f chi2/dof=%.1f/%d  vs Gaia %+.2f sigma'%(tic,b[0],eb[0],b[1],eb[1],b[2],eb[2],phS,ephS,chi2,dof,(b[1]-Pg)/np.hypot(eb[1],ePg)))
    # odd/even primary depths (each pipeline separately) and S depth summary
    for pipe in ['QLP','TESS-SPOC']:
        for kind in ['P','S']:
            L=[r for r in rows if r['tic']==tic and r['kind']==kind and r['pipe']==pipe and 'tc' in r and r['status']=='OK']
            if not L: continue
            for lab,cond in [('odd',lambda e:e%2==1),('even',lambda e:e%2==0)]:
                d=np.array([r['dep'] for r in L if cond(r['epoch'])]); ed=np.array([r['edep'] for r in L if cond(r['epoch'])])
                if len(d)==0: continue
                w=1/ed**2; mu=np.sum(w*d)/np.sum(w); emu=1/np.sqrt(np.sum(w))
                out[f'{tic}_{pipe}_{kind}_{lab}']=dict(mean=mu,err=emu,n=len(d))
                print('   %s %s %-4s n=%d mean depth=%.2f ± %.2f ppt'%(pipe,kind,lab,len(d),1e3*mu,1e3*emu))
json.dump(out,open('s7_ephem.json','w'),indent=1)
