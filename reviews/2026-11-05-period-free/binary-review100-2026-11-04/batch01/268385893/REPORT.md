# H006 — TIC 268385893

Physical verdict: **PLAUSIBLE**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four scoped VizieR gates remained unqueried after the positive control timed out, so bounded local nonmatches are not clearance.

Gaia DR3 source 2085661515089271168, SB1 period 45.87634 d. Frozen stratum `cross_method_dip`; sample position is not scientific rank. Cached quality-zero raw SAP sectors: 14, 15, 41, 54, 55, 56, 74, 75, 76, 81, 82.

## Deciding evidence

In s76 a broad flag is part of a rising step/brightening, while a separate narrow trough near BTJD 3388.84 is visible. Clean windows at the Gaia-period extrapolations in s75 (~3342.97) and s81 (~3526.47) lack comparable narrow troughs; an earlier s41 window is also quiet.

## Limits and next check

This disfavors repetition at that assumed Gaia phase, but the single trough is not securely classified; another period or non-eclipse variability remains possible. No event depth or timing precision is claimed. Seek another isolated narrow trough and test its period before source attribution.

## Reproducibility

`raw-inspection.json` verifies the bulk JSON and each used FITS SHA-256 and records representative screening windows. `raw-windows.png` shows flagged raw windows; `orbit-context.png` and `.json` show full cached-sector SAP and Gaia conjunction predictions. These predictions are not event timings. Source packets under `../../source-packets/268385893/sources.json` carry frozen target/orbit/fold receipts. `../../shared-catalogues/target-evidence.json` holds bounded novelty evidence; a failed remote query is unknown. Scripts in this batch reproduce lead artifacts.

Current TESScut sector inventory returned HTTP 200 with sectors [14, 15, 41, 54, 55, 56, 74, 75, 76, 81, 82]; it lists no additional sector beyond the cached set. The query receipt and response hash are in `sector-availability.json` and `sector-availability.raw`.

`repeat-windows.json` and `.png` test selected Gaia-period repeat opportunities; nulls apply only to that clock and phase.
