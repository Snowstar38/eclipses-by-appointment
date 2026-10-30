"""Bounded fresh archive and pipeline discovery. Read-only primary queries."""
import csv, io, json, pathlib, urllib.request, urllib.parse, concurrent.futures, time
R=pathlib.Path(__file__).parent
selected=json.loads((R.parent/'selected.json').read_text())
def get(url,data=None):
    req=urllib.request.Request(url,data=data,headers={'User-Agent':'binary-vet/1.0'})
    with urllib.request.urlopen(req,timeout=35) as r:return r.read().decode('utf8','replace')
def tap(base,q):return get(base+'?'+urllib.parse.urlencode(dict(REQUEST='doQuery',LANG='ADQL',FORMAT='csv',QUERY=q)))
jobs=[]
for tic,t in selected['targets'].items():
    ra,de=t['ra'],t['dec']; sid=t['gaia']['source_id']
    cone=f"CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{de},{60/3600}))=1"
    jobs.append((tic,'simbad',lambda q=f"SELECT main_id,otype,ra,dec FROM basic WHERE {cone}":tap('https://simbad.cds.unistra.fr/simbad/sim-tap/sync',q)))
    for table in ['B/vsx/vsx','II/366/catalog','B/sb9/main','B/wds/wds','J/ApJS/258/16/tess-ebs','J/A+A/691/A242/obaf-eb1','J/ApJS/279/50/table2','J/ApJS/279/50/table3','J/ApJS/279/50/table4']:
        u='https://vizier.cds.unistra.fr/viz-bin/asu-tsv?'+urllib.parse.urlencode({'-source':table,'-c':f'{ra} {de}','-c.rs':60,'-out.max':100,'-out.all':'','-out.add':'_r'})
        jobs.append((tic,table.replace('/','_'),lambda u=u:get(u)))
    jobs.append((tic,'exofop',lambda tic=tic:get(f'https://exofop.ipac.caltech.edu/tess/target.php?id={tic}&json')))
    for table in ['vari_eclipsing_binary','vari_summary']:
        q=f'SELECT * FROM gaiadr3.{table} WHERE source_id={sid}'
        jobs.append((tic,'gaia_'+table,lambda q=q:tap('https://gea.esac.esa.int/tap-server/tap/sync',q)))
    req={'service':'Mast.Caom.Filtered','format':'json','params':{'columns':'obsid,target_name,sequence_number,dataURL,provenance_name','filters':[{'paramName':'target_name','values':[tic]}]}}
    jobs.append((tic,'mast_pipelines',lambda req=req:get('https://mast.stsci.edu/api/v0/invoke',urllib.parse.urlencode({'request':json.dumps(req)}).encode())))
def work(j):
    tic,name,fn=j; start=time.time()
    try:
        s=fn(); (R/f'{tic}_{name}.txt').write_text(s,encoding='utf8'); status='response'; length=len(s)
    except Exception as e:status=f'{type(e).__name__}: {e}';length=0
    print(tic,name,status,length,flush=True)
    return dict(tic=tic,query=name,status=status,length=length,seconds=round(time.time()-start,1))
if __name__ == '__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:rows=list(ex.map(work,jobs))
 (R/'archive-query-log.json').write_text(json.dumps(rows,indent=2))
