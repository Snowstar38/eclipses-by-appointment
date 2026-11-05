# H005 — TIC 277891015

Physical verdict: **PLAUSIBLE**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four scoped VizieR gates remained unqueried after the positive control timed out, so bounded local nonmatches are not clearance.

Gaia DR3 source 6353362709418035200, SB1 period 34.18186 d. Frozen stratum `cross_method_dip`; sample position is not scientific rank. Cached quality-zero raw SAP sectors: 1, 13, 27, 28, 67, 68, 94, 95.

## Deciding evidence

One shallow s94 depression at BTJD ~3875.09 sits near a gap and on a changing baseline. Earlier full SAP sectors do not show a secure matched event. The s95 raw flux has pathological near-zero stretches despite quality-zero samples, so it cannot certify a null.

## Limits and next check

Eclipse shape, recurrence, period and source attribution are insecure; 206 other-CCD flags are a common-mode hint only. Recover a clean second event with usable pre/post baseline, then test pixel attribution.

## Reproducibility

`raw-inspection.json` verifies the bulk JSON and each used FITS SHA-256 and records representative screening windows. `raw-windows.png` shows flagged raw windows; `orbit-context.png` and `.json` show full cached-sector SAP and Gaia conjunction predictions. These predictions are not event timings. Source packets under `../../source-packets/277891015/sources.json` carry frozen target/orbit/fold receipts. `../../shared-catalogues/target-evidence.json` holds bounded novelty evidence; a failed remote query is unknown. Scripts in this batch reproduce lead artifacts.

Current TESScut sector inventory returned HTTP 200 with sectors [1, 13, 27, 28, 67, 68, 94, 95]; it lists no additional sector beyond the cached set. The query receipt and response hash are in `sector-availability.json` and `sector-availability.raw`.
