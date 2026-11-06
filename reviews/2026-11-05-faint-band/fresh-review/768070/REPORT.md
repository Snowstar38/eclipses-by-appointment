# U009 — TIC 768070

**Physical verdict:** PROBABLE (provisional lead classification). **Bounded review:** COMPLETE. **Catalogue status:** NO_EXACT_MATCH_IN_CHECKED_SCOPE; no new-system claim is made here. The shared-catalogue receipts define the checked scope.

## Raw events and coverage

Current TESSCut inventory added S106–S109 beyond the frozen QLP S5/S32/S98 set. Two complete target-centered, steep-contact events in S106 and S108 fit BTJD 4247.12965 and 4299.27746, with independent centered-aperture depths about 73 and 69 ppt and durations about 0.28 d. Their separation is 52.14781 d. S98 QLP SAP and an alternate TESSCut aperture show ingress and a low interval near 4038.53, within about 0.01 d of four earlier cycles, but a 0.23 d gap removes full egress and post-gap baseline shifts; its trapezoid center is not used as a precision timing.

Cached QLP sector coverage: 5,32,98. Lead verified SHA256 of every used FITS and bulk-result file before measuring. `lead-context.json` contains cadence endpoints, quality-zero sample counts and flagged-window measurements; `lead-timing.json` contains local trapezoid measurements. The gallery `lead-raw-context.png` shows representative raw SAP alongside KSPSAP where present. Detector window centers were used only as search seeds.

## Timing and Gaia geometry

S107 provides well-covered nulls at P/2 and P/3 aliases: 121 quality-zero core points at each trial, median local deficits -1.25, -0.85 and -0.40 ppt versus about 70 ppt at actual events. This bounded test supports a 52.15 d same-kind clock, while a longer period with alternating conjunctions is not exhaustively ruled out. Gaia SB1 P=52.13086±0.04613 d is compatible; an edge-on conjunction estimate is 0.91 d from S106, smaller than the roughly 3.4 d accumulated formal-period allowance from Gaia reference epoch.

## Source and alternate reduction

S106 and S108 TESSCut difference images peak on the target WCS position in differently oriented sectors, within roughly 0.16–0.18 pixel of the target. S98 difference has a target-region component plus roughly 20 e/s common drift. QLP SAP and the independently made TESSCut aperture both show its partial event; these share TESS photons.

## Limits and next check

Two full repeated events and a gap-truncated third support a real eclipsing source near the target. Close blending and the S98 background/reset prevent definitive source assignment and a precision long-baseline clock.

Acquire further target-centered repeats and a spatially resolved source check; compare complete Gaia RV covariance with eclipse timing.

## Provenance

`../queue.csv`, `../lead-source-hashes.json`, `../lead_context.py`, `../lead_timing.py`, `../lead-clocks.json`, `../lead-geometry.json`, helper pixel scripts/receipts/images and shared-catalogues exact target receipts form the audit trail. For current-sector additions see `../lead-current-sector-inventory.json`, `../lead-extra-sector-receipts.json`, and, for U009, `lead-new-clock.json` and `lead-alias-check.json`. Same photons in different reductions are not independent observations.
