"""Inspect active detector coverage in the TESScut sector list for TIC 120239458."""
import argparse
import csv
from pathlib import Path

from astropy.io import fits
from astropy.wcs import WCS
import matplotlib.pyplot as plt
import numpy as np

HERE=Path(__file__).resolve().parent


def main(cache):
    fig,axes=plt.subplots(1,3,figsize=(9,3.4),layout="constrained")
    rows=[]
    for ax,s in zip(axes,[16,56,83]):
        with fits.open(cache/f"120239458-{s}.fits") as h:
            t=h[1].data
            g=np.flatnonzero(t["QUALITY"]==0)
            stack=np.nanmedian(t["FLUX"][g[::max(1,len(g)//40)]],axis=0)
            w=WCS(h[2].header)
            x,y=w.world_to_pixel_values(335.4987751464,37.0402144428)
            i,j=int(round(float(x))),int(round(float(y)))
            center=float(stack[j,i])
            rows.append(dict(sector=s,center_x=float(x),center_y=float(y),center_rate=center,
                             max_3x3=float(np.nanmax(stack[j-1:j+2,i-1:i+2])),
                             field_max=float(np.nanmax(stack)),quality_zero_frames=len(g)))
            ax.imshow(np.arcsinh(stack/12),origin="lower",cmap="gray",vmin=0)
            ax.scatter(x,y,s=80,marker="o",facecolor="none",edgecolor="orange")
            ax.set(xticks=[],yticks=[],title=f"Sector {s}",xlabel=f"Center pixel {center:.1f} electrons/s")
    fig.suptitle("TIC 120239458 lies off the illuminated detector in sectors 56 and 83")
    fig.savefig(HERE/"120239458-sector-coverage.png",dpi=150)
    plt.close(fig)
    with (HERE/"120239458-sector-coverage.csv").open("w",newline="") as f:
        wr=csv.DictWriter(f,rows[0],lineterminator="\n")
        wr.writeheader()
        wr.writerows(rows)


if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cache",type=Path)
    main(ap.parse_args().cache)
