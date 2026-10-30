# TIC 117919258 — CONFIRMED target eclipsing binary

Full-review completion: COMPLETE. Physical verdict and novelty are separate. Four deep primary events, two supporting clean secondary events, an independent reduction and precise prior localization establish the target EB. All data are one sector; the local orbital period is useful but extrapolation to Gaia epoch or future years has appreciable uncertainty.

## Raw photometry and timing

All available QLP products in qlp-manifest.json were examined from SAP_FLUX with QUALITY==0, no gap trimming; flagged core counts remain in every event row. Exposure-integrated trapezoids with local polynomial baselines, red-noise inflation and grid-error floors were fitted. 4 accepted primary events in 1 sectors; median depth 37.161ppt (range36.577–37.897). T14=4.7222h, profile range4.5919–4.8526h; ingress T12=1.1806h, nominal trapezoid T23=2.3611h. Trapezoid flat duration is not physical totality for grazing events.

Primary linear ephemeris: P=7.2428348001±0.0005008657d, Tref=2597.7537849±0.0006134BTJD (reference cycle2); T0=2583.2681153. Chi2/dof=7.20/2; O-C RMS=1.140min. Errors are conditional on this baseline/shape and include fit red-noise/chi2 scaling, not all model systematics. The original resolved CSV and P/P2 were checked; all use the resolved full orbital period. Individual event values and exclusions are retained in fit-results.json.

The blind rolling-median dip census found6 threshold groups; there are zero groups deeper than half the median primary depth outside ±1.5T14 around either fitted eclipse phase. It is a detection census, not an astrophysical classification of small fluctuations. No isolated sector-wide systematic is used as deciding evidence. Maximum fitted background-correlated fake depth is 0.1384ppt; including native-unit background regression changes an individual depth by at most0.35%. Background units were not divided into normalized flux. Maximum flagged core count among accepted windows=4; rejected/partial windows are not treated as nulls.

|Sector|Mid BTJD|Timing error d|Depth ppt|Error ppt|O-C min|Core flagged|
|---|---:|---:|---:|---:|---:|---:|
|47|2583.2677611|0.0005903|37.435|0.366|-0.510|4|
|47|2590.5108320|0.0005903|36.886|0.376|-0.170|1|
|47|2597.7550835|0.0005903|36.577|0.427|1.870|2|
|47|2604.9957933|0.0005903|37.897|0.435|-1.190|4|

## Gaia orbit and secondary gate

Exact source917229955854793216, solutionSB1, bit_index127, own correlation vector used. SB1 covariance order P,gamma,K1,e,omega,Tp (15 lower-triangle correlations); SB2 order P,gamma,K1,K2,e,omega,Tp (21). Gaia P=7.2428161380±0.0012557446d; photometric difference=0.014sigma. Primary association is conjunctionA; extrapolated Gaia-epoch offset=-0.057061d with Gaia-only sigma0.079628d. Individual epochs, covariance-propagated conjunction errors and timing residuals are in orbit-gates.json; the Gaia-only sigma does not include extrapolated photometric uncertainty.

Gaia e=0.022529±0.030761, omega=284.7313deg. Gaia relative other-conjunction phase=0.5036479; measured optimized phase=0.5036479. Status: supported repeat secondary. Optimized depth=2.6775±0.1556ppt; 2 individual >3sigma events among2 fitted windows. Phase was optimized, so the formal S/N is conditional and is not a blind false-alarm probability. Fixed Gaia-phase tests, every covered/partial/flagged other-conjunction window and off-phase controls are retained in orbit-gates.json; optimized individual measurements, T14/ingress/flat durations and uncertainty are in secondary-fit.json/secondary-shape.json. The fixed-primary-shape upper limit applies only at its tested phase and shape; it is not a null across the Gaia uncertainty envelope.

Only two secondary events: no independent secondary period is claimed.

First-order timing proxy e cos(omega)˜0.00573 versus Gaia0.00573; this small-e proxy is approximate and uncalibrated, especially when secondary is weak. Gaia and photometric phase disagreements are retained, not converted into a false precise e claim. Numerical limb-darkened two-disk geometry was tested instead of identifying grazing trapezoid T23 with totality. Coarse best e sin(omega)=0.1250, k=0.225, impact proxy=0.655; chi2/dof=532.74/121. Fixed TIC dimensions and freely fitted flux scales make this a feasibility diagnostic, not a posterior, measured radius, or a guarantee of a unique stellar solution.

## Independent reduction and attribution

MAST product SPOC, sector47; header target=117919258, sector=47 checked. SHA256=1bb2f08e7ee6062adac0e944aeaa8bbe5eb44f52b2d113fea099be7c3cd62198. At actual fitted QLP times, the independent product gives depth range34.654–35.580ppt. All per-event depths/errors, columns, URLs and target metadata are retained in independent-manifest-results.json. This is an independent reduction of TESS pixels, not an independent observatory.

Fresh ARI Gaia60arcsec cone to G<15 has0 resolved neighbours, 0 capable of this depth under a G-band flux-ratio approximation. Fainter sources cannot fully explain a ~35–40ppt dip individually. Required fractional dips are indicative because G and TESS bandpasses/aperture throughput differ.

|Gaia source|Separation arcsec|G|Required fractional dip|
|---|---:|---:|---:|

Prior difference image sector47, 4 events: peak on target=True; deficit/target separation1.21arcsec; deficit/light separation0.13arcsec. Duplicate old/new-schema rows are one measurement, not independent repetitions. Exact records are in parent diffrun JSONL receipts.

## Physical interpretation, archives and next check

RV mass function f(M)=0.019734Msun; assumed TIC M1=1.140Msun gives edge-on minimum M2=0.3530Msun, a=18.005Rsun. A main-sequence-radius approximation gives central T14(A/B)=7.079/6.777h compared with measured4.722h; inclination/grazing/dilution and stellar evolution remain degenerate. These approximations do not veto an attributed EB. In Gaia primary-omega convention, conjunctionA puts the spectroscopic primary behind its companion, while B puts the primary in front (positive RV is receding); flux labels alone do not uniquely assign components in a blended/grazing system.

SIMBAD exact Gaia-ID name: TYC 2988-1320-1, typeSB*. Fresh IDIA nine-catalogue cones found no target vetted EB classification; shared current Gaia vari_eclipsing_binary and ExoFOP TOI/CTOI checks are negative. Catalogue details, nearby variables, query limitations and weak web-name search are in CATALOGUE-NOTE.md. Novelty status: No vetted target EB found in queried catalogues; bibliography limited. This is not a complete publication-discovery claim.

Next nominal primary after2026-10-30: 4350.519806BTJD, subsequent 4357.762641. Other-kind nominal prediction: 4346.924810BTJD, subsequent4354.167645. These extrapolations are conditional. The secondary prediction uses the primary period; only two secondary events are available. Obtain a second sector to verify the secondary ephemeris and reduce extrapolation uncertainty.

Review gates are completed with their stated limitations: archives/current prior-art pass; raw primary and secondary/coverage analysis; individual timing/error and O-C; own-source Gaia covariance; independent reduction; neighbours and localization; physical feasibility; supported physical verdict. No unavailable measurement has been silently counted as a detection. Source catalogues were not edited.

## Final adversarial review details

The largest positive off-phase fixed-template control depth was 0.23ppt. Controls calibrate low-frequency/modulated residuals; they are not an exact multiple-trial probability for the optimized secondary. The0.23ppt control is well below the2.68ppt secondary; both individual events support it, but their two-event span cannot provide an independent secondary period. 

Fixed Gaia-phase other-conjunction coverage: 3 predicted windows, status counts {'fit': 2, 'insufficient': 1}; conditional depth 2.6772ppt, control-inflated 3sigma upper value 7.7450ppt. Optimized secondary windows status counts{'fit': 2, 'insufficient': 1}; fitted secondary T14=4.7222h, T12=1.1806h, trapezoid T23=2.3611h. Uncovered windows are not counted as nulls. Full event tables and all exclusions are in the cited JSON files.
