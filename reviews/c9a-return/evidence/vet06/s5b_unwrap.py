# Unwrapped primary-B offset: dB = dA - phase(B-A)*P per draw (avoids the +-P/2 wrap that inflates s5's B scatter).
import numpy as np
from s0_gaia_predict import draws, conj, G
for tic in G:
    T0,eT0,P,eP,ph2,eph2=np.load(f's3_ephem_{tic}.npy')
    for corr in [True,False]:
        X=draws(tic,corr=corr); tA,tB,ph=conj(X); n=np.round((np.median(tA)-T0)/P); tT=T0+n*P; etT=np.hypot(eT0,n*eP)
        dA=(tT-tA+P/2)%P-P/2; dB=dA-ph*X[:,0]; dB2=dA+(1-ph)*X[:,0]
        for nm,v in [('A',dA),('B (B before primary)',dB),('B (B after primary)',dB2)]:
            s=np.hypot(np.std(v),etT); print(f'{tic} corr={corr}: primary-{nm} = {np.median(v):+.3f} +- {s:.3f} d ({np.median(v)/s:+.1f} sigma)')
