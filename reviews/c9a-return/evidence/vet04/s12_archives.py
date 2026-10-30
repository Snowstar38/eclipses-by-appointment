import requests, re, time
T={'283532878':(327.869175189832,57.9849184374285),'407877153':(275.783436380745,-79.3525721366319)}
cats=[('B/vsx/vsx',60),('J/ApJS/258/16',60),('J/A+A/652/A120',60),('I/358/veb',60),('I/357/varisum',60),('B/sb9/main',60)]
def get(url,tries=4):
    for i in range(tries):
        try: return requests.get(url,timeout=90)
        except Exception as ex: print('   retry',repr(ex)[:120]); time.sleep(3)
for tic,(ra,dec) in T.items():
    print('=====',tic)
    for c,rs in cats:
        r=get(f'https://vizier.idia.ac.za/viz-bin/asu-tsv?-source={c}&-c={ra}%20{dec}&-c.rs={rs}&-out.all&-out.add=_r')
        lines=[l for l in r.text.splitlines() if l and not l.startswith('#')]
        print(f'-- {c} r<{rs}": http {r.status_code}, {max(0,len(lines)-3)} data rows')
        for l in lines[:8]: print('   ',l[:300])
    r=get(f'https://vizier.idia.ac.za/viz-bin/asu-tsv?-c={ra}%20{dec}&-c.rs=5&-out.add=_r')
    tabs=re.findall(r'#RESOURCE=\S+\s*\n#Name: (\S+)',r.text)
    print('-- all-catalogue 5": http',r.status_code,'tables:',' '.join(tabs) if tabs else '(none parsed)', ' (n chars %d)'%len(r.text))
    r=get(f'https://simbad.harvard.edu/simbad/sim-id?Ident=TIC%20{tic}&output.format=ASCII')
    print('-- SIMBAD id:'); print('\n'.join(r.text.splitlines()[:40]))
    r=get(f'https://exofop.ipac.caltech.edu/tess/target.php?id={tic}')
    txt=r.text
    print('-- ExoFOP http',r.status_code,'len',len(txt),'TOI mentions:',len(re.findall(r'TOI-?\s?\d+',txt)),'CTOI mentions:',len(re.findall(r'CTOI',txt)))
    for m in sorted(set(re.findall(r'TOI-?\s?\d+\.\d+',txt)))[:10]: print('    ',m)
# control: known EB to validate the all-catalogue / VSX query (Algol)
r=get('https://vizier.idia.ac.za/viz-bin/asu-tsv?-source=B/vsx/vsx&-c=47.042%2040.956&-c.rs=60&-out.all')
print('-- control VSX cone on Algol:',[l[:120] for l in r.text.splitlines() if 'bet Per' in l or 'Algol' in l][:2])
r=get('https://vizier.idia.ac.za/viz-bin/asu-tsv?-c=47.042%2040.956&-c.rs=5')
print('-- control all-catalogue on Algol: tables:',len(re.findall(r'#Name: ',r.text)))
