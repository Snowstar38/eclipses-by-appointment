# Z013: TIC 198590540

Physical verdict: REFUTED. Full review completion: COMPLETE_BOUNDED. Association: OFF_TARGET_CONTAMINATION.

A strong8.933048 d deep-event clock, with alternating shallow events, is real in QLP across eight sectors. The independent S80 difference image places the eclipse deficit at a bright source approximately2.46 pixels from the target, while target3x3 loss is only about17ppt versus hundreds of ppt in QLP. Selected-target eclipses are refuted.

## Identity and raw observations

Exact Gaia DR3 2116010093296554240, nested G=11.8399725. ../identity-audit.json verifies source population, TIC FITS headers, sector IDs and SHA256 values. Parent is fresh-band-next1000. Raw mask: finite TIME, positive finite SAP_FLUX and QUALITY=0. Lead independently inspected full-sector and deciding local raw plots.

| Sector | Center BTJD | Depth ppt | Usable timing |

|---|---:|---:|---|

| 25 | 1991.403966 | 357.46 | True |

| 25 | 2000.337578 | 349.20 | True |

| 25 | 1986.913989 | 150.76 | True |

| 25 | 2004.776492 | 148.43 | True |

| 26 | 2018.203992 | 393.76 | True |

| 26 | 2027.136912 | 388.42 | True |

| 26 | 2013.709933 | 165.39 | True |

| 26 | 2031.576832 | 161.45 | True |

| 53 | 2750.713114 | 327.54 | True |

| 53 | 2759.645657 | 332.48 | True |

| 53 | 2768.578636 | 332.54 | True |

| 53 | 2764.083176 | 143.13 | True |

| 54 | 2786.444233 | 339.91 | True |

| 54 | 2795.377332 | 342.67 | True |

| 54 | 2777.511459 | 341.60 | True |

| 54 | 2781.949105 | 145.59 | True |

| 74 | 3322.427314 | 344.34 | True |

| 74 | 3331.359802 | 355.36 | True |

| 74 | 3313.495610 | 349.04 | True |

| 74 | 3335.799510 | 127.58 | True |

| 79 | 3456.422729 | 345.95 | True |

| 79 | 3474.290056 | 342.42 | True |

| 79 | 3465.362199 | 338.34 | False |

| 79 | 3478.726183 | 121.71 | True |

| 80 | 3492.156465 | 463.50 | True |

| 80 | 3483.223535 | 459.61 | True |

| 80 | 3501.089360 | 480.11 | True |

| 80 | 3496.595892 | 163.26 | True |

| 81 | 3510.020780 | 339.20 | True |

| 81 | 3527.886751 | 341.43 | True |

| 81 | 3532.327751 | 122.61 | True |

| 81 | 3523.393260 | 123.76 | True |

## Clock and aliases

Conditional same-kind recurrence=8.933048015 d; formal local period error=1.73535223e-05 d. Cycle integers=[0, 1, 3, 4, 85, 86, 87, 89, 90, 88, 149, 150, 148, 164, 166, 168, 167, 169, 170, 172]; residuals(d)=[0.0004362480087820586, 0.0009998189157158777, 0.0013181560336761322, 0.001189374108435004, 0.0005029052535974188, -2.7339201551512815e-06, -7.178533678597887e-05, -0.0005703588435608253, -0.0005195138564886292, -0.00029639360627697897, -0.0003701299415297399, -0.0009299311741415295, 0.0009733115430208272, -0.00067598462510432, 0.0005557110912377539, 0.0008682022680659429, 0.000986868778909411, 0.0007152221041906159, -0.0009128723545472894, -0.0010379528448538622]. Timing floor=max(cadence/2,0.002d); covariance precision is conditional on eclipse kind and cycle selection. Boundary or singular fits are excluded. Distinct depths/conjunction kinds were separated before fitting.

../lead-alias-covered-windows.json tests measured period, divisors2-6, doubling and Gaia period with actual quality-zero coverage. Core coverage>=75%, no large core gap and both sidebands are required. Missing data and flagged predictions are not nulls. A null requires depth+4*local point scatter < half the characteristic eclipse depth, deliberately conservative in variable/noisy sectors. Timing compatibility must also pass; a doubling cannot explain odd same-kind events merely by having no null. No exhaustive orbital posterior is claimed.

| Trial | Period d | Timing compatible | Covered | Clean nulls |

|---|---:|---|---:|---:|

| measured | 8.93304801 | True | 20 | 0 |

| divisor2 | 4.46652401 | True | 41 | 21 |

| divisor3 | 2.97768267 | True | 56 | 36 |

| divisor4 | 2.23326200 | True | 84 | 64 |

| divisor5 | 1.78660960 | True | 97 | 77 |

| divisor6 | 1.48884134 | True | 115 | 95 |

| double | 17.86609603 | False | 11 | 0 |

| Gaia | 34.82502238 | False | 7 | 7 |

## Independent reduction and ownership

helper-localization.json/png and HELPER-AUDIT.md record a fresh TESScut custom aperture, deficit image and neighbor investigation. S7/S33 are separate occasions for Z011; SAP/KSPSAP/custom extraction of one occasion reuse the same photons. Positive neighboring deficit is interpreted physically, not automatically assigned to the target. Unavailable cone queries remain unknown, not nonmatches.

## Gaia geometry

Source-specific P=34.825022382 plus/minus0.033056002 d, e=0.349736, omega=328.0873 degrees, Tp=387.148016 BTJD; mass function=0.0258926 solar masses. ../lead-gaia-covariance.json uses edge-on conjunctions and the relevant full P,e,omega,Tp correlation submatrix. Fixed-cycle local linear propagation is not a full nonlinear posterior; period equality alone does not prove association. A single event supplies no independent geometry confirmation.

## Catalogue status

The root-owned sealed ../shared-catalogues receipts provide bounded exact/source-specific matches. Physical tier is separate from novelty and claim eligibility. Known eclipsing identifications exclude novelty; failed queries remain unknown. Z009 was excluded before this exact seven-row queue and was not replaced.

## Limits and next check

Contaminant identity and its novelty are unassigned. These are aperture-signal measurements only.

Identify the bright neighboring eclipsing source separately.

## Evidence

lead-context.json; lead-series.json; lead-timing.json; lead-fullsectors.png; lead-raw-context.png where flagged; helper artifacts; ../lead-clocks.json; ../lead-alias-covered-windows.json; ../identity-audit.json; ../SOURCE-MANIFEST.json.
