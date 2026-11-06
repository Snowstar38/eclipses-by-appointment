# RS017 — TIC 403192875

Review **complete**; physical tier **CONFIRMED**; source **target-supported**; Gaia association **consistent**; publication eligible **true**.

Gaia DR36505393724082679552, selection G=11.993226, P=35.92198847825894d.

Three raw midpoints at3176.370105/4146.486119/4182.415728 give35.93021098d at cycles0/27/28 with maximum residual0.00031d. S68/104 have complete bounded23/22ppt eclipses; S102 ingress is interrupted, so it supplies a midpoint only after shifting the initial search guide to the measured trough. Third-event timing and covered-null tests remove other tested integer/divisor aliases. Gaia period differs0.80sigma and the same conjunction is within~1sigma of source covariance predictions. S68 custom aperture recovers2.17% eclipse and target-centered deficit0.164pixel away. The VSX RS entry is generic non-eclipsing variability and does not establish a prior EB identification.

## Raw events and clock

|Sector|Kind guide|Midpoint BTJD|Formal midpoint error d|Depth ppt|Duration d|Local fit usable|
|---|---|---|---|---|---|---|
|68|A|3176.370105200847|0.0011646222030326017|24.172984798935328|0.45763494151142153|True|
|102|A|4146.486118590528|0.0010772386420327537|23.6566213661211|0.47708040018972464|True|
|104|A|4182.415728477595|0.0009724238490317491|21.525527813693447|0.47326739997595946|True|

Local trapezoid usability is only a numeric quality flag: a fitted trough can be drift, an off-target eclipse or the wrong conjunction kind. It is not an eclipse verdict. Quality-zero finite positive SAP is the primary measurement; flagged finite core cadences are separately retained in the batch raw audit.

Published clock: {"period_d": 35.93021097962852, "epoch_btjd": 3176.3701161298004, "formal_period_error_d": 0.0001335423284979729, "cycles": [0, 27, 28], "times": [3176.370105200847, 4146.486118590528, 4182.415728477595], "residuals": [-1.0928953543043463e-05, 0.00030601075832237257, -0.00029508180432458175], "duration_d": 0.47326739997595946, "depth_ppt": 23.6566213661211, "max_residual_d": 0.00030601075832237257, "note": "WLS with cadence/2 or .003d floor; two-point errors conditional on integer count; period aliases tested separately. RS010 full orbital period conservatively twice successive equal minima; RS013 separate conjunction kinds."}

Clock from separate same-kind measured midpoints; opposite conjunction kinds are excluded. Formal clock errors use individual cadence/2 or0.003d floors and remain conditional on selected cycle counts. They are not calibrated coverage intervals. Raw-only alias coverage uses75%core sampling, valid sidebands and an interior-gap limit; absent or flagged coverage is not a null. The separate analytic Gaia-assisted audit tests every positive integer count under the stated source-orbit hypothesis.

## Reduction and source attribution

- [helper-localization-68.json](helper-localization-68.json): sector68, aperture loss0.021739902936755318, peak[4, 3], target[3.4953852100600953, 3.447093390308451].

Custom7x7 TESScut/3x3 aperture and QLP KSPSAP are alternative reductions of the same TESS photons, not independent observing occasions. Aperture losses can be diluted and differ between reductions. Difference peaks, target and all returned Gaia neighbor positions were inspected spatially; centroid offsets alone do not exclude unresolved neighbors. G-band flux ratios are contextual and are not compared as intrinsic neighbor loss against a blended fractional deficit. No calibrated PRF or WCS systematic confidence interval is claimed. See each helper receipt and image, lead-neighbors.json and lead-reduction.json.

## Gaia geometry and catalogue scope

Full source-specific SB1 covariance uses lower-triangle parameters P,gamma,K,e,omega,Tp and subindices0,3,4,5. Nonlinear propagation uses100000 draws, seed50701, physical0<=e<1, and conjunction epoch unwrapping before fixed-cycle propagation. The separate RS013 pair test uses200000 draws, seed50702; the RS009/015 conditioned-period test uses200000 draws, seed50703. Edge-on conjunction geometry is an assumption, not an inclination measurement. The conditioning test shares Gaia information with alias selection and is not independent orbit confirmation.

Successful shared checks cover seven source groups defined in canonical methods2.7, with target-specific receipts, scoped exact/cone results, controls and hashes in lead-central-catalogue-receipts.json. Nearby EB entries are adjudicated against the measured signal rather than automatically assigned to the target. Generic non-eclipsing variability classifications do not establish prior EB identification. The literature check covers244 locally fetched eprints with exact queue TIC/Gaia identifiers and is not exhaustive priority evidence. Physical tier, source association, prior-known identity and eligibility remain distinct.

## Limitation and next check

More complete events can improve the ephemeris; retain cadence and spatial-model systematic limits.

Evidence includes lead-context.json, lead-series.json, lead-timing.json, lead-reduction.json, raw/all-sector panels, helper-localization receipts/PNGs/FITS, Gaia-neighbor receipt, central catalogue receipt; batch clock, aliases, Gaia covariance, pair/conditioned tests, current-sector inventory, flagged-raw audit and identity/source hash audits. Exact7 queue; RS011 excluded before full review, no substitution. Parent is final fresh-band-reserve500 download cohort; no ledger/public edits. Lead and independent helper notes and final manifest accompany this report.
