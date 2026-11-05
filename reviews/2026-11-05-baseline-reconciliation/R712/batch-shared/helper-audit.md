# Independent helper: pixel and numerical checks

Retrieved representative 11×11 TESSCut products and separately measured 1×1, 3×3, 5×5 aperture light curves for all five queue targets. Inputs, SHA-256 receipts, code, plots and outputs are in `helper-pixels/`. Core ±0.3 duration, sidebands 0.75–1.75 durations on each side; cadence quality zero and per-cadence background from the median of the 48 lowest pixels. These are independent reductions of the same TESS photons, not independent observations. Positive difference-centroid offsets are descriptive and not calibrated astrometric uncertainties. Subpixel localization is ambiguous.

| TIC | representative sector | aperture depths 1×1 / 3×3 / 5×5, ppt | Gaia 60″ count | capable neighbors at conservative tested depth |
|---|---:|---|---:|---:|
|257992903|8|41.95 / 44.15 / 43.52|60|2|
|70561926|8|16.31 / 15.94 / 15.13|24|0|
|380395732|13|27.57 / 22.35 / 16.96|47|2|
|188908998|56|18.30 / 17.98 / 17.01|15|2|
|280950412|11,64|3.53 / 0.87 / 1.12; 2.49 / 0.72 / 0.47|169|57 at assumed 1.2 ppt|

The last target has weak putative dips with centers supplied by the lead; these are not established event timings and the measurements are sensitive to baseline and aperture. Neighbor lists and intrinsic required eclipse fractions are in `helper-pixels/final-neighbors.json` and `helper-pixels/280950412/results.json`; they use Gaia G as a TESS-band flux proxy, assume full target and neighbor flux capture, and ignore other flux, so are not direct pixel fractional deficits or proof of contamination. The Gaia query and receipt are preserved. Non-Gaia and unresolved sources are not excluded. For 70561926 only the target Gaia source is within 2 arcsec; the 0.30 arcsec VSX EA position and similar clock support an association, with position epochs and period mismatch as caveats.

Independent weighted period/epoch fits and Gaia conjunction calculations reproduce the saved artifacts for four timed objects; see `helper-numeric-geometry-audit.json`. No fitted timing exists for 280950412. Current MAST QLP inventory receipt: `helper-pixels/mast-availability.json`; 188908998 has sectors 56, 83; 280950412 has sectors 10, 11, 37, 38, 64, 65, 99, 100. Product listing alone does not establish event coverage or a clean null.
