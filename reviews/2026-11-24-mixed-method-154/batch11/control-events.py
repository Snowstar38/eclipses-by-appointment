"""Select one archival window and up to one two-product comparison per TIC."""
import argparse
from pathlib import Path

from review import read_csv, write_csv


def event(row):
    return {key: row[key] for key in ("tic","sector","camera","center","width")}


def choose(batch):
    targets=read_csv(batch/"batch.csv")
    archive=read_csv(batch/"archive-windows.csv")
    independent=read_csv(batch/"independent-scan.csv")
    rows=[]
    for target in targets:
        tic=target["tic"]
        sign=-1 if "bright" in target["priority_group"].lower() else 1
        flags=[r for r in archive if r["tic"]==tic and r["archive_flag"]=="True"]
        if not flags:
            continue
        nominal=min(flags,key=lambda r: abs(float(r["center"])-float(target["best_window_btjd"])))
        rows.append(event(nominal))
        candidates=[r for r in independent if r["tic"]==tic and float(r["fraction"])>=.65
                    and abs(float(r["center"])-float(nominal["center"]))>max(.2,float(r["width"]))]
        def score(row):
            return min(float(row["sap_ppt"])*sign,float(row["corrected_ppt"])*sign)
        if candidates:
            second=max(candidates,key=score)
            if score(second)>2:
                rows.append(event(second))
    write_csv(batch/"control-events.csv",rows)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--batch",type=Path,required=True)
    choose(parser.parse_args().batch)
