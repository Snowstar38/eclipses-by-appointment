import json,pathlib,urllib.request,urllib.parse,concurrent.futures,hashlib,numpy as np
from astropy.io import fits
from scipy.optimize import least_squares
R=pathlib.Path(__file__).parent; raw=json.load(open(R/'raw-events.json')); out=[]
def task(tic):
 p=R/tic/'mast-products.json'
 if not p.exists():return {'tic':tic,'error':'MAST product inventory timed out'}
 inv=json.load(open(p)); ev=raw[tic]['events'];secs=[e['sector'] for e in ev if 'tc'in e]; opts=[x for x in inv.get('data',[]) if x.get('provenance_name') in ('SPOC','TESS-SPOC','TARS') and str(x.get('dataURL','')).endswith('_lc.fits') and x.get('sequence_number') in secs];opts.sort(key=lambda x:['SPOC','TESS-SPOC','TARS'].index(x['provenance_name']))
 for product in opts:
  uri=product['dataURL'];sec=product['sequence_number'];path=R/tic/('indep_s%03d.fits'%sec)
  try:
   if not path.exists():path.write_bytes(urllib.request.urlopen('https://mast.stsci.edu/api/v0.1/Download/file?'+urllib.parse.urlencode({'uri':uri}),timeout=50).read())
   with fits.open(path) as h:
    hdr=h[0].header; cols=h[1].columns.names; identity={'header_TICID':hdr.get('TICID'),'header_OBJECT':hdr.get('OBJECT'),'header_SECTOR':hdr.get('SECTOR'),'header_RA_OBJ':hdr.get('RA_OBJ'),'header_DEC_OBJ':hdr.get('DEC_OBJ'),'uri_contains_padded_tic':str(tic).zfill(16) in uri,'header_tic_matches':str(hdr.get('TICID','')).strip()==tic,'header_sector_matches':hdr.get('SECTOR')==sec}; a=h[1].data;t=np.array(a['TIME'],float);col='SAP_FLUX' if 'SAP_FLUX' in a.columns.names else 'FLUX';y=np.array(a[col],float);q=np.array(a['QUALITY']) if 'QUALITY'in a.columns.names else np.zeros(len(t)); good=np.isfinite(t)&np.isfinite(y)&(q==0)&(y>0);rows=[]
    for e in ev:
     if e.get('sector')!=sec or 'tc' not in e:continue
     T=e['duration_d'];x=t-e['tc'];w=max(3*T,.32);m=good&(abs(x)<w);x=x[m];z=y[m]
     if len(x)<20 or sum(abs(x)<T/2)<3 or sum(x<-T*.65)<5 or sum(x>T*.65)<5:continue
     z=z/np.median(z);fr=e['ingress_fraction'];shape=np.clip((T/2-abs(x))/(T*fr),0,1);A=np.column_stack((np.ones(len(x)),x/w,(x/w)**2,-shape));c=np.linalg.lstsq(A,z,rcond=None)[0];r=z-A@c;err=np.sqrt(np.linalg.pinv(A.T@A)[-1,-1]*sum(r*r)/max(1,len(r)-4));rows.append(dict(tc=e['tc'],depth=float(c[-1]),formal_error=float(err),n_in=int(sum(abs(x)<T/2)),column=col))
   if rows:return dict(tic=tic,sector=sec,provenance=product['provenance_name'],uri=uri,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),measurements=rows,identity=identity,input_columns=cols,quality_filter='QUALITY == 0' if 'QUALITY' in cols else 'none (column missing)',note='fixed QLP-measured event shape; uninflated formal errors')
  except Exception as e: error=str(e)
 return {'tic':tic,'error':locals().get('error','No suitable independent same-sector event')}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:out=list(ex.map(task,raw))
json.dump(out,open(R/'independent-results.json','w'),indent=2);print(out)
