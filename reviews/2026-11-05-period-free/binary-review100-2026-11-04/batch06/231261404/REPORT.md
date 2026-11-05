# H058 — TIC 231261404

Physical verdict: **REFUTED** selected eclipse. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN** because four VizieR gates remain unqueried after the central positive-control failure. A primary-table nonmatch does not clear novelty.

Gaia DR3 6511402593784634496, SB1, orbital period 50.64977955290257 d. Raw QLP SAP with QUALITY=0 was inspected for all cached sectors: 1,28,68,95,102,104. The orbital period is context, not a measured photometric period in this review.

## Deciding evidence

The sector-102 screening dip near BTJD 4134.256 is actually the low plateau after an abrupt level change at a data gap; it persists for days without an eclipse egress. Sector 104 has another gap-reset low level, while sectors 28, 68 and 95 show rising ramps or edge decays. The bright flags pick those ramps, not a second eclipse kind.

## Limits and next check

The selected dip and brightenings are positive step/gap morphology, refuting an eclipse interpretation. Reinspect only if a complete isolated repeat is observed. No photometric period, epoch or depth is promoted from a refuted feature.

## Sources

`raw-inspection.json` contains source-verified FITS identities, cadence coverage and flagged-window numbers; `raw-windows.png` and `orbit-context.png` show raw event and full-sector context. `orbit-context.json` contains approximate Gaia edge-on conjunction predictions where orbital elements exist; these are diagnostic phase windows, not measured centers. `qlp-alternate.json` and `.png` preserve the available FITS flux/background/centroid columns. `../SOURCE-HASHES.json` re-verifies frozen source packets, bulk results and all 77 cached FITS; `../sector-availability.json` records the current TESSCut sector inventory.
