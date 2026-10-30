import json,pathlib,numpy as np
from astropy.io import fits
from fit_batch import trap,linear
D=pathlib.Path(__file__).parent;manifest=json.load(open(D/'independent-manifest.json'));out={}
def measure(t,f,q,b,tc,T,fr,cad,degree):
 w=max(.32,3*T);mask=np.isfinite(t)&np.isfinite(f)&(q==0)&(abs(t-tc)<w);x=t[mask]-tc;y=f[mask];good=np.isfinite(y)&(y>0);x=x[good];y=y[good]
 if sum(abs(x)<T/2)<2 or sum(x < -T*.65)<5 or sum(x>T*.65)<5:return None
 med=np.median(y);y=y/med;sh=trap(x,T,fr,cad);chi,c,res,cov=linear(x/w,y,sh,degree);beta=1
 for mins in (20,40,60):
  n=max(2,int(mins/1440/cad)); nb=len(res)//n
  if nb>=3:beta=max(beta,float(np.std(res[:nb*n].reshape(nb,n).mean(1),ddof=1)/(max(np.std(res,ddof=1),1e-12)/np.sqrt(n))))
 bdep=None; fake=None
 if b is not None:
  bb=b[mask][good];v=np.isfinite(bb)
  if sum(v)>10 and np.std(bb[v])>0:
   norm=(bb[v]-np.median(bb[v]))/np.std(bb[v]);z=linear(x[v]/w,y[v],sh[v],degree,norm);bdep=float(z[1][degree+1]);fake=float(linear(x[v]/w,norm,sh[v],degree)[1][degree+1])
 return dict(depth=float(c[-1]),error=float(np.sqrt(max(cov[-1,-1],0))*beta),red_noise_beta=beta,n_core=int(sum(abs(x)<T/2)),baseline_degree=degree,background_regressed_depth=bdep,background_template_native_sigma=fake)
for tic,m in manifest.items():
 if m['status']!='ok':out[tic]=m;continue
 sec=m['row']['sequence_number'];r=json.load(open(D/tic/'fit-results.json'));sh=r['shape'];T=sh['T14'];fr=sh['fr'];assert int(m['header']['TICID'])==int(tic) and int(m['header']['SECTOR'])==sec
 with fits.open(m['path']) as h:
  a=h[1].data;cols=a.columns.names;t=np.array(a['TIME'],float);q=np.array(a['QUALITY'],int) if 'QUALITY' in cols else np.zeros(len(t),int);cad=float(np.nanmedian(np.diff(t[np.isfinite(t)])));series={k:np.array(a[k],float) for k in ('SAP_FLUX','PDCSAP_FLUX','FLUX') if k in cols};b=np.array(a['SAP_BKG'],float) if 'SAP_BKG' in cols else None
 qp=D.parent/'data'/f'{tic}_s{sec:03}.fits'
 with fits.open(qp) as h:
  a=h[1].data;qt=np.array(a['TIME'],float);qf=np.array(a['SAP_FLUX'],float);qq=np.array(a['QUALITY'],int);qb=np.array(a['SAP_BKG'],float) if 'SAP_BKG' in a.columns.names else None;qc=float(np.nanmedian(np.diff(qt[np.isfinite(qt)])))
 ev=[]
 for e in r['events']:
  if e['status']!='fit' or e['sec']!=sec:continue
  tc=e['tc'];ev.append(dict(tc=tc,qlp={str(deg):measure(qt,qf,qq,qb,tc,T,fr,qc,deg) for deg in (1,2)},independent={k:{str(deg):measure(t,f,q,b,tc,T,fr,cad,deg) for deg in (1,2)} for k,f in series.items()}))
 out[tic]=dict(sector=sec,provenance=m['row']['provenance_name'],fits_identity_validated=True,quality_column_present='QUALITY' in cols,events=ev,note='Same TESS pixels; independent reduction only. Fixed QLP eclipse template and timing; uncertainties conditional and beta-inflated. TARS has no quality flags; its FLUX background provenance unspecified.')
out['240360239']=dict(status='No exact-target SPOC/TESS-SPOC/TARS LC in inventory; TESScut aperture regression attempted separately.')
json.dump(out,open(D/'independent-summary.json','w'),indent=2,allow_nan=False)
