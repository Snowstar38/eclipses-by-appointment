# Z005: TIC 92872537

Physical verdict: P. Full review completion: COMPLETE_BOUNDED. Association: UNRESOLVED_CLOSE_BLEND.

Deep flat-bottomed eclipses occur in S1,S68 and S95. The S95 eclipse at3893.70513 BTJD was absent from the original flagged-window list but is clear in raw full-sector flux and was fitted explicitly. Three occasions give32.816227 d. Timing-compatible null-free alternatives include65.63248 d; orbital doubling remains unresolved. Gaia32.80672+-0.04288 d and its propagated conjunctions agree.

## Identity and provenance

Exact queue Gaia DR3 6786929934144691328; nested population Gaia G=11.650675. Raw hashes and FITS TIC/sector identities verified in ../identity-audit.json. Frozen source is fresh-band-next1000, not next400. Quality mask: finite positive SAP_FLUX, finite TIME, QUALITY=0. No discovery priority is assigned by this report.

## Raw morphology and timing

Conditional recurrence period=32.816227290 d; conditional formal period uncertainty=9.94436958e-05 d. Assumed cycles=[0, 56, 78]; residuals(d)=[-0.0010758502094176947, 0.00014061353340366622, -0.00010095326979353558]. These values depend on chosen kinds and integers. Duration median=0.4053 d; fitted depth median=53.15 ppt. Local trapezoid covariance has cadence/2 and0.002d error floors in clock fit; failed/boundary fits are excluded.

| Sector | Event BTJD | Depth ppt | Fit usable |
|---|---:|---:|---|
| 1 | 1334.038425 | 53.15 | True |
| 1 | 1343.146481 | 33.50 | False |
| 68 | 3171.748370 | 54.79 | True |
| 95 | 3893.705129 | 46.25 | True |

## Aliases and actual covered windows

Raw coverage audit in ../lead-alias-covered-windows.json requires quality-zero core coverage>=75%, no large core gap, and both sidebands. Flagged screen windows are not treated as nulls. The audit records per-window source hashes, depth and noise. Neighbor integer aliases were explicitly enumerated for sparse two-epoch cases; the timing_compatible field must also pass. No exhaustive period posterior is claimed.

| Trial | Period d | Covered | Clean low-depth windows |
|---|---:|---:|---:|
| measured | 32.81622729 | 2 | 0 |
| divisor2 | 16.40811364 | 4 | 2 |
| divisor3 | 10.93874243 | 5 | 3 |
| divisor4 | 8.20405682 | 7 | 5 |
| divisor5 | 6.56324546 | 8 | 6 |
| divisor6 | 5.46937121 | 10 | 8 |

## Independent reduction and localization

Independent custom TESScut3x3 aperture extraction recovers event loss=0.02883; deficit centroid offset=0.108 TESS pixels. Local baseline-minus-event image and raw extraction are in helper-localization.png/json. This is a separate reduction of the SAME photons, not a new observing occasion. Capable neighbors and limitations are addressed in helper audit receipts.

## Source-specific Gaia orbit

Gaia P=32.80671947 +/-0.04287794 d; eccentricity=0.197792; omega=305.7077 deg. ../lead-gaia-covariance.json derives edge-on conjunctions from this source's P,e,omega,Tp and full relevant Gaia covariance submatrix. Fixed-cycle local linear propagation is not a nonlinear posterior; high uncertainty and wrong Gaia orbits remain possible. Period equality alone is not an association test.

## Limits and next check

Period32.81623 d is a favored recurrence; double65.63248 d remains possible if the sampled events alternate kinds. S95 strong baseline slope means local fitting is essential.

Observe a repeat separating the32.816 and65.632 d alternatives; fit secondary geometry.

## Catalogue status

Root-owned ../shared-catalogues contains controlled source-specific catalogue/literature receipts. Physical verdict is separate from novelty and publication eligibility. Successful bounded nonmatches do not prove exhaustive novelty.

## Evidence

lead-context.json; lead-series.json; lead-timing.json; lead-raw-context.png; helper-localization.json/png; ../identity-audit.json; ../lead-clocks.json; ../lead-gaia-covariance.json; ../lead-alias-covered-windows.json; ../helper audit.


## Final neighbor audit

Successful Gaia DR3 cone60arcsec, exact target identity present, response SHA256 77f8cd1367a03fe75429009235a3dc41317cde55dcce2246b548a8a5d0582481. Nearby-source G flux budgets are idealized target+neighbor fully captured comparisons, not a comparison of intrinsic eclipse loss to a blended pixel loss; G/TESS band, aperture throughput and further sources limit them. Full table and WCS positions in helper-gaia-neighbors.json/csv.

Gaia6786929929847131520, separation13.995arcsec,G12.029, idealized intrinsic loss0.070, WCS[5.7703945538541825, 4.764594303422554].

Gaia6786930690058936960, separation45.936arcsec,G13.674, idealized intrinsic loss0.215, WCS[6.722798954204998, 3.4771766934748856].

Gaia6786929556187567360, separation48.271arcsec,G15.840, idealized intrinsic loss1.395, WCS[6.313891127406068, 7.629827497676228].

Host attribution uncertain: a capable subpixel neighbor cannot be distinguished securely. P describes repeated aperture eclipses; root decides claim eligibility under the paper standard. For Z001 the centroid shifts toward the neighbor; for Z004 similarly; for Z005 it is mildly opposite, but separation0.68pixel remains unresolved without a deblended fit.

A clean low-depth null additionally requires measured core depth+4 times sideband robust noise < half the representative primary depth. Insensitive covered windows are ambiguous, not null. This is a descriptive conservative sensitivity bound, not a calibrated detection probability.


Claim adjudication: unresolved blends do not positively identify a neighbor-owned eclipse. Root applies the paper standard to P systems with host uncertainty separately from physical review. Only Z008 has a positive off-target attribution refutation. No automatic exclusion or novelty decision is made here.

Z005 target WCS(5.593,5.422), neighbor(5.770,4.765), centroid(5.498,5.472). The shift is mildly opposite the0.68pixel-separated neighbor, but no calibrated PRF fit excludes it.
