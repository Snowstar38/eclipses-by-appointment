"""Fit machinery for vet438089101 (own code). Variable projection: nonlinear (dtp, [P], e, w, i) by least_squares;
linear (per-segment polynomial baselines, tide S, beaming Bm) by weighted linear least squares at every step.
Data are 0.02-d bins per sector, error = the sector's white (point-to-point) scatter / sqrt(n_in_bin)."""
import numpy as np
from scipy.optimize import least_squares
from lib import true_anom, kepler_E

def segments(t, gap=0.5):
    br = np.where(np.diff(t) > gap)[0]
    return np.split(np.arange(len(t)), br + 1)

def bin_series(t, f, sec, binw=0.02, exptime=None):
    """Bin per sector. Returns dict of arrays: t, y, err, n, sec, seg, texp (bin width or exposure, for supersampling)."""
    T, Y, E, N, S, G, X = [], [], [], [], [], [], []
    segk = 0
    for s in np.unique(sec):
        m = sec == s
        ts, fs = t[m], f[m]
        white = np.std(np.diff(fs)) / np.sqrt(2)
        for sg in segments(ts):
            tt, ff = ts[sg], fs[sg]
            k = np.floor((tt - tt[0]) / binw).astype(int)
            for j in np.unique(k):
                mm = k == j
                T.append(tt[mm].mean()); Y.append(ff[mm].mean()); N.append(mm.sum())
                E.append(white / np.sqrt(mm.sum())); S.append(s); G.append(segk)
                X.append(max(binw if mm.sum() > 1 else 0.0, (exptime or {}).get(int(s), 0.0)))
            segk += 1
    return {k: np.array(v) for k, v in zip(("t", "y", "err", "n", "sec", "seg", "texp"), (T, Y, E, N, S, G, X))}

def design_baseline(B):
    """Per-segment Legendre-like polynomial columns, degree min(3, dur // 4)."""
    cols = []
    for j in np.unique(B["seg"]):
        m = B["seg"] == j
        tt = B["t"][m]; dur = tt.max() - tt.min(); deg = int(min(3, dur // 4))
        x = np.zeros(len(B["t"])); x[m] = (tt - tt.mean()) / max(dur, 1e-3) * 2
        for d in range(deg + 1):
            c = np.zeros(len(B["t"])); c[m] = x[m] ** d; cols.append(c)
    return np.array(cols).T

def design_linear_passage(B, tp, P):
    """Alternative baseline: linear per orbit passage (window = periastron +- P/2), as in Fable 5.1's persec check."""
    cyc = np.round((B["t"] - tp) / P).astype(int)
    key = B["seg"] * 100000 + cyc
    cols = []
    for k in np.unique(key):
        m = key == k
        x = np.zeros(len(B["t"])); x[m] = B["t"][m] - B["t"][m].mean()
        c0 = np.zeros(len(B["t"])); c0[m] = 1; cols += [c0, x]
    return np.array(cols).T

NSUB = 5
def _sub(B):
    off = (np.arange(NSUB) + 0.5) / NSUB - 0.5
    return (B["t"][:, None] + B["texp"][:, None] * off[None, :])

def shapes(B, tp, P, e, w, inc):
    ts = _sub(B)
    nu = true_anom(ts.ravel(), tp, P, e).reshape(ts.shape)
    R = (1 - e * e) / (1 + e * np.cos(nu))
    tid = ((1 - 3 * np.sin(inc) ** 2 * np.sin(nu + w) ** 2) / R ** 3).mean(1)
    bm = (-(np.cos(nu + w) + e * np.cos(w))).mean(1)
    return tid, bm

class Model:
    """mode: 'tide' or 'beam'; pfree: fit P; baseline: 'seg' or 'passage'."""
    def __init__(self, B, tp0, P0, mode="beam", pfree=False, baseline="seg", extra=None):
        self.B, self.tp0, self.P0, self.mode, self.pfree, self.baseline = B, tp0, P0, mode, pfree, baseline
        self.Xb = design_baseline(B) if baseline == "seg" else None
        self.extra = extra            # optional extra linear columns (e.g. prewhitening sinusoids)
        self.w8 = 1 / B["err"]

    def unpack(self, p):
        if self.pfree:
            dtp, dP, e, w, inc = p; P = self.P0 + dP
        else:
            dtp, e, w, inc = p; P = self.P0
        return self.tp0 + dtp, P, e, w, inc

    def solve(self, p, full=False):
        tp, P, e, w, inc = self.unpack(p)
        tid, bm = shapes(self.B, tp, P, e, w, inc)
        Xb = self.Xb if self.baseline == "seg" else design_linear_passage(self.B, tp, P)
        cols = [tid] + ([bm] if self.mode == "beam" else [])
        X = np.column_stack(cols + [Xb] + ([self.extra] if self.extra is not None else []))
        A = X * self.w8[:, None]; b = self.B["y"] * self.w8
        coef, *_ = np.linalg.lstsq(A, b, rcond=None)
        r = b - A @ coef
        pen = 0.0
        if coef[0] < 0: pen += 1e3 * (1 + abs(coef[0]) * 1e4)      # S > 0 enforced
        if full:
            cov = np.linalg.pinv(A.T @ A)
            return r, coef, cov, X
        return np.append(r, pen)

    def fit(self, p0, bounds=None):
        if bounds is None:
            lo = [-1.5, 0.0, -10.0, 0.0]; hi = [1.5, 0.8, 10.0, np.pi / 2]
            if self.pfree: lo.insert(1, -0.01); hi.insert(1, 0.01)
            bounds = (lo, hi)
        best = None
        starts = [p0] if not isinstance(p0[0], (list, tuple, np.ndarray)) else p0
        for s in starts:
            r = least_squares(self.solve, s, bounds=bounds, x_scale="jac", diff_step=1e-4)
            if best is None or r.cost < best.cost: best = r
        return best

    def summary(self, p):
        r, coef, cov, X = self.solve(p, full=True)
        tp, P, e, w, inc = self.unpack(p)
        npar = len(p) + X.shape[1]
        chi2 = float(r @ r); n = len(r)
        out = dict(tp=tp, P=P, e=e, w=np.degrees(w) % 360, i=np.degrees(inc), S=coef[0], sS=np.sqrt(cov[0, 0]),
                   chi2=chi2, n=n, npar=npar, dof=n - npar, bic=chi2 + npar * np.log(n))
        if self.mode == "beam":
            out.update(Bm=coef[1], sBm=np.sqrt(cov[1, 1]))
        return out
