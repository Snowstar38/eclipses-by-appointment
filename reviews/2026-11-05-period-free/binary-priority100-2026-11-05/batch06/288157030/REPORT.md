# T051 - TIC 288157030

Physical verdict: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

Selection: cross_method_dip, Gaia DR3 2949877822014915200, Gaia NSS SB1 period 54.69522926315187 d. This is a selection orbit, not a measured eclipse period.

## Raw evidence

The retained s87 deficit is a downward discontinuity immediately after the 3676.44350-3676.65646 BTJD interruption, followed by gradual recovery rather than an ingress/egress pair. In adjacent quality-zero 0.2-d windows SAP falls 1.02010 to 0.97401 of the sector median while SAP_BKG rises 1727.65 to 6100.88. Earlier s6 and s33 show broad trends, not a same-kind recurring eclipse.

## Coverage, timing and attribution

3 verified cached QLP sectors; coverage and retained-window numbers are in `initial-numerics.json` and `step-context.json`. `predicted-windows.json` lists actual cadence and sideband samples at Gaia-period and half-phase predictions; these are not clean nulls without raw context. Screening windows were predictions; no eclipse period, primary epoch or depth was measured. The s87 step has no measured eclipse midpoint; its background response makes the selected flag instrumental. Current TESSCut footprint lists new s108/s109 coverage, not analyzed here because the selected feature is positively refuted.

The shared catalogue matrix records four unavailable VizieR gates (VSX, ASAS-SN and Kostov 2025 tables 3/4). Exact nonmatches in available primary tables and Gaia do not establish novelty. The shared 120-arcsec Gaia neighbor cone is available in `../../shared-catalogues/gaia-neighbors.json`; no neighbor exclusion or Gaia-orbit geometry inference is needed to refute the selected non-eclipse feature.

Official TESSCut sector query: https://mast.stsci.edu/tesscut/api/v0.1/sector?ra=98.32554731295198&dec=-16.694372990851953; newer sectors than cached QLP: [108, 109]. Query response SHA-256: 5a3afabded03a7f46e44405b1e85e1d34a3176ea99b1c63c4ae2195ad4a9f419.

## Limits and next check

Review s108/s109 raw target pixels if an independent future eclipse claim arises.

## Sources

Bulk detector packet: `[local-path-redacted]` (SHA-256 11538b9f5165e2614f05fb6a032a0779b95fe99c593494f9dd1abd55768a5871). Each QLP FITS path and verified SHA-256 is listed in `initial-numerics.json`. Plots: `raw-flags.png` and `raw-overview.png`. Scripts: `inspect_raw.py`, `check_steps.py`, `predicted_windows.py`, `current_sectors.py`, `write_reports.py`. The official cutout is independent pixel extraction of the same photons if used; it is not an independent observing occasion.
