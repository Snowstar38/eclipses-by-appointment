"""Reproduce membership and selected numerical checks from this electronic supplement.

Run with Python 3 from any directory. Uses only the standard library.
"""
import csv
import json
import math
from pathlib import Path
from statistics import mean, median

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def rows(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def source(path):
    return json.loads(path.read_text(encoding="utf8"))


def fit_period(cycles, times):
    cx, tx = mean(cycles), mean(times)
    variance = sum((x-cx)**2 for x in cycles)
    return sum((x-cx)*(t-tx) for x,t in zip(cycles,times)) / variance


def check_host(host):
    evidence = source(HERE / host["evidence"])
    assert str(evidence["tic"]) == host["tic"]
    assert str(evidence["gaia_dr3"]) == host["gaia_dr3"]
    period = float(host["period_days"])
    assert period > 0 and math.isfinite(float(host["epoch_btjd"]))
    if host["lane"] == "ffi":
        wider = host["evidence"].startswith("ffi-wider/")
        timing = evidence["timing"] if wider else evidence["timed_photometry"]
        primary = [e for e in timing["events"] if e["phase"] == 0]
        measured = fit_period([e["k"] for e in primary], [e["center_btjd"] for e in primary])
        assert abs(measured - period) < 1e-7
        assert len(primary) == int(host["primary_events"])
        assert abs(median(e["depth_ppt"] for e in primary) - float(host["depth_ppt"])) < .001
        assert {int(str(e["sector"]).lstrip("sS")) for e in primary} == {
            int(sector) for sector in host["sectors"].split("|")
        }
        pairs = evidence["phase_specific_pixel_fits"] if wider else evidence["pixel_comparisons"]
        assert len({(e["sector"], e["phase"]) for e in pairs}) == 4
        assert all(not e["fit"].get("unresolved_capable") for e in pairs if e["phase"] == 0)
        if not wider or host["tier"] == "confirmed":
            assert all(not e["fit"].get("unresolved_capable") for e in pairs)
            assert all(e["fit"]["verdict"] == "on_target" for e in pairs)
        if wider:
            assert evidence["disposition"] == host["tier"]
            assert not evidence["catalogues"]["wide_ijspeert_2024_prsa_period_matches_15_arcmin"]
    elif host["tic"] == "375085822":
        events = evidence["events"]
        measured = fit_period([int(e["cycle"]) for e in events], [float(e["center_btjd"]) for e in events])
        assert abs(measured - period) < 1e-7
        assert {e["sector"] for e in events} == {"18", "58", "85"}
        assert all(float(e["center_distance_as"]) < 3 for e in evidence["difference_fits"])
        detections = [e for survey in evidence["independent_photometry"].values() for e in survey
                      if e.get("result") == "eclipse_seen"]
        assert {"ZTF_zg", "ZTF_zr", "ASASSN_g"}.issubset(e["survey"] for e in detections)
    elif host["lane"] == "ground":
        assert abs(period - evidence["refit"]["P"]) < 1e-7
        assert any(e.get("result") == "eclipse_seen" for e in evidence["ground_photometry"])
    elif host["lane"] == "gaia" and "fit" in evidence:
        assert abs(period - float(evidence["fit"]["period_days"])) < 1e-6


def main():
    hosts = rows(HERE / "host-stars.csv")
    ledger = {r["tic"]: r for r in rows(ROOT / "accepted-systems.csv")}
    corrected = rows(HERE / "prior-identifications.csv")
    decisions = {r["review_id"]: r for r in rows(ROOT / "scientific-review-register.csv")}
    assert len(hosts) == len({r["tic"] for r in hosts}) == len({r["gaia_dr3"] for r in hosts})
    for h in hosts:
        assert ledger[h["tic"]]["review_id"] == h["review_id"]
        assert ledger[h["tic"]]["tier"] == h["tier"]
        check_host(h)
    for row in corrected:
        assert row["tic"] not in ledger
        assert decisions[row["review_id"]]["count_addition"] == "false"
        assert float(row["earlier_period_days"]) > 0
    print(f"Verified {len(hosts)} host records and {len(corrected)} prior identifications.")


if __name__ == "__main__":
    main()
