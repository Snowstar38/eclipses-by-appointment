"""Shared helpers for the vetD checks (own code; numpy/astropy only).
Copied unchanged into each vet<TIC> folder."""
import glob, json, os
import numpy as np
from astropy.io import fits

CACHE = '[local path omitted]'


def qlp_files(tic):
    return sorted(glob.glob(os.path.join(CACHE, f'{tic}_s*.fits')))


def load_qlp(fn, allq=True):
    """Raw SAP, all cadences with finite flux. Returns dict of arrays; flux normalised to median of q==0."""
    with fits.open(fn, memmap=False) as h:
        d = h[1].data; cols = d.columns.names
        t = np.array(d['TIME'], float); f = np.array(d['SAP_FLUX'], float); q = np.array(d['QUALITY'], int)
        bk = np.array(d['SAP_BKG'], float) if 'SAP_BKG' in cols else np.full_like(t, np.nan)
        x = np.array(d['SAP_X'], float) if 'SAP_X' in cols else np.full_like(t, np.nan)
        y = np.array(d['SAP_Y'], float) if 'SAP_Y' in cols else np.full_like(t, np.nan)
        sec = int(h[0].header.get('SECTOR', -1))
    ok = np.isfinite(t) & np.isfinite(f) & (f > 0)
    if not allq: ok &= q == 0
    t, f, q, bk, x, y = t[ok], f[ok], q[ok], bk[ok], x[ok], y[ok]
    med = np.median(f[q == 0]) if np.any(q == 0) else np.median(f)
    return dict(t=t, f=f / med, q=q, bkg=bk / med, x=x, y=y, sec=sec, fn=fn)


# ---------------------------------------------------------------- Gaia astrometric orbit -> conjunctions
def corr_matrix(vec, n):
    C = np.eye(n); k = 0
    for j in range(1, n):
        for i in range(j):
            C[i, j] = C[j, i] = vec[k]; k += 1
    return C


def omega_of(A, B, F, G):
    wpO = np.arctan2(B - F, A + G); wmO = np.arctan2(-(B + F), A - G)
    return (wpO + wmO) / 2


def t_of_nu(nu, e, P, T):
    E = 2 * np.arctan(np.sqrt((1 - e) / (1 + e)) * np.tan(nu / 2))
    M = E - e * np.sin(E)
    return T + 389.0 + (M / (2 * np.pi)) * P


def nss_draws(row, n=200000, seed=1, diag=False):
    """MC draws of (A,B,F,G,e,P,T) from the full Gaia covariance (Orbital: 12 params)."""
    keys = ['a_thiele_innes', 'b_thiele_innes', 'f_thiele_innes', 'g_thiele_innes', 'eccentricity', 'period', 't_periastron']
    mu = np.array([float(row[k]) for k in keys]); sig = np.array([float(row[k + '_error']) for k in keys])
    cv = [float(v) for v in str(row['corr_vec']).strip('()[]{}').split(',')]
    npar = int(round((1 + np.sqrt(1 + 8 * len(cv))) / 2))
    C = corr_matrix(cv, npar)[npar - 7:, npar - 7:]
    if diag: C = np.eye(7)
    rng = np.random.default_rng(seed)
    s = rng.multivariate_normal(mu, C * np.outer(sig, sig), n)
    s = s[(s[:, 4] > 0) & (s[:, 4] < 0.95)]
    return mu, s


def conj_series(row, t0, t1, n=200000, diag=False):
    """Predicted conjunction times (both kinds, 'c1' at nu=90-w, 'c2' at nu=270-w; which star is in front
    is ambiguous for an astrometric orbit) in [t0, t1], with MC median and 1-sigma."""
    mu, s = nss_draws(row, n, diag=diag)
    A, B, F, G, e, P, T = s.T
    w0 = omega_of(*mu[:4]); w = omega_of(A, B, F, G)
    w = w0 + ((w - w0 + np.pi / 2) % np.pi) - np.pi / 2
    out = []
    for name, nu in (('c1', np.pi / 2 - w), ('c2', 1.5 * np.pi - w)):
        tc = t_of_nu(nu, e, P, T)
        tcn = t_of_nu(np.pi / 2 - w0 if name == 'c1' else 1.5 * np.pi - w0, mu[4], mu[5], mu[6])
        tc = tcn + ((tc - tcn + P / 2) % P) - P / 2   # no 2pi jumps across apastron
        for k in range(int(np.floor((t0 - tcn) / mu[5])) - 1, int(np.ceil((t1 - tcn) / mu[5])) + 2):
            x = tc + k * P
            m = np.median(x)
            if t0 - 30 <= m <= t1 + 30:
                out.append((name, k, m, np.std(x), np.percentile(x, 16), np.percentile(x, 84)))
    out.sort(key=lambda r: r[2])
    return out, np.degrees(w0) % 360, mu


# ---------------------------------------------------------------- trapezoid fitting
def trap(t, t0, dep, T14, T12):
    T12 = np.clip(T12, 1e-4, T14 / 2)
    x = np.abs(t - t0); m = np.zeros_like(t)
    full = x <= T14 / 2 - T12
    ing = (x > T14 / 2 - T12) & (x < T14 / 2)
    m[full] = dep
    m[ing] = dep * (T14 / 2 - x[ing]) / T12
    return 1 - m


def model(p, t, tref, npoly=2):
    t0, dep, T14, T12 = p[:4]; c = p[4:]
    base = np.polyval(c[::-1], t - tref) if len(c) else 1.0
    return trap(t, t0, dep, T14, T12) * base


def nm(fun, x0, step, it=4000, tol=1e-10):
    """Plain Nelder-Mead."""
    n = len(x0); X = [np.array(x0, float)]
    for i in range(n):
        x = np.array(x0, float); x[i] += step[i]; X.append(x)
    Fv = [fun(x) for x in X]
    for _ in range(it):
        o = np.argsort(Fv); X = [X[i] for i in o]; Fv = [Fv[i] for i in o]
        if abs(Fv[-1] - Fv[0]) < tol * (1 + abs(Fv[0])): break
        c = np.mean(X[:-1], 0); xr = c + (c - X[-1]); fr = fun(xr)
        if fr < Fv[0]:
            xe = c + 2 * (c - X[-1]); fe = fun(xe)
            X[-1], Fv[-1] = (xe, fe) if fe < fr else (xr, fr)
        elif fr < Fv[-2]:
            X[-1], Fv[-1] = xr, fr
        else:
            xc = c + 0.5 * (X[-1] - c); fc = fun(xc)
            if fc < Fv[-1]: X[-1], Fv[-1] = xc, fc
            else:
                X = [X[0] + 0.5 * (x - X[0]) for x in X]; Fv = [fun(x) for x in X]
    i = int(np.argmin(Fv)); return X[i], Fv[i]


def fit_trap(t, f, t0, dep, T14, T12, npoly=2, fix_t0=False):
    tref = t0
    p0 = [t0, dep, T14, T12, 1.0] + [0.0] * npoly
    def chi(p):
        if p[1] < 0 or p[2] <= 0 or p[3] <= 0 or p[3] > p[2] / 2: return 1e30
        if fix_t0: p = np.r_[t0, p[1:]]
        return np.sum((f - model(p, t, tref)) ** 2)
    step = [0.02, 0.02, 0.05, 0.02, 0.002] + [0.001] * npoly
    best, c2 = nm(chi, p0, step)
    for _ in range(3):
        best, c2 = nm(chi, best, [s / 3 for s in step])
    if fix_t0: best[0] = t0
    res = f - model(best, t, tref); sig = np.std(res)
    return best, c2, sig, tref


def t0_error(t, f, best, tref, sig, half=0.05, n=81):
    """1-sigma t0 error from profile chi2 (shape and baseline refit lightly via linear baseline scale only),
    inflated by a red-noise beta from binned residuals."""
    ts = best[0] + np.linspace(-half, half, n); c2 = []
    for tt in ts:
        p = best.copy(); p[0] = tt
        m = model(p, t, tref); a = np.sum(f * m) / np.sum(m * m)
        c2.append(np.sum((f - a * m) ** 2) / sig ** 2)
    c2 = np.array(c2); c2 -= c2.min(); ok = ts[c2 <= 1]
    e = (ok.max() - ok.min()) / 2 if len(ok) > 1 else (ts[1] - ts[0])
    return e
