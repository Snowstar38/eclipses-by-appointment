# Y011 TIC 162437782

Physical verdict: **CONFIRMED**. Review status: complete bounded physical review; independent helper audit in ../helper-audit.md.
Gaia DR3 5374745202619704832; nested G=11.620594. Source association: on target; broadly Gaia consistent.

Resolved flat-bottom23ppt eclipses recur in S10,S36,S63,S90,S99 over2479.86d. Same-kind timing cycles0,19,38,58,66 establish37.57349d. A bounded full integer-alias audit over0.5-100d with intermediate residual tolerance0.06d tested75 timing-compatible periods;74 produce actual covered clean nulls and only37.57368d remains.

## Raw events and clock

| Sector | Kind | BTJD center | Formal timing error d | Depth ppt | Duration d | Usable |
|---|---|---:|---:|---:|---:|---|
|10|candidate|1589.509305|0.00247925|23.18|0.3873|True|
|36|candidate|2303.416800|0.00220182|22.31|0.3779|True|
|63|candidate|3017.315973|0.00142541|22.78|0.3785|True|
|90|candidate|3768.785005|0.00134421|23.34|0.3780|True|
|99|candidate|4069.372128|0.00112704|18.95|0.3836|True|

Raw-SAP-only conditional fitted recurrence P=37.573488584d; epoch=1589.522389 BTJD; cycles=[0, 19, 38, 58, 66]. Formal period covariance error=5.19309e-05d; scatter-inflated diagnostic=5.19309e-05d. Local timing errors use a half-cadence floor in clock fitting; these are not calibrated total uncertainty. Integer cycles and eclipse kind are explicit assumptions.

Shorter aliases P/2 through P/6 were checked in actual quality-zero raw-SAP windows (lead-alias-covered-windows.json), requiring >=75% core coverage, both sidebands and no large core gap. Missing windows are not nulls. Predicted windows contaminated by another kind are not independent nulls.

## Source and alternative reduction

S90: descriptive positive-deficit centroid within1.8 target pixels is 0.054px from target. This target-window centroid is NOT a global-source fit; for Y018 the image's global peak is far off-target and overrides that misleading restricted statistic.
Nearby stars with G fluxratio>0.01 (position/ratio inventory, not a TESS-band flux calibration): 5374745374418398592 73.9arcsec ratio0.429 xy(-0.17,5.35); 5374745133900231808 76.1arcsec ratio0.035 xy(5.59,6.35).

TESScut custom3x3 aperture with cadence-specific outer-border background is an alternative reduction of the same photons. Saved independent depths and full-series images substantiate robustness; it is not another observing occasion. Source separation uses the difference morphology against capable neighbor coordinates, not an invalid comparison of intrinsic neighbor eclipse depth with blended pixel loss. G-band ratios are approximate diagnostics.

## Gaia geometry

Source-specific SB1 period=37.72301576d, e=0.36262, omega=285.9319deg, periastron=374.009175 BTJD; mass function=0.0156039 solar masses. Edge-on conjunctions use true anomaly90 or270deg minus omega. lead-gaia-covariance.json retains each event's actual conjunction predictions and local linear covariance from the source's corr_vec, order P,gamma,K,e,omega,Tp. Fixed-cycle linearization is not a full nonlinear posterior or inclination measurement. All source identities match queue/FITS headers; SHA256 checked before reuse.

## Limitations and next check

Gaia period is37.72302d: photometric difference is1.96 Gaia formal sigma. Gaia conjunction covariance is broad; no precision orbital refinement is claimed.

Later repeated events and revised spectroscopic orbit.

## Evidence and scope

Identity audit: ../identity-audit.json; raw hashes: ../lead-source-hashes.json. Representative full raw sectors and event images were visually inspected by lead. Source receipts include TESScut requests, Gaia neighborhood success/retry records and current sector inventory. Shared catalogue/literature novelty is separately owned by root and is not inferred from physical morphology. This is a bounded representative review, not exhaustive all-sector/all-event characterization.
