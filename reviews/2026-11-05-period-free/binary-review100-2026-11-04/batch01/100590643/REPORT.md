# H003 — TIC 100590643

Physical verdict: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four scoped VizieR gates remained unqueried after the positive control timed out, so bounded local nonmatches are not clearance.

Gaia DR3 source 2903839139857063680, SB1 period 56.80656 d. Frozen stratum `cross_method_dip`; sample position is not scientific rank. Cached quality-zero raw SAP sectors: 5, 6, 32, 33, 87, 98.

## Deciding evidence

Flagged s33, s87 and s98 dips are gap/step or changing-baseline segments in SAP; s98 is a long decline through a gap. Full sectors show jagged/broad variability, with no repeated resolved eclipse at the Gaia conjunctions.

## Limits and next check

This refutes the selected flagged/eclipse interpretation, not every possible unobserved eclipse. Check a clean future conjunction with a stable aperture if this variable merits follow-up.

## Reproducibility

`raw-inspection.json` verifies the bulk JSON and each used FITS SHA-256 and records representative screening windows. `raw-windows.png` shows flagged raw windows; `orbit-context.png` and `.json` show full cached-sector SAP and Gaia conjunction predictions. These predictions are not event timings. Source packets under `../../source-packets/100590643/sources.json` carry frozen target/orbit/fold receipts. `../../shared-catalogues/target-evidence.json` holds bounded novelty evidence; a failed remote query is unknown. Scripts in this batch reproduce lead artifacts.
