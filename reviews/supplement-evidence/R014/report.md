# TIC 144749615 — CONFIRMED target eclipsing binary

Full-review completion: COMPLETE. Physical verdict and novelty are separate. Forty-three primary and37 secondary detections over multiple sectors, an independent reduction, on-target prior deficit and a capable neighbour almost50arcsec away establish the target EB. A grazing/contact-shape degeneracy limits radii and eccentricity inference.

## Raw photometry and timing

All available QLP products in qlp-manifest.json were examined from SAP_FLUX with QUALITY==0, no gap trimming; flagged core counts remain in every event row. Exposure-integrated trapezoids with local polynomial baselines, red-noise inflation and grid-error floors were fitted. 43 accepted primary events in 6 sectors; median depth 36.665ppt (range34.601–38.636). T14=1.9289h, profile range1.8919–1.9658h; ingress T12=0.6751h, nominal trapezoid T23=0.5787h. Trapezoid flat duration is not physical totality for grazing events.

Primary linear ephemeris: P=2.7920366462±0.0000003597d, Tref=2501.1001829±0.0001170BTJD (reference cycle361); T0=1493.1749536. Chi2/dof=55.39/41; O-C RMS=0.536min. Errors are conditional on this baseline/shape and include fit red-noise/chi2 scaling, not all model systematics. The original resolved CSV and P/P2 were checked; all use the resolved full orbital period. Individual event values and exclusions are retained in fit-results.json.

The blind rolling-median dip census found93 threshold groups; there are zero groups deeper than half the median primary depth outside ±1.5T14 around either fitted eclipse phase. It is a detection census, not an astrophysical classification of small fluctuations. No isolated sector-wide systematic is used as deciding evidence. Maximum fitted background-correlated fake depth is 1.1885ppt; including native-unit background regression changes an individual depth by at most3.33%. Background units were not divided into normalized flux. Maximum flagged core count among accepted windows=5; rejected/partial windows are not treated as nulls.

|Sector|Mid BTJD|Timing error d|Depth ppt|Error ppt|O-C min|Core flagged|
|---|---:|---:|---:|---:|---:|---:|
|7|1495.9673345|0.0030071|37.561|0.491|0.496|0|
|7|1498.7588800|0.0030071|37.090|0.503|-0.211|0|
|7|1501.5509078|0.0030071|37.491|0.490|-0.224|0|
|7|1507.1344812|0.0034723|38.049|0.450|-0.944|0|
|7|1509.9265089|0.0034723|37.636|0.526|-0.957|0|
|7|1512.7195011|0.0034723|37.836|0.501|0.419|0|
|7|1515.5110467|0.0034723|38.636|0.470|-0.288|0|
|8|1518.3030745|0.0034722|36.582|0.459|-0.301|0|
|8|1521.0951022|0.0034722|37.522|0.470|-0.314|0|
|8|1523.8871300|0.0034722|35.970|0.406|-0.326|0|
|8|1526.6791578|0.0034722|36.133|0.454|-0.339|0|
|8|1537.8467866|0.0030070|35.584|0.416|-1.085|0|
|8|1540.6397788|0.0030070|35.036|0.496|0.291|0|
|34|2230.2725675|0.0005787|36.913|0.554|-0.087|0|
|34|2233.0641130|0.0005787|36.321|0.433|-0.795|0|
|34|2235.8571052|0.0005787|35.742|0.439|0.581|0|
|34|2238.6486508|0.0005787|37.154|0.548|-0.126|0|
|34|2244.2327063|0.0005787|37.718|0.532|-0.151|0|
|34|2247.0252163|0.0006682|35.600|0.621|0.530|3|
|34|2249.8172441|0.0005787|37.720|0.465|0.517|0|
|34|2252.6083074|0.0006044|37.014|0.531|-0.884|1|
|35|2258.1928452|0.0007577|37.205|1.365|-0.215|4|
|35|2263.7769007|0.0006682|34.601|1.052|-0.241|2|
|35|2274.9450118|0.0006044|36.003|0.509|-0.292|1|
|35|2277.7370396|0.0006339|37.060|0.504|-0.305|1|
|61|2964.5778005|0.0002411|36.624|0.508|-0.671|0|
|61|2967.3703104|0.0002411|36.872|0.527|0.011|0|
|61|2970.1623382|0.0002411|37.024|0.620|-0.002|0|
|61|2972.9543660|0.0002411|36.785|0.368|-0.015|0|
|61|2978.5384215|0.0002411|36.501|0.395|-0.040|0|
|61|2981.3309315|0.0002411|35.455|0.580|0.641|5|
|61|2984.1224771|0.0002411|37.717|0.691|-0.066|0|
|61|2986.9149871|0.0002411|36.665|0.505|0.616|0|
|88|3690.5083968|0.0002411|36.064|0.504|0.868|0|
|88|3693.3004245|0.0002411|37.459|0.772|0.855|0|
|88|3696.0924523|0.0002411|36.006|0.539|0.842|0|
|88|3698.8835157|0.0002411|36.942|0.493|-0.559|0|
|88|3701.6760256|0.0002411|36.597|0.471|0.122|0|
|88|3704.4680534|0.0002411|36.173|0.402|0.109|0|
|88|3707.2595990|0.0002411|36.074|0.478|-0.598|0|
|88|3710.0511445|0.0002411|36.096|0.426|-1.305|0|
|88|3712.8436545|0.0002411|35.346|0.714|-0.623|0|
|88|3715.6361645|0.0002411|35.649|0.481|0.058|0|

## Gaia orbit and secondary gate

Exact source5547705769022471552, solutionSB1, bit_index127, own correlation vector used. SB1 covariance order P,gamma,K1,e,omega,Tp (15 lower-triangle correlations); SB2 order P,gamma,K1,K2,e,omega,Tp (21). Gaia P=2.7919428822±0.0000425200d; photometric difference=2.205sigma. Primary association is conjunctionA; extrapolated Gaia-epoch offset=-0.028526d with Gaia-only sigma0.009918d. Individual epochs, covariance-propagated conjunction errors and timing residuals are in orbit-gates.json; the Gaia-only sigma does not include extrapolated photometric uncertainty.

Gaia e=0.033481±0.011326, omega=173.4671deg. Gaia relative other-conjunction phase=0.4788273; measured optimized phase=0.5004199. Status: supported repeat secondary. Optimized depth=5.3267±0.0838ppt; 37 individual >3sigma events among38 fitted windows. Phase was optimized, so the formal S/N is conditional and is not a blind false-alarm probability. Fixed Gaia-phase tests, every covered/partial/flagged other-conjunction window and off-phase controls are retained in orbit-gates.json; optimized individual measurements, T14/ingress/flat durations and uncertainty are in secondary-fit.json/secondary-shape.json. The fixed-primary-shape upper limit applies only at its tested phase and shape; it is not a null across the Gaia uncertainty envelope.

Secondary ephemeris P=2.7920357079±0.0000013896d, Tref=2502.4970829±0.0003789, O-C RMS3.034min, chi2/dof45.57/35.

First-order timing proxy e cos(omega)˜0.00066 versus Gaia-0.03326; this small-e proxy is approximate and uncalibrated, especially when secondary is weak. Gaia and photometric phase disagreements are retained, not converted into a false precise e claim. Numerical limb-darkened two-disk geometry was tested instead of identifying grazing trapezoid T23 with totality. Coarse best e sin(omega)=0.0500, k=0.250, impact proxy=0.900; chi2/dof=283.65/121. Fixed TIC dimensions and freely fitted flux scales make this a feasibility diagnostic, not a posterior, measured radius, or a guarantee of a unique stellar solution.

## Independent reduction and attribution

MAST product TESS-SPOC, sector34; header target=144749615, sector=34 checked. SHA256=5b5a6d339dd2ce89feb528970adc7771329bb610f3506a3f925005f5b1916ec6. At actual fitted QLP times, the independent product gives depth range32.123–40.323ppt. All per-event depths/errors, columns, URLs and target metadata are retained in independent-manifest-results.json. This is an independent reduction of TESS pixels, not an independent observatory.

Fresh ARI Gaia60arcsec cone to G<15 has1 resolved neighbours, 1 capable of this depth under a G-band flux-ratio approximation. Fainter sources cannot fully explain a ~35–40ppt dip individually. Required fractional dips are indicative because G and TESS bandpasses/aperture throughput differ.

|Gaia source|Separation arcsec|G|Required fractional dip|
|---|---:|---:|---:|
|5547699962226697216|49.62|13.202|0.292|

Prior difference image sector88, 10 events: peak on target=True; deficit/target separation5.31arcsec; deficit/light separation2.53arcsec. Duplicate old/new-schema rows are one measurement, not independent repetitions. Exact records are in parent diffrun JSONL receipts.

## Physical interpretation, archives and next check

RV mass function f(M)=0.059742Msun; assumed TIC M1=1.060Msun gives edge-on minimum M2=0.5333Msun, a=9.746Rsun. A main-sequence-radius approximation gives central T14(A/B)=3.798/3.827h compared with measured1.929h; inclination/grazing/dilution and stellar evolution remain degenerate. These approximations do not veto an attributed EB. In Gaia primary-omega convention, conjunctionA puts the spectroscopic primary behind its companion, while B puts the primary in front (positive RV is receding); flux labels alone do not uniquely assign components in a blended/grazing system.

SIMBAD exact Gaia-ID name: TYC 7125-1627-1, typeSB*. Fresh IDIA nine-catalogue cones found no target vetted EB classification; shared current Gaia vari_eclipsing_binary and ExoFOP TOI/CTOI checks are negative. Catalogue details, nearby variables, query limitations and weak web-name search are in CATALOGUE-NOTE.md. Novelty status: No vetted target EB found in queried catalogues; bibliography limited. This is not a complete publication-discovery claim.

Next nominal primary after2026-10-30: 4343.844369BTJD, subsequent 4346.636406. Other-kind nominal prediction: 4345.240650BTJD, subsequent4348.032686. These extrapolations are conditional. Refine component radii, dilution and eccentric orbit with joint RV/eclipse modeling.

Review gates are completed with their stated limitations: archives/current prior-art pass; raw primary and secondary/coverage analysis; individual timing/error and O-C; own-source Gaia covariance; independent reduction; neighbours and localization; physical feasibility; supported physical verdict. No unavailable measurement has been silently counted as a detection. Source catalogues were not edited.

## Final adversarial review details

The largest positive off-phase fixed-template control depth was 2.83ppt. Controls calibrate low-frequency/modulated residuals; they are not an exact multiple-trial probability for the optimized secondary. The repeat secondary signal is stronger than the off-phase controls and recurs in multiple sectors. 

Fixed Gaia-phase other-conjunction coverage: 56 predicted windows, status counts {'insufficient': 15, 'fit': 41}; conditional depth -0.7991ppt, control-inflated 3sigma upper value 6.7308ppt. Optimized secondary windows status counts{'insufficient': 18, 'fit': 38}; fitted secondary T14=1.8550h, T12=0.6492h, trapezoid T23=0.5565h. Uncovered windows are not counted as nulls. Full event tables and all exclusions are in the cited JSON files.
