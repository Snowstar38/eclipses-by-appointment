import os,json,glob,csv,numpy as np
from astropy.io import fits
root=os.path.dirname(__file__); src=json.load(open(root+'/selected.json')); searches={str(x['tic']):x['P'] for x in src['search']}; events=[]; sectors=[]
def write(name,rows):
 with open(root+'/'+name,'w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
for path in sorted(glob.glob(root+'/data/*.fits')):
 tic=os.path.basename(path).split('_')[0]; sec=int(os.path.basename(path).split('_s')[1][:3]); e=searches[tic]; p=e['P']; t0=e['t0']; dur=e['dur']; h=dur/2
 with fits.open(path,memmap=False) as hd:
  dat=hd[1].data; t=np.asarray(dat['TIME'],float); f=np.asarray(dat['SAP_FLUX'],float); q=np.asarray(dat['QUALITY']); b=np.asarray(dat['SAP_BKG'],float)
 finite=np.isfinite(t)&np.isfinite(f); good=finite&(q==0); tf=t[np.isfinite(t)]; cadence=np.median(np.diff(np.sort(tf))); n0=len(events)
 for k in range(int(np.ceil((np.min(tf)-t0)/p)),int(np.floor((np.max(tf)-t0)/p))+1):
  c=t0+k*p; dt=t-c; ad=np.abs(dt); inside=ad<=h; left=(dt>=-3*h)&(dt< -h); right=(dt>h)&(dt<=3*h); wide=(ad>3*h)&(ad<=5*h)
  ni=int(np.sum(good&inside)); nl=int(np.sum(good&left)); nr=int(np.sum(good&right)); nw=int(np.sum(good&wide)); complete=ni>=2 and nl>=2 and nr>=2
  med=lambda x:float(np.nanmedian(x)) if len(x) else np.nan
  base=med(f[good&(left|right)]); base2=med(f[good&wide]); val=med(f[good&inside]); depth=1000*(base-val)/base if ni and np.isfinite(base) and base else np.nan; depth2=1000*(base2-val)/base2 if ni and np.isfinite(base2) and base2 else np.nan
  bx=med(b[good&inside])-med(b[good&(left|right)]) if ni else np.nan
  tnear=np.sort(t[finite&(ad<=3*h)]); gap=float(np.max(np.diff(tnear))) if len(tnear)>1 else np.nan
  # Lowest sampled raw flux is a discrete proxy, not a fitted midpoint.
  ix=np.flatnonzero(good&inside); proxy=float(t[ix[np.argmin(f[ix])]]) if len(ix) else np.nan
  klass='descriptive_dip' if complete and np.isfinite(depth2) and depth>5 and depth2>5 else ('ambiguous_or_no_dip' if complete else 'incomplete')
  events.append(dict(tic=tic,sector=sec,epoch=k,predicted_btjd=round(c,6),search_box_d=dur,finite_in=int(np.sum(finite&inside)),good_in=ni,flagged_in=int(np.sum(finite&inside&(q!=0))),bit32_in=int(np.sum(finite&inside&((q.astype('int64')&32)!=0))),good_left=nl,good_right=nr,good_wide=nw,depth_ppt=depth,depth_wide_ppt=depth2,lowest_flux_time_proxy_btjd=proxy,bkg_delta_native=bx,local_max_gap_d=gap,nominal_cadence_d=cadence,classification=klass))
 ev=events[n0:]; ds=[x['depth_ppt'] for x in ev if x['classification']=='descriptive_dip']; sectors.append(dict(tic=tic,sector=sec,time_min=float(np.min(tf)),time_max=float(np.max(tf)),raw_rows=len(t),finite_flux_time=int(sum(finite)),quality0=int(sum(good)),flagged_finite=int(sum(finite&(q!=0))),predicted_centers=len(ev),covered=sum(x['classification']!='incomplete' for x in ev),descriptive_dips=len(ds),median_depth_ppt=med(ds)))
write('events.csv',events); write('sectors.csv',sectors)
for tic in sorted(searches):
 a=[x for x in events if x['tic']==tic]; d=[x for x in a if x['classification']=='descriptive_dip']; z=[x for x in a if x['classification']!='incomplete']; print(tic,'sectors',sum(x['tic']==tic for x in sectors),'pred',len(a),'covered',len(z),'dip',len(d),'depth',round(np.nanmedian([x['depth_ppt'] for x in z]),2) if z else None,'wide',round(np.nanmedian([x['depth_wide_ppt'] for x in z]),2) if z else None,flush=True)
