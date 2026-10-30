# TIC 341432079 — CONFIRMED target eclipsing binary

Full-review completion: COMPLETE. Physical verdict and novelty are separate. Repeated primaries and secondaries, independent reduction and new per-pixel localization favour the target over both capable neighbours. Mild Gaia eccentric-orbit/secondary-phase tension is a characterization issue.

## Raw photometry and timing

All available QLP products in qlp-manifest.json were examined from SAP_FLUX with QUALITY==0, no gap trimming; flagged core counts remain in every event row. Exposure-integrated trapezoids with local polynomial baselines, red-noise inflation and grid-error floors were fitted. 17 accepted primary events in 5 sectors; median depth 36.134ppt (range31.254–36.730). T14=4.9829h, profile range4.8526–5.1132h; ingress T12=1.2457h, nominal trapezoid T23=2.4914h. Trapezoid flat duration is not physical totality for grazing events.

Primary linear ephemeris: P=5.1087338002±0.0000034021d, Tref=2703.1501461±0.0003281BTJD (reference cycle199); T0=1686.5121199. Chi2/dof=48.41/15; O-C RMS=4.197min. Errors are conditional on this baseline/shape and include fit red-noise/chi2 scaling, not all model systematics. The original resolved CSV and P/P2 were checked; all use the resolved full orbital period. Individual event values and exclusions are retained in fit-results.json.

The blind rolling-median dip census found36 threshold groups; there are zero groups deeper than half the median primary depth outside ±1.5T14 around either fitted eclipse phase. It is a detection census, not an astrophysical classification of small fluctuations. No isolated sector-wide systematic is used as deciding evidence. Maximum fitted background-correlated fake depth is 3.6506ppt; including native-unit background regression changes an individual depth by at most11.11%. Background units were not divided into normalized flux. Maximum flagged core count among accepted windows=12; rejected/partial windows are not treated as nulls.

|Sector|Mid BTJD|Timing error d|Depth ppt|Error ppt|O-C min|Core flagged|
|---|---:|---:|---:|---:|---:|---:|
|14|1686.5053543|0.0019019|36.439|0.255|-9.742|0|
|14|1701.8328828|0.0019019|36.730|0.339|-7.831|0|
|40|2391.5093783|0.0080972|31.254|4.694|-11.529|12|
|40|2406.8468725|0.0018686|36.077|1.407|4.733|10|
|41|2422.1694181|0.0006229|36.252|0.304|-0.531|0|
|41|2427.2781790|0.0006229|36.551|0.267|-0.492|0|
|41|2437.4969466|0.0006229|35.799|0.280|1.380|0|
|41|2442.6044618|0.0006229|36.134|0.281|-0.375|0|
|54|2774.6726759|0.0006229|35.378|0.301|0.369|8|
|54|2779.7814368|0.0006229|36.195|0.410|0.408|8|
|54|2784.8914434|0.0006229|36.406|0.397|2.241|8|
|54|2790.0002043|0.0006229|35.203|0.299|2.280|12|
|54|2795.1064738|0.0006229|35.115|0.333|-1.268|5|
|81|3510.3292654|0.0006229|36.198|0.316|-1.183|0|
|81|3520.5467872|0.0006229|36.103|0.260|-1.104|0|
|81|3525.6567938|0.0006229|36.124|0.254|0.728|0|
|81|3530.7643090|0.0006229|36.333|0.308|-1.026|5|

## Gaia orbit and secondary gate

Exact source1823986543821182080, solutionSB1, bit_index127, own correlation vector used. SB1 covariance order P,gamma,K1,e,omega,Tp (15 lower-triangle correlations); SB2 order P,gamma,K1,K2,e,omega,Tp (21). Gaia P=5.1086672779±0.0004283853d; photometric difference=0.155sigma. Primary association is conjunctionA; extrapolated Gaia-epoch offset=-0.018922d with Gaia-only sigma0.021890d. Individual epochs, covariance-propagated conjunction errors and timing residuals are in orbit-gates.json; the Gaia-only sigma does not include extrapolated photometric uncertainty.

Gaia e=0.028067±0.013215, omega=159.2772deg. Gaia relative other-conjunction phase=0.4832894; measured optimized phase=0.5003486. Status: supported repeat secondary. Optimized depth=2.6987±0.0754ppt; 20 individual >3sigma events among20 fitted windows. Phase was optimized, so the formal S/N is conditional and is not a blind false-alarm probability. Fixed Gaia-phase tests, every covered/partial/flagged other-conjunction window and off-phase controls are retained in orbit-gates.json; optimized individual measurements, T14/ingress/flat durations and uncertainty are in secondary-fit.json/secondary-shape.json. The fixed-primary-shape upper limit applies only at its tested phase and shape; it is not a null across the Gaia uncertainty envelope.

Secondary ephemeris P=5.1087474561±0.0000088999d, Tref=2659.7262720±0.0010573, O-C RMS6.685min, chi2/dof14.36/18.

First-order timing proxy e cos(omega)˜0.00055 versus Gaia-0.02625; this small-e proxy is approximate and uncalibrated, especially when secondary is weak. Gaia and photometric phase disagreements are retained, not converted into a false precise e claim. Numerical limb-darkened two-disk geometry was tested instead of identifying grazing trapezoid T23 with totality. Coarse best e sin(omega)=0.0500, k=0.250, impact proxy=0.515; chi2/dof=201.03/121. Fixed TIC dimensions and freely fitted flux scales make this a feasibility diagnostic, not a posterior, measured radius, or a guarantee of a unique stellar solution.

## Independent reduction and attribution

MAST product TESS-SPOC, sector54; header target=341432079, sector=54 checked. SHA256=8b4646a460f2ad8470e901d17a81dcb2e0f11498297c3717695e53fff5bf411f. At actual fitted QLP times, the independent product gives depth range31.798–38.504ppt. All per-event depths/errors, columns, URLs and target metadata are retained in independent-manifest-results.json. This is an independent reduction of TESS pixels, not an independent observatory.

Fresh ARI Gaia60arcsec cone to G<15 has5 resolved neighbours, 2 capable of this depth under a G-band flux-ratio approximation. Fainter sources cannot fully explain a ~35–40ppt dip individually. Required fractional dips are indicative because G and TESS bandpasses/aperture throughput differ.

|Gaia source|Separation arcsec|G|Required fractional dip|
|---|---:|---:|---:|
|1823986642546802944|41.07|13.815|0.720|
|1823986578180902784|47.44|13.626|0.605|
|1823986711266237568|47.63|14.969|2.082|
|1823986642546807808|54.74|14.479|1.326|
|1823986646900389632|56.74|14.337|1.163|

Prior difference image sector40, 4 events: peak on target=True; deficit/target separation6.92arcsec; deficit/light separation8.03arcsec. Duplicate old/new-schema rows are one measurement, not independent repetitions. Exact records are in parent diffrun JSONL receipts.

A new per-pixel eclipse-template regression on hashed existing TESScut cubes tests the ambiguity directly. OOT multi-source Gaussian calibration: sigma0.700pixel, dx-0.080,dy0.080. Free deficit center is1.878arcsec from target; fixed target chi2=3719.06, best alternative-source chi2=40034.52, delta=36315.45. This strongly distinguishes target from resolved neighbours; PSF residual covariance prevents interpreting these formal chi2 values as calibrated significance or precise astrometry. See pixel-localization.json and pixel_selective.py.

## Physical interpretation, archives and next check

RV mass function f(M)=0.021608Msun; assumed TIC M1=1.499Msun gives edge-on minimum M2=0.4319Msun, a=15.544Rsun. A main-sequence-radius approximation gives central T14(A/B)=6.160/6.283h compared with measured4.983h; inclination/grazing/dilution and stellar evolution remain degenerate. These approximations do not veto an attributed EB. In Gaia primary-omega convention, conjunctionA puts the spectroscopic primary behind its companion, while B puts the primary in front (positive RV is receding); flux labels alone do not uniquely assign components in a blended/grazing system.

SIMBAD exact Gaia-ID name: HD 350336, typeSB*. Fresh IDIA nine-catalogue cones found no target vetted EB classification; shared current Gaia vari_eclipsing_binary and ExoFOP TOI/CTOI checks are negative. Catalogue details, nearby variables, query limitations and weak web-name search are in CATALOGUE-NOTE.md. Novelty status: No vetted target EB found in queried catalogues; bibliography limited. This is not a complete publication-discovery claim.

Next nominal primary after2026-10-30: 4348.162430BTJD, subsequent 4353.271164. Other-kind nominal prediction: 4345.612933BTJD, subsequent4350.721680. These extrapolations are conditional. Refine component radii, dilution and eccentric orbit with joint RV/eclipse modeling.

Review gates are completed with their stated limitations: archives/current prior-art pass; raw primary and secondary/coverage analysis; individual timing/error and O-C; own-source Gaia covariance; independent reduction; neighbours and localization; physical feasibility; supported physical verdict. No unavailable measurement has been silently counted as a detection. Source catalogues were not edited.

## Final adversarial review details

The largest positive off-phase fixed-template control depth was 0.30ppt. Controls calibrate low-frequency/modulated residuals; they are not an exact multiple-trial probability for the optimized secondary. The repeat secondary signal is stronger than the off-phase controls and recurs in multiple sectors. 

Fixed Gaia-phase other-conjunction coverage: 26 predicted windows, status counts {'insufficient': 7, 'fit': 19}; conditional depth 0.8746ppt, control-inflated 3sigma upper value 9.6162ppt. Optimized secondary windows status counts{'fit': 20, 'insufficient': 6}; fitted secondary T14=5.5043h, T12=1.3761h, trapezoid T23=2.7521h. Uncovered windows are not counted as nulls. Full event tables and all exclusions are in the cited JSON files.
