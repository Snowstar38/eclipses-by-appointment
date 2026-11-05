# T052 - TIC 41975422

Physical verdict: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

Selection: cross_method_dip, Gaia DR3 5008921603695895552, Gaia NSS SB1 period 43.924476646140036 d. This is a selection orbit, not a measured eclipse period.

## Raw evidence

The two dramatic s69 descents near 3193.3 and 3206.55 BTJD occur at spacecraft orbit/sector interruptions, with flagged lowest cadences and sudden recovery after the first gap. SAP_BKG rises 965.6 to 44960 over the first decline and 43.84 to 35350 over the second while SAP changes 1.004 to 0.942 and 1.001 to 0.952. Eight same-CCD comparison targets lack a matching drop: the evidence is target-specific background/aperture corruption, not a detector-wide veto.

## Coverage, timing and attribution

5 verified cached QLP sectors; coverage and retained-window numbers are in `initial-numerics.json` and `step-context.json`. `predicted-windows.json` lists actual cadence and sideband samples at Gaia-period and half-phase predictions; these are not clean nulls without raw context. Screening windows were predictions; no eclipse period, primary epoch or depth was measured. There are no reliable eclipse centers or cycle count from these two interruption-edge descents. Current TESSCut lists s104-s107 in addition to cached sectors; those are not needed to establish the retained s69 feature as instrumental.

The shared catalogue matrix records four unavailable VizieR gates (VSX, ASAS-SN and Kostov 2025 tables 3/4). Exact nonmatches in available primary tables and Gaia do not establish novelty. The shared 120-arcsec Gaia neighbor cone is available in `../../shared-catalogues/gaia-neighbors.json`; no neighbor exclusion or Gaia-orbit geometry inference is needed to refute the selected non-eclipse feature.

Official TESSCut sector query: https://mast.stsci.edu/tesscut/api/v0.1/sector?ra=22.9681937403791&dec=-38.82544271534891; newer sectors than cached QLP: [104, 105, 106, 107]. Query response SHA-256: 6dba95de73a679922202c1ae3d847aca7ea3fc97c4fed06f355acb68502b91e4.

## Limits and next check

Inspect current-sector target pixels only if an independent eclipse indication appears.

## Sources

Bulk detector packet: `[local-path-redacted]` (SHA-256 762048558239081cc630f2d3191a2c618570be3022dd1de5edcdfb9b221a1e40). Each QLP FITS path and verified SHA-256 is listed in `initial-numerics.json`. Plots: `raw-flags.png` and `raw-overview.png`. Scripts: `inspect_raw.py`, `check_steps.py`, `predicted_windows.py`, `current_sectors.py`, `write_reports.py`. The official cutout is independent pixel extraction of the same photons if used; it is not an independent observing occasion.
