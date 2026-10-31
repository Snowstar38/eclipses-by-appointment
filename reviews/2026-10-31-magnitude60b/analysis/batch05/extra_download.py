from pathlib import Path
import json,requests
B=Path(__file__).parent;T=json.load(open(B.parent/'targets-selected.json'));rr=[]
for tic,sec in [('102716983',59),('331861613',18)]:
 p=B/tic/'raw'/f'{tic}_s{sec:03}.fits';p.parent.mkdir(exist_ok=True);uri=dict(T[tic]['qlp'])[sec];r=requests.get('http[local path omitted]',params={'uri':uri},timeout=90);r.raise_for_status();p.write_bytes(r.content);rr.append(dict(tic=tic,sector=sec,uri=uri,path=str(p),bytes=len(r.content)))
json.dump(rr,open(B/'extra-downloads.json','w'),indent=2)
