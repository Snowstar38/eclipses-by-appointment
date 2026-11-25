"""Run 10d (Duet): fill in the node offsets run 9c's 48 configurations skipped.

Run 9c sampled the inner orbit's node offset at 0, 60, 120 and 180 deg; with i_in = 90 deg
and Gaia's i_out = 70.3 deg those are mutual inclinations of about 20, 62, 118 and 160 deg,
which straddle the ~40-50 deg where a tilted orbit's eclipses change fastest. This scans
node offsets 0-180 deg in 10-deg steps (i_in 84, 90, 96; the same four outer-orbit
phases), RK4 at P_in/1500 as r1003_nbody_numpy.py, and measures b by the exact
closest-approach estimator of r1003_sampling.py. Prints the largest |db/dt| (2.7-yr
windows, 6 yr) for each node offset and overall.

usage: python3 r1003_node_scan.py m3
"""
import itertools
import math
import sys
import numpy as np
from r1003_nbody_numpy import initial, acc, P_IN, RSUM, RSUN, YEARS, I_OUT
from r1003_sampling import slope

STEPS = 1500
NODES = list(range(0, 181, 10))


def run(m3):
    cfgs = list(itertools.product((84, 90, 96), NODES, (0.3, 2.0), (0.0, 2.5)))
    N = len(cfgs)
    pos = np.zeros((N, 3, 3)); vel = np.zeros((N, 3, 3))
    for k, c in enumerate(cfgs):
        m, pos[k], vel[k] = initial(m3, *c)
    dt = P_IN / STEPS; nsteps = int(YEARS * 365.25 / dt)
    T = [[] for _ in range(N)]; B = [[] for _ in range(N)]

    def sky(p, v):
        rx, ry = p[:, 1, 0] - p[:, 0, 0], p[:, 1, 1] - p[:, 0, 1]
        vx, vy = v[:, 1, 0] - v[:, 0, 0], v[:, 1, 1] - v[:, 0, 1]
        return rx * vx + ry * vy, p[:, 1, 2] - p[:, 0, 2], np.abs(rx * vy - ry * vx) / np.hypot(vx, vy)

    prev = sky(pos, vel); t = 0.0
    for _ in range(nsteps):
        k1v = acc(pos, m); k1x = vel
        k2v = acc(pos + 0.5 * dt * k1x, m); k2x = vel + 0.5 * dt * k1v
        k3v = acc(pos + 0.5 * dt * k2x, m); k3x = vel + 0.5 * dt * k2v
        k4v = acc(pos + dt * k3x, m); k4x = vel + dt * k3v
        pos = pos + dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x)
        vel = vel + dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)
        t += dt
        cur = sky(pos, vel)
        for k in np.nonzero((prev[0] < 0) & (cur[0] >= 0) & (cur[1] > 0))[0]:
            x = prev[0][k] / (prev[0][k] - cur[0][k])
            T[k].append(t - dt + x * dt); B[k].append(cur[2][k] / (RSUM * RSUN))
        prev = cur
    rate = np.array([slope(T[k], B[k]) for k in range(N)])
    print(f"m3 {m3}: largest |db/dt| per yr by node offset (12 configurations each: i_in 84/90/96 x outer phases)")
    print("node  i_mut(i_in=90)   max    median")
    for dn in NODES:
        s = np.array([c[1] == dn for c in cfgs])
        imut = math.degrees(math.acos(math.sin(I_OUT) * math.cos(math.radians(dn))))
        print(f"{dn:4d}     {imut:5.1f}       {rate[s].max():.3f}  {np.median(rate[s]):.3f}")
    k = int(rate.argmax())
    print(f"ALL {N} configurations: max {rate.max():.3f}/yr at {cfgs[k]}, median {np.median(rate):.3f}/yr")


if __name__ == "__main__":
    run(float(sys.argv[1]))
