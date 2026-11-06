# Z010: TIC 150606032

Physical verdict: P. Full review completion: COMPLETE_BOUNDED. Association: BYCATCH_GAIA_INCONSISTENT.

Broad bounded shallow eclipses recur in raw SAP at approximately18.68458 d, with another eclipse kind near phase0.39. Independent target-centered extraction recovers the S7 event. This clock is incompatible with Gaia27.42594 d. The long-baseline timing residuals reach0.0184d and several small-integer alternatives remain noise limited.

## Identity and raw observations

Exact Gaia DR3 5594800806969008896, nested G=11.87381. ../identity-audit.json verifies source population, TIC FITS headers, sector IDs and SHA256 values. Parent is fresh-band-next1000. Raw mask: finite TIME, positive finite SAP_FLUX and QUALITY=0. Lead independently inspected full-sector and deciding local raw plots.

| Sector | Center BTJD | Depth ppt | Usable timing |

|---|---:|---:|---|

| 7 | 1502.007076 | 5.17 | True |

| 7 | 1509.306523 | 3.49 | True |

| 8 | 1528.974200 | 2.06 | False |

| 34 | 2230.735750 | 5.31 | True |

| 34 | 2237.992085 | 4.18 | True |

| 34 | 2249.426141 | 4.61 | True |

| 61 | 2966.780000 | 4.62 | False |

| 61 | 2978.093678 | 6.30 | True |

## Clock and aliases

Conditional same-kind recurrence=18.684576124 d; formal local period error=0.000171922065 d. Cycle integers=[0, 39, 40, 79]; residuals(d)=[-0.01843321473825199, 0.011772120247314888, 0.017586363349892054, -0.013345512421892636]. Timing floor=max(cadence/2,0.002d); covariance precision is conditional on eclipse kind and cycle selection. Boundary or singular fits are excluded. Distinct depths/conjunction kinds were separated before fitting.

../lead-alias-covered-windows.json tests measured period, divisors2-6, doubling and Gaia period with actual quality-zero coverage. Core coverage>=75%, no large core gap and both sidebands are required. Missing data and flagged predictions are not nulls. A null requires depth+4*local point scatter < half the characteristic eclipse depth, deliberately conservative in variable/noisy sectors. Timing compatibility must also pass; a doubling cannot explain odd same-kind events merely by having no null. No exhaustive orbital posterior is claimed.

| Trial | Period d | Timing compatible | Covered | Clean nulls |

|---|---:|---|---:|---:|

| measured | 18.68457612 | True | 6 | 0 |

| divisor2 | 9.34228806 | True | 10 | 0 |

| divisor3 | 6.22819204 | True | 14 | 0 |

| divisor4 | 4.67114403 | True | 17 | 1 |

| divisor5 | 3.73691522 | True | 20 | 1 |

| divisor6 | 3.11409602 | True | 24 | 0 |

| double | 37.36915225 | False | 3 | 0 |

| Gaia | 27.42593598 | False | 2 | 0 |

## Independent reduction and ownership

helper-localization.json/png and HELPER-AUDIT.md record a fresh TESScut custom aperture, deficit image and neighbor investigation. S7/S33 are separate occasions for Z011; SAP/KSPSAP/custom extraction of one occasion reuse the same photons. Positive neighboring deficit is interpreted physically, not automatically assigned to the target. Unavailable cone queries remain unknown, not nonmatches.

## Gaia geometry

Source-specific P=27.425935976 plus/minus0.010161038 d, e=0.408708, omega=30.9501 degrees, Tp=388.804379 BTJD; mass function=0.0449948 solar masses. ../lead-gaia-covariance.json uses edge-on conjunctions and the relevant full P,e,omega,Tp correlation submatrix. Fixed-cycle local linear propagation is not a full nonlinear posterior; period equality alone does not prove association. A single event supplies no independent geometry confirmation.

## Catalogue status

The root-owned sealed ../shared-catalogues receipts provide bounded exact/source-specific matches. Physical tier is separate from novelty and claim eligibility. Known eclipsing identifications exclude novelty; failed queries remain unknown. Z009 was excluded before this exact seven-row queue and was not replaced.

## Limits and next check

Shallow variable baseline, unresolved capable neighbor capacity, and imperfect eclipse clock prevent confirmation.

Resolve neighbors and measure a new eclipse and both eclipse kinds.

## Evidence

lead-context.json; lead-series.json; lead-timing.json; lead-fullsectors.png; lead-raw-context.png where flagged; helper artifacts; ../lead-clocks.json; ../lead-alias-covered-windows.json; ../identity-audit.json; ../SOURCE-MANIFEST.json.
