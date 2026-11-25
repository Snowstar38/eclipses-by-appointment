"""Compare batch 6 events to same-exposure QLP camera controls."""
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits

from review import HERE, ROOT, read_csv, write_csv, measure

FIELDS = ("SAP_FLUX", "SAP_BKG", "SAP_X", "SAP_Y")


def product(path, cameras):
    with fits.open(path) as source:
        header = source[0].header
        camera = header["CAMERA"]
        if camera not in cameras:
            return None
        data = source[1].data
        corrected = "KSPSAP_FLUX" if "KSPSAP_FLUX" in data.names else "DET_FLUX"
        good = (data["QUALITY"] == 0) & np.isfinite(data["TIME"])
        good &= np.isfinite(data["SAP_FLUX"]) & np.isfinite(data[corrected])
        names = (FIELDS[0], corrected, *FIELDS[1:])
        flux = np.column_stack([data[name] for name in names]).astype(float)[good]
        order = np.argsort(data["CADENCENO"][good])
        cadence = float(source[1].header["TIMEDEL"])
        return camera, header["CCD"], data["TIME"][good][order], data["CADENCENO"][good][order], flux[order], cadence


def control_metrics(cad, flux, cadence, center_cad, width):
    dt = (cad - center_cad) * cadence
    core = abs(dt) <= width/2
    left = (dt >= -1.5*width) & (dt < -width/2)
    right = (dt <= 1.5*width) & (dt > width/2)
    fraction = min(1., core.sum()*cadence/width)
    if min(core.sum(), left.sum(), right.sum()) < 2:
        return fraction, [np.nan]*5
    left_med = np.nanmedian(flux[left], axis=0)
    right_med = np.nanmedian(flux[right], axis=0)
    t_left, t_right = np.median(dt[left]), np.median(dt[right])
    baseline = left_med + (right_med-left_med) * ((dt[:, None]-t_left)/(t_right-t_left))
    change = -np.nanmedian((flux-baseline)[core], axis=0)
    change[:2] *= 1000 / ((left_med[:2]+right_med[:2])/2)
    return fraction, change


def main():
    data_root = ROOT / "sky/data/qlp-sb-p20-60"
    by_sector = defaultdict(list)
    for row in read_csv(HERE/"archive-windows.csv"):
        if row["archive_flag"] == "True":
            by_sector[int(row["sector"])].append(row)
    for row in read_csv(HERE/"control-events.csv"):
        by_sector[int(row["sector"])].append(row)
    rows = []
    for sector, events in by_sector.items():
        cameras = {int(e["camera"]) for e in events}
        controls = {}
        for path in sorted(data_root.glob(f"*_s{sector:03}.fits")):
            array = product(path, cameras)
            if array is not None:
                controls[path.stem.split("_")[0]] = array
        for j, row in enumerate(events):
            tic = row["tic"]
            center, width = float(row["center"]), float(row["width"])
            camera, ccd, t, cad, flux, local_cadence = controls[tic]
            center_cad = np.interp(center, t, cad)
            assert camera == int(row["camera"])
            fig, axes = plt.subplots(2, 1, figsize=(9, 5), layout="constrained")
            target_result = None
            for other, (other_cam, other_ccd, _, number, values, cadence) in controls.items():
                if other_cam != camera:
                    continue
                fraction, changes = control_metrics(number, values, cadence, center_cad, width)
                values_out = dict(zip(("sap_ppt","corrected_ppt","bkg_native","x_pixel","y_pixel"),changes))
                result = dict(tic=tic,sector=sector,camera=camera,target_ccd=ccd,center_btjd=center,
                              center_cadence=center_cad,width_d=width,control_tic=other,
                              control_ccd=other_ccd,fraction=fraction,**values_out)
                rows.append(result)
                dt = (number - center_cad) * cadence
                near = np.where(abs(dt) <= 2*width)[0]
                if not near.size:
                    continue
                vals = values[near]
                if other != tic:
                    if other_ccd == ccd:
                        relative = vals[:, 0] / np.median(vals[:, 0])
                        axes[0].plot(dt[near], 1000*(relative-1), c=".65", lw=.6, alpha=.4)
                    continue
                target_result = (dt[near], vals)
            if target_result is not None:
                dt, vals = target_result
                for k, color in enumerate(("tab:blue","black")):
                    axes[0].scatter(dt, 1000*(vals[:,k]/np.median(vals[:,k])-1), color=color, s=8)
                axes[1].scatter(dt, vals[:,2]-np.nanmedian(vals[:,2]), color="tab:orange", s=8)
            for ax in axes:
                ax.axvspan(-width/2, width/2, alpha=.2, color="tab:orange")
                ax.set_xlim(-2*width,2*width)
            axes[0].set(ylabel="Relative flux (ppt)",title="Blue SAP, black corrected, gray same-CCD SAP controls")
            axes[1].set(ylabel="SAP_BKG change in native units", xlabel="Days from matched exposure")
            fig.suptitle(f"TIC {tic}  S{sector} camera {camera} CCD {ccd}  {center:.5f} BTJD")
            fig.savefig(HERE/f"{tic}-s{sector:03}-control-{j}.png",dpi=90)
            plt.close(fig)
    write_csv(HERE/"camera-controls.csv", rows)


if __name__ == "__main__":
    main()
