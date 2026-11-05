# H004 — TIC 180808330

Physical verdict: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four scoped VizieR gates remained unqueried after the positive control timed out, so bounded local nonmatches are not clearance.

Gaia DR3 source 4605155439053175296, SB1 period 25.95737 d. Frozen stratum `cross_method_dip`; sample position is not scientific rank. Cached quality-zero raw SAP sectors: 26, 40, 74, 79, 80.

## Deciding evidence

The s26 retained dips are monotonic rising segments, s80 is a gap step, and s40/s79 are brightenings. Across five full SAP sectors the dominant signal is broad variation; no repeated eclipse is isolated.

## Limits and next check

The brightening may be real variability, with source and physical mechanism unassigned. Investigate the broad variability separately if of interest.

## Reproducibility

`raw-inspection.json` verifies the bulk JSON and each used FITS SHA-256 and records representative screening windows. `raw-windows.png` shows flagged raw windows; `orbit-context.png` and `.json` show full cached-sector SAP and Gaia conjunction predictions. These predictions are not event timings. Source packets under `../../source-packets/180808330/sources.json` carry frozen target/orbit/fold receipts. `../../shared-catalogues/target-evidence.json` holds bounded novelty evidence; a failed remote query is unknown. Scripts in this batch reproduce lead artifacts.
