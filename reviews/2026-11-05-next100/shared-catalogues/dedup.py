import csv,json,hashlib,math
from pathlib import Path
H=Path(__file__).resolve().parent; Q=H.parent/'queue.csv'; B=Path('[local-path-redacted]');
def read(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def sep(a,b,c,d):
 a,b,c,d=map(math.radians,map(float,(a,b,c,d)));h=math.sin((b-d)/2)**2+math.cos(b)*math.cos(d)*math.sin((a-c)/2)**2;return math.degrees(2*math.asin(min(1,math.sqrt(h))))*3600
q=read(Q); l=read(B/'accepted-ledger.csv'); coordpath=Path('[local-path-redacted]'); coords=read(coordpath); claims=[x for x in l if x['claim_member'].lower()=='true']; ids={x['tic'] for x in claims}; gs={x['gaia_dr3'] for x in claims if x['gaia_dr3']}; cc=[x for x in coords if x['tic'] in ids or x.get('gaia_dr3') and x['gaia_dr3'] in gs];
result={'queue_sha256':sha(Q),'ledger_sha256':sha(B/'accepted-ledger.csv'),'coordinates_sha256':sha(coordpath),'claims':len(claims),'claim_coordinate_rows':len(cc),'queue_count':len(q),'radius_arcsec':120,'targets':{}}
for i,r in enumerate(q):
 result['targets'][r['sample_id']]={'tic':r['tic'],'gaia_dr3':r['gaia_dr3'],'baseline_exact_tic':[x['review_id'] for x in claims if x['tic']==r['tic']],'baseline_exact_gaia':[x['review_id'] for x in claims if r['gaia_dr3'] and x['gaia_dr3']==r['gaia_dr3']],'baseline_within_120arcsec':[{'tic':x['tic'],'gaia_dr3':x.get('gaia_dr3',''),'arcsec':round(sep(r['ra_deg'],r['dec_deg'],x['ra_deg'],x['dec_deg']),4)} for x in cc if sep(r['ra_deg'],r['dec_deg'],x['ra_deg'],x['dec_deg'])<=120], 'queue_within_120arcsec':[{'sample_id':x['sample_id'],'tic':x['tic'],'arcsec':round(sep(r['ra_deg'],r['dec_deg'],x['ra_deg'],x['dec_deg']),4)} for x in q if x['sample_id']!=r['sample_id'] and sep(r['ra_deg'],r['dec_deg'],x['ra_deg'],x['dec_deg'])<=120]}
(H/'dedup.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print('claims',len(claims),'coords',len(cc),'alerts',[(k,v) for k,v in result['targets'].items() if any(v[x] for x in ('baseline_exact_tic','baseline_exact_gaia','baseline_within_120arcsec','queue_within_120arcsec'))])
