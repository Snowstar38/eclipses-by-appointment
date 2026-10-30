# TIC 339787086 — CONFIRMED target eclipsing binary

Full-review completion: COMPLETE. Physical verdict and novelty are separate. Repeated ~36/40 ppt alternating eclipses in four sectors, independent reduction and absence of a sufficiently bright resolved neighbour establish the target EB. The Gaia SB2 association is supported by a nearly equal spectroscopic/photometric period and Gaia-epoch conjunction within about2 Gaia-only sigma, but the published Gaia orbit does not predict later eclipse times accurately. This is a confirmed target EB with an imperfect orbital solution, not a precision ephemeris or a validated association with the separate 281-day astrometric orbit.

## Raw photometry and timing

All available QLP products in qlp-manifest.json were examined from SAP_FLUX with QUALITY==0, no gap trimming; flagged core counts remain in every event row. Exposure-integrated trapezoids with local polynomial baselines, red-noise inflation and grid-error floors were fitted. 22 accepted primary events in 4 sectors; median depth 36.214ppt (range35.212–37.136). T14=3.6695h, profile range3.5826–3.7564h; ingress T12=1.2843h, nominal trapezoid T23=1.1009h. Trapezoid flat duration is not physical totality for grazing events.

Primary linear ephemeris: P=3.7794134843±0.0000086571d, Tref=2701.1571438±0.0012138BTJD (reference cycle269); T0=1684.4949165. Chi2/dof=1796.62/20; O-C RMS=6.510min. Errors are conditional on this baseline/shape and include fit red-noise/chi2 scaling, not all model systematics. The original resolved CSV and P/P2 were checked; all use the resolved full orbital period. Individual event values and exclusions are retained in fit-results.json.

The blind rolling-median dip census found50 threshold groups; there are zero groups deeper than half the median primary depth outside ±1.5T14 around either fitted eclipse phase. It is a detection census, not an astrophysical classification of small fluctuations. No isolated sector-wide systematic is used as deciding evidence. Maximum fitted background-correlated fake depth is 0.5694ppt; including native-unit background regression changes an individual depth by at most1.45%. Background units were not divided into normalized flux. Maximum flagged core count among accepted windows=8; rejected/partial windows are not treated as nulls.

|Sector|Mid BTJD|Timing error d|Depth ppt|Error ppt|O-C min|Core flagged|
|---|---:|---:|---:|---:|---:|---:|
|14|1684.4916695|0.0022731|36.859|0.479|-4.676|0|
|14|1688.2729397|0.0022731|37.136|0.422|-2.002|1|
|14|1695.8318106|0.0022731|36.652|0.579|-1.939|0|
|14|1699.6103286|0.0021263|36.311|0.420|-3.228|0|
|40|2395.0181926|0.0004862|36.377|0.402|-9.301|5|
|40|2406.3574163|0.0005176|35.861|0.538|-7.885|7|
|40|2410.1359343|0.0005358|36.320|0.396|-9.175|8|
|40|2413.9172045|0.0005012|36.745|0.387|-6.501|6|
|40|2417.6957226|0.0005012|36.440|0.480|-7.790|6|
|54|2772.9727448|0.0004599|36.042|0.342|9.713|3|
|54|2776.7512629|0.0004862|36.559|0.416|8.423|5|
|54|2780.5306983|0.0005012|36.133|0.437|8.455|6|
|54|2784.3101337|0.0005012|35.212|0.446|8.486|6|
|54|2788.0895692|0.0005012|36.295|0.452|8.518|6|
|54|2791.8680872|0.0005012|36.377|0.452|7.229|6|
|54|2795.6475227|0.0004725|36.067|0.377|7.260|4|
|81|3509.9479769|0.0004587|35.822|0.274|-5.260|0|
|81|3517.5068478|0.0004587|35.493|0.306|-5.196|0|
|81|3521.2872006|0.0004587|35.712|0.366|-3.844|0|
|81|3525.0675534|0.0004587|35.382|0.354|-2.491|0|
|81|3528.8479062|0.0004587|35.773|0.311|-1.139|0|
|81|3532.6282590|0.0004587|35.411|0.305|0.214|0|

## Gaia orbit and secondary gate

Exact source4322674031257647744, solutionSB2, bit_index255, own correlation vector used. SB1 covariance order P,gamma,K1,e,omega,Tp (15 lower-triangle correlations); SB2 order P,gamma,K1,K2,e,omega,Tp (21). Gaia P=3.7789813432±0.0000964621d; photometric difference=4.462sigma. Primary association is conjunctionB; extrapolated Gaia-epoch offset=-0.033647d with Gaia-only sigma0.016760d. Individual epochs, covariance-propagated conjunction errors and timing residuals are in orbit-gates.json; the Gaia-only sigma does not include extrapolated photometric uncertainty.

Gaia e=0.044911±0.012884, omega=356.0555deg. Gaia relative other-conjunction phase=0.4714858; measured optimized phase=0.4981861. Status: supported repeat secondary. Optimized depth=40.0133±0.1599ppt; 15 individual >3sigma events among15 fitted windows. Phase was optimized, so the formal S/N is conditional and is not a blind false-alarm probability. Fixed Gaia-phase tests, every covered/partial/flagged other-conjunction window and off-phase controls are retained in orbit-gates.json; optimized individual measurements, T14/ingress/flat durations and uncertainty are in secondary-fit.json/secondary-shape.json. The fixed-primary-shape upper limit applies only at its tested phase and shape; it is not a null across the Gaia uncertainty envelope.

Secondary ephemeris P=3.7793989754±0.0000098278d, Tref=2714.3818786±0.0015154, O-C RMS7.598min, chi2/dof861.66/13.

First-order timing proxy e cos(omega)˜0.00285 versus Gaia0.04480; this small-e proxy is approximate and uncalibrated, especially when secondary is weak. Gaia and photometric phase disagreements are retained, not converted into a false precise e claim. Numerical limb-darkened two-disk geometry was tested instead of identifying grazing trapezoid T23 with totality. Coarse best e sin(omega)=0.0750, k=0.250, impact proxy=0.935; chi2/dof=3255.67/121. Fixed TIC dimensions and freely fitted flux scales make this a feasibility diagnostic, not a posterior, measured radius, or a guarantee of a unique stellar solution.

## Independent reduction and attribution

MAST product TESS-SPOC, sector54; header target=339787086, sector=54 checked. SHA256=09afd87c6b08a025369eaa253ebe6586a187a910b0b115262463f65a05e2d3bf. At actual fitted QLP times, the independent product gives depth range34.251–36.984ppt. All per-event depths/errors, columns, URLs and target metadata are retained in independent-manifest-results.json. This is an independent reduction of TESS pixels, not an independent observatory.

Fresh ARI Gaia60arcsec cone to G<15 has0 resolved neighbours, 0 capable of this depth under a G-band flux-ratio approximation. Fainter sources cannot fully explain a ~35–40ppt dip individually. Required fractional dips are indicative because G and TESS bandpasses/aperture throughput differ.

|Gaia source|Separation arcsec|G|Required fractional dip|
|---|---:|---:|---:|

Prior difference image sector40, 8 events: peak on target=True; deficit/target separation5.1arcsec; deficit/light separation3.57arcsec. Duplicate old/new-schema rows are one measurement, not independent repetitions. Exact records are in parent diffrun JSONL receipts.

## Physical interpretation, archives and next check

SB2 dynamical q=0.9262, M1 sin³i=1.5107Msun, M2 sin³i=1.3992Msun and a sin i=14.580Rsun. These supersede the SB1/TIC-M1 surrogate in orbit-gates physics. The TIC assumed M1 is below this SB2 minimum; it is not a valid measured primary mass. Geometry chi2 is poor and must not be promoted to component characterization. Strong paired eclipses identify the target EB despite that model failure. The separate Gaia Orbital solution P280.989±2.275d is retained as possible multiplicity context; no causal explanation of eclipse timing changes is established. Linear timing residuals are sector-coherent (about-9 to+10min); published Gaia conjunction offsets accumulate across sectors.

SIMBAD exact Gaia-ID name: TYC 1604-1130-1, typeSB*. Fresh IDIA nine-catalogue cones found no target vetted EB classification; shared current Gaia vari_eclipsing_binary and ExoFOP TOI/CTOI checks are negative. Catalogue details, nearby variables, query limitations and weak web-name search are in CATALOGUE-NOTE.md. Novelty status: No vetted target EB found in queried catalogues; bibliography limited. This is not a complete publication-discovery claim.

Next nominal primary after2026-10-30: 4345.202009BTJD, subsequent 4348.981423. Other-kind nominal prediction: 4347.082236BTJD, subsequent4350.861635. These extrapolations are conditional. Linear timing extrapolation needs the systematic margin specified below. Jointly refit RV and eclipse timings; assess sector-dependent baseline effects and the separate 281-day astrometric solution.

Review gates are completed with their stated limitations: archives/current prior-art pass; raw primary and secondary/coverage analysis; individual timing/error and O-C; own-source Gaia covariance; independent reduction; neighbours and localization; physical feasibility; supported physical verdict. No unavailable measurement has been silently counted as a detection. Source catalogues were not edited.

## Final adversarial review details

The largest positive off-phase fixed-template control depth was 2.17ppt. Controls calibrate low-frequency/modulated residuals; they are not an exact multiple-trial probability for the optimized secondary. The repeat secondary signal is stronger than the off-phase controls and recurs in multiple sectors. 

The photometric versus Gaia SB2 period discrepancy is4.46sigma under the quoted uncertainties. Primary chi2/dof1796.6/20 and sector-coherent O-C of roughly-9 to+10min demonstrate limitations of a single linear ephemeris and its formal timing errors. At2026-10-30 the propagated formal linear timing scale alone is about5.7min; it is not a complete predictive error. Use at least +/-0.05d (72min) around a nominal prediction as a provisional observing search window, not a calibrated confidence interval or guarantee; further timing evolution may require more. The target is confirmed as an EB; the exact connection of all eclipses to the published SB2 orbital parameters remains imperfect, and the281-day astrometric-orbit association remains unestablished. 

Fixed Gaia-phase other-conjunction coverage: 28 predicted windows, status counts {'fit': 16, 'insufficient': 12}; conditional depth -9.4273ppt, control-inflated 3sigma upper value 8.4461ppt. Optimized secondary windows status counts{'fit': 15, 'insufficient': 13}; fitted secondary T14=3.6695h, T12=1.2843h, trapezoid T23=1.1009h. Uncovered windows are not counted as nulls. Full event tables and all exclusions are in the cited JSON files.
