# s5: fold raw QLP SAP (Q==0) on the BLS period, locally normalised (each point / median of data within +-0.6 d excluding +-0.25 d of either eclipse candidate), and scan phase for the secondary
import numpy as np
from lcio import load_qlp
E={'195865529':(3.831038,1714.20421),'468181994':(3.996917,1628.88750)}
for tic,(P,T0) in E.items():
    L=load_qlp(tic)
    t=np.concatenate([L[s]['t'] for s in L]); f=np.concatenate([L[s]['f'] for s in L])
    ph=((t-T0)/P+0.5)%1-0.5
    # local normalisation: running median over 1.2 d using points with |phase|>0.06 (outside primary)
    o=np.argsort(t); t,f,ph=t[o],f[o],ph[o]
    good=np.abs(ph)>0.06
    fn=np.empty_like(f)
    for i in range(len(t)):
        pass
    # vectorised via searchsorted windows
    tg,fg=t[good],f[good]
    lo=np.searchsorted(tg,t-0.6); hi=np.searchsorted(tg,t+0.6)
    med=np.array([np.median(fg[a:b]) if b-a>5 else np.nan for a,b in zip(lo,hi)])
    fn=f/med
    m=np.isfinite(fn)
    nb=200; b=np.floor((ph[m]+0.5)*nb).astype(int)
    prof=np.array([np.median(fn[m][b==k]) for k in range(nb)]); ctr=(np.arange(nb)+0.5)/nb-0.5
    print(tic,'P',P,'T0',T0)
    print('  primary min bin phase %.4f depth %.2f ppt'%(ctr[np.argmin(prof)],(1-prof.min())*1e3))
    sec=(np.abs(ctr)>0.1)
    k=np.argmin(np.where(sec,prof,9)); print('  secondary min bin phase %.4f (=%.4f) depth %.2f ppt'%(ctr[k],ctr[k]%1,(1-prof[k])*1e3))
    out=np.abs(ctr)>0.1; print('  out-of-eclipse bin scatter %.3f ppt'%(np.std(prof[out&(np.abs(np.abs(ctr)-0.5)>0.08)])*1e3))
    # finer secondary: box scan of width w over phase 0.3-0.7
    for w in ([0.02,0.03,0.04] if tic=='195865529' else [0.015,0.02,0.03]):
        best=None
        for c in np.arange(0.30,0.70,0.0005):
            d=(ph%1); sel=m&(np.abs(d-c)<w/2)
            if sel.sum()<20: continue
            dep=1-np.mean(fn[sel]); snr=dep/(np.std(fn[m&out[np.clip(((ph+0.5)*nb).astype(int),0,nb-1)]])/np.sqrt(sel.sum()))
            if best is None or dep>best[1]: best=(c,dep,snr,sel.sum())
        print('  box w=%.3f: best secondary phase %.4f depth %.2f ppt snr %.1f n=%d'%(w,best[0],best[1]*1e3,best[2],best[3]))
    np.savetxt(f'fold_{tic}.txt',np.c_[ctr,prof],fmt='%.5f %.6f',header='phase median_flux (local-normalised raw QLP SAP Q==0)')
