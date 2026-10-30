# TIC 266540667 — CONFIRMED target eclipsing binary

Full-review completion: COMPLETE. Physical verdict and novelty are separate. Twenty-one primary and19 secondary events, independent reduction, no capable resolved neighbour and deficit/light agreement0.52arcsec establish the target EB.

## Raw photometry and timing

All available QLP products in qlp-manifest.json were examined from SAP_FLUX with QUALITY==0, no gap trimming; flagged core counts remain in every event row. Exposure-integrated trapezoids with local polynomial baselines, red-noise inflation and grid-error floors were fitted. 21 accepted primary events in 4 sectors; median depth 38.463ppt (range33.423–39.154). T14=4.9829h, profile range4.8526–5.1132h; ingress T12=0.7474h, nominal trapezoid T23=3.4880h. Trapezoid flat duration is not physical totality for grazing events.

Primary linear ephemeris: P=3.6993685260±0.0000007262d, Tref=2558.9080632±0.0001783BTJD (reference cycle333); T0=1327.0183441. Chi2/dof=5.76/19; O-C RMS=0.639min. Errors are conditional on this baseline/shape and include fit red-noise/chi2 scaling, not all model systematics. The original resolved CSV and P/P2 were checked; all use the resolved full orbital period. Individual event values and exclusions are retained in fit-results.json.

The blind rolling-median dip census found42 threshold groups; there are zero groups deeper than half the median primary depth outside ±1.5T14 around either fitted eclipse phase. It is a detection census, not an astrophysical classification of small fluctuations. No isolated sector-wide systematic is used as deciding evidence. Maximum fitted background-correlated fake depth is 0.2472ppt; including native-unit background regression changes an individual depth by at most0.68%. Background units were not divided into normalized flux. Maximum flagged core count among accepted windows=8; rejected/partial windows are not treated as nulls.

|Sector|Mid BTJD|Timing error d|Depth ppt|Error ppt|O-C min|Core flagged|
|---|---:|---:|---:|---:|---:|---:|
|1|1327.0180543|0.0020047|38.739|0.356|-0.417|1|
|1|1330.7174177|0.0019018|38.607|0.343|-0.425|0|
|1|1334.4167811|0.0019018|38.463|0.354|-0.432|0|
|1|1338.1161446|0.0019018|38.530|0.361|-0.439|0|
|1|1341.8167537|0.0024552|38.477|0.455|1.347|4|
|1|1345.5161171|0.0020047|38.795|0.316|1.340|0|
|28|2063.1926218|0.0006229|38.522|0.279|-0.085|7|
|28|2066.8919852|0.0006229|38.934|0.459|-0.092|3|
|28|2070.5913486|0.0006229|38.501|0.348|-0.100|3|
|28|2077.9900755|0.0006229|39.154|0.280|-0.114|8|
|28|2081.6894389|0.0006229|38.692|0.333|-0.122|6|
|68|3158.2054416|0.0006229|37.996|0.333|-0.465|0|
|68|3165.6054142|0.0006229|38.426|0.427|1.314|0|
|68|3169.3035319|0.0006229|38.272|0.326|-0.487|0|
|68|3173.0041410|0.0006229|38.166|0.354|1.300|0|
|68|3176.7022587|0.0006229|38.012|0.345|-0.502|0|
|95|3886.9812822|0.0006229|33.489|0.275|-0.118|0|
|95|3890.6806457|0.0006229|33.550|0.288|-0.125|0|
|95|3898.0793725|0.0006229|33.435|0.286|-0.140|0|
|95|3901.7787359|0.0006229|33.541|0.297|-0.147|0|
|95|3905.4780994|0.0006229|33.423|0.294|-0.155|0|

## Gaia orbit and secondary gate

Exact source6776367269533991424, solutionSB1, bit_index127, own correlation vector used. SB1 covariance order P,gamma,K1,e,omega,Tp (15 lower-triangle correlations); SB2 order P,gamma,K1,K2,e,omega,Tp (21). Gaia P=3.6995626746±0.0001569517d; photometric difference=-1.237sigma. Primary association is conjunctionA; extrapolated Gaia-epoch offset=0.019372d with Gaia-only sigma0.021131d. Individual epochs, covariance-propagated conjunction errors and timing residuals are in orbit-gates.json; the Gaia-only sigma does not include extrapolated photometric uncertainty.

Gaia e=0.043473±0.018095, omega=273.3458deg. Gaia relative other-conjunction phase=0.5016168; measured optimized phase=0.4920431. Status: supported repeat secondary. Optimized depth=1.9621±0.0483ppt; 19 individual >3sigma events among19 fitted windows. Phase was optimized, so the formal S/N is conditional and is not a blind false-alarm probability. Fixed Gaia-phase tests, every covered/partial/flagged other-conjunction window and off-phase controls are retained in orbit-gates.json; optimized individual measurements, T14/ingress/flat durations and uncertainty are in secondary-fit.json/secondary-shape.json. The fixed-primary-shape upper limit applies only at its tested phase and shape; it is not a null across the Gaia uncertainty envelope.

Secondary ephemeris P=3.6993717105±0.0000031356d, Tref=2645.8156813±0.0007784, O-C RMS5.972min, chi2/dof35.81/17.

First-order timing proxy e cos(omega)˜-0.01250 versus Gaia0.00254; this small-e proxy is approximate and uncalibrated, especially when secondary is weak. Gaia and photometric phase disagreements are retained, not converted into a false precise e claim. Numerical limb-darkened two-disk geometry was tested instead of identifying grazing trapezoid T23 with totality. Coarse best e sin(omega)=-0.0250, k=0.200, impact proxy=0.235; chi2/dof=83.11/121. Fixed TIC dimensions and freely fitted flux scales make this a feasibility diagnostic, not a posterior, measured radius, or a guarantee of a unique stellar solution.

## Independent reduction and attribution

MAST product TESS-SPOC, sector1; header target=266540667, sector=1 checked. SHA256=90b127fb1e1083944f96bbb64f8c4bdf1388a2bfa77912cedaf076500102a584. At actual fitted QLP times, the independent product gives depth range37.125–37.598ppt. All per-event depths/errors, columns, URLs and target metadata are retained in independent-manifest-results.json. This is an independent reduction of TESS pixels, not an independent observatory.

Fresh ARI Gaia60arcsec cone to G<15 has0 resolved neighbours, 0 capable of this depth under a G-band flux-ratio approximation. Fainter sources cannot fully explain a ~35–40ppt dip individually. Required fractional dips are indicative because G and TESS bandpasses/aperture throughput differ.

|Gaia source|Separation arcsec|G|Required fractional dip|
|---|---:|---:|---:|

Prior difference image sector1, 6 events: peak on target=True; deficit/target separation4.06arcsec; deficit/light separation0.52arcsec. Duplicate old/new-schema rows are one measurement, not independent repetitions. Exact records are in parent diffrun JSONL receipts.

## Physical interpretation, archives and next check

RV mass function f(M)=0.012880Msun; assumed TIC M1=1.320Msun gives edge-on minimum M2=0.3269Msun, a=11.888Rsun. A main-sequence-radius approximation gives central T14(A/B)=5.624/5.157h compared with measured4.983h; inclination/grazing/dilution and stellar evolution remain degenerate. These approximations do not veto an attributed EB. In Gaia primary-omega convention, conjunctionA puts the spectroscopic primary behind its companion, while B puts the primary in front (positive RV is receding); flux labels alone do not uniquely assign components in a blended/grazing system.

SIMBAD exact Gaia-ID name: CD-36 14708, typeSB*. Fresh IDIA nine-catalogue cones found no target vetted EB classification; shared current Gaia vari_eclipsing_binary and ExoFOP TOI/CTOI checks are negative. Catalogue details, nearby variables, query limitations and weak web-name search are in CATALOGUE-NOTE.md. Novelty status: No vetted target EB found in queried catalogues; bibliography limited. This is not a complete publication-discovery claim.

Next nominal primary after2026-10-30: 4345.703061BTJD, subsequent 4349.402430. Other-kind nominal prediction: 4343.827296BTJD, subsequent4347.526668. These extrapolations are conditional. Refine component radii, dilution and eccentric orbit with joint RV/eclipse modeling.

Review gates are completed with their stated limitations: archives/current prior-art pass; raw primary and secondary/coverage analysis; individual timing/error and O-C; own-source Gaia covariance; independent reduction; neighbours and localization; physical feasibility; supported physical verdict. No unavailable measurement has been silently counted as a detection. Source catalogues were not edited.

## Final adversarial review details

The largest positive off-phase fixed-template control depth was 0.64ppt. Controls calibrate low-frequency/modulated residuals; they are not an exact multiple-trial probability for the optimized secondary. The repeat secondary signal is stronger than the off-phase controls and recurs in multiple sectors. 

Fixed Gaia-phase other-conjunction coverage: 27 predicted windows, status counts {'fit': 19, 'insufficient': 8}; conditional depth 1.5605ppt, control-inflated 3sigma upper value 4.3987ppt. Optimized secondary windows status counts{'fit': 19, 'insufficient': 8}; fitted secondary T14=4.7222h, T12=0.7083h, trapezoid T23=3.3055h. Uncovered windows are not counted as nulls. Full event tables and all exclusions are in the cited JSON files.
