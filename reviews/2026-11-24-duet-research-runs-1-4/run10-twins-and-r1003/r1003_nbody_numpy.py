"""Run 10b (Duet): R1003's switch-on rate for both Gaia tertiary solutions, NumPy only.

A plain-NumPy re-implementation of run 9c's r1003_switchon_robust.py (which needs rebound
and reboundx): same masses, orbits, element conventions (Jacobi, REBOUND's angles), the
same 48 configurations and the same measurement (the projected separation at each inner
conjunction with M2 in front, in units of R1 + R2, and the largest |slope| over any
2.7-yr window in 6 yr). Differences: a fixed-step fourth-order Runge-Kutta integrator
(P_in/1500) instead of IAS15, and no general relativity (its apsidal period at 2.88 d is
~5,000 yr). All configurations of one tertiary mass are integrated together as arrays.

usage: python3 r1003_nbody_numpy.py m3 [steps_per_inner_orbit]
"""
import itertools
import math
import sys
import numpy as np

G = 0.01720209895 ** 2          # AU^3 / (Msun day^2), REBOUND's value for these units
RSUN = 0.00465047
P_IN, E_IN, M1, M2, RSUM = 2.8787113, 0.49, 1.1, 0.9, 2.0
P_OUT, E_OUT, I_OUT = 206.587, 0.491, math.radians(70.3)
YEARS, WIN = 6.0, 2.7


def kepler_E(M, e):
    E = M if e < 0.8 else math.pi
    for _ in range(50):
        E -= (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
    return E


def orbit_to_xv(mu, P, e, inc, Om, om, M):
    a = (mu * P ** 2 / (4 * math.pi ** 2)) ** (1 / 3)
    E = kepler_E(M, e)
    f = 2 * math.atan2(math.sqrt(1 + e) * math.sin(E / 2), math.sqrt(1 - e) * math.cos(E / 2))
    r = a * (1 - e * math.cos(E))
    vfac = math.sqrt(mu / (a * (1 - e * e)))
    cO, sO, ci, si = math.cos(Om), math.sin(Om), math.cos(inc), math.sin(inc)
    cwf, swf = math.cos(om + f), math.sin(om + f)
    x = r * (cO * cwf - sO * swf * ci)
    y = r * (sO * cwf + cO * swf * ci)
    z = r * swf * si
    # REBOUND's velocity formulae
    cw, sw = math.cos(om), math.sin(om)
    cf, sf = math.cos(f), math.sin(f)
    vx = vfac * ((e + cf) * (-ci * cw * sO - cO * sw) - sf * (cw * cO - ci * sO * sw))
    vy = vfac * ((e + cf) * (ci * cw * cO - sO * sw) - sf * (cw * sO + ci * cO * sw))
    vz = vfac * ((e + cf) * cw * si - sf * si * sw)
    return np.array([x, y, z]), np.array([vx, vy, vz])


def initial(m3, inc_in, dn, w_out, M_out):
    m = np.array([M1, M2, m3])
    pos = np.zeros((3, 3)); vel = np.zeros((3, 3))
    r1, v1 = orbit_to_xv(G * (M1 + M2), P_IN, E_IN, math.radians(inc_in), math.radians(dn), 0.6, 0.0)
    pos[1], vel[1] = r1, v1
    com_r = (M2 * r1) / (M1 + M2); com_v = (M2 * v1) / (M1 + M2)
    r2, v2 = orbit_to_xv(G * (M1 + M2 + m3), P_OUT, E_OUT, I_OUT, 0.0, w_out, M_out)
    pos[2], vel[2] = com_r + r2, com_v + v2
    cm = (m[:, None] * pos).sum(0) / m.sum(); cv = (m[:, None] * vel).sum(0) / m.sum()
    return m, pos - cm, vel - cv


def acc(pos, m):
    # pos: (N, 3, 3)
    d = pos[:, None, :, :] - pos[:, :, None, :]          # (N, i, j, 3): r_j - r_i
    r2 = (d ** 2).sum(-1)
    np.einsum("nii->ni", r2)[:] = 1.0
    inv3 = r2 ** -1.5
    np.einsum("nii->ni", inv3)[:] = 0.0
    return G * np.einsum("nij,nijk,j->nik", inv3, d, m)


def run(m3, steps=1500):
    cfgs = list(itertools.product((84, 90, 96), (0, 60, 120, 180), (0.3, 2.0), (0.0, 2.5)))
    N = len(cfgs)
    pos = np.zeros((N, 3, 3)); vel = np.zeros((N, 3, 3))
    for k, c in enumerate(cfgs):
        m, pos[k], vel[k] = initial(m3, *c)
    dt = P_IN / steps
    nsteps = int(YEARS * 365.25 / dt)
    T = [[] for _ in range(N)]; B = [[] for _ in range(N)]

    def f_sky(p, v):
        rx, ry = p[:, 1, 0] - p[:, 0, 0], p[:, 1, 1] - p[:, 0, 1]
        return (rx * (v[:, 1, 0] - v[:, 0, 0]) + ry * (v[:, 1, 1] - v[:, 0, 1]),
                np.hypot(rx, ry), p[:, 1, 2] - p[:, 0, 2])

    prev = f_sky(pos, vel); t = 0.0
    for _ in range(nsteps):
        k1v = acc(pos, m); k1x = vel
        k2v = acc(pos + 0.5 * dt * k1x, m); k2x = vel + 0.5 * dt * k1v
        k3v = acc(pos + 0.5 * dt * k2x, m); k3x = vel + 0.5 * dt * k2v
        k4v = acc(pos + dt * k3x, m); k4x = vel + dt * k3v
        pos = pos + dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x)
        vel = vel + dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)
        t += dt
        cur = f_sky(pos, vel)
        hit = np.nonzero((prev[0] < 0) & (cur[0] >= 0) & (cur[2] > 0))[0]
        for k in hit:
            x = prev[0][k] / (prev[0][k] - cur[0][k])
            T[k].append(t - dt + x * dt)
            B[k].append((prev[1][k] + x * (cur[1][k] - prev[1][k])) / (RSUM * RSUN))
        prev = cur
    res = []
    for k, c in enumerate(cfgs):
        Tk, Bk = np.array(T[k]) / 365.25, np.array(B[k])
        best = 0.0
        for t0 in np.arange(0, YEARS - WIN, 0.5):
            sel = (Tk >= t0) & (Tk < t0 + WIN)
            if sel.sum() > 10:
                best = max(best, abs(np.polyfit(Tk[sel], Bk[sel], 1)[0]))
        res.append(best)
        print(f"m3 {m3} inc_in {c[0]} node {c[1]} w_out {c[2]} M_out {c[3]}: max|db/dt| {best:.3f}/yr", flush=True)
    print(f"ALL: max {max(res):.3f}/yr, median {np.median(res):.3f}/yr over {len(res)} configurations")
    return res


if __name__ == "__main__":
    run(float(sys.argv[1]), int(sys.argv[2]) if len(sys.argv) > 2 else 1500)
