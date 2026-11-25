"""Run 9c robustness: R1003 with Gaia's m3 = 0.23 Msun, sampling the inner pair's starting
sky inclination (84, 90, 96 deg), node offsets and the outer orbit's argument of periastron
and phase. Reports the largest |db/dt| (per yr, 2.7-yr windows) found in any configuration.
python3 r1003_switchon_robust.py [m3]"""
import sys, math, itertools
import numpy as np
import rebound, reboundx
sys.path.insert(0, __import__('os').path.dirname(__file__))
import r1003_switchon as R

def run(m3, inc_in, dn, w_out, M_out):
    sim = rebound.Simulation(); sim.units = ('day', 'AU', 'Msun'); sim.integrator = 'ias15'
    sim.add(m=R.M1)
    sim.add(m=R.M2, P=R.P_IN, e=R.E_IN, inc=math.radians(inc_in), Omega=math.radians(dn), omega=0.6, M=0.0)
    sim.add(m=m3, P=R.P_OUT, e=R.E_OUT, inc=R.I_OUT, Omega=0.0, omega=w_out, M=M_out)
    sim.move_to_com()
    rx = reboundx.Extras(sim); g = rx.load_force('gr_full'); rx.add_force(g); g.params['c'] = R.C
    p = sim.particles; dt = R.P_IN / 100; t = 0.0; T, B = [], []
    def f():
        a, b = p[1].x - p[0].x, p[1].y - p[0].y
        return a*(p[1].vx - p[0].vx) + b*(p[1].vy - p[0].vy), math.hypot(a, b), p[1].z - p[0].z
    prev = f(); yrs = 6.0
    while t < yrs * 365.25:
        t += dt; sim.integrate(t); cur = f()
        if prev[0] < 0 <= cur[0] and cur[2] > 0:
            x = prev[0] / (prev[0] - cur[0]); T.append(t - dt + x*dt); B.append((prev[1] + x*(cur[1]-prev[1])) / (R.RSUM*R.RSUN))
        prev = cur
    T, B = np.array(T)/365.25, np.array(B)
    best = 0
    for t0 in np.arange(0, yrs - R.WIN, 0.5):
        m = (T >= t0) & (T < t0 + R.WIN)
        if m.sum() > 10: best = max(best, abs(np.polyfit(T[m], B[m], 1)[0]))
    return best

if __name__ == '__main__':
    m3 = float(sys.argv[1]) if len(sys.argv) > 1 else 0.23
    res = []
    for inc_in, dn, w_out, M_out in itertools.product((84, 90, 96), (0, 60, 120, 180), (0.3, 2.0), (0.0, 2.5)):
        r = run(m3, inc_in, dn, w_out, M_out); res.append(r)
        print(f"m3 {m3} inc_in {inc_in} node {dn} w_out {w_out} M_out {M_out}: max|db/dt| {r:.3f}/yr", flush=True)
    print(f"ALL: max {max(res):.3f}/yr, median {np.median(res):.3f}/yr over {len(res)} configurations")
