"""Long-baseline sinusoidal frequency refinement and sector-separated folds."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from astropy.timeseries import LombScargle
from scipy.ndimage import median_filter

from review import ROOT, load, measure, write_csv

CASES = [
    (11,"345949499",.79995844,1,0,1630.6668),
    (11,"267687143",.4669,2,1,1782.0576),
    (13,"468915243",.9255904,1,0,1492.3156),
    (13,"192515640",.198933,1,1,1523.8894),
    (15,"37378337",.5997953,1,1,1523.9525),
    (15,"307642177",.179527,2,1,1792.3602),
    (15,"258526967",.207521845,2,1,1711.4936),
    (15,"466417572",.199227,1,1,2800.2724),
]


def main():
    base=Path(__file__).resolve().parents[1]
    data=ROOT/"sky/data/qlp-sb-p20-60"
    summaries={}
    for batch,tic,trial,multiple,column,epoch in CASES:
        dest=base/f"batch{batch}"
        chunks=[]
        for path in sorted(data.glob(f"{tic}_s*.fits")):
            sector, camera, t, flux, _=load(path,{})
            cadence=np.median(np.diff(t))
            size=max(3,(int(3/cadence)//2)*2+1)
            locally_filtered=flux-median_filter(flux,size=(size,1))
            chunks.append((sector,t,locally_filtered))
        t=np.concatenate([r[1] for r in chunks])
        f=np.concatenate([r[2][:,column] for r in chunks])
        freq=np.linspace(1/trial*.994,1/trial*1.006,14001)
        model=LombScargle(t-epoch,f)
        power=model.power(freq)
        best=int(np.nanargmax(power))
        dominant=1/freq[best]
        period=dominant*multiple
        mod_phase=np.linspace(0,dominant,400,endpoint=False)
        m=model.model(mod_phase,freq[best])
        refined_epoch=epoch+mod_phase[np.argmax(m) if batch<=13 else np.argmin(m)]
        fig,axes=plt.subplots(2,2,figsize=(11,6.3),layout="constrained")
        axes[0,0].plot(1/freq,power,lw=.7)
        axes[0,0].axvline(dominant, c="tab:red",lw=.8)
        axes[0,0].set(xlabel="Dominant Fourier period (d)", ylabel="LS power")
        axes[0,1].axis("off")
        axes[0,1].text(.04,.8,f"Search period {dominant:.9f} d\nDisplayed period {period:.9f} d\nPhase reference {refined_epoch:.6f} BTJD\nFourier power {power[best]:.3f}\n3 d median removed from each product",va="top")
        edges=np.linspace(-.25,.75,81)
        mid=(edges[:-1]+edges[1:])/2
        for j,ax in enumerate(axes[1]):
            for sector,tsector,flux in chunks:
                phase=((tsector-refined_epoch)/period+.25)%1-.25
                indices=np.digitize(phase,edges)-1
                med=[np.median(flux[indices==i,j]) if (indices==i).sum()>=3 else np.nan
                     for i in range(len(mid))]
                ax.plot(mid,med,lw=1,alpha=.85,label=f"S{sector}")
            ax.set(xlabel="Phase",ylabel=("SAP (ppt)" if j==0 else "Corrected QLP (ppt)"),
                   xlim=(-.25,.75))
            ax.axvline(0,c=".5",ls="--",lw=.7)
        axes[1,1].legend(ncol=3,fontsize=6)
        fig.suptitle(f"TIC {tic} | candidate short-clock waveform by sector")
        fig.savefig(dest/f"{tic}-fold.png",dpi=105)
        plt.close(fig)
        summaries.setdefault(batch,[]).append(dict(tic=tic,period_d=period,dominant_d=dominant,
                                                  epoch_btjd=refined_epoch,ls_power=power[best],
                                                  sectors=len(chunks),channel=("SAP" if column==0 else "corrected")))
    for batch,rows in summaries.items():
        write_csv(base/f"batch{batch}"/"short-clocks.csv",rows)


if __name__=="__main__":
    main()
