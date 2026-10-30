# catcheck_c2.py - independent adversarial catalogue check for 35 TESS EB candidates.
# Fresh code: queries VizieR (asu-tsv cone interface) and SIMBAD TAP directly via urllib.
# Does NOT import or reuse anything from the sb1-scale pipeline.
import json
import os
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CAND_FILE = os.path.join(HERE, "CANDIDATES.json")
RAW_FILE = os.path.join(HERE, "catcheck-c2-out.txt")
VERDICT_FILE = os.path.join(HERE, "VERDICTS-cat.md")

VIZIER_TSV = "https://vizier.cds.unistra.fr/viz-bin/asu-tsv"
SIMBAD_TAP = "https://simbad.cds.unistra.fr/simbad/sim-tap/sync"

EB_TABLES_VETTED = [
    ("J/ApJS/258/16/tess-ebs", "Prsa TESS-EB"),
    ("J/A+A/691/A242/obaf-eb1", "IJspeert OBAF"),
    ("J/ApJS/279/50/table3", "Kostov t3"),
    ("J/ApJS/279/50/table4", "Kostov t4"),
]
EB_TABLE_UNVETTED = ("J/ApJS/279/50/table2", "Kostov t2 (unvetted ML)")

raw_fh = open(RAW_FILE, "w", encoding="utf-8")


def log(s):
    raw_fh.write(s + "\n")
    raw_fh.flush()


def http_get(url, params, timeout=150, tries=2):
    qs = urllib.parse.urlencode(params)
    full = url + "?" + qs
    last_err = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(full, headers={"User-Agent": "catcheck-c2 (independent check)"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001
            last_err = e
            log(f"### HTTP attempt {attempt+1} failed for {full}\n### {e!r}")
            time.sleep(15)
    raise RuntimeError(f"HTTP failed after {tries} tries: {full} : {last_err!r}")


def parse_asu_tsv(text):
    """Parse VizieR asu-tsv output -> (header, rows). Rows are lists of strings."""
    header = None
    rows = []
    state = 0  # 0 = before header, 1 = after header (skip units/dashes), 2 = data
    for ln in text.splitlines():
        if ln.startswith("#") or not ln.strip():
            if state == 2 and not ln.strip():
                state = 3  # blank line after data ends the block
            continue
        if state == 3:
            break
        if state == 0:
            header = [c.strip() for c in ln.split("\t")]
            state = 1
        elif state == 1:
            stripped = ln.replace("\t", "").strip()
            if stripped and set(stripped) <= set("-"):
                state = 2
            # otherwise it's a units line; skip
        else:
            rows.append([c.strip() for c in ln.split("\t")])
    return header, rows


def vizier_cone(source, ra, dec, rs_arcsec, out_cols=None, max_rows=20):
    params = {
        "-source": source,
        "-c": f"{ra:.6f} {dec:+.6f}",
        "-c.rs": str(rs_arcsec),
        "-out.add": "_r",
        "-sort": "_r",
        "-out.max": str(max_rows),
    }
    if out_cols:
        params["-out"] = out_cols
    txt = http_get(VIZIER_TSV, params)
    log(f"--- VizieR {source} cone ra={ra:.6f} dec={dec:+.6f} rs={rs_arcsec}\" ---")
    log(txt.rstrip())
    return parse_asu_tsv(txt)


def vizier_first_row_pos(source):
    """Fetch one arbitrary row of a table with computed J2000 position (table self-check)."""
    params = {
        "-source": source,
        "-out.add": "_RAJ2000,_DEJ2000",
        "-out.max": "1",
    }
    txt = http_get(VIZIER_TSV, params)
    log(f"--- VizieR {source} first-row fetch ---")
    log(txt.rstrip())
    header, rows = parse_asu_tsv(txt)
    if not header or not rows:
        return None
    try:
        i_ra = header.index("_RAJ2000")
        i_de = header.index("_DEJ2000")
    except ValueError:
        return None
    try:
        return float(rows[0][i_ra]), float(rows[0][i_de])
    except (ValueError, IndexError):
        return None


def simbad_cone(ra, dec, rs_arcsec=5.0):
    q = (
        "SELECT main_id, otype, ra, dec FROM basic WHERE "
        f"CONTAINS(POINT('ICRS', ra, dec), CIRCLE('ICRS', {ra:.6f}, {dec:.6f}, {rs_arcsec}/3600.0))=1"
    )
    params = {"request": "doQuery", "lang": "adql", "format": "json", "query": q}
    txt = http_get(SIMBAD_TAP, params)
    log(f"--- SIMBAD cone ra={ra:.6f} dec={dec:+.6f} rs={rs_arcsec}\" ---")
    log(txt.rstrip()[:2000])
    try:
        j = json.loads(txt)
    except json.JSONDecodeError:
        return []
    return j.get("data", [])


def col(header, rows, name):
    if not header or name not in header:
        return [None] * len(rows)
    i = header.index(name)
    out = []
    for r in rows:
        out.append(r[i] if i < len(r) else None)
    return out


def period_relation(p_claim, p_cat_str):
    """Return 'P'/'P/2'/'2P' if catalogue period matches claimed P, P/2 or 2P within 1%."""
    try:
        p_cat = float(p_cat_str)
    except (TypeError, ValueError):
        return None
    if p_cat <= 0:
        return None
    for mult, lbl in ((1.0, "P"), (0.5, "P/2"), (2.0, "2P")):
        ref = p_claim * mult
        if abs(p_cat - ref) / ref < 0.01:
            return lbl
    return None


ECLIPSING_VSX_PREFIXES = ("E", "EA", "EB", "EW", "EP", "ELL")  # ELL noted separately below


def vsx_type_is_eclipsing(t):
    if not t:
        return False
    # VSX types can be compound like "EA/RS" or "EW:" or "E"
    first = t.split("/")[0].split("+")[0].split("|")[0].strip().rstrip(":")
    return first in ("E", "EA", "EB", "EW", "EP") or first.startswith("EA") or first.startswith("EB") or first.startswith("EW")


SIMBAD_ECLIPSING = {"EB*", "EclBin", "Al*", "bL*", "WU*", "EB*Algol", "EB*betLyr", "EB*WUMa"}


def run_control():
    log("=" * 70)
    log("CONTROL: Algol (beta Per) ra=47.04221 dec=+40.95565")
    log("=" * 70)
    ok_vsx = False
    ok_eb = False
    header, rows = vizier_cone("B/vsx/vsx", 47.04221, 40.95565, 30, out_cols="Name,Type,Period")
    names = col(header, rows, "Name")
    types = col(header, rows, "Type")
    periods = col(header, rows, "Period")
    for n, t, p in zip(names, types, periods):
        log(f"CONTROL VSX hit: {n} type={t} P={p}")
        if t and vsx_type_is_eclipsing(t):
            ok_vsx = True
    time.sleep(1)
    for src, label in EB_TABLES_VETTED + [EB_TABLE_UNVETTED]:
        h, r = vizier_cone(src, 47.04221, 40.95565, 10)
        if r:
            log(f"CONTROL: Algol found in {label} ({src}), {len(r)} row(s)")
            ok_eb = True
        time.sleep(1)
    # Per-table self-cone check: fetch a row, cone it back. Validates cone geometry per table
    # even for tables that happen not to contain Algol.
    table_ok = {}
    for src, label in EB_TABLES_VETTED + [EB_TABLE_UNVETTED]:
        pos = vizier_first_row_pos(src)
        if pos is None:
            table_ok[src] = False
            log(f"CONTROL self-check: could not get a first row position from {src}")
        else:
            time.sleep(1)
            h, r = vizier_cone(src, pos[0], pos[1], 5)
            table_ok[src] = bool(r)
            log(f"CONTROL self-check {src}: cone back at own position -> {len(r) if r else 0} row(s)")
        time.sleep(1)
    sdata = simbad_cone(47.04221, 40.95565, 10)
    for row in sdata:
        log(f"CONTROL SIMBAD hit: {row}")
    ok_simbad = any(row[1] in SIMBAD_ECLIPSING or "EclBin" in str(row[1]) for row in sdata)
    log(f"CONTROL RESULT: vsx_eclipsing={ok_vsx} any_eb_table={ok_eb} simbad_ecl={ok_simbad} table_self={table_ok}")
    return ok_vsx, ok_eb, ok_simbad, table_ok


def check_candidate(c):
    tic = c["tic"]
    ra, dec, p_claim = c["ra"], c["dec"], c["P"]
    log("=" * 70)
    log(f"CANDIDATE TIC {tic} ra={ra:.6f} dec={dec:+.6f} P={p_claim:.6f} d depth={c['depth_ppm']} ppm group={c['group']}")
    log("=" * 70)
    res = {"tic": tic, "P": p_claim, "group": c["group"], "vsx": [], "eb_hits": [], "eb_unvetted": [],
           "simbad": [], "verdict": None, "notes": []}

    # 1. VSX at 30"
    header, rows = vizier_cone("B/vsx/vsx", ra, dec, 30, out_cols="Name,Type,Period")
    for n, t, p, r_ in zip(col(header, rows, "Name"), col(header, rows, "Type"),
                           col(header, rows, "Period"), col(header, rows, "_r")):
        rel = period_relation(p_claim, p)
        res["vsx"].append({"name": n, "type": t, "period": p, "sep": r_, "match": rel})
    time.sleep(1)

    # 2. Vetted EB tables at 5"
    for src, label in EB_TABLES_VETTED:
        h, r = vizier_cone(src, ra, dec, 5)
        if r:
            for row in r:
                res["eb_hits"].append({"table": label, "row": row, "header": h})
        time.sleep(1)
    # unvetted Kostov table2 - note only
    h, r = vizier_cone(EB_TABLE_UNVETTED[0], ra, dec, 5)
    if r:
        for row in r:
            res["eb_unvetted"].append({"table": EB_TABLE_UNVETTED[1], "row": row, "header": h})
    time.sleep(1)

    # 3. SIMBAD at 5"
    for row in simbad_cone(ra, dec, 5):
        res["simbad"].append({"main_id": row[0], "otype": row[1]})
    time.sleep(1)

    # Verdict logic
    demote = False
    mistyped = False
    neighbour = False
    if res["eb_hits"]:
        demote = True
        res["notes"].append("in vetted EB table(s): " + ", ".join(sorted({h_['table'] for h_ in res["eb_hits"]})))
    for v in res["vsx"]:
        ecl = vsx_type_is_eclipsing(v["type"])
        sep = None
        try:
            sep = float(v["sep"])
        except (TypeError, ValueError):
            pass
        if ecl and v["match"]:
            demote = True
            res["notes"].append(f"VSX {v['name']} ({v['type']}) P={v['period']} matches claimed ({v['match']})")
        elif ecl and not v["match"] and sep is not None and sep <= 15:
            demote = True
            res["notes"].append(f"VSX {v['name']} ({v['type']}) at {sep}\" is eclipsing but P={v['period']} does not match claimed - period differs, still catalogued as EB")
        elif (not ecl) and v["match"]:
            mistyped = True
            res["notes"].append(f"VSX {v['name']} typed {v['type']} with matching period {v['period']} ({v['match']}) - MIS-TYPED in VSX")
        elif sep is not None and sep > 15:
            neighbour = True
            res["notes"].append(f"VSX {v['name']} ({v['type']}, P={v['period']}) at {sep}\" - likely different star")
        else:
            neighbour = True
            res["notes"].append(f"VSX {v['name']} ({v['type']}, P={v['period']}) at {v['sep']}\" - unrelated period, no demote")
    simbad_ecl = [s for s in res["simbad"]
                  if s["otype"] in SIMBAD_ECLIPSING or "EclBin" in str(s["otype"]) or "EB*" in str(s["otype"])]
    if simbad_ecl:
        demote = True
        res["notes"].append("SIMBAD already types it eclipsing: " + "; ".join(f"{s['main_id']}={s['otype']}" for s in simbad_ecl))
    if res["eb_unvetted"]:
        res["notes"].append("also flagged in Kostov table2 (unvetted ML) - noted, not demoting on it")

    if demote:
        res["verdict"] = "ALREADY-CATALOGUED"
    elif mistyped:
        res["verdict"] = "MIS-TYPED"
    elif neighbour:
        res["verdict"] = "NEIGHBOUR-NOTE"
    else:
        res["verdict"] = "NOWHERE"
    log(f"VERDICT TIC {tic}: {res['verdict']} | " + " | ".join(res["notes"]) if res["notes"] else f"VERDICT TIC {tic}: {res['verdict']}")
    return res


def main():
    with open(CAND_FILE, encoding="utf-8") as f:
        cands = json.load(f)
    log(f"catcheck-c2: {len(cands)} candidates, started {time.strftime('%Y-%m-%d %H:%M:%S')}")

    ok_vsx, ok_eb, ok_simbad, table_ok = run_control()
    if not ok_vsx:
        log("FATAL: control failed - Algol not returned as eclipsing by VSX cone. Aborting.")
        print("CONTROL FAILED: VSX")
        sys.exit(2)
    if not ok_eb:
        log("FATAL: control failed - Algol not in any EB table cone. Aborting.")
        print("CONTROL FAILED: EB tables")
        sys.exit(2)
    bad_tables = [s for s, ok in table_ok.items() if not ok]
    if bad_tables:
        log(f"WARNING: self-cone failed for tables: {bad_tables} - their null results are not trustworthy")
    print(f"CONTROL OK (vsx={ok_vsx} eb={ok_eb} simbad={ok_simbad}); self-check failures: {bad_tables}")

    results = []
    for i, c in enumerate(cands):
        print(f"[{i+1}/{len(cands)}] TIC {c['tic']} ...", flush=True)
        try:
            results.append(check_candidate(c))
        except Exception as e:  # noqa: BLE001
            log(f"ERROR on TIC {c['tic']}: {e!r}")
            results.append({"tic": c["tic"], "P": c["P"], "group": c["group"], "vsx": [], "eb_hits": [],
                            "eb_unvetted": [], "simbad": [], "verdict": "ERROR", "notes": [repr(e)]})
        time.sleep(2)

    # Write verdict table
    with open(VERDICT_FILE, "w", encoding="utf-8") as f:
        f.write("# Independent catalogue check (c2) - 35 TESS EB candidates\n\n")
        f.write(f"Run {time.strftime('%Y-%m-%d %H:%M')} by an independent checker (fresh code, no pipeline reuse).\n\n")
        f.write("Cones: VSX 30\", vetted EB tables (Prsa J/ApJS/258/16, IJspeert J/A+A/691/A242, Kostov J/ApJS/279/50 t3+t4) 5\", SIMBAD 5\". ")
        f.write(f"Control: Algol returned by VSX (EA, P~2.867) and EB tables; per-table self-cone checks in raw log; self-check failures: {bad_tables if bad_tables else 'none'}.\n\n")
        f.write("| TIC | claimed P (d) | VSX (30\") | vetted EB tables (5\") | SIMBAD otype (5\") | verdict | notes |\n")
        f.write("|---|---|---|---|---|---|---|\n")
        for r in results:
            vsx_s = "; ".join(f"{v['name']} {v['type']} P={v['period']} @{v['sep']}\"" for v in r["vsx"]) or "none"
            eb_s = "; ".join(sorted({h_["table"] for h_ in r["eb_hits"]})) or "none"
            if r["eb_unvetted"]:
                eb_s += " (+Kostov t2 unvetted)"
            sim_s = "; ".join(f"{s['main_id']}={s['otype']}" for s in r["simbad"]) or "none"
            notes = " / ".join(r["notes"]) or ""
            f.write(f"| {r['tic']} | {r['P']:.5f} | {vsx_s} | {eb_s} | {sim_s} | **{r['verdict']}** | {notes} |\n")
        f.write("\n## Summary\n\n")
        from collections import Counter
        cnt = Counter(r["verdict"] for r in results)
        for k in ("NOWHERE", "NEIGHBOUR-NOTE", "MIS-TYPED", "ALREADY-CATALOGUED", "ERROR"):
            if cnt.get(k):
                f.write(f"- {k}: {cnt[k]}\n")
        demoted = [r["tic"] for r in results if r["verdict"] == "ALREADY-CATALOGUED"]
        f.write("\nAlready catalogued as EB: " + (", ".join("TIC " + t for t in demoted) if demoted else "none") + "\n")

    with open(os.path.join(HERE, "catcheck-c2-results.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=1)
    print("DONE. Verdicts in", VERDICT_FILE)


if __name__ == "__main__":
    main()
    raw_fh.close()
