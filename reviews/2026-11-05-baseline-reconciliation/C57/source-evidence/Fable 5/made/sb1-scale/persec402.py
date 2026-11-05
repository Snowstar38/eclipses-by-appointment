r"""Per-object window-stack with empirical floor for the c9 held marginal
TIC 402940895 (c9-marg-persec.md): eclipse vs RS CVn spot-lock.

The 59955223 pattern (c8-marg-persec.md, sec59.py, refit59955223.py),
adapted, with the recorded trap avoided: NO quadratic detrend. Every
window gets a LOCAL LINEAR baseline fitted to out-of-core flux on both
sides (and a flat-median variant as a cross-check).

Steps
 0) load QLP SAP_FLUX (q==0), normalise per sector, bin to 30 min so
    s12 (30-min FFI) and s66+ (200 s) are measured on equal footing;
    per-sector quality numbers (rms, background) to flag garbage sectors.
 1) every predicted conjunction at the search ephemeris -> per-window
    depth, baseline rms, coverage (n_core, n_left, n_right).
 2) per-window empirical floor: the same measurement slid along the SAME
    sector at every off-ephemeris time (step 0.02 d, |phase| > 0.1) ->
    the window's depth as a percentile / z_emp of its own sector's null.
 3) stacked empirical floor: stack (mean over windows) at 180 trial
    phases 0.10-0.90; floor = robust scatter of the off-phase stacks;
    p_emp = fraction of off phases whose stack >= the on-phase stack.
 4) stacked profile on +-1.25 d -> width (FWHM) and shape; and a wide
    +-4 d profile to see whether the dip rides a broad spot wave.
 5) per-window time of minimum -> local linear ephemeris refit, O-C vs
    time (phase drift test), P_fit vs Gaia P.
 6) out-of-dip modulation per sector: sinusoid at P_orb (+ linear) ->
    amplitude and phase of the spot wave relative to the dip.
Receipts: persec402-out.txt (stdout), marg9-persec\402940895-*.txt/png.
"""
import glob, json, os, sys
import numpy as np
from astropy.io import fits

sys.stdout.reconfigure(encoding="utf-8")
SB = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(os.environ["TEMP"], "hunt-sb1-scale")
OUT = os.path.join(SB, "marg9-persec")
os.makedirs(OUT, exist_ok=True)
TIC = "402940895"
P0, T00, DUR = 16.4387109748565, 1632.2402, 0.261   # search.jsonl "P" row
P_GAIA, P_GAIA_ERR = 16.448138210288207, 0.0048614484
BIN = 0.5 / 24
HALF, CORE, OOT_IN = 1.25, 0.13, 0.40               # days: window, core half-width, oot inner edge

# ---------------------------------------------------------------- 0) load
def load():
    secs = {}
    for fp in sorted(glob.glob(os.path.join(CACHE, f"{TIC}_s*.fits"))):
        sec = int(os.path.basename(fp).split("_s")[1].split(".")[0])
        with fits.open(fp) as h:
            d = h[1].data
            t = np.asarray(d["TIME"], float)
            f = np.asarray(d["SAP_FLUX"], float)
            b = np.asarray(d["SAP_BKG"], float)
            q = np.asarray(d["QUALITY"], int)
        ok = np.isfinite(t) & np.isfinite(f) & (f > 0) & (q == 0)
        t, f, b = t[ok], f[ok], b[ok]
        med = np.median(f)
        f, b = f / med, b / med
        # 30-min median bins
        edges = np.arange(t.min(), t.max() + BIN, BIN)
        idx = np.digitize(t, edges)
        tb, fb, bb = [], [], []
        for i in np.unique(idx):
            m = idx == i
            if m.sum() >= 1:
                tb.append(t[m].mean()); fb.append(np.median(f[m])); bb.append(np.median(b[m]))
        secs[sec] = (np.array(tb), np.array(fb), np.array(bb))
    return secs

secs = load()
print(f"TIC {TIC}  search P {P0:.6f} t0 {T00}  dur {DUR} d | Gaia P {P_GAIA:.6f} +/- {P_GAIA_ERR:.5f}")
print(f"  (search P - Gaia P)/err = {(P0 - P_GAIA) / P_GAIA_ERR:+.2f} sigma")
print("\n0) sectors (30-min bins): n, span, point-to-point rms, 1-d-smoothed rms (activity), bkg/flux range")
secq = {}
for s, (t, f, b) in secs.items():
    p2p = 1.4826 * np.median(np.abs(np.diff(f))) / np.sqrt(2) * 1e6
    # 1-day running median -> slow-variability amplitude
    sm = np.array([np.median(f[np.abs(t - x) < 0.5]) for x in t])
    slow = (np.percentile(sm, 95) - np.percentile(sm, 5)) * 1e3
    secq[s] = (p2p, slow)
    print(f"  s{s:03d}: n {len(t):4d}  BTJD {t.min():.2f}-{t.max():.2f}  p2p {p2p:5.0f} ppm  "
          f"slow 5-95% {slow:5.1f} ppt  bkg {np.percentile(b,5):.3f}-{np.percentile(b,95):.3f}")
p2p_med = np.median([v[0] for v in secq.values()])
BAD = sorted(s for s, v in secq.items() if v[0] > 5 * p2p_med)
print(f"  garbage-sector cut (p2p > 5x median {p2p_med:.0f} ppm): {BAD} -> excluded from every "
      f"measurement below (listed in the window table only)")
secs_all = secs
secs = {s: v for s, v in secs_all.items() if s not in BAD}

# ---------------------------------------------------------------- measurement
def measure(t, f, tc, linear=True):
    dt = t - tc
    m = np.abs(dt) < HALF
    dt, ff = dt[m], f[m]
    core = np.abs(dt) < CORE
    oot = np.abs(dt) > OOT_IN
    nl, nr = int((oot & (dt < 0)).sum()), int((oot & (dt > 0)).sum())
    if core.sum() < 4 or nl < 8 or nr < 8:
        return None
    if linear:
        co = np.polyfit(dt[oot], ff[oot], 1)
        base = np.polyval(co, dt)
    else:
        base = np.full_like(dt, np.median(ff[oot]))
    r = ff / base
    dep = (1 - np.median(r[core])) * 1e6
    rms = 1.4826 * np.median(np.abs(r[oot] - np.median(r[oot]))) * 1e6
    return dep, rms, int(core.sum()), nl, nr

def conj_times(t, P, t0, phi=0.0):
    n0 = int(np.floor((t.min() - t0) / P)) - 1
    n1 = int(np.ceil((t.max() - t0) / P)) + 1
    return [(k, t0 + (k + phi) * P) for k in range(n0, n1 + 1)
            if t.min() - 0.3 <= t0 + (k + phi) * P <= t.max() + 0.3]

# ---------------------------------------------------------------- 1) + 2) per-window
print(f"\n1-2) per-window at the search ephemeris (linear local baseline; core |dt|<{CORE} d, "
      f"oot {OOT_IN}-{HALF} d each side)")
print("  sec  cycle   tc        depth_lin  depth_flat  base_rms  n_core n_L n_R | sector null: med  sd_emp  z_emp  pctile")
onwin = []
rows = []
for s, (t, f, b) in sorted(secs_all.items()):
    if s in BAD:
        for k, tc in conj_times(t, P0, T00):
            print(f"  s{s:03d} {k:4d} {tc:9.3f}   EXCLUDED (garbage sector)")
            rows.append(dict(sec=s, cycle=k, tc=round(tc, 4), measurable=False, note="garbage sector"))
        continue
    # sector null: slide along the sector at off-ephemeris times
    grid = np.arange(t.min() + HALF, t.max() - HALF, 0.02)
    ph = ((grid - T00) / P0 + 0.5) % 1 - 0.5
    nulls = []
    for x in grid[np.abs(ph) > 0.10]:
        r = measure(t, f, x)
        if r:
            nulls.append(r[0])
    nulls = np.array(nulls)
    for k, tc in conj_times(t, P0, T00):
        r = measure(t, f, tc)
        rf = measure(t, f, tc, linear=False)
        if not r:
            m = np.abs(t - tc) < HALF
            print(f"  s{s:03d} {k:4d} {tc:9.3f}   unmeasurable (bins in window {m.sum()}, "
                  f"core {(np.abs(t-tc)<CORE).sum()})")
            rows.append(dict(sec=s, cycle=k, tc=tc, measurable=False))
            continue
        dep, rms, nc, nl, nr = r
        if len(nulls) > 20:
            nm = np.median(nulls)
            sd = 1.4826 * np.median(np.abs(nulls - nm))
            z = (dep - nm) / sd
            pct = 100 * np.mean(nulls < dep)
        else:
            nm = sd = z = pct = np.nan
        print(f"  s{s:03d} {k:4d} {tc:9.3f}   {dep:7.0f}   {rf[0]:8.0f}    {rms:6.0f}   {nc:4d} {nl:3d} {nr:3d} | "
              f"{nm:+6.0f} {sd:6.0f}  {z:+5.2f}  {pct:5.1f}  (n_null {len(nulls)})")
        onwin.append((s, k, tc, dep, rms, nc))
        rows.append(dict(sec=s, cycle=k, tc=round(tc, 4), measurable=True, depth_lin=round(dep),
                         depth_flat=round(rf[0]), base_rms=round(rms), n_core=nc, n_L=nl, n_R=nr,
                         null_med=round(float(nm)), null_sd=round(float(sd)), z_emp=round(float(z), 2),
                         pctile=round(float(pct), 1)))
json.dump(rows, open(os.path.join(OUT, f"{TIC}-windows.json"), "w"), indent=1)

# ---------------------------------------------------------------- 3) stacked floor
def stack(phi, P=P0, t0=T00, exclude=()):
    d = []
    for s, (t, f, b) in sorted(secs.items()):
        if s in exclude:
            continue
        for k, tc in conj_times(t, P, t0, phi):
            r = measure(t, f, tc)
            if r:
                d.append(r[0])
    return (np.mean(d), np.median(d), len(d)) if d else (np.nan, np.nan, 0)

def floor_report(label, exclude=()):
    on = stack(0.0, exclude=exclude)
    phis = np.arange(0.10, 0.9001, 0.005)
    st = np.array([stack(p, exclude=exclude) for p in phis])
    good = st[:, 2] >= 3
    mu = st[good, 0]
    med0 = np.median(mu)
    fl = 1.4826 * np.median(np.abs(mu - med0))
    p = np.mean(mu >= on[0])
    ipk = int(np.argmax(mu))
    print(f"  [{label}] on-phase stack: mean {on[0]:+.0f} ppm, median {on[1]:+.0f} ppm, {on[2]} windows")
    print(f"     off-phase null ({good.sum()} phases 0.10-0.90, n_win >= 3): median {med0:+.0f}, "
          f"robust sd {fl:.0f} ppm, max {mu.max():+.0f} (phase {phis[good][ipk]:.3f})")
    print(f"     -> on-phase = {(on[0] - med0) / fl:+.1f} sigma_emp; p_emp = {p:.4f} "
          f"({int(np.sum(mu >= on[0]))} of {good.sum()} off phases >= on); on / off-max = {on[0] / mu.max():.2f}")
    return phis[good], st[good], on, med0, fl

print("\n3) stacked window depth vs empirical floor (equal-weight mean over windows)")
phis, st, on, med0, fl = floor_report("good sectors")
for s_drop in sorted(secs):
    floor_report(f"drop s{s_drop:03d}", exclude=(s_drop,))
i5 = int(np.argmin(np.abs(phis - 0.5)))
print(f"  phase 0.500 stack (P/2 alias test: a dip here would mean P = {P0/2:.4f}): "
      f"{st[i5, 0]:+.0f} ppm, n {int(st[i5, 2])} ({(st[i5, 0] - med0) / fl:+.1f} sigma_emp)")
with open(os.path.join(OUT, f"{TIC}-phasescan.txt"), "w") as fh:
    fh.write("# phase  stack_mean_ppm  stack_median_ppm  n_windows (all sectors; phase 0 = search ephemeris)\n")
    fh.write(f"0.000 {on[0]:.0f} {on[1]:.0f} {on[2]}\n")
    for p, (a, m, n) in zip(phis, st):
        fh.write(f"{p:.3f} {a:.0f} {m:.0f} {int(n)}\n")

# jackknife on-phase
d_on = np.array([w[3] for w in onwin])
jk = [np.mean(np.delete(d_on, i)) for i in range(len(d_on))]
print(f"  jackknife drop-one on-phase mean: {min(jk):+.0f}..{max(jk):+.0f} ppm (full {d_on.mean():+.0f}); "
      f"min single window {d_on.min():+.0f}, all > 0: {bool((d_on > 0).all())}")
medd = np.median(d_on)
print(f"  depth stability: windows {', '.join(f'{x/1e3:.1f}' for x in d_on)} ppt; median {medd/1e3:.2f}, "
      f"relMAD {1.4826 * np.median(np.abs(d_on - medd)) / medd:.3f}, min/max {d_on.min()/d_on.max():.2f}")

# scrambled-epoch null: each window independently moved to a random off-ephemeris time
# in its own sector (|phase| > 0.1), stacked; 20000 draws.
rng = np.random.default_rng(402940895)
pools = {}
for s, (t, f, b) in secs.items():
    grid = np.arange(t.min() + HALF, t.max() - HALF, 0.02)
    ph = ((grid - T00) / P0 + 0.5) % 1 - 0.5
    pools[s] = np.array([r[0] for x in grid[np.abs(ph) > 0.10] if (r := measure(t, f, x))])
draws = np.zeros(20000)
for s, k, tc, dep, rms, nc in onwin:
    draws += rng.choice(pools[s], size=draws.size)
draws /= len(onwin)
dm, ds = np.median(draws), 1.4826 * np.median(np.abs(draws - np.median(draws)))
print(f"  scrambled-epoch null ({len(onwin)} windows each redrawn from its own sector, 20000 stacks): "
      f"median {dm:+.0f}, robust sd {ds:.0f}, 99.9th pct {np.percentile(draws, 99.9):+.0f}, max {draws.max():+.0f} ppm")
print(f"     -> on-phase mean {d_on.mean():+.0f} = {(d_on.mean() - dm) / ds:+.1f} sigma_emp; "
      f"p_emp {np.mean(draws >= d_on.mean()):.5f} ({int(np.sum(draws >= d_on.mean()))}/20000)")
# a stricter version: require every redrawn window >= that window's own measured depth's minimum
allpos = np.ones(20000, bool)
for s, k, tc, dep, rms, nc in onwin:
    allpos &= rng.choice(pools[s], size=20000) >= d_on.min()
print(f"     chance that all {len(onwin)} redrawn windows reach >= {d_on.min():.0f} ppm (the weakest real window): "
      f"{allpos.mean():.5f}")

# ---------------------------------------------------------------- 4) profiles
def profile(half, step, P=P0, t0=T00, exclude=(102, 103), detrend=True):
    edges = np.arange(-half, half + step / 2, step)
    acc = [[] for _ in range(len(edges) - 1)]
    for s, (t, f, b) in sorted(secs.items()):
        if s in exclude:
            continue
        for k, tc in conj_times(t, P, t0):
            dt = t - tc
            m = np.abs(dt) < half
            if (np.abs(dt) < CORE).sum() < 4:
                continue
            dd, ff = dt[m], f[m]
            if detrend:
                oot = (np.abs(dd) > OOT_IN) & (np.abs(dd) < HALF)
                if (oot & (dd < 0)).sum() < 8 or (oot & (dd > 0)).sum() < 8:
                    continue
                ff = ff / np.polyval(np.polyfit(dd[oot], ff[oot], 1), dd)
            else:
                ff = ff / np.median(ff)
            j = np.digitize(dd, edges) - 1
            for jj, v in zip(j, ff):
                if 0 <= jj < len(acc):
                    acc[jj].append(v)
    c = 0.5 * (edges[1:] + edges[:-1])
    y = np.array([np.median(a) if len(a) >= 3 else np.nan for a in acc])
    e = np.array([1.2533 * np.std(a) / np.sqrt(len(a)) if len(a) >= 3 else np.nan for a in acc])
    return c, y, e

print("\n4) stacked profile, local-linear baseline, +-1.25 d, 0.05 d bins (excl s102/s103)")
c, y, e = profile(1.25, 0.05)
for ci, yi, ei in zip(c, y, e):
    bar = "#" * max(0, int(round((1 - yi) * 1e3))) if np.isfinite(yi) else ""
    print(f"  {ci:+.3f}  {(1 - yi) * 1e3:+6.2f} +/- {ei * 1e3:4.2f} ppt  {bar}")
dep_prof = 1 - np.nanmin(y)
half_lvl = 1 - dep_prof / 2
inside = c[np.isfinite(y) & (y < half_lvl)]
fwhm = (inside.max() - inside.min() + 0.05) if len(inside) else np.nan
print(f"  profile depth {dep_prof * 1e3:.2f} ppt, FWHM ~{fwhm:.2f} d ({fwhm * 24:.1f} h, "
      f"{fwhm / P0:.3f} phase); bins below half-depth: {inside.min():+.3f}..{inside.max():+.3f}")
oot_y = y[np.abs(c) > 0.5]
print(f"  oot (|dt|>0.5) bins: rms {np.nanstd(oot_y) * 1e6:.0f} ppm, max |dev| {np.nanmax(np.abs(oot_y - 1)) * 1e6:.0f} ppm")

print("\n4b) wide raw profile (no detrend, per-window median-normalised), +-4 d, 0.25 d bins")
cw, yw, ew = profile(4.0, 0.25, detrend=False)
for ci, yi, ei in zip(cw, yw, ew):
    print(f"  {ci:+.3f}  {(1 - yi) * 1e3:+6.2f} +/- {ei * 1e3:4.2f} ppt")

# ---------------------------------------------------------------- 5) timing / refit / drift
print("\n5) per-window time of minimum (depth maximised over tc offset +-0.4 d, 0.005 d step)")
tmins = []
for s, k, tc, dep, rms, nc in onwin:
    t, f, b = secs[s]
    offs = np.arange(-0.4, 0.4001, 0.005)
    dd = np.array([(measure(t, f, tc + o) or (np.nan,))[0] for o in offs])
    if not np.isfinite(dd).any():
        continue
    i = int(np.nanargmax(dd))
    # half-max extent of the depth-vs-offset curve as a crude timing error
    hm = dd >= dd[i] - 0.5 * rms / np.sqrt(max(nc, 1))
    lo, hi = offs[hm].min(), offs[hm].max()
    err = max((hi - lo) / 2, 0.01)
    tmins.append((s, k, tc + offs[i], dd[i], err, offs[i]))
    print(f"  s{s:03d} cyc {k:4d}: t_min {tc + offs[i]:9.3f}  (O-C vs search eph {offs[i] * 24:+6.2f} h, "
          f"+/-{err * 24:.2f} h)  depth at min {dd[i]:6.0f} ppm")
tm = np.array([x[2] for x in tmins]); ky = np.array([x[1] for x in tmins]); er = np.array([x[4] for x in tmins])
A = np.vstack([np.ones_like(ky, dtype=float), ky.astype(float)]).T
W = np.diag(1 / er**2)
cov = np.linalg.inv(A.T @ W @ A)
t0f, Pf = cov @ A.T @ W @ tm
res = tm - (t0f + ky * Pf)
chi2 = np.sum((res / er) ** 2); dof = len(tm) - 2
scale = np.sqrt(max(chi2 / dof, 1.0)) if dof > 0 else 1.0
ePf = np.sqrt(cov[1, 1]) * scale
print(f"  local linear refit ({len(tm)} minima, cycles {ky.min()}..{ky.max()} = {ky.max() - ky.min()} cycles):")
print(f"    P_fit = {Pf:.5f} +/- {ePf:.5f} d   T0 = {t0f:.4f}   rms O-C {np.sqrt(np.mean(res**2)) * 24:.2f} h, "
      f"chi2/dof {chi2:.1f}/{dof}")
print(f"    (P_fit - P_gaia)/sqrt(eG^2+ef^2) = {(Pf - P_GAIA) / np.hypot(P_GAIA_ERR, ePf):+.2f} sigma; "
      f"vs search P: {(Pf - P0) / ePf:+.2f} sigma_fit")
for (s, k, t_, d_, e_, o_), r_ in zip(tmins, res):
    yr = 2014 + (t_ + 2457000 - 2456658.5) / 365.25
    print(f"    s{s:03d} cyc {k:4d}  {yr:7.2f}  O-C {r_ * 24:+6.2f} h  ({r_ / Pf:+.4f} phase)")
# drift: quadratic term significance
if len(tm) >= 4:
    A2 = np.vstack([np.ones_like(ky, dtype=float), ky, ky.astype(float)**2]).T
    cov2 = np.linalg.inv(A2.T @ W @ A2); c2 = cov2 @ A2.T @ W @ tm
    r2 = tm - A2 @ c2
    chi2b = np.sum((r2 / er) ** 2)
    print(f"    quadratic O-C term: {c2[2] * 24 * 1e3:+.3f} mh/cyc^2 ; chi2 {chi2:.1f} -> {chi2b:.1f} (dof {dof} -> {dof - 1})")
gaia_drift = P_GAIA_ERR * (ky.max() - ky.min())
print(f"  Gaia P error alone drifts a conjunction by {gaia_drift:.2f} d = {gaia_drift / P_GAIA:.3f} phase (1 sigma) "
      f"over the TESS span; search-vs-Gaia P difference accumulates {(P_GAIA - P0) * (ky.max() - ky.min()):.2f} d")

# refit-ephemeris stack + floor
print("\n5b) stack + floor re-run at the local refit ephemeris")
def stack_P(phi, P, t0):
    d = []
    for s, (t, f, b) in sorted(secs.items()):
        for k, tc in conj_times(t, P, t0, phi):
            r = measure(t, f, tc)
            if r:
                d.append(r[0])
    return (np.mean(d), len(d)) if d else (np.nan, 0)
onf = stack_P(0.0, Pf, t0f)
offf = np.array([stack_P(p, Pf, t0f) for p in np.arange(0.10, 0.9001, 0.005)])
g = offf[:, 1] >= 3
mf = np.median(offf[g, 0]); sf = 1.4826 * np.median(np.abs(offf[g, 0] - mf))
print(f"  on {onf[0]:+.0f} ppm ({onf[1]} win); null median {mf:+.0f}, sd {sf:.0f}, max {offf[g, 0].max():+.0f} -> "
      f"{(onf[0] - mf) / sf:+.1f} sigma_emp, p_emp {np.mean(offf[g, 0] >= onf[0]):.4f}")

# ---------------------------------------------------------------- 6) spot wave per sector
print("\n6) out-of-dip modulation per sector: f = a + b*t + A*sin(2pi(t-T0)/P + phi)  (|dt from any conj| > 0.5 d)")
print("   phase_min = orbital phase of the sinusoid's minimum (0 = dip)")
for s, (t, f, b) in sorted(secs.items()):
    ph = ((t - T00) / P0) % 1
    m = np.minimum(ph, 1 - ph) * P0 > 0.5
    tt, ff = t[m], f[m]
    X = np.vstack([np.ones_like(tt), tt - tt.mean(), np.sin(2 * np.pi * (tt - T00) / P0),
                   np.cos(2 * np.pi * (tt - T00) / P0)]).T
    co, *_ = np.linalg.lstsq(X, ff, rcond=None)
    A_ = np.hypot(co[2], co[3])
    # minimum of S sin x + C cos x at x = atan2(S, C) + pi  ... solve numerically
    xs = np.linspace(0, 2 * np.pi, 3600)
    xmin = xs[np.argmin(co[2] * np.sin(xs) + co[3] * np.cos(xs))]
    span = tt.max() - tt.min()
    print(f"  s{s:03d}: semi-amp {A_ * 1e3:5.2f} ppt  phase_min {xmin / (2 * np.pi):.3f}  "
          f"slope {co[1] * 1e3:+.3f} ppt/d  (span {span:.1f} d = {span / P0:.2f} cycles)")

# ---------------------------------------------------------------- 7) background / centroid at the dips
print("\n7) systematics check at each dip: core-minus-oot median of SAP_BKG (native units) and "
      "SAP_X/SAP_Y (millipix), raw cadence; z = shift / (oot robust sd / sqrt(n_core))")
for s, k, tc, dep, rms, nc in onwin:
    fp = glob.glob(os.path.join(CACHE, f"{TIC}_s{s:03d}.fits"))[0]
    with fits.open(fp) as h:
        d = h[1].data
        t = np.asarray(d["TIME"], float); f = np.asarray(d["SAP_FLUX"], float)
        q = np.asarray(d["QUALITY"], int)
        cols = {c: np.asarray(d[c], float) for c in ("SAP_BKG", "SAP_X", "SAP_Y")}
    ok = np.isfinite(t) & np.isfinite(f) & (f > 0) & (q == 0)
    med = np.median(f[ok])
    dt = t - tc
    core = ok & (np.abs(dt) < CORE)
    oot = ok & (np.abs(dt) > OOT_IN) & (np.abs(dt) < HALF)
    out = []
    for cname, v in cols.items():
        dd = np.median(v[core]) - np.median(v[oot])
        sd = 1.4826 * np.median(np.abs(v[oot] - np.median(v[oot]))) / np.sqrt(core.sum())
        out.append(f"{cname} {dd:+9.3f} (z {dd / sd:+5.1f})" if cname == "SAP_BKG"
                   else f"{cname} {dd * 1e3:+6.1f} mpx (z {dd / sd:+5.1f})")
    print(f"  s{s:03d} cyc {k:4d}: dip {dep / 1e3:.1f} ppt | " + "  ".join(out))
    # empirical centroid floor: same core-minus-oot shift slid along the sector, off-ephemeris
    emp = []
    grid = np.arange(t[ok].min() + HALF, t[ok].max() - HALF, 0.05)
    phg = ((grid - T00) / P0 + 0.5) % 1 - 0.5
    for x in grid[np.abs(phg) > 0.10]:
        dx = t - x
        cc = ok & (np.abs(dx) < CORE); oo = ok & (np.abs(dx) > OOT_IN) & (np.abs(dx) < HALF)
        if cc.sum() < 4 or oo.sum() < 16:
            continue
        emp.append([np.median(cols[c_][cc]) - np.median(cols[c_][oo]) for c_ in ("SAP_X", "SAP_Y")])
    emp = np.array(emp)
    on_xy = [np.median(cols[c_][core]) - np.median(cols[c_][oot]) for c_ in ("SAP_X", "SAP_Y")]
    zs = []
    for j, nm in enumerate(("X", "Y")):
        m_, s_ = np.median(emp[:, j]), 1.4826 * np.median(np.abs(emp[:, j] - np.median(emp[:, j])))
        zs.append(f"{nm} z_emp {(on_xy[j] - m_) / s_:+5.1f} (pct {100 * np.mean(emp[:, j] < on_xy[j]):5.1f})")
    print(f"       empirical centroid floor ({len(emp)} off-ephemeris windows): " + "  ".join(zs))

# ---------------------------------------------------------------- figure (for the record only)
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 3, figsize=(15, 3.6))
    ax[0].errorbar(c, (1 - y) * 1e3, e * 1e3, fmt="k.")
    ax[0].invert_yaxis(); ax[0].set_xlabel("t - tc (d)"); ax[0].set_ylabel("dip (ppt)")
    ax[0].set_title("stacked profile, linear local baseline")
    ax[1].plot(phis, st[:, 0], "k-", lw=0.8); ax[1].axhline(on[0], color="tab:red")
    ax[1].axhline(med0 + 3 * fl, color="0.5", ls="--"); ax[1].set_xlabel("trial phase")
    ax[1].set_title("off-phase stacks (null) vs on-phase (red)")
    ax[2].errorbar(ky, res * 24, er * 24, fmt="k.")
    ax[2].axhline(0, color="0.5"); ax[2].set_xlabel("cycle"); ax[2].set_ylabel("O-C (h)")
    ax[2].set_title("O-C at local refit")
    plt.tight_layout(); plt.savefig(os.path.join(OUT, f"{TIC}-stack.png"), dpi=100); plt.close()
except Exception as ex:
    print("figure skipped:", ex)
print("\ndone")
