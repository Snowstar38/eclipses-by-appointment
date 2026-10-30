"""Single live mirror, bounded initial probe and then fresh missing catalogue gates."""
import archives as a
import urllib.parse,concurrent.futures,json,csv
tables=['II/366/catalog','B/sb9/main','B/wds/wds','J/ApJS/258/16/tess-ebs','J/A+A/691/A242/obaf-eb1','J/ApJS/279/50/table2','J/ApJS/279/50/table3','J/ApJS/279/50/table4']
def query(t,table):
 return 'https://vizier.idia.ac.za/viz-bin/asu-tsv?'+urllib.parse.urlencode({'-source':table,'-c':f"{t['ra']} {t['dec']}",'-c.rs':60,'-out.max':100,'-out.all':'','-out.add':'_r'})
tic,t=next(iter(a.selected['targets'].items()));u=query(t,tables[0])
try:
 s=a.get(u);(a.R/f'{tic}_idia_II_366_catalog.txt').write_text(s,encoding='utf8');print('probe response',len(s),flush=True)
except Exception as e:
 (a.R/'idia-outage.json').write_text(json.dumps({'url':u,'error':str(e)}));print('probe failed',e);raise SystemExit
jobs=[]
for tic,t in a.selected['targets'].items():
 for table in tables:
  name='idia_'+table.replace('/','_');u=query(t,table)
  if not (a.R/f'{tic}_{name}.txt').exists():jobs.append((tic,name,lambda u=u:a.get(u)))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(a.work,jobs))
(a.R/'idia-query-log.json').write_text(json.dumps(rows,indent=2))
