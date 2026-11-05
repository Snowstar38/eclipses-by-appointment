# H054 — TIC 70761950

Physical verdict: **REFUTED** selected eclipse. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN** because four VizieR gates remain unqueried after the central positive-control failure. A primary-table nonmatch does not clear novelty.

Gaia DR3 2309735834427777920, SB1, orbital period 49.94717488517798 d. Raw QLP SAP with QUALITY=0 was inspected for all cached sectors: 2,29,96. The orbital period is context, not a measured photometric period in this review.

## Deciding evidence

The two sector-96 dip flags at BTJD 3921.793 and 3925.981 mark a large flux reset and subsequent settling across a sector gap. The raw sequence starts low after the gap and rises slowly, then jumps to a different level; there is no bounded dip with ingress and egress at either screening center. Sectors 2 and 29 lack a comparable eclipse feature.

## Limits and next check

The selected features are positive gap and step artifacts, so the eclipse interpretation is refuted. Only revisit if a distinct complete repeat appears. No photometric period, epoch or depth is promoted from a refuted feature.

## Sources

`raw-inspection.json` contains source-verified FITS identities, cadence coverage and flagged-window numbers; `raw-windows.png` and `orbit-context.png` show raw event and full-sector context. `orbit-context.json` contains approximate Gaia edge-on conjunction predictions where orbital elements exist; these are diagnostic phase windows, not measured centers. `qlp-alternate.json` and `.png` preserve the available FITS flux/background/centroid columns. `../SOURCE-HASHES.json` re-verifies frozen source packets, bulk results and all 77 cached FITS; `../sector-availability.json` records the current TESSCut sector inventory.
