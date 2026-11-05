# T056 - TIC 51255152

Physical verdict: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

Selection: cross_method_dip, Gaia DR3 5753754832168478976, Gaia NSS SB1 period 35.555561613999686 d. This is a selection orbit, not a measured eclipse period.

## Raw evidence

The two s99 retained dip windows at 4051.87 and 4068.53 BTJD sample very large, slowly changing raw flux excursions. At the latter, pre/core/post quality-zero QLP SAP medians are 0.971/0.859/0.855. Target-centered TESSCut pixels independently show a slow decline before the 4067.19-4067.41 spacecraft gap, a downward step across it, then a broad rise after 4071 into much stronger brightening. The dip window is the low plateau of this step/ramp sequence, with no localized ingress or egress.

## Coverage, timing and attribution

5 verified cached QLP sectors; coverage and retained-window numbers are in `initial-numerics.json` and `step-context.json`. `predicted-windows.json` lists actual cadence and sideband samples at Gaia-period and half-phase predictions; these are not clean nulls without raw context. Screening windows were predictions; no eclipse period, primary epoch or depth was measured. The selected s99 deficit is not a localized eclipse; strong variability or extraction instability deserves separate investigation. The TESSCut extraction is of the same photons.

The shared catalogue matrix records four unavailable VizieR gates (VSX, ASAS-SN and Kostov 2025 tables 3/4). Exact nonmatches in available primary tables and Gaia do not establish novelty. The shared 120-arcsec Gaia neighbor cone is available in `../../shared-catalogues/gaia-neighbors.json`; no neighbor exclusion or Gaia-orbit geometry inference is needed to refute the selected non-eclipse feature.

Official TESSCut sector query: https://mast.stsci.edu/tesscut/api/v0.1/sector?ra=128.50628283033708&dec=-8.13219430194474; newer sectors than cached QLP: []. Query response SHA-256: 1804cb085bd42477664fadab0b15ca0ef18225019adc7f46a320c56e715eec57.

## Limits and next check

Use calibrated independent aperture photometry if seeking the origin of the large excursions.

## Sources

Bulk detector packet: `[local-path-redacted]` (SHA-256 f4670c19cc91f8ebc62905c4e6c91ef630b5c335c34ec84386b5be5014fb6b60). Each QLP FITS path and verified SHA-256 is listed in `initial-numerics.json`. Plots: `raw-flags.png` and `raw-overview.png`. Scripts: `inspect_raw.py`, `check_steps.py`, `predicted_windows.py`, `current_sectors.py`, `write_reports.py`. The official cutout is independent pixel extraction of the same photons if used; it is not an independent observing occasion.

## Target-centered pixel check

`deciding-pixels.json` records the WCS position, positive target-pixel flux and cutout SHA-256. `deciding-pixels.png` shows 1x1, 3x3 and 5x5 raw cutout sums around the deciding window. Extraction and plot reproduce with `../inspect_deciders.py`.
