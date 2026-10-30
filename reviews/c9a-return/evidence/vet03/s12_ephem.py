# Final ephemerides: weighted linear fits to individually measured mid-times (s3 json; s5 json for 331293467 secondaries),
# excluding partially covered events; joint fit with common P; O-C by sector; next three primaries in UTC.
import numpy as np, json
from astropy.time import Time
G={'70665829':dict(P=3.46588776746830707,eP=2.8460746e-04,thr=0.15),'331293467':dict(P=5.25654668202362618,eP=5.3649350e-04,thr=0.03)}
def wfit(ts,es,n,kind):
    # model t = T0 + P n + dT*kind  (kind=0 primary, 1 secondary)
    A=np.vstack([np.ones_like(n),n,kind]).T if kind.any() else np.vstack([np.ones_like(n),n]).T
    W=1/es**2; C=np.linalg.inv(A.T@(A*W[:,None])); p=C@(A.T@(W*ts)); r=ts-A@p; dof=len(ts)-A.shape[1]
    chi=np.sum(r**2*W)/dof; return p,np.sqrt(np.diag(C)*max(1,chi)),r,chi
now=Time('2026-10-30T12:00:00',scale='utc'); now_btjd=now.tdb.jd-2457000
print(f'now = {now.iso} UTC = BTJD {now_btjd:.3f}')
res={}
for tic,g in G.items():
    print('='*10,tic)
    ev=json.load(open(f's3_events_{tic}.json'))
    ev=[e for e in ev if e['D']>0.02 and e['eD']<0.01]
    good=lambda e: e.get('fill',1)>0.9 and e.get('npre',99)>=5 and e.get('npost',99)>=5
    sets={}
    for pipe in ['SPOC','QLP']:
        pr=[e for e in ev if e['pipe']==pipe and e['D']>g['thr']]; se=[e for e in ev if e['pipe']==pipe and e['D']<=g['thr']]
        if tic=='331293467' and pipe=='QLP':
            se=[dict(t0=r['t0'],et0=r['et0'],sector=r['sector'],fill=1.0 if r['nin']>=0.9*(4.07/24)/((30 if r['sector']==11 else 10 if r['sector']==38 else 10/3)/1440) else 0.5) for r in json.load(open('s5_secondary_331293467.json')) if r['kind']=='sec']
        if pr: sets[pipe]=(pr,se)
    for pipe,(pr,se) in sets.items():
        for lab,flt in [('all',lambda e:True),('full-coverage only',good)]:
            P_=[e for e in pr if flt(e)]; S_=[e for e in se if flt(e)]
            T0g=P_[len(P_)//2]['t0']
            for name,sel,k in [('primaries',P_,0),('secondaries',S_,1)]:
                if len(sel)<3: continue
                ts=np.array([e['t0'] for e in sel]); es=np.array([max(e['et0'],1e-4) for e in sel]); n=np.round((ts-T0g-k*0.5*g['P'])/g['P'])
                p,pe,r,chi=wfit(ts,es,n,np.zeros_like(n))
                print(f'{pipe} {lab:18s} {name:11s}: N={len(sel)} P={p[1]:.7f}+-{pe[1]:.7f} chi2r={chi:.2f} rms O-C {np.std(r)*1440:.2f} min; (P-P_Gaia)/sig_Gaia={(p[1]-g["P"])/g["eP"]:+.2f}')
            ts=np.array([e['t0'] for e in P_+S_]); es=np.array([max(e['et0'],1e-4) for e in P_+S_]); kind=np.array([0]*len(P_)+[1]*len(S_),float)
            n=np.round((ts-T0g-kind*0.46*g['P'])/g['P'])
            # choose reference cycle near the weighted centre of the primaries
            n0=np.round(np.average(n[kind==0])); n=n-n0
            p,pe,r,chi=wfit(ts,es,n,kind)
            print(f'{pipe} {lab:18s} JOINT      : N={len(ts)} T0={p[0]:.5f}+-{pe[0]:.5f} BTJD (BJD_TDB {p[0]+2457000:.5f}) P={p[1]:.7f}+-{pe[1]:.7f} secondary offset {p[2]:.5f}+-{pe[2]:.5f} d = phase {p[2]/p[1]:.5f}+-{pe[2]/p[1]:.5f}; chi2r={chi:.2f}; (P-P_Gaia)/sig_Gaia={(p[1]-g["P"])/g["eP"]:+.2f}')
            if lab=='full-coverage only':
                secs=sorted(set(e['sector'] for e in P_))
                print('   primary O-C by sector (min): '+'; '.join(f"s{s}: {np.mean(r[:len(P_)][[e['sector']==s for e in P_]])*1440:+.2f}" for s in secs))
                if S_: print('   secondary O-C by sector (min): '+'; '.join(f"s{s}: {np.mean(r[len(P_):][[e['sector']==s for e in S_]])*1440:+.2f}" for s in sorted(set(e['sector'] for e in S_))))
                res[f'{tic}_{pipe}']=dict(T0=p[0],eT0=pe[0],P=p[1],eP=pe[1],dsec=p[2],edsec=pe[2])
for key,v in res.items():
    tic=key.split('_')[0]
    k=np.arange(np.ceil((now_btjd-v['T0'])/v['P']),np.ceil((now_btjd-v['T0'])/v['P'])+3)
    tt=v['T0']+k*v['P']; et=np.hypot(v['eT0'],k*v['eP'])
    tu=Time(tt+2457000,format='jd',scale='tdb').utc
    print(f"{key}: next primaries (BTJD; UTC of the barycentric time, no light-time correction to Earth): "+'; '.join(f'{a:.4f}+-{b:.4f} = {c.iso[:16]}' for a,b,c in zip(tt,et,tu)))
    ts=tt+v['dsec']; tsu=Time(ts+2457000,format='jd',scale='tdb').utc
    print(f"   matching secondaries: "+'; '.join(f'{a:.4f} = {c.iso[:16]}' for a,c in zip(ts,tsu)))
json.dump(res,open('s12_ephem.json','w'),indent=1)
