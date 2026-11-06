# Z001: TIC 1269035

Physical verdict: P. Full review completion: COMPLETE_BOUNDED. Association: UNRESOLVED_CLOSE_BLEND.

Repeated narrow V eclipses at 20.48496 d, with broader shallower events between them. These are bounded eclipses rather than a smooth heartbeat. The selected Gaia period 29.0687 d fails the observed clock.

## Identity and provenance

Exact queue Gaia DR3 5645992831406897408; nested population Gaia G=11.807946. Raw hashes and FITS TIC/sector identities verified in ../identity-audit.json. Frozen source is fresh-band-next1000, not next400. Quality mask: finite positive SAP_FLUX, finite TIME, QUALITY=0. No discovery priority is assigned by this report.

## Raw morphology and timing

Conditional recurrence period=20.484956792 d; conditional formal period uncertainty=4.53143254e-05 d. Assumed cycles=[0, -1, 1, 35, 36, 37]; residuals(d)=[0.00019807603621302405, -0.001561802528158296, 0.0013884845943721302, 0.0012799416208508774, -0.0005256460754026193, -0.0007790536519678426]. These values depend on chosen kinds and integers. Duration median=0.3036 d; fitted depth median=40.77 ppt. Local trapezoid covariance has cadence/2 and0.002d error floors in clock fit; failed/boundary fits are excluded.

| Sector | Event BTJD | Depth ppt | Fit usable |
|---|---:|---:|---|
| 8 | 1520.520277 | 26.56 | False |
| 8 | 1541.001835 | 26.69 | False |
| 35 | 2278.458985 | 28.82 | False |
| 35 | 2257.979592 | 28.78 | False |
| 61 | 2985.550365 | 41.63 | True |
| 61 | 2965.063648 | 42.11 | True |
| 61 | 2975.000084 | 19.65 | False |
| 62 | 3006.036512 | 41.21 | True |
| 62 | 2995.435052 | 29.84 | False |
| 88 | 3702.524935 | 40.34 | True |
| 88 | 3712.405835 | 28.58 | False |
| 89 | 3723.008086 | 39.91 | True |
| 89 | 3743.492789 | 37.84 | True |
| 89 | 3732.891814 | 29.59 | False |

## Aliases and actual covered windows

Raw coverage audit in ../lead-alias-covered-windows.json requires quality-zero core coverage>=75%, no large core gap, and both sidebands. Flagged screen windows are not treated as nulls. The audit records per-window source hashes, depth and noise. Neighbor integer aliases were explicitly enumerated for sparse two-epoch cases; the timing_compatible field must also pass. No exhaustive period posterior is claimed.

| Trial | Period d | Covered | Clean low-depth windows |
|---|---:|---:|---:|
| measured | 20.48495679 | 6 | 0 |
| divisor2 | 10.24247840 | 12 | 6 |
| divisor3 | 6.82831893 | 20 | 14 |
| divisor4 | 5.12123920 | 22 | 16 |
| divisor5 | 4.09699136 | 31 | 25 |
| divisor6 | 3.41415947 | 35 | 29 |

## Independent reduction and localization

Independent custom TESScut3x3 aperture extraction recovers event loss=0.02915; deficit centroid offset=0.514 TESS pixels. Local baseline-minus-event image and raw extraction are in helper-localization.png/json. This is a separate reduction of the SAME photons, not a new observing occasion. Capable neighbors and limitations are addressed in helper audit receipts.

## Source-specific Gaia orbit

Gaia P=29.06869995 +/-0.01084739 d; eccentricity=0.040249; omega=97.0071 deg. ../lead-gaia-covariance.json derives edge-on conjunctions from this source's P,e,omega,Tp and full relevant Gaia covariance submatrix. Fixed-cycle local linear propagation is not a nonlinear posterior; high uncertainty and wrong Gaia orbits remain possible. Period equality alone is not an association test.

## Limits and next check

Gaia association fails; close blend and eccentric geometry remain incomplete; broader events were not used as independent same-kind timing epochs.

Resolve close companions and fit both eclipse kinds independently.

## Catalogue status

Root-owned ../shared-catalogues contains controlled source-specific catalogue/literature receipts. Physical verdict is separate from novelty and publication eligibility. Successful bounded nonmatches do not prove exhaustive novelty.

## Evidence

lead-context.json; lead-series.json; lead-timing.json; lead-raw-context.png; helper-localization.json/png; ../identity-audit.json; ../lead-clocks.json; ../lead-gaia-covariance.json; ../lead-alias-covered-windows.json; ../helper audit.


## Final neighbor audit

Successful Gaia DR3 cone60arcsec, exact target identity present, response SHA256 54615f07501b3cb09b36b1528687a83a2d1fdc49bca2f82615cb3e49ff38ab69. Nearby-source G flux budgets are idealized target+neighbor fully captured comparisons, not a comparison of intrinsic eclipse loss to a blended pixel loss; G/TESS band, aperture throughput and further sources limit them. Full table and WCS positions in helper-gaia-neighbors.json/csv.

Gaia5645992762687421440, separation14.487arcsec,G14.271, idealized intrinsic loss0.311, WCS[5.939294445161636, 5.133435016376273].

Gaia5645992797047151872, separation39.845arcsec,G14.959, idealized intrinsic loss0.560, WCS[7.0178876909062495, 6.936726716650655].

Gaia5645992831406898944, separation11.818arcsec,G16.008, idealized intrinsic loss1.425, WCS[4.956854402372851, 5.835654043450062].

Gaia5645992831406901888, separation18.539arcsec,G16.024, idealized intrinsic loss1.446, WCS[4.626672246908833, 5.53449799737853].

Host attribution uncertain: a capable subpixel neighbor cannot be distinguished securely. P describes repeated aperture eclipses; root decides claim eligibility under the paper standard. For Z001 the centroid shifts toward the neighbor; for Z004 similarly; for Z005 it is mildly opposite, but separation0.68pixel remains unresolved without a deblended fit.

A clean low-depth null additionally requires measured core depth+4 times sideband robust noise < half the representative primary depth. Insensitive covered windows are ambiguous, not null. This is a descriptive conservative sensitivity bound, not a calibrated detection probability.


Claim adjudication: unresolved blends do not positively identify a neighbor-owned eclipse. Root applies the paper standard to P systems with host uncertainty separately from physical review. Only Z008 has a positive off-target attribution refutation. No automatic exclusion or novelty decision is made here.

Z001 target WCS(5.523,5.701), neighbor(5.939,5.133), centroid(5.676,5.210). The shift points toward a capable0.70pixel-separated neighbor, but no calibrated PRF fit establishes ownership.
