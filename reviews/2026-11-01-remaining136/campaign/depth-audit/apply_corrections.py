"""Authorized bounded correction, with original bytes and hashes preserved."""
import csv,hashlib,json,os,shutil
from pathlib import Path
from PIL import Image,ImageDraw
O=Path(__file__).parent;R=O.parent
M=json.load(open(O/'correction-manifest.json'));changes=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def preserve(rel):
 p=R/rel;q=O/'originals'/rel;q.parent.mkdir(parents=True,exist_ok=True)
 if q.exists():assert q.read_bytes()==p.read_bytes(),'Prior snapshot differs: '+str(rel)
 else:shutil.copy2(p,q)
 return sha(p)
def replace(rel,data):
 before=preserve(rel) if (R/rel).exists() else None
 (R/rel).write_bytes(data);changes.append(dict(path=rel.as_posix(),before_sha256=before,after_sha256=sha(R/rel)))
batches=['batch02','batch03','batch05','batch06','batch07']
for b in batches:
 for name in ['SHA256SUMS.json','RESULTS.csv']:preserve(Path(b)/name)
for item in M:
 rel=Path(item['path']);assert sha(R/rel)==item['original_sha256'];assert sha(O/'corrected'/rel)==item['corrected_sha256'];replace(rel,(O/'corrected'/rel).read_bytes())
for b in batches:
 rel=Path(b)/'review_measure.py';s=(R/rel).read_text();old='depth_ppt=pars[2]*1000,duration_days=pars[4]';new='depth_ppt=pars[2]*1000*min(1,pars[4]/(2*max(pars[5],1e-5))),trapezoid_depth_parameter_ppt=pars[2]*1000,fitted_ingress_days=pars[5],duration_days=pars[4]';assert s.count(old)==1;replace(rel,s.replace(old,new).encode())
 note=f'''# Realized trapezoid depth correction — 2026-11-02

The cross-batch audit found that fitted trapezoid amplitude d overstates the actual model decrement when ingress k exceeds half-width w/2. Depth now means d*min(1,w/(2*k)). The original fit amplitude and ingress are retained explicitly. Original accepted evidence and prior SHA256SUMS/RESULTS bytes are preserved under ../depth-audit/originals/{b}/.

Exact original-function replay reproduced every event, timing, fit selection and secondary numeric field before correction. Across batches01–07, 11 primary event depths in eight targets and two median depths change; all 131 measured-secondary event/pooled values stay unchanged. No timing, width, quality mask, verdict or capable-neighbor membership changes. Pixel deficit images and extracted photon values stay unchanged; the two affected neighbor flux-budget proxies are rescaled only. Original helper audit attribution is retained; this note is a separate correction supplement.

See ../depth-audit/README.md, changed-events.csv, verification.json and neighbors.json for exact values, source mapping and materiality. Raw event plots/contact sheets are refreshed only where displayed depth annotations changed.
'''
 replace(Path(b)/'DEPTH-CORRECTION.md',note.encode())
for b in ['batch03','batch06']:
 rel=Path(b)/'raw-contact.png';old=Image.open(R/rel);canvas=Image.new('RGB',old.size,'white');cw=old.width//2;ch=old.height//5
 rows=list(csv.DictReader(open(R/b/'queue.csv')))
 # Existing contacts use ascending TIC order; retain it.
 rows=sorted(rows,key=lambda r:int(r['tic']))
 for i,row in enumerate(rows):
  im=Image.open(R/b/row['tic']/'raw-events.png').convert('RGB');im.thumbnail((cw,ch));canvas.paste(im,((i%2)*cw,(i//2)*ch))
 import io
 buf=io.BytesIO();canvas.save(buf,format='PNG');replace(rel,buf.getvalue())
for b in batches:
 rel=Path(b)/'SHA256SUMS.json';original=json.load(open(O/'originals'/rel));H={}
 def excluded(p):return p.name=='SHA256SUMS.json' or p.name.startswith('root-') or p.name.startswith('helper-final') or p.name in ['final-hash-verification.json','final-validation.json','final-verification.json'] or '__pycache__'in p.parts
 for name in original:
  p=(R/b/name).resolve()
  if p.exists() and not excluded(p):H[name]=sha(p)
 for p in (R/b).rglob('*'):
  if p.is_file() and not excluded(p):H[p.relative_to(R/b).as_posix()]=sha(p)
 replace(rel,(json.dumps(dict(sorted(H.items())),indent=2)+'\n').encode())
(O/'applied-manifest.json').write_text(json.dumps(changes,indent=2)+'\n')
(O/'originals-manifest.json').write_text(json.dumps({p.relative_to(O/'originals').as_posix():sha(p)for p in (O/'originals').rglob('*')if p.is_file()},indent=2)+'\n')
print('Applied',len(changes),'bounded paths; originals and manifests retained.')
