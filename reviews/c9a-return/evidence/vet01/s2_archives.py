# s2: catalogue cones (VizieR idia mirror), SIMBAD (harvard mirror), ExoFOP for both targets
import requests, re, time
VIZ='https://vizier.idia.ac.za/viz-bin/asu-tsv'
T={'195865529':(310.726437212619,43.3062048382287),'468181994':(315.803516095103,-85.598149670046)}
def get(url,timeout=90):
    for i in range(4):
        try:
            r=requests.get(url,timeout=timeout)
            if r.ok: return r.text
            print('  HTTP',r.status_code)
        except Exception as e: print('  err',e)
        time.sleep(3)
    return None
def rows(txt):
    if txt is None: return None
    L=[l for l in txt.splitlines() if l and not l.startswith('#')]
    if len(L)<3: return []
    h=L[0].split('\t'); return [dict(zip(h,[v.strip() for v in l.split('\t')])) for l in L[3:] if l.strip()]
cats=[('B/vsx/vsx',60),('J/ApJS/258/16',60),('J/A+A/652/A120',60),('I/358/veb',60),('I/357/varisum',10),('B/sb9/main',60),('I/358/vclassre',10)]
# sanity check of the mirror on a known EB: Algol in VSX
r=rows(get(f"{VIZ}?-source=B/vsx/vsx&-c=47.04221%2040.95565&-c.rs=60&-out.all"))
print('SANITY Algol VSX rows:',None if r is None else len(r), (r[0].get('Name') if r else ''))
for tic,(ra,dec) in T.items():
    print('='*20,tic,ra,dec)
    for cat,rs in cats:
        r=rows(get(f"{VIZ}?-source={cat}&-c={ra}%20{dec}&-c.rs={rs}&-out.all&-sort=_r"))
        if r is None: print(f'{cat} ({rs}"): QUERY FAILED'); continue
        print(f'{cat} ({rs}"): {len(r)} rows')
        for x in r[:5]:
            print('   ',{k:v for k,v in x.items() if v and k in ('_r','Name','Type','Period','max','min','OID','TIC','Source','Per','P','Class','Seq','Sp1','Sp2','VarType','Vmag','Gmag','RAJ2000','DEJ2000','_RAJ2000','_DEJ2000','Model','ClassSB','BestClass','VCR','VRRLyr','VCep','VPN','VST','VLPV','VEB','VRM','VMSO','VAGN','Vmicro','VCC','Vnotclassified')})
    # all-catalogue 5"
    txt=get(f"{VIZ}?-c={ra}%20{dec}&-c.rs=5&-out.max=3",timeout=180)
    if txt is None: print('ALLCAT: failed')
    else:
        tabs=re.findall(r'^#RESOURCE=.*?\n#Name: (\S+)',txt,flags=re.M) or re.findall(r'^#Name: (\S+)',txt,flags=re.M)
        print('ALLCAT 5": tables with rows:',len(tabs)); print('   ',' '.join(tabs))
    # SIMBAD
    t=get(f"https://simbad.harvard.edu/simbad/sim-coo?Coord={ra}%20{dec}&Radius=10&Radius.unit=arcsec&output.format=ASCII")
    if t: 
        for l in t.splitlines():
            if re.match(r'^(Object|Number of objects|Coordinates\(ICRS|Identifiers|Bibcodes|Types|\d+\|)',l) or 'bibcodes' in l.lower(): print('  SIMBAD:',l[:220])
    t=get(f"https://simbad.harvard.edu/simbad/sim-id?Ident=TIC%20{tic}&output.format=ASCII")
    if t:
        lines=t.splitlines()
        for i,l in enumerate(lines):
            if l.startswith('Object') or l.startswith('Identifiers') or l.startswith('Bibcodes') or 'Spectral type' in l: print('  SIMBAD-id:',l[:200]); 
            if l.startswith('Identifiers'): print('    ', ' | '.join(x.strip() for x in lines[i+1:i+6]))
    # ExoFOP
    t=get(f"https://exofop.ipac.caltech.edu/tess/target.php?id={tic}&json")
    if t:
        print('  ExoFOP bytes',len(t),' TOI mentions:',len(re.findall(r'"toi"\s*:\s*"?\d',t)), ' CTOI:', len(re.findall(r'ctoi',t,flags=re.I)))
        m=re.findall(r'"toi[^"]*"\s*:\s*[^,]*',t)[:5]; print('   ',m)
