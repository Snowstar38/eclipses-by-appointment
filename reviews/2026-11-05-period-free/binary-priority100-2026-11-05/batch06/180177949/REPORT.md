# T060 - TIC 180177949

Physical verdict: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

Selection: cross_method_dip, Gaia DR3 6054993358639322624, Gaia NSS SB2 period 39.99639231675146 d. This is a selection orbit, not a measured eclipse period.

## Raw evidence

Quality-zero raw SAP shows a persistent approximately 1.03-d sinusoidal wave in s11, s37, s64, s99, s100 and s101; independent per-sector frequency searches gave finite-grid peaks at 1.0323, 1.0334, 1.0315, 1.0316, 1.0305 and 1.0297 d. The retained broad dips and brightenings sample this wave, with no localized long-period eclipse shape.

## Coverage, timing and attribution

8 verified cached QLP sectors; coverage and retained-window numbers are in `initial-numerics.json` and `step-context.json`. `predicted-windows.json` lists actual cadence and sideband samples at Gaia-period and half-phase predictions; these are not clean nulls without raw context. Screening windows were predictions; no eclipse period, primary epoch or depth was measured. The short-period modulation is real but its physical mechanism and relation to the Gaia SB2 are not settled. The selected long-period eclipse flag is refuted, not all possible eclipses.

The shared catalogue matrix records four unavailable VizieR gates (VSX, ASAS-SN and Kostov 2025 tables 3/4). Exact nonmatches in available primary tables and Gaia do not establish novelty. The shared 120-arcsec Gaia neighbor cone is available in `../../shared-catalogues/gaia-neighbors.json`; no neighbor exclusion or Gaia-orbit geometry inference is needed to refute the selected non-eclipse feature.

Official TESSCut sector query: https://mast.stsci.edu/tesscut/api/v0.1/sector?ra=188.7697651307632&dec=-61.32530720030605; newer sectors than cached QLP: []. Query response SHA-256: 5e65c865714d170fdd7297817369a652ff0125216895819b9f616799d4bdc6d1.

## Limits and next check

Classify the short-period variable separately if of interest.

## Sources

Bulk detector packet: `[local-path-redacted]` (SHA-256 432a620b8c1726b558dad875066fafcf9b2d0e476fae99441c721225984c8a80). Each QLP FITS path and verified SHA-256 is listed in `initial-numerics.json`. Plots: `raw-flags.png` and `raw-overview.png`. Scripts: `inspect_raw.py`, `check_steps.py`, `predicted_windows.py`, `current_sectors.py`, `write_reports.py`. The official cutout is independent pixel extraction of the same photons if used; it is not an independent observing occasion.
