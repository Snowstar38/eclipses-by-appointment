import requests, re
stars={'70665829':(155.384788090706,17.2035145893056),'331293467':(212.403511923353,-60.1143106920448)}
cats=[('B/vsx/vsx',60),('J/ApJS/258/16',60),('J/A+A/652/A120',60),('I/358/veb',60),('I/357/varisum',60),('B/sb9/main',60)]
def viz(src,ra,dec,r):
    u=f'https://vizier.idia.ac.za/viz-bin/asu-tsv?'+(f'-source={src}&' if src else '')+f'-c={ra}%20{dec}&-c.rs={r}&-out.all&-out.add=_r'
    t=requests.get(u,timeout=120).text
    rows=[l for l in t.splitlines() if l and not l.startswith('#')]
    return t,rows
# sanity check with a known object: Algol (VSX), and a Prsa EB
t,rows=viz('B/vsx/vsx',47.04221,40.95564,60); print('SANITY VSX Algol rows:',len(rows)); print('\n'.join(rows[:4]))
for tic,(ra,dec) in stars.items():
    print('='*20,tic)
    for c,r in cats:
        t,rows=viz(c,ra,dec,r)
        print('--',c,f'{r}"','nlines',len(rows))
        for l in rows[:8]: print('   ',l[:300])
    t,rows=viz(None,ra,dec,5)
    tabs=re.findall(r'#RESOURCE=.*\n#Name: (\S+)',t)
    print('-- all-catalogue 5":',len(set(tabs)),'tables'); print('   ',sorted(set(tabs)))
    s=requests.get(f'https://simbad.harvard.edu/simbad/sim-coo?Coord={ra}%20{dec}&Radius=10&Radius.unit=arcsec&output.format=ASCII',timeout=60).text
    print('-- SIMBAD coo 10":'); print(s[:2500])
    e=requests.get(f'https://exofop.ipac.caltech.edu/tess/target.php?id={tic}',timeout=60).text
    print('-- ExoFOP len',len(e),'TOI mentions:',set(re.findall(r'TOI[- ]?\d+\.\d+',e)),'CTOI:',set(re.findall(r'CTOI[^<]{0,30}',e))[:5] if False else len(re.findall('CTOI',e)))
