# s2b: follow-ups: ATLAS variables (J/AJ/156/241), ASAS-SN (II/366), Kostov? , SIMBAD identifiers, ExoFOP ctoi field, all-catalogue completeness
import requests, re, json, time
VIZ='https://vizier.idia.ac.za/viz-bin/asu-tsv'
T={'195865529':(310.726437212619,43.3062048382287),'468181994':(315.803516095103,-85.598149670046)}
def get(url,timeout=120):
    for i in range(4):
        try:
            r=requests.get(url,timeout=timeout)
            if r.ok: return r.text
        except Exception as e: print('  err',e)
        time.sleep(3)
def rows(txt):
    if txt is None: return None
    L=[l for l in txt.splitlines() if l and not l.startswith('#')]
    if len(L)<3: return []
    h=L[0].split('\t'); return [dict(zip(h,[v.strip() for v in l.split('\t')])) for l in L[3:] if l.strip()]
for tic,(ra,dec) in T.items():
    print('='*10,tic)
    for cat,rs in [('J/AJ/156/241',10),('II/366',30),('J/MNRAS/503/200',30),('J/AJ/167/192',30),('J/ApJS/247/44',30)]:
        r=rows(get(f"{VIZ}?-source={cat}&-c={ra}%20{dec}&-c.rs={rs}&-out.all&-sort=_r"))
        print(cat,rs,'rows:',None if r is None else len(r))
        for x in (r or [])[:3]: print('   ',{k:v for k,v in x.items() if v})
    txt=get(f"{VIZ}?-c={ra}%20{dec}&-c.rs=5&-out.max=1&-out=_r",timeout=240)
    tabs=re.findall(r'^#Table\s+(\S+)',txt or '',flags=re.M)
    names=re.findall(r'^#Name:\s+(\S+)',txt or '',flags=re.M)
    print('ALLCAT tables (#Table):',len(tabs),'(#Name):',len(names)); print('  ',' '.join(names))
    t=get(f"https://simbad.harvard.edu/simbad/sim-id?Ident=TIC%20{tic}&output.format=ASCII")
    L=t.splitlines()
    for i,l in enumerate(L):
        if l.startswith('Identifiers'): print('SIMBAD ids:',' | '.join(x.strip() for x in L[i+1:i+4]))
        if l.startswith('Bibcodes'): print('SIMBAD bib:',' | '.join(x.strip() for x in L[i:i+3]))
        if l.startswith('Object'): print(l)
    t=get(f"https://exofop.ipac.caltech.edu/tess/target.php?id={tic}&json")
    j=json.loads(t)
    for k in j:
        if 'toi' in k.lower(): print('ExoFOP',k,':',j[k])
    print('ExoFOP keys:',list(j.keys()))
