# Q056 - TIC 346727714

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Evidence and interpretation

S94 3874.872 has only 196 of 692 expected core cadences and the same multi-target gap morphology. The S102 4145.071 flag has 47% core and lies beside a large segment-level offset; its local observed section is nearly flat, without an eclipse trough. The other seven sectors contain shallow broad ripples but no matching isolated event.

There is no measured eclipse clock or source-specific orbital comparison with Gaia SB1 P39.1545 d.

## Limits and next check

Selected-window refutation leaves any independent weak event untested. Catalogue gates for this exact queue failed; the cached primary nonmatch does not establish novelty. The verdict is about the selected eclipse interpretation, not a claim that the Gaia source cannot be binary.

Require a continuous full event, then compare source-resolved pixels.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result, and used FITS SHA-256 before plotting raw SAP for all 9 cached sectors. `lead-context.json` and `lead-local-series.json` record the numeric source series, actual quality-zero positive-flux coverage, gaps, and screen windows. `lead-flag-diagnostics.json` records actual core endpoints and gaps for 2 flagged dip windows. `lead-alternate.png` and `lead-alternate.json` compare the same-photon pipeline reductions around deciding windows. Screening centers are not measured eclipse times. The independent helper audit supplies a separate review.
