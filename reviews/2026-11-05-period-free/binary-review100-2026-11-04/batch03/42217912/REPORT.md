# H026 — TIC 42217912

Physical verdict: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four scoped VizieR gates were unavailable after a positive-control timeout. A primary-table nonmatch is not novelty clearance.

Gaia DR3 source 5939499145420713984, SB1 period 40.39429 d. Frozen stratum `cross_method_dip`; sample ID is not a new-system acceptance. Quality-zero raw SAP sectors inspected: 12, 39, 66, 93, 103, 104.

## Deciding evidence

The s66 retained dip at BTJD 3111.06 is a low segment bounded by large discontinuities and a gap, not a resolved ingress and egress. s39/s93/s103/s104 exhibit much larger broad trends and ramp/reset behavior; s103 brightening is part of that variation.

## Limits and next check

Selected dip is a gap/baseline artifact in this reduction; physical source of broader variation is unassigned. Current sector inventory contains exactly the six cached sectors. Use stable independent photometry to study broad variation if desired.

## Reproducibility

`raw-inspection.json` verifies original bulk-result and FITS SHA-256 values and tabulates representative screening windows. `raw-windows.png` shows these raw windows; `orbit-context.json` and `.png` show full cached-sector SAP and Gaia edge-on conjunction predictions. Screening/conjunction times are not measured event centers. The frozen [source packet](../../source-packets/42217912/sources.json), [central novelty evidence](../../shared-catalogues/target-evidence.json), batch scripts and SHA256SUMS.json preserve receipts.

`sector-availability.raw` and `../sector-availability.json` record the current TESSCut sector inventory and response hash.
