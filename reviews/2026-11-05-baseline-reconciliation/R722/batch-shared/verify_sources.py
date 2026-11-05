import csv,hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent
seal=json.loads((B/'queue-seal.json').read_text());s=json.loads((B/'SOURCE-SNAPSHOT.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(B/'queue.csv')==seal['sha256']
assert sha(B/'SOURCE-SNAPSHOT.json')==seal['snapshot_sha256']
q=list(csv.DictReader((B/'queue.csv').open()));assert [r['tic'] for r in q]==seal['tics']
checks=[]
for p,h in seal['source_hashes'].items():
 f=B.parent/p; assert sha(f)==h,str(f);checks.append(dict(path=str(f),sha256=h))
for r in q:
 t=s[r['tic']]['target'];assert str(t['gaia']['source_id'])==r['gaia_dr3_source_id']
 for rec in t['file_receipts']:
  f=Path(rec['path']);assert sha(f)==rec['sha256'],str(f)
  from astropy.io import fits
  with fits.open(f) as hd:
   ident=str(hd[0].header.get('TICID',hd[0].header.get('TIC_ID','')))
   # QLP headers use TICID; exact queue target also encoded in receipt URL.
   assert (not ident or ident==r['tic']), (ident,r['tic'])
   assert int(hd[0].header.get('SECTOR',rec['sector']))==rec['sector']
  checks.append(dict(path=str(f),sha256=rec['sha256'],tic=r['tic'],sector=rec['sector'],header_tic=ident))
(B/'source-verification.json').write_text(json.dumps(dict(queue_sha256=seal['sha256'],snapshot_sha256=seal['snapshot_sha256'],checks=checks,passed=True),indent=2)+'\n')
print(len(q),len(checks),'verified')
