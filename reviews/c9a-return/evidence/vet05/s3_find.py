# Find events: running-median flatten (for FINDING only), BLS around Gaia P and wide, list dips
import numpy as np
from astropy.timeseries import BoxLeastSquares
from scipy.ndimage import median_filter
from common import *
def flat(t,f,w=1.0):
    out=np.empty_like(f)
    for i in range(len(t)):
        m=np.abs(t-t[i])<w/2
        out[i]=np.median(f[m])
    return f/out
cfg={'15855794':([44,70,71],5.890538),'92881948':([5,6,32,98],8.804360)}
for tic,(secs,Pg) in cfg.items():
    T=[];F=[]
    for s in secs:
        r=load(tic,'QLP',s); t,f,e,q=r
        if s==98 or s>=70:  # bin 200s to 10 min for speed in finding
            pass
        T.append(t);F.append(flat(t,f,0.75))
    t=np.concatenate(T);f=np.concatenate(F)
    np.save(f'flat_{tic}.npy',np.vstack([t,f]))
    bls=BoxLeastSquares(t,f)
    for lab,periods in [('wide',np.exp(np.linspace(np.log(0.5),np.log(20),60000))),('nearGaia',np.linspace(Pg*0.99,Pg*1.01,20000))]:
        res=bls.power(periods,[0.04,0.06,0.08,0.12,0.16,0.2])
        i=np.argmax(res.power)
        print(tic,lab,'P=%.5f T0=%.4f dur=%.3f depth=%.5f'%(res.period[i],res.transit_time[i],res.duration[i],res.depth[i]))
        # top 5 distinct peaks
        order=np.argsort(res.power)[::-1]; seen=[]
        for j in order:
            if all(abs(res.period[j]-p)/p>0.01 for p in seen):
                seen.append(res.period[j])
            if len(seen)>=5: break
        print('   top periods:',['%.4f'%p for p in seen])
    # list individual dips below threshold
    thr=1-0.5*res.depth[i]
    sm=median_filter(f,5)
    low=sm<1-0.003
    idx=np.where(low)[0]
    groups=np.split(idx,np.where(np.diff(t[idx])>0.1)[0]+1) if len(idx) else []
    for g in groups:
        if len(g)<2: continue
        k=g[np.argmin(sm[g])]
        print('   dip at %.4f min_sm=%.4f n=%d'%(t[k],sm[k],len(g)))
