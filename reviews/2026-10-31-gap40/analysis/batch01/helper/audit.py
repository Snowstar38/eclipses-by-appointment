import json,csv,hashlib,glob,os,numpy as np
from pathlib import Path
b=Path('[local path omitted]'); s=Path('[local path omitted] 5/made/sb1-scale/diffimg'); out=[]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
for row in csv.DictReader(open(b/'queue.csv')):
 t=row['tic']; m=json.load(open(b/t/'measurements.json')); f=next((s/t).glob('diff_s*.json')); d=json.load(open(f)); g=[e for e in m['events'] if 'mid_btjd' in e and (t not in ['397586559','258621299'] or e['cycle']%2==0)]
 x=np.array([e.get('orbital_cycle',e['cycle']) for e in g]); y=np.array([e['mid_btjd'] for e in g]); w=1/np.array([e['timing_error_days'] for e in g])**2
 p=np.sum(w*(x-np.average(x,weights=w))*(y-np.average(y,weights=w)))/np.sum(w*(x-np.average(x,weights=w))**2) if len(x)>1 else None
 poss=[{'id':n['source_id'],'sep':round(n['sep'],2),'G':n['G'],'needed':round(n['depth_needed'],3),'px':n['px']} for n in d['neighbours_60'] if n['possible']]
 parity={str(k):[round(float(np.median([e['depth_ppt'] for e in m['events'] if 'mid_btjd' in e and e['cycle']%2==k])),2),sum(1 for e in m['events'] if 'mid_btjd' in e and e['cycle']%2==k)] for k in [0,1] if any('mid_btjd' in e and e['cycle']%2==k for e in m['events'])}
 out.append(dict(tic=t,measurement_sha256=sha(b/t/'measurements.json'),window_sha256=sha(b/t/'raw-windows.csv'),diff_path=str(f),diff_sha256=sha(f),cutout_sha256=sha(next(Path('[local path omitted]'+t).glob('*.fits'))),n_measured=len(g),period=m.get('period_days'),period_recomputed=p,parity=parity,target_px=d['target_px'],deficit_centroid=d['deficit_centroid'],psf_fit_frac_resid=d['psf_fit_frac_resid'],depths=[d.get('depth_ap1'),d.get('depth_ap3'),d.get('depth_ap5')],possible=poss))
json.dump(out,open(b/'helper/audit-inventory.json','w'),indent=2)
for r in out:print(r['tic'], 'N',r['n_measured'],'P',r['period'],'diff',None if r['period'] is None else r['period_recomputed']-r['period'],'parity',r['parity'],'target',np.round(r['target_px'],2),'cent',np.round(r['deficit_centroid'],2),'res',round(r['psf_fit_frac_resid'],2),'possible',len(r['possible']))
