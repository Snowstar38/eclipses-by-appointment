"""Read-only AST replay: retain original fits/selections, suppress all artifact writes."""
import ast,builtins,csv,hashlib,json,os
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent.parent
OUT=Path(__file__).resolve().parent
hashes={}
def ro_open(file,mode='r',*a,**k):
 if any(c in mode for c in 'wax+'):raise RuntimeError('Forbidden source write: '+str(file))
 p=Path(file)
 if p.is_file():hashes[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
 return builtins.open(file,mode,*a,**k)
class Transform(ast.NodeTransformer):
 def visit_If(self,n):
  if ast.unparse(n.test)=='windows':return None
  return self.generic_visit(n)
 def visit_Expr(self,n):
  s=ast.unparse(n)
  if s.startswith('json.dump(summary,'):return ast.parse('capture(summary)').body[0]
  if any(z in s for z in ['.write_text(','.savefig(','.mkdir(','json.dump(','print(']):return None
  return self.generic_visit(n)
 def visit_Call(self,n):
  n=self.generic_visit(n)
  if isinstance(n.func,ast.Name) and n.func.id=='dict':
   depth=next((k.value for k in n.keywords if k.arg=='depth_ppt'),None)
   if depth is not None:
    names={z.id for z in ast.walk(depth) if isinstance(z,ast.Name)}
    par=next((z for z in ['pars','par','v'] if z in names),None)
    if par:
     for key,expr in [('corrected_depth_ppt',f'{par}[2]*1000*min(1,{par}[4]/(2*max({par}[5],1e-5)))'),('fitted_parameters',f'{par}.tolist()')]:
      n.keywords.append(ast.keyword(arg=key,value=ast.parse(expr,mode='eval').body))
  return n
def replay(p):
 data=[];tree=Transform().visit(ast.parse(p.read_text()));ast.fix_missing_locations(tree)
 env=dict(__file__=str(p),open=ro_open,capture=lambda m:data.append(m))
 exec(compile(tree,str(p),'exec'),env)
 return data,env.get('out',{})
def dump(name,v):
 (OUT/name).write_text(json.dumps(v,indent=2,default=lambda z:z.item() if hasattr(z,'item') else str(z)))
def selected(m):
 ev=[e for e in m['events'] if e.get('timing_usable')]
 if m['tic']=='371665307':ev=[e for e in ev if e['cycle']%2==0]
 if m['tic']=='314040568':ev=[e for e in ev if e['cycle']%2==1]
 return ev
primary=[];secondary=[]
for i in range(1,8):
 b=ROOT/f'batch{i:02}';print('START',b.name,flush=True)
 replayed,_=replay(b/'review_measure.py')
 for m in replayed:
  old=json.load(ro_open(b/m['tic']/'measurements.json'));good=selected(m)
  r=dict(batch=b.name,tic=m['tic'],old_depth_ppt=old.get('depth_ppt'),replayed_old_depth_ppt=m.get('depth_ppt'),corrected_depth_ppt=float(np.median([e['corrected_depth_ppt'] for e in good])),selected_events=len(good),events=m['events'])
  r['median_delta_ppt']=r['corrected_depth_ppt']-r['old_depth_ppt'];r['corrected_event_count']=sum(abs(e['depth_ppt']-e['corrected_depth_ppt'])>1e-8 for e in m['events'] if 'depth_ppt'in e)
  r['nondepth_replay_equal']=all(m.get(k)==old.get(k) for k in ['period_days','period_error_days','primary_epoch_btjd','timing_event_count'])
  primary.append(r)
 dump('primary.json',primary)
 for name in ['secondary_timing.py','secondary_measure.py','secondary_check.py']:
  if not (b/name).exists():continue
  _,out=replay(b/name)
  for tic,z in out.items():
   es=z.get('events',[z] if 'depth_ppt'in z else [])
   if not es:continue
   accepted=[e for e in es if e.get('usable',True)]
   secondary.append(dict(batch=b.name,tic=tic,script=name,events=es,old_median_ppt=float(np.median([e['depth_ppt'] for e in accepted])) if accepted else None,corrected_median_ppt=float(np.median([e['corrected_depth_ppt'] for e in accepted])) if accepted else None,selection_preserved=True))
 dump('secondary.json',secondary)
 print('DONE',b.name,flush=True)
dump('input-sha256.json',hashes)
dump('summary.json',dict(targets=len(primary),changed_primary_medians=[{k:r[k] for k in ['batch','tic','old_depth_ppt','corrected_depth_ppt','median_delta_ppt','corrected_event_count']} for r in primary if abs(r['median_delta_ppt'])>1e-7],nondepth_replay_mismatches=[r['tic'] for r in primary if not r['nondepth_replay_equal']],secondary_targets=len(secondary),changed_secondary_medians=[{k:r[k] for k in ['batch','tic','old_median_ppt','corrected_median_ppt']} for r in secondary if r['old_median_ppt'] is not None and abs(r['old_median_ppt']-r['corrected_median_ppt'])>1e-7]))
