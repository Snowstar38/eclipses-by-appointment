"""R1117 (TIC 299941037): what can make the two eclipse depths drift apart?

Toy model of a detached grazing binary (P = 2.636664 d). Two limb-darkened
stars; depth at each conjunction computed by numerically integrating the
covered part of the eclipsed star. Compares three ways to move the depth ratio
B/A from ~0.93 (2020-21) to ~0.80 (2025):
  1. inclination drift, circular orbit (both conjunctions at same separation)
  2. inclination drift with a fixed small e*sin(w)
  3. change of e*sin(w) at fixed inclination (separations at the two
     conjunctions move in opposite directions)
Input data: Fable's per-sector depths (r1117-per-sector.csv, house QLP/SPOC
cache, 2026-11-25). Usage: python3 r1117_geometry.py r1117-per-sector.csv
"""
import sys, csv, numpy as np

P = 2.636664
M1, M2 = 1.0, 0.9          # Msun (assumed)
R1, R2 = 1.0, 0.9          # Rsun (assumed)
T1, T2 = 5800., 5500.      # K  (assumed; only the SB ratio matters)
G = 2.959122e-4            # AU^3/Msun/d^2
a = (G*(M1+M2)*P**2/(4*np.pi**2))**(1/3) * 215.032  # Rsun
u1, u2 = 0.45, 0.50        # linear limb darkening

def sb(T):  # TESS-band surface brightness ~ Planck at 0.8 micron
    lam = 0.8e-6; h=6.626e-34; c=3e8; k=1.381e-23
    return 1/(np.exp(h*c/(lam*k*T))-1)
S1, S2 = sb(T1), sb(T2)

N = 600
def flux_blocked(Rb, Rf, d, u, S):
    """flux of back star (radius Rb, LD u, SB S) hidden by front star at sky separation d"""
    x = np.linspace(-Rb, Rb, N); X, Y = np.meshgrid(x, x)
    r2 = X**2+Y**2; on = r2 < Rb**2
    mu = np.sqrt(np.clip(1-r2/Rb**2, 0, 1))
    I = S*(1-u*(1-mu))
    cov = on & ((X-d)**2+Y**2 < Rf**2)
    return (I*cov).sum(), (I*on).sum()

_, F1 = flux_blocked(R1, R2, 99, u1, S1)
_, F2 = flux_blocked(R2, R1, 99, u2, S2)
scale = lambda R: (2*R/N)**2
Ftot = F1*scale(R1) + F2*scale(R2)

def depths(inc_deg, esinw=0.0, e=None):
    ci = np.cos(np.radians(inc_deg))
    if e is None: e = abs(esinw)
    # conjunction where star 1 is eclipsed (A) and star 2 eclipsed (B)
    rA = a*(1-e**2)/(1+esinw); rB = a*(1-e**2)/(1-esinw)
    dA, dB = rA*ci, rB*ci
    bA, _ = flux_blocked(R1, R2, dA, u1, S1)
    bB, _ = flux_blocked(R2, R1, dB, u2, S2)
    return bA*scale(R1)/Ftot, bB*scale(R2)/Ftot

def T14(inc_deg, r):
    b = r*np.cos(np.radians(inc_deg))
    s = (R1+R2)**2 - b**2
    return P*24/np.pi*np.sqrt(max(s,0))/a

if __name__ == "__main__":
    rows = list(csv.DictReader(open(sys.argv[1])))
    era = lambda s: '2020-21' if s < 50 else ('2023' if s < 80 else '2025')
    print(f"a = {a:.2f} Rsun, (R1+R2)/a = {(R1+R2)/a:.3f}, SB ratio S2/S1 = {S2/S1:.3f}")
    print("\nObserved (Fable): era, product, median coreA, coreB, ratio(peak)")
    for e_ in ['2020-21','2023','2025']:
        for prod in ['SPOC','QLP']:
            sel=[r for r in rows if era(int(r['sector']))==e_ and (float(r['cadence_min'])<2.5)==(prod=='SPOC')]
            if not sel: continue
            A=np.median([float(r['coreA_ppt']) for r in sel]); B=np.median([float(r['coreB_ppt']) for r in sel])
            R=np.median([float(r['peak_ratio_BA']) for r in sel])
            print(f"  {e_:8s} {prod:4s} n={len(sel):2d} A={A:6.1f} B={B:6.1f} B/A(core)={B/A:.3f} peak={R:.3f}")
    print("\n1. Circular orbit, inclination drift: depth A, depth B, B/A, T14(h)")
    for inc in np.arange(83.6, 85.81, 0.2):
        A,B = depths(inc)
        print(f"  i={inc:5.2f}  A={A*1e3:6.1f} ppt  B={B*1e3:6.1f}  B/A={B/A:.3f}  T14={T14(inc,a):.2f}")
    # pick inclination giving A ~ 0.09 (undiluted guess)
    incs = np.arange(83.0, 87.0, 0.01)
    iA = min(incs, key=lambda i: abs(depths(i)[0]-0.090))
    A0,B0 = depths(iA)
    print(f"\n   reference i = {iA:.2f}: A={A0*1e3:.1f}, B={B0*1e3:.1f}, B/A={B0/A0:.3f}")
    print("\n3. Fixed i, vary e*sin(w): A, B, B/A")
    for es in [0,0.001,0.002,0.003,0.004,0.006,0.008]:
        A,B = depths(iA, es)
        print(f"  esinw={es:+.3f}  A={A*1e3:6.1f}  B={B*1e3:6.1f}  B/A={B/A:.3f}  (B/A relative to circular {B/A/(B0/A0):.3f})")
    print("\n2. Fixed esinw=+0.002, inclination drift: A, B, B/A")
    for inc in np.arange(iA-0.6, iA+0.61, 0.2):
        A,B = depths(inc, 0.002)
        print(f"  i={inc:5.2f}  A={A*1e3:6.1f}  B={B*1e3:6.1f}  B/A={B/A:.3f}")

def report_tests(rows):
    print("\n4. Inclination range: B/A over depths 15-290 ppt (circular):",
          f"{depths(80.0)[1]/depths(80.0)[0]:.3f} to {depths(85.8)[1]/depths(85.8)[0]:.3f}")
    i0 = 81.9  # A ~ 80 ppt, T14 ~ 2.6 h (house box width 1.0 h is a lower bound)
    A0, B0 = depths(i0)
    print(f"   working point i={i0}: A={A0*1e3:.1f} ppt, B/A={B0/A0:.3f}, T14={T14(i0,a):.2f} h")
    for es in [0.005, 0.010, 0.015]:
        A, B = depths(i0, es)
        rA = a*(1-es**2)/(1+es); rB = a*(1-es**2)/(1-es)
        print(f"   esinw={es:.3f}: B/A x{(B/A)/(B0/A0):.3f}; T14 A {T14(i0,rA):.2f} h, B {T14(i0,rB):.2f} h")
    # sector-to-sector scatter of the core ratio about a linear trend in time (sector number)
    s = np.array([int(r['sector']) for r in rows]); cr = np.array([float(r['coreB_ppt'])/float(r['coreA_ppt']) for r in rows])
    pr = np.array([float(r['peak_ratio_BA']) for r in rows])
    for name, y in [('core B/A', cr), ('peak B/A', pr)]:
        c = np.polyfit(s, y, 1); res = y - np.polyval(c, s)
        print(f"   {name}: slope {c[0]*13.4:+.4f} per year (13.4 sectors per year); rms about trend {res.std(ddof=2):.4f}")
        for lo, hi, lab in [(0,50,'2020-21 SPOC'),(50,80,'2023 QLP'),(80,100,'2025')]:
            m = (s>=lo)&(s<hi); print(f"      {lab}: rms {res[m].std(ddof=1):.4f} (n={m.sum()})")

if __name__ == "__main__":
    report_tests(list(csv.DictReader(open(sys.argv[1]))))
