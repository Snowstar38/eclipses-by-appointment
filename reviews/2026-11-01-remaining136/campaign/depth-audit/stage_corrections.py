"""Build reviewable corrected overlays and exact original snapshots ONLY under depth-audit.
Never writes accepted batch directories. Application/re-freezing is a separate root action.
"""
import csv,hashlib,io,json,re
from pathlib import Path
import numpy as np
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
O=Path(__file__).parent;R=O.parent
P=json.load(open(O/'primary.json'));N={(n['batch'],n['tic']):n for n in json.load(open(O/'neighbors.json'))}
manifest=[]
def put(rel,data):
 source=R/rel;before=source.read_bytes();dest=O/'corrected'/rel;snapshot=O/'original'/rel
 dest.parent.mkdir(parents=True,exist_ok=True);snapshot.parent.mkdir(parents=True,exist_ok=True)
 if snapshot.exists():assert snapshot.read_bytes()==before,'Original source changed since staging'
 else:snapshot.write_bytes(before)
 after=data if isinstance(data,bytes) else data.encode('utf8');dest.write_bytes(after)
 manifest.append(dict(path=rel.as_posix(),original_sha256=hashlib.sha256(before).hexdigest(),corrected_sha256=hashlib.sha256(after).hexdigest(),changed=before!=after))
def jput(rel,z):put(rel,json.dumps(z,indent=2)+'\n')
def proxy(z,ratio,Glimit):
 if isinstance(z,list):return [proxy(a,ratio,Glimit)for a in z]
 if isinstance(z,dict):
  z={k:proxy(v,ratio,Glimit)for k,v in z.items()}
  if 'depth_needed'in z:z['depth_needed']*=ratio;z['possible']=z['depth_needed']<=1
  if 'G_limit_for_depth'in z:z['G_limit_for_depth']=Glimit
 return z
batch_audits={};results={}
for r in P:
 changed=[e for e in r['events'] if 'depth_ppt'in e and abs(e['depth_ppt']-e['corrected_depth_ppt'])>1e-8]
 if not changed:continue
 rel=Path(r['batch'])/r['tic'];m=json.load(open(R/rel/'measurements.json'))
 for e,replayed in zip(m['events'],r['events']):
  if 'depth_ppt'in e:
   e['trapezoid_depth_parameter_ppt']=e['depth_ppt'];e['depth_ppt']=replayed['corrected_depth_ppt'];e['fitted_ingress_days']=replayed['fitted_parameters'][5]
 m['depth_ppt']=r['corrected_depth_ppt'];m['depth_correction_note']='Realized trapezoid decrement d*min(1,w/(2*k)); exact original fit, event selection, timing and width retained. See root depth-audit.'
 jput(rel/'measurements.json',m)
 text=(R/rel/'REPORT.md').read_text()
 for precision in [2,3]:
  if abs(r['median_delta_ppt'])>1e-8:text=text.replace(f"{r['old_depth_ppt']:.{precision}f}ppt",f"{r['corrected_depth_ppt']:.{precision}f}ppt")
 lines=text.splitlines()
 for i,line in enumerate(lines):
  if not line.startswith('|'):continue
  cells=line.split('|')
  for e in changed:
   if len(cells)>3 and cells[1].strip()==str(e['sector']) and cells[2].strip()==str(e['cycle']):
    for ci,c in enumerate(cells):
     if ci<3:continue
     for precision in [2,3]:
      if c.strip()==f"{e['depth_ppt']:.{precision}f}":cells[ci]=c.replace(c.strip(),f"{e['corrected_depth_ppt']:.{precision}f}")
    lines[i]='|'.join(cells)
 text='\n'.join(lines)+'\n'
 if abs(r['median_delta_ppt'])>1e-8:
  n=N[(r['batch'],r['tic'])];ratio=r['corrected_depth_ppt']/r['old_depth_ppt']
  for nb in n['neighbours']:
   # Only required intrinsic loss proxy table cells; other physical values unchanged.
   for precision in [4]:text=text.replace('| '+f"{nb['old_depth_needed']:.{precision}f}"+' |','| '+f"{nb['corrected_depth_needed']:.{precision}f}"+' |').replace('|'+f"{nb['old_depth_needed']:.{precision}f}"+'|','|'+f"{nb['corrected_depth_needed']:.{precision}f}"+'|')
  for sub in ['fresh-pixels/diff_fresh.json','neighbor-assessment.json']:
   if (R/rel/sub).exists():jput(rel/sub,proxy(json.load(open(R/rel/sub)),ratio,n['corrected_G_limit']))
  cap=Path(r['batch'])/'capable-neighbor-audit.json'
  if (R/cap).exists():
   if cap not in batch_audits:batch_audits[cap]=json.load(open(R/cap))
   batch_audits[cap][r['tic']]=proxy(batch_audits[cap][r['tic']],ratio,n['corrected_G_limit'])
  rp=Path(r['batch'])/'RESULTS.csv'
  if rp not in results:results[rp]=list(csv.DictReader(open(R/rp)))
  for row in results[rp]:
   if row['tic']==r['tic']:row['depth_ppt']=str(r['corrected_depth_ppt'])
 text+='\nDepth correction audit (2026-11-02): realized trapezoid decrement replaces its unconstrained amplitude parameter. Original input windows, fitted centers/widths, timing selections and physical verdict are retained; capable-neighbor membership is unchanged. See ../../depth-audit/README.md.\n'
 put(rel/'REPORT.md',text)
 windows=[e for e in r['events'] if 'mid_btjd'in e];picks=np.linspace(0,len(windows)-1,min(len(windows),6)).astype(int)
 if any(windows[i] in changed for i in picks):
  raw=np.genfromtxt(R/rel/'raw-windows.csv',delimiter=',',names=True)
  fig,axs=plt.subplots(len(picks),1,figsize=(9,len(picks)*2.3),squeeze=False)
  for ax,i in zip(axs[:,0],picks):
   e=windows[i];a=raw[(raw['sector']==e['sector'])&(raw['cycle']==e['cycle'])];x=a['btjd']-e['predicted_btjd'];ax.plot(x,a['normalized_raw_sap'],'.',ms=3);ax.plot(x,a['trapezoid_fit'],'r-');ax.set_title(f"TIC {r['tic']} s{e['sector']} cycle {e['cycle']} depth {e['corrected_depth_ppt']:.2f} ppt mid {e['mid_btjd']:.5f}");ax.set_xlabel('Days from historical predicted center');ax.set_ylabel('Raw SAP / local baseline')
  fig.tight_layout();buf=io.BytesIO();fig.savefig(buf,format='png',dpi=130);plt.close(fig);put(rel/'raw-events.png',buf.getvalue())
for rel,z in batch_audits.items():jput(rel,z)
for rel,rows in results.items():
 s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows);put(rel,s.getvalue())
(O/'correction-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Staged',len(manifest),'files; accepted originals untouched.')
