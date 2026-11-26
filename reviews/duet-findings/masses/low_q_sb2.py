"""A108 and A28, the two eclipsing Gaia SB2s with q well below 1: can a main-sequence companion of Gaia's mass make
their eclipses? Reads masses/sb2-masses.csv (sb2_masses.py); depths are Table A1c's. Run from the repository root."""
import numpy as np, pandas as pd
m=pd.read_csv('reviews/duet-findings/masses/sb2-masses.csv').set_index('review_id')
cases={'A108':(0.214,0.028,[1.45,1.90]),'A28':(0.205,0.05,[]) }
for lab,(d1,d2,R1s) in cases.items():
    r=m.loc[lab]; M1,M2=max(r.M1sin3i,r.M2sin3i),min(r.M1sin3i,r.M2sin3i); q=M2/M1; a=r.asini_Rsun
    RL=0.49*q**(2/3)/(0.6*q**(2/3)+np.log(1+q**(1/3)))          # Eggleton (1983)
    R2ms=M2**0.9; L2ms=10**(4.572*np.log10(M2)-0.102)           # low-mass main sequence (Eker et al. 2018 MLR)
    print(f'== {lab}: P = {r.P:.3f} d, e = {r.e:.3f}; M sin3i = {M1:.3f} + {M2:.3f} Msun (q = {q:.3f}), a sin i = {a:.1f} Rsun, sin3i >= {r.sin3i_min:.3f}')
    print(f'   depths {100*d1:.1f}% and {100*d2:.1f}%: eclipser/eclipsed radius ratio >= {np.sqrt(d1):.3f}, or an occulted star giving >= {100*d1:.0f}% of the light')
    print(f'   a {M2:.2f} Msun main-sequence star: R = {R2ms:.2f} Rsun, L = {L2ms:.3f} Lsun; TIC: R = {r.rad:.2f} (single-star), L = {r.lum} Lsun, {r.lumclass}')
    for R1 in R1s+[r.rad]:
        print(f'   if the eclipsed star has R = {R1:.2f}: companion R >= {np.sqrt(d1)*R1:.2f} Rsun ({np.sqrt(d1)*R1/R2ms:.1f} x main-sequence)')
    print(f'   companion Roche lobe: R_L/a = {RL:.3f}, R_L >= {RL*a:.1f} Rsun')
    if lab=='A108':
        alpha=0.15*(15+0.6)*(1+0.4)/(3-0.6)                      # Morris (1985), u = 0.6, tau = 0.4
        print(f'   ellipsoidal semi-amplitude if lobe-filling: {alpha*(M1/M2)*RL**3:.3f} x its light share, at P/2 = {r.P/2:.3f} d')
    print(f'   surface-brightness ratio d2/d1 = {d2/d1:.2f}')
