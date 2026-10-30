# Extra geometry / timing / physics checks (new in this resume):
# (1) secondary phase per observing season from the fixed-shape times (s08), (2) e cos w implied by the measured secondary
# phase (exact Kepler, using Gaia's e sin w distribution), (3) e sin w from the S/P duration ratio (407877153: flat-bottomed),
# (4) weighted mean depth at phase 0.5 (283532878), (5) rough physics from f(m), TIC radius/Teff, (6) ephemeris + next primaries in UTC.
import json, re, numpy as np
from common import GAIA
from scipy.optimize import brentq
from astropy.time import Time; from astropy.coordinates import SkyCoord, EarthLocation; import astropy.units as u
fx=json.load(open('s08_shape_oddeven.json')); rng=np.random.default_rng(7); N=20000
def M_of_nu(nu,e):
    E=2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2),np.sqrt(1+e)*np.cos(nu/2)); return E-e*np.sin(E)
def sepAB(ecw,esw):
    e=np.hypot(ecw,esw); w=np.arctan2(esw,ecw)
    return ((M_of_nu(np.pi/2-w,e)-M_of_nu(3*np.pi/2-w,e))/(2*np.pi))%1   # phase of A after B ... see below
COORD={'283532878':(327.869175189832,57.9849184374285),'407877153':(275.783436380745,-79.3525721366319)}
for tic,g in GAIA.items():
    eph=json.load(open(f's05_ephem_{tic}.json')); P=eph['P']; T0P=eph['T0P']
    print('=====',tic)
    # (1) per-season secondary phase from fixed-shape event times, QLP+SPOC (one per event, SPOC preferred)
    ev={}
    for o in fx[tic]['fixed']:
        k=(o['kind'],o['n'])
        if k not in ev or o['author']=='TESS-SPOC': ev[k]=o
    seasons={}
    for (kind,n),o in ev.items():
        yr=int(o['sector'])//13 if int(o['sector'])<40 else (int(o['sector'])-1)//7
        seasons.setdefault(yr,{'P':[],'S':[]})[kind].append(o)
    for yr,dd in sorted(seasons.items()):
        if not dd['S']: continue
        # secondary phase relative to the global primary ephemeris
        phs=np.array([((o['t0']-T0P)/P)%1 for o in dd['S']]); e_=np.array([o['et0']/P for o in dd['S']]); w_=1/e_**2
        mp=np.sum(w_*phs)/np.sum(w_); emp=1/np.sqrt(np.sum(w_))
        ocP=[(o['t0']-T0P-o['n']*P)*1440 for o in dd['P']]
        print(f'  season sectors {sorted(set(o["sector"] for o in dd["S"]+dd["P"]))}: secondary phase {mp:.5f}±{emp:.5f} (N={len(phs)}); primary O-C (min) {", ".join("%+.1f"%x for x in ocP)}')
    ph2=eph['ph2']; eph2=eph['eph2']
    # (2) e cos w implied by the measured secondary phase, for Gaia draws of e sin w
    e=np.abs(g['e']+g['ee']*rng.standard_normal(N)); w=np.radians(g['w']+g['ew']*rng.standard_normal(N)); esw=e*np.sin(w); ecw_g=e*np.cos(w)
    # measured: secondary (B) occurs ph2 after primary (A); so phase(B)-phase(A) = ph2
    def dBA(ecw,esw):
        e=np.hypot(ecw,esw); w=np.arctan2(esw,ecw)
        return ((M_of_nu(3*np.pi/2-w,e)-M_of_nu(np.pi/2-w,e))/(2*np.pi))%1
    imp=[]
    for s in esw[:4000]:
        try: imp.append(brentq(lambda c: dBA(c,s)-ph2,-0.9*np.sqrt(max(0.81-s*s,1e-6)),0.9*np.sqrt(max(0.81-s*s,1e-6))))
        except ValueError: pass
    imp=np.array(imp)
    print(f'  measured secondary phase {ph2:.5f}±{eph2:.5f}; first-order e cos w = pi/2*(ph2-0.5) = {np.pi/2*(ph2-0.5):.4f}')
    print(f'  exact e cos w implied (Gaia e sin w draws, N={len(imp)}): {np.mean(imp):.4f}±{np.std(imp):.4f}; Gaia e cos w {np.mean(ecw_g):.4f}±{np.std(ecw_g):.4f}; diff {(np.mean(imp)-np.mean(ecw_g))/np.hypot(np.std(imp),np.std(ecw_g)):+.2f} sigma')
    # (3) duration ratio -> e sin w (same impact parameter assumed; valid only if both eclipses non-grazing)
    sP=fx[tic]['shape']['P']; sS=fx[tic]['shape']['S']; R=sS['T14']/sP['T14']; eR=R*np.hypot(sS['eT14']/sS['T14'],sP['eT14']/sP['T14'])
    # T_B/T_A = (1+e sin w)/(1-e sin w)  -> e sin w = (R-1)/(R+1)
    print(f'  T14(S)/T14(P) = {R:.3f}±{eR:.3f} -> e sin w (equal-b approx) = {(R-1)/(R+1):+.3f}±{2*eR/(R+1)**2:.3f}; Gaia e sin w {np.mean(esw):+.3f}±{np.std(esw):.3f}')
    # (5) physics
    K=g['K1']; Pd=g['P']; fm=1.0361e-7*(1-g['e']**2)**1.5*K**3*Pd
    tic_par={'283532878':(1.35,1.89236,6531.0),'407877153':(0.87,1.91196,5168.0)}[tic]
    M1,R1,T1=tic_par
    m2=brentq(lambda m: m**3/(M1+m)**2-fm,1e-3,5)
    a=(M1+m2)**(1/3)*(P/365.25)**(2/3)*215.032
    print(f'  f(m)={fm:.4f} Msun; TIC M1={M1}, R1={R1:.2f}, Teff={T1}; m2(i=90)={m2:.3f} Msun; a={a:.1f} Rsun (a/R1={a/R1:.1f})')
    dP=sP['d']; dS=sS['d']; r23=sP['r23']
    for lab,cosnu in (('A (primary)',np.sin(np.radians(g['w']))),('B (secondary)',-np.sin(np.radians(g['w'])))):
        fac=np.sqrt(1-g['e']**2)/(1+g['e']*cosnu)
        print(f'    conj {lab}: separation {a*(1-g["e"]**2)/(1+g["e"]*cosnu):.1f} Rsun; central T14 for R2=k*R1 (k from depth) ~ {24*P/np.pi*R1*(1+np.sqrt(dP))/a*fac:.2f} h (observed P {24*sP["T14"]:.2f} h, S {24*sS["T14"]:.2f} h)')
    k=np.sqrt(dP); print(f'  flat-bottom approx k=sqrt(depthP)={k:.3f} -> R2~{k*R1:.2f} Rsun; depthS/depthP={dS/dP:.3f} (= surface-brightness ratio if both total/flat)')
    lam=0.8e-6; c2=0.014388
    Tg=np.linspace(2500,T1,2000); ratio=(np.exp(c2/(lam*T1))-1)/(np.exp(c2/(lam*Tg))-1)
    print(f'  Planck(800 nm) T2 giving that ratio: {Tg[np.argmin(np.abs(ratio-dS/dP))]:.0f} K')
    # (6) ephemeris and next primaries in UTC (barycentric -> geocentric light-time removed)
    c=SkyCoord(*COORD[tic],unit='deg'); loc=EarthLocation.from_geocentric(0,0,0,unit=u.m)
    print(f'  EPHEMERIS: T0 = BJD_TDB {2457000+T0P:.5f} ± {eph["eT0P"]:.5f} (BTJD {T0P:.5f}); P = {P:.6f} ± {eph["eP"]:.6f} d; secondary T0 BTJD {eph["T0S"]:.5f} ± {eph["eT0S"]:.5f}')
    now=Time('2026-10-30T00:00:00',scale='utc'); nb=now.tdb.jd-2457000
    n0=int(np.ceil((nb-T0P)/P))
    C=np.array(eph['C'])
    for n in range(n0,n0+3):
        bt=T0P+n*P; et=np.sqrt(C[0,0]+n*n*C[2,2]+2*n*C[0,2])
        tb=Time(bt+2457000,format='jd',scale='tdb')
        tg=tb
        for _ in range(3):
            ltt=tg.light_travel_time(c,kind='barycentric',location=loc); tg=tb-ltt
        print(f'    next primary n={n}: BTJD {bt:.4f} ± {et:.4f} d ({et*1440:.1f} min) -> UTC (geocentric) {tg.utc.iso[:16]} (light-time {ltt.to(u.min).value:+.1f} min)')
    nS0=int(np.ceil((nb-eph['T0S'])/P))
    print('    next secondaries BTJD: '+', '.join(f'{eph["T0S"]+n*P:.3f}' for n in range(nS0,nS0+3)))
# (4) phase-0.5 depth (283532878) from s08 output
v=[tuple(map(float,m)) for m in re.findall(r'PH0.5 .* = ([-\d.]+)±([\d.]+) ppt',open('s08_shape_oddeven.out').read())]
d=np.array([x[0] for x in v]); e=np.array([x[1] for x in v]); w=1/e**2
print(f'283532878 phase-0.5 (primary shape, fixed time): N={len(d)} weighted mean {np.sum(w*d)/np.sum(w):+.2f}±{1/np.sqrt(np.sum(w)):.2f} ppt, chi2={np.sum(w*(d-np.sum(w*d)/np.sum(w))**2):.1f}/{len(d)-1}')
