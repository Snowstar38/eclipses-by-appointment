import hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent
files=[p for p in B.glob('helper-*') if p.is_file() and p.name!='helper-hashes.json']
files += [B.parent/'shared-catalogues/gaia-neighbors.json', B.parent/'source-packets/323458448/sources.json',B.parent/'source-packets/313142904/sources.json',Path('[local-path-redacted]'),Path('[local-path-redacted]')]
(B/'helper-hashes.json').write_text(json.dumps({str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},indent=2))
