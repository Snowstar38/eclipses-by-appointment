# H057 — TIC 262548177

Physical verdict: **REFUTED** selected eclipse. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN** because four VizieR gates remain unqueried after the central positive-control failure. A primary-table nonmatch does not clear novelty.

Gaia DR3 4935773672080920704, SB1, orbital period 45.46367138413638 d. Raw QLP SAP with QUALITY=0 was inspected for all cached sectors: 2,3,29,30,69,96,103,104. The orbital period is context, not a measured photometric period in this review.

## Deciding evidence

Sector 96 has a broad wave and changing scatter around BTJD 3926.040, then another downward trend toward its end. Its selected trough tracks H052 at the same time: an independent 0.1-day binned comparison over BTJD 3923–3929 has correlation 0.9755 across 58 paired bins (helper-common-s96.json), positive contrary evidence for an individual eclipse. Sector 69 contains a much larger broad wave, sector 29 contains a large upward ramp, and sectors 103–104 show level changes around gaps. These are not a stable same-kind eclipse sequence at the Gaia 45.464 d period.

## Limits and next check

The selected eclipse feature is refuted; synchronized behavior does not assign a unique mechanism or exclude an unrelated eclipse. Obtain stable independent photometry only if a distinct contact-shaped event emerges. No photometric period, epoch or depth is promoted from a refuted feature.

## Sources

`raw-inspection.json` contains source-verified FITS identities, cadence coverage and flagged-window numbers; `raw-windows.png` and `orbit-context.png` show raw event and full-sector context. `orbit-context.json` contains approximate Gaia edge-on conjunction predictions where orbital elements exist; these are diagnostic phase windows, not measured centers. `qlp-alternate.json` and `.png` preserve the available FITS flux/background/centroid columns. `../SOURCE-HASHES.json` re-verifies frozen source packets, bulk results and all 77 cached FITS; `../sector-availability.json` records the current TESSCut sector inventory. The independent same-time comparison is in ../helper-common-s96.json/png.
