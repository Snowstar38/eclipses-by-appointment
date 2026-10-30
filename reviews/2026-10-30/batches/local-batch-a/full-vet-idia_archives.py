"""One bounded fresh five-target VizieR-IDIA multi-catalog cone pass.
All raw responses retained; parser reports table sections and tabular rows,
never treats service errors/missing table sections as a negative match.
"""
import json,urllib.request,urllib.parse,hashlib,concurrent.futures,time
from pathlib import Path
ROOT=Path(__file__).parent
tg=json.load(open(ROOT.parent/'targets-selected.json'))
tables=['B/vsx/vsx','II/366','B/sb9/main','B/wds/wds','J/ApJS/279/50/table2','J/ApJS/279/50/table3','J/ApJS/279/50/table4','J/A+A/691/A242/obaf-eb1','J/ApJS/258/16/tess-ebs']
def get(item):
 tic,t=item;params={'-source':','.join(tables),'-c':f"{t['ra']} {t['dec']}",'-c.rs':60,'-out.max':100,'-out.all':'','-out.add':'_r','-sort':'_r'}
 url='https://vizier.idia.ac.za/viz-bin/asu-tsv?'+urllib.parse.urlencode(params);receipt=dict(tic=tic,url=url,tables=tables)
 try:
  with urllib.request.urlopen(url,timeout=45) as h:b=h.read(2000000)
  (ROOT/(tic+'_idia.tsv')).write_bytes(b);text=b.decode('latin1');receipt.update(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),http='200',table_sections=[x for x in text.splitlines() if x.startswith('#Table')],service_errors=[x for x in text.splitlines() if 'Error' in x or 'not found' in x.lower()])
 except Exception as ex:receipt['error']=repr(ex)
 print(tic,receipt,flush=True);return receipt
with concurrent.futures.ThreadPoolExecutor(5) as ex:rows=list(ex.map(get,tg.items()))
json.dump(rows,open(ROOT/'idia-receipts.json','w'),indent=2)
