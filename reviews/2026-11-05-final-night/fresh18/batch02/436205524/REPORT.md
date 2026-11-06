# Y017 TIC 436205524

Physical verdict: **PROBABLE**. Review status: complete bounded physical review; independent helper audit in ../helper-audit.md.
Gaia DR3 1832432270547998592; nested G=11.937225. Source association: on target; Gaia orbit tension.

Deep111-116ppt and shallow49-52ppt eclipses form separate trains. Deep centers1695.738493,2421.209660,2444.610913,2819.045247 give23.402178d with consecutive S41 repeats. Shallow centers1685.195951,2434.060879,2808.49809 recur with the same clock at a different conjunction phase.

## Raw events and clock

| Sector | Kind | BTJD center | Formal timing error d | Depth ppt | Duration d | Usable |
|---|---|---:|---:|---:|---:|---|
|14|deep|1695.738493|0.00107599|115.69|0.2684|True|
|14|shallow|1685.195953|0.000860939|51.48|0.2573|True|
|41|deep|2421.209660|0.000248387|114.07|0.2709|True|
|41|deep|2444.610913|0.00127453|115.55|0.2706|True|
|41|shallow|2434.060879|0.000869903|48.74|0.2492|True|
|55|deep|2819.045247|0.000405821|111.24|0.2691|True|
|55|shallow|2808.498087|0.000877706|49.23|0.2459|True|

Raw-SAP-only conditional fitted recurrence P=23.402178400d; epoch=1695.741238 BTJD; cycles=[0, 31, 32, 48]. Formal period covariance error=0.000191524d; scatter-inflated diagnostic=0.000191524d. Local timing errors use a half-cadence floor in clock fitting; these are not calibrated total uncertainty. Integer cycles and eclipse kind are explicit assumptions.

Shorter aliases P/2 through P/6 were checked in actual quality-zero raw-SAP windows (lead-alias-covered-windows.json), requiring >=75% core coverage, both sidebands and no large core gap. Missing windows are not nulls. Predicted windows contaminated by another kind are not independent nulls.

## Source and alternative reduction

S41: descriptive positive-deficit centroid within1.8 target pixels is 0.189px from target. This target-window centroid is NOT a global-source fit; for Y018 the image's global peak is far off-target and overrides that misleading restricted statistic.
Nearby stars with G fluxratio>0.01 (position/ratio inventory, not a TESS-band flux calibration): 1832432270547998208 13.6arcsec ratio0.014 xy(3.75,3.63); 1832432270548004352 16.8arcsec ratio0.016 xy(2.53,3.79); 1832432270552005504 34.8arcsec ratio0.013 xy(3.37,4.99); 1832435225485513216 45.5arcsec ratio0.017 xy(1.97,5.15); 1832435122406300800 57.1arcsec ratio0.014 xy(0.86,4.77); 1832432300598754432 58.2arcsec ratio0.013 xy(5.27,5.16); 1832432236188251264 63.2arcsec ratio0.015 xy(6.17,3.76); 1832432167468784000 68.2arcsec ratio0.095 xy(0.66,1.27); 1832432236172793984 70.1arcsec ratio0.026 xy(5.92,1.35); 1832432236188240896 70.2arcsec ratio0.021 xy(5.91,1.33); 1832435225485521024 72.8arcsec ratio0.062 xy(1.83,6.57); 1832432231878175744 74.4arcsec ratio0.812 xy(6.09,1.23); 1832432098749296640 76.9arcsec ratio0.010 xy(1.79,-0.09); 1832431995670067712 81.9arcsec ratio0.055 xy(5.61,0.20); 1832432682864866304 83.7arcsec ratio0.031 xy(5.54,6.56); 1832431892590857856 85.5arcsec ratio0.019 xy(3.29,-0.80).

TESScut custom3x3 aperture with cadence-specific outer-border background is an alternative reduction of the same photons. Saved independent depths and full-series images substantiate robustness; it is not another observing occasion. Source separation uses the difference morphology against capable neighbor coordinates, not an invalid comparison of intrinsic neighbor eclipse depth with blended pixel loss. G-band ratios are approximate diagnostics.

## Gaia geometry

Source-specific SB1 period=23.37122500d, e=0.20203, omega=312.1431deg, periastron=377.317928 BTJD; mass function=0.0873488 solar masses. Edge-on conjunctions use true anomaly90 or270deg minus omega. lead-gaia-covariance.json retains each event's actual conjunction predictions and local linear covariance from the source's corr_vec, order P,gamma,K,e,omega,Tp. Fixed-cycle linearization is not a full nonlinear posterior or inclination measurement. All source identities match queue/FITS headers; SHA256 checked before reuse.

## Limitations and next check

Gaia23.371225d differs by3.46 formal sigma; source-specific conjunction residuals grow to3.301d with sigma0.993d. Real target eclipses are established, but spectroscopic association is not fully passed.

Updated radial velocities/orbit to resolve Gaia discrepancy and physical hierarchy.

## Evidence and scope

Identity audit: ../identity-audit.json; raw hashes: ../lead-source-hashes.json. Representative full raw sectors and event images were visually inspected by lead. Source receipts include TESScut requests, Gaia neighborhood success/retry records and current sector inventory. Shared catalogue/literature novelty is separately owned by root and is not inferred from physical morphology. This is a bounded representative review, not exhaustive all-sector/all-event characterization.
