# s4: independent period search (BLS) on raw QLP SAP (QUALITY==0), per-orbit median normalised, no detrending
import numpy as np, sys
from astropy.timeseries import BoxLeastSquares
from lcio import load_qlp
for tic,dur in [('195865529',[0.15,0.25,0.35]),('468181994',[0.08,0.12,0.18,0.25])]:
    L=load_qlp(tic)
    t=np.concatenate([L[s]['t'] for s in L]); f=np.concatenate([L[s]['f'] for s in L])
    # gentle normalisation: divide each 1.5-d chunk median? no -> per sector median already. remove slow trends with 3-day running median
    from scipy.ndimage import median_filter
    o=np.argsort(t); t,f=t[o],f[o]
    print(tic,'N points',len(t),'sectors',sorted(L), 'span',t.min(),t.max())
    bls=BoxLeastSquares(t,f)
    P=np.exp(np.linspace(np.log(0.5),np.log(20),200000))
    r=bls.power(P,dur,objective='snr')
    i=np.argsort(r.power)[::-1]
    shown=[]
    for k in i:
        if all(abs(P[k]/s-1)>0.01 for s in shown):
            shown.append(P[k]); print(f'  P={P[k]:.5f} power={r.power[k]:.1f} depth={r.depth[k]*1e3:.2f} ppt dur={r.duration[k]*24:.1f} h t0={r.transit_time[k]:.4f}')
        if len(shown)>=6: break
    # fine search around best
    Pb=shown[0]; Pf=np.linspace(Pb*0.998,Pb*1.002,20001); rf=bls.power(Pf,dur,objective='likelihood')
    k=np.argmax(rf.power); print(f'  fine: P={Pf[k]:.6f} depth={rf.depth[k]*1e3:.2f} ppt dur={rf.duration[k]*24:.1f} h t0={rf.transit_time[k]:.5f}')
