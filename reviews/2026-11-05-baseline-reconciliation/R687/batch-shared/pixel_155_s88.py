"""TESScut s88 A-event difference image at the frozen Gaia coordinate."""
import hashlib, io, json, math, urllib.parse, urllib.request, zipfile
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

W=Path(__file__).resolve().parent; F=W.parent/'search256'/'followups'
gaia=json.loads((W/'../search256/fresh-targets-256.json').resolve().read_text())['155346713']['gaia']
ra,dec=float(gaia['ra']),float(gaia['dec']); gid=gaia['source_id']
url='https://mast.stsci.edu/tesscut/api/v0.1/astrocut?'+urllib.parse.urlencode({'ra':ra,'dec':dec,'y':9,'x':9,'units':'px','sector':88})
receipt={'tic':155346713,'gaia_dr3_source_id':gid,'sector':88,'url':url,'cutout_px':9}
try:
    with urllib.request.urlopen(url,timeout=150) as response: archive=response.read(120_000_001)
    if len(archive)>120_000_000: raise ValueError('TESScut archive exceeds 120 MB cap')
    z=zipfile.ZipFile(io.BytesIO(archive)); members=z.namelist()
    assert len(members)==1 and members[0].lower().endswith('.fits'),members
    raw=z.read(members[0]);path=W/'155346713_tesscut_s088.fits';path.write_bytes(raw)
    receipt.update(status='ok',archive_member=members[0],zip_sha256=hashlib.sha256(archive).hexdigest(),
                   fits_sha256=hashlib.sha256(raw).hexdigest(),fits_path=str(path),bytes=len(raw))
    with fits.open(path,memmap=False) as h:
        d=h[1].data; t=np.asarray(d['TIME'],float);ff=np.asarray(d['FLUX'],float);q=np.asarray(d['QUALITY'],int)
        wcs=WCS(h[2].header);receipt['n_cadences']=len(t)
    valid=np.isfinite(t)&(q==0)&np.all(np.isfinite(ff),axis=(1,2))&(t>3701.1)&(t<3703.55)
    t=t[valid]; ff=ff[valid]
    # Nearby out-of-eclipse flux at both sides; avoid the 1.03-day event.
    core=abs(t-3702.329)<.20
    flank=(abs(t-3702.329)>.78)&(abs(t-3702.329)<1.2)
    assert core.sum()>10 and flank.sum()>10,(core.sum(),flank.sum())
    before=np.median(ff[flank],axis=0);during=np.median(ff[core],axis=0)
    deficit=before-during
    target=np.array(wcs.all_world2pix(ra,dec,0),float)
    yy,xx=np.mgrid[:deficit.shape[0],:deficit.shape[1]]
    mask=(abs(xx-target[0])<2.5)&(abs(yy-target[1])<2.5)
    weight=np.clip(deficit,0,None)*mask
    center=np.array([(weight*xx).sum()/weight.sum(),(weight*yy).sum()/weight.sum()])
    result={'tic':155346713,'sector':88,'kind':'A','n_core_cadences':int(core.sum()),
            'n_flank_cadences':int(flank.sum()),'core_rule':'|BTJD-3702.329|<0.20 d',
            'flank_rule':'0.78<|BTJD-3702.329|<1.2 d','target_xy':target.tolist(),
            'deficit_centroid_xy':center.tolist(),
            'target_offset_arcsec':float(np.linalg.norm(center-target)*21),
            'cutout_sha256':receipt['fits_sha256'],
            'limitation':'Exploratory 9x9 median difference image; centroid error not calibrated; pulsating baseline.'}
    (W/'pixel-155-s88.json').write_text(json.dumps(result,indent=2))
    fig,axs=plt.subplots(1,3,figsize=(12,4))
    for ax,img,title in zip(axs,[before,during,deficit],['flank median','eclipse core median','flank - core']):
        im=ax.imshow(img,origin='lower');fig.colorbar(im,ax=ax,fraction=.05)
        ax.plot(*target,'r+',ms=14,mew=2);ax.plot(*center,'mo',mfc='none',ms=11)
        ax.set_title(title)
    fig.suptitle(f'TIC 155346713 s88 A; target offset {result["target_offset_arcsec"]:.1f} arcsec')
    fig.tight_layout();fig.savefig(W/'pixel-155-s88.png',dpi=140)
    print(json.dumps(result,indent=2))
except Exception as e:
    receipt.update(status='error',error=repr(e)); print(repr(e))
(W/'pixel-155-s88-download.json').write_text(json.dumps(receipt,indent=2))
