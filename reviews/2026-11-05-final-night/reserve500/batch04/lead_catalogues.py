import json,csv,hashlib
from pathlib import Path
b=Path(__file__).resolve().parent;c=b.parent/'shared-catalogues';names=['target-results.json','local-table-matches-60arcsec.json','literature-adjudication.json','ROOT-CATALOGUE-SEAL.json','kebc-toi-matches.json','pending-gaia-simbad-receipts.json'];files={n:json.loads((c/n).read_text()) for n in names};hashes={n:hashlib.sha256((c/n).read_bytes()).hexdigest() for n in names}
for name in ['gaia_eb-pending.csv','gaia_nss-pending.csv','simbad-pending.csv']:hashes[name]=hashlib.sha256((c/name).read_bytes()).hexdigest()
for row in csv.DictReader((b/'queue.csv').open()):
 tic=row['tic'];r={n:([x for x in val if str(x.get('tic',''))==tic] if isinstance(val,list) else val) for n,val in files.items()}
 (b/tic/'lead-central-catalogue-receipts.json').write_text(json.dumps({'tic':tic,'central_path':str(c),'source_sha256':hashes,'receipts':r,'scope':'Seven source groups in methods2.7; source-specific nearby entries adjudicated separately. Success is scoped; unavailable remains unknown. Generic RS variability is not prior eclipsing classification.'},indent=2))
 print(tic,[(k,len(v)) for k,v in r.items() if isinstance(v,list)])
