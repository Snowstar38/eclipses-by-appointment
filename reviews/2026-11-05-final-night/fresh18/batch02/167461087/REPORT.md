# Y012 TIC 167461087

Physical verdict: **PROBABLE**. Review status: complete bounded physical review; independent helper audit in ../helper-audit.md.
Gaia DR3 1968869706364127616; nested G=11.626126. Source association: by-catch; localized target short-period eclipses; not Gaia45.2076d.

Many resolved narrow10-14ppt eclipses repeat throughout eight sectors. Measured event recurrence1.409178d is vastly shorter than selected Gaia45.207612d. Odd/even orbital identity remains unresolved;2.818356d is possible. Either short clock is inconsistent with the Gaia orbit.

## Raw events and clock

| Sector | Kind | BTJD center | Formal timing error d | Depth ppt | Duration d | Usable |
|---|---|---:|---:|---:|---:|---|
|15|candidate|1731.223833|0.00392368|10.83|0.1518|True|
|15|candidate|1715.719310|0.00727087|11.82|0.1704|True|
|15|candidate|1712.902462|0.00392807|10.04|0.1634|True|
|15|candidate|1728.404985|0.00166981|9.56|0.1282|True|
|16|candidate|1753.774730|0.00351978|14.11|0.1266|True|
|16|candidate|1752.364006|0.00352222|10.86|0.1531|True|
|16|candidate|1760.821348|0.00264447|9.85|0.1504|True|
|16|candidate|1745.316614|0.00193474|10.99|0.1218|True|
|55|candidate|2814.884091|0.00132257|13.23|0.1207|True|
|55|candidate|2806.431273|0.00156822|11.15|0.1041|True|
|55|candidate|2816.295401|0.00184602|12.15|0.1172|True|
|55|candidate|2799.385614|0.00293716|10.95|0.1332|True|
|56|candidate|2826.158463|0.0010621|11.84|0.1099|True|
|56|candidate|2843.073355|0.00134015|10.47|0.1052|True|
|56|candidate|2834.618964|0.00166773|12.97|0.1336|True|
|56|candidate|2850.117766|0.00230198|9.92|0.1573|True|
|75|candidate|3347.557142|0.00150345|14.20|0.1249|True|
|75|candidate|3365.878216|0.00113849|10.92|0.0996|True|
|75|candidate|3354.601011|0.00198465|9.76|0.1108|True|
|75|candidate|3348.969396|0.00167623|10.62|0.1196|True|
|76|candidate|3394.060007|0.00095346|11.52|0.1026|True|
|76|candidate|3375.741701|0.00137228|15.06|0.1229|True|
|76|candidate|3391.239494|0.00206466|11.14|0.1332|True|
|76|candidate|3392.648585|0.00170384|11.12|0.1349|True|
|82|candidate|3549.069819|0.00140194|11.08|0.1171|True|
|82|candidate|3542.021429|0.00185977|9.53|0.1525|True|
|82|candidate|3546.249906|0.00182729|11.26|0.1588|True|
|82|candidate|3540.613793|0.00178693|10.43|0.1251|True|
|83|candidate|3575.842521|0.00121518|11.00|0.1096|True|
|83|candidate|3574.432684|0.00143038|12.39|0.1237|True|
|83|candidate|3567.390324|0.00150499|13.06|0.1214|True|
|83|candidate|3580.068368|0.00161296|9.41|0.1283|True|

Raw-SAP-only conditional fitted recurrence P=1.409178017d; epoch=1712.910244 BTJD; cycles=[0, 2, 11, 13, 23, 28, 29, 34, 771, 776, 782, 783, 790, 796, 802, 807, 1160, 1161, 1165, 1173, 1180, 1191, 1192, 1193, 1297, 1298, 1301, 1303, 1316, 1321, 1322, 1325]. Formal period covariance error=1.47314e-06d; scatter-inflated diagnostic=1.56951e-06d. Local timing errors use a half-cadence floor in clock fitting; these are not calibrated total uncertainty. Integer cycles and eclipse kind are explicit assumptions.

Shorter aliases P/2 through P/6 were checked in actual quality-zero raw-SAP windows (lead-alias-covered-windows.json), requiring >=75% core coverage, both sidebands and no large core gap. Missing windows are not nulls. Predicted windows contaminated by another kind are not independent nulls.

## Source and alternative reduction

S82: descriptive positive-deficit centroid within1.8 target pixels is 0.047px from target. This target-window centroid is NOT a global-source fit; for Y018 the image's global peak is far off-target and overrides that misleading restricted statistic.
Nearby stars with G fluxratio>0.01 (position/ratio inventory, not a TESS-band flux calibration): 1968869637644635776 44.7arcsec ratio0.039 xy(4.61,5.37); 1968869637644635264 57.8arcsec ratio0.098 xy(5.36,5.81); 1968866717066864128 62.3arcsec ratio0.011 xy(2.39,5.80); 1968869775083596800 69.1arcsec ratio0.011 xy(0.53,2.37); 1968866682707124480 71.9arcsec ratio0.276 xy(3.88,6.80); 1968866717066859776 76.7arcsec ratio0.049 xy(1.71,6.19); 1968869775083607424 77.7arcsec ratio0.048 xy(0.51,1.10); 1968869946882323584 84.3arcsec ratio0.030 xy(3.38,-1.15); 1968869259687521792 85.4arcsec ratio0.015 xy(7.48,5.85).

TESScut custom3x3 aperture with cadence-specific outer-border background is an alternative reduction of the same photons. Saved independent depths and full-series images substantiate robustness; it is not another observing occasion. Source separation uses the difference morphology against capable neighbor coordinates, not an invalid comparison of intrinsic neighbor eclipse depth with blended pixel loss. G-band ratios are approximate diagnostics.

## Gaia geometry

Source-specific SB1 period=45.20761210d, e=0.02113, omega=60.4327deg, periastron=368.138310 BTJD; mass function=0.136442 solar masses. Edge-on conjunctions use true anomaly90 or270deg minus omega. lead-gaia-covariance.json retains each event's actual conjunction predictions and local linear covariance from the source's corr_vec, order P,gamma,K,e,omega,Tp. Fixed-cycle linearization is not a full nonlinear posterior or inclination measurement. All source identities match queue/FITS headers; SHA256 checked before reuse.

## Limitations and next check

Quoted clock is event recurrence, not uniquely identified full binary orbital period. Similar-depth alternating eclipses cannot be ruled out.

Odd/even morphology and spectroscopy to distinguish1.409/2.818d and potential hierarchy.

## Evidence and scope

Identity audit: ../identity-audit.json; raw hashes: ../lead-source-hashes.json. Representative full raw sectors and event images were visually inspected by lead. Source receipts include TESScut requests, Gaia neighborhood success/retry records and current sector inventory. Shared catalogue/literature novelty is separately owned by root and is not inferred from physical morphology. This is a bounded representative review, not exhaustive all-sector/all-event characterization.
