# Linear ephemerides from individual eclipse mid-times; compare with Gaia P; odd/even depths.
import numpy as np, pandas as pd
G={'470235665':(10.32387058023074644,2.8021412e-03),'379251709':(12.32611933721202035,4.1742143e-03)}
def linfit(n,t,e):
    A=np.vstack([np.ones_like(n),n]).T; W=1/e**2
    C=np.linalg.inv(A.T@(A*W[:,None])); p=C@(A.T@(W*t))
    r=t-A@p; chi=np.sum(W*r**2); dof=len(t)-2; s=max(1,np.sqrt(chi/dof)) if dof>0 else 1
    return p,np.sqrt(np.diag(C))*s,r,chi/max(dof,1)
def pick(d,kind,pipes):
    d=d[(d.kind==kind)&(d.status=='full')&(d.e_tc<0.005)&(d['pipe'].isin(pipes))].copy()
    # one value per epoch: prefer SPOC (lower noise in shared sectors) if both pipes given
    d['pr']=(d['pipe']!='SPOC').astype(int)
    return d.sort_values(['epoch','pr']).groupby('epoch').head(1)
for tic,(Pg,ePg) in G.items():
    d=pd.read_csv(f'events_{tic}.csv'); print('='*10,'TIC',tic,' Gaia P = %.5f +- %.5f'%(Pg,ePg))
    res={}
    for kind in ['pri','sec']:
        for pipes,lab in [(['QLP','SPOC'],'best-per-epoch'),(['QLP'],'QLP only'),(['SPOC'],'SPOC only')]:
            s=pick(d,kind,pipes)
            if len(s)<3: print(f'  {kind} {lab}: only {len(s)} events'); continue
            p,e,r,rc=linfit(s.epoch.values.astype(float),s.tc.values,s.e_tc.values)
            print(f'  {kind} {lab:15s} N={len(s):2d} T0={p[0]:.5f}+-{e[0]:.5f} P={p[1]:.6f}+-{e[1]:.6f} redchi2={rc:.2f} rms(O-C)={1440*np.std(r):.1f}min  (P-Pgaia)/sig_gaia={(p[1]-Pg)/ePg:+.2f}  /sig_comb={(p[1]-Pg)/np.hypot(ePg,e[1]):+.2f}')
            res[(kind,lab)]=(p,e,s,r)
        if kind=='pri':
            p,e,s,r=res[('pri','best-per-epoch')]
            print('    O-C per event (min): '+' '.join(f'{int(n)}:{1440*x:+.1f}' for n,x in zip(s.epoch,r)))
    # joint fit common P, separate T0s
    sp=pick(d,'pri',['QLP','SPOC']); ss=pick(d,'sec',['QLP','SPOC'])
    if len(ss)>=3:
        n=np.r_[sp.epoch,ss.epoch].astype(float); t=np.r_[sp.tc,ss.tc]; e=np.r_[sp.e_tc,ss.e_tc]; k=np.r_[np.zeros(len(sp)),np.ones(len(ss))]
        A=np.vstack([1-k,k,n]).T; W=1/e**2; C=np.linalg.inv(A.T@(A*W[:,None])); pp=C@(A.T@(W*t)); rr=t-A@pp
        sc=max(1,np.sqrt(np.sum(W*rr**2)/(len(t)-3))); ee=np.sqrt(np.diag(C))*sc
        ph=(pp[1]-pp[0])/pp[2]; eph=np.sqrt(C[0,0]+C[1,1]-2*C[0,1])*sc/pp[2]
        print(f'  JOINT pri+sec: P={pp[2]:.6f}+-{ee[2]:.6f} T0pri={pp[0]:.5f}+-{ee[0]:.5f} T0sec={pp[1]:.5f}+-{ee[1]:.5f}  secondary phase={ph%1:.5f}+-{eph:.5f}  (P-Pgaia)/sig_gaia={(pp[2]-Pg)/ePg:+.2f}')
    # odd/even depths, per pipeline (QLP and SPOC separately, full events only)
    for kind in ['pri','sec']:
        for pipe in ['QLP','SPOC']:
            s=d[(d.kind==kind)&(d.status=='full')&(d['pipe']==pipe)&(d.e_tc<0.005)]
            if pipe=='QLP': s=s[s.sector!=24] if tic=='379251709' else s
            if len(s)<4: continue
            ev=s[s.epoch%2==0]; od=s[s.epoch%2==1]
            def wm(x): w=1/x.e_depth_ppt**2; m=np.sum(w*x.depth_ppt)/np.sum(w); sd=np.std(x.depth_ppt,ddof=1)/np.sqrt(len(x)) if len(x)>1 else np.nan; return m,max(np.sqrt(1/np.sum(w)),sd)
            me,ee_=wm(ev); mo,eo=wm(od)
            te=np.mean(ev.T14_h); to=np.mean(od.T14_h)
            print(f'  odd/even {kind} {pipe}: even N={len(ev)} depth={me:.2f}+-{ee_:.2f} ppt T14={te:.2f}h | odd N={len(od)} depth={mo:.2f}+-{eo:.2f} ppt T14={to:.2f}h | diff={(me-mo)/np.hypot(ee_,eo):+.2f} sigma')
