# Z014: TIC 218292999

Physical verdict: P. Full review completion: COMPLETE_BOUNDED. Association: GAIA_ASSOCIATION_CONSISTENT.

Deep flat-bottomed eclipses recur in S43,S70,S71 at37.921288 d; approximately8ppt shallower events recur at a distinct phase. These are true eclipses, not heartbeat minima. Gaia37.979418 plus/minus0.049089 d differs by1.18 formal errors. Deep and shallow conjunction offsets are approximately1.1-1.7 local covariance sigma. Independent reduction and image place the deficit at the target.

## Identity and raw observations

Exact Gaia DR3 33692231730997120, nested G=11.579803. ../identity-audit.json verifies source population, TIC FITS headers, sector IDs and SHA256 values. Parent is fresh-band-next1000. Raw mask: finite TIME, positive finite SAP_FLUX and QUALITY=0. Lead independently inspected full-sector and deciding local raw plots.

| Sector | Center BTJD | Depth ppt | Usable timing |

|---|---:|---:|---|

| 43 | 2496.796282 | 78.36 | True |

| 43 | 2481.478831 | 7.20 | True |

| 44 | 2519.404447 | 7.70 | True |

| 70 | 3217.300633 | 79.36 | True |

| 71 | 3255.222130 | 79.29 | True |

| 71 | 3239.902242 | 7.97 | True |

## Clock and aliases

Conditional same-kind recurrence=37.921288113 d; formal local period error=0.000191829985 d. Cycle integers=[0, 19, 20]; residuals(d)=[1.6193993360502645e-05, -0.00010744615155999782, 0.00010207384593741153]. Timing floor=max(cadence/2,0.002d); covariance precision is conditional on eclipse kind and cycle selection. Boundary or singular fits are excluded. Distinct depths/conjunction kinds were separated before fitting.

../lead-alias-covered-windows.json tests measured period, divisors2-6, doubling and Gaia period with actual quality-zero coverage. Core coverage>=75%, no large core gap and both sidebands are required. Missing data and flagged predictions are not nulls. A null requires depth+4*local point scatter < half the characteristic eclipse depth, deliberately conservative in variable/noisy sectors. Timing compatibility must also pass; a doubling cannot explain odd same-kind events merely by having no null. No exhaustive orbital posterior is claimed.

| Trial | Period d | Timing compatible | Covered | Clean nulls |

|---|---:|---|---:|---:|

| measured | 37.92128811 | True | 3 | 0 |

| divisor2 | 18.96064406 | True | 6 | 3 |

| divisor3 | 12.64042937 | True | 7 | 4 |

| divisor4 | 9.48032203 | True | 10 | 7 |

| divisor5 | 7.58425762 | True | 13 | 10 |

| divisor6 | 6.32021469 | True | 17 | 14 |

| double | 75.84257623 | False | 2 | 0 |

| Gaia | 37.97941757 | False | 3 | 2 |

## Independent reduction and ownership

helper-localization.json/png and HELPER-AUDIT.md record a fresh TESScut custom aperture, deficit image and neighbor investigation. S7/S33 are separate occasions for Z011; SAP/KSPSAP/custom extraction of one occasion reuse the same photons. Positive neighboring deficit is interpreted physically, not automatically assigned to the target. Unavailable cone queries remain unknown, not nonmatches.

## Gaia geometry

Source-specific P=37.979417572 plus/minus0.049089435 d, e=0.241164, omega=295.1307 degrees, Tp=397.425896 BTJD; mass function=0.0353375 solar masses. ../lead-gaia-covariance.json uses edge-on conjunctions and the relevant full P,e,omega,Tp correlation submatrix. Fixed-cycle local linear propagation is not a full nonlinear posterior; period equality alone does not prove association. A single event supplies no independent geometry confirmation.

## Catalogue status

The root-owned sealed ../shared-catalogues receipts provide bounded exact/source-specific matches. Physical tier is separate from novelty and claim eligibility. Known eclipsing identifications exclude novelty; failed queries remain unknown. Z009 was excluded before this exact seven-row queue and was not replaced.

## Limits and next check

Capable unresolved neighbors remain a source-ownership limitation; no precision eccentric orbit is claimed.

Resolve neighboring sources and fit both eclipse kinds with RVs.

## Evidence

lead-context.json; lead-series.json; lead-timing.json; lead-fullsectors.png; lead-raw-context.png where flagged; helper artifacts; ../lead-clocks.json; ../lead-alias-covered-windows.json; ../identity-audit.json; ../SOURCE-MANIFEST.json.
