# T059 - TIC 405542204

Physical verdict: **PLAUSIBLE**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

Selection: cross_method_dip, Gaia DR3 1353525240727718016, Gaia NSS SB1 period 32.727654091525295 d. This is a selection orbit, not a measured eclipse period.

## Raw evidence

The s25/s26 QLP SAP windows contain low-amplitude multi-day depressions, and the s25 5x5 TESSCut pixel series confirms broad structure with a deeper decline near the sector end around 2009 BTJD. The s25 retained 2006.41 window lies on a smooth declining shoulder; s26 has two broad 2015/2028 windows with different shapes. These are not measured eclipse centers, but the independent target-centered extraction prevents dismissing the s25 depression as a QLP-only false positive. The s79 bright flag is a separate brief spike.

## Coverage, timing and attribution

6 verified cached QLP sectors; coverage and retained-window numbers are in `initial-numerics.json` and `step-context.json`. `predicted-windows.json` lists actual cadence and sideband samples at Gaia-period and half-phase predictions; these are not clean nulls without raw context. Screening windows were predictions; no eclipse period, primary epoch or depth was measured. A long eclipse remains possible. No complete same-kind repeated ingress/egress pair, secure cycle count, source attribution or geometry has been established; the raw pixel extraction shares TESS photons.

The shared catalogue matrix records four unavailable VizieR gates (VSX, ASAS-SN and Kostov 2025 tables 3/4). Exact nonmatches in available primary tables and Gaia do not establish novelty. The shared 120-arcsec Gaia neighbor cone is in `../../shared-catalogues/gaia-neighbors.json`; source attribution and orbital geometry remain unresolved.

Official TESSCut sector query: https://mast.stsci.edu/tesscut/api/v0.1/sector?ra=256.82000732240635&dec=40.053531927939915; newer sectors than cached QLP: []. Query response SHA-256: 828fdba029fc09fa25e5664f8ae225455eb1b6b6f77fd1c4e683580d240103cc.

## Limits and next check

Obtain calibrated target-centered pixel photometry across the s25/s26 boundary and a future predicted interval to establish whether a localized eclipse repeats.

## Sources

Bulk detector packet: `[local-path-redacted]` (SHA-256 2e8e5c6163e987d18295206759382eeaac192079cf1788ab7d3dd5b8b0f118d8). Each QLP FITS path and verified SHA-256 is listed in `initial-numerics.json`. Plots: `raw-flags.png` and `raw-overview.png`. Scripts: `inspect_raw.py`, `check_steps.py`, `predicted_windows.py`, `current_sectors.py`, `write_reports.py`. The official cutout is independent pixel extraction of the same photons if used; it is not an independent observing occasion.

## Target-centered pixel check

`deciding-pixels.json` records the WCS position, positive target-pixel flux and cutout SHA-256. `deciding-pixels.png` shows 1x1, 3x3 and 5x5 raw cutout sums around the deciding window. Extraction and plot reproduce with `../inspect_deciders.py`.
