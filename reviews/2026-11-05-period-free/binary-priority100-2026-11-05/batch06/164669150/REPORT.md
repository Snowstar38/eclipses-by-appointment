# T058 - TIC 164669150

Physical verdict: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

Selection: cross_method_dip, Gaia DR3 2107357456480717056, Gaia NSS SB1 period 49.82288947113167 d. This is a selection orbit, not a measured eclipse period.

## Raw evidence

Retained s53/s55/s74/s75/s80/s82 dips and brightenings repeatedly straddle interruptions with discontinuous SAP steps. The s53 and s55 apparent dips occur after 0.92-d gaps on a smooth broad ramp; s74/s75/s80 show step changes across 0.21-d orbit gaps and broad post-gap brightenings. They are not bounded eclipse ingress/egress pairs.

## Coverage, timing and attribution

12 verified cached QLP sectors; coverage and retained-window numbers are in `initial-numerics.json` and `step-context.json`. `predicted-windows.json` lists actual cadence and sideband samples at Gaia-period and half-phase predictions; these are not clean nulls without raw context. Screening windows were predictions; no eclipse period, primary epoch or depth was measured. Multiple sectors make the gap pattern recur, but they do not supply repeated same-kind eclipses. Background and baseline behavior leave the origin of broad variability open.

The shared catalogue matrix records four unavailable VizieR gates (VSX, ASAS-SN and Kostov 2025 tables 3/4). Exact nonmatches in available primary tables and Gaia do not establish novelty. The shared 120-arcsec Gaia neighbor cone is available in `../../shared-catalogues/gaia-neighbors.json`; no neighbor exclusion or Gaia-orbit geometry inference is needed to refute the selected non-eclipse feature.

Official TESSCut sector query: https://mast.stsci.edu/tesscut/api/v0.1/sector?ra=284.10563454391024&dec=46.64517310754861; newer sectors than cached QLP: []. Query response SHA-256: 44d726fb42467a4e7f0c1047f16cd68681a5a0794073e977321ab9462ea22d3f.

## Limits and next check

Inspect independent target-pixel photometry only if a stable eclipse ephemeris emerges.

## Sources

Bulk detector packet: `[local-path-redacted]` (SHA-256 56a2b9a6074f5227ee3bd5a8aff18cc6e83d68062cf713c76a0bfd3504f3bc5f). Each QLP FITS path and verified SHA-256 is listed in `initial-numerics.json`. Plots: `raw-flags.png` and `raw-overview.png`. Scripts: `inspect_raw.py`, `check_steps.py`, `predicted_windows.py`, `current_sectors.py`, `write_reports.py`. The official cutout is independent pixel extraction of the same photons if used; it is not an independent observing occasion.
