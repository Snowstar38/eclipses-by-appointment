# E028 — TIC 39053050

Review complete. Physical tier: **UNRESOLVED**. Gaia DR3 4413932942296878592; selection P=56.31520497033753d,G=11.6307535.

Only S51 has usable cached QLP. Whole-sector raw SAP shows sparse roughly5ppt scatter and a long central gap; the selected compact feature is not securely distinguished from noise. No high-confidence eclipse morphology or clock is established. This is a completed noise-limited review, not an unperformed check or a physical proof of non-eclipsing behavior.

## Representative raw measurements

|Sector|fit midpoint BTJD|formal error d|depth ppt|duration d|usable midpoint|
|---|---|---|---|---|---|


Reported period=unresolvedd; local formal error=not assignedd. Clock and cycle choices are in lead-clocks.json. Timing uncertainties are local formal fit errors; clock fits use cadence/2 or .004d floor for E034. They do not incorporate all systematics. Gap-cut midpoints are excluded explicitly. E029 has three events including adjacent S107/S108 eclipses; tested photometric timing alternatives do not survive. E034 representative residuals reach.0086d.

## Method and source attribution

Quality-zero finite positive raw SAP is primary evidence; all cached sector contexts and representative discrete events were inspected. KSPSAP and custom TESScut apertures reuse the same photons. Missing/gap-cut or flagged windows are not clean nulls. Aliases test divisors2–6 and endpoint integer alternatives over approximately5–100d; lead-alias-summary.json and lead-alias-covered-windows.json preserve each compatible alternative and covered raw evidence. Geometry uses this source's SB1 full covariance with edge-on conjunction assumptions, both conjunction kinds and a fixed integer cycle. Nonlinear draws unwrap base conjunction about nominal before propagating the fixed cycle; seed50701 and100000draws. Geometry is an association check, not an inclination measurement or exact physical model.

Pixel result: {"status": null, "target_xy": null, "positive_diff_centroid_xy": null, "centroid_offset_pixels": null, "aperture_loss": null}. Pixels and Gaia-neighbor geometry are considered together. E032's target aperture alone is contaminated and does not establish ownership. E029 S107/S108 source and event shapes pass a separate helper audit, with two-orientation Gaussian image bootstrap retained. E028/E033 have no credible discrete eclipse to localize; omitting pixel extraction does not manufacture a negative source test.

## Current availability and catalogue scope

lead-current-sector-inventory.json records successful current MAST sector responses. Bounded extras: E029S87/107/108/109 and E031S65/102 are preserved in lead-extra-sector-receipts.json and per-sector FITS/NPZ/plots. E029S87 and E031S65/S102 have near-zero flux/no target PSF and are unusable. E029 S107 contains broad spacecraft-like bowls that are excluded, plus a separate narrow eclipse at BTJD 4275.578; S108 has another narrow eclipse on a sloping baseline.

Scoped shared checks find no prior target eclipsing identification in the seven required sources; per-target receipt and shared seal are retained. No negative claim is made from a failed request. Literature checks and scoped catalogue nonmatches do not establish exhaustive priority.

## Limitation and next check

Higher precision or another discrete event is needed; no target addition is warranted.

Physical tier, Gaia association, source ownership and novelty are recorded separately. Completion means the bounded deciding review is performed, not that every selected lead is a detection. Exact6 reviewed without substitution; previously published E030 excluded upstream. No ledger or publication edit. Evidence/scripts and helper final audit are sealed at batch level.
