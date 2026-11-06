# Z006: TIC 95324628

Physical verdict: P. Full review completion: COMPLETE_BOUNDED. Association: SHORT_PERIOD_BYCATCH.

Deep eclipses at2787.81866,3512.78381 and3523.14050 BTJD fit10.356645 d, including two same-kind events in S81. A shallower eclipse3525.83126 is at phase0.2598 after the primary, supporting noncircular geometry if it belongs to the same source. Gaia56.1241 d is incompatible.

## Identity and provenance

Exact queue Gaia DR3 4239611700214875904; nested population Gaia G=11.914187. Raw hashes and FITS TIC/sector identities verified in ../identity-audit.json. Frozen source is fresh-band-next1000, not next400. Quality mask: finite positive SAP_FLUX, finite TIME, QUALITY=0. No discovery priority is assigned by this report.

## Raw morphology and timing

Conditional recurrence period=10.356645350 d; conditional formal period uncertainty=0.000100459796 d. Assumed cycles=[0, 71, 70]; residuals(d)=[3.719707819982432e-06, 2.1597519662464038e-05, -2.190605437135673e-05]. These values depend on chosen kinds and integers. Duration median=0.1797 d; fitted depth median=383.67 ppt. Local trapezoid covariance has cadence/2 and0.002d error floors in clock fit; failed/boundary fits are excluded.

| Sector | Event BTJD | Depth ppt | Fit usable |
|---|---:|---:|---|
| 54 | 2787.818660 | 378.19 | True |
| 81 | 3523.140498 | 383.67 | True |
| 81 | 3512.783809 | 384.60 | True |
| 81 | 3525.831262 | 205.38 | True |

## Aliases and actual covered windows

Raw coverage audit in ../lead-alias-covered-windows.json requires quality-zero core coverage>=75%, no large core gap, and both sidebands. Flagged screen windows are not treated as nulls. The audit records per-window source hashes, depth and noise. Neighbor integer aliases were explicitly enumerated for sparse two-epoch cases; the timing_compatible field must also pass. No exhaustive period posterior is claimed.

| Trial | Period d | Covered | Clean low-depth windows |
|---|---:|---:|---:|
| measured | 10.35664535 | 3 | 0 |
| divisor2 | 5.17832267 | 6 | 3 |
| divisor3 | 3.45221512 | 9 | 6 |
| divisor4 | 2.58916134 | 12 | 9 |
| divisor5 | 2.07132907 | 14 | 11 |
| divisor6 | 1.72610756 | 17 | 14 |

## Independent reduction and localization

Independent custom TESScut3x3 aperture extraction recovers event loss=0.28744; deficit centroid offset=0.128 TESS pixels. Local baseline-minus-event image and raw extraction are in helper-localization.png/json. This is a separate reduction of the SAME photons, not a new observing occasion. Capable neighbors and limitations are addressed in helper audit receipts.

## Source-specific Gaia orbit

Gaia P=56.12410134 +/-0.02971224 d; eccentricity=0.404139; omega=201.4553 deg. ../lead-gaia-covariance.json derives edge-on conjunctions from this source's P,e,omega,Tp and full relevant Gaia covariance submatrix. Fixed-cycle local linear propagation is not a nonlinear posterior; high uncertainty and wrong Gaia orbits remain possible. Period equality alone is not an association test.

## Limits and next check

No precise independent eccentric orbit; Gaia association fails. Exact-source external RV warning in arXiv2608.06453 says FEROS & RVs inconsistent with orbit; this weakens use of Gaia and is not prior EB evidence.

Fit both kinds and obtain/reanalyse RVs at10.35665 d; verify the RV literature row.

## Catalogue status

Root-owned ../shared-catalogues contains controlled source-specific catalogue/literature receipts. Physical verdict is separate from novelty and publication eligibility. Successful bounded nonmatches do not prove exhaustive novelty.

## Evidence

lead-context.json; lead-series.json; lead-timing.json; lead-raw-context.png; helper-localization.json/png; ../identity-audit.json; ../lead-clocks.json; ../lead-gaia-covariance.json; ../lead-alias-covered-windows.json; ../helper audit.


## Final neighbor audit

Successful Gaia DR3 cone60arcsec, exact target identity present, response SHA256 dbe96d138941d57c117acb3083871005e9525ee9e0fae96e6cc0ade7a5fd364b. Nearby-source G flux budgets are idealized target+neighbor fully captured comparisons, not a comparison of intrinsic eclipse loss to a blended pixel loss; G/TESS band, aperture throughput and further sources limit them. Full table and WCS positions in helper-gaia-neighbors.json/csv.

Gaia4239611494056445184, separation2.949arcsec,G17.685, idealized intrinsic loss58.761, WCS[5.598187916297088, 6.030242954094083].


A clean low-depth null additionally requires measured core depth+4 times sideband robust noise < half the representative primary depth. Insensitive covered windows are ambiguous, not null. This is a descriptive conservative sensitivity bound, not a calibrated detection probability.


Claim adjudication: unresolved blends do not positively identify a neighbor-owned eclipse. Root applies the paper standard to P systems with host uncertainty separately from physical review. Only Z008 has a positive off-target attribution refutation. No automatic exclusion or novelty decision is made here.
