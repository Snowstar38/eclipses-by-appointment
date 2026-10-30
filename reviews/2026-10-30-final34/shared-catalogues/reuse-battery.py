import json,hashlib,ast,re,urllib.parse
from pathlib import Path
p=Path(__file__).parent;t=json.loads((p/'targets-selected.json').read_text());root=Path('[local working path omitted]')
tabs=['J/ApJS/258/16/tess-ebs','J/A+A/691/A242/obaf-eb1','J/ApJS/279/50/table3','J/ApJS/279/50/table4']; results=[];missing=[]
for tic,x in t.items():
 candidates=[]
 for f in sorted(root.glob('*ebcats*out*.txt')):
  for line in f.read_text(errors='replace').splitlines():
   if line.startswith(tic+' | ') and 'FAILED' not in line and 'ERROR' not in line:
    candidates.append((f,line))
 if not candidates:missing.append(tic);continue
 f,line=candidates[-1];raw=line.split(' | ',1)[1]; entries={}
 for name, row in re.findall(r'(tess-ebs|obaf-eb1|table[234]) (\{[^}]*\})',raw): entries[name]=ast.literal_eval(row)
 assert raw=='none of the vetted/unvetted EB tables' or entries,(tic,raw)
 for tb in tabs:
  url='https://vizier.cds.unistra.fr/viz-bin/asu-tsv?'+urllib.parse.urlencode({'-source':tb,'-c':f"{x['ra']} {x['dec']}",'-c.rs':5,'-out.max':2,'-out.all':'','-out.add':'_r'})
  results.append(dict(tic=tic,table=tb,status='success',rows=[entries[tb.split('/')[-1]]] if tb.split('/')[-1] in entries else [],historical=True,source_file=str(f),source_sha256=hashlib.sha256(f.read_bytes()).hexdigest(),source_line=line,url=url,queried_at_utc=None,timestamp_note='Historical successful receipt; original UTC not recorded. Reuse does not imply fresh query.'))
(p/'eb-battery-receipts.json').write_text(json.dumps(results,indent=2));print('reused',len(results),'missing',missing,'matches',[(r['tic'],r['table'],r['rows']) for r in results if r['rows']])
