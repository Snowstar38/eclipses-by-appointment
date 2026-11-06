# Y013 TIC 277772867

Physical verdict: **CONFIRMED**. Review status: complete bounded physical review; independent helper audit in ../helper-audit.md.
Gaia DR3 6390922060982433664; nested G=11.948586. Source association: on target; Gaia orbit consistent.

Deep resolved50-64ppt eclipses in S1,S27,S94,S95,S101,S102,S104 form one22.50887d kind. Consecutive S94/S95 establish recurrence directly. Broad distorted S101 trough at4112.8 is excluded as instrumental context, distinct from clean4104.731 eclipse. S103 incomplete/edge features are excluded from timing. Small S1 feature1344.83 is not merged into the deep-kind train.

## Raw events and clock

| Sector | Kind | BTJD center | Formal timing error d | Depth ppt | Duration d | Usable |
|---|---|---:|---:|---:|---:|---|
|1|deep|1336.138804|0.000273539|62.56|0.2957|True|
|1|shallow|1344.829896|0.0044194|4.96|0.4522|True|
|27|deep|2056.423614|0.000329484|63.91|0.2933|True|
|94|deep|3879.642947|0.000293774|49.10|0.2874|True|
|94|deep|3857.133207|0.000230027|53.58|0.2953|True|
|95|deep|3902.151618|0.00019911|50.89|0.2880|True|
|101|deep|4112.810256|0.0177125|75.18|0.9000|False|
|101|deep|4104.730984|0.000289776|53.80|0.2871|True|
|102|deep|4149.749791|0.000253968|54.21|0.2868|True|
|103|deep|4172.178526|93256.3|55.08|0.4455|False|
|103|deep|4164.929001|0.00486571|34.93|0.9000|False|
|104|deep|4194.765139|0.000342759|52.54|0.2861|True|

Raw-SAP-only conditional fitted recurrence P=22.508866511d; epoch=1336.140485 BTJD; cycles=[0, 32, 112, 113, 114, 123, 125, 127]. Formal period covariance error=3.31152e-05d; scatter-inflated diagnostic=3.31152e-05d. Local timing errors use a half-cadence floor in clock fitting; these are not calibrated total uncertainty. Integer cycles and eclipse kind are explicit assumptions.

Shorter aliases P/2 through P/6 were checked in actual quality-zero raw-SAP windows (lead-alias-covered-windows.json), requiring >=75% core coverage, both sidebands and no large core gap. Missing windows are not nulls. Predicted windows contaminated by another kind are not independent nulls.

## Source and alternative reduction

S95: descriptive positive-deficit centroid within1.8 target pixels is 0.034px from target. This target-window centroid is NOT a global-source fit; for Y018 the image's global peak is far off-target and overrides that misleading restricted statistic.
Nearby stars with G fluxratio>0.01 (position/ratio inventory, not a TESS-band flux calibration): 6390921992262953216 88.6arcsec ratio0.010 xy(7.24,5.34).

TESScut custom3x3 aperture with cadence-specific outer-border background is an alternative reduction of the same photons. Saved independent depths and full-series images substantiate robustness; it is not another observing occasion. Source separation uses the difference morphology against capable neighbor coordinates, not an invalid comparison of intrinsic neighbor eclipse depth with blended pixel loss. G-band ratios are approximate diagnostics.

## Gaia geometry

Source-specific SB1 period=22.51000796d, e=0.34512, omega=130.6532deg, periastron=392.301434 BTJD; mass function=0.0296149 solar masses. Edge-on conjunctions use true anomaly90 or270deg minus omega. lead-gaia-covariance.json retains each event's actual conjunction predictions and local linear covariance from the source's corr_vec, order P,gamma,K,e,omega,Tp. Fixed-cycle linearization is not a full nonlinear posterior or inclination measurement. All source identities match queue/FITS headers; SHA256 checked before reuse.

## Limitations and next check

QLP aperture dilution changes sector depths. Fit-boundary and singular/unusable events are omitted; no precise claim about the broad S101 trough.

Characterize shallow conjunction and revised sector apertures.

## Evidence and scope

Identity audit: ../identity-audit.json; raw hashes: ../lead-source-hashes.json. Representative full raw sectors and event images were visually inspected by lead. Source receipts include TESScut requests, Gaia neighborhood success/retry records and current sector inventory. Shared catalogue/literature novelty is separately owned by root and is not inferred from physical morphology. This is a bounded representative review, not exhaustive all-sector/all-event characterization.
