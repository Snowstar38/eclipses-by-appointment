"""Targeted new-sector TESSCut fetch and measured alias-window coverage for T002/T007."""
import csv,hashlib,io,json,zipfile,concurrent.futures
from pathlib import Path
import requests,numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;Q={r['sample_id']:r for r in csv.DictReader((B/'queue.csv').open())}
todo=[('T002',s) for s in (105,107,108,109)]+[('T007',109)]
def get(item):
 sid,s=item;r=Q[sid];p=B/r['tic']/f'lead-s{s}-tesscut.fits';o=dict(sample_id=sid,tic=r['tic'],sector=s,path=str(p))
 try:
  z=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':r['ra_deg'],'dec':r['dec_deg'],'x':11,'y':11,'units':'px','sector':s},timeout=120);o.update(url=z.url,status=z.status_code,zip_sha256=hashlib.sha256(z.content).hexdigest());z.raise_for_status();f=zipfile.ZipFile(io.BytesIO(z.content));data=f.read(f.namelist()[0]);p.write_bytes(data);o['fits_sha256']=hashlib.sha256(data).hexdigest()
 except Exception as e:o['error']=repr(e)
 return o
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool: receipts=list(pool.map(get,todo))
(B/'lead-newsector-fetch.json').write_text(json.dumps(receipts,indent=2)+'\n')
print([(r['sample_id'],r['sector'],r.get('status'),r.get('error')) for r in receipts],flush=True)
out=[]
for r in receipts:
 if 'error' in r:continue
 row=Q[r['sample_id']];p=Path(r['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==r['fits_sha256']
 with fits.open(p,memmap=False) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['FLUX'],float);qual=np.asarray(a['QUALITY'],int);w=WCS(h[2].header)
 good=np.isfinite(t)&(qual==0);t=t[good];f=f[good]
 tx,ty=map(float,w.all_world2pix(float(row['ra_deg']),float(row['dec_deg']),0));yy,xx=np.indices(f.shape[1:]);mask=(abs(xx-round(tx))<=1)&(abs(yy-round(ty))<=1)
 bg=np.nanmedian(np.sort(f.reshape(len(f),-1),axis=1)[:,:40],axis=1);flux=np.nansum(f[:,mask],axis=1)-bg*np.isfinite(f[:,mask]).sum(axis=1)
 rec=dict(sample_id=r['sample_id'],tic=r['tic'],sector=r['sector'],fits_sha256=r['fits_sha256'],target_pixel=[tx,ty],ap3_baseline=float(np.nanmedian(flux)),n_quality0=int(len(t)),start_btjd=float(t.min()),end_btjd=float(t.max()),cadence_days=float(np.median(np.diff(t))),max_gap_days=float(np.max(np.diff(t))),ap3_p01_p99=[float(v) for v in np.nanpercentile(flux/np.nanmedian(flux),[1,99])])
 if rec['sample_id']=='T002':
  first=1435.0295;last=2149.0344;cycles=(28,29,30);duration=.24
 else:
  first=1499.5882;last=3715.7806;cycles=(54,57,60);duration=1.6
 rec['aliases']=[]
 for n0 in cycles:
  per=(last-first)/n0
  for n in range(int((t.min()-first)/per)-1,int((t.max()-first)/per)+2):
   pred=first+n*per
   if pred<t.min()-.5 or pred>t.max()+.5:continue
   delta=t-pred;core=np.abs(delta)<duration/2;left=(delta>=-2.5*duration)&(delta< -1.5*duration);right=(delta>1.5*duration)&(delta<=2.5*duration)
   ct=t[core];base=np.nanmedian(np.r_[flux[left],flux[right]]) if sum(left)+sum(right)>4 else float('nan')
   a=dict(integer_cycles_between_old_events=n0,period_days=per,new_cycle=n,predicted_btjd=pred,core_n=int(sum(core)),left_n=int(sum(left)),right_n=int(sum(right)),expected_core_n=duration/rec['cadence_days'],core_first=float(ct.min()) if len(ct) else None,core_last=float(ct.max()) if len(ct) else None,core_max_gap=float(np.max(np.diff(ct))) if len(ct)>1 else None,core_deficit_ppt=float((1-np.nanmedian(flux[core])/base)*1000) if len(ct) and np.isfinite(base) and base>0 else None,side_scatter_ppt=float(1.4826*np.nanmedian(abs(np.r_[flux[left],flux[right]]/base-1))*1000) if np.isfinite(base) and base>0 else None)
   if len(ct)>1:a['sensitive']=bool(rec['ap3_baseline']>100 and len(ct)>.75*a['expected_core_n'] and ct.min()<pred-duration/2+2*rec['cadence_days'] and ct.max()>pred+duration/2-2*rec['cadence_days'] and a['core_max_gap']<3*rec['cadence_days'] and sum(left)>5 and sum(right)>5)
   else:a['sensitive']=False
   rec['aliases'].append(a)
 out.append(rec)
 fig,axs=plt.subplots(1,2,figsize=(12,4));axs[0].imshow(np.nanmedian(f,axis=0),origin='lower');axs[0].plot(tx,ty,'r+');axs[1].plot(t,flux,'.',ms=1)
 for a in rec['aliases']:
  if a['integer_cycles_between_old_events'] in (29,57):axs[1].axvline(a['predicted_btjd'],color='r',lw=.7)
 fig.suptitle(f"{r['sample_id']} s{r['sector']} target AP3 {rec['ap3_baseline']:.1f}");fig.tight_layout();fig.savefig(B/r['tic']/f'lead-s{r["sector"]}-coverage.png',dpi=120);plt.close(fig)
 print(r['sample_id'],r['sector'],'baseline',round(rec['ap3_baseline'],1),'windows',[(a['integer_cycles_between_old_events'],round(a['predicted_btjd'],2),a['sensitive'],round(a['core_deficit_ppt'] or 0,1)) for a in rec['aliases']],flush=True)
(B/'lead-newsector-coverage.json').write_text(json.dumps(out,indent=2)+'\n')
