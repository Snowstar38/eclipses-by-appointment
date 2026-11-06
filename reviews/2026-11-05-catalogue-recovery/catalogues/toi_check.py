r"""Is any claim or candidate a TESS Object of Interest? (2026-11-05)

    python toi_check.py [<tic-json> ...]           -> toi-check.txt beside this file

Reads the TICs of the 802 (claims.json), every claim_member in Astra's accepted-ledger.csv,
and any --extra JSON files given (same shape as extra-astra-1105.json), fetches the current
TOI list from ExoFOP into %TEMP%\fable51-toi\toi.csv (overwritten each run; the fetched file
is untrusted data and is only ever read as CSV), and prints every match by TIC id with the
TOI number, dispositions, period, depth and comment. R725 = TIC 219345200 = TOI-706.01 was
missed by eight catalogue tables and would have been caught here.
"""
import csv, json, os, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = r"[workspace]/Astra\made\binary-claim-review-2026-11-05\accepted-ledger.csv"
TOI_URL = "https://exofop.ipac.caltech.edu/tess/download_toi.php?sort=toi&output=csv"
TMP = HERE
os.makedirs(TMP, exist_ok=True)
out = open(os.path.join(HERE, "toi-check.txt"), "w", encoding="utf-8")


def say(s=""):
    print(s, flush=True); out.write(s + "\n")


label = json.load(open(os.path.join(HERE, 'exact-labels.json'), encoding='utf-8'))
say(f"{len(label)} TICs: {sum(v == 'run-802' for v in label.values())} run-only, "
    f"{sum(v.startswith('ledger-') for v in label.values())} ledger claims, "
    f"{sum(not (v == 'run-802' or v.startswith('ledger-')) for v in label.values())} extra")

csv_path = os.path.join(TMP, "toi.csv")
req = urllib.request.Request(TOI_URL, headers={"User-Agent": "house-gate/1.0"})
with urllib.request.urlopen(req, timeout=30) as f, open(csv_path, "wb") as g:
    g.write(f.read())
n = 0; hits = []
with open(csv_path, encoding="utf-8", errors="replace", newline="") as f:
    for r in csv.DictReader(f):
        n += 1
        t = r["TIC ID"].strip()
        if t in label:
            hits.append(r)
say(f"TOI list: {n} rows fetched {__import__('datetime').date.today()}; {len(hits)} match")
for r in hits:
    say(f"  TIC {r['TIC ID']:>10} = {label[r['TIC ID']]:<28} TOI-{r['TOI']:<9} TESS {r['TESS Disposition']:<3} "
        f"TFOPWG {r['TFOPWG Disposition']:<3} P {r.get('Period (days)', ''):<14} depth(ppm) {r.get('Depth (ppm)', ''):<10} "
        f"{(r.get('Comments') or '')[:140]}")
out.close()
