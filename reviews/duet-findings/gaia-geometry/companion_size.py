"""Is Gaia's companion big enough to make the eclipse?

For every Gaia-fold system with a gaia-geometry.json entry (mass function, TIC radius,
assumed m1) and a tabled primary depth, and whose primary eclipse sits on the conjunction
where Gaia's visible star is eclipsed (run 8's kind 0, unambiguous timing), the companion
is the eclipser. Its mass at i = 90 deg follows from the mass function; a main-sequence
star of that mass has at most radius R_MS(m2) (generous relation, +20%); the deepest
eclipse it can cause on the visible star is 1.3 (R2/R1)^2 (central, limb-darkened).
A depth more than 1.5 times that means the companion Gaia measured cannot make this
eclipse: a different binary (blend), a wrong TIC radius, or a companion that is not on
the main sequence. To stay conservative m1 is taken as max(house m1, 1.6 Msun), which
raises m2 and R2.
For kind-1 primaries (the companion is the eclipsed star) the eclipse can remove at most
the companion's share of the light; with the house m1, m2 from the mass function and
L ~ m^3 on the main sequence (shallower than bolometric, generous to the companion), the
depth must not exceed m2^3 / (m1^3 + m2^3).
A tight variant (house m1, no inflation, no limb-darkening allowance, no margin) is
printed too, to show how much the verdicts lean on the generous assumptions.
usage: python3 companion_size.py <repo-root> conjunction-kind.csv
"""
import glob
import json
import os
import sys
import numpy as np
import pandas as pd

M1_FLOOR, INFL, LD, MARGIN = 1.6, 1.2, 1.3, 1.5
REGS = [("bright73-review.csv", "depth_ppt"), ("remaining-screened-review.csv", "depth_ppt"),
        ("bright-followup-review.csv", "depth_ppt"), ("gap-review.csv", "depth_ppt"),
        ("magnitude-review.csv", "depth_ppt"), ("appointments-review.csv", "depth_ppt"),
        ("faint-band-review.csv", "depth_ppt"), ("period-free-review.csv", "depth_ppt"),
        ("returned-review.csv", "primary_depth_reported")]


def r_ms(m):
    m = np.asarray(m, float)
    return np.where(m < 1.0, m ** 0.8, m ** 0.57) * INFL


def m2_from_f(f, m1):
    lo, hi = 0.0, 20.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if mid ** 3 / (m1 + mid) ** 2 < f else (lo, mid)
    return 0.5 * (lo + hi)


def main(root, kindcsv, tight=False):
    global M1_FLOOR, INFL, LD, MARGIN
    if tight:
        M1_FLOOR, INFL, LD, MARGIN = 0.0, 1.0, 1.0, 1.0
    geo = {}
    for f in sorted(glob.glob(os.path.join(root, "reviews/**/gaia-geometry.json"), recursive=True)):
        for tic, d in json.load(open(f)).items():
            if not isinstance(d, dict):  # one file (R688) holds a single flat record, not a TIC-keyed map
                continue
            fm = d.get("mass_function", d.get("mass_function_solar"))
            r1 = d.get("r1_tic", d.get("tic_radius_solar"))
            m1 = d.get("m1_assumed", d.get("assumed_m1_solar"))
            if fm is not None and r1 is not None:
                geo.setdefault(str(tic), (float(fm), float(r1), float(m1 or 1.0)))
    dep = {}
    for fn, col in REGS:
        t = pd.read_csv(os.path.join(root, fn), dtype={"tic": str})
        for a, b in zip(t.tic, pd.to_numeric(t[col], errors="coerce")):
            if np.isfinite(b):
                dep.setdefault(str(a).split(".")[0], float(b))
    kall = pd.read_csv(kindcsv, dtype={"tic": str})
    k = kall[kall.tier.isin(["confirmed", "probable"]) & (kall.kind == 0)
          & (kall.z_closest.abs() < 3) & (kall.z_other.abs() > 3)].copy()
    k["fm"] = k.tic.map(lambda t: geo.get(t, (np.nan,) * 3)[0])
    k["r1"] = k.tic.map(lambda t: geo.get(t, (np.nan,) * 3)[1])
    k["m1"] = k.tic.map(lambda t: geo.get(t, (np.nan,) * 3)[2])
    k["depth_ppt"] = k.tic.map(dep)
    k = k.dropna(subset=["fm", "r1", "depth_ppt"])
    k["m1_used"] = np.maximum(k.m1, M1_FLOOR)
    k["m2"] = [m2_from_f(f, m) for f, m in zip(k.fm, k.m1_used)]
    k["r2_max"] = r_ms(k.m2)
    k["depth_max_ppt"] = 1e3 * np.minimum(LD * (k.r2_max / k.r1) ** 2, 1.0)
    k["excess"] = k.depth_ppt / k.depth_max_ppt
    k["too_deep"] = k.excess > MARGIN
    print(f"kind-0 accepted systems with mass function, TIC radius and depth: {len(k)}")
    print(pd.crosstab(k.tier, k.too_deep, margins=True))
    dw = k[k.r1 < 2.5]
    print("dwarf visible stars (R1 < 2.5):")
    print(pd.crosstab(dw.tier, dw.too_deep, margins=True))
    out = k.sort_values("excess", ascending=False)
    print(out[out.too_deep][["review_id", "tic", "tier", "P", "fm", "r1", "m2", "r2_max", "depth_ppt",
                             "depth_max_ppt", "excess"]].round(3).to_string(index=False))
    if tight:
        print(f"tight variant: too deep in {int(k.too_deep.sum())} of {len(k)}; by tier "
              f"{k.groupby('tier').too_deep.mean().round(3).to_dict()}")
        M1_FLOOR, INFL, LD, MARGIN = 1.6, 1.2, 1.3, 1.5
        return
    k1 = kall[kall.tier.isin(["confirmed", "probable"]) & (kall.kind == 1)
              & (kall.z_closest.abs() < 3) & (kall.z_other.abs() > 3)].copy()
    for c, i in (("fm", 0), ("r1", 1), ("m1", 2)):
        k1[c] = k1.tic.map(lambda t: geo.get(t, (np.nan,) * 3)[i])
    k1["depth_ppt"] = k1.tic.map(dep)
    k1 = k1.dropna(subset=["fm", "r1", "depth_ppt"])
    k1["m2"] = [m2_from_f(f, m) for f, m in zip(k1.fm, k1.m1)]
    k1["light_share"] = k1.m2 ** 3 / (k1.m1 ** 3 + k1.m2 ** 3)
    k1["excess"] = k1.depth_ppt / 1e3 / k1.light_share
    print(f"\nkind-1 accepted systems: {len(k1)}; depth above the companion's light share: "
          f"{int((k1.excess > 1).sum())}; largest depth/share {k1.excess.max():.2f} ({k1.loc[k1.excess.idxmax(), 'review_id']})")
    out[["review_id", "tic", "tier", "P", "e", "fm", "r1", "m1", "m1_used", "m2", "r2_max", "depth_ppt",
         "depth_max_ppt", "excess", "too_deep", "source"]].round(4).to_csv("companion-size.csv", index=False)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], tight=True)
    print()
    main(sys.argv[1], sys.argv[2])
