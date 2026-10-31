"""Extra archives: VizieR 60" cones on EB / variable catalogues (asu-tsv), Gaia DR3 vari_classifier_result,
SIMBAD identifiers + bibcodes, ZTF DR light curve (IRSA). python -X utf8 arch3.py <tic> <gaia_sid> <ra> <dec> <outdir>"""
import csv, io, json, os, sys, urllib.parse, urllib.request
tic, sid, ra, de, out = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
def get(u, data=None, t=300):
    return urllib.request.urlopen(u, data, timeout=t).read().decode('utf-8', 'replace')
TABS = {'Prsa+2022 TESS EBs': 'J/ApJS/258/16/tess-ebs', 'IJspeert+2024 OBAF EB': 'J/A+A/691/A242/obaf-eb1',
        'Kostov+2025 t2 (unvetted)': 'J/ApJS/279/50/table2', 'Kostov+2025 t3': 'J/ApJS/279/50/table3', 'Kostov+2025 t4': 'J/ApJS/279/50/table4',
        'Gaia DR3 EB (Mowlavi+2023)': 'J/A+A/674/A16', 'ZTF periodic vars (Chen+2020)': 'J/ApJS/249/18/table2',
        'ATLAS vars (Heinze+2018)': 'J/AJ/156/241/table4', 'ASAS-SN vars (Jayasinghe)': 'II/366/catalog',
        'WISE vars (Chen+2018)': 'J/ApJS/237/28/table1', 'VSX': 'B/vsx/vsx', 'SB9': 'B/sb9/main', 'WDS': 'B/wds/wds',
        'Gaia DR3 vari_summary (VizieR)': 'I/358/vclassre', 'Kepler/K2 EB?': 'J/AJ/151/68/table2',
        'TESS OBA EB (Southworth?)': 'J/MNRAS/510/1413', 'Justesen+2021 TESS EBs': 'J/ApJ/912/123/table1',
        'Howell+? KELT vars (Oelkers 2018)': 'J/AJ/155/39/table3', 'ASAS (Pojmanski) ACVS': 'II/264/asas3'}
o = {}
for name, tb in TABS.items():
    u = 'http[local path omitted]' + urllib.parse.urlencode({'-source': tb, '-c': f'{ra} {de}', '-c.rs': 60, '-out.max': 20, '-out.add': '_r', '-out.all': ''})
    try:
        L = [l for l in get(u).splitlines() if l and not l.startswith('#')]
        rows = [dict(zip(L[0].split('\t'), r.split('\t'))) for r in L[2:]] if len(L) > 2 else []
        o[name] = rows; print(f'{name} [{tb}]: {len(rows)} rows' + ''.join(f"\n    r={r.get('_r','?')}\" " + ' '.join(f'{k}={v.strip()}' for k, v in list(r.items())[:12] if v.strip()) for r in rows[:5]))
    except Exception as e: o[name] = str(e); print(name, 'ERROR', e)
G = 'http[local path omitted]'
for t in ('vari_classifier_result', 'vari_summary', 'vari_eclipsing_binary', 'vari_rotation_modulation', 'vari_long_period_variable'):
    d = urllib.parse.urlencode({'REQUEST': 'doQuery', 'LANG': 'ADQL', 'FORMAT': 'csv', 'QUERY': f'SELECT * FROM gaiadr3.{t} WHERE source_id={sid}'}).encode()
    try: r = list(csv.DictReader(io.StringIO(get(G, d)))); o['gaia_' + t] = r; print('Gaia DR3', t, len(r), r[:1])
    except Exception as e: print('Gaia', t, 'ERROR', e)
S = 'http[local path omitted]'
for lab, q in (('ids', f"SELECT i.id FROM ident i JOIN basic b ON i.oidref=b.oid WHERE CONTAINS(POINT('ICRS',b.ra,b.dec),CIRCLE('ICRS',{ra},{de},{5/3600}))=1"),
               ('refs', f"SELECT r.bibcode FROM has_ref h JOIN basic b ON h.oidref=b.oid JOIN ref r ON r.oidbib=h.oidbibref WHERE CONTAINS(POINT('ICRS',b.ra,b.dec),CIRCLE('ICRS',{ra},{de},{5/3600}))=1"),
               ('otypes', f"SELECT o.otype FROM otypes o JOIN basic b ON o.oidref=b.oid WHERE CONTAINS(POINT('ICRS',b.ra,b.dec),CIRCLE('ICRS',{ra},{de},{5/3600}))=1")):
    d = urllib.parse.urlencode({'REQUEST': 'doQuery', 'LANG': 'ADQL', 'FORMAT': 'csv', 'QUERY': q}).encode()
    try: r = list(csv.DictReader(io.StringIO(get(S, d)))); o['simbad_' + lab] = r; print('SIMBAD', lab, [list(x.values())[0] for x in r])
    except Exception as e: print('SIMBAD', lab, 'ERROR', e)
if de > -31:
    u = f'http[local path omitted],r,i&FORMAT=csv'
    try:
        txt = get(u, t=600); open(os.path.join(out, 'ztf_lc.csv'), 'w').write(txt)
        rows = list(csv.DictReader(io.StringIO(txt))); print('ZTF DR light curve rows:', len(rows), 'oids', sorted(set(r['oid'] for r in rows)))
    except Exception as e: print('ZTF ERROR', e)
json.dump(o, open(os.path.join(out, 'arch3.json'), 'w'), indent=1)
