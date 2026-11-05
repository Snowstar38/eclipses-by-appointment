# H027 — TIC 113645244

Physical verdict: **CONFIRMED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four scoped VizieR gates were unavailable after a positive-control timeout. A primary-table nonmatch is not novelty clearance.

Gaia DR3 source 6740862492885594624, SB1 period 41.96173 d. Frozen stratum `cross_method_dip`; sample ID is not a new-system acceptance. Quality-zero raw SAP sectors inspected: 13, 27, 67, 94.

## Deciding evidence

Four narrow V-shaped raw eclipses in s13/s27/s67/s94 have independent fitted centers BTJD 1676.36097, 2053.87179, 3144.45939, 3857.53608. Integer cycles 0/9/35/52 give 41.94565 d and later timing residuals under 0.002 d. Nearby 5–14 first-interval assignments disagree by days except 9; the 20.9728 d half-period predicts a fully sampled s94 event at 3878.51, where no comparable dip occurs. Gaia P=41.96173 ± 0.02910 d and predicted conjunction at s13 differs by 0.10 d. Independent s67 TESSCut aperture recovers ~10.3 ppt; difference centroid lies 0.16 pixel from target, with capable Gaia neighbors 40–43 arcsec away at distinct WCS positions.

## Limits and next check

Local triangular-model centers/depths have no calibrated error. Gaia orbital covariance is unavailable; quoted geometry is approximate. Pixel reduction shares photons with SAP, and neighbor flux ratios use approximate G band. The broad s94 feature near 3874.6 is not assigned to this narrow eclipse kind. Observe another complete narrow eclipse with resolved photometry and fit a precision clock.

## Reproducibility

`raw-inspection.json` verifies original bulk-result and FITS SHA-256 values and tabulates representative screening windows. `raw-windows.png` shows these raw windows; `orbit-context.json` and `.png` show full cached-sector SAP and Gaia edge-on conjunction predictions. Screening/conjunction times are not measured event centers. The frozen [source packet](../../source-packets/113645244/sources.json), [central novelty evidence](../../shared-catalogues/target-evidence.json), batch scripts and SHA256SUMS.json preserve receipts.

[Independent helper audit](../helper-audit.md), [source attribution](../helper-source-attribution.json), `../helper-timing.json`, and helper pixel receipts document the event timing, aliases and WCS assessment.

The [half-period null](../helper-half-alias.json) records actual quality-zero cadence coverage and baseline around BTJD 3878.51. [Orbital calculation](../helper-orbit.json) uses marginal errors only; it is not a covariance-aware significance test.
