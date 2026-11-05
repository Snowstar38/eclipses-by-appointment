import hashlib,json,pathlib
D=pathlib.Path(r'[local-path-redacted]');B=pathlib.Path(r'[local-path-redacted]');out={}
for s in [80,91,92]:
 p=D/f'362778566_s{s:03}.fits';out[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
json.dump(out,open(B/'helper-T033-sector-hashes.json','w'),indent=2)
