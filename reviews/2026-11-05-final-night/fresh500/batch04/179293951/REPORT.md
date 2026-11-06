# E031 — TIC 179293951

Review complete. Physical tier: **PLAUSIBLE**. Gaia DR3 6110086209770411264; selection P=51.40506253188426d,G=11.576324.

The bounded deep S11 eclipse has resolved ingress, flat bottom and recovery, centered on the target in a fresh pixel extraction. S38 has a shallower partial dip emerging from a gap, without a valid midpoint or demonstrated same-kind recurrence. Its fitted midpoint is explicitly unusable despite a numerically finite covariance. Fresh S65/S102 cutouts contain no stellar PSF and near-zero flux, so they are unavailable evidence, not clean nulls. No period is assigned.

## Representative raw measurements

|Sector|fit midpoint BTJD|formal error d|depth ppt|duration d|usable midpoint|
|---|---|---|---|---|---|
|11|1603.3550181058597|0.002216914125694064|20.95929939951178|1.5788348193918988|True|
|38|2347.961851746791|0.016663057286829635|10.975369920645532|1.7791376761361457|False|

Reported period=unresolvedd; local formal error=not assignedd. Clock and cycle choices are in lead-clocks.json. Timing uncertainties are local formal fit errors; clock fits use cadence/2 or .004d floor for E034. They do not incorporate all systematics. Gap-cut midpoints are excluded explicitly. E029 has three events including adjacent S107/S108 eclipses; tested photometric timing alternatives do not survive. E034 representative residuals reach.0086d.

## Method and source attribution

Quality-zero finite positive raw SAP is primary evidence; all cached sector contexts and representative discrete events were inspected. KSPSAP and custom TESScut apertures reuse the same photons. Missing/gap-cut or flagged windows are not clean nulls. Aliases test divisors2–6 and endpoint integer alternatives over approximately5–100d; lead-alias-summary.json and lead-alias-covered-windows.json preserve each compatible alternative and covered raw evidence. Geometry uses this source's SB1 full covariance with edge-on conjunction assumptions, both conjunction kinds and a fixed integer cycle. Nonlinear draws unwrap base conjunction about nominal before propagating the fixed cycle; seed50701 and100000draws. Geometry is an association check, not an inclination measurement or exact physical model.

Pixel result: {"status": "measured", "target_xy": [3.0159394167579316, 3.50471542663389], "positive_diff_centroid_xy": [3.1326508800319113, 3.7835823287162214], "centroid_offset_pixels": 0.3023050028308332, "aperture_loss": 0.022749592429660348}. Pixels and Gaia-neighbor geometry are considered together. E032's target aperture alone is contaminated and does not establish ownership. E029 S107/S108 source and event shapes pass a separate helper audit, with two-orientation Gaussian image bootstrap retained. E028/E033 have no credible discrete eclipse to localize; omitting pixel extraction does not manufacture a negative source test.

## Current availability and catalogue scope

lead-current-sector-inventory.json records successful current MAST sector responses. Bounded extras: E029S87/107/108/109 and E031S65/102 are preserved in lead-extra-sector-receipts.json and per-sector FITS/NPZ/plots. E029S87 and E031S65/S102 have near-zero flux/no target PSF and are unusable. E029 S107 contains broad spacecraft-like bowls that are excluded, plus a separate narrow eclipse at BTJD 4275.578; S108 has another narrow eclipse on a sloping baseline.

Scoped shared checks find no prior target eclipsing identification in the seven required sources; per-target receipt and shared seal are retained. No negative claim is made from a failed request. Literature checks and scoped catalogue nonmatches do not establish exhaustive priority.

## Limitation and next check

Another complete same-kind event is required; obtain usable later-sector stellar photometry and test integer cycles.

Physical tier, Gaia association, source ownership and novelty are recorded separately. Completion means the bounded deciding review is performed, not that every selected lead is a detection. Exact6 reviewed without substitution; previously published E030 excluded upstream. No ledger or publication edit. Evidence/scripts and helper final audit are sealed at batch level.
