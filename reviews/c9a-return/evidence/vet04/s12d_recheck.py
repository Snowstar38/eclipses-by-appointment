# repeat the VSX / Gaia-EB / Prsa / IJspeert cones for both targets immediately after a passing Algol VSX control (mirror was flaky in s12c)
import requests, time
def q(src,ra,dec,rs):
    for i in range(4):
        try:
            r=requests.get(f'https://vizier.idia.ac.za/viz-bin/asu-tsv?-source={src}&-c={ra}%20{dec}&-c.rs={rs}&-out.all',timeout=120)
            L=[l for l in r.text.splitlines() if l and not l.startswith('#')]; return r.status_code,max(0,len(L)-3),(L[3][:150] if len(L)>3 else ''),len(r.text)
        except Exception as ex: time.sleep(5)
    return None,None,'',0
for att in range(3):
    c=q('B/vsx/vsx',47.04221,40.95565,60); print('control Algol VSX:',c)
    if c[1]: break
    time.sleep(20)
for tic,ra,dec in (('283532878',327.869175189832,57.9849184374285),('407877153',275.783436380745,-79.3525721366319)):
    for src in ('B/vsx/vsx','I/358/veb','J/ApJS/258/16','J/A+A/652/A120','I/357/varisum','B/sb9/main'):
        print(tic,src,'60":',q(src,ra,dec,60))
print('control Algol VSX after:',q('B/vsx/vsx',47.04221,40.95565,60))
