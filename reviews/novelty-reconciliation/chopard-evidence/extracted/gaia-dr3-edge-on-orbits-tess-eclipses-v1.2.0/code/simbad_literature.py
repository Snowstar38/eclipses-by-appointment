#!/usr/bin/env python3
"""Literature of the candidates from SIMBAD, found by their Gaia DR3 identifier (robust to proper motion and to the
epoch of the coordinates). For each star: SIMBAD main identifier and object type, every reference with its year and
title, the titles that mention eclipses, transits or binarity marked with '*'.
Run from ~/Desktop/piste3:   python3 simbad_literature.py 146197633037335168 1364450812894866688 ...
Output: vetting/literature.txt and vetting/literature_summary.csv"""
import os, re, sys, time
import pandas as pd
from astroquery.simbad import Simbad

WORDS = re.compile(r"eclips|transit|binar|light.?curve|photometr|variab", re.I)


def one(sid):
    q = f"""SELECT b.main_id, b.otype, r.bibcode, r."year", r.title
            FROM ident AS i JOIN basic AS b ON b.oid = i.oidref
            LEFT JOIN has_ref AS h ON h.oidref = b.oid LEFT JOIN ref AS r ON r.oidbib = h.oidbibref
            WHERE i.id = 'Gaia DR3 {sid}'"""
    return Simbad.query_tap(q).to_pandas()


def main():
    ids = [int(x) for x in sys.argv[1:]]
    os.makedirs("vetting", exist_ok=True)
    lines, rows = [], []
    for sid in ids:
        try:
            t = one(sid)
        except Exception as exc:
            print(f"Gaia DR3 {sid}: SIMBAD query failed ({str(exc)[:120]})"); lines.append(f"== Gaia DR3 {sid}: query failed"); continue
        if t.empty:
            print(f"Gaia DR3 {sid}: not in SIMBAD"); lines.append(f"== Gaia DR3 {sid}: not in SIMBAD"); continue
        name, otype = str(t["main_id"].iloc[0]), str(t["otype"].iloc[0])
        refs = t.dropna(subset=["bibcode"]).sort_values("year")
        hits = refs[refs["title"].fillna("").str.contains(WORDS)]
        lines.append(f"== Gaia DR3 {sid} = {name} [{otype}], {len(refs)} references, {len(hits)} with eclipse/transit/binary/variability words")
        for r in refs.itertuples():
            mark = "*" if WORDS.search(str(r.title or "")) else " "
            lines.append(f"   {mark} {int(r.year) if r.year == r.year else '????'} {r.bibcode}  {r.title}")
        rows.append(dict(source_id=sid, simbad=name, otype=otype, n_refs=len(refs), n_refs_keywords=len(hits)))
        print(f"Gaia DR3 {sid} = {name} [{otype}]: {len(refs)} references ({len(hits)} with keywords)", flush=True)
        time.sleep(0.5)
    open("vetting/literature.txt", "w").write("\n".join(lines) + "\n")
    pd.DataFrame(rows).to_csv("vetting/literature_summary.csv", index=False)
    print("-> vetting/literature.txt, vetting/literature_summary.csv")


if __name__ == "__main__":
    main()
