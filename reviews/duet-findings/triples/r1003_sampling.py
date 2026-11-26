"""Does the way run 9c measured the impact parameter inflate its switch-on rates?

Run 9c (r1003_switchon_robust.py) samples the integration every P_in/100 and takes the
impact parameter b as the LINEAR interpolation of the projected separation between the two
samples that bracket each conjunction. Near conjunction the separation is V-shaped,
sqrt(b^2 + (v t)^2), so a linear interpolation overestimates b by up to v*dt/2 (about 0.3
in units of R1 + R2 at P_in/100 for this eccentric 2.88-d orbit), by an amount that depends
on where the samples fall relative to the conjunction. That phase drifts slowly, so the
error drifts too and adds a spurious slope.

This integrates the same 48 configurations as r1003_nbody_numpy.py (RK4, P_in/1500, no GR)
and measures b three ways at every conjunction with M2 in front:
  lin100  : run 9c's estimator, applied to samples every P_in/100 (every 15th step)
  lin1500 : the same estimator on every step (what r1003_nbody_numpy.py reported)
  exact   : the closest approach of the sky-plane relative motion, |r x v| / |v|, from the
            state at the step after the conjunction (exact to second order in dt)
and reports the largest |db/dt| over 2.7-yr windows in 6 yr for each.

usage: python3 r1003_sampling.py m3
"""
import itertools
import sys
import numpy as np
from r1003_nbody_numpy import initial, acc, P_IN, RSUM, RSUN, YEARS, WIN

STEPS, SUB = 1500, 15


def slope(T, B):
    T = np.array(T) / 365.25; B = np.array(B); best = 0.0
    for t0 in np.arange(0, YEARS - WIN, 0.5):
        s = (T >= t0) & (T < t0 + WIN)
        if s.sum() > 10:
            best = max(best, abs(np.polyfit(T[s], B[s], 1)[0]))
    return best


def run(m3):
    cfgs = list(itertools.product((84, 90, 96), (0, 60, 120, 180), (0.3, 2.0), (0.0, 2.5)))
    N = len(cfgs)
    pos = np.zeros((N, 3, 3)); vel = np.zeros((N, 3, 3))
    for k, c in enumerate(cfgs):
        m, pos[k], vel[k] = initial(m3, *c)
    dt = P_IN / STEPS
    nsteps = int(YEARS * 365.25 / dt)
    est = {n: ([[] for _ in range(N)], [[] for _ in range(N)]) for n in ("lin100", "lin1500", "exact")}

    def sky(p, v):
        rx, ry = p[:, 1, 0] - p[:, 0, 0], p[:, 1, 1] - p[:, 0, 1]
        vx, vy = v[:, 1, 0] - v[:, 0, 0], v[:, 1, 1] - v[:, 0, 1]
        return rx * vx + ry * vy, np.hypot(rx, ry), p[:, 1, 2] - p[:, 0, 2], np.abs(rx * vy - ry * vx) / np.hypot(vx, vy)

    def record(name, prev, cur, t, h, exact=False):
        hit = np.nonzero((prev[0] < 0) & (cur[0] >= 0) & (cur[2] > 0))[0]
        T, B = est[name]
        for k in hit:
            x = prev[0][k] / (prev[0][k] - cur[0][k])
            T[k].append(t - h + x * h)
            b = cur[3][k] if exact else prev[1][k] + x * (cur[1][k] - prev[1][k])
            B[k].append(b / (RSUM * RSUN))

    prev = sky(pos, vel); prev100 = prev; t = 0.0
    for i in range(1, nsteps + 1):
        k1v = acc(pos, m); k1x = vel
        k2v = acc(pos + 0.5 * dt * k1x, m); k2x = vel + 0.5 * dt * k1v
        k3v = acc(pos + 0.5 * dt * k2x, m); k3x = vel + 0.5 * dt * k2v
        k4v = acc(pos + dt * k3x, m); k4x = vel + dt * k3v
        pos = pos + dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x)
        vel = vel + dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)
        t += dt
        cur = sky(pos, vel)
        record("lin1500", prev, cur, t, dt)
        record("exact", prev, cur, t, dt, exact=True)
        if i % SUB == 0:
            record("lin100", prev100, cur, t, dt * SUB)
            prev100 = cur
        prev = cur
    out = {}
    print(f"m3 {m3}: largest |db/dt| per yr (2.7-yr windows, 6 yr), three estimators of b")
    print("inc_in node w_out M_out   lin100  lin1500   exact   b_exact range")
    for name in est:
        out[name] = [slope(est[name][0][k], est[name][1][k]) for k in range(N)]
    for k, c in enumerate(cfgs):
        bx = est["exact"][1][k]
        print(f"{c[0]:6d} {c[1]:4d} {c[2]:5.1f} {c[3]:5.1f}   {out['lin100'][k]:6.3f}  {out['lin1500'][k]:6.3f}  {out['exact'][k]:6.3f}   {min(bx):.2f}-{max(bx):.2f}")
    for name in est:
        print(f"ALL {name:8s}: max {max(out[name]):.3f}/yr, median {np.median(out[name]):.3f}/yr")
    return out


if __name__ == "__main__":
    run(float(sys.argv[1]))
