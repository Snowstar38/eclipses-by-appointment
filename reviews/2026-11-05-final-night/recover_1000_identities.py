from pathlib import Path
import json,io,csv,shutil,types,hashlib,concurrent.futures
import fresh_band1000 as pipeline
W=pipeline.W
for name in ('identity-outcomes.json','targets.json','feasibility-summary.json'):
    dest=W/('initial-timeout-'+name)
    if not dest.exists():shutil.copy2(W/name,dest)
original_request=pipeline.request_receipt;original_invoke=pipeline.invoke
selected=json.loads((W/'selection.json').read_text())['selected']
def request(name,url,params=None,data=None,timeout=40):
    if name!='gaia-neighbour':return original_request(name,url,params,data,timeout)
    def chunk(start):
        d=dict(data);d['QUERY']='SELECT dr3_source_id,dr2_source_id,angular_distance,magnitude_difference FROM gaiadr3.dr2_neighbourhood WHERE dr3_source_id IN ('+','.join(r['source_id'] for r in selected[start:start+100])+')'
        r=original_request(f'gaia-neighbour-retry-{start:04d}',url,data=d,timeout=40)
        return list(csv.DictReader(io.StringIO(r.text))) if r is not None and r.text.startswith('dr3_source_id,') else []
    with concurrent.futures.ThreadPoolExecutor(2) as ex:parts=list(ex.map(chunk,range(0,len(selected),100)))
    combined=[r for part in parts for r in part];assert combined,'All neighbourhood retries unavailable; preserve initial unresolved outcomes'
    out=io.StringIO();writer=csv.DictWriter(out,fieldnames=list(combined[0]));writer.writeheader();writer.writerows(combined)
    (W/'gaia-neighbour-retry-combined.csv').write_text(out.getvalue(),encoding='utf8')
    print('Recovered neighbourhood rows',len(combined),'successful chunks',sum(bool(p) for p in parts),flush=True)
    return types.SimpleNamespace(text=out.getvalue())
def invoke(name,req):
    if name.startswith('tic-'):
        p=W/(name+'.response');rp=W/(name+'.receipt.json')
        if p.exists() and rp.exists():
            rec=json.loads(rp.read_text());assert hashlib.sha256(p.read_bytes()).hexdigest()==rec['sha256']
            j=json.loads(p.read_text());
            if j.get('status')=='COMPLETE' and j.get('paging',{}).get('pagesFiltered',1)<=1:return j
    return original_invoke(name,req)
pipeline.request_receipt=request;pipeline.invoke=invoke
pipeline.identities()
