# Y010 TIC 159860053

Physical verdict: **CONFIRMED**. Review status: complete bounded physical review; independent helper audit in ../helper-audit.md.
Gaia DR3 6586467386484245632; nested G=11.974446. Source association: on target; Gaia orbit consistent.

S28 deep eclipse85.9ppt at2066.022032 and shallow10.0ppt at2076.721832 are opposite conjunction kinds. S68 has two shallow eclipses at3155.097998 and3179.070447. Current inventory adds S106: custom extraction resolves deep82.45ppt at4246.771460 and shallow9.82ppt at4257.470515. Deep and shallow recur separately; same-kind consecutive shallow events establish approximately23.964d. S106 is a new observing occasion; alternate extractions of S28 are not.

## Raw events and clock

| Sector | Kind | BTJD center | Formal timing error d | Depth ppt | Duration d | Usable |
|---|---|---:|---:|---:|---:|---|
|28|deep|2066.022032|0.000330595|85.92|0.2500|True|
|28|shallow|2076.721832|0.00278522|9.97|0.4037|True|
|68|shallow|3155.097998|0.00276547|9.70|0.4370|True|
|68|shallow|3179.070447|0.00254816|11.65|0.4387|True|

Raw-SAP-only conditional fitted recurrence P=23.964020631d; epoch=2076.721674 BTJD; cycles=[0, 45, 46]. Formal period covariance error=8.66154e-05d; scatter-inflated diagnostic=0.000194179d. Local timing errors use a half-cadence floor in clock fitting; these are not calibrated total uncertainty. Integer cycles and eclipse kind are explicit assumptions.

Shorter aliases P/2 through P/6 were checked in actual quality-zero raw-SAP windows (lead-alias-covered-windows.json), requiring >=75% core coverage, both sidebands and no large core gap. Missing windows are not nulls. Predicted windows contaminated by another kind are not independent nulls.

Final common two-kind refit including S106: P=23.964284060d, deep epoch2066.021652 and shallow epoch2076.714237 BTJD. Formal period error0.000031512d; scatter-inflated diagnostic0.000081229d, neither a calibrated total uncertainty. Separate epochs and cycle integers0,0,45,46,91,91 are saved in lead-y010-two-kind-refit.json. This supersedes the raw-SAP-only period for the result row.
S106 lead-s106-checks.json adds actual covered P/2 extras, closing the S28/S68 P/2 gap. S106 timing/depth fits are in lead-s106-timing.json. Deep event repeats91 cycles after S28; shallow kinds have their own clock.

## Source and alternative reduction

S28: descriptive positive-deficit centroid within1.8 target pixels is 0.042px from target. This target-window centroid is NOT a global-source fit; for Y018 the image's global peak is far off-target and overrides that misleading restricted statistic.
Nearby stars with G fluxratio>0.01 (position/ratio inventory, not a TESS-band flux calibration): 6586467279109256960 40.3arcsec ratio0.012 xy(1.95,2.40); 6586467592642676608 43.0arcsec ratio0.070 xy(4.04,5.27); 6586467352124505984 56.0arcsec ratio0.179 xy(6.10,2.09); 6586467794505341312 81.1arcsec ratio0.012 xy(6.98,5.34); 6586467214685552128 82.3arcsec ratio0.021 xy(2.69,-0.56).
S106: descriptive positive-deficit centroid within1.8 target pixels is 0.104px from target. This target-window centroid is NOT a global-source fit; for Y018 the image's global peak is far off-target and overrides that misleading restricted statistic.
Nearby stars with G fluxratio>0.01 (position/ratio inventory, not a TESS-band flux calibration): 6586467279109256960 40.3arcsec ratio0.012 xy(5.62,3.30); 6586467592642676608 43.0arcsec ratio0.070 xy(2.09,2.61); 6586467352124505984 56.0arcsec ratio0.179 xy(2.70,6.53); 6586467794505341312 81.1arcsec ratio0.012 xy(-0.17,4.69); 6586467214685552128 82.3arcsec ratio0.021 xy(7.07,6.09).

TESScut custom3x3 aperture with cadence-specific outer-border background is an alternative reduction of the same photons. Saved independent depths and full-series images substantiate robustness; it is not another observing occasion. Source separation uses the difference morphology against capable neighbor coordinates, not an invalid comparison of intrinsic neighbor eclipse depth with blended pixel loss. G-band ratios are approximate diagnostics.

## Gaia geometry

Source-specific SB1 period=23.95793660d, e=0.27048, omega=120.7144deg, periastron=389.818728 BTJD; mass function=0.0278456 solar masses. Edge-on conjunctions use true anomaly90 or270deg minus omega. lead-gaia-covariance.json retains each event's actual conjunction predictions and local linear covariance from the source's corr_vec, order P,gamma,K,e,omega,Tp. Fixed-cycle linearization is not a full nonlinear posterior or inclination measurement. All source identities match queue/FITS headers; SHA256 checked before reuse.

## Limitations and next check

S106 custom aperture has smooth baseline drift; local straight baseline and two-kind morphology are used. Covariance errors are conditional.

Refine two-kind ephemeris with S106 and future Gaia orbit.

## Evidence and scope

Identity audit: ../identity-audit.json; raw hashes: ../lead-source-hashes.json. Representative full raw sectors and event images were visually inspected by lead. Source receipts include TESScut requests, Gaia neighborhood success/retry records and current sector inventory. Shared catalogue/literature novelty is separately owned by root and is not inferred from physical morphology. This is a bounded representative review, not exhaustive all-sector/all-event characterization.
