"""Join the independent readings by TIC and count evidence per aperture."""
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def table(name):
    with (HERE / name).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def unique(name):
    rows = table(name)
    out = {r["tic"]: r for r in rows}
    assert len(rows) == len(out) == 35
    return out


if __name__ == "__main__":
    batch, timing, visual = [unique(f) for f in ("batch.csv", "sol/outcome.csv", "terra/assessment.csv")]
    assert batch.keys() == timing.keys() == visual.keys()
    pixels = table("pixels/fits.csv")
    ground = table("ground/phase-checks.csv")
    wide = json.loads((HERE / "credit/wide.json").read_bytes())
    assert len(wide["receipts"]) == 11 and all(r["complete"] for r in wide["receipts"])
    gaia = json.loads((HERE / "credit/all-sources.json").read_bytes())
    catalog = {r["tic"]:r for r in json.loads((HERE / "credit/villanova-exact.json").read_bytes())}
    rows = []
    for tic, r in batch.items():
        t = timing[tic]
        px = [v for v in pixels if v["tic"] == tic]
        g = [v for v in ground if v["tic"] == tic and v["supports_tess_prediction"] == "True"]
        prior = [v for v in wide["rows"] if v["tic"] == tic and v["matched_tic"] == tic and
                 v["catalogue"] == "J/ApJS/279/50/table2"]
        rows.append(dict(tic=tic, group=r["group"], machine_flagged=r["machine_flagged"],
                         visual=visual[tic]["visual_assessment"], timing=t["outcome"],
                         trial_period_d=t["alternate_period_d"], hits=t["alternate_hits"],
                         covered=t["alternate_covered"], sectors_with_hits=t["alternate_sectors"],
                         pixel_windows_tested=len(px), pixel_sectors_favor_target="|".join(map(str, sorted({
                             int(v["sector"]) for v in px if v["assessment"] == "favors_target"}))),
                         ztf_bands_supporting="|".join(sorted({v["band"] for v in g})),
                         ztf_clocks_supporting="|".join(sorted({v["clock_source"] for v in g})),
                         kostov_table2_exact=bool(prior), villanova_exact_record=catalog[tic]["exact"],
                         gaia_dr3=gaia[tic]["adopted_gaia"]))
    with (HERE / "outcomes.csv").open("w", newline="", encoding="utf8") as f:
        w = csv.DictWriter(f, rows[0], lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
