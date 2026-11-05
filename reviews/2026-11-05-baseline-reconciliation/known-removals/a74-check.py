"""A74 (TIC 427345302) in ASAS-SN Sky Patrol v2: an independent check of Opus 5.5's
2026-11-01 result (Opus 5.5\\made\\hd282670-asassn\\zp.py), written without reading
their code past the docstring. Same raw files, different estimators, and two things
their script did not do: a sliding-epoch null that keeps the real sampling, and the
same statistic run on the alias periods the TESS pair alone allows.

Fixed beforehand (catalogue row): t0 BTJD 2884.986, P 173.8755 d, half-length 5.4 h.
"""
import os, sys, numpy as np, pandas as pd

SRC = os.environ.get("A74_INPUT_DIR", ".")
P, T0, HALF = 173.8755, 2457000 + 2884.986, 5.4 / 24  # days
rng = np.random.default_rng(427345302)

# --- comparison stars -> per-image zero point (sigma-clipped mean of log ratios) ---
c = pd.read_csv(f"{SRC}\\a74_comps_raw.csv")
c = c[(c.quality == "G") & (c.flux > 0)]
bright = c.groupby("asas_sn_id").mag.median()
c = c[c.asas_sn_id.isin(bright[bright < 14].index)].copy()
c["lr"] = np.log10(c.flux / c.groupby(["asas_sn_id", "camera"]).flux.transform("median"))

def clipped_mean(x, k=3.0, it=2):
    x = np.asarray(x, float)
    for _ in range(it):
        m, s = x.mean(), x.std()
        x = x[np.abs(x - m) <= k * max(s, 1e-6)]
    return x.mean(), x.std(), len(x)

rows = []
for img, g in c.groupby("image_id"):
    if len(g) < 8:
        continue
    m, s, n = clipped_mean(g.lr)
    rows.append((img, m, s, n))
zp = pd.DataFrame(rows, columns=["image_id", "zp", "zp_sd", "zp_n"]).set_index("image_id")

# --- target ---
d = pd.read_csv(f"{SRC}\\a74_raw.csv")
d = d[(d.quality == "G") & (d.flux > 0) & d.image_id.isin(zp.index)].copy()
d = d.join(zp, on="image_id")
d["fraw"] = d.flux / d.groupby("camera").flux.transform("median")           # no zero point
d["f"] = d.flux / 10 ** d.zp
d["f"] = d.f / d.groupby("camera").f.transform("median")                      # zero-pointed
d = d[d.groupby("camera").f.transform("size") >= 20].copy()
mad = d.groupby("camera").f.transform(lambda x: 1.4826 * np.median(np.abs(x - np.median(x))))
d["z"] = (1 - d.f) / mad
d["zraw"] = (1 - d.fraw) / d.groupby("camera").fraw.transform(lambda x: 1.4826 * np.median(np.abs(x - np.median(x))))
print(f"{len(d)} good target points with a zero point, {d.jd.min():.0f}-{d.jd.max():.0f}; "
      f"cameras {d.camera.value_counts().to_dict()}")
print(f"per-camera MAD sigma: {d.groupby('camera').f.apply(lambda x: 1.4826*np.median(np.abs(x-np.median(x)))).round(4).to_dict()}")
for thr in (1.8, 2.0, 3.0, 3.4):
    print(f"  base rate z >= {thr}: {(d.z >= thr).mean():.4f}  ({(d.z >= thr).sum()} points)")

def window(t0, p, half=HALF):
    dt = ((d.jd - t0) / p + 0.5) % 1 - 0.5
    return d[np.abs(dt * p) < half].assign(dt_h=dt[np.abs(dt * p) < half] * p * 24)

def stat(t0, p):
    w = window(t0, p)
    if len(w) == 0:
        return 0, np.nan, np.nan
    return len(w), w.z.mean(), w.z.min()

# --- the fixed ephemeris ---
print("\n== fixed ephemeris: P 173.8755, t0 BTJD 2884.986, +-5.4 h ==")
w = window(T0, P).sort_values("jd")
for _, r in w.iterrows():
    cyc = round((r.jd - T0) / P)
    print(f"  JD {r.jd:.3f} cycle {cyc:+3d} cam {r.camera} dt {r.dt_h:+5.2f} h  "
          f"flux {r.f:.4f} (raw {r.fraw:.4f})  z {r.z:+.1f} (raw {r.zraw:+.1f})  "
          f"zp from {int(r.zp_n)} comps, sd {r.zp_sd:.3f} dex")
n_obs, mean_obs, min_obs = stat(T0, P)
print(f"  n {n_obs}, mean z {mean_obs:.2f}, min z {min_obs:.2f}")
near = d[(np.abs((((d.jd - T0) / P + 0.5) % 1 - 0.5) * P) >= HALF)
         & (np.abs((((d.jd - T0) / P + 0.5) % 1 - 0.5) * P) < 10 / 24)]
print(f"  control, 5.4-10 h either side: n {len(near)}, mean flux {near.f.mean():.4f}, mean z {near.z.mean():+.2f}")

# --- sliding-epoch null: same period, same window, every other epoch ---
print("\n== null: the same statistic at every other epoch (phase steps of 0.5 h, real sampling) ==")
phases = np.arange(0, P, 0.5 / 24)
res = np.array([stat(T0 + ph, P) for ph in phases])
n, mz, minz = res[:, 0], res[:, 1], res[:, 2]
ok = n >= 3
print(f"  {len(phases)} epochs tried, {ok.sum()} with >= 3 points in window")
print(f"  P(mean z >= {mean_obs:.2f} | n>=3) = {(mz[ok] >= mean_obs).mean():.5f}   ({(mz[ok] >= mean_obs).sum()} of {ok.sum()})")
print(f"  P(min z  >= {min_obs:.2f} | n>=3) = {(minz[ok] >= min_obs).mean():.5f}   ({(minz[ok] >= min_obs).sum()} of {ok.sum()})")
ok4 = n >= 4
print(f"  with >= 4 points: {ok4.sum()} epochs; P(mean z >= obs) = {(mz[ok4] >= mean_obs).mean():.5f}, "
      f"P(min z >= obs) = {(minz[ok4] >= min_obs).mean():.5f}")
# which epochs beat it, if any
for i in np.where(ok & (mz >= mean_obs))[0][:10]:
    print(f"    epoch +{phases[i]*24:7.1f} h: n {int(n[i])} mean z {mz[i]:.2f} min z {minz[i]:.2f}")

# --- the alias periods the two TESS eclipses alone allow (N cycles between them) ---
print("\n== aliases: same t0, the in-window points for each cycle count N between the TESS pair ==")
for N in (1, 2, 3, 5, 6):
    p = (3406.613 - 2884.986) / N
    w = window(T0, p)
    zs = ", ".join(f"{z:+.1f}" for z in w.sort_values("jd").z)
    print(f"  N {N}: P {p:9.4f}  n {len(w):2d}  mean z {w.z.mean() if len(w) else float('nan'):+.2f}   z: {zs}")
p = 173.19
w = window(T0, p)
print(f"  Gaia astrometric P {p}: n {len(w)}, mean z {w.z.mean() if len(w) else float('nan'):+.2f}")

# --- secondary ---
print("\n== secondary at phase 0.4378 (from two ZTF nights; duration unknown, +-5.4 h assumed) ==")
w = window(T0 + 0.4378 * P, P).sort_values("jd")
for _, r in w.iterrows():
    print(f"  JD {r.jd:.3f} cam {r.camera} dt {r.dt_h:+5.2f} h  flux {r.f:.4f}  z {r.z:+.1f}")
print(f"  n {len(w)}, mean z {w.z.mean() if len(w) else float('nan'):+.2f}")

# --- the three NEW cycles only: drop cycle +2 (the ZTF night, already counted) ---
print("\n== null again with cycle +2 removed (JD 2460232.77 is the ZTF night; three new cycles only) ==")
keep = np.abs(d.jd - 2460232.767) > 1.0
d_all = d
d = d_all[keep].copy()
n_obs3, mean_obs3, min_obs3 = stat(T0, P)
print(f"  fixed epoch: n {n_obs3}, mean z {mean_obs3:.2f}, min z {min_obs3:.2f}")
res = np.array([stat(T0 + ph, P) for ph in phases])
n, mz, minz = res[:, 0], res[:, 1], res[:, 2]
ok = n >= 3
print(f"  P(mean z >= {mean_obs3:.2f} | n>=3) = {(mz[ok] >= mean_obs3).mean():.5f}   ({(mz[ok] >= mean_obs3).sum()} of {ok.sum()})")
for i in np.where(ok & (mz >= mean_obs3))[0][:10]:
    print(f"    epoch +{phases[i]*24:7.1f} h: n {int(n[i])} mean z {mz[i]:.2f} min z {minz[i]:.2f}")
d = d_all
