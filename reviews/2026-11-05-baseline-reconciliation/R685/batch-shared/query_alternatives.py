import csv,json,urllib.parse,urllib.request
from pathlib import Path
here=Path(__file__).resolve().parent
ids=[r['tic'] for r in csv.DictReader((here/'queue.csv').open())]
req={'service':'Mast.Caom.Filtered','format':'json','pagesize':5000,'page':1,
     'params':{'columns':'target_name,sequence_number,dataURL,provenance_name',
               'filters':[{'paramName':'provenance_name','values':['SPOC','TESS-SPOC','TARS','TGLC']},
                          {'paramName':'target_name','values':ids}]}}
body=urllib.parse.urlencode({'request':json.dumps(req)}).encode()
with urllib.request.urlopen(urllib.request.Request('https://mast.stsci.edu/api/v0/invoke',data=body),timeout=90) as h:raw=h.read()
(here/'alternative-caom-response.json').write_bytes(raw)
x=json.loads(raw);print(x.get('status'),len(x.get('data',[])))
for tic in ids:
    rows=[r for r in x['data'] if r['target_name']==tic and r.get('dataURL','').endswith('lc.fits')]
    print(tic,[(r['provenance_name'],r['sequence_number']) for r in rows])
