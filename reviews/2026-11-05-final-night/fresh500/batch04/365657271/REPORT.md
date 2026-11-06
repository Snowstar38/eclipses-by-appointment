# E034 — TIC 365657271

Review complete. Physical tier: **CONFIRMED**. Gaia DR3 6634669941888721408; selection P=41.648935513604755d,G=11.752435.

Three resolved flat-bottom raw events in S13/S93/S104 give41.659387d with cycles0/52/60. The partial S39 terminal event is qualitatively consistent but excluded from midpoint fitting. Target-centered S93 difference image and custom3x3 extraction confirm eclipse morphology. Divisors2–6 have covered nulls; photometry retains83.31883,55.54589 and27.77294d alternatives. Source-specific Gaia41.648936d orbit and full nonlinear conjunction covariance uniquely select the41.659387d clock among tested aliases. The joint Gaia-assisted cycle choice is stated explicitly; photometry alone is not unique.

## Representative raw measurements

|Sector|fit midpoint BTJD|formal error d|depth ppt|duration d|usable midpoint|
|---|---|---|---|---|---|
|13|1681.1124260961242|0.003691511240732351|6.032279819414537|0.7449274819160366|True|
|39|2389.2557879771257|0.11162627349990688|5.2668244754358104|0.6146981623959321|False|
|93|3847.3863104390102|0.0036474855697023216|6.218034689642737|0.7089436735725717|True|
|104|4180.677465748128|0.004598931425654189|4.852410998273032|0.6523736160060418|True|

Reported period=41.659387210584114d; local formal error=0.00018945116548964216d. Clock and cycle choices are in lead-clocks.json. Timing uncertainties are local formal fit errors; clock fits use cadence/2 or .004d floor for E034. They do not incorporate all systematics. Gap-cut midpoints are excluded explicitly. E029 has three events including adjacent S107/S108 eclipses; tested photometric timing alternatives do not survive. E034 representative residuals reach.0086d.

## Method and source attribution

Quality-zero finite positive raw SAP is primary evidence; all cached sector contexts and representative discrete events were inspected. KSPSAP and custom TESScut apertures reuse the same photons. Missing/gap-cut or flagged windows are not clean nulls. Aliases test divisors2–6 and endpoint integer alternatives over approximately5–100d; lead-alias-summary.json and lead-alias-covered-windows.json preserve each compatible alternative and covered raw evidence. Geometry uses this source's SB1 full covariance with edge-on conjunction assumptions, both conjunction kinds and a fixed integer cycle. Nonlinear draws unwrap base conjunction about nominal before propagating the fixed cycle; seed50701 and100000draws. Geometry is an association check, not an inclination measurement or exact physical model.

Pixel result: {"status": "measured", "target_xy": [3.1952916225010792, 3.6157801403024123], "positive_diff_centroid_xy": [3.3917993673421796, 3.6831585670275286], "centroid_offset_pixels": 0.2077381673416969, "aperture_loss": 0.0066043654439655874}. Pixels and Gaia-neighbor geometry are considered together. E032's target aperture alone is contaminated and does not establish ownership. E029 S107/S108 source and event shapes pass a separate helper audit, with two-orientation Gaussian image bootstrap retained. E028/E033 have no credible discrete eclipse to localize; omitting pixel extraction does not manufacture a negative source test.

## Current availability and catalogue scope

lead-current-sector-inventory.json records successful current MAST sector responses. Bounded extras: E029S87/107/108/109 and E031S65/102 are preserved in lead-extra-sector-receipts.json and per-sector FITS/NPZ/plots. E029S87 and E031S65/S102 have near-zero flux/no target PSF and are unusable. E029 S107 contains broad spacecraft-like bowls that are excluded, plus a separate narrow eclipse at BTJD 4275.578; S108 has another narrow eclipse on a sloping baseline.

Scoped shared checks find no prior target eclipsing identification in the seven required sources; per-target receipt and shared seal are retained. No negative claim is made from a failed request. Literature checks and scoped catalogue nonmatches do not establish exhaustive priority.

## Limitation and next check

An eclipse outside the common4-cycle spacing would remove purely photometric integer ambiguity; additional sectors can refine representative timing.

Physical tier, Gaia association, source ownership and novelty are recorded separately. Completion means the bounded deciding review is performed, not that every selected lead is a detection. Exact6 reviewed without substitution; previously published E030 excluded upstream. No ledger or publication edit. Evidence/scripts and helper final audit are sealed at batch level.
