# RS015 — TIC 298976044

Review **complete**; physical tier **CONFIRMED**; source **target-supported**; Gaia association **Gaia-assisted-consistent**; publication eligible **true**.

Gaia DR31900237292895732352, selection G=11.606545, P=50.9602481957259d.

Two clear bounded rounded raw eclipses at1732.901356 and3567.462422 have~100ppt fitted depths. The conditional36-cycle clock is50.96002962d. Raw-only aliases survive coverage in sectors15/16/56/83; no newer sector was found. Source Gaia period50.96024820d uniquely admits36positive integer cycles within3sigma (neighboring aliases>44sigma away). After full covariance conditioning on the measured period, the same-conjunction epoch remains consistent at a two-sided tail~0.072. S83 independent custom aperture recovers8.62% loss and a target-centered deficit0.086pixel away.

## Raw events and clock

|Sector|Kind guide|Midpoint BTJD|Formal midpoint error d|Depth ppt|Duration d|Local fit usable|
|---|---|---|---|---|---|---|
|15|candidate|1732.9013558069632|0.0005617903566933753|99.22984583456883|0.378169004923562|True|
|83|candidate|3567.4624220808246|0.00026018349359285413|103.47699853971992|0.37511447669745424|True|

Local trapezoid usability is only a numeric quality flag: a fitted trough can be drift, an off-target eclipse or the wrong conjunction kind. It is not an eclipse verdict. Quality-zero finite positive SAP is the primary measurement; flagged finite core cadences are separately retained in the batch raw audit.

Published clock: {"period_d": 50.96002961871849, "epoch_btjd": 1732.9013558069612, "formal_period_error_d": 0.0003011315336078535, "cycles": [0, 36], "times": [1732.9013558069632, 3567.4624220808246], "residuals": [2.0463630789890885e-12, -2.2737367544323206e-12], "duration_d": 0.3766417408105081, "depth_ppt": 101.35342218714437, "max_residual_d": 2.2737367544323206e-12, "note": "WLS with cadence/2 or .003d floor; two-point errors conditional on integer count; period aliases tested separately. RS010 full orbital period conservatively twice successive equal minima; RS013 separate conjunction kinds."}

Gaia-assisted, conditional on the target source-orbit and same-kind identification. Raw photometric aliases remain. Conditioned Gaia epoch consistency is not independent validation. Formal clock errors use individual cadence/2 or0.003d floors and remain conditional on selected cycle counts. They are not calibrated coverage intervals. Raw-only alias coverage uses75%core sampling, valid sidebands and an interior-gap limit; absent or flagged coverage is not a null. The separate analytic Gaia-assisted audit tests every positive integer count under the stated source-orbit hypothesis.

## Reduction and source attribution

- [helper-localization-83.json](helper-localization-83.json): sector83, aperture loss0.0862405511689841, peak[4, 4], target[3.760527653902386, 3.6925924620016213].

Custom7x7 TESScut/3x3 aperture and QLP KSPSAP are alternative reductions of the same TESS photons, not independent observing occasions. Aperture losses can be diluted and differ between reductions. Difference peaks, target and all returned Gaia neighbor positions were inspected spatially; centroid offsets alone do not exclude unresolved neighbors. G-band flux ratios are contextual and are not compared as intrinsic neighbor loss against a blended fractional deficit. No calibrated PRF or WCS systematic confidence interval is claimed. See each helper receipt and image, lead-neighbors.json and lead-reduction.json.

## Gaia geometry and catalogue scope

Full source-specific SB1 covariance uses lower-triangle parameters P,gamma,K,e,omega,Tp and subindices0,3,4,5. Nonlinear propagation uses100000 draws, seed50701, physical0<=e<1, and conjunction epoch unwrapping before fixed-cycle propagation. The separate RS013 pair test uses200000 draws, seed50702; the RS009/015 conditioned-period test uses200000 draws, seed50703. Edge-on conjunction geometry is an assumption, not an inclination measurement. The conditioning test shares Gaia information with alias selection and is not independent orbit confirmation.

Successful shared checks cover seven source groups defined in canonical methods2.7, with target-specific receipts, scoped exact/cone results, controls and hashes in lead-central-catalogue-receipts.json. Nearby EB entries are adjudicated against the measured signal rather than automatically assigned to the target. Generic non-eclipsing variability classifications do not establish prior EB identification. The literature check covers244 locally fetched eprints with exact queue TIC/Gaia identifiers and is not exhaustive priority evidence. Physical tier, source association, prior-known identity and eligibility remain distinct.

## Limitation and next check

Obtain a third same-kind eclipse for a Gaia-independent clock; preserve the conditional period error and explicitly Gaia-assisted inference.

Evidence includes lead-context.json, lead-series.json, lead-timing.json, lead-reduction.json, raw/all-sector panels, helper-localization receipts/PNGs/FITS, Gaia-neighbor receipt, central catalogue receipt; batch clock, aliases, Gaia covariance, pair/conditioned tests, current-sector inventory, flagged-raw audit and identity/source hash audits. Exact7 queue; RS011 excluded before full review, no substitution. Parent is final fresh-band-reserve500 download cohort; no ledger/public edits. Lead and independent helper notes and final manifest accompany this report.
