from pathlib import Path
import json,hashlib,csv
B=Path('.'); D=B.parent
sources={}
for n in ['queue.csv','targets-selected.json','BRIEF.md','INTEGRATION-NOTES.md','shared-catalogues/coverage-matrix.csv','shared-catalogues/gaia-nss_two_body_orbit.csv','shared-catalogues/sha256-manifest.csv']:
 p=D/n;sources[str(p)]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
manifest={'scope':'final34 positions31-34 only','source_files':sources,'files':{}}
for p in sorted(B.rglob('*')):
 if p.is_file() and p.name not in ['manifest.json'] and p.suffix.lower() not in ['.fits']:
  manifest['files'][str(p.relative_to(B))]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
(B/'manifest.json').write_text(json.dumps(manifest,indent=2))
print(len(manifest['files']),'files hashed; excludes FITS bytes, source hashes in raw-events/qlp-results')
