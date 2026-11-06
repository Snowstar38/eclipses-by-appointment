# Z011: TIC 157000271

Physical verdict: REFUTED. Full review completion: COMPLETE_BOUNDED. Association: OFF_TARGET_CONTAMINATION.

Real narrow eclipses at1495.63888,1513.27205,2218.45869 and2236.09264 BTJD follow17.629745 d. Independent difference images in S7 and S33 place their deficit on the bright northern star several pixels from the target. This is positive off-target evidence, not merely an uncertain centroid.

## Identity and raw observations

Exact Gaia DR3 5564100037135889024, nested G=11.928539. ../identity-audit.json verifies source population, TIC FITS headers, sector IDs and SHA256 values. Parent is fresh-band-next1000. Raw mask: finite TIME, positive finite SAP_FLUX and QUALITY=0. Lead independently inspected full-sector and deciding local raw plots.

| Sector | Center BTJD | Depth ppt | Usable timing |

|---|---:|---:|---|

| 7 | 1513.272051 | 6.16 | True |

| 7 | 1495.638884 | 6.18 | True |

| 33 | 2218.458694 | 6.38 | True |

| 34 | 2236.092643 | 4.53 | True |

## Clock and aliases

Conditional same-kind recurrence=17.629745370 d; formal local period error=0.000193881847 d. Cycle integers=[0, -1, 40, 41]; residuals(d)=[0.001872395162081375, -0.001549433821310231, -0.0012994218864150753, 0.002903833084019425]. Timing floor=max(cadence/2,0.002d); covariance precision is conditional on eclipse kind and cycle selection. Boundary or singular fits are excluded. Distinct depths/conjunction kinds were separated before fitting.

../lead-alias-covered-windows.json tests measured period, divisors2-6, doubling and Gaia period with actual quality-zero coverage. Core coverage>=75%, no large core gap and both sidebands are required. Missing data and flagged predictions are not nulls. A null requires depth+4*local point scatter < half the characteristic eclipse depth, deliberately conservative in variable/noisy sectors. Timing compatibility must also pass; a doubling cannot explain odd same-kind events merely by having no null. No exhaustive orbital posterior is claimed.

| Trial | Period d | Timing compatible | Covered | Clean nulls |

|---|---:|---|---:|---:|

| measured | 17.62974537 | True | 7 | 0 |

| divisor2 | 8.81487268 | True | 16 | 1 |

| divisor3 | 5.87658179 | True | 22 | 2 |

| divisor4 | 4.40743634 | True | 32 | 3 |

| divisor5 | 3.52594907 | True | 41 | 4 |

| divisor6 | 2.93829089 | True | 47 | 5 |

| double | 35.25949074 | False | 4 | 0 |

| Gaia | 26.84540824 | False | 6 | 1 |

## Independent reduction and ownership

helper-localization.json/png and HELPER-AUDIT.md record a fresh TESScut custom aperture, deficit image and neighbor investigation. S7/S33 are separate occasions for Z011; SAP/KSPSAP/custom extraction of one occasion reuse the same photons. Positive neighboring deficit is interpreted physically, not automatically assigned to the target. Unavailable cone queries remain unknown, not nonmatches.

## Gaia geometry

Source-specific P=26.845408243 plus/minus0.090400614 d, e=0.337661, omega=211.2886 degrees, Tp=392.916221 BTJD; mass function=0.000251188 solar masses. ../lead-gaia-covariance.json uses edge-on conjunctions and the relevant full P,e,omega,Tp correlation submatrix. Fixed-cycle local linear propagation is not a full nonlinear posterior; period equality alone does not prove association. A single event supplies no independent geometry confirmation.

## Catalogue status

The root-owned sealed ../shared-catalogues receipts provide bounded exact/source-specific matches. Physical tier is separate from novelty and claim eligibility. Known eclipsing identifications exclude novelty; failed queries remain unknown. Z009 was excluded before this exact seven-row queue and was not replaced.

## Limits and next check

The contaminating eclipsing source is not identified here. The aperture clock is not a period of the selected Gaia source.

Identify and review the northern contaminant separately.

## Evidence

lead-context.json; lead-series.json; lead-timing.json; lead-fullsectors.png; lead-raw-context.png where flagged; helper artifacts; ../lead-clocks.json; ../lead-alias-covered-windows.json; ../identity-audit.json; ../SOURCE-MANIFEST.json.
