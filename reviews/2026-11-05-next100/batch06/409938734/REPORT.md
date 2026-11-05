# Q052 - TIC 409938734

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Evidence and interpretation

The four retained windows in S94/S101/S103/S104 are declines into or asymmetric recoveries from segment gaps, not repeated complete eclipse cores. The S94 3874.874 window has 193 of 692 expected core cadences; S101 4113.264 has 49% core, S103 4165.008 has 44%, and S104 4197.372 has 36%. The S94 shape repeats at the same time in unrelated Q053/Q055/Q056/Q058/Q059 on several cameras and CCDs. Earlier S13/S67 shallow broad dips do not reproduce a stable eclipse morphology.

No observed eclipse centers define a clock or a source-specific connection to Gaia SB1 P22.0772 d.

## Limits and next check

Refutes the selected repeat-sector eclipse evidence; a separate weak signal elsewhere is not excluded. Catalogue gates for this exact queue failed; the cached primary nonmatch does not establish novelty. The verdict is about the selected eclipse interpretation, not a claim that the Gaia source cannot be binary.

Require a fully observed isolated ingress, core, egress and source-localized loss.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result, and used FITS SHA-256 before plotting raw SAP for all 8 cached sectors. `lead-context.json` and `lead-local-series.json` record the numeric source series, actual quality-zero positive-flux coverage, gaps, and screen windows. `lead-flag-diagnostics.json` records actual core endpoints and gaps for 4 flagged dip windows. `lead-alternate.png` and `lead-alternate.json` compare the same-photon pipeline reductions around deciding windows. Screening centers are not measured eclipse times. The independent helper audit supplies a separate review.
