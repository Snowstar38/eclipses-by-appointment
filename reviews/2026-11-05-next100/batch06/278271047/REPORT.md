# Q059 - TIC 278271047

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Evidence and interpretation

S11 1614.054 is a narrow one-sided deficit with 46% nominal core coverage and no replicated profile in ten intervening sectors. S94 3874.878 has only 30% core and coincides with the shared gap feature across several cameras/CCDs. Their 2260.8 d spacing cannot establish a period because the two shapes are dissimilar and one is common instrumental structure.

No measured eclipse clock is available to compare with Gaia SB1 P26.2349 d.

## Limits and next check

Selected-window refutation does not rule out a separate weak binary signal. Catalogue gates for this exact queue failed; the cached primary nonmatch does not establish novelty. The verdict is about the selected eclipse interpretation, not a claim that the Gaia source cannot be binary.

Obtain another clean isolated event with full local cadence coverage.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result, and used FITS SHA-256 before plotting raw SAP for all 12 cached sectors. `lead-context.json` and `lead-local-series.json` record the numeric source series, actual quality-zero positive-flux coverage, gaps, and screen windows. `lead-flag-diagnostics.json` records actual core endpoints and gaps for 2 flagged dip windows. `lead-alternate.png` and `lead-alternate.json` compare the same-photon pipeline reductions around deciding windows. Screening centers are not measured eclipse times. The independent helper audit supplies a separate review.
