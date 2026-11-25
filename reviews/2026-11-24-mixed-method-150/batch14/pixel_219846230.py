"""Test whether the three S48 TIC 219846230 dips occupy one detector pixel."""
import argparse
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EVENTS = [(2616.2194, .05), (2625.9347, .07), (2627.3097, .045)]


def write_csv(path, rows):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def window(time, center, width):
    phase = (time-center)/width
    return ((phase>=-2)&(phase<=-1), abs(phase)<.35, (phase>=1)&(phase<=2))


def deficit(time, data, center, width):
    left, core, right = window(time,center,width)
    if any(np.count_nonzero(i)<3 for i in (left,core,right)):
        return None
    before, during, after = (np.median(data[m],axis=0) for m in (left,core,right))
    tl, ti, tr = map(lambda m: np.median(time[m]),(left,core,right))
    return before+(after-before)*(ti-tl)/(tr-tl)-during, (left,core,right)


def align_baseline(t, values, masks):
    left, _, right = masks
    before, after = np.nanmedian(values[left],axis=0), np.nanmedian(values[right],axis=0)
    l, r = np.median(t[left]),np.median(t[right])
    trailing = (1,)*(values.ndim-1)
    return before+(after-before)*((t-l)/(r-l)).reshape((-1,)+trailing)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--ffi",type=Path,default=ROOT/"tmp/mixed150-pixels/219846230-48.fits")
    parser.add_argument("--qlp",type=Path,default=ROOT/"sky/data/qlp-sb-p20-60/219846230_s048.fits")
    args=parser.parse_args()
    with fits.open(args.ffi) as source, fits.open(args.qlp) as other:
        d=source[1].data
        good=(d["QUALITY"]==0)&np.isfinite(d["TIME"])
        t,f=(d[k][good].astype(float) for k in ("TIME","FLUX"))
        bkg=d["FLUX_BKG"][good].astype(float)
        q=other[1].data
        corrected="KSPSAP_FLUX" if "KSPSAP_FLUX" in q.names else "DET_FLUX"
        qualified=(q["QUALITY"]==0)&np.isfinite(q["TIME"])
        q=q[qualified]
        q=q[np.argsort(q["TIME"])]
        qt=q["TIME"]
        # The TESScut product stores zero in every CADENCENO field.
        # Match the slightly different barycentric timestamps within 17.28 s,
        # much less than the 600 s S48 exposures.
        after=np.clip(np.searchsorted(qt,t),1,qt.size-1)
        before=after-1
        nearest=np.where(abs(qt[after]-t)<abs(qt[before]-t),after,before)
        match=abs(qt[nearest]-t)<.0002
        aligned=np.full((t.size,2),np.nan)
        cad=np.full(t.size,-1)
        cad[match]=q["CADENCENO"][nearest[match]]
        for k,name in enumerate(("SAP_FLUX",corrected)):
            aligned[match,k]=q[name][nearest[match]]
        h=source[1].header
        origin=np.array([h["1CRV4P"],h["2CRV4P"]])
    ref=np.median(f,axis=0)
    yy,xx=np.indices(ref.shape)
    # A plane through the faint outer pixels models additive spatial background.
    # The stellar profiles are not part of the fit.
    quiet=(ref<85)&(xx>0)&(xx<14)&(yy>0)&(yy<14)
    design=np.stack([np.ones(ref.shape),xx-7,yy-7],axis=-1)
    coefficients=np.linalg.lstsq(design[quiet],f[:,quiet].T,rcond=None)[0]
    sky=np.einsum("yxp,pt->tyx",design,coefficients)
    clean=f-sky
    signal=[]
    for c,w in EVENTS:
        diff,_=deficit(t,clean,c,w)
        y,x=np.unravel_index(np.argmax(diff),diff.shape)
        signal.append((y,x))
    assert len(set(signal))==1
    y,x=signal[0]
    group=(abs(xx-x)<=1)&(abs(yy-y)<=1)
    rim=group&((xx!=x)|(yy!=y))
    quiet_ref=np.median(clean,axis=0)
    prf=[]
    for label,px,py in (("target",7,8),("local star",10,10),("faint local peak",4,9)):
        cut=quiet_ref[py-1:py+2,px-1:px+2]
        annulus=(np.hypot(xx-px,yy-py)>=2)&(np.hypot(xx-px,yy-py)<=3)&(abs(quiet_ref)<35)
        ped=np.median(quiet_ref[annulus])
        block=cut-ped
        prf.append(dict(label=label,x=px,y=py,central_e_per_s=block[1,1],
                        adjacent8_e_per_s=block.sum()-block[1,1],
                        adjacent8_to_center=(block.sum()-block[1,1])/block[1,1]))
    write_csv(HERE/"219846230-prf-reference.csv",prf)
    rows,pixels,history=[],[],[]
    fig,axes=plt.subplots(3,3,figsize=(12,9),layout="constrained",height_ratios=[1,1.2,.7])
    for k,(center,width) in enumerate(EVENTS):
        diff,masks=deficit(t,clean,center,width)
        left,core,right=masks
        raw,_=deficit(t,f,center,width)
        drift=align_baseline(t,clean,masks)-clean
        wanted=abs(t-center)<3*width
        pix=drift[:,y,x]
        neighbors=drift[:,rim].sum(axis=1)
        flux=align_baseline(t,aligned,masks)-aligned
        flux*=1000/align_baseline(t,aligned,masks)
        sample=wanted & np.isfinite(flux[:,0]) & np.isfinite(flux[:,1])
        r=np.corrcoef(np.column_stack([pix[sample],flux[sample]]).T)[0,1:]
        # Nearby pseudo-events estimate repeatability of summed surround loss
        # on exactly the same apertures, excluding portions near the real dips.
        blank=[]
        for candidate in t[(abs(t-center)>.25)&(abs(t-center)<1.1)][::3]:
            if any(abs(candidate-c)<3*(width+w) for c,w in EVENTS):
                continue
            sample_diff=deficit(t,clean,candidate,width)
            if sample_diff is not None:
                blank.append(sample_diff[0][rim].sum())
        mad=1.4826*np.median(abs(np.array(blank)-np.median(blank)))
        upper=(max(0,diff[rim].sum())+3*mad)/diff[y,x]
        wide=abs(t-center)<.75
        split=np.median(clean[core,y,x])+diff[y,x]/2
        low=wide&(clean[:,y,x]<split)
        high=wide&~low
        lower, upper_level=(np.median(clean[m,y,x]) for m in (low,high))
        rows.append(dict(center_btjd=center,width_d=width,stamp_x=x,stamp_y=y,detector_column=origin[0]+x,
                         detector_row=origin[1]+y,left_n=left.sum(),core_n=core.sum(),right_n=right.sum(),
                         raw_pixel_loss=raw[y,x],sky_corrected_pixel_loss=diff[y,x],
                         sky_corrected_adjacent8_loss=diff[rim].sum(),blank_windows=len(blank),
                         adjacent8_blank_mad=mad,adjacent8_ratio_plus_3mad=upper,
                         low_median_e_per_s=lower,high_median_e_per_s=upper_level,
                         low_n=low.sum(),high_n=high.sum(),
                         pearson_pixel_qlp_sap=r[0],pearson_pixel_qlp_corrected=r[1],
                         qlp_sap_ppt=np.nanmedian(flux[core,0]),qlp_corrected_ppt=np.nanmedian(flux[core,1])))
        for py,px in zip(*np.where(group)):
            pixels.append(dict(center_btjd=center,x=px,y=py,raw_loss_e_per_s=raw[py,px],
                               loss_e_per_s=diff[py,px],stamp_median_flux_e_per_s=ref[py,px]))
        for i in np.flatnonzero(wanted):
            history.append(dict(center_btjd=center,time_btjd=t[i],cadenceno=int(cad[i]),
                                pixel_flux_e_per_s=clean[i,y,x],pixel_loss_e_per_s=pix[i],
                                adjacent8_loss_e_per_s=neighbors[i],qlp_sap_loss_ppt=flux[i,0],
                                qlp_corrected_loss_ppt=flux[i,1]))
        ax=axes[0,k]
        cut=diff[y-1:y+2,x-1:x+2]
        ax.imshow(cut,vmin=-7,vmax=65,origin="lower",cmap="coolwarm")
        for py in range(3):
            for px in range(3):
                ax.text(px,py,f"{cut[py,px]:.1f}",ha="center",va="center",
                        color="white" if cut[py,px]>45 else "black",fontsize=9)
        ax.set(title=f"{center:.4f} BTJD | loss (e-/s)",xticks=range(3),yticks=range(3),
               xticklabels=range(x-1,x+2),yticklabels=range(y-1,y+2))
        ax=axes[1,k]
        d=t[wanted]-center
        ax.plot(d,pix[wanted],".-",label="Pixel (6, 9)",c="tab:blue",lw=.9)
        ax.plot(d,neighbors[wanted],".-",label="Eight neighbors",c=".45",lw=.9)
        ax.axvspan(-.35*width,.35*width,color="orange",alpha=.15)
        ax.axhline(0,c=".5",lw=.5)
        ax.set(xlabel="Days from event",ylabel="Native FFI loss (e-/s)")
        second=ax.twinx()
        second.plot(d,flux[wanted,0],"--",lw=.8,c="tab:orange",label="QLP SAP")
        second.plot(d,flux[wanted,1],":",lw=1,c="tab:purple",label="QLP corrected")
        second.set_ylabel("QLP loss (ppt)")
        if k==0:
            ax.legend(fontsize=7,loc="upper left")
            second.legend(fontsize=7,loc="upper right")
        ax=axes[2,k]
        ax.plot(t[wide]-center,clean[wide,y,x],".",ms=2)
        ax.axvline(0,c="tab:red",lw=1)
        ax.set(xlabel="Days from event",ylabel="Pixel flux (e-/s)")
    fig.suptitle("TIC 219846230 • TESS Sector 48 • one native detector pixel drives all three QLP dips")
    fig.savefig(HERE/"219846230-native-pixel.png",dpi=125)
    plt.close(fig)
    write_csv(HERE/"219846230-native-summary.csv",rows)
    write_csv(HERE/"219846230-native-neighbors.csv",pixels)
    write_csv(HERE/"219846230-native-cadences.csv",history)
    print(f"Background column range {np.nanmin(bkg)}–{np.nanmax(bkg)}; matched {match.sum()} cadences")


if __name__=="__main__":
    main()
