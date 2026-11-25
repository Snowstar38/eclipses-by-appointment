"""Run 9c (Duet): can Gaia's 206.6-d orbit switch R1003's eclipses on in <= 2.7 yr?

Uses Gaia DR3 5861580639046056832 as measured (Fable's ESA TAP copy, 2026-11-25):
P_out = 206.587 d, e_out = 0.491, astrometric inclination 70.3 deg, and the tertiary mass
implied by the photocentre orbit (tertiary_mass.py: m3 = 0.23 Msun for a 1.1 + 0.9 Msun
inner pair; 0.5 and 1.0 Msun shown for contrast). Inner pair: P = 2.8787113 d, e = 0.49
(run 7), R1 + R2 = 2.0 Rsun, near edge-on. The sky inclination of the outer orbit fixes the
mutual inclination's lower bound: an eclipsing inner orbit has i_in = 79-101 deg, so
i_mut >= ~9 deg; with i_in = 90 deg exactly, i_mut >= 19.7 deg.
REBOUNDx adds general relativity ('gr', all bodies) so apsidal precession is not ignored.
Output: for each m3 and mutual inclination, the fastest change of the impact parameter b
(units of R1 + R2) over any 2.7-yr window in 12 yr, and whether e_in or the orbit runs away.
Needs rebound, reboundx, numpy.  python3 r1003_switchon.py
"""
import math, sys
import numpy as np
import rebound, reboundx

C = 173.1446; RSUN = 0.00465047
P_IN, E_IN, M1, M2, RSUM = 2.8787113, 0.49, 1.1, 0.9, 2.0
P_OUT, E_OUT, I_OUT = 206.587, 0.491, math.radians(70.3)
YEARS, WIN = 12.0, 2.7

def run(m3, dnode_deg, w_in=0.6, w_out=1.3, M_out=0.0, gr=True):
    sim = rebound.Simulation(); sim.units = ('day', 'AU', 'Msun'); sim.integrator = 'ias15'
    sim.add(m=M1)
    sim.add(m=M2, P=P_IN, e=E_IN, inc=math.pi/2, Omega=math.radians(dnode_deg), omega=w_in, M=0.0)
    sim.add(m=m3, P=P_OUT, e=E_OUT, inc=I_OUT, Omega=0.0, omega=w_out, M=M_out)
    sim.move_to_com()
    if gr:
        rx = reboundx.Extras(sim); g = rx.load_force('gr_full'); rx.add_force(g); g.params['c'] = C
    p = sim.particles
    o_in = p[1].orbit(primary=p[0]); o_out = p[2].orbit(primary=sim.com(last=2))
    n1 = np.array([math.sin(o_in.inc)*math.sin(o_in.Omega), -math.sin(o_in.inc)*math.cos(o_in.Omega), math.cos(o_in.inc)])
    n2 = np.array([math.sin(o_out.inc)*math.sin(o_out.Omega), -math.sin(o_out.inc)*math.cos(o_out.Omega), math.cos(o_out.inc)])
    imut = math.degrees(math.acos(np.clip(n1 @ n2, -1, 1)))
    dt = P_IN / 120; t = 0.0; T, B, EIN = [], [], []
    def f():
        rx_, ry_ = p[1].x - p[0].x, p[1].y - p[0].y
        return rx_*(p[1].vx - p[0].vx) + ry_*(p[1].vy - p[0].vy), math.hypot(rx_, ry_), p[1].z - p[0].z
    prev = f()
    while t < YEARS * 365.25:
        t += dt; sim.integrate(t); cur = f()
        if prev[0] < 0 <= cur[0] and cur[2] > 0:
            x = prev[0] / (prev[0] - cur[0])
            T.append(t - dt + x*dt); B.append((prev[1] + x*(cur[1] - prev[1])) / (RSUM*RSUN))
            if len(T) % 50 == 0: EIN.append(p[1].orbit(primary=p[0]).e)
        prev = cur
    T, B = np.array(T)/365.25, np.array(B)
    best = 0.0
    for t0 in np.arange(0, YEARS - WIN, 0.25):
        m = (T >= t0) & (T < t0 + WIN)
        if m.sum() > 10: best = max(best, abs(np.polyfit(T[m], B[m], 1)[0]))
    return imut, best, B.min(), B.max(), min(EIN), max(EIN)

if __name__ == '__main__':
    print("m3   node  i_mut  max|db/dt| per yr (2.7-yr window)  b range in 12 yr   e_in range")
    for m3 in (0.23, 0.5, 1.0):
        for dn in (0, 30, 50, 70, 90, 120):
            r = run(m3, dn)
            print(f"{m3:4.2f} {dn:4d}  {r[0]:5.1f}   {r[1]:6.3f}                          {r[2]:5.2f}-{r[3]:5.2f}       {r[4]:.3f}-{r[5]:.3f}", flush=True)
