"""Physics: mass function, m2, a, separations/velocities at both conjunctions, central durations, impact parameter implied
by the B duration, whether A can eclipse, overlap-area depth checks, neighbour dilution. -> physics.txt"""
import numpy as np, json
P, K, e, w = 27.476839, 34.53659, 0.44494, np.radians(313.215); sK = 0.6466; se = 0.0130; sw = np.radians(1.97)
G = 2.959122e-4  # AU^3 / (Msun d^2)
fM = 1.0361e-7 * (1 - e**2)**1.5 * K**3 * P
print(f'f(M) = {fM:.4f} Msun')
def m2of(M1):
    m = 0.1
    for _ in range(200): m = (fM * (M1 + m)**2)**(1/3)
    return m
RS = 215.032
for M1, R1 in ((1.15, 1.15), (1.244, 1.249), (1.35, 1.40)):
    m2 = m2of(M1); R2 = m2**0.8 if m2 < 1 else m2**0.57   # rough MS radius
    a = (G * (M1 + m2) * P**2 / (4*np.pi**2))**(1/3) * RS
    print(f'M1 {M1} R1 {R1}: m2(i=90) {m2:.3f} Msun (R2~{R2:.2f}), a {a:.1f} Rsun')
    for lab, nu in (('A', np.pi/2 - w), ('B', 1.5*np.pi - w)):
        r = a * (1 - e**2) / (1 + e*np.cos(nu)); v = 2*np.pi*a/P * (1 + e*np.cos(nu)) / np.sqrt(1 - e**2)  # Rsun/d transverse at conj
        Tc = 2 * (R1 + R2) / v * 24
        print(f'   {lab}: nu {np.degrees(nu)%360:6.1f}  sep r {r:5.1f} Rsun  v_t {v:5.1f} Rsun/d  central T14 {Tc:5.2f} h  P(ecl)~(R1+R2)/r {100*(R1+R2)/r:4.1f}%')
    # B observed T14 3.40 h -> impact (in units of R1+R2): T = Tc*sqrt(1-bb^2)
    nuB = 1.5*np.pi - w; rB = a*(1-e**2)/(1+e*np.cos(nuB)); vB = 2*np.pi*a/P*(1+e*np.cos(nuB))/np.sqrt(1-e**2); TcB = 2*(R1+R2)/vB*24
    bb = np.sqrt(max(0, 1 - (3.40/TcB)**2)); cosi = bb*(R1+R2)/rB
    nuA = np.pi/2 - w; rA = a*(1-e**2)/(1+e*np.cos(nuA)); bA = rA*cosi/(R1+R2)
    print(f'   B T14 3.40 h vs central {TcB:.2f} h -> b_B/(R1+R2) {bb:.2f}, i {np.degrees(np.arccos(cosi)):.2f} deg; at A b_A/(R1+R2) = {bA:.2f} -> {"NO A eclipse" if bA > 1 else "A eclipse expected"}')
    # largest R1+R2 sum for which b_A<1 would need central T_B <= 3.40/sqrt(1-(rB/rA)^2)
    Tmax = 3.40 / np.sqrt(1 - (rB/rA)**2); print(f'   A would eclipse only if central T14(B) <= {Tmax:.2f} h, i.e. R1+R2 <= {Tmax/24*vB/2:.2f} Rsun')
    # overlap at closest approach
    k = R2/R1; d = bb*(1+k)
    def ov(d, k):
        if d >= 1+k: return 0.0
        if d <= 1-k: return np.pi*k*k
        a1 = np.arccos((d*d+1-k*k)/(2*d)); a2 = np.arccos((d*d+k*k-1)/(2*d*k))
        return a1 + k*k*a2 - 0.5*np.sqrt((-d+1+k)*(d+k-1)*(d-k+1)*(d+k+1))
    A = ov(d, k)
    print(f'   at mid-B: d {d:.2f} R1, overlap {A/np.pi:.4f} of primary disk, {A/(np.pi*k*k):.3f} of companion disk')
    print(f'     if B = companion in front of primary (transit): depth ~ {A/np.pi*100*0.8:.2f}% x L1frac (limb-darkened edge ~0.8)')
    print(f'     if B = primary in front of companion (occultation): depth ~ {A/(np.pi*k*k)*100:.1f}% x L2frac  -> needs L2frac ~ {1.7/(A/(np.pi*k*k)):.1f}%')
# Gaia e,w sampled -> fraction where A eclipse is geometrically excluded given B duration (M1=1.244)
rng = np.random.default_rng(3); n = 20000; ee = rng.normal(e, se, n); ww = rng.normal(w, sw, n); M1 = rng.normal(1.244, 0.1, n); R1 = rng.normal(1.249, 0.08, n)
m2 = np.array([ (lambda M: [ (x:=0.1), [ (x:=( (1.0361e-7*(1-E**2)**1.5*K**3*P)*(M+x)**2)**(1/3)) for _ in range(60)] , x][2])(M) for M,E in zip(M1,ee)])
R2 = m2**0.8; a = (G*(M1+m2)*P**2/(4*np.pi**2))**(1/3)*RS
rB = a*(1-ee**2)/(1+ee*np.cos(1.5*np.pi-ww)); rA = a*(1-ee**2)/(1+ee*np.cos(np.pi/2-ww)); vB = 2*np.pi*a/P*(1+ee*np.cos(1.5*np.pi-ww))/np.sqrt(1-ee**2)
TcB = 2*(R1+R2)/vB*24; bb = np.sqrt(np.clip(1-(3.40/TcB)**2, 0, 1)); bA = bb*rA/rB
print(f'MC (e,w Gaia; M1 1.244+-0.1, R1 1.249+-0.08, R2=m2^0.8): central T14(B) {np.median(TcB):.2f} h; b_B {np.median(bb):.2f}; b_A {np.median(bA):.2f} [{np.percentile(bA,2.5):.2f}, {np.percentile(bA,97.5):.2f}]; P(b_A<1) = {np.mean(bA<1):.4f}')
print(f'e sin w (Gaia) {e*np.sin(w):+.3f}: T(A)/T(B) central = rA/rB = (1+e cos nuB)/(1+e cos nuA) = {(1+e*np.cos(1.5*np.pi-w))/(1+e*np.cos(np.pi/2-w)):.2f}')
# dilution
g = json.load(open('gaia.json')); G0 = float(g['src'][0]['phot_g_mean_mag'])
print('Neighbours (G<16, <90"): fractional dip each would need for an observed 1.70%:')
for r in g['nb'][1:]:
    Gm = float(r['phot_g_mean_mag'] or 99)
    if Gm < 16: print(f"   G {Gm:.2f} sep {float(r['sep']):.1f}\": needs {1.70*10**(0.4*(Gm-G0)):.0f}%")
