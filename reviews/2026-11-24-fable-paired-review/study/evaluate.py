"""Evaluate frozen rankings against the dated per-aperture adjudications."""
import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ORDERS = {"Fable":"fable_rank", "Existing priority":"queue_rank", "Source and clock":"source_clock_rank"}
ENDPOINTS = {"accepted_confirmed","accepted_probable","identified_prior_eclipse","ruled_out","unresolved","insufficient"}
FLAGS = ["clock_agrees","repeated_events","narrow_with_alternation_or_secondary","zero_capable_neighbours",
         "saved_photometry_cut","prior_position_and_period_clear","stream","source_clock_score"]

def read(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))

def write(path, rows):
    with path.open("w",encoding="utf8",newline="") as stream:
        w=csv.DictWriter(stream,fieldnames=rows[0],lineterminator="\n")
        w.writeheader();w.writerows(rows)

def wilson(k,n):
    if not n:return ("","")
    z=1.959963984540054
    center=(k+z*z/2)/(n+z*z);half=z*math.sqrt(k*(n-k)/n+z*z/4)/(n+z*z)
    return round(max(0,center-half),5),round(min(1,center+half),5)

def counts(group):
    n=len(group)
    k=sum(r["addition_credit"] for r in group);confirmed=sum(r["confirmed_credit"] for r in group)
    unresolved=sum(r["endpoint"] in {"unresolved","insufficient"} for r in group)
    lo,hi=wilson(k,n)
    return dict(n=n,accepted_unique=k,confirmed_unique=confirmed,
        probable_unique=k-confirmed,identified_prior_apertures=sum(r["endpoint"]=="identified_prior_eclipse" for r in group),
        physically_identified_apertures=sum(r["endpoint"] in {"accepted_confirmed","accepted_probable","identified_prior_eclipse"} for r in group),
        ruled_out=sum(r["endpoint"]=="ruled_out" for r in group),unresolved=sum(r["endpoint"]=="unresolved" for r in group),
        insufficient=sum(r["endpoint"]=="insufficient" for r in group),extra_followup=sum(r["extra_followup"]=="True" for r in group),
        addition_fraction=round(k/n,5),yield_wilson_lo=lo,yield_wilson_hi=hi,unresolved_upper_bound=round((k+unresolved)/n,5))

def evaluate(endpoints, dest, features=HERE/"frozen-features.csv"):
    expected="e3f0bed40427fd46be89f971beb9976e3d3cf8ed9b6d755ba663ee8c323f24a7"
    assert hashlib.sha256(features.read_bytes()).hexdigest()==expected, "Frozen preliminary features differ from the registered snapshot"
    frozen=read(features);decisions=read(endpoints)
    assert len(frozen)==len(decisions)==len({r["tic"] for r in decisions})==402
    assert {r["tic"] for r in frozen}=={r["tic"] for r in decisions}
    by_tic={r["tic"]:r for r in decisions}
    assert set(r["endpoint"] for r in decisions)<=ENDPOINTS
    assert set(r["extra_followup"] for r in decisions)<={"True","False"}
    for r in decisions:
        assert (r["endpoint"] in {"accepted_confirmed","accepted_probable"}) == bool(r.get("accepted_host_id"))
        assert r.get("source_decision","").strip()
    assigned=set()
    for r in sorted(frozen,key=lambda x:int(x["tic"])):
        final=by_tic[r["tic"]];r.update(final)
        host=final.get("accepted_host_id") or ""
        r["addition_credit"]=bool(host and host not in assigned)
        r["confirmed_credit"]=r["addition_credit"] and r["endpoint"]=="accepted_confirmed"
        if host:assigned.add(host)
    if dest:dest.mkdir(parents=True,exist_ok=True)
    yield_rows=[];curves=[]
    for lane in ["all","2min","ffi"]:
        cohort=[r for r in frozen if lane=="all" or r["stream"]==lane]
        total=counts(cohort)
        for name,col in ORDERS.items():
            ordered=sorted(cohort,key=lambda r:int(r[col]))
            for nall in [23,100,402]:
                k=math.floor(nall*len(cohort)/402+.5)
                selected=counts(ordered[:k])
                yield_rows.append(dict(stream=lane,order=name,budget_all_lanes=nall,**selected,
                    accepted_recall=round(selected["accepted_unique"]/total["accepted_unique"],5) if total["accepted_unique"] else "",
                    confirmed_recall=round(selected["confirmed_unique"]/total["confirmed_unique"],5) if total["confirmed_unique"] else "",
                    expected_random_additions=round(k*total["accepted_unique"]/len(cohort),3)))
            if lane=="all":
                hits=confirmed=prior=holds=0
                for i,r in enumerate(ordered,1):
                    hits+=r["addition_credit"];confirmed+=r["confirmed_credit"]
                    prior+=r["endpoint"]=="identified_prior_eclipse";holds+=r["endpoint"] in {"insufficient","unresolved"}
                    curves.append(dict(order=name,review_count=i,cumulative_additions=hits,cumulative_confirmed=confirmed,
                        cumulative_prior_eclipse_apertures=prior,cumulative_unresolved_or_insufficient=holds,
                        expected_random_additions=round(i*total["accepted_unique"]/len(cohort),4)))
    factor_rows=[dict(feature="whole_cohort",value="all",**counts(frozen))]
    for flag in FLAGS:
        values=sorted({r[flag] for r in frozen})
        for value in values:
            sub=[r for r in frozen if r[flag]==value]
            factor_rows.append(dict(feature=flag,value=value,**counts(sub)))
    by_lane=[]
    for lane in ["2min","ffi"]:
        local=[r for r in frozen if r["stream"]==lane]
        for flag in [f for f in FLAGS if f!="stream"]:
            for value in sorted({r[flag] for r in local}):
                by_lane.append(dict(stream=lane,feature=flag,value=value,
                    **counts([r for r in local if r[flag]==value])))
    write(dest/"feature-yield-by-stream.csv",by_lane)
    write(dest/"review-budget-yield.csv",yield_rows)
    write(dest/"feature-yield.csv",factor_rows)
    write(dest/"cumulative-yield.csv",curves)
    return frozen, yield_rows,factor_rows

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("endpoints",type=Path)
    parser.add_argument("--out",type=Path,default=HERE)
    parser.add_argument("--features",type=Path,default=HERE/"frozen-features.csv")
    args=parser.parse_args()
    assert hashlib.sha256(args.features.read_bytes()).hexdigest()=="e3f0bed40427fd46be89f971beb9976e3d3cf8ed9b6d755ba663ee8c323f24a7"
    r,b,f=evaluate(args.endpoints,args.out,args.features)
    print("Joined all",len(r),"frozen TICs;",counts(r))
if __name__=="__main__":main()
