import json,pathlib,urllib.request,hashlib,datetime
from astropy.io import fits
import numpy as np
import fit_batch as f
root=f.ROOT; inventory=json.load(open(root.parent.parent/'shared-full-review/mast-next60.json'))['data']; out=[]
for tic in f.targets:
 r=json.load(open(root/tic/'fit-results.json')); ev=[e for e in r['events'] if e['status']=='fit' and not e['scan_edge']]; sectors=set(e['sec'] for e in ev)
 products=[x for x in inventory if x['target_name']==tic and x['provenance_name'] in ('SPOC','TESS-SPOC','TARS') and x['dataURL'].endswith('_lc.fits') and x['sequence_number'] in sectors]
 products.sort(key=lambda x: (['SPOC','TESS-SPOC','TARS'].index(x['provenance_name']),-sum(e['sec']==x['sequence_number'] for e in ev)))
 for product in products:
  uri=product['dataURL']; url='https://mast.stsci.edu/api/v0.1/Download/file?uri='+uri; sec=product['sequence_number']; path=root.parent/'data'/f'{tic}_{product["provenance_name"]}_s{sec:03d}_indep.fits'; row=dict(tic=tic,sector=sec,product=product['provenance_name'],uri=uri,url=url,utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
  try:
   if not path.exists():
    with urllib.request.urlopen(url,timeout=75) as h:path.write_bytes(h.read())
   b=path.read_bytes();row['sha256']=hashlib.sha256(b).hexdigest(); row['bytes']=len(b)
   with fits.open(path,memmap=False) as h:
    d=h[1].data; names=d.columns.names; row['columns']=names; row['header_target']=str(h[0].header.get('TICID',h[0].header.get('OBJECT','')));row['header_sector']=h[0].header.get('SECTOR'); t=np.asarray(d['TIME'],float); q=np.asarray(d['QUALITY'],int) if 'QUALITY' in names else np.zeros(len(t),int)
    results=[]
    for col in ['SAP_FLUX','PDCSAP_FLUX','FLUX']:
     if col not in names:continue
     y=np.asarray(d[col],float); good=np.isfinite(t)&np.isfinite(y)&(q==0)&(y>0)
     for e in ev:
      if e['sec']!=sec:continue
      T=e['T14'];x=t-e['tc'];m=good&(abs(x)<max(3*T,.32)); xx=x[m];yy=y[m]; med=np.median(yy) if len(yy) else 0
      if med<=0 or sum(abs(xx)<T/2)<3 or sum(xx<-.65*T)<5 or sum(xx>.65*T)<5:continue
      z=f.linear(xx/max(3*T,.32),yy/med,f.trap(xx,T,r['shape']['fr'],np.median(np.diff(t[np.isfinite(t)])))); results.append(dict(column=col,tc=e['tc'],n_in=int(sum(abs(xx)<T/2)),depth=float(z[1][-1]),error=float(np.sqrt(z[3][-1,-1]))))
    row['measurements']=results
   out.append(row)
   if results:break
  except Exception as e:row['error']=str(e);out.append(row)
json.dump(out,open(root/'independent-manifest-results.json','w'),indent=2);print([(x['tic'],x.get('product'),len(x.get('measurements',[])),x.get('error')) for x in out],flush=True)
