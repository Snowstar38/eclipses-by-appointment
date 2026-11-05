# H059 — TIC 129543547

Physical verdict: **REFUTED** selected eclipse. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN** because four VizieR gates remain unqueried after the central positive-control failure. A primary-table nonmatch does not clear novelty.

Gaia DR3 6669670519439832704, SB1, orbital period 31.69682608826778 d. Raw QLP SAP with QUALITY=0 was inspected for all cached sectors: 27,67,94. The orbital period is context, not a measured photometric period in this review.

## Deciding evidence

The sector-94 flagged dip at BTJD 3874.940 is embedded in the broad decline and rebound shared at nearly the same time by H053 and H055. The numeric common-s94.json comparison has all three low near BTJD 3875 and back up by 3876, despite distant sky positions. Sector 27 instead has another many-day variable trend, and sector 67 has a broad mild trough; neither gives a clean same-kind repeat.

## Limits and next check

The selected sector-94 eclipse is refuted; a weaker separate eclipse remains possible. Require a new isolated complete event before source or timing work. No photometric period, epoch or depth is promoted from a refuted feature.

## Sources

`raw-inspection.json` contains source-verified FITS identities, cadence coverage and flagged-window numbers; `raw-windows.png` and `orbit-context.png` show raw event and full-sector context. `orbit-context.json` contains approximate Gaia edge-on conjunction predictions where orbital elements exist; these are diagnostic phase windows, not measured centers. `qlp-alternate.json` and `.png` preserve the available FITS flux/background/centroid columns. `../SOURCE-HASHES.json` re-verifies frozen source packets, bulk results and all 77 cached FITS; `../sector-availability.json` records the current TESSCut sector inventory. The cross-target numeric comparison is in ../common-s94.json and the independent fine-bin audit is in ../helper-common-s94.json/png.
