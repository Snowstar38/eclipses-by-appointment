"""Measure the short repeat in TIC 170337570 and check variable-star clocks."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from astropy.timeseries import BoxLeastSquares, LombScargle
from scipy.ndimage import median_filter
from scipy.optimize import least_squares

from review import HERE, ROOT, load, read_csv, measure, write_csv


def main():
    data = ROOT / "sky/data/qlp-sb-p20-60"
    rows = []
    for target in read_csv(HERE / "batch.csv"):
        tic = target["tic"]
        all_t, all_f = [], []
        for path in sorted(data.glob(f"{tic}_s*.fits")):
            sector, _, t, flux, _ = load(path, {})
            cadence = np.median(np.diff(t))
            corrected = flux[:, 1]
            detrended = corrected - median_filter(corrected, size=max(3, (int(2/cadence)//2)*2+1))
            power = LombScargle(t, detrended)
            frequency = np.linspace(.2, 17, 9000)
            values = power.power(frequency)
            best = np.argmax(values)
            rows.append(dict(tic=tic, sector=sector, period_d=1/frequency[best], power=values[best]))
            all_t.extend(t)
            all_f.extend(detrended)
        if tic != "170337570":
            continue
        t, f = np.asarray(all_t), np.asarray(all_f)
        bls = BoxLeastSquares(t, f)
        p = np.linspace(.865, .874, 30001)
        z = bls.power(p, [.035,.05,.065], objective="likelihood", oversample=10)
        best = np.argsort(z.power)[-1]
        print("Global BLS", p[best], z.transit_time[best], z.duration[best])
        fig, axs = plt.subplots(2, 1, figsize=(11, 6), layout="constrained")
        axs[0].plot(p, z.power)
        axs[0].set(xlabel="Period (days)", ylabel="BLS likelihood")
        period, epoch = p[best], z.transit_time[best]
        event_rows, times, cycles = [], [], []
        for path in sorted(data.glob(f"{tic}_s*.fits")):
            sector, _, t, flux, guard = load(path, {})
            c = np.arange(int(np.ceil((t.min()-epoch)/period)), int(np.floor((t.max()-epoch)/period))+1)
            for cycle in c:
                center = epoch + period*cycle
                offsets = np.arange(-.042, .043, .003)
                trials = [measure(t, flux, guard, center+x, .05) for x in offsets]
                scores = [r["corrected_ppt"] if r["fraction"] >= .65 and min(r["left_n"],r["right_n"]) >= 2
                          and np.isfinite(r["corrected_ppt"]) else -np.inf for r in trials]
                j = np.argmax(scores)
                if np.isfinite(scores[j]) and scores[j] > 3.5 and trials[j]["sap_ppt"] > 2.5:
                    times.append(center+offsets[j])
                    cycles.append(cycle)
                    event_rows.append(dict(sector=sector, cycle=cycle, center=center+offsets[j], **trials[j]))
            near = ((t-epoch)/period + .5) % 1 - .5
            axs[1].scatter(near*period, flux[:, 1], s=1, alpha=.14, label=f"S{sector}")
        fit = least_squares(lambda pars: pars[0]+pars[1]*np.array(cycles)-times, (epoch,period),loss="soft_l1",f_scale=.008)
        print("Robust fit from centers",fit.x)
        fit_epoch, fit_period = fit.x
        for r in event_rows:
            r["fit_residual_d"] = r["center"] - fit_epoch - fit_period*r["cycle"]
        for sector in sorted(set(r["sector"] for r in event_rows)):
            events = [r for r in event_rows if r["sector"]==sector]
            print(sector,len(events),np.median([r["fit_residual_d"] for r in events]),
                  [round(float(np.median([r["corrected_ppt"] for r in events if r["cycle"]%2 == parity])),2)
                   for parity in (0,1)])
        axs[1].set(xlabel="Days from short-clock center", ylabel="Corrected flux (ppt)",xlim=(-.2,.2),ylim=(-20,8))
        axs[1].legend(ncol=6)
        fig.savefig(HERE / "170337570-short-clock.png",dpi=130)
        plt.close(fig)
        write_csv(HERE / "170337570-event-centers.csv", event_rows)
    write_csv(HERE / "short-variability.csv", rows)


if __name__ == "__main__":
    main()
