"""Plot field-median losses on cameras 2, 3 and 4 across the three flagged exposures."""
import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import check


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("cache",type=Path)
    args=p.parse_args()
    check.EPOCHS=list(range(38475,38498))
    roster=pd.read_csv(check.HERE/"roster.csv")
    fields=roster[(roster.role=="field")&(roster.camera!=1)].to_dict("records")
    d=pd.DataFrame(r for star in fields for r in check.check(star,args.cache) if r["status"]=="measured")
    fig,axes=plt.subplots(3,1,figsize=(8.2,5.8),sharex=True,sharey=True,layout="constrained")
    for ax,(camera,epoch) in zip(axes,[(4,38482),(2,38490),(3,38491)]):
        sub=d[d.camera==camera]
        g=sub.groupby("cadenceno")
        for key,color,name,marker in [("corrected_loss_ppt","#aa3b49","QLP corrected","o"),
                                       ("sap_loss_ppt","#206a8a","Aperture flux","+")]:
            med=g[key].median().where(g.size()>=12)/10
            ax.scatter(med.index,med.to_numpy(),label=name,color=color,marker=marker,s=27)
        n=len(sub[sub.cadenceno==epoch])
        loss=sub.loc[sub.cadenceno==epoch,"corrected_loss_ppt"].median()/10
        ax.text(epoch,loss+1.1,f"{n} stars",ha="center",fontsize=9)
        ax.set_ylim(-2,18);ax.set_ylabel(f"Camera {camera}\nLight loss (%)")
        ax.axhline(0,color="#aaaaaa",lw=.5,zorder=0)
    axes[0].legend(frameon=False,loc="upper right",fontsize=8)
    axes[-1].set_xticks([38476,38480,38482,38486,38490,38491,38496],
                        ["38476","38480","38482","38486","38490","38491","38496"],rotation=30)
    axes[-1].set_xlabel("TESS exposure number (sector 26, half-hour cadence)")
    fig.suptitle("The apparent dips follow the camera across unrelated stars")
    fig.savefig(check.HERE/"camera-dips.png",dpi=150)
