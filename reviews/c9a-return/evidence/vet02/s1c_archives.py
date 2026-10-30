# Follow-up after the restart: SIMBAD object type + bibcode count (full ASCII record), and the all-catalogue
# 5" VizieR list for 379251709 (s1b crashed on it), with retries; plus the TIC contamination ratios from targets.csv.
import requests, re, time, csv
T = {'470235665': ('2287291537931000064', 345.747449371502, 81.6998220902246), '379251709': ('519027491846682624', 29.7546213215801, 67.5461688632913)}
def get(url, to=180):
    for i in range(4):
        try:
            r = requests.get(url, timeout=to)
            if r.ok: return r.text
        except Exception as e: print('  retry', i, type(e).__name__)
        time.sleep(5)
for tic, (gid, ra, dec) in T.items():
    s = get(f'https://simbad.harvard.edu/simbad/sim-id?Ident=Gaia%20DR3%20{gid}&output.format=ASCII') or ''
    obj = re.findall(r'Object (.+?)  ---  (\S+)  ---', s); bib = re.findall(r'Bibcodes\s+\S+\s+\(.*?\)\s+\((\d+)\)', s)
    ids = s.split('Identifiers')[1].strip() if 'Identifiers' in s else ''
    print(tic, 'SIMBAD object/type:', obj, '| bibcodes:', bib or 'none listed')
    print('   identifiers:', re.sub(r'\s{2,}', ' | ', ids.split('Bibcodes')[0])[:400])
    for l in s.splitlines():
        if l.startswith('Bibcodes') or l.startswith('Notes') or l.startswith('Measures'): print('  ', l)
    if tic == '379251709':
        t = get(f'https://vizier.idia.ac.za/viz-bin/asu-tsv?-c={ra}%20{dec}&-c.rs=5&-out.max=1&-meta.max=1000', 300) or ''
        tabs = re.findall(r'#Name: (\S+)', t)
        print(tic, 'all-catalogue 5" tables (%d):' % len(tabs), ' '.join(tabs))
        print('   variability/EB/journal tables:', [x for x in tabs if re.match(r'(B/vsx|J/|I/358|I/357|B/sb9|II/366|B/gcvs)', x)])
for r in csv.DictReader(open('[local path omitted]')):
    if r['tic'] in T: print(r['tic'], 'TIC contratio', r['tic_contratio'], 'Teff', r['tic_Teff'], 'R', r['tic_rad'], 'M', r['tic_mass'], 'logg', r['tic_logg'], 'plx', r['tic_plx'], 'lum', r['tic_lum'])
