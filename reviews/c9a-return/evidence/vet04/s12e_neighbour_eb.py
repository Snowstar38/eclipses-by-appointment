# full VSX and Gaia DR3 EB rows for the catalogued EB 29.6" from TIC 283532878 (Gaia DR3 2202301140233408128)
import requests
for src in ('B/vsx/vsx','I/358/veb'):
    r=requests.get(f'https://vizier.idia.ac.za/viz-bin/asu-tsv?-source={src}&-c=327.869175189832%2057.9849184374285&-c.rs=60&-out.all',timeout=120)
    L=[l for l in r.text.splitlines() if l and not l.startswith('#')]
    for h,v in zip(L[0].split('\t'),L[3].split('\t')): print(src,h.strip(),'=',v.strip())
