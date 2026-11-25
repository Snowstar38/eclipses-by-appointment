"""Run 10a, two single rows outside the equal-dips set: R1090 (run 5's untestable
prediction) and R1737 (Earthshine's 80.93-d alternative), plus rows whose tabled
secondary is shallower than any main-sequence companion making the primary allows.
usage: python3 two_rows.py earthshine-pop-results-855.csv invisible-secondary-test.csv host-stars.csv
"""
import sys
import pandas as pd
import invisible_secondary as I

pop, test, hosts = sys.argv[1:4]
p = pd.read_csv(pop)
for rid in ("R1090", "R1737"):
    r = p[p.review_id == rid].iloc[0]
    r2, ds, _ = I.bound(r)
    lim = I.limit(r)
    print(f"{rid}: P = {r.P_d} d, depth {r.depth_fit_ppt} ppt, host {r.teff:.0f} K / {r.rad:.2f} Rsun -> "
          f"companion >= {r2:.2f} Rsun, secondary at P >= {ds:.1f} ppt; limit {lim:.1f} ppt ({ds / lim:.0f}x)")
o = pd.read_csv(test)
h = pd.read_csv(hosts)
h["head"] = h.period_resolution.fillna("").str.split("|").str[0].str.strip()
m = o.merge(h[["review_id", "head", "secondary_phase", "secondary_depth_ppt"]], on="review_id")
s = m[m["head"].str.startswith("P: secondary at")].copy()
s["tab_over_min"] = s.secondary_depth_ppt / s.sec_pred_ppt
low = s[s.tab_over_min < 1 / 1.5].sort_values("tab_over_min")
print(f"\nrows whose table records a secondary that Earthshine's fold left open: {len(s)}; "
      f"tabled secondary < min/1.5: {len(low)}")
print(low[["review_id", "P_d", "teff", "rad", "depth_fit_ppt", "secondary_phase", "secondary_depth_ppt",
           "sec_pred_ppt", "tab_over_min", "reading"]].round(2).to_string(index=False))
