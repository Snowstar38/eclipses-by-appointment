# Z002: TIC 22210159

Physical verdict: P. Full review completion: COMPLETE_BOUNDED. Association: GAIA_ASSOCIATION_TENSION.

Four deep narrow eclipses on flat baselines span S10 to S100. The eclipse clock 34.873695 d differs from Gaia34.843240 d by about4.5 formal Gaia period errors. Propagated Gaia conjunction offsets increase from0.829 to3.023 d, about3.9-4.4 local covariance sigma. Real repeated eclipses remain secure, but the Gaia geometry check fails at face value.

## Identity and provenance

Exact queue Gaia DR3 6144678735362837376; nested population Gaia G=11.5665245. Raw hashes and FITS TIC/sector identities verified in ../identity-audit.json. Frozen source is fresh-band-next1000, not next400. Quality mask: finite positive SAP_FLUX, finite TIME, QUALITY=0. No discovery priority is assigned by this report.

## Raw morphology and timing

Conditional recurrence period=34.873694641 d; conditional formal period uncertainty=6.60650139e-05 d. Assumed cycles=[0, 21, 42, 72]; residuals(d)=[-0.001599128264842875, -0.00023569210861751344, 0.00027441325846666587, -0.00013726707220484968]. These values depend on chosen kinds and integers. Duration median=0.1716 d; fitted depth median=90.84 ppt. Local trapezoid covariance has cadence/2 and0.002d error floors in clock fit; failed/boundary fits are excluded.

| Sector | Event BTJD | Depth ppt | Fit usable |
|---|---:|---:|---|
| 10 | 1584.937158 | 89.14 | True |
| 37 | 2317.286109 | 93.39 | True |
| 64 | 3049.634206 | 92.53 | True |
| 100 | 4095.844634 | 75.00 | True |

## Aliases and actual covered windows

Raw coverage audit in ../lead-alias-covered-windows.json requires quality-zero core coverage>=75%, no large core gap, and both sidebands. Flagged screen windows are not treated as nulls. The audit records per-window source hashes, depth and noise. Neighbor integer aliases were explicitly enumerated for sparse two-epoch cases; the timing_compatible field must also pass. No exhaustive period posterior is claimed.

| Trial | Period d | Covered | Clean low-depth windows |
|---|---:|---:|---:|
| measured | 34.87369464 | 3 | 0 |
| divisor2 | 17.43684732 | 5 | 2 |
| divisor3 | 11.62456488 | 9 | 6 |
| divisor4 | 8.71842366 | 12 | 9 |
| divisor5 | 6.97473893 | 20 | 17 |
| divisor6 | 5.81228244 | 19 | 16 |

## Independent reduction and localization

Independent custom TESScut3x3 aperture extraction recovers event loss=0.08544; deficit centroid offset=0.115 TESS pixels. Local baseline-minus-event image and raw extraction are in helper-localization.png/json. This is a separate reduction of the SAME photons, not a new observing occasion. Capable neighbors and limitations are addressed in helper audit receipts.

## Source-specific Gaia orbit

Gaia P=34.84324047 +/-0.00674647 d; eccentricity=0.529476; omega=82.4505 deg. ../lead-gaia-covariance.json derives edge-on conjunctions from this source's P,e,omega,Tp and full relevant Gaia covariance submatrix. Fixed-cycle local linear propagation is not a nonlinear posterior; high uncertainty and wrong Gaia orbits remain possible. Period equality alone is not an association test.

## Limits and next check

Gaia covariance is local linear and may understate orbit uncertainty; a wrong Gaia orbit or unresolved source remains possible; no independent eccentric solution is claimed.

Obtain new RVs or published RV reanalysis and two-kind eclipse geometry.

## Catalogue status

Root-owned ../shared-catalogues contains controlled source-specific catalogue/literature receipts. Physical verdict is separate from novelty and publication eligibility. Successful bounded nonmatches do not prove exhaustive novelty.

## Evidence

lead-context.json; lead-series.json; lead-timing.json; lead-raw-context.png; helper-localization.json/png; ../identity-audit.json; ../lead-clocks.json; ../lead-gaia-covariance.json; ../lead-alias-covered-windows.json; ../helper audit.


## Final neighbor audit

Successful Gaia DR3 cone60arcsec, exact target identity present, response SHA256 0d798c5ed6fe3e363711f9fa3721ecc43c198f69a122c6f111ab9e02b40cc0a1. Nearby-source G flux budgets are idealized target+neighbor fully captured comparisons, not a comparison of intrinsic eclipse loss to a blended pixel loss; G/TESS band, aperture throughput and further sources limit them. Full table and WCS positions in helper-gaia-neighbors.json/csv.


A clean low-depth null additionally requires measured core depth+4 times sideband robust noise < half the representative primary depth. Insensitive covered windows are ambiguous, not null. This is a descriptive conservative sensitivity bound, not a calibrated detection probability.


Claim adjudication: unresolved blends do not positively identify a neighbor-owned eclipse. Root applies the paper standard to P systems with host uncertainty separately from physical review. Only Z008 has a positive off-target attribution refutation. No automatic exclusion or novelty decision is made here.
