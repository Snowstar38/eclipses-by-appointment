"""Direct AAVSO VSX cone checks, paced and bounded by healthy positive controls."""
from pathlib import Path
import csv,json,urllib.request,urllib.parse,hashlib,time,datetime
W=Path(__file__).resolve().parent;C=W.parent
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'
def rows(p):return list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))
def query(key,ra,dec):
    url='https://www.aavso.org/vsx/index.php?'+urllib.parse.urlencode({'view':'api.list','ra':ra,'dec':dec,'radius':120/3600,'format':'json'})
    rec={'key':key,'ra_deg':ra,'dec_deg':dec,'radius_arcsec':120,'url':url,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':UA}),timeout=20).read()
        d=json.loads(data);assert 'VSXObjects' in d
        f='vsx-'+key+'.json';(W/f).write_bytes(data)
        obj=d.get('VSXObjects') or {};obj=obj.get('VSXObject',[]) if isinstance(obj,dict) else []
        if isinstance(obj,dict):obj=[obj]
        rec.update(status='success',file=f,sha256=hashlib.sha256(data).hexdigest(),objects=obj)
    except Exception as e:rec.update(status='UNKNOWN',error=repr(e))
    return rec
def main():
    targets=[{'key':r['sample_id'],'tic':r['tic'],'gaia_dr3':r['gaia_dr3'],'ra':r['ra_deg'],'dec':r['dec_deg'],'scope':'next100'} for r in rows(C/'queue.csv')]
    old=Path('[local-path-redacted]')
    coords={r['tic']:r for r in rows(old/'coordinates.csv')}
    for r in rows(old/'root-decisions.csv'):
        if r['claim_decision']=='PENDING_CATALOGUE':
            c=coords[r['tic']];targets.append({'key':'prior-'+r['tic'],'tic':r['tic'],'gaia_dr3':c.get('gaia_dr3',''),'ra':c['ra_deg'],'dec':c['dec_deg'],'scope':'prior41'})
    for r in rows(C/'off-target-followup.csv'):
        targets.append({'key':'neighbor-'+r['gaia_dr3'],'tic':'','gaia_dr3':r['gaia_dr3'],'ra':r['ra_deg'],'dec':r['dec_deg'],'scope':'off-target-followup'})
    (W/'vsx-queue.json').write_text(json.dumps(targets,indent=2)+'\n')
    control=query('algol-pre',47.04221855,40.95564667)
    assert control['status']=='success' and any(x.get('Name')=='bet Per' for x in control['objects'])
    out=[control];failures=0
    for r in targets:
        time.sleep(3.5);rec=query(r['key'],r['ra'],r['dec']);rec.update({k:r[k] for k in ['tic','gaia_dr3','scope']});out.append(rec)
        (W/'vsx-results.json').write_text(json.dumps(out,indent=2)+'\n')
        failures=failures+1 if rec['status']!='success' else 0
        print(r['key'],rec['status'],len(rec.get('objects',[])),flush=True)
        if failures>=3:break
    time.sleep(3.5);out.append(query('algol-post',47.04221855,40.95564667))
    (W/'vsx-results.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
