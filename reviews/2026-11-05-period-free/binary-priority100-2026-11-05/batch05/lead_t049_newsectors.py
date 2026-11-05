"""Bounded current-sector check for T049; source availability is not a null."""
import hashlib,io,json,zipfile
from pathlib import Path
import requests,numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent/'334142514';out=[]
for sector in (108,109):
    try:
        r=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=dict(ra=116.52048301546138,dec=-17.427921591823292,x=11,y=11,units='px',sector=sector),timeout=120);r.raise_for_status()
        z=zipfile.ZipFile(io.BytesIO(r.content));payload=z.read(z.namelist()[0]);path=B/f'lead-s{sector}-tesscut.fits';path.write_bytes(payload)
        with fits.open(path,memmap=False) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY'],int);w=WCS(h[2].header)
        x,y=map(float,w.all_world2pix(116.52048301546138,-17.427921591823292,0));yy,xx=np.indices(f.shape[1:]);mask=(abs(xx-round(x))<=1)&(abs(yy-round(y))<=1);lc=np.nansum(f[:,mask],axis=1)
        good=np.isfinite(t)&np.isfinite(lc)&(q==0);tg=t[good];lg=lc[good]
        rec=dict(sector=sector,url=r.url,zip_sha256=hashlib.sha256(r.content).hexdigest(),fits_sha256=hashlib.sha256(payload).hexdigest(),target_pixel=[x,y],mask_pixel_count=int(mask.sum()),side_median_electrons_per_second=float(np.median(lg)),start_btjd=float(tg.min()),end_btjd=float(tg.max()),n_quality0=int(len(tg)),max_internal_gap_days=float(max(np.diff(tg))),source_path=str(path))
        out.append(rec)
        fig,ax=plt.subplots(figsize=(11,3));ax.plot(tg,lg/np.median(lg),'.',ms=1);ax.set(xlabel='BTJD',ylabel='3x3 raw / sector median',title=f'T049 S{sector} target-centered cutout');fig.tight_layout();fig.savefig(B/f'lead-s{sector}.png',dpi=130);plt.close(fig)
        print(sector,rec['start_btjd'],rec['end_btjd'],rec['n_quality0'],flush=True)
    except Exception as ex:out.append(dict(sector=sector,error=repr(ex)));print(sector,'UNKNOWN',repr(ex),flush=True)
(B/'lead-newsectors.json').write_text(json.dumps(out,indent=2)+'\n')
