# control: the same VizieR-mirror cone queries as s12 must return rows for a known object (Algol = bet Per, in VSX, SB9 and Gaia varisum)
import requests
for c,rs in [('B/vsx/vsx',60),('B/sb9/main',60),('I/357/varisum',60)]:
    for i in range(4):
        try: r=requests.get(f'https://vizier.idia.ac.za/viz-bin/asu-tsv?-source={c}&-c=47.04221%2040.95565&-c.rs={rs}&-out.all',timeout=120); break
        except Exception as ex: print('retry',repr(ex)[:80])
    lines=[l for l in r.text.splitlines() if l and not l.startswith('#')]
    print(f'control Algol {c} r<{rs}": http {r.status_code}, {max(0,len(lines)-3)} data rows; first: {lines[3][:120] if len(lines)>3 else None}')
