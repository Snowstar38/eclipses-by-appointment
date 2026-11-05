# Q055 - TIC 158235054

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Evidence and interpretation

The S94 3874.819 flag has 189 of 692 nominal core cadences and coincides with the shared S94 gap feature. S104 4197.274 has 195 of 416 nominal core cadences, runs through a segment break and recovers asymmetrically. S13/S27/S67 show irregular millimagnitude trends but no repeat of either selected profile. DET_FLUX suppresses much of both flagged shapes.

The two windows are not measured same-kind events and yield no photometric period for the Gaia SB1 P39.4473 d orbit.

## Limits and next check

Refutes the selected repeat-sector claim, not all possible low-amplitude variability. Catalogue gates for this exact queue failed; the cached primary nonmatch does not establish novelty. The verdict is about the selected eclipse interpretation, not a claim that the Gaia source cannot be binary.

Find a clean full eclipse away from a segment break before source attribution.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result, and used FITS SHA-256 before plotting raw SAP for all 5 cached sectors. `lead-context.json` and `lead-local-series.json` record the numeric source series, actual quality-zero positive-flux coverage, gaps, and screen windows. `lead-flag-diagnostics.json` records actual core endpoints and gaps for 2 flagged dip windows. `lead-alternate.png` and `lead-alternate.json` compare the same-photon pipeline reductions around deciding windows. Screening centers are not measured eclipse times. The independent helper audit supplies a separate review.
