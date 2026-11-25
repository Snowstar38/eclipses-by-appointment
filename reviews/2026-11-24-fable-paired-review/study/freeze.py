"""Freeze original photometric features and three candidate orderings."""
from pathlib import Path
import csv
import hashlib
import json
from collections import Counter

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent.parent.parent
FABLE = PROJECT / "sky/fable52-2026-11-22/tce-graveyard"
PARENT = "3ae245b41eda9e8b24cc4f93611704ce879daba1"

def rows(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    paths = [FABLE/"candidates.csv", FABLE/"candidates-ffi.csv"]
    fable = {(lane,r["tic"]):r for lane,path in zip(["2min","ffi"],paths) for r in rows(path) if r["tier"]=="candidate" and r["validation"]=="light curve" and r["catalogue_gate"]=="not_in_checked_catalogues"}
    roster = HERE.parent/"batches.csv"
    features = []
    for idx, row in enumerate(rows(roster),1):
        assert (idx-1)//10 + 1 == int(row["batch"]) and (idx-1)%10+1 == int(row["slot"])
        assert row["outcome"] == "queued for follow-up"
        t = row["tic"]
        old = fable[row["stream"], t]
        raw = PROJECT/old["evidence_path"]
        v = json.loads(raw.read_text(encoding="utf8"))
        assert t == str(v["tic"]) and v["status"]=="ok" and float(row["rank_score"])==float(old["rank_score"])
        sig = v.get("n_events_sig") or 0
        cov = v.get("n_events_covered") or 0
        n = float(old["n_capable_42"]) if old["n_capable_42"] else None
        clock = v.get("global_agrees") is True
        repeats = sig >= 4 and cov > 0 and sig/cov >= 0.5
        shape = v.get("duty_below_half") is not None and v["duty_below_half"] < .12 and ((v.get("sec_snr") or 0)>=5 or (v.get("oddeven_sig_lc") or 0)>=5)
        clear = n == 0
        features.append(dict(tic=t, stream=row["stream"], queue_rank=idx, fable_score=old["rank_score"],
              clock_agrees=clock, repeated_events=repeats, narrow_with_alternation_or_secondary=shape, zero_capable_neighbours=clear,
              source_clock_score=sum((clock,repeats,shape,clear)), saved_photometry_cut=row["passed_saved_photometry_selection"],
              prior_position_and_period_clear=row["open_after_position_period_comparison"], photometric_period_days=v.get("P_lc"),
              primary_depth_ppt=v.get("depth_lc_ppt"), duty_fraction=v.get("duty_below_half"), secondary_snr=v.get("sec_snr"),
              odd_even_snr=v.get("oddeven_sig_lc"), significant_events=sig, covered_events=cov, capable_neighbours_within_42as=n,
              fable_measurement_sha256=sha(raw)))
    assert len(features)==len({r["tic"] for r in features})==402
    assert Counter(r["stream"] for r in features)=={"ffi":67,"2min":335}
    for name,key in [("fable_rank",lambda r:(-float(r["fable_score"]),int(r["tic"]))),
                     ("source_clock_rank",lambda r:(-r["source_clock_score"],-float(r["fable_score"]),int(r["tic"])))]:
        for rank,r in enumerate(sorted(features,key=key),1):r[name]=rank
    dest = HERE/"frozen-features.csv"
    with dest.open("w",encoding="utf8",newline="") as s:
        w=csv.DictWriter(s,fieldnames=features[0],lineterminator="\n")
        w.writeheader();w.writerows(features)
    manifest=dict(catalogue_parent=PARENT,cohort_size=len(features),files={p.name:sha(p) for p in [*paths,roster,dest,HERE/"analysis-plan.md",Path(__file__)]})
    (HERE/"feature-manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf8")
    print(sha(dest),Counter(r["source_clock_score"] for r in features))

if __name__=="__main__":main()
