# H001 — TIC 418125608

Physical verdict: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four scoped VizieR gates remained unqueried after the positive control timed out, so bounded local nonmatches are not clearance.

Gaia DR3 source 1820196595922849536, SB1 period 38.34833 d. Frozen stratum `cross_method_dip`; sample position is not scientific rank. Cached quality-zero raw SAP sectors: 54, 81.

## Deciding evidence

The only retained dip, s81 BTJD 3518.706, is the start of a descending trend immediately before a gap and large flux step. The full s54/s81 SAP curves show broad evolving baselines, not a resolved repeat.

## Limits and next check

Refutation applies to the selected dip claim; a different hidden eclipse is not excluded. Independent high-resolution light curve of the s81 interval or a new clean conjunction window.

## Reproducibility

`raw-inspection.json` verifies the bulk JSON and each used FITS SHA-256 and records representative screening windows. `raw-windows.png` shows flagged raw windows; `orbit-context.png` and `.json` show full cached-sector SAP and Gaia conjunction predictions. These predictions are not event timings. Source packets under `../../source-packets/418125608/sources.json` carry frozen target/orbit/fold receipts. `../../shared-catalogues/target-evidence.json` holds bounded novelty evidence; a failed remote query is unknown. Scripts in this batch reproduce lead artifacts.
