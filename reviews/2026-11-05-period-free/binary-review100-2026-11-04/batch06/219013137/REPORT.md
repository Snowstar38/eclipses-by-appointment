# H051 — TIC 219013137

Physical verdict: **REFUTED** selected eclipse. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN** because four VizieR gates remain unqueried after the central positive-control failure. A primary-table nonmatch does not clear novelty.

Gaia DR3 1694963767685503872, SB1, orbital period 47.21445939069959 d. Raw QLP SAP with QUALITY=0 was inspected for all cached sectors: 14,15,16,20,21,22,40,41,47,48,49,74,75,76,80. The orbital period is context, not a measured photometric period in this review.

## Deciding evidence

The sector-80 screening dip at BTJD 3491.303 follows a multi-day downward drift into the midsector data gap. Its supposed recovery is the offset at the start of the next observing segment; the pre-gap flux does not show a resolved eclipse egress. Sector 49 has a similar reset and settling curve at a gap, while the other thirteen raw sectors show smaller changing baselines rather than a coherent 47.214 d eclipse kind. The screening window is therefore a gap/trend feature.

## Limits and next check

The selected sector-80 feature is refuted; these data do not rule out a weaker separate eclipse. Only reconsider on a new resolved repeat with complete ingress and egress. No photometric period, epoch or depth is promoted from a refuted feature.

## Sources

`raw-inspection.json` contains source-verified FITS identities, cadence coverage and flagged-window numbers; `raw-windows.png` and `orbit-context.png` show raw event and full-sector context. `orbit-context.json` contains approximate Gaia edge-on conjunction predictions where orbital elements exist; these are diagnostic phase windows, not measured centers. `qlp-alternate.json` and `.png` preserve the available FITS flux/background/centroid columns. `../SOURCE-HASHES.json` re-verifies frozen source packets, bulk results and all 77 cached FITS; `../sector-availability.json` records the current TESSCut sector inventory.
