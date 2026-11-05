import pathlib,hashlib,json
b=pathlib.Path(__file__).parent
files=sorted(p for p in b.rglob('helper-*') if p.is_file() and p.name!='helper-source-manifest.json')
# Include exact shared Gaia NSS source used by geometry, and original sealed packet.
files += [b.parent/'shared-catalogues/gaia_nss.csv',b.parent/'source-packets/280051953/sources.json']
result={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
(b/'helper-source-manifest.json').write_text(json.dumps(result,indent=2)+'\n')
