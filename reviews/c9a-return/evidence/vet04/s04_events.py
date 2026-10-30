# fit every predicted primary/secondary event individually in raw SAP QUALITY==0 flux (QLP and TESS-SPOC separately)
from common import *; from fitlib import *; import json,sys
CFG={'283532878':dict(T0=1761.98,P=17.446,ph2=0.678,T14=0.26,d1=0.075,d2=0.011,win=0.7),
     '407877153':dict(T0=1634.25,P=17.0895,ph2=0.545,T14=0.36,d1=0.030,d2=0.002,win=0.8)}
def texp_of(s):
    return float(np.round(np.median(np.diff(s['t'])),5))
rows=[]
for tic,c in CFG.items():
    print('=====',tic)
    for s in load(tic):
        te=texp_of(s); t,f=s['t'],s['f']
        n0=int(np.floor((t.min()-c['T0'])/c['P']))-1; n1=int(np.ceil((t.max()-c['T0'])/c['P']))+1
        for n in range(n0,n1+1):
            for kind,ph,dg in (('P',0.0,c['d1']),('S',c['ph2'],c['d2'])):
                tp=c['T0']+(n+ph)*c['P']
                if tp<t.min()-c['T14'] or tp>t.max()+c['T14']: continue
                near=np.abs(t-tp)<c['T14']/2
                # also check against the full (flagged) cadences
                nearall=np.abs(s['t_all']-tp)<c['T14']/2
                nflag=np.sum(nearall & (s['q_all']!=0))
                if near.sum()< 3:
                    print(s['author'],s['sector'],kind,n,'pred %.3f'%tp,'NOT COVERED by q==0 data (flagged cadences in window: %d)'%nflag); 
                    rows.append(dict(tic=tic,author=s['author'],sector=int(s['sector']),kind=kind,n=n,pred=tp,status='gap',nflag=int(nflag))); continue
                r=fit_event(t,f,te,tp,dg,c['T14'],c['win'])
                if r is None: continue
                p,e=r['p'],r['e']
                st='ok' if (r['cov']>0.6 and r['npre']>5 and r['npost']>5) else 'partial'
                print(s['author'],s['sector'],kind,n,'pred %.3f'%tp,'t0=%.4f±%.4f d=%.2f±%.2fppt T14=%.2f±%.2fh T23/T14=%.2f±%.2f rms=%.2fppt beta=%.2f cov=%.2f pre/post=%d/%d nflag=%d %s'%(
                    p['t0'],e['t0'],1e3*p['d'],1e3*e['d'],24*p['T14'],24*e['T14'],p['r23'],e['r23'],1e3*r['rms'],r['beta'],r['cov'],r['npre'],r['npost'],nflag,st))
                rows.append(dict(tic=tic,author=s['author'],sector=int(s['sector']),kind=kind,n=n,pred=tp,status=st,nflag=int(nflag),
                                 t0=p['t0'],et0=e['t0'],d=p['d'],ed=e['d'],T14=p['T14'],eT14=e['T14'],r23=p['r23'],er23=e['r23'],rms=r['rms'],beta=r['beta'],cov=r['cov'],texp=te))
json.dump(rows,open('s04_events.json','w'),indent=1)
