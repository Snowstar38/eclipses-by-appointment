import io,zipfile,json,hashlib,csv
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).parent
cases=[('Q082',11,1619.39,.35,.8,1.5,'5866918974111662848'),('Q083',57,2872.425,.25,.65,1.05,'387423818380396416'),('Q083',84,3602.601,.25,.65,1.05,'387423818380396416'),('Q090',41,2430,.7,7,9,'2143064916926398848')]
out=[]
for sid,sec,c,h,lo,hi,targetid in cases:
 p=B/f'helper-{sid}-s{sec}.zip'; raw=p.read_bytes()
 with zipfile.ZipFile(io.BytesIO(raw)) as z: data=z.read(z.namelist()[0])
 with fits.open(io.BytesIO(data),memmap=False) as f:
  a=f[1].data;t=np.array(a['TIME'],float);cube=np.array(a['FLUX'],float);q=np.array(a['QUALITY']);w=WCS(f[2].header)
 rows=list(csv.DictReader((B/f'helper-{sid}-gaia.csv').open())); coords=[]
 for r in rows:
  x,y=w.world_to_pixel_values(float(r['ra']),float(r['dec']));coords.append({'id':r['source_id'],'G':float(r['phot_g_mean_mag']),'x':float(x),'y':float(y),'target':r['source_id']==targetid})
 tar=next(x for x in coords if x['target']); good=(q==0)&np.isfinite(t)&np.all(np.isfinite(cube),axis=(1,2));core=good&(abs(t-c)<h);side=good&(abs(t-c)>lo)&(abs(t-c)<hi)
 base=np.median(cube[side],axis=0);dip=np.median(cube[core],axis=0);dif=base-dip; yy,xx=np.indices(base.shape); ann=((xx-tar['x'])**2+(yy-tar['y'])**2)>4**2; sky=np.median(base[ann]); near=(xx-tar['x'])**2+(yy-tar['y'])**2<2**2; targetflux=float((base[near]-sky).sum()); wt=np.maximum(dif,0)*near; total=wt.sum(); cent=[float((wt*xx).sum()/total),float((wt*yy).sum()/total)] if total>0 else None
 entry={'sample':sid,'sector':sec,'center':c,'target':tar,'ncore':int(core.sum()),'nside':int(side.sum()),'sky_median':float(sky),'target_aperture_background_subtracted':targetflux,'center_pixel':float(base[round(tar['y']),round(tar['x'])]),'difference_centroid':cent,'zip_sha256':hashlib.sha256(raw).hexdigest(),'gaia_csv_sha256':hashlib.sha256((B/f'helper-{sid}-gaia.csv').read_bytes()).hexdigest(),'sources':coords}
 out.append(entry)
 fig,ax=plt.subplots(1,2,figsize=(10,4));ax[0].imshow(base,origin='lower');ax[1].imshow(dif,origin='lower',cmap='RdBu_r');
 for a in ax:
  for v in coords:
   if -0.5<v['x']<10.5 and -.5<v['y']<10.5:
    a.plot(v['x'],v['y'],'rx' if v['target'] else 'co');a.text(v['x']+.15,v['y']+.15,f"{v['G']:.1f}",color='white',fontsize=7)
 ax[0].set_title('baseline');ax[1].set_title('baseline - trough');fig.suptitle(f'{sid} S{sec}');fig.tight_layout();fig.savefig(B/f'helper-{sid}-s{sec}-pixel.png',dpi=130);plt.close(fig)
(B/'helper-pixel.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
