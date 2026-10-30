# s7: linear ephemerides from individual mid-times (events_qlp.csv), O-C, odd/even, secondary phase; P vs Gaia.
import numpy as np, csv
from lcio import load_qlp, fit_event, model, trap
from scipy.optimize import least_squares
R=list(csv.DictReader(open('events_qlp.csv')))
GAIA={'195865529':(3.83110403752586048,3.8206780e-04),'468181994':(3.99921890501413024,9.9554090e-04)}
def linfit(E,t,e):
    w=1/e**2; A=np.c_[np.ones_like(E),E]
    C=np.linalg.inv(A.T@(A*w[:,None])); p=C@(A.T@(w*t)); res=t-A@p
    chi2=np.sum(res**2*w); dof=len(t)-2; s=max(1,np.sqrt(chi2/dof))
    return p,np.sqrt(np.diag(C))*s,res,chi2/dof
def wmean(x,e):
    w=1/e**2; m=np.sum(w*x)/np.sum(w); return m,1/np.sqrt(np.sum(w)), np.sum((x-m)**2*w)/(len(x)-1)
out={}
for tic in GAIA:
    print('='*20,tic)
    rows=[r for r in R if r['tic']==tic and r['status']=='ok']
    def get(typ):
        rr=[r for r in rows if r['type']==typ and np.isfinite(float(r['e_t0'])) and float(r['e_t0'])<0.005]
        return (np.array([int(r['epoch']) for r in rr],float),np.array([float(r['t0']) for r in rr]),np.array([float(r['e_t0']) for r in rr]),
                np.array([float(r['depth']) for r in rr]),np.array([float(r['e_depth']) for r in rr]),np.array([int(r['sector']) for r in rr]))
    E,t,e,d,ed,s=get('P')
    excl=[r for r in rows if r['type']=='P' and not (np.isfinite(float(r['e_t0'])) and float(r['e_t0'])<0.005)]
    print('primaries used',len(E),'; excluded as partial (bad covariance):',[(r['sector'],r['epoch']) for r in excl])
    Eref=np.round(np.median(E))
    p,pe,res,rchi=linfit(E-Eref,t,e)
    T0=p[0];P=p[1]
    print(f'Primary ephemeris: T0(E={int(Eref)}) = {p[0]:.6f} +- {pe[0]:.6f} BTJD, P = {p[1]:.7f} +- {pe[1]:.7f} d, red.chi2 {rchi:.2f}, O-C rms {np.std(res)*1440:.2f} min')
    # also with T0 at the first epoch
    p0,pe0,_,_=linfit(E-E.min(),t,e); print(f'   (T0 at E={int(E.min())}: {p0[0]:.6f} +- {pe0[0]:.6f})')
    Pg,ePg=GAIA[tic]; print(f'   Gaia P = {Pg:.6f} +- {ePg:.6f}; P_ecl - P_Gaia = {P-Pg:+.6f} d = {(P-Pg)/np.hypot(ePg,pe[1]):+.2f} sigma')
    for ss in sorted(set(s)):
        m=s==ss; print(f'   s{ss}: n={m.sum()} mean O-C {np.mean(res[m])*1440:+.2f} min, depth wmean {wmean(d[m],ed[m])[0]*1e3:.2f}+-{wmean(d[m],ed[m])[1]*1e3:.2f} ppt (scatter chi2r {wmean(d[m],ed[m])[2]:.2f})')
    # odd/even within sectors (normalise each depth by its sector mean to remove dilution differences)
    dn=np.array([d[i]/wmean(d[s==s[i]],ed[s==s[i]])[0] for i in range(len(d))])
    odd=(E%2==1)
    mo=wmean(dn[odd],ed[odd]/d[odd]); me=wmean(dn[~odd],ed[~odd]/d[~odd])
    print(f'   odd/even primaries (sector-normalised): odd {mo[0]:.4f}+-{mo[1]:.4f} (n={odd.sum()}), even {me[0]:.4f}+-{me[1]:.4f} (n={(~odd).sum()}), diff {(mo[0]-me[0])/np.hypot(mo[1],me[1]):+.2f} sigma')
    mo2=wmean(d[odd],ed[odd]); me2=wmean(d[~odd],ed[~odd]); print(f'   raw depths odd {mo2[0]*1e3:.2f}+-{mo2[1]*1e3:.2f} even {me2[0]*1e3:.2f}+-{me2[1]*1e3:.2f} ppt')
    # secondaries
    Es,ts,es,ds,eds,ss_=get('S')
    if tic=='195865529':
        Es2=Es+0.5  # S epoch n means phase n+0.5
        ps,pes,ress,rchis=linfit(Es2-Eref,ts,es)
        print(f'Secondary ephemeris: T0s = {ps[0]:.6f} +- {pes[0]:.6f}, P = {ps[1]:.7f} +- {pes[1]:.7f}, red.chi2 {rchis:.2f}; n={len(Es)}')
        print(f'   P_sec - P_prim = {ps[1]-P:+.7f} +- {np.hypot(pes[1],pe[1]):.7f} d')
        # phase of secondary = (T0s - T0 - 0.5P)/P + 0.5 : evaluated at Eref
        phs=0.5+(ps[0]-T0)/P; ephs=np.hypot(pes[0],pe[0])/P
        print(f'   secondary phase = {phs:.5f} +- {ephs:.5f}  -> e cos w ~ (pi/2)(phi-0.5) = {np.pi/2*(phs-0.5):+.5f} +- {np.pi/2*ephs:.5f} (first order, sin i~1)')
        oddS=(Es%2==1); a=wmean(ds[oddS],eds[oddS]); b=wmean(ds[~oddS],eds[~oddS]); print(f'   odd/even secondaries {a[0]*1e3:.2f}+-{a[1]*1e3:.2f} / {b[0]*1e3:.2f}+-{b[1]*1e3:.2f} ppt')
        print(f'   secondary depth wmean {wmean(ds,eds)[0]*1e3:.2f}+-{wmean(ds,eds)[1]*1e3:.2f} ppt; per-event chi2r {wmean(ds,eds)[2]:.2f}')
        # durations
        rr=[r for r in rows if r['type']=='S']; print('   secondary T14 median %.2f h, T23 median %.2f h'%(np.median([float(r['T14_h']) for r in rr]),np.median([float(r['T23_h']) for r in rr])))
        rr=[r for r in rows if r['type']=='P']; print('   primary T14 median %.2f h, T23 median %.2f h'%(np.median([float(r['T14_h']) for r in rr]),np.median([float(r['T23_h']) for r in rr])))
    else:
        rr=[r for r in rows if r['type']=='P']; print('   primary T14 median %.2f h (16-84%%: %.2f-%.2f), T23 median %.2f h'%(np.median([float(r['T14_h']) for r in rr]),*np.percentile([float(r['T14_h']) for r in rr],[16,84]),np.median([float(r['T23_h']) for r in rr])))
        print(f'   secondary individual depths: wmean {wmean(ds,eds)[0]*1e3:.2f}+-{wmean(ds,eds)[1]*1e3:.2f} ppt, n={len(ds)}, chi2r {wmean(ds,eds)[2]:.2f}; n with depth>2sigma: {(ds/eds>2).sum()}; n<0: {(ds<0).sum()}')
        # per sector secondary depth
        for q in sorted(set(ss_)):
            m=ss_==q; w=wmean(ds[m],eds[m]); print(f'     s{q}: n={m.sum()} secondary {w[0]*1e3:.2f}+-{w[1]*1e3:.2f} ppt')
        # fold fit of the secondary with phase free, fixed primary shape, on locally normalised data
        L=load_qlp(tic)
        T14=float(np.median([float(r['T14_h']) for r in rr]))/24; f23=float(np.median([float(r['f23']) for r in rr]))
        tt=[];ff=[];tx=[]
        for sct in L:
            t_,f_=L[sct]['t'],L[sct]['f']
            n0=int(np.floor((t_.min()-T0)/P))-1; n1=int(np.ceil((t_.max()-T0)/P))+1
            for n in range(n0,n1+1):
                tc=T0+(n-Eref+0.49)*P  # wait, T0 refers to Eref
            for n in range(n0,n1+1):
                tc=T0+(n+0.49)*P
                m=np.abs(t_-tc)<0.45
                if m.sum()<20: continue
                oot=m&(np.abs(t_-tc)>0.17)
                if oot.sum()<10: continue
                c=np.polyfit(t_[oot]-tc,f_[oot],2); tt.append(((t_[m]-T0)/P)%1); ff.append(f_[m]/np.polyval(c,t_[m]-tc)); tx.append(np.full(m.sum(),L[sct]['texp']))
        ph=np.concatenate(tt);fl=np.concatenate(ff);tx=np.concatenate(tx)
        def fun(q):
            phc,dep=q; return (1-np.array([0]*0+[0])) if False else (1-trap(ph*P,phc*P,dep,T14,f23))-fl
        r=least_squares(fun,[0.49,0.0015]); J=r.jac; cov=np.linalg.inv(J.T@J)*np.var(r.fun)
        print(f'   FOLD fit of secondary (primary shape fixed T14={T14*24:.2f} h, T23/T14={f23:.2f}; local quadratic per event, |dt|>0.17 d): phase {r.x[0]:.4f}+-{np.sqrt(cov[0,0]):.4f}, depth {r.x[1]*1e3:.2f}+-{np.sqrt(cov[1,1])*1e3:.2f} ppt, N={len(ph)}')
        def fun2(q):
            phc,dep,T,f=q; return (1-trap(ph*P,phc*P,dep,T,f))-fl
        r2=least_squares(fun2,[r.x[0],r.x[1],T14,f23],bounds=([0.4,0,0.05,0],[0.6,0.01,0.3,0.99])); J=r2.jac; cov2=np.linalg.inv(J.T@J)*np.var(r2.fun)
        print(f'   FOLD fit free shape: phase {r2.x[0]:.4f}+-{np.sqrt(cov2[0,0]):.4f}, depth {r2.x[1]*1e3:.2f}+-{np.sqrt(cov2[1,1])*1e3:.2f} ppt, T14 {r2.x[2]*24:.2f}+-{np.sqrt(cov2[2,2])*24:.2f} h')
        # null test: same fit at phase 0.25 and 0.75
        for pc in (0.25,0.75):
            tt=[];ff=[]
            for sct in L:
                t_,f_=L[sct]['t'],L[sct]['f']
                n0=int(np.floor((t_.min()-T0)/P))-1; n1=int(np.ceil((t_.max()-T0)/P))+1
                for n in range(n0,n1+1):
                    tc=T0+(n+pc)*P; m=np.abs(t_-tc)<0.45
                    if m.sum()<20: continue
                    oot=m&(np.abs(t_-tc)>0.17)
                    if oot.sum()<10: continue
                    c=np.polyfit(t_[oot]-tc,f_[oot],2); tt.append(((t_[m]-T0)/P)%1); ff.append(f_[m]/np.polyval(c,t_[m]-tc))
            ph0=np.concatenate(tt);fl0=np.concatenate(ff)
            rr0=least_squares(lambda q:(1-trap(ph0*P,pc*P,q[0],T14,f23))-fl0,[0.0005]); J=rr0.jac; c0=np.linalg.inv(J.T@J)*np.var(rr0.fun)
            print(f'   null box at phase {pc}: depth {rr0.x[0]*1e3:+.2f}+-{np.sqrt(c0[0,0])*1e3:.2f} ppt')
        out[tic+'_sec']=(r.x[0],np.sqrt(cov[0,0]))
    out[tic]=dict(T0=T0,eT0=pe[0],P=P,eP=pe[1],Eref=Eref)
import json; json.dump({k:(v if isinstance(v,dict) else list(v)) for k,v in out.items()},open('ephem.json','w'),indent=1,default=float)
