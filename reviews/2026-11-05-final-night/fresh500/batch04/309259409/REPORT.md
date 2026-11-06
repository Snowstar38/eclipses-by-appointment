# E032 — TIC 309259409

Review complete. Physical tier: **REFUTED**. Gaia DR3 3454971752759931136; selection P=36.85781261844228d,G=11.931819.

The S45 compact depression is real in the blended QLP aperture but comes from a northern neighbor. The deficit peaks at pixel(2,6), aligned with Gaia3454968832182263168,G14.16355 at(1.882,5.863); the selected target lies near(3.1,3.6). Target-peak pixel(3,4) has loss-0.000584, while northern pixels(2,6)/(2,5) show3.23%/1.77% losses. Thus the target eclipse interpretation is refuted. A possible single eclipse on the neighbor remains separate from the target and the selected Gaia orbit.

## Representative raw measurements

|Sector|fit midpoint BTJD|formal error d|depth ppt|duration d|usable midpoint|
|---|---|---|---|---|---|
|45|2531.9970186733094|0.008191287669313487|6.10611362922897|0.9054688030207668|True|

Reported period=unresolvedd; local formal error=not assignedd. Clock and cycle choices are in lead-clocks.json. Timing uncertainties are local formal fit errors; clock fits use cadence/2 or .004d floor for E034. They do not incorporate all systematics. Gap-cut midpoints are excluded explicitly. E029 has three events including adjacent S107/S108 eclipses; tested photometric timing alternatives do not survive. E034 representative residuals reach.0086d.

## Method and source attribution

Quality-zero finite positive raw SAP is primary evidence; all cached sector contexts and representative discrete events were inspected. KSPSAP and custom TESScut apertures reuse the same photons. Missing/gap-cut or flagged windows are not clean nulls. Aliases test divisors2–6 and endpoint integer alternatives over approximately5–100d; lead-alias-summary.json and lead-alias-covered-windows.json preserve each compatible alternative and covered raw evidence. Geometry uses this source's SB1 full covariance with edge-on conjunction assumptions, both conjunction kinds and a fixed integer cycle. Nonlinear draws unwrap base conjunction about nominal before propagating the fixed cycle; seed50701 and100000draws. Geometry is an association check, not an inclination measurement or exact physical model.

Pixel result: {"status": "measured", "target_xy": [3.1150606045930083, 3.623353794166582], "positive_diff_centroid_xy": [2.3961944719892436, 5.215567925474967], "centroid_offset_pixels": 1.746972912366648, "aperture_loss": 0.0017911440772840903}. Pixels and Gaia-neighbor geometry are considered together. E032's target aperture alone is contaminated and does not establish ownership. E029 S107/S108 source and event shapes pass a separate helper audit, with two-orientation Gaussian image bootstrap retained. E028/E033 have no credible discrete eclipse to localize; omitting pixel extraction does not manufacture a negative source test.

## Current availability and catalogue scope

lead-current-sector-inventory.json records successful current MAST sector responses. Bounded extras: E029S87/107/108/109 and E031S65/102 are preserved in lead-extra-sector-receipts.json and per-sector FITS/NPZ/plots. E029S87 and E031S65/S102 have near-zero flux/no target PSF and are unusable. E029 S107 contains broad spacecraft-like bowls that are excluded, plus a separate narrow eclipse at BTJD 4275.578; S108 has another narrow eclipse on a sloping baseline.

Scoped shared checks find no prior target eclipsing identification in the seven required sources; per-target receipt and shared seal are retained. No negative claim is made from a failed request. Literature checks and scoped catalogue nonmatches do not establish exhaustive priority.

## Limitation and next check

A wider extraction or follow-up can classify the northern variable; do not count the selected target.

Physical tier, Gaia association, source ownership and novelty are recorded separately. Completion means the bounded deciding review is performed, not that every selected lead is a detection. Exact6 reviewed without substitution; previously published E030 excluded upstream. No ledger or publication edit. Evidence/scripts and helper final audit are sealed at batch level.
