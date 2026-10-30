# follow-up to s12: SIMBAD by coordinates (TIC ids are not SIMBAD identifiers), full list of VizieR tables within 5",
# and ExoFOP context for the "CTOI" string hits.
import requests, re, time
T={'283532878':(327.869175189832,57.9849184374285),'407877153':(275.783436380745,-79.3525721366319)}
def get(url,tries=4):
    for i in range(tries):
        try: return requests.get(url,timeout=120)
        except Exception as ex: print('   retry',repr(ex)[:120]); time.sleep(3)
for tic,(ra,dec) in T.items():
    print('=====',tic)
    r=get(f'https://simbad.harvard.edu/simbad/sim-coo?Coord={ra}%20{dec}&Radius=10&Radius.unit=arcsec&output.format=ASCII')
    print('-- SIMBAD sim-coo 10":'); print('\n'.join(l for l in r.text.splitlines()[:60] if l.strip()))
    r=get(f'https://vizier.idia.ac.za/viz-bin/asu-tsv?-c={ra}%20{dec}&-c.rs=5&-out=_r&-out.max=1&-meta.all=0')
    tabs=sorted(set(re.findall(r'#Table\s+(\S+)',r.text)) | set(re.findall(r'#Name: (\S+)',r.text)))
    print(f'-- all-catalogue 5" (out.max=1 per table): {len(tabs)} tables:'); print('   '+' '.join(tabs))
    var=[t for t in tabs if re.match(r'(B/vsx|B/gcvs|II/366|J/ApJS/258/16|J/A\+A/652/A120|I/358|I/357|B/sb9|J/AJ/.*|J/MNRAS/.*|J/A\+A/.*|J/ApJ/.*)',t)]
    print('   variability/binary-relevant or journal tables:',' '.join(var) if var else '(none)')
    r=get(f'https://exofop.ipac.caltech.edu/tess/target.php?id={tic}')
    for m in re.finditer(r'.{0,80}CTOI.{0,80}',r.text): print('   ExoFOP CTOI context:',re.sub(r'<[^>]+>',' ',m.group(0)).strip()[:160])
    print('   ExoFOP TOI pattern hits:',sorted(set(re.findall(r'TOI-?\s?\d{2,5}(?:\.\d+)?',r.text)))[:10])
r=get('https://vizier.idia.ac.za/viz-bin/asu-tsv?-c=47.042%2040.956&-c.rs=5&-out=_r&-out.max=1')
print('-- control all-catalogue on Algol, tables:',len(set(re.findall(r'#Table\s+(\S+)',r.text))|set(re.findall(r'#Name: (\S+)',r.text))),'; has B/vsx:', 'B/vsx' in r.text)
