# Q089 - TIC 382040915

**Physical verdict:** REFUTED. **Review completion:** COMPLETE. **Catalogue novelty:** UNKNOWN.

## Raw morphology and coverage

Nine cached sectors. S94 flags at 3869.57 and 3874.93 have only 50% and 27% nominal core coverage at strong breaks; the latter is the six-target common trough. S101 4112.92 has 49% core coverage at a reset. An unflagged V near S67 BTJD 3147 loses egress across a 0.220-d gap and is highly correlated with unrelated targets on other cameras.

## Timing and orbital interpretation

No flagged or unflagged feature supplies a representative complete eclipse and repeated same-kind center. The screen values cannot resolve aliases or support Gaia P38.4737 d.

## Source and alternative reduction

S94 is cross-camera common mode. The independent helper compared the S67 V with unrelated controls (correlations 0.967 and 0.959 on 0.1-d bins), and Q086 S39 shares a broad decline near 2381. Those positive comparisons favor an instrumental origin for the inspected exceptions. Raw SAP, cross-target controls and the S39 KSPSAP comparison were inspected. S67 lacks KSPSAP; no unavailable reduction is treated as a null.

## Limits and next check

This refutes the selected repeat-sector eclipse interpretation and the inspected S67 exception; unseen weaker events remain outside this bounded review.

Require a clean isolated eclipse outside shared camera/systematic features before source attribution.

## Provenance

`lead-context.json`, `lead-local-series.json` and `lead-flag-diagnostics.json` preserve raw quality-zero time/flux, actual endpoints and gaps for all 9 cached sectors and selected windows. `lead-raw-context.png` and `lead-dip-zooms.png` show the morphology. Batch-level cross-target, alternate-reduction and exception receipts and independent `helper-audit.md` support the source findings. The context script checks the sealed source-packet, bulk-result and FITS SHA-256 receipts. Screening window centers are predictions, never measured eclipse times. Exact target VSX query receipts are in `../../tap-recovery/vsx-Q089.json`; remaining ASAS-SN and Kostov gates are unavailable, so novelty stays UNKNOWN.
