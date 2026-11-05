# Q081 - TIC 410117870

**Physical verdict:** REFUTED. **Review completion:** COMPLETE. **Catalogue novelty:** UNKNOWN.

## Raw morphology and coverage

Nine cached sectors. S94 flags at 3868.50 and 3874.86 meet coverage breaks, with only 40% and 39% of nominal cores sampled. S103 4165.04 and S104 4197.32 also straddle gaps with 34% and 48% core coverage. Sector-wide SAP shows sharp resets and ramps rather than isolated full ingress, bottom and egress.

## Timing and orbital interpretation

No measured discrete eclipse centers remain after the gap checks. The apparent S94, S103 and S104 spacings cannot define an integer-cycle eclipse period or be compared meaningfully with Gaia P25.0979 d.

## Source and alternative reduction

The S94 3874.7 trough occurs simultaneously in six queue targets on cameras 2, 3 and 4 and CCDs 1-4. Q081 S104 shares a flagged gap feature with Q086 at 4197. The shared features favor spacecraft/reduction effects over a target-owned eclipse. Independent raw SAP views and the cross-target S94 overlay reproduce the selected feature. QLP alternate columns do not create another observing occasion.

## Limits and next check

This refutes the selected repeat-sector eclipse interpretation; it does not exclude every weaker eclipse elsewhere.

Require a fully sampled isolated repeat outside shared spacecraft events before reconsidering the source.

## Provenance

`lead-context.json`, `lead-local-series.json` and `lead-flag-diagnostics.json` preserve raw quality-zero time/flux, actual endpoints and gaps for all 9 cached sectors and selected windows. `lead-raw-context.png` and `lead-dip-zooms.png` show the morphology. Batch-level cross-target, alternate-reduction and exception receipts and independent `helper-audit.md` support the source findings. The context script checks the sealed source-packet, bulk-result and FITS SHA-256 receipts. Screening window centers are predictions, never measured eclipse times. Exact target VSX query receipts are in `../../tap-recovery/vsx-Q081.json`; remaining ASAS-SN and Kostov gates are unavailable, so novelty stays UNKNOWN.
