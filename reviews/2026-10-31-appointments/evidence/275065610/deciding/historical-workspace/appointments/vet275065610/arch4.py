"""Neighbour variability + Kostov t2 rows + NASA Exoplanet Archive TOI table. python -X utf8 arch4.py"""
import csv, io, json, urllib.parse, urllib.request
ra, de = 268.40948, 18.81502
def get(u, d=None): return urllib.request.urlopen(u, d, timeout=300).read().decode('utf-8', 'replace')
G = 'http[local path omitted]'
def gq(a):
    d = urllib.parse.urlencode({'REQUEST': 'doQuery', 'LANG': 'ADQL', 'FORMAT': 'csv', 'QUERY': a}).encode()
    return list(csv.DictReader(io.StringIO(get(G, d))))
cone = f"1=CONTAINS(POINT('ICRS',s.ra,s.dec),CIRCLE('ICRS',{ra},{de},{120/3600}))"
for t in ('vari_eclipsing_binary', 'vari_summary', 'vari_classifier_result', 'nss_two_body_orbit'):
    try:
        r = gq(f"SELECT v.*, s.phot_g_mean_mag, DISTANCE(POINT('ICRS',s.ra,s.dec),POINT('ICRS',{ra},{de}))*3600 AS sep FROM gaiadr3.{t} v JOIN gaiadr3.gaia_source s ON v.source_id=s.source_id WHERE {cone}")
        print(t, len(r)); [print('   ', {k: x[k] for k in list(x)[:14]}, 'sep', x['sep'], 'G', x['phot_g_mean_mag']) for x in r]
    except Exception as e: print(t, 'ERR', e)
# neighbour 45" TIC 275065613 in gaia_source
r = gq(f"SELECT source_id,ra,dec,phot_g_mean_mag,bp_rp,parallax,ruwe,non_single_star,phot_variable_flag,radial_velocity,rv_amplitude_robust,rv_chisq_pvalue FROM gaiadr3.gaia_source WHERE source_id=4551531565476021504")
print('nb45', r)
u = 'http[local path omitted]' + urllib.parse.urlencode({'-source': 'J/ApJS/279/50/table2', '-c': f'{ra} {de}', '-c.rs': 60, '-out.all': '', '-out.add': '_r'})
print(get(u)[-3000:])
u = 'http[local path omitted]' + urllib.parse.urlencode({'query': "select toi,tid,tfopwg_disp,pl_orbper,ra,dec from toi where tid in (275065610,275065613) or (ra between 268.38 and 268.44 and dec between 18.79 and 18.84)", 'format': 'csv'})
print('TOI table:', get(u))
