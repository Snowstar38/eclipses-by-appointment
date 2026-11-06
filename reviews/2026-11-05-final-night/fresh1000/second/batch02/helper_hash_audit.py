import json,hashlib,pathlib
b=pathlib.Path('.')
a=json.loads((b/'lead-source-hashes.json').read_text()); out=[]
for tic,v in a.items():
 for s in v['source']:
  p=pathlib.Path(s['path']); h=hashlib.sha256(p.read_bytes()).hexdigest();out.append({'tic':tic,'sector':s['sector'],'match':h==s['sha256'],'sha256':h})
for tic in a:
 p=b/tic/'helper-tesscut.fits'; rec=json.loads((b/tic/'helper-localization.json').read_text()); h=hashlib.sha256(p.read_bytes()).hexdigest();out.append({'tic':tic,'file':str(p),'match':h==rec['fits_sha256'],'sha256':h})
(b/'helper-independent-hash-audit.json').write_text(json.dumps(out,indent=2));print(len(out),sum(not x['match'] for x in out))
