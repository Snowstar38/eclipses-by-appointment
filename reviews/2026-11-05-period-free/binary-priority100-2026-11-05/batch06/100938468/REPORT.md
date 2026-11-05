# T053 - TIC 100938468

Physical verdict: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

Selection: cross_method_dip, Gaia DR3 5710141908882383744, Gaia NSS SB1 period 37.2731414204704 d. This is a selection orbit, not a measured eclipse period.

## Raw evidence

The retained s88 deficit is an immediate step after the 3703.89294-3704.10359 BTJD interruption, then slow recovery. Adjacent quality-zero SAP medians change 0.97150 to 0.95710 while SAP_BKG changes -177.17 to 214.995. The other four cached sectors contain broad trends and no matching eclipse.

## Coverage, timing and attribution

5 verified cached QLP sectors; coverage and retained-window numbers are in `initial-numerics.json` and `step-context.json`. `predicted-windows.json` lists actual cadence and sideband samples at Gaia-period and half-phase predictions; these are not clean nulls without raw context. Screening windows were predictions; no eclipse period, primary epoch or depth was measured. The s88 shape is a gap-associated background step, without measured eclipse ingress, center or egress.

The shared catalogue matrix records four unavailable VizieR gates (VSX, ASAS-SN and Kostov 2025 tables 3/4). Exact nonmatches in available primary tables and Gaia do not establish novelty. The shared 120-arcsec Gaia neighbor cone is available in `../../shared-catalogues/gaia-neighbors.json`; no neighbor exclusion or Gaia-orbit geometry inference is needed to refute the selected non-eclipse feature.

Official TESSCut sector query: https://mast.stsci.edu/tesscut/api/v0.1/sector?ra=129.34663660456968&dec=-15.756480101402808; newer sectors than cached QLP: []. Query response SHA-256: a820aaf748147676d941ca2d7e64f0f8cce4f01911e4e614ced62474ea7e867f.

## Limits and next check

Seek a clean future raw eclipse before any physical-period claim.

## Sources

Bulk detector packet: `[local-path-redacted]` (SHA-256 890d9646dd3ceff73f8388652c04256509a805d003be0584712bb1c31fbfee8f). Each QLP FITS path and verified SHA-256 is listed in `initial-numerics.json`. Plots: `raw-flags.png` and `raw-overview.png`. Scripts: `inspect_raw.py`, `check_steps.py`, `predicted_windows.py`, `current_sectors.py`, `write_reports.py`. The official cutout is independent pixel extraction of the same photons if used; it is not an independent observing occasion.
