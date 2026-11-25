"""Check complete text members of the Chopard-Vilhem releases for exact identifiers."""
import argparse
import csv
import hashlib
import json
import re
import zipfile
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEXT = {".csv", ".json", ".jsonl", ".tsv", ".txt", ".md", ".tex", ".ecsv", ".html"}


def main(archives):
    with (HERE.parent / "roster.csv").open() as stream:
        roster = list(csv.DictReader(stream))
    roster.append({"tic": "257808672", "gaia_dr3": "1786928913098116864"})
    ids = {r[key]: r["tic"] for r in roster for key in ("gaia_dr3", "tic")}
    token = re.compile(rb"(?<![0-9])[0-9]{6,20}(?![0-9])")
    manifests, records = [], []
    for path in archives:
        with zipfile.ZipFile(path) as archive:
            names = [n for n in archive.namelist() if Path(n).suffix.lower() in TEXT]
            manifests.append(dict(archive=path.name,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),text_members=len(names)))
            for name in names:
                found = defaultdict(set)
                raw = archive.read(name)
                for m in token.finditer(raw):
                    code = m[0].decode()
                    if code in ids:
                        found[ids[code]].add(code)
                for tic, codes in found.items():
                    records.append(dict(tic=tic,archive=path.name,member=name,identifiers="|".join(sorted(codes))))
    (HERE / "survey-archives.json").write_text(json.dumps(manifests,indent=2)+"\n")
    with (HERE/"survey-archive-matches.csv").open("w",newline="",encoding="utf8") as out:
        writer=csv.DictWriter(out,fieldnames=["tic","archive","member","identifiers"],lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archives",nargs="+",type=Path)
    main(parser.parse_args().archives)
