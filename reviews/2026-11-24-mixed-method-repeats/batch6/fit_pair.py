"""Fit eclipse-like shapes in the overlapping S81 apertures."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import least_squares
from review import HERE, ROOT, load, write_csv


def fit(t, flux, guess, narrow=False):
    around = abs(t - guess) < 1.1
    u, y = t[around]-guess, flux[around]

    def residual(pars):
        offset, slope, depth, center, flat, wing = pars
        occulted = np.clip((flat+wing-abs(u-center))/wing,0,1)
        return offset+slope*u-depth*occulted-y

    init = (0, 0, 60, 0, .06, .055) if narrow else (0, 0, 120, 0, .16, .22)
    lo = (-50, -50, 1, -.2, .005, .005)
    hi = (50, 50, 500, .2, .42, .5)
    sol = least_squares(residual, init, bounds=(lo,hi),loss="soft_l1",f_scale=3)
    offset, slope, depth, center, flat, wing = sol.x
    return guess+center, depth, 2*flat, 2*(flat+wing), sol.x


def main():
    directory = ROOT/"sky/data/qlp-sb-p20-60"
    apertures = ("212431508", "212431520")
    guesses = (3512.52, 3532.14)
    rows = []
    fig, axes = plt.subplots(2, 2, figsize=(11, 6), layout="constrained")
    for i, tic in enumerate(apertures):
        _, _, t, flux, _ = load(directory/f"{tic}_s081.fits", {})
        for j, guess in enumerate(guesses):
            center, depth, flat, width, fit_parameters = fit(t, flux[:, 0], guess, narrow=j==1)
            rows.append(dict(tic=tic, sector=81, event=j+1, center_btjd=center,
                             peak_depth_ppt=depth, flat_width_d=flat, total_width_d=width))
            ax = axes[i,j]
            span = .8 if j == 0 else .4
            keep = abs(t-center) < span
            ax.scatter(t[keep]-center, flux[keep,0], c="tab:blue", s=5, alpha=.6, label="SAP")
            ax.scatter(t[keep]-center, flux[keep,1], c=".25", s=5, alpha=.5, label="Corrected")
            offset, slope, _, _, half_flat, wing = fit_parameters
            x = np.linspace(-span,span,400)
            occulted = np.clip((half_flat+wing-abs(x))/wing,0,1)
            ax.plot(x,offset+slope*(x+center-guess)-depth*occulted,c="tab:red",lw=1,label="SAP trapezoid")
            ax.set(title=f"TIC {tic}  |  {center:.5f} BTJD", xlabel="Days from fitted center",
                   ylabel="Flux (ppt)", xlim=(-span,span))
    axes[0,0].legend(loc="lower left")
    fig.suptitle("S81 | The same unequal eclipses appear in two overlapping QLP apertures")
    fig.savefig(HERE/"212431508-212431520-eclipse-pair.png",dpi=125)
    plt.close(fig)
    write_csv(HERE/"212431508-shape-fits.csv",rows)


if __name__=="__main__":
    main()
