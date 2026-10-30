# Rough physical sanity check: mass function, companion mass, separation, central-eclipse duration, surface-brightness ratio.
import numpy as np
from scipy.optimize import brentq
S={'70665829':dict(P=3.4657654,K=60.968,e=0.0769,M1=0.851,R1=0.7595,T1=5080,T14=2.83,d1=0.299,d2=0.067,undil=1.0),
   '331293467':dict(P=5.2568199,K=48.728,e=0.0215,M1=1.69,R1=1.732,T1=7411,T14=4.07,d1=0.085,d2=0.014,undil=None)}
def planck_ratio(T2,T1,lam=0.8e-6):  # TESS-band surface brightness ratio, monochromatic at 800 nm
    c=1.4388e-2/lam; return (np.exp(c/T1)-1)/(np.exp(c/T2)-1)
for tic,s in S.items():
    fm=1.0361e-7*(1-s['e']**2)**1.5*s['K']**3*s['P']
    print(f"== TIC {tic}: f(m) = {fm:.4f} Msun")
    for M1 in (0.85*s['M1'],s['M1'],1.15*s['M1']):
        m2=brentq(lambda m: m**3/(M1+m)**2-fm,0.01,5)   # sin i = 1 (eclipsing)
        a=4.2084*(M1+m2)**(1/3)*s['P']**(2/3)
        # approximate dwarf sequence (Pecaut & Mamajek-style values, rounded): mass, Teff, R
        tab=np.array([[0.44,3560,0.43],[0.50,3660,0.48],[0.57,3850,0.55],[0.63,4050,0.62],[0.69,4440,0.68],[0.75,4800,0.74],[0.80,5000,0.78],[0.90,5400,0.88]])
        T2=np.interp(m2,tab[:,0],tab[:,1]); R2=np.interp(m2,tab[:,0],tab[:,2])
        Tc=s['P']*24/np.pi*np.arcsin((s['R1']+R2)/a)
        k=R2/s['R1']; J=planck_ratio(T2,s['T1'])
        print(f"   M1={M1:.2f}: m2(i=90)={m2:.3f} Msun, a={a:.2f} Rsun (a/R1={a/s['R1']:.1f}), R2~{R2:.2f} Rsun, k~{k:.2f}, T2~{T2:.0f} K, central T14={Tc:.2f} h (observed {s['T14']} h -> b>0), "
              f"J(800nm)~{J:.3f}; expected depth ratio d2/d1 ~ J for a total/annular pair = {J:.2f} (observed {s['d2']/s['d1']:.2f}); companion light fraction ~ {k**2*J/(1+k**2*J):.3f}")
