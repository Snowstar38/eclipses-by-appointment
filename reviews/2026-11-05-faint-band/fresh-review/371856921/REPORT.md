# U002 — TIC 371856921

**Physical verdict:** PLAUSIBLE (provisional lead classification). **Bounded review:** COMPLETE. **Catalogue status:** NO_EXACT_MATCH_IN_CHECKED_SCOPE; no new-system claim is made here. The shared-catalogue receipts define the checked scope.

## Raw events and coverage

S23 has one complete, flat-bottomed raw SAP depression centered by a local trapezoid at BTJD 1951.95793 with about 57 ppt depth and resolved ingress/egress. S50 has a broad wave but no matching discrete event.

Cached QLP sector coverage: 23,50. Lead verified SHA256 of every used FITS and bulk-result file before measuring. `lead-context.json` contains cadence endpoints, quality-zero sample counts and flagged-window measurements; `lead-timing.json` contains local trapezoid measurements. The gallery `lead-raw-context.png` shows representative raw SAP alongside KSPSAP where present. Detector window centers were used only as search seeds.

## Timing and Gaia geometry

The current TESSCut inventory contains only S23 and S50, matching the frozen QLP inventory. Gaia P=23.128222 d predicts an S50 conjunction at 2668.933 BTJD, before quality-zero S50 begins at 2669.4; the following conjunction is after the sector ends. S50 therefore supplies no sensitive repeat null. One observed occasion cannot select an integer cycle or establish recurrence. A source-specific edge-on Gaia conjunction is within about 0.275 d of S23, supportive but not a confirmation.

## Source and alternate reduction

S23 TESSCut difference peak is at the target WCS pixel. Raw SAP and KSPSAP show the same event; these use the same photons. The pixel check does not remove all close blends.

## Limits and next check

Single event; no second sensitive QLP/TESSCut sector is currently available. Eclipse interpretation, source ownership and orbital cycle remain uncertain.

Obtain another complete eclipse with source localization.

## Provenance

`../queue.csv`, `../lead-source-hashes.json`, `../lead_context.py`, `../lead_timing.py`, `../lead-clocks.json`, `../lead-geometry.json`, helper pixel scripts/receipts/images and shared-catalogues exact target receipts form the audit trail. For current-sector additions see `../lead-current-sector-inventory.json`, `../lead-extra-sector-receipts.json`, and, for U009, `lead-new-clock.json` and `lead-alias-check.json`. Same photons in different reductions are not independent observations.
