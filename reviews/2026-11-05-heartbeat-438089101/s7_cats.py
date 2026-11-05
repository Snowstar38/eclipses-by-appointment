"""Step 7: catalogues and literature, CDS-outage edition.
 (a) VizieR NAMED tables on the IDIA mirror (vizier.idia.ac.za, asu-tsv), each with a positive control (Algol for the
     all-sky tables; the table's own first row for the TESS EB/heartbeat tables), and the CatalogsExamined header
     checked so a misnamed table cannot silently search everything.
 (b) VSX through the AAVSO API (Algol control), 3.5-s pacing, browser UA.
 (c) Gaia DR3 vari tables via ESA TAP for the target id.
 (d) the nine cached heartbeat-paper arXiv sources (read-only, latin-1, untrusted data): TIC, Gaia, TYC, 2MASS ids,
     decimal and sexagesimal RA/Dec stems; positive control per paper = re-finding the first TIC id it lists.
 (e) SIMBAD: CDS is down; one attempt on the CfA mirror only.
Writes s7_out.txt."""
import os, re, io, tarfile, gzip, json, time, math, urllib.request, urllib.parse
from lib import *

say = say_to(open(os.path.join(OUT, "s7_out.txt"), "w"))
MIR = "https://vizier.idia.ac.za/viz-bin/asu-tsv"
ALGOL = (47.04221855, 40.95564667)
MIR = "https://vizier.idia.ac.za/viz-bin/votable"
def asu(src, ra, de, r_as, maxn=50, extra=None):
    """POST to the mirror's votable endpoint (the route the house uses). Returns (examined tables, table names,
    [(fieldnames, row)], nbytes). A misnamed table returns no <TABLE>, so it cannot silently become a catch-all."""
    p = {"-source": src, "-c": f"{ra} {de}", "-c.rs": r_as, "-out.max": maxn, "-out.add": "_r", "-sort": "_r"}
    if ra is None: p = {"-source": src, "-out.max": 1}
    txt = urllib.request.urlopen(urllib.request.Request(MIR, urllib.parse.urlencode(p).encode(), headers=UA),
                                 timeout=180).read().decode("utf-8", "replace")
    tabs = re.findall(r'<TABLE[^>]*name="([^"]+)"', txt)
    body = []
    for tb in re.findall(r"<TABLE.*?</TABLE>", txt, re.S):
        fields = re.findall(r'<FIELD[^>]*name="([^"]+)"', tb)
        for tr in re.findall(r"<TR>(.*?)</TR>", tb, re.S):
            body.append((fields, [re.sub(r"<.*?>", "", x).strip() for x in re.findall(r"<TD[^>]*>(.*?)</TD>|<TD/>", tr)]))
    return [str(len(tabs))], tabs, body, len(txt)

TABLES = [("B/vsx/vsx", "VSX", "algol", 30), ("II/366/catalog", "ASAS-SN variables", "algol", 30),
          ("B/sb9/main", "SB9", "algol", 30), ("B/wds/wds", "WDS", "algol", 30),
          ("J/ApJS/258/16/tess-ebs", "Prsa+2022 TESS EBs", "first", 30),
          ("J/A+A/691/A242/obaf-eb1", "IJspeert+2024 OBAF EBs", "first", 30),
          ("J/ApJS/279/50/table2", "Kostov+2025 t2", "first", 30), ("J/ApJS/279/50/table3", "Kostov+2025 t3", "first", 30),
          ("J/ApJS/279/50/table4", "Kostov+2025 t4", "first", 30),
          ("J/ApJS/276/17", "Solanki+2024/25 heartbeat tables (all tables of the catalogue)", "first", 30),
          ("J/AJ/151/68", "Kirk+2016 Kepler EB/HB", "first", 30), ("J/ApJ/829/34", "Shporer+2016 HB", "first", 30),
          ("J/ApJS/259/16", "Wrona+2022 OGLE HB", "first", 30),
          ("I/355/vari", "Gaia DR3 vari_summary (VizieR)", "first", 30), ("J/A+A/674/A16", "Gaia DR3 vari EB (Mowlavi+2023)", "first", 30)]
for src, name, ctl, r in TABLES:
    try:
        ex, tabs, body, n = asu(src, RA, DEC, r)
        s = f"{name} [{src}]: CatalogsExamined {ex or '?'} tables {tabs[:6]}; target cone {r}\": {len(body)} rows ({n} bytes)"
        for hdr, row in body[:5]:
            s += "\n      " + " | ".join(f"{h}={v}" for h, v in list(zip(hdr, row))[:8])
        say(s)
        if ctl == "algol":
            ex2, tabs2, body2, _ = asu(src, *ALGOL, 30)
            say(f"   control Algol: {len(body2)} rows; first: " + (" | ".join(body2[0][1][:5]) if body2 else "NONE"))
        else:
            ex2, tabs2, body2, _ = asu(src, None, None, None)
            if body2:
                hdr, row = body2[0]
                ra_k = [i for i, h in enumerate(hdr) if h.startswith("_RA") or h in ("RAJ2000", "RA_ICRS", "RAdeg", "ra")]
                de_k = [i for i, h in enumerate(hdr) if h.startswith("_DE") or h in ("DEJ2000", "DE_ICRS", "DEdeg", "dec")]
                if ra_k and de_k:
                    try:
                        cra, cde = row[ra_k[0]], row[de_k[0]]
                        if ":" in cra or " " in cra.strip():
                            from astropy.coordinates import SkyCoord; import astropy.units as u
                            c = SkyCoord(cra, cde, unit=(u.hourangle, u.deg)); cra, cde = c.ra.deg, c.dec.deg
                        ex3, _, body3, _ = asu(src, float(cra), float(cde), 5)
                        say(f"   control first row ({float(cra):.4f}, {float(cde):.4f}): re-found {len(body3)} rows")
                    except Exception as ex_:
                        say(f"   control first row: could not parse coords ({ex_}); first row {row[:4]}")
                else:
                    say(f"   control: table answered (first row {row[:4]}), no coordinate column to re-cone")
            else:
                say("   control: NO first row returned")
    except Exception as ex_:
        say(f"{name} [{src}]: QUERY FAILED {ex_}")
    time.sleep(1.0)

# (b) AAVSO VSX API
def vsx(ra, dec, rad=30):
    u = "https://www.aavso.org/vsx/index.php?" + urllib.parse.urlencode({"view": "api.list", "ra": ra, "dec": dec, "radius": rad / 3600, "format": "json"})
    hdr = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"}
    d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=hdr), timeout=60).read().decode("utf-8"))
    o = (d.get("VSXObjects") or {}); o = o.get("VSXObject", []) if isinstance(o, dict) else []
    return [o] if isinstance(o, dict) else o
for lab, (ra, de), rad in (("target", (RA, DEC), 30), ("target 120\"", (RA, DEC), 120), ("Algol", ALGOL, 30)):
    try:
        v = vsx(ra, de, rad)
        say(f"AAVSO VSX API {lab}: {len(v)} objects: " + "; ".join(f"{x.get('Name')} {x.get('VariabilityType')} P={x.get('Period')}" for x in v[:6]))
    except Exception as ex_:
        say(f"AAVSO VSX API {lab}: FAILED {ex_}")
    time.sleep(3.5)

# (c) Gaia vari tables for the target id
for tb in ("vari_summary", "vari_classifier_result", "vari_eclipsing_binary", "vari_rotation_modulation", "vari_short_timescale"):
    try:
        r = tap(f"SELECT * FROM gaiadr3.{tb} WHERE source_id = {GAIA_ID}")
        say(f"Gaia DR3 {tb}: {len(r)} rows for the target")
    except Exception as ex_:
        say(f"Gaia DR3 {tb}: FAILED {ex_}")
r = tap("SELECT COUNT(*) AS n FROM gaiadr3.vari_eclipsing_binary WHERE source_id = 5307278580723030144")
say(f"   control: vari_eclipsing_binary rows for the ECL neighbour 5307278580723030144: {r[0]['n']}")

# (d) arXiv cache
AD = os.path.join(os.environ["TEMP"], "heartbeats", "vet365670788", "arxiv")
PAPERS = {"2506.14869": "Callahan+2025 (Gaia SB + TESS)", "2608.12474": "Callahan+2026 (APOGEE + TESS)",
          "2407.18621": "Li+2024a", "2408.01019": "Li+2024b (TEOs)", "2508.01156": "Li+2025 (42 HB)",
          "2505.04067": "Li+2025 (RNN)", "2407.14421": "Solanki+2025", "2012.11559": "Kolaczek-Szymanski+2021",
          "2109.14616": "Wrona+2022"}
PATS = [r"438089101", r"5307278653764442880", r"8588[-\s]0*1489", r"09282887", r"142\.120", r"142\.12[0-9]",
        r"09[:\sh]+28[:\sm]+28", r"55[:\s°d]+38[:\s']+2[67]", r"\-55\.640", r"\-55\.641"]
for aid, name in PAPERS.items():
    fn = os.path.join(AD, aid + ".src")
    if not os.path.exists(fn): say(f"arXiv {aid} {name}: MISSING"); continue
    raw = open(fn, "rb").read(); texts = {}
    try:
        tf = tarfile.open(fileobj=io.BytesIO(raw), mode="r:*")
        for m in tf.getmembers():
            if m.isfile() and not re.search(r"\.(png|jpe?g|pdf|eps|ps|gif)$", m.name, re.I):
                texts[m.name] = tf.extractfile(m).read().decode("latin-1")
    except Exception:
        try: texts["main"] = gzip.decompress(raw).decode("latin-1")
        except Exception: texts["main"] = raw.decode("latin-1")
    alltx = "\n".join(texts.values())
    tics = re.findall(r"TIC[\s~]*(\d{6,10})", alltx) or re.findall(r"\b(\d{8,9})\b", alltx)
    ctl = tics[0] if tics else None
    ctl_n = len(re.findall(re.escape(ctl), alltx)) if ctl else 0
    hits = []
    for p in PATS:
        for mm in re.finditer(p, alltx):
            hits.append(f"/{p}/ ...{alltx[max(0, mm.start()-50):mm.end()+50]!r}")
    say(f"arXiv {aid} {name}: {len(texts)} files, {len(alltx)} chars, {len(set(tics))} distinct TIC-like ids; control TIC {ctl} found x{ctl_n}; target hits: {len(hits)}")
    for h in hits[:6]: say("     " + h[:240])

# (e) SIMBAD (CfA mirror only; Strasbourg not probed)
try:
    u = "https://simbad.cfa.harvard.edu/simbad/sim-coo?" + urllib.parse.urlencode({"Coord": f"{RA} {DEC}", "Radius": 10, "Radius.unit": "arcsec", "output.format": "ASCII"})
    txt = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read().decode("latin-1")
    say("SIMBAD (CfA mirror): " + txt[:1500].replace("\n", " | "))
except Exception as ex_:
    say(f"SIMBAD (CfA mirror): NOT REACHABLE ({ex_}); Strasbourg not probed (CDS outage) -> SIMBAD object type / reference count NOT CHECKED")
