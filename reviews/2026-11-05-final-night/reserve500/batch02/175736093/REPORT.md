# RS009 — TIC 175736093

Review **complete**; physical tier **CONFIRMED**; source **target-supported**; Gaia association **Gaia-assisted-consistent**; publication eligible **true**.

Gaia DR33678144914950124288, selection G=11.731341, P=26.05597812473687d.

Two bounded raw eclipses at BTJD2568.765270 and3794.018769 recover ~30ppt depths. The conditional47-cycle clock is26.06922338d. Raw-only integer aliases survive the limited sectors46/91. Exhaustive positive-integer cycle bounds using the source Gaia period leave only47cycles within3sigma; nearest alternatives differ25.7/28.2sigma. Full covariance conditioning on the measured clock leaves the same-conjunction epoch consistent (two-sided tail~0.152). Independent S91 custom aperture recovers2.82% loss with target-centered deficit0.047pixel away.

## Raw events and clock

|Sector|Kind guide|Midpoint BTJD|Formal midpoint error d|Depth ppt|Duration d|Local fit usable|
|---|---|---|---|---|---|---|
|46|candidate|2568.765270004284|0.0008359719794370609|29.700918080579946|0.2693246543216204|True|
|91|candidate|3794.0187689876284|0.0006679243415004319|30.060817468946166|0.2653484317026947|True|

Local trapezoid usability is only a numeric quality flag: a fitted trough can be drift, an off-target eclipse or the wrong conjunction kind. It is not an eclipse verdict. Quality-zero finite positive SAP is the primary measurement; flagged finite core cadences are separately retained in the batch raw audit.

Published clock: {"period_d": 26.069223382624383, "epoch_btjd": 2568.765270004284, "formal_period_error_d": 9.763769377628115e-05, "cycles": [0, 47], "times": [2568.765270004284, 3794.0187689876284], "residuals": [0.0, -1.8189894035458565e-12], "duration_d": 0.26733654301215753, "depth_ppt": 29.880867774763054, "max_residual_d": 1.8189894035458565e-12, "note": "WLS with cadence/2 or .003d floor; two-point errors conditional on integer count; period aliases tested separately. RS010 full orbital period conservatively twice successive equal minima; RS013 separate conjunction kinds."}

Gaia-assisted, conditional on the target source-orbit and same-kind identification. Raw photometric aliases remain. Conditioned Gaia epoch consistency is not independent validation. Formal clock errors use individual cadence/2 or0.003d floors and remain conditional on selected cycle counts. They are not calibrated coverage intervals. Raw-only alias coverage uses75%core sampling, valid sidebands and an interior-gap limit; absent or flagged coverage is not a null. The separate analytic Gaia-assisted audit tests every positive integer count under the stated source-orbit hypothesis.

## Reduction and source attribution

- [helper-localization-91.json](helper-localization-91.json): sector91, aperture loss0.028235827145396852, peak[3, 4], target[3.2384092035288665, 3.7931798888064625].

Custom7x7 TESScut/3x3 aperture and QLP KSPSAP are alternative reductions of the same TESS photons, not independent observing occasions. Aperture losses can be diluted and differ between reductions. Difference peaks, target and all returned Gaia neighbor positions were inspected spatially; centroid offsets alone do not exclude unresolved neighbors. G-band flux ratios are contextual and are not compared as intrinsic neighbor loss against a blended fractional deficit. No calibrated PRF or WCS systematic confidence interval is claimed. See each helper receipt and image, lead-neighbors.json and lead-reduction.json.

## Gaia geometry and catalogue scope

Full source-specific SB1 covariance uses lower-triangle parameters P,gamma,K,e,omega,Tp and subindices0,3,4,5. Nonlinear propagation uses100000 draws, seed50701, physical0<=e<1, and conjunction epoch unwrapping before fixed-cycle propagation. The separate RS013 pair test uses200000 draws, seed50702; the RS009/015 conditioned-period test uses200000 draws, seed50703. Edge-on conjunction geometry is an assumption, not an inclination measurement. The conditioning test shares Gaia information with alias selection and is not independent orbit confirmation.

Successful shared checks cover seven source groups defined in canonical methods2.7, with target-specific receipts, scoped exact/cone results, controls and hashes in lead-central-catalogue-receipts.json. Nearby EB entries are adjudicated against the measured signal rather than automatically assigned to the target. Generic non-eclipsing variability classifications do not establish prior EB identification. The literature check covers244 locally fetched eprints with exact queue TIC/Gaia identifiers and is not exhaustive priority evidence. Physical tier, source association, prior-known identity and eligibility remain distinct.

## Limitation and next check

Obtain a third complete same-kind eclipse to resolve the clock independently of Gaia; retain Gaia-assisted dependence and conditional timing error.

Evidence includes lead-context.json, lead-series.json, lead-timing.json, lead-reduction.json, raw/all-sector panels, helper-localization receipts/PNGs/FITS, Gaia-neighbor receipt, central catalogue receipt; batch clock, aliases, Gaia covariance, pair/conditioned tests, current-sector inventory, flagged-raw audit and identity/source hash audits. Exact7 queue; RS011 excluded before full review, no substitution. Parent is final fresh-band-reserve500 download cohort; no ledger/public edits. Lead and independent helper notes and final manifest accompany this report.
