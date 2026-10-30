# TIC 97509220 — CONFIRMED target eclipsing binary

Full-review completion: COMPLETE. Physical verdict and novelty are separate. Four ~37 ppt primary eclipses are repeated in rawSAP and TARS, and targeted pixels locate the disappearing light on the target rather than either capable neighbour. The local period agrees with the Gaia SB1 period to0.48sigma and RV requires a stellar companion. The optimized ~1.8ppt secondary is not secure because an off-phase control is deeper; that ambiguity does not remove the attributed primary EB.

## Raw photometry and timing

All available QLP products in qlp-manifest.json were examined from SAP_FLUX with QUALITY==0, no gap trimming; flagged core counts remain in every event row. Exposure-integrated trapezoids with local polynomial baselines, red-noise inflation and grid-error floors were fitted. 4 accepted primary events in 1 sectors; median depth 37.089ppt (range37.042–37.450). T14=4.0171h, profile range3.9302–4.1040h; ingress T12=0.6026h, nominal trapezoid T23=2.8120h. Trapezoid flat duration is not physical totality for grazing events.

Primary linear ephemeris: P=5.2102346549±0.0001587900d, Tref=3815.9763862±0.0002511BTJD (reference cycle2); T0=3805.5559169. Chi2/dof=1.00/2; O-C RMS=0.362min. Errors are conditional on this baseline/shape and include fit red-noise/chi2 scaling, not all model systematics. The original resolved CSV and P/P2 were checked; all use the resolved full orbital period. Individual event values and exclusions are retained in fit-results.json.

The blind rolling-median dip census found4 threshold groups; there are zero groups deeper than half the median primary depth outside ±1.5T14 around either fitted eclipse phase. It is a detection census, not an astrophysical classification of small fluctuations. No isolated sector-wide systematic is used as deciding evidence. Maximum fitted background-correlated fake depth is 0.0809ppt; including native-unit background regression changes an individual depth by at most0.21%. Background units were not divided into normalized flux. Maximum flagged core count among accepted windows=0; rejected/partial windows are not treated as nulls.

|Sector|Mid BTJD|Timing error d|Depth ppt|Error ppt|O-C min|Core flagged|
|---|---:|---:|---:|---:|---:|---:|
|92|3805.5556658|0.0005021|37.450|0.433|-0.362|0|
|92|3810.7664026|0.0005021|37.130|0.385|0.362|0|
|92|3821.1868719|0.0005021|37.042|0.359|0.362|0|
|92|3826.3966044|0.0005021|37.048|0.360|-0.362|0|

## Gaia orbit and secondary gate

Exact source6767648451564895360, solutionSB1, bit_index127, own correlation vector used. SB1 covariance order P,gamma,K1,e,omega,Tp (15 lower-triangle correlations); SB2 order P,gamma,K1,K2,e,omega,Tp (21). Gaia P=5.2106396818±0.0008243086d; photometric difference=-0.482sigma. Primary association is conjunctionA; extrapolated Gaia-epoch offset=0.131501d with Gaia-only sigma0.096159d. Individual epochs, covariance-propagated conjunction errors and timing residuals are in orbit-gates.json; the Gaia-only sigma does not include extrapolated photometric uncertainty.

Gaia e=0.046223±0.041905, omega=300.1219deg. Gaia relative other-conjunction phase=0.5147779; measured optimized phase=0.5007016. Status: ambiguous secondary; no secure detection. Optimized depth=1.7957±0.2166ppt; 4 individual >3sigma events among4 fitted windows. Phase was optimized, so the formal S/N is conditional and is not a blind false-alarm probability. Fixed Gaia-phase tests, every covered/partial/flagged other-conjunction window and off-phase controls are retained in orbit-gates.json; optimized individual measurements, T14/ingress/flat durations and uncertainty are in secondary-fit.json/secondary-shape.json. The fixed-primary-shape upper limit applies only at its tested phase and shape; it is not a null across the Gaia uncertainty envelope.

Secondary ephemeris P=5.2119796745±0.0020251515d, Tref=3818.5851514±0.0026340, O-C RMS7.729min, chi2/dof5.49/2.

First-order timing proxy e cos(omega)˜0.00110 versus Gaia0.02320; this small-e proxy is approximate and uncalibrated, especially when secondary is weak. Gaia and photometric phase disagreements are retained, not converted into a false precise e claim. Numerical limb-darkened two-disk geometry was tested instead of identifying grazing trapezoid T23 with totality. Coarse best e sin(omega)=0.0250, k=0.200, impact proxy=0.305; chi2/dof=312.21/121. Fixed TIC dimensions and freely fitted flux scales make this a feasibility diagnostic, not a posterior, measured radius, or a guarantee of a unique stellar solution.

## Independent reduction and attribution

MAST product TARS, sector92; header target=97509220, sector=92 checked. SHA256=a18537b7a081d89fb267694c539dff8c73c303f605092066637bc10542aae323. At actual fitted QLP times, the independent product gives depth range36.826–39.345ppt. All per-event depths/errors, columns, URLs and target metadata are retained in independent-manifest-results.json. This is an independent reduction of TESS pixels, not an independent observatory.

Fresh ARI Gaia60arcsec cone to G<15 has2 resolved neighbours, 2 capable of this depth under a G-band flux-ratio approximation. Fainter sources cannot fully explain a ~35–40ppt dip individually. Required fractional dips are indicative because G and TESS bandpasses/aperture throughput differ.

|Gaia source|Separation arcsec|G|Required fractional dip|
|---|---:|---:|---:|
|6767648451564893568|33.62|13.634|0.478|
|6767648245406462080|48.16|11.694|0.080|

Prior difference image sector92, 4 events: peak on target=True; deficit/target separation1.19arcsec; deficit/light separation14.94arcsec. Duplicate old/new-schema rows are one measurement, not independent repetitions. Exact records are in parent diffrun JSONL receipts.

A new per-pixel eclipse-template regression on hashed existing TESScut cubes tests the ambiguity directly. OOT multi-source Gaussian calibration: sigma0.550pixel, dx-0.000,dy-0.000. Free deficit center is0.840arcsec from target; fixed target chi2=11700.55, best alternative-source chi2=86931.84, delta=75231.28. This strongly distinguishes target from resolved neighbours; PSF residual covariance prevents interpreting these formal chi2 values as calibrated significance or precise astrometry. See pixel-localization.json and pixel_selective.py.

## Physical interpretation, archives and next check

RV mass function f(M)=0.004633Msun; assumed TIC M1=1.178Msun gives edge-on minimum M2=0.2072Msun, a=14.099Rsun. A main-sequence-radius approximation gives central T14(A/B)=4.888/4.512h compared with measured4.017h; inclination/grazing/dilution and stellar evolution remain degenerate. These approximations do not veto an attributed EB. In Gaia primary-omega convention, conjunctionA puts the spectroscopic primary behind its companion, while B puts the primary in front (positive RV is receding); flux labels alone do not uniquely assign components in a blended/grazing system.

SIMBAD exact Gaia-ID name: TYC 6894-2722-1, typeSB*. Fresh IDIA nine-catalogue cones found no target vetted EB classification; shared current Gaia vari_eclipsing_binary and ExoFOP TOI/CTOI checks are negative. Catalogue details, nearby variables, query limitations and weak web-name search are in CATALOGUE-NOTE.md. Novelty status: No vetted target EB found in queried catalogues; bibliography limited. This is not a complete publication-discovery claim.

Next nominal primary after2026-10-30: 4347.420321BTJD, subsequent 4352.630556. Other-kind nominal prediction: 4344.995098BTJD, subsequent4350.207078. These extrapolations are conditional. The secondary prediction is tentative because its detection is ambiguous. Obtain another eclipse sector to improve local period and test the weak secondary against phase controls.

Review gates are completed with their stated limitations: archives/current prior-art pass; raw primary and secondary/coverage analysis; individual timing/error and O-C; own-source Gaia covariance; independent reduction; neighbours and localization; physical feasibility; supported physical verdict. No unavailable measurement has been silently counted as a detection. Source catalogues were not edited.

## Final adversarial review details

The largest positive off-phase fixed-template control depth was 3.43ppt. Controls calibrate low-frequency/modulated residuals; they are not an exact multiple-trial probability for the optimized secondary. The3.43ppt control exceeds the candidate1.80ppt secondary, so no secure secondary or geometry derived from that candidate is claimed. Primary-only EB classification rests on the repeatability, pixels, independent TARS reduction and RV companion. 

Fixed Gaia-phase other-conjunction coverage: 6 predicted windows, status counts {'insufficient': 2, 'fit': 4}; conditional depth 0.5904ppt, control-inflated 3sigma upper value 9.6586ppt. Optimized secondary windows status counts{'insufficient': 2, 'fit': 4}; fitted secondary T14=4.1909h, T12=0.6286h, trapezoid T23=2.9336h. Uncovered windows are not counted as nulls. The optimized secondary remains ambiguous. Full event tables and all exclusions are in the cited JSON files.
