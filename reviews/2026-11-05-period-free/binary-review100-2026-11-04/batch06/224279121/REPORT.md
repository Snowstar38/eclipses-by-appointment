# H052 — TIC 224279121

Physical verdict: **REFUTED** selected eclipse. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN** because four VizieR gates remain unqueried after the central positive-control failure. A primary-table nonmatch does not clear novelty.

Gaia DR3 6537661233557980928, SB1, orbital period 37.55269026667582 d. Raw QLP SAP with QUALITY=0 was inspected for all cached sectors: 2,29,69,96. The orbital period is context, not a measured photometric period in this review.

## Deciding evidence

Sector 96 shows a broad, changing wave through BTJD 3926.333 with irregular scatter in its trough; the raw curve continues to decline again after BTJD 3930. The selected trough tracks H057 in the same sector: an independent 0.1-day binned comparison over BTJD 3923–3929 has correlation 0.9755 across 58 paired bins (helper-common-s96.json). These are widely separated targets and the synchronized shape is positive contrary evidence for an individual eclipse. Earlier sectors 2, 29 and 69 show broad dips and rises at differing phases and widths.

## Limits and next check

The selected sector-96 eclipse interpretation is refuted; synchronized behavior does not identify a unique instrument mechanism or the source of the broader modulation. Study the modulation with stable independent photometry if useful. No photometric period, epoch or depth is promoted from a refuted feature.

## Sources

`raw-inspection.json` contains source-verified FITS identities, cadence coverage and flagged-window numbers; `raw-windows.png` and `orbit-context.png` show raw event and full-sector context. `orbit-context.json` contains approximate Gaia edge-on conjunction predictions where orbital elements exist; these are diagnostic phase windows, not measured centers. `qlp-alternate.json` and `.png` preserve the available FITS flux/background/centroid columns. `../SOURCE-HASHES.json` re-verifies frozen source packets, bulk results and all 77 cached FITS; `../sector-availability.json` records the current TESSCut sector inventory. The independent same-time comparison is in ../helper-common-s96.json/png.
