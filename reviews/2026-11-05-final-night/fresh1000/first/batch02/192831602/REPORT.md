# Z012: TIC 192831602

Physical verdict: P. Full review completion: COMPLETE_BOUNDED. Association: GAIA_ASSOCIATION_CONSISTENT.

Four narrow bounded approximately9ppt eclipses span S5,S6,S32,S87. Consecutive early events and later repeats recover39.167170 d. Gaia39.144337 plus/minus0.044364 d and source-specific conjunctions agree within propagated covariance. Custom extraction and difference image recover the event at target position.

## Identity and raw observations

Exact Gaia DR3 4809169065671083264, nested G=11.830393. ../identity-audit.json verifies source population, TIC FITS headers, sector IDs and SHA256 values. Parent is fresh-band-next1000. Raw mask: finite TIME, positive finite SAP_FLUX and QUALITY=0. Lead independently inspected full-sector and deciding local raw plots.

| Sector | Center BTJD | Depth ppt | Usable timing |

|---|---:|---:|---|

| 5 | 1447.838016 | 8.81 | True |

| 6 | 1486.999824 | 9.33 | True |

| 32 | 2192.006386 | 9.26 | True |

| 87 | 3680.360299 | 9.63 | True |

## Clock and aliases

Conditional same-kind recurrence=39.167169945 d; formal local period error=8.99317767e-05 d. Cycle integers=[0, 1, 19, 57]; residuals(d)=[0.00656698497459729, 0.001205125739943469, -0.0012918176712446439, 0.00016257417473752866]. Timing floor=max(cadence/2,0.002d); covariance precision is conditional on eclipse kind and cycle selection. Boundary or singular fits are excluded. Distinct depths/conjunction kinds were separated before fitting.

../lead-alias-covered-windows.json tests measured period, divisors2-6, doubling and Gaia period with actual quality-zero coverage. Core coverage>=75%, no large core gap and both sidebands are required. Missing data and flagged predictions are not nulls. A null requires depth+4*local point scatter < half the characteristic eclipse depth, deliberately conservative in variable/noisy sectors. Timing compatibility must also pass; a doubling cannot explain odd same-kind events merely by having no null. No exhaustive orbital posterior is claimed.

| Trial | Period d | Timing compatible | Covered | Clean nulls |

|---|---:|---|---:|---:|

| measured | 39.16716995 | True | 4 | 0 |

| divisor2 | 19.58358497 | True | 6 | 1 |

| divisor3 | 13.05572332 | True | 9 | 3 |

| divisor4 | 9.79179249 | True | 10 | 2 |

| divisor5 | 7.83343399 | True | 16 | 3 |

| divisor6 | 6.52786166 | True | 19 | 6 |

| double | 78.33433989 | False | 1 | 0 |

| Gaia | 39.14433675 | False | 4 | 0 |

## Independent reduction and ownership

helper-localization.json/png and HELPER-AUDIT.md record a fresh TESScut custom aperture, deficit image and neighbor investigation. S7/S33 are separate occasions for Z011; SAP/KSPSAP/custom extraction of one occasion reuse the same photons. Positive neighboring deficit is interpreted physically, not automatically assigned to the target. Unavailable cone queries remain unknown, not nonmatches.

## Gaia geometry

Source-specific P=39.144336749 plus/minus0.04436367 d, e=0.292702, omega=245.3058 degrees, Tp=388.009080 BTJD; mass function=0.0308552 solar masses. ../lead-gaia-covariance.json uses edge-on conjunctions and the relevant full P,e,omega,Tp correlation submatrix. Fixed-cycle local linear propagation is not a full nonlinear posterior; period equality alone does not prove association. A single event supplies no independent geometry confirmation.

## Catalogue status

The root-owned sealed ../shared-catalogues receipts provide bounded exact/source-specific matches. Physical tier is separate from novelty and claim eligibility. Known eclipsing identifications exclude novelty; failed queries remain unknown. Z009 was excluded before this exact seven-row queue and was not replaced.

## Limits and next check

Close-neighbor capacity must be resolved to confirm ownership; independent extraction reuses the same photons.

Resolve capable neighbors and obtain additional eclipse or RV measurements.

## Evidence

lead-context.json; lead-series.json; lead-timing.json; lead-fullsectors.png; lead-raw-context.png where flagged; helper artifacts; ../lead-clocks.json; ../lead-alias-covered-windows.json; ../identity-audit.json; ../SOURCE-MANIFEST.json.
