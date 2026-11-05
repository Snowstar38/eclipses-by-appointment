# R723 — TIC 241479387

**Physical verdict: PROBABLE. Bounded review completion: COMPLETE. Catalogue novelty: UNKNOWN / INCOMPLETE SCOPED CHECKS.**

Locked Gaia DR3 6070539937618487040; RA 206.06768158998938, Dec -49.4295364304687 deg; Gaia G 11.897648. Exact queue/snapshot/source identity and SHA-256 checks passed. This is one selected period-fold candidate, not a blind-search completeness or occurrence estimate.

Six sharp raw SAP eclipses recur over 114 cycles, including adjacent selected-kind cycles 65/66/67. The eclipse and clock are secure. A close capable Gaia neighbor remains unresolved by the target-centered pixel deficit, so ownership remains probable.

## Raw events and measured clock

Quality-zero finite positive QLP SAP_FLUX, with local out-of-eclipse normalization and linear-baseline trapezoid fits, gives **P = 22.0211693739 ± 0.0000261910 d**, reference BTJD **1618.56993120 ± 0.00214106**, for **selected repeating eclipse; primary/secondary identity unestablished**. These are actual fitted event centers, not the screening predictions. Median realized central depth 51.875 ppt and representative duration 0.2481 d (5.95 h) are diluted pipeline measurements.

| Sector | Selected-kind cycle | Measured BTJD | Timing allowance (d) | Realized depth (ppt) | Duration (d) | Adopted |
|---|---:|---:|---:|---:|---:|---|
| 11 | 0 | 1618.56579599 | 0.0104167 | 51.853 | 0.2439 | yes |
| 64 | 65 | 3049.94479635 | 0.0011574 | 54.344 | 0.2395 | yes |
| 65 | 66 | 3071.96823398 | 0.0011574 | 51.897 | 0.2451 | yes |
| 65 | 67 | 3093.98844454 | 0.0011574 | 55.346 | 0.2539 | yes |
| 101 | 113 | 4106.96332768 | 0.0033029 | 51.762 | 0.2775 | yes |
| 102 | 114 | 4128.98299119 | 0.0011574 | 47.402 | 0.2511 | yes |

Linear same-kind event fit, individual max(formal center covariance, half cadence), scatter-inflated covariance if reduced chi square > 1; excludes uncalibrated model/pipeline systematics. Timing allowances are not calibrated coverage intervals. The fit errors exclude model, baseline, dilution and pipeline systematics. `batch-shared/timing-sensitivity.json` retains leave-one-event-out diagnostics. `raw-events.png` shows the fitted samples; the excluded s26 model, if present, remains visible as rejected evidence.

All six accepted events use the same selected deep morphology. The full raw diagnostic fold establishes no comparable second eclipse; no upper limit on a shallower other-kind eclipse is claimed. Adjacent s 65 events and actual half-phase nulls test recurrence. The epoch does not claim to name the deeper primary.

## Recurrence, aliases and actual nulls

The selected period predicts no sensitive clean raw null. Near-baseline integer-cycle alternatives N±1 and N±2, plus half, third and double clocks, were tested using actual event centers and actual raw quality/coverage. The double-clock timing test assumes the selected events have the same kind; Gaia's independently measured spectroscopic period also favors the adopted orbital factor. This is a bounded alias check, not a mathematical exclusion of every possible period.

| Tested clock | Period (d) | Max selected-kind timing residual (d) | Timing rejected | Sensitive raw nulls |
|---|---:|---:|---|---:|
| selected | 22.02116937 | 0.0041 | False | 0 |
| half | 11.01058469 | 0.0041 | False | 4 |
| third | 7.34038979 | 0.0041 | False | 10 |
| double | 44.04233875 | 22.0210 | True | 0 |
| integer_112 | 22.41443924 | 3.9345 | True | 4 |
| integer_113 | 22.21608137 | 9.5457 | True | 4 |
| integer_115 | 21.82971474 | 9.3863 | True | 3 |
| integer_116 | 21.64152754 | 3.7946 | True | 3 |

A sensitive null requires at least 75% central cadence coverage, at least 3 clean central points, at least 4 sideband points on each side, scatter less than one-quarter of the measured event depth, and median deficit + 5×scatter/sqrt(N) below 0.4×event depth; the loss must also be below max(0.1×depth,3×scatter/sqrt(N)). Flagged/incomplete predictions are never clean nulls. The complete per-window counts and deficits are in `batch-shared/coverage-alias.json`.

Representative half null: s11 BTJD 1607.559347, 7 clean core samples, -1.010 ppt median deficit and 2.238 ppt sideband scatter.
Representative third null: s11 BTJD 1603.889152, 7 clean core samples, 0.513 ppt median deficit and 2.844 ppt sideband scatter.

## Separate extraction and source attribution

An independent custom TESScut extraction of the s 102 event at BTJD 4128.98299 reproduces the loss: central 1 x 1,3 x 3,5 x 5 apertures give 40.384,40.446,25.312 ppt. The alternative reduction is deliberately compared by its own diluted depth, not forced to the 51.875 ppt QLP median.

The s 102 difference image is concentrated at the target; its positive-deficit centroid offset is 0.139 pixel, descriptive only. The 60 arcsec Gaia census contains 71 sources. Two non-target sources remain capable under optimistic G-band full-capture assumptions at the minimum measured 25.312 ppt aperture loss: Gaia 6070540006339062784 at 8.588 arcsec (about 0.409 TESS pixel), requiring 18.85% intrinsic loss, and Gaia 6070539967673962240 at 41.794 arcsec (about 1.990 pixel), requiring 15.77%. The close neighbor cannot be cleanly separated by this broad pixel deficit. A target-like peak alone does not exclude that neighbor. Source attribution remains unresolved.

TESScut aperture extraction is an alternative reduction of the same TESS photons. It tests extraction/processing robustness and does not constitute another observing occasion. Gaia G flux ratios are optimistic capability proxies; no TESS PRF likelihood or calibrated source probability is inferred.

## Gaia orbit and physical plausibility

The source-specific SB1 solution has P = 22.0326022524 ± 0.0055244 d, e = 0.39640, omega = 331.7157 deg, K1 = 41.216 km/s, and mass function 0.12369 solar masses. The measured period differs by -0.0114329 d (-2.070 quoted Gaia sigma). Closest edge-on conjunction B predicts BTJD 1619.177792; measured minus predicted is -0.607860 d (-0.027589 phase), with source-specific linear covariance allowance 0.305553 d. The full Gaia correlation matrix is positive definite (minimum eigenvalue 0.051819).

The period and conjunction differences are approximately 2.07 and 1.99 quoted/linear Gaia sigma respectively: mild tension is retained explicitly, with no exact orbit agreement imposed. This is not a decisive contradiction to the same spectroscopic binary; future velocities could test it.
The sharp repeated deficits, finite duration and spectroscopic mass function are consistent with stellar eclipses. These checks do not determine component masses, radii or inclination precisely. The orbit comparison uses the published primary velocity and edge-on conjunction approximation. See `gaia-nss-row.json` and `batch-shared/gaia-geometry.json`.

## Catalogue status, limits and next check

The shared selected12 catalogue handoff preserves full-source Prsa and IJspeert nonmatches and a successful direct VSX response explicitly empty for this target. VSX API completeness was not independently certified. ASAS-SN and both vetted Kostov scopes remain unavailable; failed requests are unknown. Novelty remains pending, and **no new-system claim follows from this physical review**. Original bulk Gaia/SIMBAD identities and scoped outcomes remain in the sealed shared handoff.

The event is real and repeats, but a capable 8.59 arcsec Gaia neighbor prevents definitive target ownership. Aperture dilution varies strongly, and TIC 241479387 has mild roughly 2 sigma Gaia period/conjunction tension. Timing fit errors are conditional and exclude extraction/model systematics. No exhaustive all-sector characterization or Monte Carlo was performed. Novelty remains pending because scoped catalogue coverage is incomplete.

Next check: Obtain resolved eclipse photometry separating the 8.59 arcsec neighbor, and compare a new timed eclipse or velocities with the Gaia orbit.

Evidence: `measurements.json`, `raw-events.png`, `kind-fold.png`, `catalogue-evidence.json`; shared local analysis files `batch-shared/coverage-alias.json`, `batch-shared/gaia-geometry.json`, `batch-shared/source-verification.json`, `batch-shared/external-source-verification.json`, and helper artifacts named in the lead audit. No exhaustive all-event fit or Monte Carlo was required. Root alone accepts and integrates the review.
