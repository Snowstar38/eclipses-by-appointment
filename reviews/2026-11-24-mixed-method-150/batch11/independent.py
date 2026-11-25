"""Independent sector diagnostics in SAP, corrected flux and QLP background."""
import argparse
from collections import defaultdict

import numpy as np
from astropy.io import fits
from astropy.timeseries import LombScargle
from scipy.ndimage import median_filter

from review import ROOT, read_csv, write_csv, load, measure


def cumulative_windows(t, flux, width, sign):
    edges = np.searchsorted(t, t[:, None] + width * np.array([-1.5, -.5, .5, 1.5]))
    terms = np.vstack([np.zeros((1, flux.shape[1])), np.cumsum(flux, axis=0)])
    n = np.diff(edges)
    means = np.diff(terms[edges], axis=1) / np.maximum(1, n[:, :, None])
    good = (n >= np.maximum(2, .60 * width / np.median(np.diff(t)))).all(axis=1)
    score = np.min(sign * ((means[:, 0] + means[:, 2])/2 - means[:, 1]), axis=1)
    score[~good] = -np.inf
    return score


def ancillary(path, centers, flagged):
    with fits.open(path) as hdus:
        header, data = hdus[0].header, hdus[1].data
        corrected = "KSPSAP_FLUX" if "KSPSAP_FLUX" in data.names else "DET_FLUX"
        t = data["TIME"]
        flagged = np.isin(data["CADENCENO"], list(flagged.get((header["SECTOR"],header["CAMERA"]),[])))
        quality = (data["QUALITY"] == 0) & ~flagged
        fields = ["SAP_FLUX", corrected, "SAP_BKG", "SAP_X", "SAP_Y"]
        flux = np.column_stack([data[name] for name in fields]).astype(float)
        m = np.isfinite(t) & np.isfinite(flux[:, :3]).all(axis=1) & quality
        order = np.argsort(t[m])
        t, flux = t[m][order], flux[m][order]
        out = []
        for row in centers:
            center, width = float(row["center"]), float(row["width"])
            dt = t-center
            near = abs(dt) < width*1.5
            core = abs(dt) <= width/2
            side = near & ~core
            if np.sum(core)<2 or np.sum(side)<4:
                continue
            med = np.median(flux[side],axis=0)
            change = np.median(flux[core],axis=0)-med
            mad = 1.4826*np.median(abs(flux[side]-med),axis=0)
            corr = np.corrcoef(flux[near,:3].T)
            out.append(dict(tic=row["tic"],sensor=header["CCD"],sector=row["sector"],camera=row["camera"],
                            center=center,width=width,archive_flag=row["archive_flag"],
                            sap_ppt=row["sap_ppt"],corrected_ppt=row["corrected_ppt"],bkg_change=change[2],
                            bkg_side_mad=mad[2],x_change=change[3],y_change=change[4],
                            r_sap_bkg=corr[0,2],r_corrected_bkg=corr[1,2]))
        return out


def run(batch, root):
    data_root = root/"sky/data/qlp-sb-p20-60"
    guards = defaultdict(set)
    for row in read_csv(root/"sky/mixed-fold-2026-11-24/cadence-controls/flagged-exposures.csv"):
        if row["screen_flag"] == "True":
            guards[(int(row["sector"]),int(row["camera"]))].add(int(row["cadenceno"]))
    archive = defaultdict(list)
    for row in read_csv(batch/"archive-windows.csv"):
        archive[row["tic"],int(row["sector"])].append(row)
    spectra, candidates, background = [], [], []
    frequencies = np.linspace(.2, 22, 14000)
    for target in read_csv(batch/"batch.csv"):
        tic = target["tic"]
        sign = -1 if target["priority_group"] == "brightening_lead" else 1
        for path in sorted(data_root.glob(f"{tic}_s*.fits")):
            sector, camera, t, flux, guard = load(path,guards)
            if len(t)<25:
                continue
            ts, fs = t[~guard],flux[~guard]
            dt = np.median(np.diff(ts))
            corrected = fs[:,1] - median_filter(fs[:,1], size=max(3,(int(2/dt)//2)*2+1))
            pows = LombScargle(ts, corrected).power(frequencies)
            i = np.nanargmax(pows)
            spectra.append(dict(tic=tic,sector=sector,period_d=1/frequencies[i],power=pows[i]))
            for width in (.06,.12,.24,.48,.96,1.6):
                score = cumulative_windows(ts,fs,width,sign)
                for k in range(1,3):
                    i = np.argmax(score)
                    if not np.isfinite(score[i]):
                        break
                    row = dict(tic=tic,sector=sector,camera=camera,center=ts[i],width=width,rank=k,
                               signed_score=score[i],**measure(t,flux,guard,ts[i],width))
                    candidates.append(row)
                    score[abs(ts-ts[i])<width] = -np.inf
            background += ancillary(path,archive[tic,sector],guards)
    write_csv(batch/"periodograms.csv",spectra)
    write_csv(batch/"independent-scan.csv",candidates)
    write_csv(batch/"background.csv",background)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch",type=__import__("pathlib").Path,required=True)
    parser.add_argument("--root",type=__import__("pathlib").Path,default=ROOT)
    args = parser.parse_args()
    run(args.batch,args.root)
