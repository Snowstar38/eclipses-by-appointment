# Z003: TIC 34308477

Physical verdict: PLAUSIBLE. Full review completion: COMPLETE_BOUNDED. Association: GAIA_ASSOCIATION_POSSIBLE.

Two genuine eclipses occur at1442.69724 and2182.44887 BTJD. Their separation739.75163 d admits many integer-cycle aliases. The near-Gaia15-cycle value49.316776 d and its half24.658388 d survive existing coverage. The period is a candidate, not measured uniquely. Current-sector inventory includes S109; independent S109 extraction has gaps at the predicted event and provides no clean null for this value.

## Identity and provenance

Exact queue Gaia DR3 3192336529831629056; nested population Gaia G=11.650722. Raw hashes and FITS TIC/sector identities verified in ../identity-audit.json. Frozen source is fresh-band-next1000, not next400. Quality mask: finite positive SAP_FLUX, finite TIME, QUALITY=0. No discovery priority is assigned by this report.

## Raw morphology and timing

Conditional recurrence period=49.316775524 d; conditional formal period uncertainty=0.000732007282 d. Assumed cycles=[0, 15]; residuals(d)=[-1.5916157281026244e-12, -4.547473508864641e-13]. These values depend on chosen kinds and integers. Duration median=0.2673 d; fitted depth median=40.68 ppt. Local trapezoid covariance has cadence/2 and0.002d error floors in clock fit; failed/boundary fits are excluded.

| Sector | Event BTJD | Depth ppt | Fit usable |
|---|---:|---:|---|
| 5 | 1442.697237 | 43.55 | True |
| 32 | 2182.448870 | 37.82 | True |

## Aliases and actual covered windows

Raw coverage audit in ../lead-alias-covered-windows.json requires quality-zero core coverage>=75%, no large core gap, and both sidebands. Flagged screen windows are not treated as nulls. The audit records per-window source hashes, depth and noise. Neighbor integer aliases were explicitly enumerated for sparse two-epoch cases; the timing_compatible field must also pass. No exhaustive period posterior is claimed.

| Trial | Period d | Covered | Clean low-depth windows |
|---|---:|---:|---:|
| measured | 49.31677552 | 2 | 0 |
| divisor2 | 24.65838776 | 2 | 0 |
| divisor3 | 16.43892517 | 4 | 2 |
| divisor4 | 12.32919388 | 4 | 2 |
| divisor5 | 9.86335510 | 5 | 3 |
| divisor6 | 8.21946259 | 5 | 3 |

## Independent reduction and localization

Independent custom TESScut3x3 aperture extraction recovers event loss=0.04252; deficit centroid offset=0.125 TESS pixels. Local baseline-minus-event image and raw extraction are in helper-localization.png/json. This is a separate reduction of the SAME photons, not a new observing occasion. Capable neighbors and limitations are addressed in helper audit receipts.

## Source-specific Gaia orbit

Gaia P=49.19877862 +/-0.08598016 d; eccentricity=0.303881; omega=9.8010 deg. ../lead-gaia-covariance.json derives edge-on conjunctions from this source's P,e,omega,Tp and full relevant Gaia covariance submatrix. Fixed-cycle local linear propagation is not a nonlinear posterior; high uncertainty and wrong Gaia orbits remain possible. Period equality alone is not an association test.

## Limits and next check

Only two same-kind occasions; many aliases remain. Gaia conjunction offsets2.406+-2.523 and4.176+-3.746 d are consistent but cannot select the clock alone.

Acquire a predicted eclipse at a time separating49.3168 and competing integer aliases.

## Catalogue status

Root-owned ../shared-catalogues contains controlled source-specific catalogue/literature receipts. Physical verdict is separate from novelty and publication eligibility. Successful bounded nonmatches do not prove exhaustive novelty.

## Evidence

lead-context.json; lead-series.json; lead-timing.json; lead-raw-context.png; helper-localization.json/png; ../identity-audit.json; ../lead-clocks.json; ../lead-gaia-covariance.json; ../lead-alias-covered-windows.json; ../helper audit.


## Final neighbor audit

Successful Gaia DR3 cone60arcsec, exact target identity present, response SHA256 79b1a1226ed90771762b5b7407947e40065facb86a054c0eb5f82507e62d8cac. Nearby-source G flux budgets are idealized target+neighbor fully captured comparisons, not a comparison of intrinsic eclipse loss to a blended pixel loss; G/TESS band, aperture throughput and further sources limit them. Full table and WCS positions in helper-gaia-neighbors.json/csv.


A clean low-depth null additionally requires measured core depth+4 times sideband robust noise < half the representative primary depth. Insensitive covered windows are ambiguous, not null. This is a descriptive conservative sensitivity bound, not a calibrated detection probability.


Claim adjudication: unresolved blends do not positively identify a neighbor-owned eclipse. Root applies the paper standard to P systems with host uncertainty separately from physical review. Only Z008 has a positive off-target attribution refutation. No automatic exclusion or novelty decision is made here.
