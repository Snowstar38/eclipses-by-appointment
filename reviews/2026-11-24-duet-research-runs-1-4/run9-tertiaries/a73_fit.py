"""Run 9a (Duet): fit A73's secondary-eclipse phase history with an N-body triple.

Data: Fable's per-eclipse secondary phases through TESS s86 (a73-secondary-phases.csv,
house timing table, 2026-11-25): phase = (t_sec - t_prim,prev)/17.538 d.
Model: rebound IAS15, star 1 (1.2 Msun) + star 2 (1.0 Msun) on the 17.54-d orbit,
tertiary on Gaia's 124.725-d orbit at inclination 90.95 deg (Gaia DR3 2290881958791909248).
Free: e_in, omega_in, m3, omega_out, M_out (outer phase at BTJD 1750), mutual inclination
i_mut and its orientation phi (inner orbit: inc = 90.95 + i_mut cos phi, node = i_mut sin phi).
e_out is held fixed per fit, so the script returns the best chi^2 for each e_out.
Each secondary eclipse in the model is matched to the observed one by time.
With JOINT=1 the secondary depths are fitted too (uniform discs R1 = 1.4, R2 = 1.0 Rsun,
free depth scale), so the model's impact-parameter history must follow the fade.
Usage: [JOINT=1] [M3_RANGE=lo,hi] python3 a73_fit.py a73-secondary-phases.csv e_out [maxiter] [seed]
(run 9 used maxiter 50, seed 11; M3_RANGE=0.85,0.95 for the Gaia-mass fits)
"""
import math, sys, csv, json, os
import numpy as np
import rebound
from scipy.optimize import differential_evolution

C = 173.1446            # AU/day
P_IN, P_OUT = 17.538, 124.72477
M1, M2 = (float(x) for x in __import__('os').environ.get('M_IN', '1.2,1.0').split(','))   # inner masses (Msun); M_IN=1.4,1.2 to test
I_OUT = math.radians(90.95)
T_START = 1750.0
T_PRIM0 = 1774.8831 - 0.5037 * 17.538   # primary before the first observed secondary
SIGMA = 0.002           # model/timing floor on phase (35 min)

def load(path):
    r = list(csv.DictReader(open(path)))
    return np.array([float(x['t0_btjd']) for x in r]), np.array([float(x['phase']) for x in r]), np.array([float(x['depth']) for x in r])

def build(e_in, w_in, m3, e_out, w_out, M_out, imut, phi):
    sim = rebound.Simulation(); sim.units = ('day', 'AU', 'Msun'); sim.integrator = 'ias15'
    sim.add(m=M1)
    inc_in = I_OUT + math.radians(imut) * math.cos(phi)
    node_in = math.radians(imut) * math.sin(phi)
    f = math.pi / 2 - w_in                                  # star 2 in front (primary) at omega + f = 90 deg
    E = 2 * math.atan2(math.sqrt(1 - e_in) * math.sin(f / 2), math.sqrt(1 + e_in) * math.cos(f / 2))
    M_conj = E - e_in * math.sin(E)
    M0 = M_conj - 2 * math.pi * (T_PRIM0 - T_START) / P_IN   # first primary at T_PRIM0
    sim.add(m=M2, P=P_IN, e=e_in, inc=inc_in, Omega=node_in, omega=w_in, M=M0)
    sim.add(m=m3, P=P_OUT, e=e_out, inc=I_OUT, Omega=0.0, omega=w_out, M=M_out)
    sim.move_to_com()
    return sim

def conjunctions(sim, t_end, steps=60):
    """Return lists of (time, kind, sky separation in AU); kind 1 = star 2 in front (primary)."""
    p = sim.particles; dt = P_IN / steps; t = 0.0; out = []
    def f():
        rx, ry = p[1].x - p[0].x, p[1].y - p[0].y
        vx, vy = p[1].vx - p[0].vx, p[1].vy - p[0].vy
        # sky separation at closest approach, from the straight-line approximation (exact near conjunction)
        return rx * vx + ry * vy, abs(rx * vy - ry * vx) / math.hypot(vx, vy), p[1].z - p[0].z
    hist = [f()]; ts = [0.0]
    while t < t_end:
        t += dt; sim.integrate(t); cur = f(); hist.append(cur); ts.append(t)
        prev = hist[-2]
        if prev[0] < 0 <= cur[0]:
            x = prev[0] / (prev[0] - cur[0]); tm = t - dt + x * dt
            sep = prev[1] + x * (cur[1] - prev[1])   # perpendicular distance: smooth, so interpolation is fine
            zc = (p[0].m * p[0].z + p[1].m * p[1].z) / (p[0].m + p[1].m)
            out.append((tm - zc / C, 1 if cur[2] > 0 else 0, sep))
    return out

def model_phases(params, e_out, t_obs, span=None):
    e_in, w_in, m3, w_out, M_out, imut, phi = params
    sim = build(e_in, w_in, m3, e_out, w_out, M_out, imut, phi)
    span = span or (t_obs.max() - T_START + 40)
    cj = conjunctions(sim, span)
    prim = [(t + T_START, s) for t, k, s in cj if k == 1]
    sec = [(t + T_START, s) for t, k, s in cj if k == 0]
    return prim, sec

def phases_at(prim, sec, t_obs):
    """Match by cycle number, not by time: the model's mean inner period can differ slightly."""
    pt = np.array([t for t, _ in prim]); st = np.array([t for t, _ in sec])
    ph = np.full(len(t_obs), np.nan); bsec = np.full(len(t_obs), np.nan)
    p0 = int(np.argmin(abs(pt - T_PRIM0)))
    sec_after = np.nonzero(st > pt[p0])[0]
    for i, to in enumerate(t_obs):
        n = int(round((to - T_PRIM0) / P_IN - 0.5))
        if n >= len(sec_after): continue
        j = sec_after[n]
        k = np.searchsorted(pt, st[j]) - 1
        ph[i] = (st[j] - pt[k]) / P_IN; bsec[i] = sec[j][1]
    return ph, bsec

RSUN = 0.00465047
R1, R2 = 1.4, 1.0        # assumed radii (Rsun), as in run 7
SIG_DEPTH = 0.005        # absolute floor on secondary depth (Fable's trapezoid fits, raw QLP)
JOINT = os.environ.get('JOINT', '0') == '1'

def covered_fraction(d):
    """fraction of star 2's (uniform) disc hidden behind star 1 at sky separation d (Rsun)"""
    d = np.asarray(d, float); out = np.zeros_like(d)
    out[d <= R1 - R2] = 1.0
    m = (d > R1 - R2) & (d < R1 + R2); x = d[m]
    a1 = R1**2 * np.arccos(np.clip((x**2 + R1**2 - R2**2) / (2 * x * R1), -1, 1))
    a2 = R2**2 * np.arccos(np.clip((x**2 + R2**2 - R1**2) / (2 * x * R2), -1, 1))
    a3 = 0.5 * np.sqrt(np.clip((-x + R1 + R2) * (x + R1 - R2) * (x - R1 + R2) * (x + R1 + R2), 0, None))
    out[m] = (a1 + a2 - a3) / (math.pi * R2**2)
    return out

def depth_term(bsec, dep_obs):
    """best scale D0 (linear least squares) and chi^2 of secondary depths"""
    f = covered_fraction(bsec / RSUN)
    if f.sum() == 0: return 1e6, 0.0
    D0 = float((f * dep_obs).sum() / (f * f).sum())
    return float((((D0 * f - dep_obs) / SIG_DEPTH) ** 2).sum()), D0

def chi2(params, e_out, t_obs, ph_obs, dep_obs=None):
    try:
        prim, sec = model_phases(params, e_out, t_obs)
        ph, bsec = phases_at(prim, sec, t_obs)
    except Exception:
        return 1e6
    if np.any(np.isnan(ph)): return 1e6
    c = float(np.sum(((ph - ph_obs) / SIGMA) ** 2))
    if dep_obs is not None:
        c += depth_term(bsec, dep_obs)[0]
    return c

M3R = tuple(float(x) for x in os.environ.get('M3_RANGE', '0.1,1.0').split(','))
BOUNDS = [(0.0, 0.15), (0, 2 * math.pi), M3R, (0, 2 * math.pi), (0, 2 * math.pi), (0.0, 8.0), (0, 2 * math.pi)]
NAMES = ['e_in', 'omega_in', 'm3', 'omega_out', 'M_out', 'i_mut_deg', 'phi']

if __name__ == '__main__':
    t_obs, ph_obs, dep_obs = load(sys.argv[1]); e_out = float(sys.argv[2])
    maxiter = int(sys.argv[3]) if len(sys.argv) > 3 else 60
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    r = differential_evolution(chi2, BOUNDS, args=(e_out, t_obs, ph_obs, dep_obs if JOINT else None), maxiter=maxiter, popsize=12,
                               seed=seed, tol=1e-6, polish=False, workers=1, updating='immediate')
    res = dict(e_out=e_out, joint=JOINT, m3_range=M3R, chi2=r.fun, n=len(t_obs), params=dict(zip(NAMES, map(float, r.x))), nfev=r.nfev)
    print(json.dumps(res))
