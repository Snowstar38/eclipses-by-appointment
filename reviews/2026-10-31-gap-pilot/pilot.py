"""Reproducible bounded exploratory pilots. Writes only beside this script."""
import os,json,csv,pathlib,sys,hashlib,concurrent.futures,urllib.request,urllib.parse
import numpy as np
from astropy.io import fits
ROOT=pathlib.Path('[local path omitted]'); OUT=pathlib.Path(__file__).parent
SD=ROOT/'Fable 5/made/sb1-scale'; DATA=pathlib.Path(os.environ['TEMP'])/'hunt-sb1-scale'
AD=ROOT/'sky/data/qlp-sb-p20-60'
sys.path.insert(0,str(ROOT/'Fable 5.1/made/appointments'))
import appoint
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def availability(k):
 req={'service':'Mast.Caom.Filtered','format':'json','pagesize':2000,'page':1,'params':{'columns':'obs_collection,provenance_name,sequence_number,t_min,t_max,t_obs_release,obs_id,dataproduct_type,target_name','filters':[{'paramName':'target_name','values':[k]},{'paramName':'dataproduct_type','values':['timeseries']}]}}
 try:
  body=urllib.parse.urlencode({'request':json.dumps(req)}).encode()
  r=json.load(urllib.request.urlopen(urllib.request.Request('http[local path omitted]',data=body),timeout=55))
  (OUT/f'availability-{k}.json').write_text(json.dumps(r,indent=1))
  return {'tic':k,'rows':len(r.get('data',[])),'sectors':sorted(set(int(x['sequence_number']) for x in r.get('data',[]) if x.get('sequence_number') is not None)),'status':r.get('status')}
 except Exception as e:return {'tic':k,'error':repr(e)}
def band():
 tg=json.load(open(SD/'targets.json')); hist={r['tic']:r for r in map(json.loads,open(SD/'search.jsonl'))}
 queue={r['tic'] for r in csv.DictReader(open(OUT.parent/'queue.csv'))}
 cached={f.name.split('_s')[0] for f in DATA.glob('*.fits')}
 eligible=sorted((float(v['gaia']['phot_g_mean_mag']),k) for k,v in tg.items() if k not in queue and k in cached and 12<=float(v['gaia']['period'])<=14.8)
 # Fixed brightness-order prefix, independent of positive outcomes. Extend with a new prefix later if useful.
 limit=int(sys.argv[2]) if len(sys.argv)>2 else 24
 selected=[k for g,k in eligible[:limit]]
 (OUT/f'band-selection-{limit}.json').write_text(json.dumps({'rule':f'first{limit} cached Gaia12-14.8d by G, excluding fixed40; not an unsearched population','eligible_count':len(eligible),'tics':selected,'source_hashes':{str(p):sha(p) for p in [SD/'targets.json',SD/'search.jsonl',OUT.parent/'queue.csv']}},indent=1))
 rows=[]
 for k in selected:
  h=hist.get(k,{}); v=tg[k]; ep=h.get('P',{}); P=ep.get('P',float(v['gaia']['period'])); t0=ep.get('t0'); dur=ep.get('dur',.15)
  row={'tic':k,'G':v['gaia']['phot_g_mean_mag'],'P_gaia':v['gaia']['period'],'control_gaia_veb':v['gaia'].get('veb'),'historical_search':h,'events':[],'files':[]}
  for p in sorted(DATA.glob(f'{k}_s*.fits')):
   row['files'].append({'path':str(p),'sha256':sha(p)})
   with fits.open(p) as ff:
    d=ff[1].data;m=np.isfinite(d['TIME'])&np.isfinite(d['SAP_FLUX'])&(d['QUALITY']==0);t=np.asarray(d['TIME'][m],float);f=np.asarray(d['SAP_FLUX'][m],float)
   if len(t)<100 or t0 is None:continue
   f/=np.median(f);s=appoint.robust_scatter(t,f)
   for n in range(int(np.ceil((t.min()-t0)/P)),int(np.floor((t.max()-t0)/P))+1):
    c=t0+n*P;dep,snr,far,halves=appoint.window_stat(t,f,s,np.array([c]),dur)
    row['events'].append({'sector':int(p.stem[-3:]),'cycle':n,'center':c,'depth_ppt':float(dep[0]*1000),'snr':float(snr[0]),'far':float(far[0]),'halves':bool(halves[0])})
  rows.append(row);print(k,'measured',len(row['events']),flush=True)
 (OUT/f'band-results-{limit}.json').write_text(json.dumps(rows,indent=1))
def longpilot():
 tg=json.load(open(AD/'targets.json')); old=[json.loads(l) for l in open(AD/'results-overlap.jsonl')]
 # Explicit hypothesis: the 14-hour duration ceiling plus far-ratio/null gates suppress long eclipses.
 eligible=[r for r in old if not r.get('control') and r.get('best',{}).get('dur_h')==14 and r['best'].get('halves') and r['best'].get('far') is not None and .6<r['best']['far']<1.6 and r['best']['snr']>=8 and (r.get('z') is None or r['z']<8)]
 selected=sorted(eligible,key=lambda r:(float(tg[r['tic']]['gaia']['phot_g_mean_mag']),r['tic']))[:16]
 (OUT/'long-selection.json').write_text(json.dumps({'rule':'brightest16 noncontrols historical14h, halves, far0.6-1.6, snr>=8, z<8 or unavailable; no outcome selection','eligible_count':len(eligible),'selected':selected,'source_sha256':sha(AD/'results-overlap.jsonl')},indent=1))
 rows=[]
 for r in selected:
  k=r['tic'];p=AD/f"{k}_s{r['best']['sector']:03d}.fits";out={'tic':k,'historical_best':r['best'],'historical_z':r.get('z'),'path':str(p)}
  if not p.exists():out['error']='cached FITS absent';rows.append(out);continue
  out['sha256']=sha(p);t,f=appoint.load(str(p));t,f=appoint.binit(t,f);s=appoint.robust_scatter(t,f);c=np.arange(r['best']['t']-.5,r['best']['t']+.5,1/96);out['duration_tests']=[]
  for dh in [8,14,18,24,36,48]:
   de,sn,far,ha=appoint.window_stat(t,f,s,c,dh/24)
   if not np.isfinite(sn).any():continue
   i=np.nanargmax(sn);out['duration_tests'].append({'duration_h':dh,'center':float(c[i]),'depth_ppt':float(de[i]*1e3),'snr':float(sn[i]),'far':float(far[i]),'halves':bool(ha[i])})
  rows.append(out);print('long',k,flush=True)
 (OUT/'long-results.json').write_text(json.dumps(rows,indent=1))
if __name__=='__main__':
 if sys.argv[1]=='availability':
  keys=['28594244','50662345','193016110','67717320','28596169','334634917','365156806','366141684']
  with concurrent.futures.ThreadPoolExecutor(4) as ex:r=list(ex.map(availability,keys))
  (OUT/'availability-summary.json').write_text(json.dumps(r,indent=1));print(json.dumps(r,indent=1))
 elif sys.argv[1]=='band':band()
 elif sys.argv[1]=='long':longpilot()
