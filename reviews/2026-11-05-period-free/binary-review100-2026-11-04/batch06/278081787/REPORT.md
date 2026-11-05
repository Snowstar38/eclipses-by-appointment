# H055 — TIC 278081787

Physical verdict: **REFUTED** selected eclipse. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN** because four VizieR gates remain unqueried after the central positive-control failure. A primary-table nonmatch does not clear novelty.

Gaia DR3 5211293208483257088, SB1, orbital period 24.96171982255034 d. Raw QLP SAP with QUALITY=0 was inspected for all cached sectors: 1,4,7,10,11,12,13,27,28,30,31,33,34,37,38,39,61,63,64,65,66,67,87,88,90,93,94,97. The orbital period is context, not a measured photometric period in this review.

## Deciding evidence

The sector-94 candidate around BTJD 3875.079 is the same-time decline and rebound found in H053 and H059 at widely separated coordinates; common-s94.json records the synchronized minima and recovery. The bright flags in sectors 12 and 28 are strong upward ramps ending at data gaps, rather than opposite eclipse kinds. The 28-sector raw overview shows no coherent 24.962 d eclipse sequence matching these selected features.

## Limits and next check

Refutation applies to the selected dip and brightening interpretation; the target could host a weaker unrelated signal. Look for a separate complete eclipse in future photometry before assigning a period. No photometric period, epoch or depth is promoted from a refuted feature.

## Sources

`raw-inspection.json` contains source-verified FITS identities, cadence coverage and flagged-window numbers; `raw-windows.png` and `orbit-context.png` show raw event and full-sector context. `orbit-context.json` contains approximate Gaia edge-on conjunction predictions where orbital elements exist; these are diagnostic phase windows, not measured centers. `qlp-alternate.json` and `.png` preserve the available FITS flux/background/centroid columns. `../SOURCE-HASHES.json` re-verifies frozen source packets, bulk results and all 77 cached FITS; `../sector-availability.json` records the current TESSCut sector inventory. The cross-target numeric comparison is in ../common-s94.json and the independent fine-bin audit is in ../helper-common-s94.json/png.
