import pathlib,hashlib,json
p=pathlib.Path(__file__).parent
files=sorted(x for x in p.iterdir() if x.is_file() and x.name!='helper-hashes.json')
result={x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in files}
(p/'helper-hashes.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(len(result),'helper files hashed')
