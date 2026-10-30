# s13: geometry vs the Gaia DR3 SB1 orbit (Monte Carlo, 20000 draws of P, Tp, e, omega; e truncated at >=0) and rough physics.
# A = conjunction at nu = 90 - omega (companion in front of Gaia's RV star), B = nu = 270 - omega.
import numpy as np, csv, json
rng=np.random.default_rng(42); N=20000
T={r['tic']:r for r in csv.DictReader(open('../targets.csv'))}
EP=json.load(open('ephem.json'))
# observed: primary T0/P from s7 (ephem.json); secondary phase: 195865529 from s7.out (0.49999+-0.00007);
# 468181994 from s7b.out all-sector fit 0.4956, error = scatter of 7 per-sector phases / sqrt(7) (s7b.out)
sec468=np.array([0.4923,0.4881,0.4970,0.4948,0.4942,0.4957,0.4969])
OBS={'195865529':(0.49999,0.00007),'468181994':(0.4956,np.std(sec468,ddof=1)/np.sqrt(7))}
print(f'468181994 per-sector secondary phases (s7b): mean {sec468.mean():.4f}, sd {sec468.std(ddof=1):.4f}, sem {OBS["468181994"][1]:.4f}')
def circ(x):
    # wrap phases around their circular mean so that a distribution centred near +-0.5 is not split
    c=np.angle(np.mean(np.exp(2j*np.pi*x)))/(2*np.pi); return c+((x-c+0.5)%1-0.5)
def planckJ(T2,T1,lam=0.80):
    x=14388/lam; return (np.exp(x/T1)-1)/(np.exp(x/T2)-1)
def tconj(nu_deg,e,Tp,P):
    nu=np.radians(nu_deg); E=2*np.arctan(np.sqrt((1-e)/(1+e))*np.tan(nu/2)); M=E-e*np.sin(E)
    return Tp+(M/(2*np.pi))*P
for tic in ['195865529','468181994']:
    r=T[tic]; g=lambda k: float(r[k])
    P=rng.normal(g('gaia_Per'),g('gaia_e_Per'),N); Tp=rng.normal(g('gaia_tperi_btjd'),g('gaia_e_Tperi'),N)
    e=np.abs(rng.normal(g('gaia_ecc'),g('gaia_e_ecc'),N)); w=rng.normal(g('gaia_omega'),g('gaia_e_omega'),N)
    T0,Pe=EP[tic]['T0'],EP[tic]['P']
    print('='*20,tic,f"Gaia P={g('gaia_Per'):.6f}+-{g('gaia_e_Per'):.6f} Tp(BTJD)={g('gaia_tperi_btjd'):.3f}+-{g('gaia_e_Tperi'):.3f} e={g('gaia_ecc'):.3f}+-{g('gaia_e_ecc'):.3f} w={g('gaia_omega'):.1f}+-{g('gaia_e_omega'):.1f} K1={g('gaia_K1'):.2f}")
    tA=tconj(90-w,e,Tp,P); tB=tconj(270-w,e,Tp,P)
    ncyc=(T0-g('gaia_tperi_btjd'))/g('gaia_Per'); print(f'  cycles from Gaia Tp to TESS T0: {ncyc:.1f}; Gaia-P error alone -> {ncyc*g("gaia_e_Per"):.3f} d at TESS epoch')
    for lab,tc in (('A',tA),('B',tB)):
        # (1) propagate Gaia ephemeris forward to the TESS T0
        n=np.round((T0-tc)/P); dphi=(T0-(tc+n*P))/P; dphi=circ(dphi)
        m,s=np.median(dphi),0.5*(np.percentile(dphi,84.13)-np.percentile(dphi,15.87))
        # (2) propagate the observed eclipse back to the Gaia epoch with the eclipse period (error negligible)
        n2=np.round((T0-tc)/Pe); dphi2=circ((T0-n2*Pe-tc)/Pe)
        m2,s2=np.median(dphi2),0.5*(np.percentile(dphi2,84.13)-np.percentile(dphi2,15.87))
        print(f'  primary minus conjunction {lab}: (fwd, Gaia P) {m:+.4f} +- {s:.4f} phase = {m*Pe:+.3f} +- {s*Pe:.3f} d ({abs(m)/s:.2f} sigma) | (back, eclipse P) {m2:+.4f} +- {s2:.4f} ({abs(m2)/s2:.2f} sigma)')
    # secondary phase prediction
    dAB=((tB-tA)/P)%1
    for lab,pred in (('primary=A',dAB),('primary=B',(1-dAB)%1)):
        pm,ps=np.median(pred),0.5*(np.percentile(pred,84.13)-np.percentile(pred,15.87))
        o,oe=OBS[tic]; print(f'  {lab}: predicted secondary phase {pm:.4f} +- {ps:.4f}; observed {o:.5f} +- {oe:.5f} -> {(o-pm)/np.hypot(ps,oe):+.2f} sigma')
    ecw=e*np.cos(np.radians(w)); esw=e*np.sin(np.radians(w))
    print(f'  Gaia e cos w = {np.median(ecw):+.4f} +- {np.std(ecw):.4f}; e sin w = {np.median(esw):+.4f} +- {np.std(esw):.4f}; observed (pi/2)(phi_s-0.5) = {np.pi/2*(OBS[tic][0]-0.5):+.5f} +- {np.pi/2*OBS[tic][1]:.5f}')
    # physics
    K=g('gaia_K1'); Pd=g('gaia_Per'); ec=g('gaia_ecc')
    fm=1.0361e-7*(1-ec**2)**1.5*K**3*Pd
    for M1 in ((1.43,1.50) if tic=='195865529' else (1.2,1.48)):
        m2=0.1
        for _ in range(60): m2=(fm*(M1+m2)**2)**(1/3)
        a=4.2084*(M1+m2)**(1/3)*Pe**(2/3)
        print(f'  f(m)={fm:.4f} Msun; M1={M1}: m2(i=90)={m2:.3f} Msun, a={a:.2f} Rsun')
        K2=K*M1/m2; dtl=Pe*86400/(np.pi*299792.458)*(K2-K)
        print(f'     Roemer delay of secondary eclipse (Kaplan 2010, P(K2-K1)/(pi c)): {dtl:.0f} s = {dtl/86400/Pe:.5f} phase')
    # trapezoid geometry (no LD): sum and difference of fractional radii from T14, T23; solve with depth ~ k^2 for the primary
    T14,T23,dep={'195865529':(5.22,2.16,0.190),'468181994':(3.67,2.41,0.0232)}[tic]
    S14=np.sin(np.pi*T14/24/Pe)**2; S23=np.sin(np.pi*T23/24/Pe)**2
    print(f'  T14={T14} h, T23={T23} h (s7 medians): (r1+r2)>={np.sqrt(S14):.4f}, |r1-r2|>={np.sqrt(S23):.4f} (i=90)')
    best=None
    for ci in np.linspace(0,0.3,30001):
        x=ci**2; sp=np.sqrt(S14*(1-x)+x); sm=np.sqrt(S23*(1-x)+x); r1=(sp+sm)/2; r2=(sp-sm)/2
        k=r2/r1; d=abs(k*k-dep)
        if best is None or d<best[0]: best=(d,ci,r1,r2,k)
    _,ci,r1,r2,k=best; b=ci/r1
    rho=3*np.pi/(6.674e-8*(Pe*86400)**2)/r1**3/1.41
    a=4.2084*(M1+m2)**(1/3)*Pe**(2/3)
    print(f'  -> R1 ~ {r1*a:.2f} Rsun, R2 ~ {r2*a:.2f} Rsun for a={a:.2f} Rsun (last M1 above)')
    J=(0.0513/0.192) if tic=='195865529' else (0.00145/0.0232)
    for T2 in ((4500,5000,5200) if tic=='195865529' else (3200,3400)):
        T1=6600 if tic=='195865529' else 5800
        print(f'  Planck(800 nm) surface-brightness ratio T2={T2} K / T1={T1} K: {planckJ(T2,T1):.3f}  (observed S/P depth ratio {J:.3f})')
    print(f'  flat-bottom solution with k^2=depth({dep}): cos i={ci:.4f} (i={np.degrees(np.arccos(ci)):.1f} deg), r1=R1/a={r1:.4f}, r2={r2:.4f}, k={k:.3f}, b={b:.2f}; rho1 ~ {rho:.2f} rho_sun (ignores m2, LD)')
