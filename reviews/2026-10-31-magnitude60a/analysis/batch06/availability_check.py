import json,requests
from pathlib import Path
from astropy.io import fits
import numpy as np
B=Path('[local path omitted]');out={}
for tic in ['396859601','20176241']:
 req={'service':'Mast.Caom.Filtered','format':'json','pagesize':2000,'page':1,'params':{'columns':'obs_collection,provenance_name,sequence_number,t_min,t_max,t_obs_release,obs_id,dataproduct_type,target_name,dataURL','filters':[{'paramName':'target_name','values':[tic]},{'paramName':'dataproduct_type','values':['timeseries']}]}}
 try:
  rr=requests.post('http[local path omitted]',data={'request':json.dumps(req)},timeout=60);rr.raise_for_status();data=rr.json();out[tic]={'request':req,'response':data}
 except Exception as e:out[tic]={'error':str(e)}
 m=json.load(open(B/tic/'measurements.json'));P=m['historical_period_days'];T=m['historical_epoch_btjd'];dur=m['search_duration_days'];windows=[]
 for fp in (B.parent/'shared-qlp').glob(tic+'_s*.fits'):
  with fits.open(fp) as h:t=np.array(h[1].data['TIME'],float);q=np.array(h[1].data['QUALITY'],int);f=np.array(h[1].data['SAP_FLUX'],float)
  finite=np.isfinite(t)&np.isfinite(f)&(f>0)
  for n in range(int(np.ceil((np.nanmin(t)-T)/P)),int(np.floor((np.nanmax(t)-T)/P))+1):
   dt=t-(T+n*P);core=abs(dt)<dur/3;pre=(dt>-3*dur)&(dt<-dur);post=(dt>dur)&(dt<3*dur)
   windows.append(dict(sector=int(fp.stem.split('_s')[1]),cycle=n,predicted_btjd=T+n*P,all_core=int(sum(core&finite)),clean_core=int(sum(core&finite&(q==0))),clean_pre=int(sum(pre&finite&(q==0))),clean_post=int(sum(post&finite&(q==0)))))
 out[tic]['raw_window_coverage']=windows
json.dump(out,open(B/'single-cycle-availability.json','w'),indent=2)
print([(t,[(r.get('provenance_name'),r.get('sequence_number')) for r in d.get('response',{}).get('data',[])],d['raw_window_coverage']) for t,d in out.items()])
