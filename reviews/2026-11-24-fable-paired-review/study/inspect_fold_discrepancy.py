"""Explore the disagreement between the archived fold and scalar depth after the 402-star review."""
import csv,json
from pathlib import Path
from collections import Counter
import numpy as np

HERE=Path(__file__).resolve().parent
def read(path):
    with path.open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def calculate(decisions,seed,dest):
    result=[]
    for r in read(decisions):
        t=r["tic"]
        original=json.loads((seed/(t+".json")).read_bytes())
        depth=original.get("depth_lc_ppt");path=seed/(t+"_fold.npz")
        row=dict(tic=t,paired_bin_depth_ppt="",reported_depth_ppt=depth,ratio="",flag=False,endpoint=r["endpoint"])
        if path.exists() and depth is not None and np.isfinite(depth) and depth>0:
            with np.load(path) as z:
                flux=z["fold"];base=np.nanmedian(flux)
                if base>0 and np.isfinite(flux).sum()>=2:
                    loss=1000*(1-flux/base)
                    neighbors=np.minimum(loss,np.roll(loss,-1))
                    if np.isfinite(neighbors).any():
                        d=float(np.nanmax(neighbors));ratio=d/max(1.,depth)
                        row.update(paired_bin_depth_ppt=round(d,3),ratio=round(ratio,3),flag=bool(d>=10 and ratio>=5))
        result.append(row)
    with (dest/"exploratory-fold-discrepancy.csv").open("w",encoding="utf8",newline="") as f:
        w=csv.DictWriter(f,result[0],lineterminator="\n");w.writeheader();w.writerows(result)
    combined={}
    for flag in (True,False):
        chosen=[r for r in result if r["flag"]==flag];counts=Counter(r["endpoint"] for r in chosen)
        combined[flag]=(len(chosen),counts["accepted_confirmed"]+counts["accepted_probable"],counts["identified_prior_eclipse"])
    yes,no=combined[True],combined[False]
    text=f"""# A clue for revisiting a failed period

After inspecting the corrected periods, we compared two quantities that Fable had saved before this review. In the original phase curve, we measured the deepest pair of adjacent bins using the shallower of the two. We flagged curves where that loss was at least 10 parts per thousand and at least five times the reported primary depth, using a floor of 1 part per thousand for the denominator. The calculation retains the circular phase boundary. A row without a usable positive saved depth or a usable pair of bins receives no flag.

| Original fold | Apertures | Catalogue additions | Previously reported eclipses or candidates |
|---|---:|---:|---:|
| Meets both conditions | {yes[0]} | {yes[1]} | {yes[2]} |
| Remaining apertures | {no[0]} | {no[1]} | {no[2]} |

Five of the eight hosts accepted in the initial pass already met the flag. We then revisited every other flagged aperture without a catalogue identification. The follow-up added one probable host, TIC 247999198, with two deep TESS eclipses and a favored but ambiguous recurrence in ASAS-SN. Including that follow-up raises the flagged yield to the count in the table. Five other revisited apertures each showed one isolated event above the deep-event search threshold over the indexed sectors tested.

The disparity can arise when a trial period lines up two individual eclipses but predicts many empty windows. Looking for individual events in the original time series preserves the information needed to recover an orbital period. Flux outliers or changing modulation can also deepen a folded bin.

We chose the thresholds after seeing outcomes, and the review gave unusual folds extra attention. This row-level comparison is exploratory. A separate cohort with thresholds fixed in advance is needed to measure predictive yield. The three predeclared rankings and their outcomes remain in the [main comparison](README.md).
"""
    (dest/"exploratory-fold-discrepancy.md").write_text(text,encoding="utf8")
    print(combined)
if __name__=="__main__":
    seed=HERE.parent/"fable-inputs/validate"
    if not seed.is_dir():seed=HERE.parents[1]/"fable52-2026-11-22/tce-graveyard/validate"
    calculate(HERE.parent/"adjudications.csv",seed,HERE)
