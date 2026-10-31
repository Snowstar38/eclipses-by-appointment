"""Quick VizieR asu-tsv 60" cones (60-s timeout each) on EB/variable catalogues. python -u viz.py"""
import urllib.parse, urllib.request
ra, de = 316.46118586319, 29.32349956807
T = {'VSX': 'B/vsx/vsx', 'Prsa+2022': 'J/ApJS/258/16/tess-ebs', 'IJspeert+2024': 'J/A+A/691/A242/obaf-eb1', 'Kostov t2': 'J/ApJS/279/50/table2',
     'Kostov t3': 'J/ApJS/279/50/table3', 'Kostov t4': 'J/ApJS/279/50/table4', 'Mowlavi+2023 Gaia EB': 'J/A+A/674/A16', 'ASAS-SN vars': 'II/366/catalog',
     'SB9': 'B/sb9/main', 'WDS': 'B/wds/wds', 'ATLAS vars': 'J/AJ/156/241/table4', 'Gaia DR3 vari classif': 'I/358/vclassre', 'ASAS ACVS': 'II/264/asas3'}
for k, tb in T.items():
    u = 'http[local path omitted]' + urllib.parse.urlencode({'-source': tb, '-c': f'{ra} {de}', '-c.rs': 60, '-out.max': 20, '-out.add': '_r'})
    try:
        L = [l for l in urllib.request.urlopen(u, timeout=60).read().decode('utf-8', 'replace').splitlines() if l and not l.startswith('#')]
        rows = L[2:] if len(L) > 2 else []
        print(f'{k} [{tb}]: {len(rows)} rows', *[r[:200] for r in rows[:3]], sep='\n   ')
    except Exception as e: print(k, 'ERROR', e)
