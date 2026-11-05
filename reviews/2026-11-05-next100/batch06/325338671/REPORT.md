# Q053 - TIC 325338671

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Evidence and interpretation

S94 3874.888 has only 39% of its nominal core and matches the cross-target S94 gap feature. S103 4165.043 has 34% core and ends in a gap; S104 4197.338 has 46% core and is synchronous with Q052/Q055. S102 4147.027 is flat at its selected center, while S104 4185.629 is a level change after a gap rather than a closed trough. Raw sectors 1/13/27/67/95 also show no matching eclipse profile.

The flags supply no measured same-kind timing to test against Gaia SB1 P50.9465 d.

## Limits and next check

The selected eclipse interpretation is refuted; low-amplitude unrelated variability remains possible. Catalogue gates for this exact queue failed; the cached primary nonmatch does not establish novelty. The verdict is about the selected eclipse interpretation, not a claim that the Gaia source cannot be binary.

Seek an isolated full event away from shared segment boundaries.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result, and used FITS SHA-256 before plotting raw SAP for all 10 cached sectors. `lead-context.json` and `lead-local-series.json` record the numeric source series, actual quality-zero positive-flux coverage, gaps, and screen windows. `lead-flag-diagnostics.json` records actual core endpoints and gaps for 5 flagged dip windows. `lead-alternate.png` and `lead-alternate.json` compare the same-photon pipeline reductions around deciding windows. Screening centers are not measured eclipse times. The independent helper audit supplies a separate review.
