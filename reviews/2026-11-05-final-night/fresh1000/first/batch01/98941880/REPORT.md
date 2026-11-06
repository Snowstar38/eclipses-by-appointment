# Z008: TIC 98941880

Physical verdict: REFUTED. Full review completion: COMPLETE_BOUNDED. Association: OFF_TARGET_CONTAMINATION.

An eclipse train at4.3978035 d is real in QLP but the independent S90 deficit lies about3.7 pixels from the target at a bright southern source. A target-centered3x3 extraction has only about0.5 percent loss versus11 percent QLP. Difference image provides positive off-target evidence. S101 has five fully covered predicted cores with only2.0-2.6 ppt losses, showing strongly changing dilution/aperture coupling rather than stable target eclipses.

## Identity and provenance

Exact queue Gaia DR3 3487621819263620096; nested population Gaia G=11.756892. Raw hashes and FITS TIC/sector identities verified in ../identity-audit.json. Frozen source is fresh-band-next1000, not next400. Quality mask: finite positive SAP_FLUX, finite TIME, QUALITY=0. No discovery priority is assigned by this report.

## Raw morphology and timing

Conditional recurrence period=4.397803495 d; conditional formal period uncertainty=5.20580589e-06 d. Assumed cycles=[0, -1, -4, -3, 159, 158, 162, 161, 324, 326, 325, 327, 494, 492, 491, 496]; residuals(d)=[0.0006593275445538893, -0.001071828220574389, -0.0028879500475795794, -0.000658919251009138, -0.00033422254637116566, 0.0018118720363418106, -0.006189186867686658, 0.004966438441442733, -0.00010116464954990079, 0.0005610489160972065, 3.922729911209899e-05, -0.00024709076114959316, 0.0002845339804480318, -0.0004857522462771158, -0.00011349241913194419, 0.00012413387867127312]. These values depend on chosen kinds and integers. Duration median=0.2850 d; fitted depth median=43.07 ppt. Local trapezoid covariance has cadence/2 and0.002d error floors in clock fit; failed/boundary fits are excluded.

| Sector | Event BTJD | Depth ppt | Fit usable |
|---|---:|---:|---|
| 10 | 1591.177420 | 44.57 | True |
| 10 | 1586.777885 | 46.50 | True |
| 10 | 1573.582659 | 46.95 | True |
| 10 | 1577.982691 | 45.59 | True |
| 36 | 2290.427182 | 39.41 | True |
| 36 | 2286.031525 | 37.54 | True |
| 36 | 2303.614738 | 38.35 | True |
| 36 | 2299.228090 | 35.21 | True |
| 63 | 3016.064992 | 41.18 | True |
| 63 | 3024.861261 | 41.27 | True |
| 63 | 3020.462936 | 40.36 | True |
| 63 | 3029.258256 | 41.58 | True |
| 90 | 3763.691972 | 114.68 | True |
| 90 | 3754.895594 | 110.18 | True |
| 90 | 3750.498163 | 110.92 | True |
| 90 | 3772.487418 | 111.74 | True |

## Aliases and actual covered windows

Raw coverage audit in ../lead-alias-covered-windows.json requires quality-zero core coverage>=75%, no large core gap, and both sidebands. Flagged screen windows are not treated as nulls. The audit records per-window source hashes, depth and noise. Neighbor integer aliases were explicitly enumerated for sparse two-epoch cases; the timing_compatible field must also pass. No exhaustive period posterior is claimed.

| Trial | Period d | Covered | Clean low-depth windows |
|---|---:|---:|---:|
| measured | 4.39780350 | 24 | 5 |
| divisor2 | 2.19890175 | 46 | 27 |
| divisor3 | 1.46593450 | 68 | 49 |
| divisor4 | 1.09945087 | 89 | 70 |
| divisor5 | 0.87956070 | 106 | 87 |
| divisor6 | 0.73296725 | 132 | 113 |

## Independent reduction and localization

Independent custom TESScut3x3 aperture extraction recovers event loss=0.00452; deficit centroid offset=2.079 TESS pixels. Local baseline-minus-event image and raw extraction are in helper-localization.png/json. This is a separate reduction of the SAME photons, not a new observing occasion. Capable neighbors and limitations are addressed in helper audit receipts.

## Source-specific Gaia orbit

Gaia P=56.41085048 +/-0.01982885 d; eccentricity=0.226962; omega=266.2967 deg. ../lead-gaia-covariance.json derives edge-on conjunctions from this source's P,e,omega,Tp and full relevant Gaia covariance submatrix. Fixed-cycle local linear propagation is not a nonlinear posterior; high uncertainty and wrong Gaia orbits remain possible. Period equality alone is not an association test.

## Limits and next check

The contaminating source is not identified here. The measured4.3978 d clock describes the aperture signal, not the selected Gaia star.

Identify the southern eclipsing contaminant with Gaia-resolved or ground-based photometry.

## Catalogue status

Root-owned ../shared-catalogues contains controlled source-specific catalogue/literature receipts. Physical verdict is separate from novelty and publication eligibility. Successful bounded nonmatches do not prove exhaustive novelty.

## Evidence

lead-context.json; lead-series.json; lead-timing.json; lead-raw-context.png; helper-localization.json/png; ../identity-audit.json; ../lead-clocks.json; ../lead-gaia-covariance.json; ../lead-alias-covered-windows.json; ../helper audit.


## Final neighbor audit

Successful Gaia DR3 cone60arcsec, exact target identity present, response SHA256 e130fbedb05ac5baf751846a96d5a7e64268808afdd461c45bcda6feadc90deb. Nearby-source G flux budgets are idealized target+neighbor fully captured comparisons, not a comparison of intrinsic eclipse loss to a blended pixel loss; G/TESS band, aperture throughput and further sources limit them. Full table and WCS positions in helper-gaia-neighbors.json/csv.

Gaia3487621784903882368, separation51.020arcsec,G14.910, idealized intrinsic loss0.087, WCS[7.37658829253758, 7.1798197941840325].

Gaia3487621853623358976, separation22.209arcsec,G16.646, idealized intrinsic loss0.412, WCS[5.7190411471537255, 6.8178146747423884].


A clean low-depth null additionally requires measured core depth+4 times sideband robust noise < half the representative primary depth. Insensitive covered windows are ambiguous, not null. This is a descriptive conservative sensitivity bound, not a calibrated detection probability.


Claim adjudication: unresolved blends do not positively identify a neighbor-owned eclipse. Root applies the paper standard to P systems with host uncertainty separately from physical review. Only Z008 has a positive off-target attribution refutation. No automatic exclusion or novelty decision is made here.
