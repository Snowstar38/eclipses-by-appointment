import pathlib,json,glob,numpy as np
from astropy.io import fits
r=pathlib.Path(__file__).parent
for path in r.glob('*_measurements.json'):
 m=json.loads(path.read_text());tic=m['tic'];ep=m['ephemeris'];P=ep['P'];t0=ep['T0']; widths=[e['T14_d'] for e in m['events'] if e['coverage_ok']];width=float(np.median(widths));peaks=[]
 for fn in glob.glob(str(r.parent/'data'/f'{tic}_s*.fits')):
  a=fits.getdata(fn,1);t=np.array(a['TIME'],float);y=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY']);ok=np.isfinite(t)&np.isfinite(y)&(q==0);t=t[ok];y=y[ok];sec=int(pathlib.Path(fn).stem.split('_s')[-1]);
  if len(t)<20:continue
  for c in np.arange(min(t)+.5,max(t)-.5,max(.04,width/3)):
   inn=abs(t-c)<width/2; flank=(abs(t-c)>width*.7)&(abs(t-c)<max(.5,width*1.5));
   if inn.sum()<3 or flank.sum()<8:continue
   yy=y/np.median(y[flank]);depth=float(np.median(yy[flank])-np.median(yy[inn]));noise=float(1.4826*np.median(abs(yy[flank]-np.median(yy[flank]))));cad=np.median(np.diff(t));inside=t[inn];gap=float(np.max(np.diff(inside))) if len(inside)>1 else 99;phase=float(((c-t0)/P)%1)
   if depth>max(.003,3*noise):peaks.append({'sector':sec,'time':float(c),'depth':depth,'phase':phase,'gap_flag':bool(gap>2.1*cad),'n_in':int(inn.sum())})
 # de-duplicate overlapping peaks
 peaks.sort(key=lambda x:x['depth'],reverse=True);kept=[]
 for e in peaks:
  if not any(v['sector']==e['sector'] and abs(v['time']-e['time'])<width for v in kept):kept.append(e)
 out={'width_d':width,'threshold':'median dip > max(3 ppt, 3x flank MAD); not calibrated S/N','peaks':kept,'caveat':'coarse box census; threshold misses shallow events and correlated trends can cause false peaks; gap flag addresses only in-window gaps'};(r/f'{tic}_blind_census.json').write_text(json.dumps(out,indent=2));print(tic,len(kept),sum(x['gap_flag'] for x in kept))
