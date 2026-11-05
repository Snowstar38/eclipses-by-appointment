# T055 - TIC 417309915

Physical verdict: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

Selection: cross_method_dip, Gaia DR3 1995022621220079104, Gaia NSS SB1 period 58.5048634657712 d. This is a selection orbit, not a measured eclipse period.

## Raw evidence

The s24 selected dip overlaps the 1968.31957-1969.27791 BTJD interruption. Its quality-zero core SAP median 0.99538 matches the preceding 0.99408; the apparent dip was made by using the following brightening (post median 1.05563) as baseline. Target-centered s24 TESSCut 1x1 and 3x3 pixels independently show flat flux before the interruption and an enormous positive rise just afterward, peaking around 1970.7. There is no negative eclipse feature to time in the selected window.

## Coverage, timing and attribution

8 verified cached QLP sectors; coverage and retained-window numbers are in `initial-numerics.json` and `step-context.json`. `predicted-windows.json` lists actual cadence and sideband samples at Gaia-period and half-phase predictions; these are not clean nulls without raw context. Screening windows were predictions; no eclipse period, primary epoch or depth was measured. The brightening physics is unsettled; the selected dip is a baseline artifact. The pixel extraction is of the same TESS photons and not another observing occasion.

The shared catalogue matrix records four unavailable VizieR gates (VSX, ASAS-SN and Kostov 2025 tables 3/4). Exact nonmatches in available primary tables and Gaia do not establish novelty. The shared 120-arcsec Gaia neighbor cone is available in `../../shared-catalogues/gaia-neighbors.json`; no neighbor exclusion or Gaia-orbit geometry inference is needed to refute the selected non-eclipse feature.

Official TESSCut sector query: https://mast.stsci.edu/tesscut/api/v0.1/sector?ra=359.8873146380807&dec=56.88765626700866; newer sectors than cached QLP: []. Query response SHA-256: f4fa454a381569aa537f9f22a0924350615122307fb85207a9e08e3e6625efef.

## Limits and next check

If the brightenings matter independently, compare calibrated pixel background across spacecraft orbits.

## Sources

Bulk detector packet: `[local-path-redacted]` (SHA-256 deeef660c29dad4765665abaf8225720ae17a402c1eaf153aaa5ac859b915f43). Each QLP FITS path and verified SHA-256 is listed in `initial-numerics.json`. Plots: `raw-flags.png` and `raw-overview.png`. Scripts: `inspect_raw.py`, `check_steps.py`, `predicted_windows.py`, `current_sectors.py`, `write_reports.py`. The official cutout is independent pixel extraction of the same photons if used; it is not an independent observing occasion.

## Target-centered pixel check

`deciding-pixels.json` records the WCS position, positive target-pixel flux and cutout SHA-256. `deciding-pixels.png` shows 1x1, 3x3 and 5x5 raw cutout sums around the deciding window. Extraction and plot reproduce with `../inspect_deciders.py`.
