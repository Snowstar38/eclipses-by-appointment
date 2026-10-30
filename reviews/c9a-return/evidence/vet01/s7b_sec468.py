# s7b: TIC 468181994 secondary: individual-event depths (shape and phase fixed from the fold), per-sector fold fits (phase free), recentred windows
import numpy as np, csv, json
from lcio import load_qlp, trap
from scipy.optimize import least_squares
tic='468181994'; J=json.load(open('ephem.json'))[tic]; P,T0=J['P'],J['T0']
R=[r for r in csv.DictReader(open('events_qlp.csv')) if r['tic']==tic and r['type']=='P' and r['status']=='ok']
T14=np.median([float(r['T14_h']) for r in R])/24; f23=np.median([float(r['f23']) for r in R])
L=load_qlp(tic)
def collect(center, secs, half=0.45, excl=0.17):
    out=[]
    for s in secs:
        t_,f_=L[s]['t'],L[s]['f']
        n0=int(np.floor((t_.min()-T0)/P))-1; n1=int(np.ceil((t_.max()-T0)/P))+1
        for n in range(n0,n1+1):
            tc=T0+(n+center)*P; m=np.abs(t_-tc)<half
            if m.sum()<15: continue
            oot=m&(np.abs(t_-tc)>excl)
            if (oot&(t_<tc)).sum()<5 or (oot&(t_>tc)).sum()<5: continue
            c=np.polyfit(t_[oot]-tc,f_[oot],2)
            out.append((s,n,t_[m],f_[m]/np.polyval(c,t_[m]-tc)))
    return out
def fitphase(ev):
    ph=np.concatenate([((e[2]-T0)/P)%1 for e in ev]); fl=np.concatenate([e[3] for e in ev])
    r=least_squares(lambda q:(1-trap(ph*P,q[0]*P,q[1],T14,f23))-fl,[0.495,0.0014],bounds=([0.45,-0.01],[0.55,0.01]))
    Jm=r.jac; cov=np.linalg.inv(Jm.T@Jm)*np.var(r.fun); return r.x,np.sqrt(np.diag(cov)),len(ph)
print(f'shape from primaries: T14={T14*24:.2f} h, T23/T14={f23:.2f}; P={P:.7f} T0={T0:.5f}')
for cen in (0.49,0.50,0.495):
    x,e,n=fitphase(collect(cen,sorted(L))); print(f'all sectors, windows centred at phase {cen}: phase {x[0]:.4f}+-{e[0]:.4f}, depth {x[1]*1e3:.2f}+-{e[1]*1e3:.2f} ppt (N={n})')
for s in sorted(L):
    x,e,n=fitphase(collect(0.5,[s])); print(f'  s{s}: phase {x[0]:.4f}+-{e[0]:.4f}, depth {x[1]*1e3:.2f}+-{e[1]*1e3:.2f} ppt (N={n})')
# split halves in time
for nm,ss in [('s12-39',[12,13,27,39]),('s67-94',[67,93,94])]:
    x,e,n=fitphase(collect(0.5,ss)); print(f'  {nm}: phase {x[0]:.4f}+-{e[0]:.4f}, depth {x[1]*1e3:.2f}+-{e[1]*1e3:.2f} ppt')
x,e,n=fitphase(collect(0.5,sorted(L))); phs=x[0]
# individual events: depth with phase fixed at phs
rows=[]
for s,nn,t_,fl in collect(phs,sorted(L)):
    tc=T0+(nn+phs)*P
    m_in=np.abs(t_-tc)<T14/2
    if m_in.sum()<3: continue
    r=least_squares(lambda q:(1-trap(t_,tc,q[0],T14,f23))-fl,[0.0014]); Jm=r.jac; ee=np.sqrt(np.linalg.inv(Jm.T@Jm)[0,0]*np.var(r.fun))
    rows.append((s,nn,tc,r.x[0],ee,m_in.sum()))
d=np.array([r[3] for r in rows]); ed=np.array([r[4] for r in rows])
w=1/ed**2; m=np.sum(w*d)/np.sum(w)
print(f'individual secondaries (phase fixed {phs:.4f}): n={len(d)}, wmean {m*1e3:.2f}+-{1/np.sqrt(w.sum())*1e3:.2f} ppt, chi2r about mean {np.sum((d-m)**2*w)/(len(d)-1):.2f}, n>2sigma {np.sum(d/ed>2)}, n>0 {np.sum(d>0)}')
for r in rows: print(f'  S s{r[0]} E{r[1]} mid {r[2]:.4f} depth {r[3]*1e3:+.2f}+-{r[4]*1e3:.2f} ppt (n_in {r[5]})')
