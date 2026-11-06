# Z004: TIC 71295367

Physical verdict: P. Full review completion: COMPLETE_BOUNDED. Association: UNRESOLVED_CLOSE_BLEND. Host attribution: uncertain; claim eligibility is root owned.

Numerous sharp eclipses recur on a0.8710831 d deep-event clock across five sectors. Eighty-three covered deep-event windows contain deficits. Interleaved dips suggest a second eclipse kind; period halving and doubling require explicit odd/even geometry. Gaia20.2679 d cannot explain the train.

## Identity and provenance

Exact queue Gaia DR3 1096049957152995328; nested population Gaia G=11.991994. Raw hashes and FITS TIC/sector identities verified in ../identity-audit.json. Frozen source is fresh-band-next1000, not next400. Quality mask: finite positive SAP_FLUX, finite TIME, QUALITY=0. No discovery priority is assigned by this report.

## Raw morphology and timing

Conditional recurrence period=0.871083097 d; conditional formal period uncertainty=2.33979266e-06 d. Assumed cycles=[0, -24, -9, 386, 391, 807, 796, 808, 817, 839, 819]; residuals(d)=[0.0006945521736270166, 0.00017416192804375896, 0.00023065194864102523, -0.0005151665432094887, -0.00017232027312275022, 0.000788266529525572, -0.00032280313189403387, -0.0003458117976151698, 0.0004803604351764079, 0.00015922999273243477, -0.0004365143709037511]. These values depend on chosen kinds and integers. Duration median=0.0535 d; fitted depth median=24.36 ppt. Local trapezoid covariance has cadence/2 and0.002d error floors in clock fit; failed/boundary fits are excluded.

| Sector | Event BTJD | Depth ppt | Fit usable |
|---|---:|---:|---|
| 20 | 1867.502399 | 14.15 | True |
| 20 | 1865.767476 | 18.75 | True |
| 20 | 1864.901094 | 23.64 | True |
| 20 | 1859.675203 | 20.74 | True |
| 47 | 2605.322145 | 24.36 | True |
| 47 | 2584.415631 | 22.94 | True |
| 47 | 2597.481934 | 24.44 | True |
| 47 | 2587.899324 | 23.44 | False |
| 60 | 2941.559011 | 25.08 | True |
| 60 | 2945.914770 | 26.22 | True |
| 60 | 2960.722903 | 24.00 | False |
| 60 | 2958.110621 | 24.74 | False |
| 73 | 3308.286299 | 23.07 | True |
| 73 | 3289.121748 | 22.80 | False |
| 73 | 3298.703274 | 23.71 | True |
| 73 | 3309.156248 | 23.24 | True |
| 74 | 3316.996822 | 26.37 | True |
| 74 | 3336.160329 | 24.56 | True |
| 74 | 3318.738071 | 23.91 | True |
| 74 | 3325.707223 | 24.32 | False |

## Aliases and actual covered windows

Raw coverage audit in ../lead-alias-covered-windows.json requires quality-zero core coverage>=75%, no large core gap, and both sidebands. Flagged screen windows are not treated as nulls. The audit records per-window source hashes, depth and noise. Neighbor integer aliases were explicitly enumerated for sparse two-epoch cases; the timing_compatible field must also pass. No exhaustive period posterior is claimed.

| Trial | Period d | Covered | Clean low-depth windows |
|---|---:|---:|---:|
| measured | 0.87108310 | 83 | 0 |
| divisor2 | 0.43554155 | 166 | 3 |
| divisor3 | 0.29036103 | 244 | 157 |
| divisor4 | 0.21777077 | 320 | 152 |
| divisor5 | 0.17421662 | 400 | 267 |
| divisor6 | 0.14518052 | 486 | 314 |

## Independent reduction and localization

Independent custom TESScut3x3 aperture extraction recovers event loss=0.02009; deficit centroid offset=0.285 TESS pixels. Local baseline-minus-event image and raw extraction are in helper-localization.png/json. This is a separate reduction of the SAME photons, not a new observing occasion. Capable neighbors and limitations are addressed in helper audit receipts.

## Source-specific Gaia orbit

Gaia P=20.26789599 +/-0.03390637 d; eccentricity=0.151928; omega=347.9617 deg. ../lead-gaia-covariance.json derives edge-on conjunctions from this source's P,e,omega,Tp and full relevant Gaia covariance submatrix. Fixed-cycle local linear propagation is not a nonlinear posterior; high uncertainty and wrong Gaia orbits remain possible. Period equality alone is not an association test.

## Limits and next check

Orbital period versus alternating eclipse interval unresolved; no Gaia association or eccentricity claim; near blends remain bounded by pixel resolution.

Fit odd/even events and both kinds and obtain short-period RVs.

## Catalogue status

Root-owned ../shared-catalogues contains controlled source-specific catalogue/literature receipts. Physical verdict is separate from novelty and publication eligibility. Successful bounded nonmatches do not prove exhaustive novelty.

## Evidence

lead-context.json; lead-series.json; lead-timing.json; lead-raw-context.png; helper-localization.json/png; ../identity-audit.json; ../lead-clocks.json; ../lead-gaia-covariance.json; ../lead-alias-covered-windows.json; ../helper audit.


Gaia neighbor1096049201238750976 is9.21arcsec from target, G15.7005 versus target11.992. Relative G flux0.03285 would require about63.2% intrinsic loss in an idealized fully captured target+neighbor blend to explain the2.01% custom3x3 loss. This budget is approximate because G differs from TESS and throughput is unknown. Target WCS(5.066,5.536), neighbor(5.504,5.654), positive deficit centroid(5.315,5.675): the centroid lies toward the capable neighbor. This is not calibrated/deblended astrometry; the neighbor remains a credible alternate source. P describes real repeated aperture eclipses; the selected Gaia source is uncertain.


## Final neighbor audit

Successful Gaia DR3 cone60arcsec, exact target identity present, response SHA256 28bbdc3b50f6555078743f32ffaa7c36977c25aab82e9d59f2d41a4edde9a6d3. Nearby-source G flux budgets are idealized target+neighbor fully captured comparisons, not a comparison of intrinsic eclipse loss to a blended pixel loss; G/TESS band, aperture throughput and further sources limit them. Full table and WCS positions in helper-gaia-neighbors.json/csv.

Gaia1096049201238750976, separation9.205arcsec,G15.701, idealized intrinsic loss0.632, WCS[5.504391390750691, 5.654205146878074].

Host attribution uncertain: a capable subpixel neighbor cannot be distinguished securely. P describes repeated aperture eclipses; root decides claim eligibility under the paper standard. For Z001 the centroid shifts toward the neighbor; for Z004 similarly; for Z005 it is mildly opposite, but separation0.68pixel remains unresolved without a deblended fit.

A clean low-depth null additionally requires measured core depth+4 times sideband robust noise < half the representative primary depth. Insensitive covered windows are ambiguous, not null. This is a descriptive conservative sensitivity bound, not a calibrated detection probability.


Claim adjudication: unresolved blends do not positively identify a neighbor-owned eclipse. Root applies the paper standard to P systems with host uncertainty separately from physical review. Only Z008 has a positive off-target attribution refutation. No automatic exclusion or novelty decision is made here.
