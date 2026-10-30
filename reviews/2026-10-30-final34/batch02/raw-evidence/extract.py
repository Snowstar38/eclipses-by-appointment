import json,pathlib,hashlib,numpy as np,subprocess,sys,shutil
from astropy.io import fits
from astropy.wcs import WCS
from scipy.optimize import least_squares
R=pathlib.Path(__file__).parent; B=pathlib.Path(r'[local working path omitted]'); C=pathlib.Path(r'[local working path omitted]'); ids='431698773 424878861 47719859 350335402 48777160 382260140 162234490 358766055 37307440 89575652'.split(); allout={}
for tic in ids:
 try:
  old=next((B/tic).glob('diff*.json')); d=json.load(open(old)); es=d['events']; sec=d['sector']; P=(es[-1]['t']-es[0]['t'])/(es[-1]['cycle']-es[0]['cycle']); t0=es[0]['t']; source=C/('vet'+tic)/('tesscut_s%03d.fits'%sec); gaia=B/tic/'gaia.json'; g=json.load(open(gaia)); out=R/tic;out.mkdir(exist_ok=True);shutil.copyfile(gaia,out/'gaia.json')
  with fits.open(source,memmap=False) as h:
   a=h[1].data;t=np.array(a['TIME'],float);F=np.array(a['FLUX'],float);q=np.array(a['QUALITY']);w=WCS(h[2].header);src=g['src'][0];x,y=w.all_world2pix(float(src['ra']),float(src['dec']),0);ix=int(round(float(x)));iy=int(round(float(y))); b=np.median(np.sort(F.reshape(len(t),-1),axis=1)[:,:int(F.shape[1]*F.shape[2]*.4)],axis=1); flux=F[:,iy-1:iy+2,ix-1:ix+2].sum(axis=(1,2))-9*b;ok=np.isfinite(t)&np.isfinite(flux)&(q==0)&(flux>0);t=t[ok];flux=flux[ok]
  events=[]
  for e in es:
   center=e['t']; m=np.abs(t-center)<min(1.5,P*.2);xx=t[m]-center;yy=flux[m];yy=yy/np.median(yy)
   if len(xx)<20:continue
   def model(a):return a[0]+a[1]*xx+a[2]*xx**2-a[3]*np.clip((a[5]/2-np.abs(xx-a[4]))/(a[5]*a[6]),0,1)
   f=least_squares(lambda a:model(a)-yy,[1,0,0,min(.7,max(.01,d['depth_ap3'])),0,.3,.25],bounds=([.4,-1,-1,0,-.5,.04,.05],[1.6,1,1,.95,.5,1.8,.5]),max_nfev=3000);a=f.x;err=float(np.std(model(a)-yy));events.append(dict(cycle=e['cycle'],tc=float(center+a[4]),depth=float(a[3]),duration_d=float(a[5]),ingress_fraction=float(a[6]),rms=err,n=len(xx),edge=bool(abs(a[4])>.49 or a[5]>1.79)))
  good=[e for e in events if not e['edge'] and e['depth']>3*e['rms']]; ep=None
  if len(good)>1:
   fit=np.polyfit([e['cycle'] for e in good],[e['tc'] for e in good],1); ep={'period_d':float(fit[0]),'epoch_btjd_at_cycle_zero':float(fit[1]),'n_events':len(good),'timing_rms_min':float(np.std([e['tc']-np.polyval(fit,e['cycle']) for e in good])*1440),'note':'conditional on seed cycle counts; same sector; no formal uncertainty'}
  dur=float(np.median([e['duration_d'] for e in good])) if good else .3; dep=float(np.median([e['depth'] for e in good])) if good else d['depth_ap3']; cmd=[sys.executable,str(R/'diffstack.py'),tic,str(sec),str(P),str(t0),str(dur*24),str(dep),'fresh'];run=subprocess.run(cmd,cwd=out,text=True,capture_output=True); (out/'diffstack.log').write_text(run.stdout+'\n'+run.stderr)
  allout[tic]={'sector':sec,'seed_period_d':P,'seed_epoch_btjd':t0,'events':events,'representative_ephemeris':ep,'source_cutout':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'gaia_cache':str(gaia),'gaia_sha256':hashlib.sha256(gaia.read_bytes()).hexdigest(),'seed_receipt':str(old),'seed_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'method':'Independent 3x3 TESScut pixel extraction, median faintest 40% pixel background per cadence, QUALITY=0; quadratic local baseline and trapezoid; same FFI photons as QLP, not independent observations. Seed cycle counts from cached search. Native cadence, no uncertainty or finite exposure model.','diffstack_exit':run.returncode}
  print(tic,len(good),ep,run.returncode,flush=True)
 except Exception as ex:allout[tic]={'error':repr(ex)};print(tic,repr(ex),flush=True)
json.dump(allout,open(R/'raw-events.json','w'),indent=2)

