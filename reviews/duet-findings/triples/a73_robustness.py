"""How robust is the A73 match?  Varies the outer eccentricity, the tertiary mass
and the starting orientation of the outer orbit (argument of periastron and mean anomaly) at a
mutual inclination of 5 degrees, and compares with what TESS shows for A73 over 2019-2024
(paper Figure 4): secondary phase 0.461-0.532, single-cycle periods 17.39-17.85 d, primary
O-C within about +-6 h of a linear ephemeris, and the eclipses fading over ~4 years.
Needs rebound and numpy.  Run from the repository root:
    python3 reviews/duet-findings/triples/a73_robustness.py"""
import copy, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import triple_nbody as T

base = copy.deepcopy(T.STARS['A73'])
OBS = 'observed: sec. phase 0.461-0.532, cycles 17.39-17.85 d, O-C ~13 h peak to peak, fade over ~4 yr'
print(OBS)
print('e_out  m3    omega_out M_out  stable  sec. phase (5 yr)  single cycles (d)  O-C 5 yr (h)  |b| change/yr')
orig_build = T.build
for e_out in (0.1, 0.15, 0.2, 0.25):
    for m3 in (0.3, 0.4):
        for om, M in ((1.3, 0.0), (3.0, 2.0), (4.6, 4.0)):
            s = copy.deepcopy(base); s['e_out'] = e_out
            T.build = lambda s_, imut, m3_, integrator='ias15', om=om, M=M: orig_build(
                s_, imut, m3_, omega_out=om, M_out=M, integrator=integrator)
            ok, n = T.stable(s, 5, m3)
            if not ok:
                print('%.2f   %.1f   %.1f       %.1f    no (%d)' % (e_out, m3, om, M, n)); continue
            r = T.eclipses(s, 5, m3, years=6.0)
            print('%.2f   %.1f   %.1f       %.1f    yes     %.3f-%.3f        %.2f-%.2f        %5.1f          %.3f' % (
                e_out, m3, om, M, r['sp_min'], r['sp_max'], r['per_min'], r['per_max'], r['oc5_range_h'], r['db5']))
T.build = orig_build
