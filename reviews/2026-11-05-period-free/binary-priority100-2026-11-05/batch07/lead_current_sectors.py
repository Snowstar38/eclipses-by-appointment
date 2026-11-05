"""Bounded current TESS footprint availability for all ten queue targets."""
import csv,json,requests
from pathlib import Path
B=Path(__file__).resolve().parent; out=[]
for r in csv.DictReader((B/'queue.csv').open(newline='')):
    try:
        res=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/sector',params={'ra':r['ra_deg'],'dec':r['dec_deg'],'radius':0,'units':'deg'},timeout=40)
        res.raise_for_status();js=res.json()
        out.append(dict(sample_id=r['sample_id'],tic=r['tic'],url=res.url,status=res.status_code,response=js))
        print(r['sample_id'],[x.get('sectorName') for x in js.get('results',[])],flush=True)
    except Exception as ex:
        out.append(dict(sample_id=r['sample_id'],tic=r['tic'],error=repr(ex)))
        print(r['sample_id'],repr(ex),flush=True)
(B/'lead-current-sectors.json').write_text(json.dumps(out,indent=2)+'\n')
