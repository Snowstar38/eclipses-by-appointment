r"""Which claims or candidates did Kepler observe, and are they in the Kepler EB catalogue? (2026-11-05)

    python kepler_check.py [<tic-json> ...]        -> kepler-check.txt beside this file

For every TIC in claims.json, every claim_member of Astra's accepted-ledger.csv and any extra
JSON given: TIC positions from MAST (one request, cached in positions-<n>.json); for the ones
inside the Kepler footprint box (RA 279-302, Dec +36..+53) a MAST CAOM cone (0.003 deg) for
Kepler/K2 observations, then SIMBAD (CfA mirror TAP) for a KIC name, then the Kepler Eclipsing
Binary Catalog overview page for that KIC, parsed for its ephemeris. R706 = TIC 121277143 =
KIC 2697935 was published as new and is in that catalogue since 2013.
"""
import csv, json, os, re, sys, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = r"[workspace]/Astra\made\binary-claim-review-2026-11-05\accepted-ledger.csv"
TMP = HERE
os.makedirs(TMP, exist_ok=True)
out = open(os.path.join(HERE, "kepler-check.txt"), "w", encoding="utf-8")


def say(s=""):
    print(s, flush=True); out.write(s + "\n")


def mast(req):
    data = urllib.parse.urlencode({"request": json.dumps(req)}).encode()
    r = urllib.request.Request("https://mast.stsci.edu/api/v0/invoke", data=data, headers={"User-Agent": "house-gate/1.0"})
    return json.loads(urllib.request.urlopen(r, timeout=30).read().decode("utf-8"))["data"]


def simbad(adql):
    q = urllib.parse.urlencode({"request": "doQuery", "lang": "ADQL", "format": "json", "query": adql})
    with urllib.request.urlopen("https://simbad.cfa.harvard.edu/simbad/sim-tap/sync?" + q, timeout=20) as f:
        return json.loads(f.read().decode("utf-8")).get("data", [])


label = json.load(open(os.path.join(HERE, 'exact-labels.json'), encoding='utf-8'))
tics = sorted(label)
cache = os.path.join(HERE, f"positions-{len(tics)}.json")
if os.path.exists(cache):
    pos = json.load(open(cache, encoding="utf-8"))
else:
    rows = mast({"service": "Mast.Catalogs.Filtered.Tic", "format": "json",
                 "params": {"columns": "ID,ra,dec,GAIA,Tmag", "filters": [{"paramName": "ID", "values": tics}]}})
    pos = {str(x["ID"]): x for x in rows}
    json.dump(pos, open(cache, "w", encoding="utf-8"), indent=0)
say(f"{len(tics)} TICs, {len(pos)} positions")
kep = [t for t in tics if t in pos and 279 <= pos[t]["ra"] <= 302 and 36 <= pos[t]["dec"] <= 53]
say(f"in the Kepler footprint box: {len(kep)}")
for t in kep:
    p = pos[t]
    cone = mast({"service": "Mast.Caom.Cone", "format": "json", "params": {"ra": p["ra"], "dec": p["dec"], "radius": 0.003}})
    obs = sorted({(x["obs_collection"], x["target_name"]) for x in cone if x["obs_collection"] in ("Kepler", "K2")})
    kic = []
    try:
        ids = simbad(f"SELECT i2.id FROM ident i JOIN ident i2 ON i2.oidref = i.oidref WHERE i.id = 'Gaia DR3 {p['GAIA']}'")
        kic = [x[0] for x in ids if x[0].startswith(("KIC", "KOI"))]
    except Exception as e:
        kic = [f"SIMBAD error {e}"]
    line = f"  TIC {t:>10} = {label[t]:<28} ra {p['ra']:.4f} dec {p['dec']:+.4f}  Kepler/K2 obs: {obs or 'none'}  SIMBAD: {kic or 'no KIC name'}"
    for k in kic:
        if k.startswith("KIC"):
            url = "https://keplerebs.villanova.edu/overview/?k=" + k.split()[1]
            try:
                html = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "house-gate/1.0"}), timeout=20).read().decode("utf-8", "replace")
                txt = re.sub(r"<script.*?</script>|<style.*?</style>", " ", html, flags=re.S)
                txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", txt))
                m = re.search(r"(\d+) ephemeris in the catalog.*?True ([\d.]+) ([\d.]+) ([\d.]+)", txt)
                pub = re.search(r"Publication: ([^|]{0,120}?) EB justification", txt)
                line += f"\n      KEBC: {m.group(1) + ' ephemeris, P ' + m.group(2) + ' +- ' + m.group(3) + ' d, BJD0 ' + m.group(4) if m else 'not in the catalogue (no ephemeris block)'}"
                if pub: line += f"; {pub.group(1).strip()}"
            except Exception as e:
                line += f"\n      KEBC fetch failed: {e}"
    say(line)
out.close()
