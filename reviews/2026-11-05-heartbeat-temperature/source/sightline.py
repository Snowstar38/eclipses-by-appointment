"""Independent extinction check: GSP-Phot A_G / E(BP-RP) for Gaia stars near
TIC 438089101's sightline, binned by distance. If stars at ~1.4 kpc carry
E(B-V) ~ 0.15 rather than Schlegel's 0.555 full column, the low-extinction
solution is the field's, not just this fit's."""
import json, sys, time
import urllib.request, urllib.parse

RA, DEC = 142.120297, -55.640822
ADQL = f"""
SELECT parallax, parallax_error, ag_gspphot, ebpminrp_gspphot,
       teff_gspphot, phot_g_mean_mag,
       DISTANCE(POINT('ICRS', ra, dec), POINT('ICRS', {RA}, {DEC})) AS sep
FROM gaiadr3.gaia_source
WHERE CONTAINS(POINT('ICRS', ra, dec),
               CIRCLE('ICRS', {RA}, {DEC}, 0.1)) = 1
  AND ag_gspphot IS NOT NULL
  AND parallax > 0.2 AND parallax_error < 0.15
"""
url = 'https://gea.esac.esa.int/tap-server/tap/sync'
data = urllib.parse.urlencode({
    'REQUEST': 'doQuery', 'LANG': 'ADQL', 'FORMAT': 'json', 'QUERY': ADQL,
}).encode()
for attempt in range(3):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=data), timeout=120) as r:
            res = json.load(r)
        break
    except Exception as e:
        print(f'attempt {attempt+1}: {e}', file=sys.stderr)
        time.sleep(10)
else:
    sys.exit('ESA TAP unreachable')

rows = res['data']
print(f'{len(rows)} stars with GSP-Phot A_G within 6 arcmin')
import statistics
bins = [(0.9, 1.3), (1.1, 1.8), (0.55, 0.85)]  # kpc ranges via plx
for lo_kpc, hi_kpc in [(0.8, 1.2), (1.2, 1.7), (1.7, 2.5), (0.4, 0.8)]:
    sel = [r for r in rows if 1.0/hi_kpc <= float(r[0]) <= 1.0/lo_kpc]
    if not sel:
        print(f'{lo_kpc}-{hi_kpc} kpc: 0 stars'); continue
    ags = sorted(float(r[2]) for r in sel)
    ebs = sorted(float(r[3]) for r in sel)
    med_ag = statistics.median(ags); med_eb = statistics.median(ebs)
    q1, q3 = ags[len(ags)//4], ags[3*len(ags)//4]
    # E(B-V) from A_G via A_G = 0.789*3.1*E -> E = A_G/2.446
    print(f'{lo_kpc}-{hi_kpc} kpc: n={len(sel):3d}  median A_G {med_ag:.3f} '
          f'(IQR {q1:.3f}-{q3:.3f}) -> E(B-V) ~ {med_ag/2.446:.3f}; '
          f'median E(BP-RP) {med_eb:.3f} -> E(B-V) ~ {med_eb/1.280:.3f}')
json.dump(rows, open('sightline_rows.json', 'w'))
print('saved sightline_rows.json')
