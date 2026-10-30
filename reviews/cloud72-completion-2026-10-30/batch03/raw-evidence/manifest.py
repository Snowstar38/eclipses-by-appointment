import json,pathlib,hashlib
r=pathlib.Path(__file__).parent
files=sorted(p for p in r.rglob('*') if p.is_file() and p.name!='receipt-manifest.json')
json.dump([{'path':str(p.relative_to(r)).replace('\\','/'),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files],open(r/'receipt-manifest.json','w'),indent=2)
