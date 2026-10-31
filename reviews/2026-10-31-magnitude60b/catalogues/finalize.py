import json,csv,hashlib,urllib.request,urllib.parse
from pathlib import Path
from datetime import datetime,timezone
p=Path(__file__).parent; t=json.loads((p/'targets-selected.json').read_text());base=Path('[local path omitted] 5.1/made/paper/work/novelty-reconciliation/chopard-evidence/extracted/gaia-dr3-edge-on-orbits-tess-eclipses-v1.2.0');out={'checked_utc':datetime.now(timezone.utc).isoformat(),'scope':'cached public v1.2.0 only; later releases not searched; embargo93 identities unknown','sources':[],'targets':[]}
for name in ['track3_detail.csv','vetting/dossier.csv']:
 f=base/name; rows=list(csv.DictReader(open(f))); out['sources'].append({'path':str(f),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'rows':len(rows)})
 for tic,x in t.items():
  g=x['gaia']['source_id']; matches=[r for r in rows if r.get('source_id')==g or r.get('TIC')==tic];out['targets'].append({'tic':tic,'gaia_dr3':g,'table':name,'matches':matches,'outcome':'exact overlap' if matches else 'no exact overlap'})
(p/'chopard-comparison-summary.json').write_text(json.dumps(out,indent=2))
url='http[local path omitted]';q='SELECT * FROM gaiadr3.vari_eclipsing_binary WHERE source_id IN (46626164993792)'; r={'query':q,'url':url,'utc':datetime.now(timezone.utc).isoformat()}
try:
 raw=urllib.request.urlopen(url,urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q}).encode(),timeout=25).read(); assert b'46626164993792' in raw;(p/'control-gaia-eb-exact.csv').write_bytes(raw);r.update(status='success',sha256=hashlib.sha256(raw).hexdigest())
except Exception as e:r.update(status='unavailable',error=repr(e))
(p/'control-gaia-eb-exact-receipt.json').write_text(json.dumps(r,indent=2));print(r)
