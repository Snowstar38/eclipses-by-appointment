"""Eclipse timing (O - C) survey from the raw eclipse windows kept in the repository.

For every target with a raw-windows.csv (normalised raw SAP flux around each predicted
primary) and a measurements.json (ephemeris) beside it:
  1. fold all windows on the measured ephemeris and build an empirical eclipse template
     (median in phase bins, linearly interpolated);
  2. fit each event's time shift, depth scale and a linear baseline by least squares on a
     shift grid refined by a parabola; the 1-sigma error comes from the chi-square curvature
     with the residual scatter of that event;
  3. refit a linear ephemeris, rebuild the template once and repeat;
  4. fit linear and quadratic ephemerides to the event times and report reduced chi-square,
     the quadratic term's significance and the per-sector mean residuals.
Writes etv-events.csv (one row per event) and etv-summary.csv (one row per target).
Usage: python3 reviews/duet-findings/timing/etv_survey.py   (from the repository root)
"""
import json, os, subprocess, sys
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
files = subprocess.run(['git', 'ls-files', '*raw-windows.csv'], capture_output=True, text=True).stdout.split()

def template(ph, f, w):
    """median flux in phase bins of width ~w/8 across +-1.5 w; returns (x, y)"""
    edges = np.linspace(-1.5 * w, 1.5 * w, 49)
    x = 0.5 * (edges[1:] + edges[:-1]); y = np.full(len(x), np.nan)
    for i in range(len(x)):
        m = (ph >= edges[i]) & (ph < edges[i + 1])
        if m.sum() >= 3: y[i] = np.median(f[m])
    ok = np.isfinite(y)
    return x[ok], y[ok]

def fit_event(t, f, tc, tx, ty, w, grid):
    best = []
    for dt in grid:
        model = np.interp(t - tc - dt, tx, ty, left=ty[0], right=ty[-1]) - 1.0
        A = np.vstack([model, np.ones_like(t), t - tc]).T
        c, res, *_ = np.linalg.lstsq(A, f, rcond=None)
        r = f - A @ c
        best.append((np.sum(r * r), c[0]))
    chi = np.array([b[0] for b in best]); i = int(np.argmin(chi))
    if i == 0 or i == len(grid) - 1: return None
    y0, y1, y2 = chi[i - 1], chi[i], chi[i + 1]; h = grid[1] - grid[0]
    curv = (y0 - 2 * y1 + y2) / h**2
    if curv <= 0: return None
    dt = grid[i] + 0.5 * h * (y0 - y2) / (y0 - 2 * y1 + y2)
    s2 = y1 / max(len(t) - 4, 1)                      # residual variance
    err = np.sqrt(2 * s2 / curv)                      # delta chi2 = 1 with chi2 = SSR / s2
    return dt, err, best[i][1], np.sqrt(s2)

seen = {}
for f in files:
    tic = os.path.basename(os.path.dirname(f))
    mj = os.path.join(os.path.dirname(f), 'measurements.json')
    if not os.path.exists(mj): continue
    n = sum(1 for _ in open(f))
    if tic not in seen or n > seen[tic][1]: seen[tic] = (f, n, mj)

ev_rows, sm_rows = [], []
for tic, (f, _, mj) in sorted(seen.items()):
    m = json.load(open(mj)); d = pd.read_csv(f).dropna(subset=['btjd', 'normalized_raw_sap'])
    P = m.get('period_days'); T0 = m.get('primary_epoch_btjd'); w = m.get('search_duration_days') or 0.1
    durs = [e.get('duration_days') for e in m.get('events', []) if e.get('duration_days')]
    if durs: w = float(np.median(durs))
    if not (P and T0) or d.cycle.nunique() < 4: continue
    T0 = T0 - m.get('epoch_cycle', 0) * P
    times = None
    for it in range(2):
        ph = ((d.btjd - T0) / P + 0.5) % 1 - 0.5; ph = ph * P
        tx, ty = template(ph.values, d.normalized_raw_sap.values, w)
        if len(tx) < 10 or ty.min() > 0.9995: break
        grid = np.linspace(-0.3 * w, 0.3 * w, 61)
        rows = []
        for (sec, cyc), g in d.groupby(['sector', 'cycle']):
            tc = T0 + np.round((g.btjd.mean() - T0) / P) * P
            core = np.abs(g.btjd - tc) < 0.6 * w
            if core.sum() < 3 or len(g) < 10: continue
            r = fit_event(g.btjd.values, g.normalized_raw_sap.values, tc, tx, ty, w, grid)
            if r is None: continue
            rows.append(dict(tic=tic, sector=sec, cycle=int(round((tc - T0) / P)), t_mid=tc + r[0], err_d=r[1], depth_scale=r[2], rms=r[3], n=len(g),
                             cadence_min=round(float(np.median(np.diff(np.sort(g.btjd.values)))) * 1440, 2)))
        if len(rows) < 4: break
        e = pd.DataFrame(rows)
        good = (e.err_d < 0.1 * w) & (e.depth_scale > 0.5) & (e.depth_scale < 1.5)
        e = e[good]
        if len(e) < 4: break
        W = 1 / e.err_d**2
        A = np.vstack([np.ones(len(e)), e.cycle]).T
        c = np.linalg.solve(A.T @ (A * W.values[:, None]), A.T @ (W * e.t_mid))
        T0, P = c[0], c[1]; times = e
    if times is None: continue
    e = times.copy(); W = 1 / e.err_d**2; x = e.cycle.values.astype(float)
    def wfit(deg):
        A = np.vander(x, deg + 1, increasing=True)
        C = np.linalg.inv(A.T @ (A * W.values[:, None])); c = C @ (A.T @ (W * e.t_mid))
        r = e.t_mid - A @ c; return c, C, r, float(np.sum(W * r * r))
    c1, C1, r1, chi1 = wfit(1); c2, C2, r2, chi2 = wfit(2)
    e['oc_min'] = r1 * 1440; e['err_min'] = e.err_d * 1440
    ev_rows.append(e)
    span = (x.max() - x.min()) * P
    sec_mean = e.groupby('sector').apply(lambda g: np.average(g.oc_min, weights=1 / g.err_min**2), include_groups=False)
    sm_rows.append(dict(tic=tic, P_d=round(P, 8), P_err_d=float(np.sqrt(C1[1, 1])), n_events=len(e), n_sectors=e.sector.nunique(),
        span_d=round(span, 1), median_err_min=round(float(e.err_min.median()), 2), chi2r_lin=round(chi1 / max(len(e) - 2, 1), 2),
        dchi2_quad=round(chi1 - chi2, 1), quad_sigma=round(c2[2] / np.sqrt(C2[2, 2]), 1),
        quad_amp_min=round(abs(c2[2]) * ((x.max() - x.min()) / 2)**2 * 1440, 2),
        sector_oc_range_min=round(float(sec_mean.max() - sec_mean.min()), 2) if len(sec_mean) > 1 else 0.0,
        source=f))
    print(tic, len(e), sm_rows[-1]['chi2r_lin'], sm_rows[-1]['quad_sigma'], file=sys.stderr)

pd.concat(ev_rows).round(7).to_csv(os.path.join(HERE, 'etv-events.csv'), index=False)
pd.DataFrame(sm_rows).to_csv(os.path.join(HERE, 'etv-summary.csv'), index=False)
print(len(sm_rows), 'targets timed')
