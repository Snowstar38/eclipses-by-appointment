# U006 — TIC 356801225

**Physical verdict:** CONFIRMED (provisional lead classification). **Bounded review:** COMPLETE. **Catalogue status:** NO_EXACT_MATCH_IN_CHECKED_SCOPE; no new-system claim is made here. The shared-catalogue receipts define the checked scope.

## Raw events and coverage

Four deep raw SAP eclipses in S40, S54, S80 and S81 have sharp matching ingress/egress and fitted depths about 228–241 ppt. Centers 2409.550, 2781.933, 3480.150 and 3526.696 BTJD fit cycle indices 0,8,23,24 with P=46.547769 d and 0.00081 d timing residual RMS. S80 begins near ingress, but the depression and recovery are clear; the other three provide complete context.

Cached QLP sector coverage: 40,54,80,81. Lead verified SHA256 of every used FITS and bulk-result file before measuring. `lead-context.json` contains cadence endpoints, quality-zero sample counts and flagged-window measurements; `lead-timing.json` contains local trapezoid measurements. The gallery `lead-raw-context.png` shows representative raw SAP alongside KSPSAP where present. Detector window centers were used only as search seeds.

## Timing and Gaia geometry

The adjacent S80/S81 same-kind occurrences fix the approximate 46.55 d cycle independently of the long-baseline integer assignment. P/2 through P/5 predict S80 raw cores at BTJD 3503.424, 3495.666, 3491.787 and 3489.460: each has 120–121 quality-zero core points, both local baselines and median depths from -0.64 to +0.64 ppt against about 230 ppt actual eclipses. A P/6 prediction at 3487.908 is gapped, but the second P/6 prediction at 3495.666 has 121 complete points and -0.64 ppt median deficit. These are bounded actual-cadence nulls. Gaia SB1 P=46.549324±0.020222 d agrees, and a source-specific edge-on conjunction is within 0.0009 phase of the S40 measured event. The period error from a local trapezoid covariance is not a total calibrated ephemeris uncertainty.

## Source and alternate reduction

S81 TESSCut difference flux peaks on target WCS, distinctly away from the 52.25 arcsec cataloged EA neighbor with P=0.6754534 d. The neighbor short clock cannot explain the observed 46.55 d train. S54 KSPSAP is badly distorted whereas raw SAP retains the eclipse; independent TESSCut supports the representative target event.

## Limits and next check

Four target-region raw eclipses, independent reductions and compatible Gaia geometry satisfy the bounded physical classification. Close unresolved blends and detailed stellar parameters remain unmeasured. The distant cataloged EA is not this signal.

Obtain resolved follow-up photometry and a formal joint RV/eclipsing fit.

## Provenance

`../queue.csv`, `../lead-source-hashes.json`, `../lead_context.py`, `../lead_timing.py`, `../lead-clocks.json`, `../lead-geometry.json`, helper pixel scripts/receipts/images and shared-catalogues exact target receipts form the audit trail. For current-sector additions see `../lead-current-sector-inventory.json`, `../lead-extra-sector-receipts.json`, and, for U009, `lead-new-clock.json` and `lead-alias-check.json`. Same photons in different reductions are not independent observations.
