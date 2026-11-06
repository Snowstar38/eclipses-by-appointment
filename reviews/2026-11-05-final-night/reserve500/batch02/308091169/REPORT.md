# RS016 — TIC 308091169

Review **complete**; physical tier **REFUTED**; source **known-neighbor-contamination**; Gaia association **not-associated**; publication eligible **false**.

Gaia DR34580706870298334848, selection G=11.636727, P=25.49654615759391d.

Both selected events belong to the known nearby Prsa EB TIC308091162 / Gaia4580706767219118464, catalog period3.35457022d and separation51.38arcsec. Ten S79/80 midpoints yield a local3.35452605d short clock. S26 and S79 difference peaks(2,2)/(4,6) track the known neighbor positions(2.303,1.548)/(4.297,5.880); target positions are(3.972,3.341)/(3.008,3.748). Target3x3 losses are only0.04%/0.17%. The S26 positive near-target centroid is undefined because the actual deficit is outside the restricted weighting region; it is not quoted as an astrometric measurement. Pixel peak/neighbor positions in two orientations are decisive. The long extrapolation phase discrepancy does not establish a separate target event. Gaia25.49655d is unrelated to the short train.

## Raw events and clock

|Sector|Kind guide|Midpoint BTJD|Formal midpoint error d|Depth ppt|Duration d|Local fit usable|
|---|---|---|---|---|---|---|
|26|candidate|2018.9194608346038|0.004930254605317987|6.3903989980226195|0.20201852292323216|True|
|79|candidate|3478.433202180272|0.006689989420547633|6.733771098597227|0.25032829420993885|True|
|79|short|3471.7191379339083|0.004272260120609256|6.211188722463522|0.19502279236393394|True|
|79|short|3468.370694962068|0.012116023910863126|5.226481475600073|0.1731080585531501|True|
|79|short|3465.0356270071134|0.006039683446419714|6.203035703597345|0.40662271031562364|True|
|79|short|3454.9464867035063|0.00673706770790531|5.6670220339621205|0.19698123413570945|True|
|80|short|3481.7921515465705|0.003802091091272307|4.732526655412096|0.22047350712831804|True|
|80|short|3485.14234|0.0|8.62287583192023|0.35|False|
|80|short|3488.49691|0.0|10.921813709716677|0.35|False|
|80|short|3491.854369557929|0.01034921747652117|3.266462240806335|0.14005010162589604|True|
|80|short|3495.2083602060193|0.002968500850556959|4.4221800276193655|0.16369941674543353|True|
|80|short|3498.561547725485|0.0031978565992080077|5.055857224435819|0.2230334855227215|True|
|80|short|3501.9203218418807|0.007356102534701964|3.8782824945504584|0.15768660283466945|True|

Local trapezoid usability is only a numeric quality flag: a fitted trough can be drift, an off-target eclipse or the wrong conjunction kind. It is not an eclipse verdict. Quality-zero finite positive SAP is the primary measurement; flagged finite core cadences are separately retained in the batch raw audit.

Published clock: None; screening/contaminant clock is not a target ephemeris.

No target period is inferred from the selected pattern. Formal clock errors use individual cadence/2 or0.003d floors and remain conditional on selected cycle counts. They are not calibrated coverage intervals. Raw-only alias coverage uses75%core sampling, valid sidebands and an interior-gap limit; absent or flagged coverage is not a null. The separate analytic Gaia-assisted audit tests every positive integer count under the stated source-orbit hypothesis.

## Reduction and source attribution

- [helper-localization-26.json](helper-localization-26.json): sector26, aperture loss0.0004103748693962128, peak[2, 2], target[3.9720173349073598, 3.340869100879961].
- [helper-localization-79.json](helper-localization-79.json): sector79, aperture loss0.0017029008462494666, peak[4, 6], target[3.00813673388991, 3.7477901462055767].

Custom7x7 TESScut/3x3 aperture and QLP KSPSAP are alternative reductions of the same TESS photons, not independent observing occasions. Aperture losses can be diluted and differ between reductions. Difference peaks, target and all returned Gaia neighbor positions were inspected spatially; centroid offsets alone do not exclude unresolved neighbors. G-band flux ratios are contextual and are not compared as intrinsic neighbor loss against a blended fractional deficit. No calibrated PRF or WCS systematic confidence interval is claimed. See each helper receipt and image, lead-neighbors.json and lead-reduction.json.

## Gaia geometry and catalogue scope

Full source-specific SB1 covariance uses lower-triangle parameters P,gamma,K,e,omega,Tp and subindices0,3,4,5. Nonlinear propagation uses100000 draws, seed50701, physical0<=e<1, and conjunction epoch unwrapping before fixed-cycle propagation. The separate RS013 pair test uses200000 draws, seed50702; the RS009/015 conditioned-period test uses200000 draws, seed50703. Edge-on conjunction geometry is an assumption, not an inclination measurement. The conditioning test shares Gaia information with alias selection and is not independent orbit confirmation.

Successful shared checks cover seven source groups defined in canonical methods2.7, with target-specific receipts, scoped exact/cone results, controls and hashes in lead-central-catalogue-receipts.json. Nearby EB entries are adjudicated against the measured signal rather than automatically assigned to the target. Generic non-eclipsing variability classifications do not establish prior EB identification. The literature check covers244 locally fetched eprints with exact queue TIC/Gaia identifiers and is not exhaustive priority evidence. Physical tier, source association, prior-known identity and eligibility remain distinct.

## Limitation and next check

No new target EB claim; retain the known neighbor identity and do not assign its catalogue classification to the target.

Evidence includes lead-context.json, lead-series.json, lead-timing.json, lead-reduction.json, raw/all-sector panels, helper-localization receipts/PNGs/FITS, Gaia-neighbor receipt, central catalogue receipt; batch clock, aliases, Gaia covariance, pair/conditioned tests, current-sector inventory, flagged-raw audit and identity/source hash audits. Exact7 queue; RS011 excluded before full review, no substitution. Parent is final fresh-band-reserve500 download cohort; no ledger/public edits. Lead and independent helper notes and final manifest accompany this report.
