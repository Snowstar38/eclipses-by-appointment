# Observed TESS primary vs Gaia conjunctions A/B; observed secondary phase vs Gaia prediction. Uses s0 MC draws (correlated & not).
import numpy as np
from s0_gaia_predict import draws, conj, G
for tic in G:
    T0,eT0,P,eP,ph2,eph2=np.load(f's3_ephem_{tic}.npy'); Pg,ePg=G[tic][0],G[tic][1]
    print(f'== {tic}: TESS P={P:.6f}+-{eP:.6f}; Gaia P={Pg:.6f}+-{ePg:.6f}; diff={(P-Pg)/np.hypot(eP,ePg):+.2f} sigma')
    for corr in [True,False]:
        X=draws(tic,corr=corr); tA,tB,ph=conj(X)
        n=np.round((np.median(tA)-T0)/P); tT=T0+n*P; etT=np.hypot(eT0,n*eP)
        # backward: TESS primary taken to Gaia epoch, offset from nearest A and B (mod P)
        dA=(tT-tA+P/2)%P-P/2; dB=(tT-tB+P/2)%P-P/2
        # forward: Gaia conj A propagated to TESS epoch with Gaia P draws
        m=np.round((T0-np.median(tA))/Pg); fA=((tA+m*X[:,0])-T0+P/2)%P-P/2; fB=((tB+m*X[:,0])-T0+P/2)%P-P/2
        print(f'  corr={corr}: backward (n={int(n)}, TESS err {etT:.4f} d): primary-A = {np.median(dA):+.3f} +- {np.hypot(np.std(dA),etT):.3f} d ({np.median(dA)/np.hypot(np.std(dA),etT):+.1f} sig); primary-B = {np.median(dB):+.3f} +- {np.hypot(np.std(dB),etT):.3f} d ({np.median(dB)/np.hypot(np.std(dB),etT):+.1f} sig)')
        print(f'             forward (m={int(m)}): primary-A = {-np.median(fA):+.3f} +- {np.std(fA):.3f} d; primary-B = {-np.median(fB):+.3f} +- {np.std(fB):.3f} d')
        print(f'             secondary phase: observed {ph2:.5f}+-{eph2:.5f}; Gaia predicted {np.median(ph):.4f}+-{np.std(ph):.4f} -> {(ph2-np.median(ph))/np.hypot(np.std(ph),eph2):+.2f} sigma; (if primary were B: predicted {1-np.median(ph):.4f})')
    print(f'  BJD_TDB T0 = {T0+2457000:.5f}')
