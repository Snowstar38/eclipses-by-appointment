"""Show all ten ground cutouts aligned on the original saved TESS screening epoch."""
import argparse
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from check import HERE, observations, np, pd, Path


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache",type=Path)
    args=parser.parse_args()
    fig,axes=plt.subplots(5,2,figsize=(10,11),layout="constrained")
    colors={"g":"#328966","V":"#7c5590","zg":"#e67721","zr":"#bb5549"}
    for ax,r in zip(axes.flat,pd.read_csv(HERE/"archived-clocks.csv").itertuples(),strict=True):
        half=.36*r.duration_d
        n=0
        for ids,t,y,_ in observations(r.tic,args.cache):
            dx=(t-r.epoch_btjd+.5*r.period_d)%r.period_d-.5*r.period_d
            mask=abs(dx)<=1
            ax.scatter(dx[mask],y[mask]*1000,s=9,color=colors[ids["band"]],alpha=.48,linewidths=0)
            n+=mask.sum()
        if n==0:
            ax.text(.5,.5,"No measurements in either archive",ha="center",transform=ax.transAxes,fontsize=9)
        ax.axvspan(-half,half,color="#bbbbbb",alpha=.30)
        ax.axhline(0,color="#444444",linewidth=.5)
        ax.set(xlim=(-1,1),ylim=(90,-70),title=f"TIC {r.tic}    {r.period_d:.4f} d")
    fig.suptitle("Ground photometry at the archived TESS folds\nASAS-SN g (green), V (purple), ZTF g (orange)   |   gray: tested eclipse core")
    fig.supxlabel("Days from predicted center")
    fig.supylabel("Millimagnitudes relative to object / camera median (fainter downward)")
    fig.savefig(HERE/"archived-predictions.png",dpi=135)
