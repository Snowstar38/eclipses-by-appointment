# E029 — TIC 48099288

Review complete. Physical tier: **CONFIRMED**. Gaia DR3 2925011408780136960; selection P=37.84651671501455d,G=11.573237.

A narrow S6 raw eclipse repeats in newly retrieved S107 and S108 at BTJD 4275.577562 and 4313.440381. Local custom pixel extraction recovers the same-kind approximately 9 ppt, 0.13 d events, separate from broad S107 spacecraft bowls. Three times give 37.859888d with cycles 0/74/75. Adjacent later events reject all tested longer integer aliases by timing; divisors 2-6 fail covered predictions. All three events lie within the full nonlinear covariance of conjunction A. Independent per-pixel local detrending and Gaussian-plus-plane difference fits in two detector orientations support target ownership: S107 center (2.052,2.274) vs target (2.226,2.258), S108 center (2.570,2.685) vs target (2.535,2.596). All 200 independent core/side frame bootstrap positions in each sector are closer to target than either capable G14.61/G14.72 neighbor. The bootstrap is a bounded model check, not calibrated astrometry or exclusion of unresolved companions.

## Representative raw measurements

|Sector|fit midpoint BTJD|formal error d|depth ppt|duration d|usable midpoint|
|---|---|---|---|---|---|
|6|1473.9479014290005|0.0013478374220847631|10.856511659059334|0.1361795559314717|True|
|108|4313.440381225984|0.002007380611182158|8.633176979085402|0.13523980964686813|True|
|107|4275.57756199203|0.002173350258100164|9.02590955244912|0.12753216879901913|True|

Reported period=37.859888369845585d; local formal error=0.00014098139496645102d. Clock and cycle choices are in lead-clocks.json. Timing uncertainties are local formal fit errors; clock fits use cadence/2 or .004d floor for E034. They do not incorporate all systematics. Gap-cut midpoints are excluded explicitly. E029 has three events including adjacent S107/S108 eclipses; tested photometric timing alternatives do not survive. E034 representative residuals reach.0086d.

## Method and source attribution

Quality-zero finite positive raw SAP is primary evidence; all cached sector contexts and representative discrete events were inspected. KSPSAP and custom TESScut apertures reuse the same photons. Missing/gap-cut or flagged windows are not clean nulls. Aliases test divisors2–6 and endpoint integer alternatives over approximately5–100d; lead-alias-summary.json and lead-alias-covered-windows.json preserve each compatible alternative and covered raw evidence. Geometry uses this source's SB1 full covariance with edge-on conjunction assumptions, both conjunction kinds and a fixed integer cycle. Nonlinear draws unwrap base conjunction about nominal before propagating the fixed cycle; seed50701 and100000draws. Geometry is an association check, not an inclination measurement or exact physical model.

Pixel result: {"status": "measured", "target_xy": [3.7696285452621217, 3.222833865614361], "positive_diff_centroid_xy": [3.57689544709434, 3.2485898779247946], "centroid_offset_pixels": 0.19444644326777208, "aperture_loss": 0.007481211961662515}. Pixels and Gaia-neighbor geometry are considered together. E032's target aperture alone is contaminated and does not establish ownership. E029 S107/S108 source and event shapes pass a separate helper audit, with two-orientation Gaussian image bootstrap retained. E028/E033 have no credible discrete eclipse to localize; omitting pixel extraction does not manufacture a negative source test.

## Current availability and catalogue scope

lead-current-sector-inventory.json records successful current MAST sector responses. Bounded extras: E029S87/107/108/109 and E031S65/102 are preserved in lead-extra-sector-receipts.json and per-sector FITS/NPZ/plots. E029S87 and E031S65/S102 have near-zero flux/no target PSF and are unusable. E029 S107 contains broad spacecraft-like bowls that are excluded, plus a separate narrow eclipse at BTJD 4275.578; S108 has another narrow eclipse on a sloping baseline.

Scoped shared checks find no prior target eclipsing identification in the seven required sources; per-target receipt and shared seal are retained. No negative claim is made from a failed request. Literature checks and scoped catalogue nonmatches do not establish exhaustive priority.

## Limitation and next check

Another complete event can refine timing and source association; the representative formal period error does not include all systematic timing errors.

Physical tier, Gaia association, source ownership and novelty are recorded separately. Completion means the bounded deciding review is performed, not that every selected lead is a detection. Exact6 reviewed without substitution; previously published E030 excluded upstream. No ledger or publication edit. Evidence/scripts and helper final audit are sealed at batch level.
