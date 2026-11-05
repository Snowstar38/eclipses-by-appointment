# H002 — TIC 352438536

Physical verdict: **CONFIRMED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four scoped VizieR gates remained unqueried after the positive control timed out, so bounded local nonmatches are not clearance.

Gaia DR3 source 6355981883553499776, SB1 period 58.99727 d. Frozen stratum `cross_method_dip`; sample position is not scientific rank. Cached quality-zero raw SAP sectors: 13, 27, 67, 93, 94, 101, 102, 103.

## Deciding evidence

Raw SAP has complete flat-bottom declines in s27 and s101, ~35–38 ppt over ~2.7 d. Locally fitted centers are BTJD 2040.0819 and 4106.0797; their 35-cycle separation gives 59.0285 d, 1.2 Gaia formal period sigma above 58.9973 d. Two further occasions corroborate N35 without precision centers: s94 has a post-gap low state and sharp egress near 3871.3, matching the predicted center 3869.966 plus ~1.35 d half-duration; s103 has ingress near 4163.8 and egress near 4166.3 bracketing predicted center 4165.108, with the middle lost to a gap. N34 predicts a clean null in s13 and N36 a mostly quiet s94 window near 3876.52; other nearby aliases differ from Gaia by >60 formal sigma. The Gaia B conjunction differs by 0.0007 phase. Independent TESSCut aperture of s27 gives 35.41 ppt from the same photons, and WCS difference flux peaks 0.242 pixel from the target; all Gaia neighbors within 60 arcsec are too faint under approximate G-band total-disappearance bounds.

## Limits and next check

Period is a rounded two-complete-event estimate supported by two partial occasions, conditional on N35; no calibrated period error. Other screened shallow dips are not assigned to the same eclipse kind. The WCS/neighbor assessment is bounded and uses approximate G-to-TESS flux. Obtain another complete same-kind eclipse and independent photometry for a precision ephemeris.

## Reproducibility

`raw-inspection.json` verifies the bulk JSON and each used FITS SHA-256 and records representative screening windows. `raw-windows.png` shows flagged raw windows; `orbit-context.png` and `.json` show full cached-sector SAP and Gaia conjunction predictions. These predictions are not event timings. Source packets under `../../source-packets/352438536/sources.json` carry frozen target/orbit/fold receipts. `../../shared-catalogues/target-evidence.json` holds bounded novelty evidence; a failed remote query is unknown. Scripts in this batch reproduce lead artifacts.

The result epoch BTJD 2040.0819 labels the deeper sampled eclipse kind as a provisional primary; no stellar primary or opposite eclipse kind has been established. `local-fits.json`, `cycle-coverage.json`, `alias-tests.json`, and helper attribution artifacts document the measured events, alias checks, alternative aperture and WCS difference image. The s94/s103 partial contacts corroborate recurrence but are not fitted precision centers.
