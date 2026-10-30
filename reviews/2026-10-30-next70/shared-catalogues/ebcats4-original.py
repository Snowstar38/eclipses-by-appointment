"""Run the ebcats vetted-table battery over c4-montage.json, resumable.
Appends to c4-ebcats-out.txt here; skips tics already in it. Output format
identical to ebcats.py/ebcats2.py. Retries each table query 3x with backoff."""
import json, os, re, sys, time, urllib.request, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(os.environ["TEMP"], "hunt-sb1-scale")
TG = json.load(open(os.path.join(D, "targets.json")))
TABS = ["J/ApJS/279/50/table2", "J/ApJS/279/50/table3", "J/ApJS/279/50/table4",
        "J/A+A/691/A242/obaf-eb1", "J/ApJS/258/16/tess-ebs"]

OUT = os.path.join(HERE, "c4-ebcats-out.txt")
done = set()
if os.path.exists(OUT):
    done = {l.split(" | ")[0].strip() for l in open(OUT) if " | " in l}
todo = [t for t in json.load(open(os.path.join(HERE, "c4-montage.json"))) if t not in done]
print(f"{len(todo)} to query ({len(done)} already done)", flush=True)

def cone(tb, ra, de):
    u = "https://vizier.cds.unistra.fr/viz-bin/asu-tsv?" + urllib.parse.urlencode(
        {"-source": tb, "-c": f"{ra} {de}", "-c.rs": 5, "-out.max": 2, "-out.all": "", "-out.add": "_r"})
    for attempt in range(3):
        try:
            return [l for l in urllib.request.urlopen(u, timeout=120).read().decode("latin-1").splitlines()
                    if l and not l.startswith("#")]
        except Exception:
            if attempt == 2: raise
            time.sleep(10 * (attempt + 1))

with open(OUT, "a") as fo:
    for i, tic in enumerate(todo):
        tg = TG[tic]; out = []
        try:
            for tb in TABS:
                rows = cone(tb, tg["ra"], tg["dec"])
                if len(rows) > 2:
                    hdr = rows[0].split("\t"); v = dict(zip(hdr, rows[3 if len(rows) > 3 else 2].split("\t")))
                    keep = {k: v[k].strip() for k in v if re.match(r"(_r|TIC|Per|P$|Period|period)", k)}
                    out.append(f"{tb.split('/')[-1]} {keep}")
            fo.write(f"{tic} | {' ; '.join(out) or 'none of the vetted/unvetted EB tables'}\n"); fo.flush()
        except Exception as ex:
            fo.write(f"{tic} | BATTERY FAILED {repr(ex)[:60]}\n"); fo.flush()
        if i % 25 == 0: print(i, flush=True)
        time.sleep(0.3)
print("battery done", flush=True)
