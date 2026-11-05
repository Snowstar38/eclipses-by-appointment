# Q060 - TIC 161168392

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Evidence and interpretation

S1/S28/S95/S104 SAP shows smooth broad waves and segment offsets. S1 1340.328 lies on a wave slope with 51% nominal core; S102 4133.860 is a sharp level drop across a gap but is flat after the break; S104 4197.068 is on a broad decline next to a gap and recovers by a segment step. DET_FLUX suppresses the S102 and S104 structures while SYS_RM_FLUX tracks much of the raw trend.

None of the three flags supplies a measured same-kind eclipse center or a clock to associate with Gaia SB1 P59.1137 d.

## Limits and next check

The selected eclipse claim is refuted; smooth variability has no secure physical classification from these reductions. Catalogue gates for this exact queue failed; the cached primary nonmatch does not establish novelty. The verdict is about the selected eclipse interpretation, not a claim that the Gaia source cannot be binary.

Seek a complete isolated profile away from gaps with independent pixel evidence.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result, and used FITS SHA-256 before plotting raw SAP for all 5 cached sectors. `lead-context.json` and `lead-local-series.json` record the numeric source series, actual quality-zero positive-flux coverage, gaps, and screen windows. `lead-flag-diagnostics.json` records actual core endpoints and gaps for 3 flagged dip windows. `lead-alternate.png` and `lead-alternate.json` compare the same-photon pipeline reductions around deciding windows. Screening centers are not measured eclipse times. The independent helper audit supplies a separate review.
