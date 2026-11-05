import pathlib,hashlib,json
b=pathlib.Path(__file__).resolve().parent
files=sorted(p for p in b.glob('helper*') if p.is_file() and p.name!='helper-hashes.json')+sorted(p for p in (b/'helper-pixels').rglob('*') if p.is_file())
(b/'helper-hashes.json').write_text(json.dumps({str(p.relative_to(b)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},indent=2)+'\n')
