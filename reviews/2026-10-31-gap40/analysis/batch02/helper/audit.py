import json,glob,numpy as np,hashlib,os
base='[local path omitted]'
for f in sorted(glob.glob(base+'/*/measurements.json')):
 d=json.load(open(f)); e=d['events']; x=np.array([v['cycle'] for v in e]); y=np.array([v['mid_btjd'] for v in e]); sig=np.array([v['timing_error_days'] for v in e]); p,c=np.polyfit(x,y,1,w=1/sig); print(d['tic'],len(e),'fit',format(p,'.10f'),'saved',d['period_days'],'max residual',round(max(abs(y-(p*x+c))),6),'sha256',hashlib.sha256(open(f,'rb').read()).hexdigest())
 if d['tic'] in ('416646907','345406164'):
  for s in sorted(set(v['sector'] for v in e)):
   a=[v for v in e if v['sector']==s]; print(' sector',s, 'depths (cycle, ppt)',[(v['cycle'],round(v['depth_ppt'],2)) for v in a])
for tic,sector in [('401138717','38'),('152400959','07')]:
 f=f'[local path omitted] 5/made/sb1-scale/diffimg/{tic}/diff_s{sector}.json';d=json.load(open(f));print(tic,'diff sha256',hashlib.sha256(open(f,'rb').read()).hexdigest(),'target',d['target_px'],'centroid offset',d['deficit_minus_target_px'],'peak',d['peak_deficit_px'],'events',d['n_events'],'possible',d['n_possible'])
