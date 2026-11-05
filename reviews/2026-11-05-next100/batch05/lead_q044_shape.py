"""Compare Q044 repeated shape in raw QLP SAP and independent TESSCut aperture."""
import hashlib,io,json,zipfile
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;tic='143497778';d=B/tic
ctx=json.loads((d/'lead-context.json').read_text());s=next(z for z in ctx['sectors'] if z['sector']==89)
fp=Path(s['source_path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==s['source_sha256']
with fits.open(fp,memmap=False) as h:
 a=h[1].data;t0=np.asarray(a['TIME'],float);f0=np.asarray(a['SAP_FLUX'],float);q0=np.asarray(a['QUALITY'],int)
good0=np.isfinite(t0)&np.isfinite(f0)&(f0>0)&(q0==0);t0=t0[good0];f0=f0[good0]
zpath=B/'lead-Q044-s089.zip';zhash=hashlib.sha256(zpath.read_bytes()).hexdigest()
with zipfile.ZipFile(zpath) as arc:raw=arc.read(arc.namelist()[0])
with fits.open(io.BytesIO(raw),memmap=False) as h:
 a=h[1].data;t=np.asarray(a['TIME'],float);F=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY'],int);w=WCS(h[2].header)
tx,ty=w.world_to_pixel_values(118.06761825541145,-44.94875919504381);tx=float(np.asarray(tx).reshape(-1)[0]);ty=float(np.asarray(ty).reshape(-1)[0])
yy,xx=np.indices(F.shape[1:]);ap=(np.abs(xx-round(tx))<=1)&(np.abs(yy-round(ty))<=1);sky=((xx<2)|(xx>8)|(yy<2)|(yy>8))
bg=np.nanmedian(np.where(F[:,sky]>0,F[:,sky],np.nan),axis=1);f=np.sum(F[:,ap],axis=1)-bg*ap.sum();good=np.isfinite(t)&(q==0)&np.isfinite(f)&(f>0)&np.isfinite(bg);t=t[good];f=f[good]
centers=[3719.77709,3743.1722];out=[];fig,axs=plt.subplots(2,1,figsize=(10,6))
for ax,c in zip(axs,centers):
 rec={'center_btjd':c,'qlp_fits_sha256':s['source_sha256'],'tesscut_zip_sha256':zhash,'tesscut_target_xy':[tx,ty]}
 for label,tt,ff in [('QLP_SAP',t0,f0),('TESSCut_3x3',t,f)]:
  x=tt-c;sel=np.abs(x)<.8;x=x[sel];y=ff[sel];base=np.median(y[(x>-.75)&(x<-.45)]);yn=y/base
  ax.plot(x,yn,'.',ms=2,alpha=.65,label=label)
  levels={}
  for name,lo,hi in [('before',-.7,-.45),('ingress',-.38,-.28),('floor',-.18,.17),('egress',.3,.4),('after',.5,.7)]:
   v=yn[(x>=lo)&(x<hi)];levels[name]=dict(points=len(v),median=float(np.median(v)) if len(v) else None,mad=float(1.4826*np.median(np.abs(v-np.median(v)))) if len(v) else None)
  rec[label]=levels
 out.append(rec);ax.set(xlim=(-.8,.8),ylabel='flux / pre-event median',title=f'Q044 S89 BTJD {c:.5f}');ax.legend()
fig.tight_layout();fig.savefig(d/'lead-shape.png',dpi=140);plt.close(fig)
(d/'lead-shape.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
