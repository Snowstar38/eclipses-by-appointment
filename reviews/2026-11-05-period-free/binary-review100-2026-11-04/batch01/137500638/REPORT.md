# H007 — TIC 137500638

Physical verdict: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four scoped VizieR gates remained unqueried after the positive control timed out, so bounded local nonmatches are not clearance.

Gaia DR3 source 1145707750552302080, SB1 period 56.80267 d. Frozen stratum `cross_method_dip`; sample position is not scientific rank. Cached quality-zero raw SAP sectors: 19, 20, 26, 40, 47, 53, 59, 60, 73, 74.

## Deciding evidence

The s59 dip flag is a gap recovery. The s74 selected dip is the low state before a large broad brightening, and its brightening flag captures that rise. Full ten-sector SAP context has variable baseline and no isolated repeated eclipse.

## Limits and next check

The broad brightening may have an astrophysical cause; eclipse refutation is limited to this candidate interpretation. Analyze the brightening morphology separately if pursued.

## Reproducibility

`raw-inspection.json` verifies the bulk JSON and each used FITS SHA-256 and records representative screening windows. `raw-windows.png` shows flagged raw windows; `orbit-context.png` and `.json` show full cached-sector SAP and Gaia conjunction predictions. These predictions are not event timings. Source packets under `../../source-packets/137500638/sources.json` carry frozen target/orbit/fold receipts. `../../shared-catalogues/target-evidence.json` holds bounded novelty evidence; a failed remote query is unknown. Scripts in this batch reproduce lead artifacts.
