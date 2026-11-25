"""Check the frozen shortlist, earlier identifications and three event-time fits using Python 3."""
import csv
import json
from collections import Counter
from pathlib import Path
from statistics import mean, median

HERE = Path(__file__).resolve().parent

def rows(name):
    with (HERE / name).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))

def data(name):
    return json.loads((HERE / name).read_text(encoding="utf8"))

def period(events):
    x = [e["cycle"] for e in events]
    y = [e["center_btjd"] for e in events]
    return sum((a - mean(x)) * (b - mean(y)) for a,b in zip(x,y)) / sum((a - mean(x))**2 for a in x)

def main():
    queue = rows("current-shortlist.csv")
    assert len(queue) == len({r["tic"] for r in queue}) == 707
    assert Counter(r["stream"] for r in queue) == {"ffi":97, "2min":610}
    assert sum(r["had_previous_project_record"] == "True" for r in queue) == 258
    assert sum(r["individual_review_this_pass"] == "True" for r in queue) == 45
    assert sum(r["outcome"] == "queued for follow-up" for r in queue) == 402
    assert sum(r["outcome"] == "queued for follow-up" and r["passed_saved_photometry_selection"] == "True" and r["open_after_position_period_comparison"] == "True" for r in queue) == 23
    assert all(r["control_pass"] for r in data("vsx-queries.json")["batches"])
    earlier = rows("kounkel-identifications.csv")
    assert len(earlier) == 10 and all(r["earlier_classification"] == "d" and float(r["separation_arcsec"]) < .15 for r in earlier)
    assert len(rows("kounkel-shortlist.csv")) == 3
    hosts = rows("host-stars.csv")
    assert {h["tic"] for h in hosts} == {"298900954","95816910","305928109"}
    for h in hosts:
        s = data(h["evidence"])
        assert str(s["tic"]) == h["tic"] and str(s["gaia_dr3"]) == h["gaia_dr3"]
        if h["lane"] == "spoc":
            events = s["refined_photometry"]["events"]
            assert s["credit"]["gaia_radial_velocity_orbit"]["row"]["nss_solution_type"] == "SB1"
        else:
            events = [e for e in s["events"] if e["origin"] == "QLP" and e["phase"] == 0]
            assert len(s["pixels"]) == 4 and all(p["fit"]["verdict"] == "on_target" and not p["fit"]["unresolved_capable"] for p in s["pixels"])
        assert len(events) == int(h["primary_events"])
        assert abs(period(events) - float(h["period_days"])) < 1e-6
        assert abs(median(e["depth_ppt"] for e in events) - float(h["depth_ppt"])) <= .001
    later = next(r for r in data("clocks/95816910-sectors.json") if r["sector"] == 72)
    for kind in ["QLP","TESS-SPOC","fixed_aperture"]:
        assert len(later[kind]["primary"]) == 2 and all(abs(e[2]) < 1 for e in later[kind]["primary"])
    print("Verified the 707-target accounting, ten prior identifications and three individual timing solutions.")

if __name__ == "__main__":
    main()
