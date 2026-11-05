# T054 - TIC 198279430

Physical verdict: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

Selection: cross_method_dip, Gaia DR3 1634905521999277952, Gaia NSS SB1 period 59.5634217888597 d. This is a selection orbit, not a measured eclipse period.

## Raw evidence

The s17 retained dip lies on a monotonic rising shoulder entering an interruption. Brightening flags in s84 near 3586 and 3599 BTJD coincide with SAP_BKG jumps -331.75 to 3790.5 and -407.07 to 5254.4 while SAP rises 0.99897 to 1.011 and 0.99838 to 1.0203. The extensive raw series contains background/step features, not a repeated eclipse morphology.

## Coverage, timing and attribution

42 verified cached QLP sectors; coverage and retained-window numbers are in `initial-numerics.json` and `step-context.json`. `predicted-windows.json` lists actual cadence and sideband samples at Gaia-period and half-phase predictions; these are not clean nulls without raw context. Screening windows were predictions; no eclipse period, primary epoch or depth was measured. Bright features can be variable or instrumental; the stated background correlation is positive contrary evidence for these retained eclipse flags, not a proof that the star has no intrinsic variability.

The shared catalogue matrix records four unavailable VizieR gates (VSX, ASAS-SN and Kostov 2025 tables 3/4). Exact nonmatches in available primary tables and Gaia do not establish novelty. The shared 120-arcsec Gaia neighbor cone is available in `../../shared-catalogues/gaia-neighbors.json`; no neighbor exclusion or Gaia-orbit geometry inference is needed to refute the selected non-eclipse feature.

Official TESSCut sector query: https://mast.stsci.edu/tesscut/api/v0.1/sector?ra=250.2428683517925&dec=64.36763152588395; newer sectors than cached QLP: []. Query response SHA-256: 342c8aaefbb8b2fff4520c548228fa11ee7ed3e9ea1d3b5e2f0df2946a7ef29e.

## Limits and next check

Revisit only with independently extracted stable-background pixel photometry.

## Sources

Bulk detector packet: `[local-path-redacted]` (SHA-256 17cb1e6777fc2ffd94c6d96e576cc001aabefc69b57b0177a636747826cc5a20). Each QLP FITS path and verified SHA-256 is listed in `initial-numerics.json`. Plots: `raw-flags.png` and `raw-overview.png`. Scripts: `inspect_raw.py`, `check_steps.py`, `predicted_windows.py`, `current_sectors.py`, `write_reports.py`. The official cutout is independent pixel extraction of the same photons if used; it is not an independent observing occasion.
