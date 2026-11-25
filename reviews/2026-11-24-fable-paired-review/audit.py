"""Verify cohort, input hashes, plotted reviews, accepted hosts and frozen-ranking yields offline."""
import csv, hashlib, json
from collections import Counter
from pathlib import Path

def table(path):
    with path.open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def check(base):
    base=Path(base); cohort=table(base/"batches.csv"); decisions=table(base/"adjudications.csv")
    frozen=table(base/"study/frozen-features.csv");hosts=table(base/"host-stars.csv")
    tics=[r["tic"] for r in cohort]
    assert len(set(tics))==len(tics)==402 and [r["tic"] for r in decisions]==tics
    assert set(tics)=={r["tic"] for r in frozen}
    inputs=json.loads((base/"study/feature-manifest.json").read_bytes())["files"]
    for k,v in inputs.items():
        path=base/k if k=="batches.csv" else base/("fable-inputs" if k.startswith("candidates") else "study")/k
        assert digest(path)==v,k
    for r in frozen:
        assert digest(base/"fable-inputs/validate"/(r["tic"]+".json"))==r["fable_measurement_sha256"]
    for i,r in enumerate(decisions):
        assert (int(r["batch"]),int(r["slot"]))==(i//10+1,i%10+1)
        assert all((base/"terra"/x.strip()).is_file() for x in r["visual_panels"].split(";")), r["tic"]
        assert all((base/folder/(r["tic"]+".json")).is_file() for folder in ("pixels","sol/objects"))
    assert {r["accepted_host_id"] for r in decisions if r["accepted_host_id"]}=={r["gaia_dr3"] for r in hosts}
    assert len(hosts)==len({h["tic"] for h in hosts})
    for h in hosts:
        evidence=json.loads((base/h["evidence"]).read_bytes())
        assert str(evidence["tic"])==h["tic"] and str(evidence["gaia_dr3"])==h["gaia_dr3"]
        assert abs(float(h["period_days"])-float(evidence["host"]["period_days"]))<1e-7
    verdict={r["tic"]:r for r in decisions}
    for row in table(base/"study/review-budget-yield.csv"):
        if row["stream"]!="all":continue
        sortkey={"Fable":"fable_rank","Existing priority":"queue_rank","Source and clock":"source_clock_rank"}[row["order"]]
        part=sorted(frozen,key=lambda r:int(r[sortkey]))[:int(row["n"])]
        assert len({verdict[t["tic"]]["accepted_host_id"] for t in part if verdict[t["tic"]]["accepted_host_id"]})==int(row["accepted_unique"])
    receipt=json.loads((base/"study/analysis-receipt.json").read_bytes())
    assert digest(base/"adjudications.csv")==receipt["decisions_sha256"]
    for name,v in receipt["results"].items():assert digest(base/"study"/name)==v,name
    return Counter(r["endpoint"] for r in decisions)

if __name__=="__main__":print("Verified 402 paired reviews",dict(check(Path(__file__).resolve().parent)))
