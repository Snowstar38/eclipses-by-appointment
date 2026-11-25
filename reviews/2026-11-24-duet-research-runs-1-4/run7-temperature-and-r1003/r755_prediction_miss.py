"""Run 7d (Duet): how far can R755's eclipses drift from a two-eclipse linear ephemeris over
the ~30 cycles (2 years) between TESS s89 and the paper's predicted BTJD 4327.29 and 4351.95?
Uses triple_nbody.py's R755 model (Gaia's 300.8-d orbit as the tertiary, assumed masses), starts
the clock at 8 points spread over one outer orbit, and reports the miss after 28-30 cycles.
Needs rebound and numpy.  Run from the repository root:
    python3 reviews/2026-11-24-duet-research-runs-1-4/run7-temperature-and-r1003/r755_prediction_miss.py"""
import copy, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import triple_nbody as T

s = copy.deepcopy(T.STARS['R755'])
print('m3   i_mut   miss after 28-30 cycles (h): median, max over 8 starting phases of the outer orbit')
orig = T.build
for m3 in (0.25, 0.5, 1.0):
    for imut in (3, 10, 20):
        miss = []
        for k in range(8):
            M = 2 * np.pi * k / 8
            sim = orig(s, imut, m3, M_out=M)
            p = sim.particles; dt = s['P_in'] / 300; t = 0.0; times = []
            def f():
                rx, ry = p[1].x - p[0].x, p[1].y - p[0].y
                return rx * (p[1].vx - p[0].vx) + ry * (p[1].vy - p[0].vy), p[1].z - p[0].z
            prev = f()
            while len(times) < 31:
                t += dt; sim.integrate(t); cur = f()
                if prev[0] < 0 <= cur[0] and cur[1] > 0:
                    x = prev[0] / (prev[0] - cur[0]); tm = t - dt + x * dt
                    zc = (p[0].m * p[0].z + p[1].m * p[1].z) / (p[0].m + p[1].m)
                    times.append(tm - zc / T.C_AU_PER_DAY)
                prev = cur
            P2 = times[1] - times[0]
            miss.append(max(abs(times[n] - (times[0] + n * P2)) for n in (28, 29, 30)) * 24)
        print('%.2f  %3d     %5.1f  %5.1f' % (m3, imut, np.median(miss), max(miss)))
