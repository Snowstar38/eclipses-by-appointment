"""Frozen next400-source faint-band feasibility and raw-event harvest; all failures retained."""
from pathlib import Path
import csv,json,hashlib,requests,datetime,concurrent.futures,io,sys,shutil
from collections import defaultdict,Counter
W=Path(__file__).resolve().parent/'fresh-band-next400';W.mkdir(exist_ok=True)
H=Path('[workspace]');A=H/'Astra/made'; OLD=A/'toward1000-2026-11-03'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p):return list(csv.DictReader(p.open(encoding='utf-8-sig')))
def save(name,obj):(W/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf8')
def freeze():
    nss=OLD/'search256/sources/nss.csv';historical=OLD/'search256/sources/targets.json'
    prior144=OLD/'pilot48/sources/fresh-preregister-144.json';prior256=OLD/'search256/fresh-preregister-256.json'
    ext=A/'binary-extension-2026-11-04/REVISIT-REGISTER.csv';ledger=A/'final-night-2026-11-05/accepted-ledger.csv'
    history=json.loads(historical.read_text()); exclusions=defaultdict(list)
    for v in history.values():exclusions[str(v['gaia']['source_id'])].append('historical_appointment_target')
    for f in (prior144,prior256):
        for r in json.loads(f.read_text())['selected']:exclusions[r['source_id']].append(f.parent.name+'/'+f.name)
    for r in json.loads((A/'final-night-2026-11-05/fresh-band/selection.json').read_text())['selected']:exclusions[r['source_id']].append('initial_fresh100')
    for r in rows(ext):exclusions[r['gaia_dr3']].append('20-24_extension')
    for r in rows(ledger):
        if r['gaia_dr3']:exclusions[r['gaia_dr3']].append('current_review_ledger')
    parent=[r for r in rows(nss) if 11.5<=float(r['phot_g_mean_mag'])<12 and 20<=float(r['period'])<60]
    eligible=[r for r in parent if not exclusions[r['source_id']] and not r['veb']]
    picked=[];strata=[]
    for lo,hi,n in [(20,24,50),(24,40,175),(40,60,175)]:
        pool=[r for r in eligible if lo<=float(r['period'])<hi]
        pool.sort(key=lambda r:hashlib.sha256(('final-night-band-v1:'+r['source_id']).encode()).hexdigest())
        assert len(pool)>=n
        picked+=pool[:n];strata.append({'period_range':[lo,hi],'eligible':len(pool),'selected':n})
    assert len(picked)==400 and len({r['source_id'] for r in picked})==400
    save('selection.json',{'rule':'Hash-ranked Gaia IDs within fixed period strata, before new TESS inspection; exclude historical appointment targets, selected144, selected256, 20-24 extension and current physical ledger by available DR3 IDs. TIC deduplication follows mapping. No substitutions. At most8 QLP sectors per target (earliest2/latest6), all availability retained. No coverage/detection probability interpretation.','parent':len(parent),'eligible':len(eligible),'strata':strata,'selected':picked,'source_hashes':{str(p):sha(p) for p in (nss,historical,prior144,prior256,ext,ledger)}})
    save('all-parent-dispositions.json',[{'source_id':r['source_id'],'reasons':exclusions[r['source_id']]+(['Gaia_EB_control'] if r['veb'] else []),'selected':r in picked} for r in parent])
    print('Frozen',len(parent),len(eligible),strata,flush=True)
def request_receipt(name,url,params=None,data=None,timeout=40):
    out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':url,'params':params,'data':data}
    try:
        r=requests.post(url,data=data,timeout=(10,timeout)) if data is not None else requests.get(url,params=params,timeout=(10,timeout))
        (W/(name+'.response')).write_bytes(r.content);out.update(http_status=r.status_code,sha256=hashlib.sha256(r.content).hexdigest(),bytes=len(r.content));r.raise_for_status();out['status']='HTTP_SUCCESS'
        save(name+'.receipt.json',out);return r
    except Exception as e:
        out.update(status='unavailable',error=repr(e));save(name+'.receipt.json',out);return None
def invoke(name,req):
    r=request_receipt(name,'https://mast.stsci.edu/api/v0/invoke',data={'request':json.dumps(req)})
    if r is None:return None
    try:
        j=r.json();assert j.get('status')=='COMPLETE' and j.get('paging',{}).get('pagesFiltered',1)<=1;return j
    except Exception:return None
def identities():
    selected=json.loads((W/'selection.json').read_text())['selected']
    q='SELECT dr3_source_id,dr2_source_id,angular_distance,magnitude_difference FROM gaiadr3.dr2_neighbourhood WHERE dr3_source_id IN ('+','.join(r['source_id'] for r in selected)+')'
    params={'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q}
    r=request_receipt('gaia-neighbour','https://gaia.ari.uni-heidelberg.de/tap/sync',data=params,timeout=50)
    nn=defaultdict(list)
    if r is not None and 'dr3_source_id' in r.text:
        for v in csv.DictReader(io.StringIO(r.text)):nn[v['dr3_source_id']].append(v)
    def cone(g):
        sid=g['source_id'];j=invoke('tic-'+sid,{'service':'Mast.Catalogs.Tic.Cone','params':{'ra':float(g['ra']),'dec':float(g['dec']),'radius':20/3600},'format':'json','pagesize':5000,'page':1})
        match=[]
        if j is not None and len(nn[sid])==1:match=[t for t in j['data'] if str(t.get('GAIA'))==nn[sid][0]['dr2_source_id']]
        return {'gaia':g,'neighborhood':nn[sid],'matches':match,'status':'unique_identity' if len(match)==1 else 'unresolved_identity','cone_success':j is not None}
    with concurrent.futures.ThreadPoolExecutor(3) as ex:out=list(ex.map(cone,selected))
    counts=Counter(str(v['matches'][0]['ID']) for v in out if v['status']=='unique_identity')
    ledger={r['tic'] for r in rows(A/'final-night-2026-11-05/accepted-ledger.csv')}
    screened={str(json.loads(l)['tic']) for l in (H/'sky/data/qlp-sb-p20-60/results.jsonl').open()}
    for v in out:
        if v['status']=='unique_identity':
            tic=str(v['matches'][0]['ID']);v['tic']=tic
            if counts[tic]!=1:v['status']='shared_tic_ambiguous'
            elif tic in ledger or tic in screened:v['status']='historical_tic_overlap'
    save('identity-outcomes.json',out)
    eligible=[v['tic'] for v in out if v['status']=='unique_identity']
    j=invoke('qlp-inventory',{'service':'Mast.Caom.Filtered','format':'json','params':{'columns':'target_name,sequence_number,dataURL,provenance_name','filters':[{'paramName':'provenance_name','values':['QLP']},{'paramName':'target_name','values':eligible}]},'pagesize':50000,'page':1}) if eligible else None
    products=defaultdict(set)
    if j:
        for r in j['data']:
            if r.get('dataURL','').endswith('.fits'):products[str(r['target_name']).lstrip('0')].add((int(r['sequence_number']),r['dataURL']))
    targets={}
    for v in out:
        if v['status']!='unique_identity':continue
        tic=v['tic'];allp=sorted(products[tic]);by={s:u for s,u in allp};sectors=sorted(by);chosen=sorted(set(sectors[:2]+sectors[-6:]))
        targets[tic]={'gaia':v['gaia'],'control':False,'ra':float(v['matches'][0]['ra']),'dec':float(v['matches'][0]['dec']),'qlp_all':allp,'qlp':[(s,by[s]) for s in chosen],'inventory_status':'success' if j else 'unavailable'}
    save('targets.json',targets);save('feasibility-summary.json',{'identity':dict(Counter(v['status'] for v in out)),'unique_tics':len(targets),'qlp_available':sum(bool(v['qlp']) for v in targets.values()),'qlp_files_selected':sum(len(v['qlp']) for v in targets.values()),'inventory_success':j is not None})
    print((W/'feasibility-summary.json').read_text(),flush=True)
def download():
    from astropy.io import fits
    targets=json.loads((W/'targets.json').read_text());D=W/'data';D.mkdir(exist_ok=True)
    old_controls=json.loads((OLD/'search256/controls-selected.json').read_text())['targets']
    for tic,v in old_controls.items():
        assert tic not in targets;targets[tic]=dict(v,control=True,qlp_all=v['qlp'],inventory_status='historical_positive_control')
    save('screen-targets.json',targets)
    jobs=[(tic,s,u) for tic,v in targets.items() for s,u in v['qlp']]
    def get(job):
        tic,s,u=job;p=D/f'{tic}_s{s:03d}.fits';rec={'tic':tic,'sector':s,'uri':u,'path':str(p)}
        try:
            if not p.exists():
                cached=H/'sky/data/qlp-sb-p20-60'/p.name
                if cached.exists():p.hardlink_to(cached);rec['reused']=True
                else:
                    assert shutil.disk_usage(D).free>8*1024**3,'8GB reserve reached'
                    r=requests.get('https://mast.stsci.edu/api/v0.1/Download/file',params={'uri':u},timeout=(10,60));r.raise_for_status()
                    tmp=p.with_suffix('.part');tmp.write_bytes(r.content)
                    with fits.open(tmp) as f:assert int(f[0].header['TICID'])==int(tic) and int(f[0].header['SECTOR'])==s
                    tmp.replace(p)
            with fits.open(p) as f:assert int(f[0].header['TICID'])==int(tic) and int(f[0].header['SECTOR'])==s
            rec.update(status='success',sha256=sha(p),bytes=p.stat().st_size)
        except Exception as e:rec.update(status='unavailable',error=repr(e))
        return rec
    receipts=[]
    with concurrent.futures.ThreadPoolExecutor(3) as ex,(W/'downloads.jsonl').open('w') as log:
        for i,r in enumerate(ex.map(get,jobs),1):
            receipts.append(r);log.write(json.dumps(r)+'\n');log.flush()
            if i%50==0:print('Downloaded',i,len(jobs),flush=True)
    save('downloads.json',receipts)
    for tic,v in targets.items():v['files']=[r for r in receipts if r['tic']==tic and r['status']=='success']
    save('population.json',{'targets':targets,'science':400,'controls':2,'selection_sha256':sha(W/'selection.json'),'downloads_sha256':sha(W/'downloads.json')})
    (D/'targets.json').write_text(json.dumps(targets),encoding='utf8')
    print('Download complete',Counter(r['status'] for r in receipts),flush=True)
def scan_one(pair):
    import importlib.util,os,numpy as np
    tic,tg=pair;sys.path.insert(0,str(OLD/'search256/sources'))
    os.environ['APPOINTMENTS_DATA']=str(W/'data');import appoint
    appoint.D=str(W/'data');appoint.NULL_MODE='overlap';appoint.rng_global=np.random.default_rng(int(tic)%2**32)
    module=A/'binary-exploration-2026-11-04/bulk_events.py'
    spec=importlib.util.spec_from_file_location('bulk',module);bulk=importlib.util.module_from_spec(spec);spec.loader.exec_module(bulk)
    result=bulk.one(tic,tg)
    (W/'bulk-results'/f'{tic}.json').write_text(json.dumps(result),encoding='utf8')
    try:result=appoint.star(tic,tg,nnull=40)
    except Exception as e:result={'tic':tic,'error':repr(e)}
    (W/'appointment-results'/f'{tic}.json').write_text(json.dumps(result),encoding='utf8')
    return {'tic':tic,'z':result.get('z'),'error':result.get('error')}
def scan():
    for f in ('bulk-results','appointment-results'):(W/f).mkdir(exist_ok=True)
    pop=json.loads((W/'population.json').read_text())
    save('screen-seal.json',{'population_sha256':sha(W/'population.json'),'appointment_program_sha256':sha(OLD/'search256/sources/appoint.py'),'event_program_sha256':sha(A/'binary-exploration-2026-11-04/bulk_events.py'),'wrapper_sha256':sha(Path(__file__)),'null_windows':40,'null_mode':'overlap','conjunction_rng':'TIC modulo2^32 reset per target, numpy default_rng','sample':'400 science +2 separately labelled historical Gaia EB controls; up to8 sectors chosen before flux inspection','notes':'Same frozen raw-SAP algorithms; screening measurements are not physical classifications. Retain all failures/nonflags.'})
    todo=[(k,v) for k,v in pop['targets'].items() if not (W/'appointment-results'/f'{k}.json').exists()]
    with concurrent.futures.ProcessPoolExecutor(2) as ex:
        for i,r in enumerate(ex.map(scan_one,todo),1):print('Screened',i,len(todo),r,flush=True)
if __name__=='__main__':
    {'freeze':freeze,'identities':identities,'download':download,'scan':scan}[sys.argv[1]]()
