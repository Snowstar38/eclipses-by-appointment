# s6: individual eclipse events from raw QLP SAP (QUALITY==0): trapezoid x quadratic baseline, exposure-supersampled,
# errors from the Jacobian scaled by residual rms and by a red-noise beta factor (Winn+2008, bins 20-60 min).
import numpy as np, json, sys
from lcio import load_qlp, fit_event, model
CFG={'195865529':dict(P=3.831038,T0=1714.20421,types={'P':(0.0,0.19,0.25,0.3),'S':(0.5,0.047,0.25,0.3)}),
     '468181994':dict(P=3.996917,T0=1628.88750,types={'P':(0.0,0.024,0.15,0.3),'S':(0.4915,0.0015,0.15,0.3)})}
def beta(res,t,dtmin=20/1440,dtmax=60/1440):
    s1=np.std(res); bs=[]
    for w in np.linspace(dtmin,dtmax,5):
        edges=np.arange(t.min(),t.max()+w,w); idx=np.digitize(t,edges)
        mb=[res[idx==k].mean() for k in np.unique(idx) if (idx==k).sum()>=2]
        n=np.mean([(idx==k).sum() for k in np.unique(idx)])
        M=len(mb)
        if M<4: continue
        exp=s1/np.sqrt(n)*np.sqrt(M/(M-1)); bs.append(np.std(mb)/exp)
    return max(1.0,np.median(bs)) if bs else 1.0
allrows=[]
for tic,c in CFG.items():
    L=load_qlp(tic); P,T0=c['P'],c['T0']
    print('='*30,tic)
    # pass 1: free-shape fits of primaries to get mean shape; secondaries with free shape only for 195865529
    shapes={}
    for typ,(phi,dg,T14g,f23g) in c['types'].items():
        rows=[]
        for s in sorted(L):
            t,f,texp=L[s]['t'],L[s]['f'],L[s]['texp']
            tall,qall=L[s]['tall'],L[s]['qall']
            n0=int(np.ceil((tall.min()-T0)/P-phi)); n1=int(np.floor((tall.max()-T0)/P-phi))
            for n in range(n0-1,n1+2):
                tc=T0+(n+phi)*P
                if tc<tall.min()-T14g or tc>tall.max()+T14g: continue
                win=np.abs(tall-tc)<T14g/2
                nflag=int(np.sum(win&(qall!=0))); ngood=int(np.sum(np.abs(t-tc)<T14g/2))
                fix=None
                if typ=='S' and tic=='468181994': fix=shapes['P']
                r=fit_event(t,f,tc,dg,T14g,f23g,halfwin=1.6*T14g if typ=='P' or tic=='195865529' else 2.0*T14g,fix_shape=fix,texp=texp)
                ok=r is not None and r['pre']>=4 and r['post']>=4 and r['cen']>=3
                row=dict(tic=tic,type=typ,sector=s,epoch=n,t_pred=round(tc,4),n_in_good=ngood,n_in_flagged=nflag,texp_min=round(texp*1440,1))
                if r is None or not ok:
                    row.update(status='lost/partial', pre=None if r is None else int(r['pre']), post=None if r is None else int(r['post']), cen=None if r is None else int(r['cen']))
                else:
                    tt=r['tt']; res=r['ff']-model(r['p'],tt,r['tref'],texp); b=beta(res,tt)
                    p,e=r['p'],r['e']*b
                    row.update(status='ok',t0=p[0],e_t0=e[0],depth=p[1],e_depth=e[1],T14_h=p[2]*24,e_T14_h=e[2]*24,T23_h=p[2]*p[3]*24,f23=p[3],rms_ppt=r['rms']*1e3,beta=b,npts=r['n'])
                rows.append(row)
        # summary
        ok=[r for r in rows if r['status']=='ok']
        if typ=='P' or tic=='195865529':
            T14m=np.median([r['T14_h'] for r in ok])/24; f23m=np.median([r['f23'] for r in ok])
            shapes[typ]=(T14m,f23m)
        allrows+=rows
        print(f'{typ}: {len(ok)} measured of {len(rows)} predicted in sector spans')
        for r in rows:
            if r['status']=='ok':
                print(f"  {typ} s{r['sector']:<3d} E{r['epoch']:<4d} t0={r['t0']:.5f}+-{r['e_t0']:.5f} depth={r['depth']*1e3:7.2f}+-{r['e_depth']*1e3:5.2f} ppt T14={r['T14_h']:.2f}+-{r['e_T14_h']:.2f} h T23={r['T23_h']:.2f} h rms={r['rms_ppt']:.2f} beta={r['beta']:.2f} n={r['npts']} cad={r['texp_min']}m")
            else:
                print(f"  {typ} s{r['sector']:<3d} E{r['epoch']:<4d} pred {r['t_pred']:.3f} LOST/PARTIAL: good pts in T14 {r['n_in_good']}, flagged pts in T14 {r['n_in_flagged']}, pre/post/cen {r.get('pre')}/{r.get('post')}/{r.get('cen')}")
    print('shapes (T14 d, T23/T14):',shapes)
import csv
keys=sorted({k for r in allrows for k in r})
with open('events_qlp.csv','w',newline='') as fo:
    w=csv.DictWriter(fo,fieldnames=keys); w.writeheader(); [w.writerow(r) for r in allrows]
