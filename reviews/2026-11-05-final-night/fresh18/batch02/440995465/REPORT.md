# Y018 TIC 440995465

Physical verdict: **REFUTED**. Review status: complete bounded physical review; independent helper audit in ../helper-audit.md.
Gaia DR3 5863670570085033216; nested G=11.746747. Source association: contamination; off-target source; exact neighbor unresolved; target claim refuted.

S64/S65 contain two eclipse trains separated by roughly4.28/4.75d with same-kind9.030318d clock. Difference deficits for B-kind3053.788 and3062.822 (the displayed selected event), and A-kind3058.099 all peak near x2,y0 while target is3.34,3.32. Lower-three-row deficit centroids lie3.34-3.41 pixels from target (lead-y018-global-source.json). Both kinds belong to the off-target source. A target-centered independent aperture shows small apparent brightenings because an eclipsing border source biases background subtraction. Thus the QLP dips cannot be assigned to the selected target.

## Raw events and clock

| Sector | Kind | BTJD center | Formal timing error d | Depth ppt | Duration d | Usable |
|---|---|---:|---:|---:|---:|---|
|64|A|3049.038353|0.00268247|17.01|0.4150|True|
|64|A|3058.099248|0.0026375|17.48|0.3873|True|
|64|A|3067.112183|0.00295583|17.68|0.4196|True|
|65|A|3076.196665|0.0134804|7.88|0.6568|True|
|65|A|3085.142448|0.00441694|10.14|0.3787|True|
|65|A|3094.200729|0.00507227|12.23|0.3890|True|
|64|B|3044.757247|0.00281539|17.31|0.4954|True|
|64|B|3053.788256|0.00297356|18.63|0.5002|True|
|64|B|3062.821531|0.00367493|14.02|0.4435|True|
|65|B|3071.852461|0.00408559|11.51|0.4451|True|
|65|B|3080.876096|0.00557371|9.48|0.3998|True|
|65|B|3089.903177|0.00851174|9.06|0.4439|True|

Raw-SAP-only conditional fitted recurrence P=9.030317680d; epoch=3044.758315 BTJD; cycles=[0, 1, 2, 3, 4, 5]. Formal period covariance error=0.00109404d; scatter-inflated diagnostic=0.00109404d. Local timing errors use a half-cadence floor in clock fitting; these are not calibrated total uncertainty. Integer cycles and eclipse kind are explicit assumptions.

Shorter aliases P/2 through P/6 were checked in actual quality-zero raw-SAP windows (lead-alias-covered-windows.json), requiring >=75% core coverage, both sidebands and no large core gap. Missing windows are not nulls. Predicted windows contaminated by another kind are not independent nulls.

## Source and alternative reduction

S64: descriptive positive-deficit centroid within1.8 target pixels is 1.289px from target. This target-window centroid is NOT a global-source fit; for Y018 the image's global peak is far off-target and overrides that misleading restricted statistic.
Nearby stars with G fluxratio>0.01 (position/ratio inventory, not a TESS-band flux calibration): 5863670570085035392 8.3arcsec ratio0.136 xy(3.11,3.67); 5863670570087641856 21.5arcsec ratio0.017 xy(2.48,2.72); 5863670570085032704 22.8arcsec ratio0.042 xy(2.33,2.83); 5863670570085030400 25.4arcsec ratio0.015 xy(2.71,2.25); 5863670570085034240 31.0arcsec ratio0.011 xy(1.81,3.06); 5863670604444776960 43.1arcsec ratio0.030 xy(4.53,5.05); 5863647102381596416 48.5arcsec ratio0.104 xy(1.93,1.43); 5863647102381597312 53.2arcsec ratio0.022 xy(1.39,1.60); 5863673525009889536 55.0arcsec ratio0.018 xy(0.92,4.71); 5863647033662115072 62.9arcsec ratio0.066 xy(3.49,0.23); 5863647102381592576 64.8arcsec ratio0.158 xy(2.45,0.29); 5863650126038577152 75.3arcsec ratio0.038 xy(-0.44,3.43); 5863647033662112768 79.3arcsec ratio0.025 xy(3.72,-0.57); 5863647102381591680 79.8arcsec ratio0.038 xy(1.87,-0.28); 5863670295207110528 82.7arcsec ratio0.015 xy(5.19,-0.38); 5863673559382289536 83.3arcsec ratio0.062 xy(2.29,7.31); 5863647033662111744 84.5arcsec ratio0.012 xy(4.14,-0.79); 5863670329566859136 85.8arcsec ratio0.019 xy(7.64,3.00); 5863650126038577536 85.8arcsec ratio0.117 xy(-0.97,3.52); 5863650126038578816 86.9arcsec ratio0.114 xy(-0.99,4.00); 5863673555060451328 88.3arcsec ratio0.074 xy(3.82,7.62); 5863650126038577024 88.9arcsec ratio0.012 xy(-1.10,3.07); 5863670295207441280 89.9arcsec ratio0.017 xy(6.85,0.43).
S64: descriptive positive-deficit centroid within1.8 target pixels is 0.573px from target. This target-window centroid is NOT a global-source fit; for Y018 the image's global peak is far off-target and overrides that misleading restricted statistic.
Nearby stars with G fluxratio>0.01 (position/ratio inventory, not a TESS-band flux calibration): 5863670570085035392 8.3arcsec ratio0.136 xy(3.11,3.67); 5863670570087641856 21.5arcsec ratio0.017 xy(2.48,2.72); 5863670570085032704 22.8arcsec ratio0.042 xy(2.33,2.83); 5863670570085030400 25.4arcsec ratio0.015 xy(2.71,2.25); 5863670570085034240 31.0arcsec ratio0.011 xy(1.81,3.06); 5863670604444776960 43.1arcsec ratio0.030 xy(4.53,5.05); 5863647102381596416 48.5arcsec ratio0.104 xy(1.93,1.43); 5863647102381597312 53.2arcsec ratio0.022 xy(1.39,1.60); 5863673525009889536 55.0arcsec ratio0.018 xy(0.92,4.71); 5863647033662115072 62.9arcsec ratio0.066 xy(3.49,0.23); 5863647102381592576 64.8arcsec ratio0.158 xy(2.45,0.29); 5863650126038577152 75.3arcsec ratio0.038 xy(-0.44,3.43); 5863647033662112768 79.3arcsec ratio0.025 xy(3.72,-0.57); 5863647102381591680 79.8arcsec ratio0.038 xy(1.87,-0.28); 5863670295207110528 82.7arcsec ratio0.015 xy(5.19,-0.38); 5863673559382289536 83.3arcsec ratio0.062 xy(2.29,7.31); 5863647033662111744 84.5arcsec ratio0.012 xy(4.14,-0.79); 5863670329566859136 85.8arcsec ratio0.019 xy(7.64,3.00); 5863650126038577536 85.8arcsec ratio0.117 xy(-0.97,3.52); 5863650126038578816 86.9arcsec ratio0.114 xy(-0.99,4.00); 5863673555060451328 88.3arcsec ratio0.074 xy(3.82,7.62); 5863650126038577024 88.9arcsec ratio0.012 xy(-1.10,3.07); 5863670295207441280 89.9arcsec ratio0.017 xy(6.85,0.43).
S64: descriptive positive-deficit centroid within1.8 target pixels is 1.113px from target. This target-window centroid is NOT a global-source fit; for Y018 the image's global peak is far off-target and overrides that misleading restricted statistic.
Nearby stars with G fluxratio>0.01 (position/ratio inventory, not a TESS-band flux calibration): 5863670570085035392 8.3arcsec ratio0.136 xy(3.11,3.67); 5863670570087641856 21.5arcsec ratio0.017 xy(2.48,2.72); 5863670570085032704 22.8arcsec ratio0.042 xy(2.33,2.83); 5863670570085030400 25.4arcsec ratio0.015 xy(2.71,2.25); 5863670570085034240 31.0arcsec ratio0.011 xy(1.81,3.06); 5863670604444776960 43.1arcsec ratio0.030 xy(4.53,5.05); 5863647102381596416 48.5arcsec ratio0.104 xy(1.93,1.43); 5863647102381597312 53.2arcsec ratio0.022 xy(1.39,1.60); 5863673525009889536 55.0arcsec ratio0.018 xy(0.92,4.71); 5863647033662115072 62.9arcsec ratio0.066 xy(3.49,0.23); 5863647102381592576 64.8arcsec ratio0.158 xy(2.45,0.29); 5863650126038577152 75.3arcsec ratio0.038 xy(-0.44,3.43); 5863647033662112768 79.3arcsec ratio0.025 xy(3.72,-0.57); 5863647102381591680 79.8arcsec ratio0.038 xy(1.87,-0.28); 5863670295207110528 82.7arcsec ratio0.015 xy(5.19,-0.38); 5863673559382289536 83.3arcsec ratio0.062 xy(2.29,7.31); 5863647033662111744 84.5arcsec ratio0.012 xy(4.14,-0.79); 5863670329566859136 85.8arcsec ratio0.019 xy(7.64,3.00); 5863650126038577536 85.8arcsec ratio0.117 xy(-0.97,3.52); 5863650126038578816 86.9arcsec ratio0.114 xy(-0.99,4.00); 5863673555060451328 88.3arcsec ratio0.074 xy(3.82,7.62); 5863650126038577024 88.9arcsec ratio0.012 xy(-1.10,3.07); 5863670295207441280 89.9arcsec ratio0.017 xy(6.85,0.43).

TESScut custom3x3 aperture with cadence-specific outer-border background is an alternative reduction of the same photons. Saved independent depths and full-series images substantiate robustness; it is not another observing occasion. Source separation uses the difference morphology against capable neighbor coordinates, not an invalid comparison of intrinsic neighbor eclipse depth with blended pixel loss. G-band ratios are approximate diagnostics.

## Gaia geometry

Source-specific SB1 period=43.72627556d, e=0.44353, omega=260.0833deg, periastron=381.993375 BTJD; mass function=0.0846899 solar masses. Edge-on conjunctions use true anomaly90 or270deg minus omega. lead-gaia-covariance.json retains each event's actual conjunction predictions and local linear covariance from the source's corr_vec, order P,gamma,K,e,omega,Tp. Fixed-cycle linearization is not a full nonlinear posterior or inclination measurement. All source identities match queue/FITS headers; SHA256 checked before reuse.

## Limitations and next check

Exact contaminant identity remains blended at the7x7 edge. Gaia5863647102381592576 at64.8arcsec and x2.45,y0.29 is capable (G fluxratio0.1583), but attribution to this particular neighbor is not claimed.

Larger cutout and contaminant-centered extraction; no selected-target EB claim.

## Evidence and scope

Identity audit: ../identity-audit.json; raw hashes: ../lead-source-hashes.json. Representative full raw sectors and event images were visually inspected by lead. Source receipts include TESScut requests, Gaia neighborhood success/retry records and current sector inventory. Shared catalogue/literature novelty is separately owned by root and is not inferred from physical morphology. This is a bounded representative review, not exhaustive all-sector/all-event characterization.
