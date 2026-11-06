r"""Read every fetched e-print (untrusted: latin-1, read-only, run with
python -I) and look for any of the claim set's identifiers:
  * Gaia DR3 source ids (18-19 digits, unambiguous), and
  * TIC ids, either as "TIC <id>" / "TIC<id>" / "TIC-<id>" or, for ids of
    eight digits or more, bare.
For each hit prints the paper, the member file, the identifier, our label if
any, and 160 characters of context. Writes grep-out.txt beside this file.
    python -I grep_sources.py <srcdir> [--extra <file.json>]
--extra adds claims beyond the run's 802: a JSON object keyed by TIC with
"source_id" (Gaia DR3) and "label" (shown beside hits), e.g. Astra's new
additions in extra-astra-1104.json. The output file is then grep-out-<stem>.txt.
"""
import gzip, io, json, os, re, sys, tarfile

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(sys.argv[1], "eprints")
C = json.load(open(os.path.join(HERE, "claims.json")))
cites = json.load(open(os.path.join(HERE, "cites.json"), encoding="utf-8"))
by_arx = {e["arxiv"]: e for e in cites.values() if e.get("arxiv")}
labels = C["labels"]
tic_of_gaia = {v["source_id"]: t for t, v in C.get("gaia", {}).items()}
OUTNAME = "grep-out.txt"
if "--extra" in sys.argv:
    xpath = sys.argv[sys.argv.index("--extra") + 1]
    extra = json.load(open(xpath, encoding="utf-8"))
    for t, v in extra.items():
        if t not in C["claims"]:
            C["claims"].append(t)
        if v.get("source_id"):
            tic_of_gaia[v["source_id"]] = t
        labels[t] = v.get("label", "extra")
    OUTNAME = "grep-out-" + os.path.splitext(os.path.basename(xpath))[0] + ".txt"
    print(f"extra claims: {len(extra)} from {os.path.basename(xpath)}")
gaia_re = re.compile(r"\b(" + "|".join(sorted(tic_of_gaia, key=len, reverse=True)) + r")\b") if tic_of_gaia else None
tics = sorted(C["claims"], key=len, reverse=True)
tic_ctx = re.compile(r"TIC[\s\-_~]*(?:\\,|\\ |&)?(" + "|".join(tics) + r")\b")
tic_bare = re.compile(r"(?<![\d.])(" + "|".join(t for t in tics if len(t) >= 8) + r")(?![\d.])")
out = open(os.path.join(HERE, OUTNAME), "w", encoding="utf-8")


def say(s=""):
    print(s, flush=True); out.write(s + "\n")


def texts_of(path):
    raw = open(path, "rb").read()
    t = {}
    try:
        tf = tarfile.open(fileobj=io.BytesIO(raw), mode="r:*")
        for m in tf.getmembers():
            if m.isfile() and not re.search(r"\.(png|jpe?g|pdf|eps|ps|gif|fits|npy|pkl|bst|cls|sty|synctex(\.gz)?|aux|log|out)$", m.name, re.I):
                t[m.name] = tf.extractfile(m).read().decode("latin-1")
    except Exception:
        try:
            t["main"] = gzip.decompress(raw).decode("latin-1")
        except Exception:
            t["main"] = raw.decode("latin-1")
    return t


files = sorted(f for f in os.listdir(SRC) if f.endswith(".src"))
say(f"{len(files)} e-prints, {len(tics)} TICs, {len(tic_of_gaia)} Gaia ids")
papers_hit, nhits, nchars = 0, 0, 0
for f in files:
    aid = f[:-4].replace("_", "/")
    meta = by_arx.get(aid, {})
    hits = []
    for name, txt in texts_of(os.path.join(SRC, f)).items():
        nchars += len(txt)
        for m in tic_ctx.finditer(txt):
            hits.append(("TIC", m.group(1), name, txt[max(0, m.start() - 80):m.end() + 80]))
        for m in tic_bare.finditer(txt):
            if not tic_ctx.search(txt[max(0, m.start() - 12):m.end()]):
                hits.append(("bare", m.group(1), name, txt[max(0, m.start() - 80):m.end() + 80]))
        if gaia_re:
            for m in gaia_re.finditer(txt):
                hits.append(("Gaia", tic_of_gaia[m.group(1)], name, txt[max(0, m.start() - 80):m.end() + 80]))
    if hits:
        papers_hit += 1
        say(f"\n## {aid}  {meta.get('year','')}  {meta.get('title','')[:100]}")
        seen = set()
        for kind, t, name, ctx in hits:
            key = (kind, t, name)
            if key in seen:
                continue
            seen.add(key); nhits += 1
            say(f"  [{kind}] TIC {t}{' = ' + labels[t] if t in labels else ''}  ({name}): "
                + re.sub(r"\s+", " ", ctx).strip())
say(f"\n{papers_hit} papers with hits, {nhits} distinct (kind, id, file) hits, {nchars/1e6:.0f} Mchars read")
out.close()
