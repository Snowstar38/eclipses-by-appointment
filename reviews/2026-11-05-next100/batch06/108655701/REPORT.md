# Q054 - TIC 108655701

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Evidence and interpretation

Across S7/S34/S61/S88 the raw curve is dominated by broad, roughly 10 to 15 d waves of several percent amplitude. Sixteen selected 0.12 d dip windows fall on different wave slopes or local ripples; they do not repeat a discrete ingress, flat core, and egress. S7 KSPSAP suppresses the broad wave but retains small rapid wiggles; S88 DET_FLUX suppresses the wave while SYS_RM_FLUX tracks SAP. Reduction sensitivity cautions against assigning its physical cause.

No event-derived eclipse center or period supports a Gaia SB1 P21.9628 d eclipse interpretation.

## Limits and next check

These windows do not demonstrate eclipses; the origin of the broad modulation is not established by these same-photon reductions. Catalogue gates for this exact queue failed; the cached primary nonmatch does not establish novelty. The verdict is about the selected eclipse interpretation, not a claim that the Gaia source cannot be binary.

Characterize the modulation with independent pixel extraction if its variable-star nature is of interest.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result, and used FITS SHA-256 before plotting raw SAP for all 4 cached sectors. `lead-context.json` and `lead-local-series.json` record the numeric source series, actual quality-zero positive-flux coverage, gaps, and screen windows. `lead-flag-diagnostics.json` records actual core endpoints and gaps for 16 flagged dip windows. `lead-alternate.png` and `lead-alternate.json` compare the same-photon pipeline reductions around deciding windows. Screening centers are not measured eclipse times. The independent helper audit supplies a separate review.
