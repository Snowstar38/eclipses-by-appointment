# Q058 - TIC 469821735

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Evidence and interpretation

S94 3868.501 has only 39% core because of a roughly 1.06 d gap, and 3874.873 has 28% core at the shared S94 gap feature. S100 4092.325 and S103 4158.550/4170.126 are low-amplitude baseline ripples or segment-edge structures; S102 4133.904 is a level change with no closed trough. The remaining sectors show small unrelated changes, not a repeated eclipse kind.

No event-derived period or measured conjunction ties these flags to Gaia SB2 P32.4127 d.

## Limits and next check

Refutes the selected repeat-sector morphology; no source claim follows from the blended aperture. Catalogue gates for this exact queue failed; the cached primary nonmatch does not establish novelty. The verdict is about the selected eclipse interpretation, not a claim that the Gaia source cannot be binary.

Find two complete matching events before timing and source tests.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result, and used FITS SHA-256 before plotting raw SAP for all 10 cached sectors. `lead-context.json` and `lead-local-series.json` record the numeric source series, actual quality-zero positive-flux coverage, gaps, and screen windows. `lead-flag-diagnostics.json` records actual core endpoints and gaps for 6 flagged dip windows. `lead-alternate.png` and `lead-alternate.json` compare the same-photon pipeline reductions around deciding windows. Screening centers are not measured eclipse times. The independent helper audit supplies a separate review.
