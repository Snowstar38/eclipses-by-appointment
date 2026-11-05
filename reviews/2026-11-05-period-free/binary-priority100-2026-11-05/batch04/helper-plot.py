import json, csv, hashlib, pathlib, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
B=pathlib.Path(r'[local-path-redacted]'); S=pathlib.Path(r'[local-path-redacted]')
records=[]
for row in csv.DictReader(open(B/'queue.csv')):
 j=json.load(open(S/(row['tic']+'.json'))); wins=[]
 for f in j['files']:
  for w in f.get('windows',[]):
   if w.get('flag'): wins.append((f,w))
 wins.sort(key=lambda z:-abs(z[1]['contrast'])); wins=wins[:8]
 if not wins: continue
 fig,axs=plt.subplots(len(wins),1,figsize=(11,2.2*len(wins)),squeeze=False)
 for ax,(f,w) in zip(axs[:,0],wins):
  p=pathlib.Path(f['path']); actual=hashlib.sha256(p.read_bytes()).hexdigest()
  with fits.open(p,memmap=False) as h:
   d=h[1].data; t=np.array(d['TIME']); y=np.array(d['SAP_FLUX'],float); q=np.array(d['QUALITY']); x=w['time']; span=max(2.,3*w['duration']); m=np.isfinite(t)&np.isfinite(y)&(abs(t-x)<span); base=np.nanmedian(y[m&(q==0)]); good=m&(q==0); bad=m&(q!=0)
   ax.plot(t[good],y[good]/base,'.',ms=2); ax.plot(t[bad],y[bad]/base,'.',ms=2,color='red',alpha=.5); ax.axvline(x,color='k',lw=.6); ax.axvspan(x-w['duration']/2,x+w['duration']/2,color='grey',alpha=.15); ax.set_title(f"s{f['sector']} {w['kind']} t={x:.4f} d={w['duration']} hash={'OK' if actual==f['sha256'] else 'MISMATCH'}",fontsize=9); ax.grid(alpha=.2)
  records.append(dict(sample=row['sample_id'],tic=row['tic'],sector=f['sector'],time=x,duration=w['duration'],kind=w['kind'],file=str(p),sha256=actual,expected=f['sha256'],match=actual==f['sha256']))
 fig.suptitle(row['sample_id']+' TIC '+row['tic']+' SAP raw, quality=0 blue, flagged red'); fig.tight_layout(); fig.savefig(B/('helper-'+row['sample_id']+'.png'),dpi=100); plt.close(fig)
json.dump(records,open(B/'helper-source-hashes.json','w'),indent=2)
