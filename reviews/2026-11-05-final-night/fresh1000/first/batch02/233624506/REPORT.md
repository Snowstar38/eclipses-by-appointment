# Z015: TIC 233624506

Physical verdict: C. Full review completion: COMPLETE_BOUNDED. Association: GAIA_ASSOCIATION_CONSISTENT.

Deep approximately117ppt V-shaped eclipses recur from S14 through S86 on29.006333 d. Shallower approximately40ppt events recur at phase0.5704 after the deep events. The two kinds support noncircular geometry if co-spatial. Gaia28.998850 plus/minus0.008708 d and both source-specific conjunctions agree. Independent custom extraction and difference image recover target-centered loss.

## Identity and raw observations

Exact Gaia DR3 2253708741967579264, nested G=11.70532. ../identity-audit.json verifies source population, TIC FITS headers, sector IDs and SHA256 values. Parent is fresh-band-next1000. Raw mask: finite TIME, positive finite SAP_FLUX and QUALITY=0. Lead independently inspected full-sector and deciding local raw plots.

| Sector | Center BTJD | Depth ppt | Usable timing |

|---|---:|---:|---|

| 14 | 1694.499141 | 118.13 | True |

| 80 | 3492.895025 | 116.64 | True |

| 80 | 3480.435556 | 38.91 | True |

| 81 | 3521.898791 | 119.87 | True |

| 81 | 3509.438911 | 41.41 | True |

| 82 | 3550.904963 | 116.95 | True |

| 82 | 3538.444942 | 39.24 | True |

| 84 | 3608.917856 | 119.06 | True |

| 85 | 3625.463291 | 42.37 | True |

| 86 | 3637.925187 | 94.82 | True |

| 86 | 3654.471066 | 44.44 | True |

## Clock and aliases

Conditional same-kind recurrence=29.006333136 d; formal local period error=0.000153860774 d. Cycle integers=[0, 62, 63, 64, 66, 67]; residuals(d)=[-0.001359279617190623, 0.0018702550332818646, -0.0006969596115595778, -0.0008583846051806177, -0.000631045906629879, 0.0003662432573037222]. Timing floor=max(cadence/2,0.002d); covariance precision is conditional on eclipse kind and cycle selection. Boundary or singular fits are excluded. Distinct depths/conjunction kinds were separated before fitting.

../lead-alias-covered-windows.json tests measured period, divisors2-6, doubling and Gaia period with actual quality-zero coverage. Core coverage>=75%, no large core gap and both sidebands are required. Missing data and flagged predictions are not nulls. A null requires depth+4*local point scatter < half the characteristic eclipse depth, deliberately conservative in variable/noisy sectors. Timing compatibility must also pass; a doubling cannot explain odd same-kind events merely by having no null. No exhaustive orbital posterior is claimed.

| Trial | Period d | Timing compatible | Covered | Clean nulls |

|---|---:|---|---:|---:|

| measured | 29.00633314 | True | 6 | 0 |

| divisor2 | 14.50316657 | True | 11 | 5 |

| divisor3 | 9.66877771 | True | 19 | 13 |

| divisor4 | 7.25158328 | True | 24 | 18 |

| divisor5 | 5.80126663 | True | 31 | 25 |

| divisor6 | 4.83438886 | True | 37 | 31 |

| double | 58.01266627 | False | 4 | 0 |

| Gaia | 28.99885013 | False | 6 | 5 |

## Independent reduction and ownership

helper-localization.json/png and HELPER-AUDIT.md record a fresh TESScut custom aperture, deficit image and neighbor investigation. S7/S33 are separate occasions for Z011; SAP/KSPSAP/custom extraction of one occasion reuse the same photons. Positive neighboring deficit is interpreted physically, not automatically assigned to the target. Unavailable cone queries remain unknown, not nonmatches.

## Gaia geometry

Source-specific P=28.998850132 plus/minus0.008708183 d, e=0.128498, omega=35.5502 degrees, Tp=385.771586 BTJD; mass function=0.109894 solar masses. ../lead-gaia-covariance.json uses edge-on conjunctions and the relevant full P,e,omega,Tp correlation submatrix. Fixed-cycle local linear propagation is not a full nonlinear posterior; period equality alone does not prove association. A single event supplies no independent geometry confirmation.

## Catalogue status

The root-owned sealed ../shared-catalogues receipts provide bounded exact/source-specific matches. Physical tier is separate from novelty and claim eligibility. Known eclipsing identifications exclude novelty; failed queries remain unknown. Z009 was excluded before this exact seven-row queue and was not replaced.

## Limits and next check

No concrete capable catalogued neighbor found within60arcsec; the2.4arcsec neighbor would require about81.75 intrinsic fractional loss under the idealized flux approximation. Bandpass and throughput remain approximate and arbitrarily close companions cannot be excluded. S86 has a strong baseline discontinuity and is locally fitted.

Resolve neighboring sources and obtain additional RV and two-kind timings.

## Evidence

lead-context.json; lead-series.json; lead-timing.json; lead-fullsectors.png; lead-raw-context.png where flagged; helper artifacts; ../lead-clocks.json; ../lead-alias-covered-windows.json; ../identity-audit.json; ../SOURCE-MANIFEST.json.
