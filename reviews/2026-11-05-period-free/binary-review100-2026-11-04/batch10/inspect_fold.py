"""Hash-verified QLP SAP inspection of frozen batch-10 P and P/2 windows."""
import csv, json, hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

B=Path(__file__).resolve().parent
for row in csv.DictReader((B/'queue.csv').open(newline='')):
 tic=row['tic']; packet=json.loads((B.parent/'source-packets'/tic/'sources.json').read_text())
 out=B/tic;out.mkdir(exist_ok=True)
 for key in ('bulk_result','fold_result'):
  p=Path(packet[key]);assert hashlib.sha256(p.read_bytes()).hexdigest()==packet[key+'_sha256']
 data={'sample_id':row['sample_id'],'tic':tic,'packet_sha256':hashlib.sha256((B.parent/'source-packets'/tic/'sources.json').read_bytes()).hexdigest(),'fold':packet['fold'],'sectors':[],'windows':[]}
 fig,axes=plt.subplots(len(packet['target']['files'])+2,1,figsize=(11,2*(len(packet['target']['files'])+2)),squeeze=False)
 k=0; alltime=[];allflux=[]
 for fobj in packet['target']['files']:
  p=Path(fobj['path']);sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha==fobj['sha256']
  with fits.open(p,memmap=False) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
   alt={name:np.asarray(a[name],float) for name in ('KSPSAP_FLUX','SAP_BKG') if name in a.names}
  m=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[m];f=f[m];alt={name:v[m] for name,v in alt.items()}
  if not len(t):continue
  norm=np.median(f);y=f/norm;dt=float(np.median(np.diff(t)))
  sec={'sector':p.stem.split('_s')[-1],'path':str(p),'sha256':sha,'start':float(t.min()),'end':float(t.max()),'n':len(t),'cadence':dt,'gaps_gt_0p3d':[[float(t[i]),float(t[i+1])] for i in np.where(np.diff(t)>.3)[0]]}
  data['sectors'].append(sec);alltime.extend(t);allflux.extend(y)
  ax=axes[k,0];k+=1;ix=np.arange(0,len(t),max(1,len(t)//2000));ax.plot(t[ix],y[ix],'.',ms=1);ax.set_title(f'{tic} {p.stem} SAP full, {t.min():.1f}-{t.max():.1f}',fontsize=9);ax.set_ylabel('SAP/median')
  for kind in ('P','P2'):
   sol=packet['fold'][kind];P=sol['P'];t0=sol['t0'];dur=sol['dur']
   for cyc in range(int(np.floor((t.min()-t0)/P))-1,int(np.ceil((t.max()-t0)/P))+2):
    c=t0+cyc*P
    if c<t.min()-.9 or c>t.max()+.9:continue
    off=t-c;core=np.abs(off)<dur/2;left=(off>=-max(.7,3*dur))&(off<=-max(.3,1.5*dur));right=(off>=max(.3,1.5*dur))&(off<=max(.7,3*dur));side=left|right
    before=(off>=-dur)&(off<0);after=(off>=0)&(off<=dur)
    local=(np.abs(off)<=max(.7,3*dur));lt=t[local]
    gaps=np.diff(lt); maxgap=float(gaps.max()) if len(gaps) else None
    if side.sum()>=4:
     base=float(np.median(f[side]));depth=float(1000*(1-np.median(f[core])/base)) if core.sum()>=2 else None
     altdepth={name:float(1000*(1-np.median(v[core])/np.median(v[side]))) if core.sum()>=2 and np.median(v[side])>0 else None for name,v in alt.items()}
    else:base=None;depth=None;altdepth={name:None for name in alt}
    rec={'kind':kind,'sector':sec['sector'],'cycle':cyc,'predicted_btjd':float(c),'duration':dur,'n_core':int(core.sum()),'n_left':int(left.sum()),'n_right':int(right.sum()),'n_before':int(before.sum()),'n_after':int(after.sum()),'core_first':float(t[core].min()) if core.sum() else None,'core_last':float(t[core].max()) if core.sum() else None,'max_local_gap_days':maxgap,'depth_ppt':depth,'alt_depth_ppt':altdepth,'baseline_ppt_offset_lr':float(1000*(np.median(f[right])-np.median(f[left]))/base) if base and left.sum()>=2 and right.sum()>=2 else None,'local_p05_p95_ppt':[float(x) for x in np.percentile(1000*(f[local]/base-1),[5,95])] if base and local.sum()>3 else None}
    data['windows'].append(rec)
    if kind=='P':ax.axvspan(c-dur/2,c+dur/2,color='red',alpha=.16)
  ax.set_ylim(*np.percentile(y,[1,99]))
 for j,kind in enumerate(('P','P2')):
  sol=packet['fold'][kind];tt=np.asarray(alltime);yy=np.asarray(allflux);phase=((tt-sol['t0']+sol['P']/2)%sol['P'])/sol['P']-.5
  ax=axes[k+j,0];ax.plot(phase,yy,'.',ms=.8,alpha=.25);bins=np.linspace(-.5,.5,101);ix=np.digitize(phase,bins);xb=[];yb=[]
  for n in range(1,len(bins)):
   z=yy[ix==n]
   if len(z)>=3:xb.append((bins[n-1]+bins[n])/2);yb.append(np.median(z))
  ax.plot(xb,yb,'r-',lw=1);ax.set_title(f'{kind} fold {sol["P"]:.5f} d, z={sol["z"]:.2f}',fontsize=9);ax.set_xlim(-.1,.1);ax.set_ylim(*np.percentile(yy,[1,99]));ax.set_ylabel('SAP/sector median')
 fig.tight_layout();fig.savefig(out/'raw-fold.png',dpi=130);plt.close(fig)
 (out/'raw-fold.json').write_text(json.dumps(data,indent=2)+'\n')
 print(row['sample_id'],tic,'sectors',len(data['sectors']),'windows',len(data['windows']),flush=True)
