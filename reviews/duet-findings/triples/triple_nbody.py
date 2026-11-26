"""N-body tests of whether a Gaia astrometric orbit can be the third body of an
eclipsing binary whose eclipses change (A73, R755, R1003).

For each star and each assumed mutual inclination and tertiary mass, the script
  1. integrates the triple for STAB_ORBITS outer orbits (WHFast) and calls it unstable if the
     inner semi-major axis changes by > 20%, e_in > 0.95 or the outer orbit unbinds;
  2. if stable, integrates 12 years with IAS15 and records every primary eclipse as seen from
     +z (the sky plane is x-y): mid-time (light-travel time included), impact parameter b in
     units of R1 + R2, and single-cycle periods.
It reports the eclipse-timing range after a linear fit, the range of single-cycle periods, how
fast b changes (|db/dt| in (R1+R2) per year) and the fraction of the 12 years with b < 1
(eclipsing at all).  Both orbits are set edge-on (inclination 90 deg to the sky); the mutual
inclination is put in the sky position angle of the outer orbit's node, since eclipses
cannot measure the inner node.  Needs rebound and numpy (pip install rebound numpy).
    python3 reviews/duet-findings/triples/triple_nbody.py [star ...]
Masses and radii are assumptions (below), so read the results as 'which mutual inclinations
can reproduce what TESS shows', not as fits."""
import math, sys
import numpy as np
import rebound

C_AU_PER_DAY = 173.1446
RSUN_AU = 0.00465047
STAB_ORBITS = 2000
IMUTS = (0, 3, 6, 10, 20, 40)
M3S = (0.25, 0.5, 1.0)

STARS = {
    # name: inner P, e, masses (Msun), radii (Rsun), outer orbit from Gaia DR3 (P, e)
    'A73':   dict(P_in=17.538, e_in=0.05, m1=1.2, m2=1.0, R1=1.4, R2=1.0, P_out=124.7248, e_out=0.412,
                  note='Gaia DR3 2290881958791909248 Orbital (Chopard-Vilhem track3 copy)'),
    'A73_e015': dict(P_in=17.538, e_in=0.05, m1=1.2, m2=1.0, R1=1.4, R2=1.0, P_out=124.7248, e_out=0.15,
                  note='A73 with e_out lowered to 0.15 (Gaia value 0.41 is unstable)'),
    'R1003_P83': dict(P_in=2.8787113, e_in=0.49, m1=1.1, m2=0.9, R1=1.1, R2=0.9, P_out=82.6, e_out=0.3, years=4.0, steps=150,
                  imuts=(10, 20, 40, 60), note='R1003 with a hypothetical 82.6-d tertiary (Gaia 206.59 / 2.5)'),
    'R1003_hi': dict(P_in=2.8787113, e_in=0.49, m1=1.1, m2=0.9, R1=1.1, R2=0.9, P_out=206.587, e_out=0.3, years=4.0, steps=150,
                  imuts=(60, 80), note='R1003 with the Gaia period at high mutual inclination'),
    'R755':  dict(P_in=24.6548, e_in=0.13, m1=1.3, m2=0.8, R1=1.5, R2=0.8, P_out=300.805, e_out=0.262,
                  note='Gaia DR3 5523899796082005376 Orbital; inner e from its 24.68-d SB1'),
    'R1003': dict(P_in=2.8787113, e_in=0.49, m1=1.1, m2=0.9, R1=1.1, R2=0.9, P_out=206.587, e_out=0.3, years=4.0, steps=150,
                  note='Gaia DR3 5861580639046056832 Orbital; e_out not in the repository, 0.3 assumed'),
}

def build(s, imut_deg, m3, omega_in=0.5, omega_out=1.3, M_out=0.0, integrator='ias15'):
    sim = rebound.Simulation()
    sim.units = ('day', 'AU', 'Msun')
    sim.integrator = integrator
    sim.add(m=s['m1'])
    sim.add(m=s['m2'], P=s['P_in'], e=s['e_in'], inc=math.pi / 2, Omega=0.0, omega=omega_in, M=0.0)
    sim.add(m=m3, P=s['P_out'], e=s['e_out'], inc=math.pi / 2, Omega=math.radians(imut_deg),
            omega=omega_out, M=M_out)
    sim.move_to_com()
    return sim

def stable(s, imut, m3):
    sim = build(s, imut, m3, integrator='whfast')
    sim.dt = s['P_in'] / 40
    o = sim.particles[1].orbit(primary=sim.particles[0]); a0 = o.a
    T = STAB_ORBITS * s['P_out']; n = 400
    for k in range(1, n + 1):
        sim.integrate(T * k / n, exact_finish_time=0)
        o = sim.particles[1].orbit(primary=sim.particles[0])
        oo = sim.particles[2].orbit(primary=sim.com(last=2))   # Jacobi orbit of the tertiary
        if not (0.8 < o.a / a0 < 1.2) or o.e > 0.95 or oo.e >= 1 or oo.a < 0:
            return False, k / n * STAB_ORBITS
    return True, STAB_ORBITS

def eclipses(s, imut, m3, years=None):
    years = years or s.get('years', 12.0)
    sim = build(s, imut, m3)
    p = sim.particles
    Rsum = (s['R1'] + s['R2']) * RSUN_AU
    dt = s['P_in'] / s.get('steps', 400)
    t_end = years * 365.25
    times, bs, sec = [], [], []
    def f():
        rx, ry = p[1].x - p[0].x, p[1].y - p[0].y
        return rx * (p[1].vx - p[0].vx) + ry * (p[1].vy - p[0].vy), math.hypot(rx, ry), p[1].z - p[0].z
    prev = f(); t = 0.0
    while t < t_end:
        t += dt; sim.integrate(t)
        cur = f()
        if prev[0] < 0 <= cur[0] and cur[2] > 0:          # sky-separation minimum, star 2 in front
            x = prev[0] / (prev[0] - cur[0]); tm = t - dt + x * dt
            sep = prev[1] + x * (cur[1] - prev[1])
            zc = (p[0].m * p[0].z + p[1].m * p[1].z) / (p[0].m + p[1].m)   # inner-pair barycentre along LOS
            times.append(tm - zc / C_AU_PER_DAY); bs.append(sep / Rsum)
        elif prev[0] < 0 <= cur[0] and cur[2] <= 0 and times:   # secondary conjunction
            x = prev[0] / (prev[0] - cur[0]); sec.append((t - dt + x * dt, times[-1]))
        prev = cur
    times, bs = np.array(times), np.array(bs)
    E = np.arange(len(times), dtype=float)              # one primary conjunction per inner orbit
    yrs = (times - times[0]) / 365.25
    w5 = yrs <= min(5.0, yrs[-1])                                     # a TESS-like 5-year span
    A5 = np.vstack([np.ones(w5.sum()), E[w5]]).T
    coef, *_ = np.linalg.lstsq(A5, times[w5], rcond=None)
    oc5 = times[w5] - A5 @ coef
    per = np.diff(times)
    out = np.nonzero(bs >= 1)[0]
    t_out = yrs[out[0]] if len(out) else float('inf')   # years until the eclipses first stop
    sp = np.array([(ts - tp) / s['P_in'] for ts, tp in sec if (tp - times[0]) / 365.25 <= 5.0])
    sp_range = (sp.min(), sp.max()) if len(sp) else (float('nan'), float('nan'))
    db5 = (bs[w5].max() - bs[w5].min()) / min(5.0, yrs[-1])
    return dict(sp_min=sp_range[0], sp_max=sp_range[1], db5=db5, oc5_range_h=24 * (oc5.max() - oc5.min()), per_min=per.min(), per_max=per.max(),
                b_start=bs[0], b_5yr=bs[w5][-1], years_to_b1=t_out, frac_ecl=float(np.mean(bs < 1)), n=len(bs))

def main(names):
    for name in names:
        s = STARS[name]
        print('\n%s: P_in %.4f d, P_out %.2f d (ratio %.1f), e_out %.2f; %s' % (
            name, s['P_in'], s['P_out'], s['P_out'] / s['P_in'], s['e_out'], s['note']))
        print('  m3   i_mut  stable (outer orbits)  O-C range in 5 yr (h)  single-cycle P (d)  b0 -> b(5 yr)  |b| change/yr  years to b>1  eclipsing  secondary phase (5 yr)')
        for m3 in s.get('m3s', M3S):
            for imut in s.get('imuts', IMUTS):
                ok, n = stable(s, imut, m3)
                if not ok:
                    print('  %.2f %3d    UNSTABLE after %.0f' % (m3, imut, n)); continue
                r = eclipses(s, imut, m3)
                print('  %.2f %3d    yes (%d)              %7.2f              %.3f-%.3f     %.2f -> %.2f    %5.3f        %6.2f        %.2f      %.3f-%.3f' % (
                    m3, imut, n, r['oc5_range_h'], r['per_min'], r['per_max'], r['b_start'], r['b_5yr'], r['db5'], r['years_to_b1'], r['frac_ecl'], r['sp_min'], r['sp_max']))

if __name__ == '__main__':
    main(sys.argv[1:] or ['A73', 'A73_e015', 'R755', 'R1003', 'R1003_P83', 'R1003_hi'])
