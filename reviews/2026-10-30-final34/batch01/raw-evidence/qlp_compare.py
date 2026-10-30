import pathlib,json,urllib.request,urllib.parse,concurrent.futures,hashlib,numpy as np
from astropy.io import fits
from scipy.optimize import least_squares
R=pathlib.Path(__file__).parent; raw=json.load(open(R/'raw-events.json'))
def task(item):
 tic,v=item;sec=v['sector']; padded=tic.zfill(16); parts='/'.join([padded[i:i+4] for i in range(0,16,4)]);uri=f'mast:HLSP/qlp/s{sec:04d}/{parts}/hlsp_qlp_tess_ffi_s{sec:04d}-{padded}_tess_v01_llc.fits';path=R/tic/f'qlp_s{sec:03d}.fits'
 try:
  if not path.exists(): path.write_bytes(urllib.request.urlopen('https://mast.stsci.edu/api/v0.1/Download/file?'+urllib.parse.urlencode({'uri':uri}),timeout=60).read())
  with fits.open(path) as h:
   hdr=h[0].header;a=h[1].data;t=np.array(a['TIME'],float);y=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY']);ok=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[ok];y=y[ok]
  rows=[]
  for ev in v['events']:
   D=ev['duration_d']; tc=ev['tc']; w=min(v['seed_period_d']*.2,max(.6,3*D));m=abs(t-tc)<w;x=t[m]-tc;z=y[m];
   if len(x)<20 or sum(abs(x)<D/2)<3:continue
   z=z/np.median(z)
   def f(a):return a[0]+a[1]*x+a[2]*x*x-a[3]*np.clip((a[5]/2-abs(x-a[4]))/(a[5]*a[6]),0,1)
   try:
    a=least_squares(lambda a:f(a)-z,[1,0,0,min(.8,max(.005,ev['depth'])),0,D,.25],bounds=([.3,-1,-1,0,-D,.3*D,.05],[1.7,1,1,.99,D,2*D,.5]),max_nfev=2000).x;rows.append({'cycle':ev['cycle'],'tc':float(tc+a[4]),'depth':float(a[3]),'duration_d':float(a[5]),'rms':float(np.std(z-f(a))),'n':len(x),'n_in':int(sum(abs(x-a[4])<a[5]/2)),'edge':bool(abs(a[4])>.95*D or a[5]>1.99*D)})
   except Exception as ex:rows.append({'cycle':ev['cycle'],'error':repr(ex)})
  good=[e for e in rows if 'tc' in e and not e['edge'] and e['depth']>3*e['rms']]; ep=None
  if len(good)>=2:
   a=np.polyfit([e['cycle'] for e in good],[e['tc'] for e in good],1);ep={'period_d':float(a[0]),'epoch_btjd_cycle_zero':float(a[1]),'n_events':len(good),'timing_rms_min':float(np.std([e['tc']-np.polyval(a,e['cycle']) for e in good])*1440)}
  return tic,{'uri':uri,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'header_TICID':str(hdr.get('TICID')),'header_SECTOR':hdr.get('SECTOR'),'events':rows,'representative_ephemeris':ep,'method':'QLP SAP_FLUX QUALITY=0; quadratic local baseline and trapezoid; independent extraction, same TESS FFI photons; cycle counts seeded from previous search; native cadence, no exposure integration or uncertainty.'}
 except Exception as ex:return tic,{'uri':uri,'error':repr(ex)}
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool: out=dict(pool.map(task,raw.items()))
json.dump(out,open(R/'qlp-results.json','w'),indent=2)
for tic,v in out.items():print(tic,len(v.get('events',[])),v.get('representative_ephemeris'),v.get('error'),flush=True)
