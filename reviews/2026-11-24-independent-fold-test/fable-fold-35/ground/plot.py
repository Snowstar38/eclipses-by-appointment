"""Plot each ground recovery at a period and phase determined from TESS."""
import argparse
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from test_clock import HERE, PALOMAR, Time, SkyCoord, np, pd, Path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache", type=Path)
    args = parser.parse_args()
    tests = pd.read_csv(HERE / "phase-checks.csv")
    passed = tests[tests.supports_tess_prediction]
    fig, axes = plt.subplots(4, 2, figsize=(10, 9), layout="constrained")
    for ax, (tic, group) in zip(axes.flat, passed.groupby("tic"), strict=True):
        best = group.sort_values(["cycles_in_core", "n_good"], ascending=False).iloc[0]
        raw = pd.read_csv(args.cache / f"{tic}.csv.gz")
        for band, color in [("zg", "#268557"), ("zr", "#964555")]:
            flux = raw[(raw.filtercode==band) & (raw.catflags==0) & (raw.magerr>0) & (raw.magerr<.2)]
            for _, g in flux.groupby("oid"):
                if len(g)<30:
                    continue
                t=Time(g.mjd.to_numpy()+g.exptime.to_numpy()/172800,format="mjd",scale="utc",location=PALOMAR)
                coord=SkyCoord(np.median(g.ra),np.median(g.dec),unit="deg")
                b=(t.tdb+t.light_travel_time(coord)).jd-2457000
                dx=(b-best.epoch_btjd+.5*best.period_d)%best.period_d-.5*best.period_d
                dy=g.mag.to_numpy()-np.median(g.mag)
                sel=abs(dx)<.7
                ax.scatter(dx[sel],dy[sel],s=6,alpha=.42,color=color,linewidths=0)
        ax.axvspan(-best.halfwidth_d,best.halfwidth_d,color="#888888",alpha=.14)
        ax.axhline(0,linewidth=.6,color="#333333")
        ax.set(xlim=(-.7,.7), ylim=(max(.16,2.3*best.depth_mag),-.075),
               title=f"TIC {tic}   |   {best.period_d:.4f} days")
    fig.suptitle("ZTF observations around the TESS-predicted eclipse\nGreen: g band   /   red: r band   /   shaded: tested eclipse core")
    fig.supxlabel("Days from the TESS prediction")
    fig.supylabel("Magnitude relative to each ZTF object's median (fainter downward)")
    fig.savefig(HERE/"recoveries.png", dpi=140)
