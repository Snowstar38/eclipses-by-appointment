# H010 — TIC 52919409

Physical verdict: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four scoped VizieR gates remained unqueried after the positive control timed out, so bounded local nonmatches are not clearance.

Gaia DR3 source 5583065032167575296, SB1 period 58.87404 d. Frozen stratum `cross_method_dip`; sample position is not scientific rank. Cached quality-zero raw SAP sectors: 6, 7, 33, 34, 87.

## Deciding evidence

s6 and s34 flags follow broad quasi-periodic variability, with s34 interrupted by a gap; their shapes and context do not support a matched eclipse. Full five-sector SAP curves show rolling modulation rather than stable flat-bottom events.

## Limits and next check

This refutes the screened eclipse interpretation but does not identify the physical source of variability. Compare independent photometry if the non-eclipse variability is investigated.

## Reproducibility

`raw-inspection.json` verifies the bulk JSON and each used FITS SHA-256 and records representative screening windows. `raw-windows.png` shows flagged raw windows; `orbit-context.png` and `.json` show full cached-sector SAP and Gaia conjunction predictions. These predictions are not event timings. Source packets under `../../source-packets/52919409/sources.json` carry frozen target/orbit/fold receipts. `../../shared-catalogues/target-evidence.json` holds bounded novelty evidence; a failed remote query is unknown. Scripts in this batch reproduce lead artifacts.
