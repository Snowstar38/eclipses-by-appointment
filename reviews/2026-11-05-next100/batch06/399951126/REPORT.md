# Q057 - TIC 399951126

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Evidence and interpretation

Twelve raw sectors show broad irregular waves, often several percent deep, with bright flags on corresponding crests and segment jumps. The 23 selected dip flags sample wave troughs and slopes, with depths and spacing changing between sectors; S14 near 1693, S81 near 3522, and S82 near 3543 are wide U-shaped minima rather than discrete eclipses. KSPSAP in S14 and DET_FLUX in S81/S82 suppress the broad wave, so its physical origin remains unsettled.

No reproducible narrow same-kind eclipse morphology, event timing, or alias-tested period connects these minima to Gaia SB1 P21.2616 d.

## Limits and next check

The selected eclipse interpretation is refuted. The broad modulation itself may be intrinsic or extraction-related and is not classified further here. Catalogue gates for this exact queue failed; the cached primary nonmatch does not establish novelty. The verdict is about the selected eclipse interpretation, not a claim that the Gaia source cannot be binary.

Use independent target-centered pixels to determine the broad-wave source before any variable-star classification.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result, and used FITS SHA-256 before plotting raw SAP for all 12 cached sectors. `lead-context.json` and `lead-local-series.json` record the numeric source series, actual quality-zero positive-flux coverage, gaps, and screen windows. `lead-flag-diagnostics.json` records actual core endpoints and gaps for 23 flagged dip windows. `lead-alternate.png` and `lead-alternate.json` compare the same-photon pipeline reductions around deciding windows. Screening centers are not measured eclipse times. The independent helper audit supplies a separate review.
