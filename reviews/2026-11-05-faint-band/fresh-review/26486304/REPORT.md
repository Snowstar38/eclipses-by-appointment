# U005 — TIC 26486304

**Physical verdict:** CONFIRMED (provisional lead classification). **Bounded review:** COMPLETE. **Catalogue status:** NO_EXACT_MATCH_IN_CHECKED_SCOPE; no new-system claim is made here. The shared-catalogue receipts define the checked scope.

## Raw events and coverage

Sixteen resolved raw SAP dips occur across S14/S15/S75/S76/S80–S83 in two nearly equal-depth conjunction tracks. Representative flat-bottom dips are 34–46 ppt in the long-cadence and later 10-minute data, with consistent contacts across years. A same-kind eight-event fit spanning 2019–2024 gives P=26.079664 d and 0.00462 d residual RMS. The two kinds alternate by about 13.14 and 12.94 d in both early and late sectors, compatible with eccentric-orbit conjunction spacing rather than a constant half-period.

Cached QLP sector coverage: 14,15,75,76,80,81,82,83. Lead verified SHA256 of every used FITS and bulk-result file before measuring. `lead-context.json` contains cadence endpoints, quality-zero sample counts and flagged-window measurements; `lead-timing.json` contains local trapezoid measurements. The gallery `lead-raw-context.png` shows representative raw SAP alongside KSPSAP where present. Detector window centers were used only as search seeds.

## Timing and Gaia geometry

Successive same-kind events in adjacent S14/S15 and S75/S76 and repeated late sectors directly fix the approximate 26.08 d cycle. A P/2 single-kind interpretation fails because consecutive intervals are 13.1379/12.9402 d early and 13.1409/12.9387 d late. P/3, P/4 and P/6 predict complete raw S75 cores with 172–173 quality-zero points and median depths between -0.16 and +0.33 ppt against about 44 ppt actual eclipses. The first tested P/5 core is gapped (83 points), but an earlier P/5 prediction at BTJD 3352.753 has 173 complete points and -0.38 ppt median deficit. Gaia SB1 P=26.08509±0.00852 d agrees. An edge-on conjunction estimate is offset -0.0087 phase at the early epoch, within the 0.42 d simple period-accumulation allowance. Full Gaia covariance is not characterized.

## Source and alternate reduction

The S81 TESSCut independent aperture/difference measurements for both conjunction kinds have nearly identical target-centered spatial patterns and positive target flux. Raw SAP and KSPSAP preserve representative dips. These are independent reductions of the same TESS photons, not additional observing occasions.

## Limits and next check

The binary eclipse interpretation and target-region attribution satisfy this bounded review. TESS pixels do not uniquely exclude a very close unresolved blend. Catalogue novelty remains separate.

Fit both conjunction tracks jointly and obtain resolved imaging if available.

## Provenance

`../queue.csv`, `../lead-source-hashes.json`, `../lead_context.py`, `../lead_timing.py`, `../lead-clocks.json`, `../lead-geometry.json`, helper pixel scripts/receipts/images and shared-catalogues exact target receipts form the audit trail. For current-sector additions see `../lead-current-sector-inventory.json`, `../lead-extra-sector-receipts.json`, and, for U009, `lead-new-clock.json` and `lead-alias-check.json`. Same photons in different reductions are not independent observations.
