# Sanity: each catalogue answers through the mirror (rows within 3 deg of each target), so the empty 60" cones in s2 are real.
import requests
stars={'70665829':(155.384788090706,17.2035145893056),'331293467':(212.403511923353,-60.1143106920448)}
for src in ['B/vsx/vsx','J/ApJS/258/16','J/A+A/652/A120','I/358/veb','I/357/varisum','B/sb9/main']:
    for tic,(ra,dec) in stars.items():
        u=f'https://vizier.idia.ac.za/viz-bin/asu-tsv?-source={src}&-c={ra}%20{dec}&-c.rs=10800&-out.max=3&-sort=_r&-out.add=_r'
        try:
            t=requests.get(u,timeout=180).text
            rows=[l for l in t.splitlines() if l and not l.startswith('#') and l[0] in ' 0123456789']
            print(f'{src:16s} around {tic}: {len(rows)} rows (max 3); nearest _r(arcsec): {[l.split()[0] for l in rows[:3]]}')
        except Exception as e: print(src,tic,'failed',e)
