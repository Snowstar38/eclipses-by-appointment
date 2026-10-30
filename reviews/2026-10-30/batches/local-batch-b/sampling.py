import csv,os,json,numpy as np
from astropy.io import fits
root=os.path.dirname(__file__); path=root+'/events.csv'; rows=list(csv.DictReader(open(path))); known={60:[2943.2],61:[2981.8],62:[3007],63:[3033.5],65:[3082.8,3089.8],67:[3147],83:[3564.5],85:[3616.5],86:[3649.3],87:[3688.8],89:[3732],94:[3875]}
cache={}
for x in rows:
 key=(x['tic'],int(x['sector']))
 if key not in cache:
  with fits.open(f'{root}/data/{key[0]}_s{key[1]:03}.fits',memmap=False) as hd:
   d=hd[1].data; cache[key]=(np.array(d['TIME'],float),np.array(d['SAP_FLUX'],float),np.array(d['QUALITY']))
 t,f,q=cache[key]; c=float(x['predicted_btjd']); h=float(x['search_box_d'])/2; dt=t-c; good=np.isfinite(t)&np.isfinite(f)&(q==0); cd=float(x['nominal_cadence_d']); expected=2*h/cd
 tin=np.sort(t[good&(abs(dt)<=h)]); gap=np.max(np.diff(tin)) if len(tin)>1 else float('nan')
 left=f[good&(dt>=-3*h)&(dt< -h)]; right=f[good&(dt>h)&(dt<=3*h)]; ml=np.median(left) if len(left) else np.nan; mr=np.median(right) if len(right) else np.nan; baseline=(ml+mr)/2
 ratios=[int(x[n])/expected for n in ('good_in','good_left','good_right')]; robust=x['classification']!='incomplete' and min(ratios)>=0.6 and np.isfinite(gap) and gap<2*cd
 x.update(expected_in=expected,in_coverage_ratio=ratios[0],left_coverage_ratio=ratios[1],right_coverage_ratio=ratios[2],inbox_max_gap_d=gap,robust_sampling=robust,low_coverage=min(ratios)<0.6,inbox_gap_flag=bool(not np.isfinite(gap) or gap>=2*cd),left_minus_right_ppt=1000*(ml-mr)/baseline if baseline else np.nan,known_systematic_near=','.join(str(v) for v in known.get(key[1],[]) if abs(v-c)<=2*h))
with open(path,'w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
sp=root+'/sectors.csv'; secs=list(csv.DictReader(open(sp)))
for s in secs:
 a=[x for x in rows if x['tic']==s['tic'] and x['sector']==s['sector']]; z=[x for x in a if x['classification']!='incomplete']; s['all_sampled_median_depth_ppt']=np.nanmedian([float(x['depth_ppt']) for x in z]) if z else np.nan; s['robust_sampling_windows']=sum(x['robust_sampling'] for x in a)
with open(sp,'w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=secs[0]); w.writeheader(); w.writerows(secs)
for tic in sorted({x['tic'] for x in rows}):
 a=[x for x in rows if x['tic']==tic]; print(tic,'robust',sum(x['robust_sampling'] for x in a),'systematic',[(x['sector'],x['predicted_btjd'],x['known_systematic_near']) for x in a if x['known_systematic_near']])
