"""Look for the TESS eclipse at fixed phase in resolved ZTF photometry of TIC 257808672."""
import argparse
import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import least_squares

from sampling import HERE, observations

PERIOD=3.19798973
EPOCH=2802.5393100


def design(phase):
    return np.column_stack([np.ones(len(phase)),np.sin(2*np.pi*phase),np.cos(2*np.pi*phase),
                            np.sin(4*np.pi*phase),np.cos(4*np.pi*phase)])


def main(cache):
    rng=np.random.default_rng(257808672)
    fig,axes=plt.subplots(1,2,figsize=(10,4.5),layout="constrained",sharey=True)
    cuts=[]
    for ax,band,color in zip(axes,["zg","zr"],["#26766c","#ab5136"]):
        phs,values,cycles=[],[],[]
        for info,t,y,err in observations("257808672",cache):
            if info["survey"]!="ZTF" or info["band"]!=band:
                continue
            phase=((t-EPOCH)/PERIOD+.25)%1-.25
            for block in np.unique(np.floor(t/150)):
                sl=np.floor(t/150)==block
                baseline=sl & (abs(phase)>.075) & (abs(phase-.5)>.075)
                if baseline.sum()<15 or len(np.unique(np.floor(phase[baseline]*10)))<5:
                    continue
                a=design(phase[baseline])
                coef=least_squares(lambda c:(a@c-y[baseline])/np.maximum(err[baseline],.015),
                                   np.zeros(5),loss="soft_l1").x
                phs.extend(phase[sl])
                values.extend((y[sl]-design(phase[sl])@coef)*1000)
                cycles.extend(np.floor((t[sl]-EPOCH)/PERIOD+.25).astype(int))
        ph,y,n=map(np.array,(phs,values,cycles))
        ax.scatter(ph,y,color=color,alpha=.24,s=7)
        edges=np.linspace(-.25,.75,51)
        bins=np.digitize(ph,edges)
        med=[np.median(y[bins==i]) if np.sum(bins==i)>=3 else np.nan for i in range(1,len(edges))]
        ax.plot((edges[1:]+edges[:-1])/2,med,color=color,lw=1.8)
        ax.axhline(0,color="gray",lw=.7)
        for center,label in [(0,"primary"),(.5,"secondary")]:
            sel=abs(ph-center)<.022
            by_cycle=np.array([np.median(y[sel&(n==cycle)]) for cycle in np.unique(n[sel])])
            if len(by_cycle)==0:
                continue
            lo,hi=np.quantile(np.median(rng.choice(by_cycle,size=(5000,len(by_cycle)),replace=True),axis=1),[.025,.975])
            cuts.append(dict(tic="257808672",band=band,event=label,points=len(ph),in_core=int(sel.sum()),cycles=len(by_cycle),
                             core_loss_mmag=np.median(by_cycle),bootstrap_lo=lo,bootstrap_hi=hi))
            ax.axvspan(center-.022,center+.022,color=color,alpha=.09)
        ax.set(title="ZTF "+band[-1]+" band",xlabel="Phase from the TESS primary",xlim=(-.25,.75),ylim=(525,-90))
    axes[0].set_ylabel("Residual magnitude (mmag)")
    fig.suptitle("Light from the resolved neighbor, TIC 257808672\nBroad modulation fitted outside the two TESS eclipse windows")
    fig.savefig(HERE/"257808672-ztf.png",dpi=150)
    plt.close(fig)
    with (HERE/"257808672-ztf.csv").open("w",newline="") as f:
        wr=csv.DictWriter(f,cuts[0],lineterminator="\n")
        wr.writeheader()
        wr.writerows(cuts)


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache",type=Path)
    main(parser.parse_args().cache)
