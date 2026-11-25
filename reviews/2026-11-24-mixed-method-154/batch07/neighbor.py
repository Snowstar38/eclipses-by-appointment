"""Measure both fixed eclipse families in the neighbor's TESSCut pixel profile."""
import argparse
import csv
import sys
from pathlib import Path

from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"followup"))
from scene import fit_scene, gaia_field, locate

TIC = "257808668"
TARGET = "1786928913098117504"
NEIGHBOR = "1786928913098116864"
PERIOD = 3.1979897310877785
EPOCH = 2802.539310015015
WIDTH = .17026473


def save(path, rows):
    with path.open("w", newline="", encoding="utf-8") as stream:
        out = csv.DictWriter(stream, list(rows[0]))
        out.writeheader()
        out.writerows(rows)


def fourier(phase):
    return np.column_stack((np.ones(len(phase)), *(f(phase*2*np.pi*k)
                           for k in (1, 2) for f in (np.cos, np.sin))))


def run(cache):
    windows, folded, scores = [], [], []
    for sector in (55, 82):
        with fits.open(cache/f"{TIC}-{sector}.fits") as h:
            d = h[1].data
            clean = (d["QUALITY"] == 0) & np.isfinite(d["TIME"])
            t, cube = np.array(d["TIME"][clean]), np.array(d["FLUX"][clean], dtype=float)
            wcs = WCS(h[2].header)
        frame = np.nanmedian(cube, axis=0)
        x, y, rel, ids, index = gaia_field(dict(tic=TIC,gaia_dr3=TARGET,btjd=np.median(t)),wcs,frame.shape)
        sigma, dx, dy = fit_scene(frame,x,y,rel)
        x, y = x+dx, y+dy
        keep = (rel > .015*max(rel)) | (ids == TARGET) | (ids == NEIGHBOR)
        x, y, ids = x[keep], y[keep], ids[keep]
        ti, = np.flatnonzero(ids == TARGET)
        ni, = np.flatnonzero(ids == NEIGHBOR)
        scale = 3600*np.sqrt(abs(np.linalg.det(wcs.pixel_scale_matrix)))
        yy, xx = np.indices(frame.shape)
        use = np.all(np.isfinite(cube), axis=0)
        stars = np.exp(-.5*((xx[use,None]-x)**2+(yy[use,None]-y)**2)/sigma**2)
        frame_grad = np.gradient(frame)
        backgrounds = np.column_stack((np.ones(use.sum()), xx[use], yy[use]))
        design = np.column_stack((stars, backgrounds, *(g[use] for g in frame_grad)))

        differences = (cube[:,use]-frame[use])@np.linalg.pinv(design).T
        # Keep signed detector flux. The quiescent neighbor flux is not stable in this blended static scene.
        photo = differences[:,[ti,ni]]
        phase = ((t-EPOCH)/PERIOD+.5)%1-.5
        out_event = (abs(phase)>.085)&(abs(phase)<.415)
        primary_core = abs(phase)<WIDTH/(2*PERIOD)
        secondary_core = (.5-abs(phase))<WIDTH/(2*PERIOD)
        matrix = fourier(phase)
        smooth = matrix@np.linalg.lstsq(matrix[out_event],photo[out_event,1],rcond=None)[0]
        for label, vals in (("outside_dips",out_event),("primary_core",primary_core),
                            ("secondary_core",secondary_core)):
            scores.append(dict(sector=sector,sample=label,n=int(vals.sum()),
                               fourier_residual_median_rate=float(np.median(photo[vals,1]-smooth[vals])),
                               fourier_residual_mad_rate=float(1.4826*np.median(abs(
                                  (photo[vals,1]-smooth[vals])-np.median(photo[vals,1]-smooth[vals]))))))
        for left in np.linspace(-.5,.49,100):
            use_bin = (phase>=left)&(phase<left+.01)
            if use_bin.any():
                target, neighbor = np.median(photo[use_bin],axis=0)
                folded.append(dict(sector=sector,phase=left+.005,target_rate=target,neighbor_rate=neighbor,
                                   smooth_neighbor_rate=float(np.median(smooth[use_bin]))))
        step = np.median(np.diff(t))
        for kind, phase_zero in (("primary",0),("secondary",.5)):
            for k in np.arange(np.ceil((min(t)-EPOCH)/PERIOD-phase_zero),
                               np.floor((max(t)-EPOCH)/PERIOD-phase_zero)+1,dtype=int):
                center = EPOCH+(k+phase_zero)*PERIOD
                dt = (t-center)/WIDTH
                masks = [((dt>=-2)&(dt<=-1)),abs(dt)<.35,((dt>=1)&(dt<=2))]
                if any(mask.sum()<max(2,.6*WIDTH*f/step) for mask,f in zip(masks,[1,.7,1])):
                    continue
                l, i, r = (np.nanmedian(cube[m],axis=0) for m in masks)
                diff = (l+r)/2-i
                cx,cy = locate(diff,sigma)
                l1, i1, r1 = (np.median(photo[m],axis=0) for m in masks)
                delta = (l1+r1)/2 - i1
                windows.append(dict(sector=sector,kind=kind,cycle=k,center_btjd=center,
                                    target_depth_rate=delta[0],neighbor_depth_rate=delta[1],
                                    image_target_offset_as=np.hypot(x[ti]-cx,y[ti]-cy)*scale,
                                    image_neighbor_offset_as=np.hypot(x[ni]-cx,y[ni]-cy)*scale,
                                    core_points=int(masks[1].sum())))
    save(HERE/"neighbor-windows.csv",windows)
    save(HERE/"neighbor-fold.csv",folded)
    save(HERE/"neighbor-harmonic-check.csv",scores)
    fig, axes = plt.subplots(2, 1, figsize=(9,6),sharex=True)
    for sector, ax in zip((55,82),axes):
        sample = [r for r in folded if r["sector"]==sector]
        for field, label, c in (("neighbor_rate","neighbor","#172f68"),
                                ("target_rate","nominated target","#b3851e"),
                                ("smooth_neighbor_rate","out-of-dip Fourier fit","#6a6a6a")):
            ax.plot([r["phase"] for r in sample],[r[field] for r in sample],label=label,c=c,lw=1.3)
        ax.set(ylabel=f"S{sector} (e⁻/s)")
        ax.legend(fontsize=8)
    axes[-1].set_xlabel("Phase relative to primary minimum")
    fig.suptitle("TIC 257808668 cutouts | separated flux profiles")
    fig.tight_layout()
    fig.savefig(HERE/"plots"/"257808668-neighbor-fold.png",dpi=120)
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache",type=Path)
    run(parser.parse_args().cache)


