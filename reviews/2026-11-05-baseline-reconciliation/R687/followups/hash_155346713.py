import hashlib
import json
from pathlib import Path

here = Path(__file__).resolve().parent
names = [p for p in here.iterdir() if p.is_file() and p.name != 'SHA256SUMS-155346713.json']
manifest = {'scope': 'Adaptive follow-up TIC 155346713; original frozen screening files excluded',
            'files': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(names)}}
(here / 'SHA256SUMS-155346713.json').write_text(json.dumps(manifest, indent=2))
verified = all(hashlib.sha256((here / name).read_bytes()).hexdigest() == digest
               for name, digest in manifest['files'].items())
print(len(manifest['files']), 'files, verified:', verified)
