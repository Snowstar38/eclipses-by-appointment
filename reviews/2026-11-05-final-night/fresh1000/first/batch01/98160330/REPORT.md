# Z007: TIC 98160330

Physical verdict: C. Full review completion: COMPLETE_BOUNDED. Association: GAIA_ASSOCIATION_CONSISTENT.

Five deep eclipses span S7,S33,S34,S87,S88. Consecutive-sector events directly recover30.22345 d; shallow eclipses recur at a different phase and are not counted as primary repeats. The period agrees with Gaia30.23494+-0.01150 d. Deep-event conjunction offsets are roughly1.6-2.6 local covariance sigma, with the earliest coarse-cadence epoch least consistent. Later primary and shallow-event phases are compatible with the eccentric Gaia orbit.

## Identity and provenance

Exact queue Gaia DR3 5603463584206598784; nested population Gaia G=11.838103. Raw hashes and FITS TIC/sector identities verified in ../identity-audit.json. Frozen source is fresh-band-next1000, not next400. Quality mask: finite positive SAP_FLUX, finite TIME, QUALITY=0. No discovery priority is assigned by this report.

## Raw morphology and timing

Conditional recurrence period=30.223445611 d; conditional formal period uncertainty=5.48591028e-05 d. Assumed cycles=[0, 23, 24, 72, 73]; residuals(d)=[-0.012720623040650025, 0.000330467478306673, 0.0017541302668178105, 0.0002337462888135633, -0.00045642363829756505]. These values depend on chosen kinds and integers. Duration median=0.2387 d; fitted depth median=76.40 ppt. Local trapezoid covariance has cadence/2 and0.002d error floors in clock fit; failed/boundary fits are excluded.

| Sector | Event BTJD | Depth ppt | Fit usable |
|---|---:|---:|---|
| 7 | 1509.816140 | 67.62 | True |
| 33 | 2204.968440 | 73.89 | True |
| 34 | 2235.193309 | 76.40 | True |
| 34 | 2246.923584 | 9.11 | True |
| 61 | 2972.299235 | 9.17 | True |
| 87 | 3685.917178 | 79.78 | True |
| 88 | 3716.139934 | 76.91 | True |

## Aliases and actual covered windows

Raw coverage audit in ../lead-alias-covered-windows.json requires quality-zero core coverage>=75%, no large core gap, and both sidebands. Flagged screen windows are not treated as nulls. The audit records per-window source hashes, depth and noise. Neighbor integer aliases were explicitly enumerated for sparse two-epoch cases; the timing_compatible field must also pass. No exhaustive period posterior is claimed.

| Trial | Period d | Covered | Clean low-depth windows |
|---|---:|---:|---:|
| measured | 30.22344561 | 5 | 0 |
| divisor2 | 15.11172281 | 10 | 5 |
| divisor3 | 10.07448187 | 14 | 9 |
| divisor4 | 7.55586140 | 17 | 12 |
| divisor5 | 6.04468912 | 19 | 14 |
| divisor6 | 5.03724094 | 28 | 23 |

## Independent reduction and localization

Independent custom TESScut3x3 aperture extraction recovers event loss=0.07307; deficit centroid offset=0.130 TESS pixels. Local baseline-minus-event image and raw extraction are in helper-localization.png/json. This is a separate reduction of the SAME photons, not a new observing occasion. Capable neighbors and limitations are addressed in helper audit receipts.

## Source-specific Gaia orbit

Gaia P=30.23494332 +/-0.01150477 d; eccentricity=0.289314; omega=171.0593 deg. ../lead-gaia-covariance.json derives edge-on conjunctions from this source's P,e,omega,Tp and full relevant Gaia covariance submatrix. Fixed-cycle local linear propagation is not a nonlinear posterior; high uncertainty and wrong Gaia orbits remain possible. Period equality alone is not an association test.

## Limits and next check

Period error is a conditional local covariance, not a calibrated total precision. TESS cannot exclude arbitrarily close companions; earliest30-minute timing has0.0127 d residual.

Higher cadence primary/secondary timing and RV characterization.

## Catalogue status

Root-owned ../shared-catalogues contains controlled source-specific catalogue/literature receipts. Physical verdict is separate from novelty and publication eligibility. Successful bounded nonmatches do not prove exhaustive novelty.

## Evidence

lead-context.json; lead-series.json; lead-timing.json; lead-raw-context.png; helper-localization.json/png; ../identity-audit.json; ../lead-clocks.json; ../lead-gaia-covariance.json; ../lead-alias-covered-windows.json; ../helper audit.


## Final neighbor audit

Successful Gaia DR3 cone60arcsec, exact target identity present, response SHA256 350d82cc217a87f26931716f372336049eee755380c2fc05cab0cd8533154de3. Nearby-source G flux budgets are idealized target+neighbor fully captured comparisons, not a comparison of intrinsic eclipse loss to a blended pixel loss; G/TESS band, aperture throughput and further sources limit them. Full table and WCS positions in helper-gaia-neighbors.json/csv.

Gaia5603463618566333696, separation38.647arcsec,G13.900, idealized intrinsic loss0.561, WCS[3.3331398192122528, 4.504204180922997].

Gaia5603464374480580608, separation45.432arcsec,G15.347, idealized intrinsic loss1.923, WCS[5.406945032097273, 2.9124635682543785].

Gaia5603463515487121536, separation35.647arcsec,G15.374, idealized intrinsic loss1.970, WCS[4.2033284933155475, 6.724627973887257].

The capable neighbor38.65arcsec away is2.03pixels from target and opposite the observed small deficit-centroid displacement. The deficit peak is at target pixel(5,5), centroid(5.208,5.386) versus target(5.216,5.256). This resolved neighbor is strongly disfavored as main eclipse source. Close unresolved companions remain possible.

A clean low-depth null additionally requires measured core depth+4 times sideband robust noise < half the representative primary depth. Insensitive covered windows are ambiguous, not null. This is a descriptive conservative sensitivity bound, not a calibrated detection probability.


Claim adjudication: unresolved blends do not positively identify a neighbor-owned eclipse. Root applies the paper standard to P systems with host uncertainty separately from physical review. Only Z008 has a positive off-target attribution refutation. No automatic exclusion or novelty decision is made here.
