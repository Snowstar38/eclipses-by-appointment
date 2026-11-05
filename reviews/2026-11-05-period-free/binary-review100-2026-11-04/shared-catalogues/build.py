"""Bounded, reproducible identity/novelty audit of the sealed H001-H100 queue."""
import csv
import hashlib
import json
import math
import os
import re
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
OLD = Path('[local-path-redacted]')
ARCH = OLD / 'catalogue-archives'
QUEUE = BASE / 'queue.csv'
SEAL = json.loads((BASE / 'queue-seal.json').read_text(encoding='utf-8'))
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(QUEUE) == SEAL['queue_sha256']
Q = list(csv.DictReader(QUEUE.open(encoding='utf-8-sig', newline='')))
assert len(Q) == 100 and len({x['tic'] for x in Q}) == 100
TICS = {x['tic'] for x in Q}

def write(name, obj):
    (HERE / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def angle(ra1, dec1, ra2, dec2):
    a,b,c,d = map(math.radians, (ra1,dec1,ra2,dec2))
    h=math.sin((b-d)/2)**2+math.cos(b)*math.cos(d)*math.sin((a-c)/2)**2
    return math.degrees(2*math.asin(min(1,math.sqrt(h))))*3600

def table(path):
    return list(csv.DictReader(path.open(encoding='utf-8-sig', newline='')))

prsa_path=ARCH/'mast-prsa.csv'; ij_path=ARCH/'ijspeert-identities.csv'
prsa=table(prsa_path); ij=table(ij_path)
assert len(prsa)==4584 and len(ij)==69057
sources={
 'prsa':{'path':str(prsa_path),'sha256':sha(prsa_path),'rows':len(prsa),'receipt':str(prsa_path)+'.receipt.json'},
 'ijspeert':{'path':str(ij_path),'sha256':sha(ij_path),'rows':len(ij),'receipt':str(ARCH/'ijspeert-identity-table.receipt.json')},
 'queue':{'path':str(QUEUE),'sha256':sha(QUEUE),'rows':len(Q)}
}
assert sources['prsa']['sha256']=='97e81f6c01716a431379ab6bd37d1182b611a485107110e0eba830f817ba7a8f'
assert sources['ijspeert']['sha256']=='8cc6a6b97bc21195d0564659d637f6928aec4364baa7bfa86f82e015742ef75e'

# Search historical verdicts and the live ledger by exact TIC; a prior review must be visible.
prior={t:[] for t in TICS}; prior_sources=[]
for name in ('review412','review9','review_cached10','review_cached5','review_unmatched10','review_unmatched2'):
    p=OLD/name/'RESULTS.csv'; rows=table(p)
    prior_sources.append({'path':str(p),'sha256':sha(p),'rows':len(rows)})
    for row in rows:
        if row.get('tic') in prior: prior[row['tic']].append({'source':str(p),'row':row})
for p in (OLD/'accounting/accepted-proposal-ledger.csv',OLD/'PENDING-NOVELTY.csv'):
    rows=table(p); prior_sources.append({'path':str(p),'sha256':sha(p),'rows':len(rows)})
    for row in rows:
        if row.get('tic') in prior: prior[row['tic']].append({'source':str(p),'row':row})
sky=Path('[local-path-redacted]')
sky_text=sky.read_text(encoding='utf-8')
prior_sources.append({'path':str(sky),'sha256':sha(sky)})
for tic in TICS:
    if re.search(r'(?<!\d)'+tic+r'(?!\d)',sky_text):
        prior[tic].append({'source':str(sky),'match':'exact TIC token; inspect context'})

# Reuse a historical target cone only if its raw bytes and target-specific identity/scope agree.
cache={t:{} for t in TICS}; seen=0
for root,dirs,files in os.walk(OLD):
    dirs[:]=[d for d in dirs if d in ('receipts','raw') or not (d.startswith('__') or d in ('primary-cache','mast-prsa-cache','controls-cache','original-receipts'))]
    if Path(root).name!='receipts': continue
    for f in files:
        m=re.fullmatch(r'(\d+)-(vsx|asassn|kostov2025_table[34]|prsa2022|ijspeert2024)\.json',f)
        if not m or m[1] not in cache: continue
        p=Path(root)/f
        try: rec=json.loads(p.read_text(encoding='utf-8'))
        except (ValueError,UnicodeError): continue
        if rec.get('status')!='success' or rec.get('network_attempted') is False: continue
        raw=p.parent.parent/'raw'/(p.stem+'.txt')
        if not raw.is_file() or sha(raw)!=rec.get('sha256'): continue
        q=next(x for x in Q if x['tic']==m[1]); url=urllib.parse.urlparse(rec.get('url',''))
        params=urllib.parse.parse_qs(url.query)
        try:
            ra,dec=map(float,params['-c'][0].split()); radius=float(params['-c.rs'][0])
        except (KeyError,ValueError): continue
        expected=5 if m[2] in ('prsa2022','ijspeert2024') else 60
        if angle(ra,dec,float(q['ra_deg']),float(q['dec_deg']))>0.01 or radius!=expected: continue
        entry={'receipt':str(p),'receipt_sha256':sha(p),'raw':str(raw),'raw_sha256':sha(raw),'bytes':raw.stat().st_size,'url':rec['url']}
        cache[m[1]].setdefault(m[2],entry);seen+=1

# This one service probe is a positive control. Failure prevents treating remote gates as negatives.
probe_url='https://vizier.cfa.harvard.edu/viz-bin/asu-tsv?-source=B%2Fvsx%2Fvsx&-c=0.00006+-75.86906&-c.rs=60&-out.max=100&-out.all=&-out.add=_r'
probe={'url':probe_url,'positive_control':'VSX known source at 0.00006 -75.86906','timeout_seconds':8,'queried_utc':datetime.now(timezone.utc).isoformat()}
try:
    with urllib.request.urlopen(urllib.request.Request(probe_url,headers={'User-Agent':'Astra-catalogue-review100/1.0'}),timeout=8) as response:
        raw=response.read(1000001)
    if len(raw)>1000000 or b'VizieR' not in raw or b'#ERROR' in raw: raise ValueError('invalid or overlong positive-control response')
    p=HERE/'positive-control-vsx.tsv';p.write_bytes(raw)
    probe.update(status='success',raw=str(p),sha256=sha(p),bytes=len(raw))
except Exception as exc:
    probe.update(status='unavailable',error=repr(exc))
write('remote-control.json',probe)

records=[]
for q in Q:
    tic=q['tic'];gaia=q['gaia_dr3'];ra=float(q['ra_deg']);dec=float(q['dec_deg'])
    prsa_exact=[x for x in prsa if x['tess_id']==tic]
    ij_exact=[x for x in ij if x['TIC']==tic or x['GaiaDR3']==gaia]
    prsa_near=[{'tic':x['tess_id'],'separation_arcsec':round(angle(ra,dec,float(x['ra']),float(x['dec'])),4)} for x in prsa if angle(ra,dec,float(x['ra']),float(x['dec']))<=5]
    ij_near=[{'tic':x['TIC'],'gaia_dr3':x['GaiaDR3'],'separation_arcsec':round(angle(ra,dec,float(x['RAJ2000']),float(x['DEJ2000'])),4)} for x in ij if angle(ra,dec,float(x['RAJ2000']),float(x['DEJ2000']))<=5]
    status='known prior candidate; adjudication required' if prsa_exact or ij_exact or prior[tic] else 'novelty unknown: incomplete remote gates'
    records.append({'sample_id':q['sample_id'],'tic':tic,'gaia_dr3':gaia,'ra_deg':ra,'dec_deg':dec,'known_prior_exact_note':q['known_prior_exact_note'],'novelty_status':status,'primary_prsa_exact_rows':prsa_exact,'primary_ijspeert_exact_rows':ij_exact,'primary_prsa_5arcsec_rows':prsa_near,'primary_ijspeert_5arcsec_rows':ij_near,'prior_review_or_register':prior[tic],'verified_historical_cone_receipts':cache[tic],'remote_status':'control unavailable; unqueried scopes remain unknown' if probe['status']!='success' else 'control success; target remote scopes unqueried'})
write('target-evidence.json',{'scope':'exact TIC/Gaia and 5 arcsec primary cones; target-specific historical receipts verified; remote unknown unless explicit successful target receipt','sources':sources,'prior_sources':prior_sources,'remote_control':'remote-control.json','targets':records})
with (HERE/'TARGET-STATUS.csv').open('w',encoding='utf-8',newline='') as f:
    fields=('sample_id','tic','gaia_dr3','ra_deg','dec_deg','novelty_status','prsa_exact','ijspeert_exact','prsa_5arcsec','ijspeert_5arcsec','prior_review_or_register','verified_cached_cones','remote_status')
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for x in records:
        w.writerow({'sample_id':x['sample_id'],'tic':x['tic'],'gaia_dr3':x['gaia_dr3'],'ra_deg':x['ra_deg'],'dec_deg':x['dec_deg'],'novelty_status':x['novelty_status'],'prsa_exact':len(x['primary_prsa_exact_rows']),'ijspeert_exact':len(x['primary_ijspeert_exact_rows']),'prsa_5arcsec':len(x['primary_prsa_5arcsec_rows']),'ijspeert_5arcsec':len(x['primary_ijspeert_5arcsec_rows']),'prior_review_or_register':len(x['prior_review_or_register']),'verified_cached_cones':','.join(sorted(x['verified_historical_cone_receipts'])),'remote_status':x['remote_status']})
print(json.dumps({'targets':len(records),'primary_exact':sum(bool(x['primary_prsa_exact_rows'] or x['primary_ijspeert_exact_rows']) for x in records),'primary_near':sum(bool(x['primary_prsa_5arcsec_rows'] or x['primary_ijspeert_5arcsec_rows']) for x in records),'prior':sum(bool(x['prior_review_or_register']) for x in records),'cached_receipts':seen,'control':probe['status']}))
