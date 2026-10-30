# Locate secondary in flattened fold (finding aid only): box scan over phase
import numpy as np
cfg={'15855794':(5.89118,2503.1195,0.08),'92881948':(8.80498,1445.1987,0.045)}
for tic,(P,T0,dur) in cfg.items():
    t,f=np.load(f'flat_{tic}.npy')
    ph=((t-T0)/P+0.25)%1-0.25
    w=dur/P
    best=[]
    for c in np.arange(0.05,0.95,0.0005):
        m=np.abs(ph-c)<w/2; o=(np.abs(ph-c)>w)&(np.abs(ph-c)<3*w)
        if m.sum()<10: continue
        d=np.median(f[o])-np.mean(f[m]); err=np.std(f[o])/np.sqrt(m.sum())
        best.append((d/err,c,d,m.sum()))
    best.sort(reverse=True)
    print(tic,'top secondary candidates (snr,phase,depth,n):')
    for b in best[:8]: print('   %.1f %.4f %.5f %d'%b)
    # fine profile of primary
    for c0,lab in [(0,'prim'),(best[0][1],'sec')]:
        bins=np.arange(-2.5*w,2.5*w+1e-9,w/8)
        dph=ph-c0
        print(' ',lab,'binned profile (dphase*P in h, flux):')
        for a,b in zip(bins[:-1],bins[1:]):
            m=(dph>=a)&(dph<b)
            if m.sum(): print('    %+6.2f h  %.5f  n=%d'%((a+b)/2*P*24,np.median(f[m]),m.sum()))
