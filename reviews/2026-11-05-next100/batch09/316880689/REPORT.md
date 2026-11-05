# Q085 - TIC 316880689

**Physical verdict:** REFUTED. **Review completion:** COMPLETE. **Catalogue novelty:** UNKNOWN.

## Raw morphology and coverage

Ten cached sectors. S1 flags are successive minima of broad wavy variability and S28 flags are high-amplitude step/brightening disturbances. S68 and S103 contain smooth multi-day waves; S94, S95, S102 and S104 flags fall on common spacecraft events, coverage breaks or monotonic slopes. Examples: S94 and S95 nominal dip cores have 34% and 37% coverage, S103 4164.27 has 49%.

## Timing and orbital interpretation

No repeatable discrete ingress and egress yields measured same-kind centers. The screened dips cannot select an alias near Gaia P20.9445 d.

## Source and alternative reduction

The S94 3874.61 flag is simultaneous with five other targets across cameras/CCDs; S102 4144.53 is shared with Q082. These identify a common contribution to the selected flags, while the broad waves may have a separate source. S1 KSPSAP suppresses the broad SAP variation; that alone is not a physical null. The raw sector morphology and documented gap/step coverage carry the refutation.

## Limits and next check

This rejects the selected repeat-sector eclipse interpretation, not all possible stellar variability.

Characterize the broad wave separately if scientifically useful; require a distinct fully covered repeated eclipse for an EB claim.

## Provenance

`lead-context.json`, `lead-local-series.json` and `lead-flag-diagnostics.json` preserve raw quality-zero time/flux, actual endpoints and gaps for all 10 cached sectors and selected windows. `lead-raw-context.png` and `lead-dip-zooms.png` show the morphology. Batch-level cross-target, alternate-reduction and exception receipts and independent `helper-audit.md` support the source findings. The context script checks the sealed source-packet, bulk-result and FITS SHA-256 receipts. Screening window centers are predictions, never measured eclipse times. Exact target VSX query receipts are in `../../tap-recovery/vsx-Q085.json`; remaining ASAS-SN and Kostov gates are unavailable, so novelty stays UNKNOWN.
