# R724 — TIC 421331604

**Physical verdict: CONFIRMED. Bounded review completion: COMPLETE. Catalogue novelty: UNKNOWN / INCOMPLETE SCOPED CHECKS.**

Locked Gaia DR3 2139755043329847808; RA 289.13676729847265, Dec 54.11160750199081 deg; Gaia G 11.910119. Exact queue/snapshot/source identity and SHA-256 checks passed. This is one selected period-fold candidate, not a blind-search completeness or occurrence estimate.

Five accepted deeper-eclipse midpoints establish the 22.69233-day clock, with many additional clean covered raw events. A shallower other-kind eclipse repeats at phase 0.2876. The independent extraction and target-like difference image, absence of capable nearby Gaia sources, and Gaia geometry support the selected star as an eclipsing spectroscopic binary.

## Raw events and measured clock

Quality-zero finite positive QLP SAP_FLUX, with local out-of-eclipse normalization and linear-baseline trapezoid fits, gives **P = 22.6923265655 ± 0.0000683106 d**, reference BTJD **1705.35915917 ± 0.00515015**, for **deeper selected eclipse; shallower conjunction at phase 0.28756**. These are actual fitted event centers, not the screening predictions. Median realized central depth 75.445 ppt and representative duration 0.3902 d (9.36 h) are diluted pipeline measurements.

| Sector | Selected-kind cycle | Measured BTJD | Timing allowance (d) | Realized depth (ppt) | Duration (d) | Adopted |
|---|---:|---:|---:|---:|---:|---|
| 14 | 0 | 1705.35680964 | 0.0104168 | 74.597 | 0.3855 | yes |
| 26 | 14 | 2023.07200358 | 0.0104169 | 46.874 | 0.3275 | no: Only egress is covered; unconstrained ingress and bottom make a model-dependent center/depth, excluded from ephemeris and depth summary. |
| 54 | 47 | 2771.89807436 | 0.0034723 | 76.105 | 0.3902 | yes |
| 54 | 48 | 2794.59110462 | 0.0034723 | 74.592 | 0.3816 | yes |
| 76 | 74 | 3384.59170537 | 0.0011574 | 76.135 | 0.3919 | yes |
| 83 | 82 | 3566.12960436 | 0.0011573 | 75.445 | 0.3916 | yes |

Linear same-kind event fit, individual max(formal center covariance, half cadence), scatter-inflated covariance if reduced chi square > 1; excludes uncalibrated model/pipeline systematics. Timing allowances are not calibrated coverage intervals. The fit errors exclude model, baseline, dilution and pipeline systematics. `batch-shared/timing-sensitivity.json` retains leave-one-event-out diagnostics. `raw-events.png` shows the fitted samples; the excluded s26 model, if present, remains visible as rejected evidence.

A distinct shallower eclipse is separately measured in five raw events: s14, s54, two s76 events, and s83, with central losses 8.863–9.521 ppt and phases 0.287465–0.287692. These other-kind events are excluded from the deeper-eclipse ephemeris. Their separate table and plots are in opposite-eclipse-kind.json and opposite-eclipse-kind.png. The s 26 deeper event covers only egress and is excluded from precision timing and median depth.

## Recurrence, aliases and actual nulls

The selected period predicts no sensitive clean raw null. Near-baseline integer-cycle alternatives N±1 and N±2, plus half, third and double clocks, were tested using actual event centers and actual raw quality/coverage. The double-clock timing test assumes the selected events have the same kind; Gaia's independently measured spectroscopic period also favors the adopted orbital factor. This is a bounded alias check, not a mathematical exclusion of every possible period.

| Tested clock | Period (d) | Max selected-kind timing residual (d) | Timing rejected | Sensitive raw nulls |
|---|---:|---:|---|---:|
| selected | 22.69232657 | 0.0023 | False | 0 |
| half | 11.34616328 | 0.0023 | False | 14 |
| third | 7.56410886 | 0.0023 | False | 37 |
| double | 45.38465313 | 22.6919 | True | 0 |
| integer_80 | 23.25965993 | 4.5370 | True | 16 |
| integer_81 | 22.97250364 | 9.8037 | True | 17 |
| integer_83 | 22.41894933 | 9.5707 | True | 18 |
| integer_84 | 22.15205708 | 4.3238 | True | 17 |

A sensitive null requires at least 75% central cadence coverage, at least 3 clean central points, at least 4 sideband points on each side, scatter less than one-quarter of the measured event depth, and median deficit + 5×scatter/sqrt(N) below 0.4×event depth; the loss must also be below max(0.1×depth,3×scatter/sqrt(N)). Flagged/incomplete predictions are never clean nulls. The complete per-window counts and deficits are in `batch-shared/coverage-alias.json`.

Representative half null: s14 BTJD 1694.012996, 11 clean core samples, -0.025 ppt median deficit and 0.698 ppt sideband scatter.
Representative third null: s14 BTJD 1690.230941, 12 clean core samples, -0.671 ppt median deficit and 0.754 ppt sideband scatter.

## Separate extraction and source attribution

Independent custom TESScut extraction of the s 14 deeper event at BTJD 1705.35681 reproduces the loss: central 1 x 1,3 x 3,5 x 5 apertures give 63.759,61.550,58.485 ppt. QLP alternative aperture depths 61.576/70.331/73.799 ppt test additional dilution but are not another pipeline; the custom pixel reduction supplies the independent extraction check.

The s 14 difference image follows the target-shaped pixel illumination, with a descriptive positive-deficit centroid offset 0.560 pixel. The target lies near a pixel boundary, so this scalar offset is not a calibrated source probability. All 25 Gaia sources within 60 arcsec were screened at the conservative minimum 58.485 ppt aperture loss; no non-target source is capable under optimistic G-band full-capture assumptions. The target-like deficit and the neighbor census support target attribution at this bounded review level.

TESScut aperture extraction is an alternative reduction of the same TESS photons. It tests extraction/processing robustness and does not constitute another observing occasion. Gaia G flux ratios are optimistic capability proxies; no TESS PRF likelihood or calibrated source probability is inferred.

## Gaia orbit and physical plausibility

The source-specific SB1 solution has P = 22.6954372770 ± 0.0108847 d, e = 0.45158, omega = 223.3042 deg, K1 = 29.437 km/s, and mass function 0.04261 solar masses. The measured period differs by -0.0031107 d (-0.286 quoted Gaia sigma). Closest edge-on conjunction A predicts BTJD 1705.487753; measured minus predicted is -0.128594 d (-0.005666 phase), with source-specific linear covariance allowance 0.704614 d. The full Gaia correlation matrix is positive definite (minimum eigenvalue 0.034146).

The period difference is 0.286 quoted Gaia sigma and selected-conjunction offset is 0.183 linear covariance sigma. The separate shallower eclipse nearphase 0.2876 is also consistent with the expected eccentric two-conjunction geometry. No physical contradiction is found.
The sharp repeated deficits, finite duration and spectroscopic mass function are consistent with stellar eclipses. These checks do not determine component masses, radii or inclination precisely. The orbit comparison uses the published primary velocity and edge-on conjunction approximation. See `gaia-nss-row.json` and `batch-shared/gaia-geometry.json`.

## Catalogue status, limits and next check

The shared selected12 catalogue handoff preserves full-source Prsa and IJspeert nonmatches and a successful direct VSX response explicitly empty for this target. VSX API completeness was not independently certified. ASAS-SN and both vetted Kostov scopes remain unavailable; failed requests are unknown. Novelty remains pending, and **no new-system claim follows from this physical review**. Original bulk Gaia/SIMBAD identities and scoped outcomes remain in the sealed shared handoff.

The sector 26 egress-only model is excluded from adopted timing and depth. Depths depend on aperture dilution. Pixel centroids and Gaia G-band capability proxies are descriptive rather than calibrated TESS PRF likelihoods. Timing fit errors exclude model/pipeline systematics. No exhaustive all-sector characterization or Monte Carlo was performed. Physical confirmation is separate from pending catalogue novelty.

Next check: Recover the missing scoped catalogue checks before any new-system claim; a future clean deeper eclipse can refine the selected-kind clock.

Evidence: `measurements.json`, `raw-events.png`, `kind-fold.png`, `catalogue-evidence.json`; shared local analysis files `batch-shared/coverage-alias.json`, `batch-shared/gaia-geometry.json`, `batch-shared/source-verification.json`, `batch-shared/external-source-verification.json`, and helper artifacts named in the lead audit. No exhaustive all-event fit or Monte Carlo was required. Root alone accepts and integrates the review.
