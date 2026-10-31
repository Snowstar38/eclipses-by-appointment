"""Gaia DR3: target row, NSS orbit and every source within 90". python -X utf8 gaia_q.py <source_id> <outdir>
-> <outdir>/gaia.json"""
import csv, io, json, os, sys, urllib.parse, urllib.request
sid, out = sys.argv[1], sys.argv[2]
TAP = 'http[local path omitted]'
def q(adql):
    d = urllib.parse.urlencode({'REQUEST': 'doQuery', 'LANG': 'ADQL', 'FORMAT': 'csv', 'QUERY': adql}).encode()
    for k in range(2):
        try: return list(csv.DictReader(io.StringIO(urllib.request.urlopen(TAP, d, timeout=300).read().decode('utf-8', 'replace'))))
        except Exception as e: print('retry', e)
    raise SystemExit('Gaia TAP failed twice')
o = {}
o['src'] = q(f'SELECT source_id,ra,dec,phot_g_mean_mag,bp_rp,parallax,ruwe,non_single_star FROM gaiadr3.gaia_source WHERE source_id={sid}')
o['nss'] = q(f'SELECT source_id,nss_solution_type,period,period_error,eccentricity,t_periastron FROM gaiadr3.nss_two_body_orbit WHERE source_id={sid}')
ra, de = float(o['src'][0]['ra']), float(o['src'][0]['dec'])
o['nb'] = q(f"SELECT source_id,ra,dec,phot_g_mean_mag,bp_rp,parallax,"
            f"DISTANCE(POINT('ICRS',ra,dec),POINT('ICRS',{ra},{de}))*3600 AS sep FROM gaiadr3.gaia_source "
            f"WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{de},{90/3600})) ORDER BY sep")
os.makedirs(out, exist_ok=True); json.dump(o, open(os.path.join(out, 'gaia.json'), 'w'), indent=1)
print(o['src'][0]); print(o['nss'])
for r in o['nb']: print(f"  {r['source_id']} sep {float(r['sep']):5.1f} G {r['phot_g_mean_mag']}")
