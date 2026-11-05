from pathlib import Path
from astropy.io import fits
import numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt,json,hashlib
p=Path(__file__).parent/'174306672';fp=p/'helper-s84-tesscut.fits';qp=Path(r'[local-path-redacted]')
with fits.open(fp,memmap=False) as h:
 d=h[1].data;t=np.array(d['TIME']);q=np.array(d['QUALITY']);f=np.array(d['FLUX']); bg=np.nanmedian(f[:,0:3,3:8],axis=(1,2));ap=np.nansum(f[:,4:7,4:8],axis=(1,2));corr=ap-12*bg
with fits.open(qp) as h:
 d=h[1].data;tt=np.array(d['TIME']);qq=np.array(d['QUALITY']);sap=np.array(d['SAP_FLUX'])
fig,ax=plt.subplots(3,1,figsize=(12,8),sharex=True);g=(q==0)&np.isfinite(t);gq=(qq==0)&np.isfinite(tt)&np.isfinite(sap)
for a,y,l in [(ax[0],bg,'active background counts / pixel'),(ax[1],corr,'background-corrected 4x3 counts')]:a.plot(t[g],y[g],'.',ms=.5);a.set_ylabel(l)
ax[2].plot(tt[gq],sap[gq],'.',ms=.5);ax[2].set_ylabel('QLP SAP');ax[2].set_xlabel('BTJD');fig.tight_layout();fig.savefig(p/'helper-s84-background.png',dpi=140)
out=[]
for core,side in [((3585.72,3585.95),[(3585.1,3585.35),(3586.45,3586.7)]),((3599.05,3599.55),[(3597.5,3598.1),(3600.5,3601.1)])]:
 c=g&(t>core[0])&(t<core[1]);s=g&(((t>side[0][0])&(t<side[0][1]))|((t>side[1][0])&(t<side[1][1])));cq=gq&(tt>core[0])&(tt<core[1]);sq=gq&(((tt>side[0][0])&(tt<side[0][1]))|((tt>side[1][0])&(tt<side[1][1])));out.append(dict(core=core,background_core=float(np.median(bg[c])),background_sides=float(np.median(bg[s])),corrected_core=float(np.median(corr[c])),corrected_sides=float(np.median(corr[s])),corrected_frac=float(np.median(corr[c])/np.median(corr[s])-1),sap_frac=float(np.median(sap[cq])/np.median(sap[sq])-1)))
(p/'helper-s84-background.json').write_text(json.dumps(dict(method='4x3 active target+neighbor aperture x4:8 y4:7, subtract 12 times median active sky x3:8 y0:3; detector edge truncates PSFs',results=out,qlp_sha256=hashlib.sha256(qp.read_bytes()).hexdigest(),pixel_sha256=hashlib.sha256(fp.read_bytes()).hexdigest()),indent=2));print(out)
