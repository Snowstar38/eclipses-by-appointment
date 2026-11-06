# Y014 TIC 332686088

Physical verdict: **PLAUSIBLE**. Review status: complete bounded physical review; independent helper audit in ../helper-audit.md.
Gaia DR3 410632546043387904; nested G=11.5612. Source association: target blend unresolved; capable2.1arcsec neighbor.

A single resolved11.7ppt event at2890.333168 in S58 is preserved in custom aperture at9.03ppt. S85 full raw sector shows no convincing repeat, but absence without a tested photometric clock is not a null. Current all-sector inventory contains only58,85.

## Raw events and clock

| Sector | Kind | BTJD center | Formal timing error d | Depth ppt | Duration d | Usable |
|---|---|---:|---:|---:|---:|---|
|58|candidate|2890.333168|0.00141251|11.66|0.1674|True|

## Source and alternative reduction

S58: descriptive positive-deficit centroid within1.8 target pixels is 0.046px from target. This target-window centroid is NOT a global-source fit; for Y018 the image's global peak is far off-target and overrides that misleading restricted statistic.
Nearby stars with G fluxratio>0.01 (position/ratio inventory, not a TESS-band flux calibration): 410629595402430336 2.1arcsec ratio0.089 xy(3.72,3.78); 410632447260716032 20.6arcsec ratio0.023 xy(2.81,4.10); 410632584699658112 49.3arcsec ratio0.020 xy(5.50,5.45); 410630007719279872 77.7arcsec ratio0.013 xy(7.43,4.39).

TESScut custom3x3 aperture with cadence-specific outer-border background is an alternative reduction of the same photons. Saved independent depths and full-series images substantiate robustness; it is not another observing occasion. Source separation uses the difference morphology against capable neighbor coordinates, not an invalid comparison of intrinsic neighbor eclipse depth with blended pixel loss. G-band ratios are approximate diagnostics.

## Gaia geometry

Source-specific SB1 period=42.22469538d, e=0.30297, omega=238.7322deg, periastron=394.229022 BTJD; mass function=0.0828691 solar masses. Edge-on conjunctions use true anomaly90 or270deg minus omega. lead-gaia-covariance.json retains each event's actual conjunction predictions and local linear covariance from the source's corr_vec, order P,gamma,K,e,omega,Tp. Fixed-cycle linearization is not a full nonlinear posterior or inclination measurement. All source identities match queue/FITS headers; SHA256 checked before reuse.

## Limitations and next check

Single event has no photometric period. Gaia410629595402430336 at2.1arcsec has approximate G fluxratio0.0887, sufficient to mimic the event and unresolved by TESS; localization is to the blend. Gaia conjunction residual2.934d versus linear sigma1.292d does not establish association.

Resolve capable close neighbor and observe a same-kind repeat; do not freeze a Gaia-period ephemeris.

## Evidence and scope

Identity audit: ../identity-audit.json; raw hashes: ../lead-source-hashes.json. Representative full raw sectors and event images were visually inspected by lead. Source receipts include TESScut requests, Gaia neighborhood success/retry records and current sector inventory. Shared catalogue/literature novelty is separately owned by root and is not inferred from physical morphology. This is a bounded representative review, not exhaustive all-sector/all-event characterization.
