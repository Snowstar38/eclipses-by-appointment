import csv,json,glob,hashlib,math
from pathlib import Path
import numpy as np
from scipy.optimize import curve_fit
B=Path(r'[local path omitted]'); rows=list(csv.DictReader(open(B/'queue.csv'))); out={}
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def gauss(x,a,b,d,c,s): return a+b*x-d*np.exp(-.5*((x-c)/s)**2)
for row in rows:
 t=row['tic']; p=B/t; m=json.load(open(p/'measurements.json')); data=list(csv.DictReader(open(p/'raw-windows.csv'))); ev=[]
 for e in m['events']:
  if not e.get('timing_usable'): continue
  if t=='436092743' and e['cycle']%2!=1: continue
  z=[r for r in data if int(r['sector'])==e['sector'] and int(r['cycle'])==e['cycle']]; x=np.array([float(r['btjd'])-e['mid_btjd'] for r in z]); y=np.array([float(r['normalized_raw_sap']) for r in z]); w=e['duration_days']
  try:
   q,_=curve_fit(gauss,x,y,p0=[1,0,e['depth_ppt']/1000,0,w/3],bounds=([.5,-1,0,-w,.03*w],[1.5,1,1,w,2*w]),maxfev=10000)
   ev.append((e.get('orbital_cycle',e['cycle']),e['mid_btjd']+q[3],q[2]*1000))
  except: pass
 n=np.array([v[0] for v in ev]); tt=np.array([v[1] for v in ev]); coeff=np.polyfit(n-n.min(),tt,1); dg=next((p/'historical').glob('diff_s*.json')); d=json.load(open(dg)); target=np.array(d['target_px']); cen=np.array(d['deficit_centroid']); ns=[]
 for a in d['neighbours_60']:
  if a['possible']:
   npos=np.array(a['px']);ns.append({'source_id':a['source_id'],'separation_arcsec':a['sep'],'required_fraction':a['depth_needed'],'centroid_to_neighbor_px':float(np.linalg.norm(cen-npos)),'centroid_to_target_px':float(np.linalg.norm(cen-target))})
 out[t]={'gaussian_refit_events':len(ev),'gaussian_unweighted_period_days':float(coeff[0]),'gaussian_measured_midpoints_btjd':[x[1] for x in ev],'lead_period_days':m['period_days'],'gaia_period_days':json.load(open(B/'gaia-geometry.json'))[t]['period_days'],'centroid_vs_capable_neighbors':ns,'hashes':{str(f.relative_to(B.parent)):sha(f) for f in [p/'measurements.json',p/'raw-windows.csv',dg,*list((p/'historical').glob('diff_s*.png')),*list((p/'historical').glob('gaia.json'))]},'qlp_hashes':{str(f.relative_to(B.parent)):sha(f) for f in (B.parent/'shared-qlp').glob(t+'_s*.fits')}}
 print(t,round(coeff[0],8),round(m['period_days'],8),'cen',[(round(v['centroid_to_target_px'],2),round(v['centroid_to_neighbor_px'],2)) for v in ns])
json.dump(out,open(B/'helper-numerical-audit.json','w'),indent=2)
