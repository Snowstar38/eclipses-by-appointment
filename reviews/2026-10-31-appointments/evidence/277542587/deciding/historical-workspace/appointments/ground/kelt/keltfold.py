"""Does a KELT light curve from 2006-2017 hold the eclipses TESS saw once in 2020-2025?
For a star whose period rests on Gaia's spectroscopic orbit alone, scan periods across
Gaia's P +- NSIG sigma, anchor the phase on the TESS eclipse time, and measure the mean
flux deficit of the KELT points that fall inside the eclipse window (box of width T14,
and its central half) against the rest. A real eclipse gives a sharp S/N peak at one
period; the grid's own S/N scatter is the null. Second eclipse (B) optional: the two
windows are tested jointly and separately.
python keltfold.py <kelt.txt> <name> <P> <sigP> <T0_btjd> <T14_h> <depth_pct> [T0b T14b_h depthb] [--nsig 4]
writes <name>_fold.txt and <name>_fold.png beside the input.
"""
import os, sys, argparse, numpy as np, datetime as dt
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt

def utc(jd):
    return (dt.datetime(2000, 1, 1, 12) + dt.timedelta(days=jd - 2451545.0)).strftime("%Y-%m-%d %H:%M")

def load(fn):
    d = np.loadtxt(fn); t, o, p, mag, err = d.T
    keep = np.zeros(len(t), bool)
    for oo in (0, 1):   # per orientation: TFA if it exists, else raw
        has_tfa = ((o == oo) & (p == 1)).any()
        keep |= (o == oo) & (p == (1 if has_tfa else 0))
    t, o, mag = t[keep], o[keep], mag[keep]
    flux = 10 ** (-0.4 * mag)
    for oo in (0, 1):
        k = o == oo
        if k.any(): flux[k] /= np.median(flux[k])
    good = (flux > 0.5) & (flux < 1.5)
    return t[good], flux[good]

def scan(t, flux, Ps, T0, T14d, half=False):
    """mean deficit of in-window points vs out-of-window, per trial period"""
    w = T14d / 2 * (0.5 if half else 1.0)
    dep = np.full(len(Ps), np.nan); snr = np.full(len(Ps), np.nan); nin = np.zeros(len(Ps), int)
    for i, P in enumerate(Ps):
        ph = ((t - T0 + P / 2) % P) - P / 2
        m = np.abs(ph) < w
        n = m.sum(); nin[i] = n
        if n < 3: continue
        out = flux[~m]; inn = flux[m]
        d = np.mean(out) - np.mean(inn)
        e = np.sqrt(np.var(inn, ddof=1) / n + np.var(out, ddof=1) / len(out))
        # a floor on the error from the global scatter so a few quiet points cannot fake a peak
        e = max(e, 1.4826 * np.median(np.abs(flux - np.median(flux))) / np.sqrt(n))
        dep[i] = d; snr[i] = d / e
    return dep, snr, nin

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fn"); ap.add_argument("name")
    ap.add_argument("P", type=float); ap.add_argument("sigP", type=float)
    ap.add_argument("T0", type=float); ap.add_argument("T14", type=float); ap.add_argument("depth", type=float)
    ap.add_argument("rest", nargs="*", type=float)
    ap.add_argument("--nsig", type=float, default=4.0)
    a = ap.parse_args()
    here = os.path.dirname(os.path.abspath(a.fn))
    t, flux = load(a.fn)
    T0 = a.T0 + 2457000.0; T14d = a.T14 / 24
    B = None
    if len(a.rest) == 3:
        B = (a.rest[0] + 2457000.0, a.rest[1] / 24, a.rest[2])
    ncyc = (T0 - np.median(t)) / a.P
    step = (T14d / 6) / abs(ncyc)                     # a sixth of the window per cycle count
    Ps = np.arange(a.P - a.nsig * a.sigP, a.P + a.nsig * a.sigP, step)
    out = open(os.path.join(here, f"{a.name}_fold.txt"), "w")
    def pr(*x):
        s = " ".join(str(y) for y in x); print(s); out.write(s + "\n")
    sc = 1.4826 * np.median(np.abs(flux - np.median(flux)))
    pr(f"{a.name}: {len(t)} KELT points {utc(t.min())[:10]} to {utc(t.max())[:10]}, point scatter {sc*100:.2f}%; "
       f"{abs(ncyc):.0f} cycles from the TESS eclipse; Gaia P {a.P} +- {a.sigP} d; grid {len(Ps)} periods, step {step:.5f} d")
    pr(f"expected in-window points per trial period: {len(t) * T14d / a.P:.1f}; A depth {a.depth}% is {a.depth/100/sc:.1f} sigma per point")
    res = {}
    for label, (t0, w, dpt) in {"A": (T0, T14d, a.depth), **({"B": B} if B else {})}.items():
        for half in (False, True):
            dep, snr, nin = scan(t, flux, Ps, t0, w, half)
            key = f"{label}{'c' if half else ''}"
            res[key] = (dep, snr, nin)
            j = np.nanargmax(snr)
            fin = np.isfinite(snr)
            pr(f"  {key:2s} ({'central half' if half else 'full box'}): best P {Ps[j]:.5f} S/N {snr[j]:.1f} depth {dep[j]*100:+.2f}% "
               f"n_in {nin[j]}; grid S/N median {np.nanmedian(snr):.2f}, robust sd {1.4826*np.nanmedian(np.abs(snr[fin]-np.nanmedian(snr))):.2f}, "
               f"2nd-best S/N {np.sort(snr[fin])[-2]:.1f}; expected depth {dpt}%")
    if B:
        # joint: both windows at once
        depA, snrA, _ = res["A"]; depB, snrB, _ = res["B"]
        joint = np.nan_to_num(snrA) + np.nan_to_num(snrB)
        j = np.argmax(joint)
        pr(f"  A+B joint S/N sum: best P {Ps[j]:.5f} ({snrA[j]:.1f} + {snrB[j]:.1f}); A depth {depA[j]*100:+.2f}%, B {depB[j]*100:+.2f}%")
    # strongest candidate: full-box A
    dep, snr, nin = res["A"]; j = np.nanargmax(snr); Pbest = Ps[j]
    pr(f"\nbest A period {Pbest:.5f} d is {(Pbest - a.P)/a.sigP:+.2f} sigma from Gaia; eclipses it predicts after today:")
    now = (dt.datetime.utcnow() - dt.datetime(2000, 1, 1, 12)).total_seconds() / 86400 + 2451545.0
    k = int(np.ceil((now - T0) / Pbest))
    for kk in range(k, k + 4):
        pr(f"   {utc(T0 + kk * Pbest)}  (BTJD {T0 + kk*Pbest - 2457000:.3f})")
    out.close()
    fig, ax = plt.subplots(2, 1, figsize=(10, 7))
    ax[0].plot(Ps, res["A"][1], lw=0.8, label="A, full box")
    ax[0].plot(Ps, res["Ac"][1], lw=0.8, label="A, central half")
    if B:
        ax[0].plot(Ps, res["B"][1], lw=0.8, label="B, full box")
    ax[0].axvline(a.P, color="k", ls=":", lw=0.8, label="Gaia P"); ax[0].legend(fontsize=8)
    ax[0].set_xlabel("trial period (d)"); ax[0].set_ylabel("in-window deficit S/N"); ax[0].set_title(f"{a.name}: KELT vs TESS eclipse, period scan")
    ph = ((t - T0 + Pbest / 2) % Pbest) - Pbest / 2
    ax[1].plot(ph * 24, (flux - 1) * 100, ".", ms=3, alpha=0.6)
    ax[1].axvspan(-a.T14 / 2, a.T14 / 2, color="r", alpha=0.12, label=f"A window, P = {Pbest:.5f}")
    ax[1].set_xlim(-5 * a.T14, 5 * a.T14); ax[1].set_ylim(-max(5, 2 * a.depth), 5)
    ax[1].set_xlabel("hours from predicted A mid-eclipse"); ax[1].set_ylabel("flux - 1 (%)"); ax[1].legend(fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(here, f"{a.name}_fold.png"), dpi=110)

if __name__ == "__main__":
    main()
