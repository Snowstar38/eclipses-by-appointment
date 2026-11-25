"""Join the masked reviewers' tables to the saved flags after both readings are locked."""
import csv,json
from pathlib import Path
D=Path(__file__).resolve().parent
def rows(path):
    with path.open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def compile_one(folder,eligible):
    batch=rows(folder/"batch.csv")
    reviewers=[{r["tic"]:r for r in rows(folder/n/"assessment.csv")} for n in ("sol","terra")]
    assert all(set(index)=={r["tic"] for r in batch} for index in reviewers)
    result=[]
    for row in batch:
        t=row["tic"];n,v=[index[t] for index in reviewers]
        assert all(r["endpoint"].lower() in {"yes","no","uncertain","single"} for r in (n,v))
        a,b=(int(r["endpoint"].lower()=="yes") for r in (n,v))
        result.append(dict(**row,flag=eligible[t]["flag"],numerical_positive=a,visual_positive=b,endpoint=int(a and b),
                    numerical_status=n["endpoint"],visual_status=v["endpoint"],numerical_note=n["assessment"],visual_note=v.get("assessment") or v["assessment notes"]))
    with (folder/"outcomes.csv").open("w",encoding="utf8",newline="") as f:
        w=csv.DictWriter(f,result[0],lineterminator="\n");w.writeheader();w.writerows(result)
    return result
def main():
    eligible={r["tic"]:r for r in rows(D/"eligible.csv")}
    datasets=[compile_one(d,eligible) for d in (D,D/"ffi")]
    for cohort in datasets:
        print([(sum(r["endpoint"] for r in cohort if r["flag"]==flag),sum(r["flag"]==flag for r in cohort)) for flag in ("1","0")])
if __name__=="__main__":main()
