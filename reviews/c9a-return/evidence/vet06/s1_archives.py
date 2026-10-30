# Archive cones (VizieR mirror), all-catalogue 5", SIMBAD (Harvard mirror), ExoFOP.
import requests, re, time
T={'468827621':(91.9386505142516,69.034466660429),'416285595':(287.318165074913,24.0684959972507)}
VIZ='https://vizier.idia.ac.za/viz-bin/asu-tsv'
def get(url):
    for i in range(4):
        try:
            r=requests.get(url,timeout=90)
            if r.ok: return r.text
            print('HTTP',r.status_code)
        except Exception as e: print('ERR',e)
        time.sleep(3)
    return None
cats=[('B/vsx/vsx',60),('J/ApJS/258/16',60),('J/A+A/652/A120',60),('I/358/veb',60),('I/357/varisum',60),('B/sb9/main',60),('I/358/vclassre',60),('II/366',60),('J/AJ/162/170',60)]
for tic,(ra,dec) in T.items():
    print('='*20,tic,ra,dec)
    for c,rs in cats:
        t=get(f"{VIZ}?-source={c}&-c={ra}%20{dec}&-c.rs={rs}&-out.all&-sort=_r")
        if t is None: print(c,'FAILED'); continue
        lines=[l for l in t.splitlines() if l and not l.startswith('#')]
        print(f'--- {c} r<{rs}": {max(0,len(lines)-3)} rows')
        for l in lines[:3+5]: print('   ',l[:500])
    t=get(f"{VIZ}?-c={ra}%20{dec}&-c.rs=5&-out.max=5")
    tabs=re.findall(r'#Name: (\S+)', t or '')
    print('--- all-catalogue 5": tables:', len(tabs)); print('   ', ' '.join(tabs))
    s=get(f"https://simbad.harvard.edu/simbad/sim-id?Ident=TIC%20{tic}&output.format=ASCII")
    print('--- SIMBAD id:'); print((s or 'FAILED')[:2500])
    s=get(f"https://simbad.harvard.edu/simbad/sim-coo?Coord={ra}%20{dec}&Radius=10&Radius.unit=arcsec&output.format=ASCII")
    print('--- SIMBAD coo 10":'); print((s or 'FAILED')[:2000])
    e=get(f"https://exofop.ipac.caltech.edu/tess/target.php?id={tic}")
    if e:
        print('--- ExoFOP: TOI mentions', len(re.findall(r'TOI-?\s?\d+\.\d\d',e)), 'CTOI mentions', len(re.findall(r'CTOI',e)), set(re.findall(r'TOI-?\s?\d+\.\d\d',e)))
        m=re.findall(r'(TYC [\d-]+|2MASS J[\d+-]+|Gaia DR\d \d+|UCAC4 [\d-]+|HD \d+|BD[+-]\d+ \d+)',e); print('   names:',sorted(set(m))[:12])
    else: print('--- ExoFOP FAILED')
t=get(f"{VIZ}?-source=B/vsx/vsx&-c=47.0422%2040.9556&-c.rs=60&-out.all")
print('sanity Algol VSX rows:', max(0,len([l for l in t.splitlines() if l and not l.startswith('#')])-3) if t else 'FAILED')
