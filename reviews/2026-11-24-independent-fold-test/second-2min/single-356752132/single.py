import concurrent.futures
import io,json,hashlib
from pathlib import Path
import numpy as np,pandas as pd,requests
from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
import astropy.units as u
ROOT=Path(__file__).resolve().parent
B=ROOT.parent
TIC='356752132'
CENTER=2454.7637
RA,DEC=61.2056621205833,9.58541843190467
manifest=json.loads((B/'sol/archive.json').read_text())
line=next(r for r in manifest if str(r['tic'])==TIC and r['sector']==42)
stem=line['url'].split('/')[-1]
lc_url=line['url']
tp_url='https://stpubdata.s3.us-east-1.amazonaws.com/tess/public/tid/s0042/0000/0003/5675/2132/'+stem.replace('_lc.fits','_tp.fits')
def download(name,url):
 path=ROOT/f'{name}.fits'
 if not path.exists():
  r=requests.get(url, timeout=(7,24));r.raise_for_status();path.write_bytes(r.content)
 return path
with concurrent.futures.ThreadPoolExecutor(3) as pool:
 lp,pp=list(pool.map(lambda args:download(*args),[('target-lc',lc_url),('target-tpf',tp_url)]))
for p in (lp,pp):
 with fits.open(p) as h:
  print(p.name,p.stat().st_size,hashlib.file_digest(p.open('rb'),'sha256').hexdigest())
  print([(x.name,x.data.shape if x.data is not None else None) for x in h])
  print({x:h[0].header.get(x) for x in ['TICID','SECTOR','CAMERA','CCD','CROWDSAP','FLFRCSAP']})
  print({x:h[1].header.get(x) for x in ['CROWDSAP','FLFRCSAP']})
  print(h[1].columns.names)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

center=2454.769
summary=dict(tic=int(TIC),sector=42,camera=4,ccd=3,provided_btjd=CENTER,
             measurement_center_btjd=center,core_half_width_d=.012,shoulder_abs_limits_d=[.07,.13],
             files={p.name:dict(url=url,sha256=hashlib.file_digest(p.open("rb"),"sha256").hexdigest())
                    for p,url in [(lp,lc_url),(pp,tp_url)]})
with fits.open(lp) as h, fits.open(pp) as hp:
    d=h[1].data
    t=d["TIME"]
    pix=hp[1].data
    assert np.all(t==pix["TIME"],where=np.isfinite(t))
    ap=(hp[2].data&2)!=0
    dt=t-center
    quality=d["QUALITY"]
    in_all=abs(dt)<.012
    inner=in_all&(quality==0)
    shoulder=(abs(dt)>.07)&(abs(dt)<.13)&(quality==0)
    out=(abs(dt)<.14)&(quality==0)
    fit_masks=dict(n_inner=int(inner.sum()),n_shoulder=int(shoulder.sum()),
                   n_quality_nonzero_inner=int(np.sum(in_all&(quality!=0))),
                   aperture_pixels=int(ap.sum()),crowdsap=h[1].header["CROWDSAP"],
                   flfrcsap=h[1].header["FLFRCSAP"])
    summary.update(fit_masks)
    f=pix["FLUX"][out].astype(float); b=pix["FLUX_BKG"][out].astype(float)
    raw=pix["RAW_CNTS"][out].astype(float)
    x=dt[out]*24
    y,sx=np.indices(ap.shape)
    ring=(np.hypot(sx-6.79,y-6.85)>3)&(sx<=5)
    base_img=np.nanmedian((f+b)[shoulder[out]],0)
    in_flx=f+b-base_img
    mx=np.argmax(in_flx.reshape(len(x),-1),axis=1)
    track_y,track_x=np.unravel_index(mx,ap.shape)
    w=WCS(hp[2].header)
    ra,dec=w.pixel_to_world_values(track_x,track_y)
    track_power=np.max(in_flx.reshape(len(x),-1),axis=1)
    table=pd.DataFrame(dict(btjd=t[out],quality=quality[out],
        sap=d["SAP_FLUX"][out],pdc=d["PDCSAP_FLUX"][out],sap_bkg=d["SAP_BKG"][out],
        sap_plus_bkg=d["SAP_FLUX"][out]+d["SAP_BKG"][out],
        pos_corr_1=d["POS_CORR1"][out],pos_corr_2=d["POS_CORR2"][out],
        calibrated_ap=np.sum(f[:,ap],axis=1),background_ap=np.sum(b[:,ap],axis=1),
        pre_subtraction_ap=np.sum((f+b)[:,ap],axis=1),raw_ap=np.sum(raw[:,ap],axis=1),
        calibrated_ring_per_pixel=np.median(f[:,ring],axis=1),
        pre_subtraction_ring_per_pixel=np.median((f+b)[:,ring],axis=1),
        brightest_difference_x=track_x,brightest_difference_y=track_y,
        brightest_difference_ra=ra,brightest_difference_dec=dec,
        brightest_difference_e_per_s=track_power))
    num_cols=list(table.columns[2:14])
    core_meds={}
    for name in num_cols:
        a=table.loc[inner[out],name].median(); c=table.loc[shoulder[out],name].median()
        core_meds[name]=dict(median_core=float(a),median_shoulders=float(c),core_minus_shoulder=float(a-c))
    summary["window_statistics"]=core_meds
    d_sap= -core_meds["sap"]["core_minus_shoulder"]/core_meds["sap"]["median_shoulders"]
    summary["naive_fractional_sap_loss_divided_by_crowdsap"]=float(d_sap/fit_masks["crowdsap"])
    summary["interpretation"]="Local moving positive feature at stamp edge drove a broad background overestimate. No target eclipse in aperture after restoring the pipeline background."
    table.to_csv(ROOT/"window.csv",index=False)
    fig,ax=plt.subplots(1,3,figsize=(13.4,4.2),layout="constrained")
    for name in ("sap","sap_bkg","sap_plus_bkg"):
        ax[0].plot(x,table[name]-core_meds[name]["median_shoulders"],label=name,marker=".",ms=2)
    ax[0].axhline(0,color=".6",lw=.7)
    ax[0].legend(fontsize=8); ax[0].set(xlabel="Hours from core center",ylabel="Change from shoulders (e−/s)")
    df=np.median(f[inner[out]],0)-np.median(f[shoulder[out]],0)
    im=ax[1].imshow(df,origin="lower",vmin=-38,vmax=80,cmap="coolwarm")
    ax[1].contour(ap,levels=[.5],colors="black",linewidths=1)
    ax[1].set(title="Calibrated flux change",xlabel="Stamp x",ylabel="Stamp y")
    fig.colorbar(im,ax=ax[1],label="e−/s per pixel")
    strong=track_power>70
    im2=ax[2].scatter(track_x[strong],track_y[strong]+np.linspace(-.09,.09,strong.sum()),c=x[strong],s=24,cmap="viridis")
    ax[2].contour(ap,levels=[.5],colors="black",linewidths=1)
    ax[2].set(title="Brightest moving excess",xlabel="Stamp x",ylabel="Stamp y",xlim=(0,10.6),ylim=(-.5,10.5),aspect="equal")
    fig.colorbar(im2,ax=ax[2],label="Hours from core center")
    fig.savefig(ROOT/"event.png",dpi=160)
(ROOT/"evidence.json").write_text(json.dumps(summary,indent=2),encoding="utf8")
print(json.dumps(summary,indent=2))
