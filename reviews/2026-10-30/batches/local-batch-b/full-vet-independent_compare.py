import pathlib,glob,json,numpy as np
from astropy.io import fits
r=pathlib.Path(__file__).parent
for file in glob.glob(str(r/'data'/'*_TESS-SPOC*.fits')):
 tic=pathlib.Path(file).name.split('_')[0]; m=json.loads((r/f'{tic}_measurements.json').read_text()); a=fits.getdata(file,1); t=np.array(a['TIME'],float);q=np.array(a['QUALITY']); result=[]
 for e in m['independent']:
  z={'cycle':e['cycle'],'sector':e['sector']};c=e['tc'];w=e['T14_d'];f=e['T12_d']/w
  for col in ['SAP_FLUX','PDCSAP_FLUX']:
   v=np.array(a[col],float);ok=np.isfinite(t)&np.isfinite(v)&(q==0)&(abs(t-c)<.7);x=t[ok]-c;y=v[ok];y=y/np.median(y);h=np.clip((w/2-abs(x))/(w*f),0,1);A=np.column_stack([np.ones(len(x)),x,-h]);co=np.linalg.lstsq(A,y,rcond=None)[0];res=y-A@co;z[col]=float(co[2]);z[col+'_error']=float(np.sqrt(np.linalg.pinv(A.T@A)[2,2]*np.var(res)))
  result.append(z)
 (r/f'{tic}_independent_comparison.json').write_text(json.dumps(result,indent=2));print(tic,result)
