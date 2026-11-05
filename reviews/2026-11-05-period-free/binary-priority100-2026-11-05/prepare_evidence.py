"""Shared immutable source index and raw visual previews; no classifications."""
from pathlib import Path
import csv,json,hashlib
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
W=Path(__file__).resolve().parent
H=W.parent/'binary-exploration-2026-11-04'
O=W/'source-packets';O.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
Q=list(csv.DictReader((W/'queue.csv').open(encoding='utf8')))
pop=json.loads((H/'bulk-population.json').read_text(encoding='utf8'))['targets']
index={};verified=0
for r in Q:
 tic=r['tic'];out=O/tic;out.mkdir(exist_ok=True)
 bp=H/'bulk-results'/f'{tic}.json';bulk=json.loads(bp.read_text(encoding='utf8'))
 foldp=next((H/p/'per-target'/f'{tic}.json' for p in ['pool1024','pool900'] if (H/p/'per-target'/f'{tic}.json').exists()),None)
 fold=json.loads(foldp.read_text(encoding='utf8')) if foldp else None
 expected={x['path']:x['sha256'] for x in pop[tic]['files']}
 data={};receipts=[]
 for rec in bulk['files']:
  p=Path(rec['path']);h=sha(p);assert h==rec['sha256']==expected[str(p)]
  with fits.open(p,memmap=False) as hd:
   assert str(int(hd[0].header['TICID']))==tic
   d=hd[1].data;t=np.array(d['TIME'],float);f=np.array(d['SAP_FLUX'],float);q=np.array(d['QUALITY'],int)
  ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
  if len(f): f=f/np.median(f)
  data[rec['sector']]=(t,f)
  receipts.append({'path':str(p),'sha256':h,'sector':rec['sector'],'quality0_samples':len(t)})
  verified+=1
 packet={'queue_row':r,'target':pop[tic],'bulk_result':str(bp),'bulk_result_sha256':sha(bp),'fold_result':str(foldp) if foldp else None,'fold_result_sha256':sha(foldp) if foldp else None,'fold':fold,'verified_files':receipts,'preview_caveat':'Representative raw SAP quality0 plots only; not fitted events, physical decisions or full coverage audits.'}
 (out/'sources.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf8')
 index[tic]={'packet':str(out/'sources.json'),'sha256':sha(out/'sources.json'),'sample_id':r['sample_id'],'batch':r['batch']}
 # Batch01 lead is preparing its own full panels; avoid duplicating them.
 if r['batch']!='batch01':
  kind='brightening' if r['sample_stratum']=='brightening_lead' else 'dip'
  windows=[dict(x,sector=rec['sector']) for rec in bulk['files'] for x in rec.get('windows',[]) if x['kind']==kind]
  windows.sort(key=lambda x:(x['flag'],abs(x['contrast'])),reverse=True)
  picks=[];sectors=set()
  for x in windows:
   if x['sector'] not in sectors:
    picks.append(x);sectors.add(x['sector'])
   if len(picks)==4:break
  if picks:
   fig,axs=plt.subplots(len(picks),2,figsize=(12,2.7*len(picks)),squeeze=False)
   for (a,b),ev in zip(axs,picks):
    t,f=data[ev['sector']];a.plot(t,f,'.',ms=1.2);a.axvline(ev['time'],color='r',lw=.6)
    a.set_title(f"S{ev['sector']} raw SAP / sector median; quality=0",fontsize=9)
    m=abs(t-ev['time'])<max(3*ev['duration'],.5);b.plot(t[m]-ev['time'],f[m],'.',ms=2)
    b.axvspan(-ev['duration']/2,ev['duration']/2,alpha=.12,color='r')
    b.set_title(f"Screen window {ev['time']:.5f}, d={ev['duration']:.2f}; NOT fitted",fontsize=9)
   fig.suptitle(f"{r['sample_id']} TIC {tic}: {r['sample_stratum']} | representative {kind} windows")
   fig.tight_layout();fig.savefig(out/'raw-preview.png',dpi=110);plt.close(fig)
 print(r['sample_id'],tic,len(receipts),flush=True)
(W/'source-packet-index.json').write_text(json.dumps({'queue_sha256':sha(W/'queue.csv'),'bulk_population_sha256':sha(H/'bulk-population.json'),'verified_fits':verified,'targets':index},indent=2)+'\n',encoding='utf8')
print('DONE',len(index),verified,flush=True)
