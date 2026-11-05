# H053 — TIC 318649725

Physical verdict: **REFUTED** selected eclipse. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN** because four VizieR gates remain unqueried after the central positive-control failure. A primary-table nonmatch does not clear novelty.

Gaia DR3 6342084743774717312, AstroSpectroSB1, orbital period 49.062612879930775 d. Raw QLP SAP with QUALITY=0 was inspected for all cached sectors: 12,13,67,93,94. The orbital period is context, not a measured photometric period in this review.

## Deciding evidence

The sector-94 dip near BTJD 3874.887 sits in a broad decline and recovery at BTJD 3874–3877 that also occurs in sector-94 raw SAP of H055 and H059, targets widely separated on the sky. The common-s94.json bins show all three low around 3875 and recovering by 3876. Earlier sectors 12 and 13 have smooth multi-day waves, and sector 67 has another gradual downturn, not isolated eclipse contacts. The common timed feature and changing baseline refute this selected eclipse.

## Limits and next check

A common feature is diagnostic, without identifying a unique instrumental mechanism or excluding an unrelated weaker eclipse. Seek a new isolated complete event before timing or source analysis. No photometric period, epoch or depth is promoted from a refuted feature.

## Sources

`raw-inspection.json` contains source-verified FITS identities, cadence coverage and flagged-window numbers; `raw-windows.png` and `orbit-context.png` show raw event and full-sector context. `orbit-context.json` contains approximate Gaia edge-on conjunction predictions where orbital elements exist; these are diagnostic phase windows, not measured centers. `qlp-alternate.json` and `.png` preserve the available FITS flux/background/centroid columns. `../SOURCE-HASHES.json` re-verifies frozen source packets, bulk results and all 77 cached FITS; `../sector-availability.json` records the current TESSCut sector inventory. The cross-target numeric comparison is in ../common-s94.json and the independent fine-bin audit is in ../helper-common-s94.json/png.
