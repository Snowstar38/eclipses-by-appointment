"""Hash-verified raw SAP survey of the ten frozen brightening leads."""
import csv, hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
S=B.parent/'source-packets'
for row in csv.DictReader((B/'queue.csv').open(newline='')):
 tic=row['tic']; packet=json.loads((S/tic/'sources.json').read_text()); bulk=Path(packet['bulk_result'])
 assert hashlib.sha256(bulk.read_bytes()).hexdigest()==packet['bulk_result_sha256']
 obj=json.loads(bulk.read_text()); out=B/tic; out.mkdir(exist_ok=True)
 dat={'sample_id':row['sample_id'],'tic':tic,'gaia_period_days':float(row['gaia_period_days']),'sectors':[],'windows':[],'bulk_sha256':packet['bulk_result_sha256']}
 nplot=len(obj['files'])+sum(sum(w['flag'] for w in x.get('windows',[])) for x in obj['files'])
 fig,ax=plt.subplots(nplot,1,figsize=(10,max(2,1.7*nplot)),squeeze=False)
 k=0
 for item in obj['files']:
  if item['status']!='ok':dat['sectors'].append({'sector':item['sector'],'status':item['status']});continue
  path=Path(item['path']);hsh=hashlib.sha256(path.read_bytes()).hexdigest();assert hsh==item['sha256']
  with fits.open(path,memmap=False) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
   names=a.names; alt={name:np.asarray(a[name],float) for name in ('KSPSAP_FLUX','SAP_BKG','SAP_X','SAP_Y') if name in names}
  good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);tt=t[good];ff=f[good]
  cadence=float(np.median(np.diff(tt))); gaps=np.diff(tt);norm=float(np.median(ff));yr=ff/norm
  sec={'sector':item['sector'],'path':str(path),'sha256':hsh,'start_btjd':float(tt.min()),'end_btjd':float(tt.max()),'quality0_n':int(good.sum()),'cadence_days':cadence,'gaps_over_0p5d':[[float(tt[i]),float(tt[i+1])] for i in np.where(gaps>.5)[0]],'sap_median':norm,'sap_p05_p95':[float(x) for x in np.percentile(yr,[5,95])]}
  dat['sectors'].append(sec)
  a0=ax[k,0];k+=1;a0.plot(tt[::max(1,len(tt)//1500)],yr[::max(1,len(tt)//1500)],'.',ms=1.5)
  a0.set_title(f"{tic} s{item['sector']} full SAP, {tt.min():.1f}-{tt.max():.1f}",fontsize=9);a0.set_ylabel('SAP/median')
  for w in item['windows']:
   if not w['flag']:continue
   c=float(w['time']);d=float(w['duration']);half=max(2*d,1.0);sel=good&(abs(t-c)<half)
   side=sel&(abs(t-c)>max(.65*d,.18));core=sel&(abs(t-c)<.25*d)
   left=side&(t<c);right=side&(t>c);pre=sel&(t<c-.5*d);post=sel&(t>c+.5*d)
   base=float(np.median(f[side])) if side.sum() else norm
   fw=f[sel]/base;tw=t[sel];dw={
    'sector':item['sector'],'kind':w['kind'],'screen_btjd':c,'duration_days':d,'screen_contrast':w['contrast'],'screen_depth_fraction':w['depth'],'screen_supported':w['supported'],
    'n_window':int(sel.sum()),'n_core':int(core.sum()),'n_left':int(left.sum()),'n_right':int(right.sum()),'local_baseline_sap':base,
    'core_delta_ppt':float(1000*(np.median(f[core])/base-1)) if core.sum() else None,
    'pre_delta_ppt':float(1000*(np.median(f[pre])/base-1)) if pre.sum() else None,
    'post_delta_ppt':float(1000*(np.median(f[post])/base-1)) if post.sum() else None,
    'pre_post_step_ppt':float(1000*(np.median(f[post])-np.median(f[pre]))/base) if pre.sum() and post.sum() else None,
    'max_internal_gap_days':float(np.max(np.diff(tw))) if len(tw)>1 else None,
    'alt_columns':{name:{'core':float(np.median(v[core])) if core.sum() else None,'side':float(np.median(v[side])) if side.sum() else None} for name,v in alt.items()}}
   dat['windows'].append(dw)
   a1=ax[k,0];k+=1;a1.plot(tw-c,fw,'.',ms=2.5);a1.axvline(0,c='r',lw=.7);a1.axhline(1,c='k',lw=.5)
   a1.set_title(f"s{item['sector']} {w['kind']} BTJD {c:.3f}, core {dw['core_delta_ppt']:.1f} ppt, step {dw['pre_post_step_ppt']:.1f} ppt",fontsize=9)
   a1.set_ylabel('local SAP');a1.set_xlabel('days from screen center')
 fig.tight_layout();fig.savefig(out/'raw-context.png',dpi=120);plt.close(fig)
 (out/'raw-inspection.json').write_text(json.dumps(dat,indent=2)+'\n')
 print(row['sample_id'],tic, len(dat['sectors']),len(dat['windows']),flush=True)
