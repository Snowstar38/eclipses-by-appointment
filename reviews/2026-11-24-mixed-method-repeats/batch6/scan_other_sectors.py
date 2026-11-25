"""Find the strongest independent two-product dip windows per sector."""
import numpy as np

from review import HERE, ROOT, load, measure, read_csv, write_csv


def cumulative_windows(t, flux, width):
    edges = np.searchsorted(t, t[:, None] + width * np.array([-1.5, -.5, .5, 1.5]))
    sums = np.vstack([np.zeros((1, flux.shape[1])), np.cumsum(flux, axis=0)])
    counts = np.diff(edges)
    means = np.diff(sums[edges], axis=1) / np.maximum(1, counts[:, :, None])
    available = np.maximum(2, .65 * width / np.median(np.diff(t)))
    good = (counts >= available).all(axis=1)
    scores = np.min((means[:, 0] + means[:, 2])/2 - means[:, 1], axis=1)
    scores[~good] = -np.inf
    return scores


def main():
    data_root = ROOT / "sky/data/qlp-sb-p20-60"
    flags = {}
    guard_file = ROOT/"sky/mixed-fold-2026-11-24/cadence-controls/flagged-exposures.csv"
    for row in read_csv(guard_file):
        if row["screen_flag"] == "True":
            flags.setdefault((int(row["sector"]), int(row["camera"])), set()).add(int(row["cadenceno"]))
    rows = []
    for target in read_csv(HERE/"batch.csv"):
        tic = target["tic"]
        for path in sorted(data_root.glob(f"{tic}_s*.fits")):
            sector, camera, t, flux, guard = load(path, flags)
            for width in (.12, .24, .48, .96, 1.6):
                scores = cumulative_windows(t[~guard], flux[~guard], width)
                candidates = t[~guard]
                for rank in range(1, 4):
                    i = np.argmax(scores)
                    if not np.isfinite(scores[i]):
                        break
                    center = candidates[i]
                    result = measure(t, flux, guard, center, width)
                    rows.append(dict(tic=tic,sector=sector,camera=camera,width_d=width,
                                     rank=rank,center_btjd=center,score_ppt=scores[i],**result))
                    scores[abs(candidates-center)<width] = -np.inf
    write_csv(HERE/"independent-dip-scan.csv",rows)


if __name__ == "__main__":
    main()
