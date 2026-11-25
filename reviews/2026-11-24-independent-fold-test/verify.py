"""Reconstruct the masked pilot draw and check every published result using the Python standard library."""
import csv, hashlib, io, json, sys, zipfile
from pathlib import Path
D=Path(__file__).resolve().parent
def table(name):
    with (D/name).open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def key(t):
    return hashlib.sha256(("Fable-independent-pilot-20261124/"+t).encode()).hexdigest()
def verify():
    eligible=table("eligible.csv");order=sorted(eligible,key=lambda r:key(r["tic"]));selected=[];used=set()
    for r in order:
        assert (r["flag"]=="1")== (float(r["paired_bin_depth_ppt"])>=10 and float(r["paired_bin_depth_ppt"])>=5*max(1,float(r["depth_ppt"])))
    for r in (x for x in order if x["flag"]=="1"):
        controls=[x for x in order if x["flag"]=="0" and x["stream"]==r["stream"] and x["tic"] not in used]
        if not controls:continue
        control=min(controls,key=lambda x:(abs(x["sectors"].count("|")-r["sectors"].count("|")),key(x["tic"])))
        selected.extend([r,control]);used.add(control["tic"])
        if len(selected)>=10:break
    assert selected==table("assignments.csv")
    tics={r["tic"] for r in selected}
    assert len(selected)==len(tics)==10
    batch=table("batch.csv")
    assert [r["tic"] for r in batch]==sorted(tics,key=int)
    assert all(set(r)=={"tic","stream","sectors","ra_deg","dec_deg"} for r in batch)
    final=table("outcomes.csv")
    assert len(final)==len(tics) and {r["tic"] for r in final}==tics
    decision={r["tic"]:r for r in final}
    for r in selected:assert r["flag"]==decision[r["tic"]]["flag"]
    for r in final:assert int(r["endpoint"])==int(r["numerical_positive"]=="1" and r["visual_positive"]=="1")
    extension=table("ffi/outcomes.csv"); expected={r["tic"]:r["flag"] for r in eligible if r["stream"]=="ffi"}
    assert len(extension)==len(expected)==13 and not(tics & set(expected))
    assert {r["tic"]:r["flag"] for r in extension}==expected
    assert {r["tic"] for r in table("ffi/batch.csv")}==set(expected)
    for r in extension:assert int(r["endpoint"])==int(r["numerical_positive"]=="1" and r["visual_positive"]=="1")
    return [[sum(int(r["endpoint"]) for r in sample if r["flag"]==group) for group in ("1","0")] for sample in (final,extension)]
def verify_inputs():
    import numpy as np
    with zipfile.ZipFile(D/"original-folds.zip") as z:
        for r in table("eligible.csv"):
            t=r["tic"];s=z.read(t+".json");f=z.read(t+"_fold.npz")
            assert hashlib.sha256(s).hexdigest()==r["measurement_sha256"] and hashlib.sha256(f).hexdigest()==r["fold_sha256"]
            assert json.loads(s)["depth_lc_ppt"]==float(r["depth_ppt"])
            with np.load(io.BytesIO(f)) as data:
                flux=data["fold"];loss=1000*(1-flux/np.nanmedian(flux))
                assert np.isclose(np.nanmax(np.minimum(loss,np.roll(loss,-1))),float(r["paired_bin_depth_ppt"]))
if __name__=="__main__":
    print("Verified matched pilot and full-frame extension. Flagged and comparison positives:",verify())
    if "--inputs" in sys.argv:verify_inputs();print("Verified original folds and depth measurements.")
