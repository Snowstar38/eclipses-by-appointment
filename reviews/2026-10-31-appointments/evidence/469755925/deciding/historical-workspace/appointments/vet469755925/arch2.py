"""Further archives: Gaia DR3 vari tables + full NSS row, VSX, SB9, WDS (VizieR), ExoFOP TOI/CTOI.
python -X utf8 arch2.py <tic> <gaia_source_id> <ra> <dec> <outjson>"""
import csv, io, json, sys, urllib.parse, urllib.request
tic, sid, ra, de, out = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
def tap(url, adql):
    d = urllib.parse.urlencode({'REQUEST': 'doQuery', 'LANG': 'ADQL', 'FORMAT': 'csv', 'QUERY': adql}).encode()
    for k in range(3):
        try: return list(csv.DictReader(io.StringIO(urllib.request.urlopen(url, d, timeout=300).read().decode('utf-8', 'replace'))))
        except Exception as e: err = str(e)
    return [{'error': err}]
G = 'http[local path omitted]'; V = 'http[local path omitted]'
o = {}
o['nss_full'] = tap(G, f'SELECT * FROM gaiadr3.nss_two_body_orbit WHERE source_id={sid}')
o['vari_summary'] = tap(G, f'SELECT * FROM gaiadr3.vari_summary WHERE source_id={sid}')
o['vari_eb'] = tap(G, f'SELECT * FROM gaiadr3.vari_eclipsing_binary WHERE source_id={sid}')
o['astro'] = tap(G, f'SELECT source_id,radial_velocity,radial_velocity_error,rv_nb_transits,rv_chisq_pvalue,rv_renormalised_gof,rv_amplitude_robust,phot_variable_flag,teff_gspphot,logg_gspphot,ruwe,ipd_frac_multi_peak,ipd_gof_harmonic_amplitude FROM gaiadr3.gaia_source WHERE source_id={sid}')
cone = lambda tb, ra_, de_, r: (f"SELECT *, DISTANCE(POINT('ICRS',{ra_},{de_}),POINT('ICRS',{ra},{de}))*3600 AS sep FROM \"{tb}\" "
                                f"WHERE 1=CONTAINS(POINT('ICRS',{ra_},{de_}),CIRCLE('ICRS',{ra},{de},{r/3600}))")
o['vsx'] = tap(V, cone('B/vsx/vsx', 'RAJ2000', 'DEJ2000', 60))
o['sb9'] = tap(V, cone('B/sb9/main', 'RAJ2000', 'DEJ2000', 30))
o['wds'] = tap(V, cone('B/wds/wds', 'RAJ2000', 'DEJ2000', 30))
try:
    u = f'http[local path omitted]'
    j = json.loads(urllib.request.urlopen(u, timeout=120).read())
    o['exofop'] = {k: j.get(k) for k in ('tois', 'ctois', 'stellar_comments', 'planet_parameters')}
    o['exofop_basic'] = j.get('basic_info')
except Exception as e: o['exofop'] = {'error': str(e)}
json.dump(o, open(out, 'w'), indent=1)
for k, v in o.items():
    if isinstance(v, list):
        print(k, len(v), [{kk: vv for kk, vv in r.items() if vv not in ('', None)} for r in v][:3] if k != 'nss_full' else '')
    else: print(k, v)
