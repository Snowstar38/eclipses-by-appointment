"""Reproduce the queue-locked identity, prior-source and bounded remote audit."""
import csv, hashlib, html, importlib.util, io, json, math, re, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
OLD=Path('[local-path-redacted]')
EXT=Path('[local-path-redacted]')
QPATH=BASE/'queue.csv'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
Q=list(csv.DictReader(QPATH.open(encoding='utf-8-sig',newline='')))
SEAL=json.loads((BASE/'queue-seal.json').read_text())
assert sha(QPATH)==SEAL['queue_sha256'] and len(Q)==10
assert [x['sample_id'] for x in Q]==[f'N{i:03d}' for i in range(1,11)]
assert [int(x['priority_rank']) for x in Q]==list(range(101,111))
assert len({x['tic'] for x in Q})==len({x['gaia_dr3'] for x in Q})==10
def write(name,obj): (HERE/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def table(p): return list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))
def sep(a,b,c,d):
    a,b,c,d=map(math.radians,(float(a),float(b),float(c),float(d)))
    h=math.sin((b-d)/2)**2+math.cos(b)*math.cos(d)*math.sin((a-c)/2)**2
    return math.degrees(2*math.asin(min(1,math.sqrt(h))))*3600

sources={}
def source(label,p):
    sources[label]={'path':str(p),'sha256':sha(p)}
    return p
prp=source('prsa',EXT/'catalogue-archives/mast-prsa.csv')
ijp=source('ijspeert',EXT/'catalogue-archives/ijspeert-identities.csv')
pr=table(prp); ij=table(ijp)
assert len(pr)==4584 and len(ij)==69057
assert sha(prp)=='97e81f6c01716a431379ab6bd37d1182b611a485107110e0eba830f817ba7a8f'
assert sha(ijp)=='8cc6a6b97bc21195d0564659d637f6928aec4364baa7bfa86f82e015742ef75e'
hist=[]
for name in ('review412','review9','review_cached10','review_cached5','review_unmatched10','review_unmatched2'):
    p=source(name,EXT/name/'RESULTS.csv'); hist.append((str(p),table(p)))
for name,p in [('ledger',EXT/'accounting/accepted-proposal-ledger.csv'),('pending',EXT/'PENDING-NOVELTY.csv'),('accepted100',OLD.parent/'accepted-results.csv')]:
    p=source(name,p);hist.append((str(p),table(p)))
sky=source('sky_catalogue',Path('[local-path-redacted]')).read_text(encoding='utf-8')

# Prior audit's local-source parsers are reused without writing to its sealed directory.
spec=importlib.util.spec_from_file_location('prior_local',OLD/'local_catalogues.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);mod.HERE=HERE
identity=[dict(tic=x['tic'],gaia_dr3=x['gaia_dr3'],ra=float(x['ra_deg']),dec=float(x['dec_deg'])) for x in Q]
hb=mod.heartbeat(identity);ch=mod.chopard(identity);tm=mod.tarrants_mendes(identity)
for label,p in [('heartbeat_source',Path(hb['sources'][0]['path'])),('chopard_track',Path(ch['sources'][0]['path'])),('chopard_dossier',Path(ch['sources'][1]['path'])),('tarrants_crossmatch',Path(tm['source']['path'])),('tarrants_primary',Path(tm['primary_html_exact_gaia_check']['path']))]:source(label,p)

# Two service endpoints, one known-source positive control each. No fanout after failure.
control=[]
for host in ('vizier.cfa.harvard.edu','vizier.cds.unistra.fr'):
    url=f'https://{host}/viz-bin/asu-tsv?-source=B%2Fvsx%2Fvsx&-c=0.00006+-75.86906&-c.rs=60&-out.max=100&-out.all=&-out.add=_r'
    rec={'url':url,'timeout_seconds':8,'queried_utc':datetime.now(timezone.utc).isoformat(),'positive_control':'known VSX source','queue_sha256':sha(QPATH)}
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Astra-next10-audit/1.0'}),timeout=8) as r:raw=r.read(1000001)
        if len(raw)>1000000 or b'VizieR' not in raw or b'#ERROR' in raw or b'No object found' in raw:raise ValueError('invalid positive-control response')
        p=HERE/f'vsx-control-{host}.tsv';p.write_bytes(raw)
        rec.update(status='success',raw=str(p),sha256=sha(p))
    except Exception as e:rec.update(status='unavailable',error=repr(e))
    control.append(rec)
    if rec['status']=='success':break
write('vizier-controls.json',control)

# Fresh exact Gaia/SIMBAD bulk requests for this exact identity set.
ids=sorted(x['gaia_dr3'] for x in Q); remote={}
jobs=[(f'gaia_{label}','https://gaia.ari.uni-heidelberg.de/tap/sync',f'SELECT * FROM gaiadr3.{tab} WHERE source_id IN ('+','.join(ids)+')','source_id') for label,tab in [('eb','vari_eclipsing_binary'),('summary','vari_summary'),('nss','nss_two_body_orbit')]]
query='SELECT ident.id,basic.main_id,basic.otype,basic.ra,basic.dec FROM ident JOIN basic ON ident.oidref=basic.oid WHERE ident.id IN ('+','.join("'Gaia DR3 "+x+"'" for x in ids)+')'
jobs.append(('simbad','https://simbad.cfa.harvard.edu/simbad/sim-tap/sync',query,'id'))
for label,url,query,key in jobs:
    body=urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':query}).encode()
    rec={'url':url,'body_sha256':hashlib.sha256(body).hexdigest(),'timeout_seconds':8,'queried_utc':datetime.now(timezone.utc).isoformat(),'queue_sha256':sha(QPATH)}
    try:
        with urllib.request.urlopen(urllib.request.Request(url,data=body,headers={'User-Agent':'Astra-next10-audit/1.0'}),timeout=8) as r:raw=r.read(2000001)
        if len(raw)>2000000:raise ValueError('response exceeds limit')
        txt=raw.decode('utf-8-sig');data=list(csv.DictReader(io.StringIO(txt)))
        if key not in (data[0].keys() if data else txt.splitlines()[0].split(',')):raise ValueError('invalid CSV layout')
        allowed=set(ids) if label!='simbad' else {'Gaia DR3 '+x for x in ids}
        if any(x[key] not in allowed for x in data):raise ValueError('unexpected source identity')
        p=HERE/(label+'.csv');p.write_bytes(raw);rec.update(status='success',raw=str(p),sha256=sha(p),rows=len(data))
    except Exception as e:rec.update(status='unavailable',error=repr(e))
    remote[label]=rec
write('remote-receipts.json',remote)

rows=[]
for q in Q:
    tic=q['tic'];gaia=q['gaia_dr3'];ra=q['ra_deg'];dec=q['dec_deg']
    prior=[{'path':p,'row':r} for p,rr in hist for r in rr if r.get('tic')==tic]
    if re.search(r'(?<!\d)'+tic+r'(?!\d)',sky):prior.append({'path':str(Path('[local-path-redacted]')),'match':'exact TIC token; context required'})
    pe=[r for r in pr if r['tess_id']==tic]
    ie=[r for r in ij if r['TIC']==tic or r['GaiaDR3']==gaia]
    pn=[{'tic':r['tess_id'],'separation_arcsec':round(sep(ra,dec,r['ra'],r['dec']),4)} for r in pr if sep(ra,dec,r['ra'],r['dec'])<=5]
    inn=[{'tic':r['TIC'],'gaia_dr3':r['GaiaDR3'],'separation_arcsec':round(sep(ra,dec,r['RAJ2000'],r['DEJ2000']),4)} for r in ij if sep(ra,dec,r['RAJ2000'],r['DEJ2000'])<=5]
    rremote={}
    for name,rec in remote.items():
        rr=table(Path(rec['raw'])) if rec['status']=='success' else []
        rremote[name]={'status':rec['status'],'exact_rows':[r for r in rr if r.get('source_id',r.get('id','')) in (gaia,'Gaia DR3 '+gaia)]}
    alerts=[]
    if pe:alerts.append('Prsa exact TIC')
    if ie:alerts.append('IJspeert exact TIC/Gaia')
    if ch['targets'][tic]:alerts.append('Chopard public v1.2.0')
    if tm['targets'][tic]:alerts.append('Tarrants-Mendes primary/crossmatch')
    if any(x.get('paper')=='Callahan+2025' and x.get('eclipses_flag')=='True' for x in hb['targets'][tic]):alerts.append('Callahan 2025 eclipse flag')
    if prior:alerts.append('prior review/register identity')
    if rremote['gaia_eb']['exact_rows']:alerts.append('Gaia DR3 EB exact')
    if any(x.get('otype') in ('EB*','Al*','bL*','WU*') for x in rremote['simbad']['exact_rows']):alerts.append('SIMBAD EB type exact')
    rows.append({'sample_id':q['sample_id'],'tic':tic,'gaia_dr3':gaia,'primary_prsa_exact':pe,'primary_ijspeert_exact':ie,'primary_prsa_5arcsec':pn,'primary_ijspeert_5arcsec':inn,'prior_review_or_register':prior,'heartbeat':hb['targets'][tic],'chopard':ch['targets'][tic],'tarrants_mendes':tm['targets'][tic],'remote':rremote,'prior_alerts':alerts,'novelty_status':'KNOWN PRIOR IDENTITY; interpretation required' if alerts else 'UNKNOWN; incomplete catalogue gates','physical_verdict':'independent batch review'})
write('target-evidence.json',{'queue_sha256':sha(QPATH),'source_hashes':sources,'vizier_controls':control,'remote_receipts':'remote-receipts.json','targets':rows})
with (HERE/'TARGET-STATUS.csv').open('w',encoding='utf-8',newline='') as f:
    fields=['sample_id','tic','gaia_dr3','novelty_status','prior_alerts','prsa_exact','ijspeert_exact','prsa_5arcsec','ijspeert_5arcsec','gaia_eb','gaia_summary','gaia_nss','simbad','vsx_asassn_kostov_gates']
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for r in rows:w.writerow({'sample_id':r['sample_id'],'tic':r['tic'],'gaia_dr3':r['gaia_dr3'],'novelty_status':r['novelty_status'],'prior_alerts':'; '.join(r['prior_alerts']),'prsa_exact':len(r['primary_prsa_exact']),'ijspeert_exact':len(r['primary_ijspeert_exact']),'prsa_5arcsec':len(r['primary_prsa_5arcsec']),'ijspeert_5arcsec':len(r['primary_ijspeert_5arcsec']),**{k:r['remote'][k]['status'] for k in ('gaia_eb','gaia_summary','gaia_nss','simbad')},'vsx_asassn_kostov_gates':'UNKNOWN; not checked per target'})
print(json.dumps({'queue_sha256':sha(QPATH),'targets':len(rows),'alerts':[(r['sample_id'],r['tic'],r['prior_alerts']) for r in rows if r['prior_alerts']],'remote':{k:v['status'] for k,v in remote.items()},'vizier_control':[x['status'] for x in control]}))
