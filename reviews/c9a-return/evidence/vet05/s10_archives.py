import requests, re
V='https://vizier.idia.ac.za/viz-bin/asu-tsv'
stars={'15855794':(61.98479061937,22.75262439668),'92881948':(83.23743198367,-22.99121122673),'CONTROL_Algol':(47.04221857,40.95564667)}
cats=[('B/vsx/vsx',60),('J/ApJS/258/16',60),('J/A+A/652/A120',60),('I/358/veb',60),('I/357/varisum',60),('B/sb9/main',60)]
def rows(txt):
    L=[l for l in txt.splitlines() if l and not l.startswith('#')]
    return L
for name,(ra,dec) in stars.items():
    print('=====',name,ra,dec)
    for cat,rad in cats:
        try:
            r=requests.get(V,params={'-source':cat,'-c':f'{ra} {dec}','-c.rs':rad,'-out.all':'','-out.add':'_r','-sort':'_r'},timeout=90)
            L=rows(r.text)
            # header lines: names, units, dashes
            data=L[3:] if len(L)>3 else []
            print(f'  {cat} r<{rad}": HTTP {r.status_code}, {len(data)} rows')
            for l in L[:1]+data[:4]: print('     ',l[:400])
        except Exception as ex: print('  ',cat,'ERR',ex)
    try:
        r=requests.get(V,params={'-c':f'{ra} {dec}','-c.rs':5,'-out.add':'_r'},timeout=120)
        tabs=re.findall(r'#RESOURCE=\S+\s*\n#Name: (\S+)',r.text)
        if not tabs: tabs=re.findall(r'#Name: (\S+)',r.text)
        print('  ALL-CAT r<5": HTTP',r.status_code,len(tabs),'tables:',' '.join(tabs))
    except Exception as ex: print('  ALL ERR',ex)
for tic,(ra,dec) in list(stars.items())[:2]:
    r=requests.get('https://simbad.harvard.edu/simbad/sim-coo',params={'Coord':f'{ra} {dec}','Radius':10,'Radius.unit':'arcsec','output.format':'ASCII'},timeout=60)
    print('===== SIMBAD',tic); print(r.text[:2500])
    r=requests.get('https://simbad.harvard.edu/simbad/sim-id',params={'Ident':f'TIC {tic}','output.format':'ASCII'},timeout=60)
    print('--- sim-id TIC',tic); print(r.text[:2500])
    r=requests.get(f'https://exofop.ipac.caltech.edu/tess/target.php?id={tic}',timeout=60)
    t=r.text
    print('===== ExoFOP',tic,'HTTP',r.status_code,'len',len(t),'TOI mentions:',len(re.findall(r'TOI[- ]?\d',t)),'CTOI mentions:',len(re.findall(r'CTOI',t)))
    for m in re.findall(r'(TOI[- ]?\d+\.\d+|CTOI[^<]{0,60})',t)[:10]: print('    ',m)
