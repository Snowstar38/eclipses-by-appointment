# RS013 — TIC 281540788

Review **complete**; physical tier **PROBABLE**; source **target-supported**; Gaia association **rejected-paired-conjunction-geometry**; publication eligible **true**.

Gaia DR34905403442934128256, selection G=11.580432, P=40.8392487731809d.

Repeated deep eclipses are real. Six same-kind raw midpoints give40.75489255d at cycles0,1,45,63,69,70 with maximum residual0.00167d. The opposite kind occurs12.70980875d later and is never mixed into the clock. Source Gaia period40.83924877d differs2.57sigma, but its eccentric conjunction pair is inconsistent: observed12.70981d versus full-covariance MC median17.89037d and99.73% interval14.33053–20.42365d (two-sided tail2.08e-5). Epoch cancellation makes this stronger than individually propagated late conjunction windows. S1 primary and secondary kinds are independently imaged from the same cutout: aperture losses14.5%/15.2%, target-centered offsets0.132/0.156pixel, both peaks at target pixel(4,3). This establishes both kinds on target at TESS resolution. Physical probable EB is retained with failed Gaia geometry; association to the published Gaia orbit is excluded.

## Raw events and clock

|Sector|Kind guide|Midpoint BTJD|Formal midpoint error d|Depth ppt|Duration d|Local fit usable|
|---|---|---|---|---|---|---|
|1|candidate|1337.3209230801074|0.00020985474052390043|158.49457464351048|0.529470764414334|True|
|1|candidate|1350.0307318332414|0.0001793648608247066|164.7755740598904|0.5137377471221508|True|
|2|candidate|1378.0755881246405|0.00014463456412926314|161.67060530648394|0.5288430341907197|True|
|68|candidate|3171.2908653380523|0.00016321992444174362|159.74810455458274|0.530363718565262|True|
|95|candidate|3904.878500246216|0.0001583185405726079|135.75358821449962|0.5314790771252763|True|
|95|candidate|3895.6150062649135|17311.876700606645|28.705550181287617|0.7187055556364693|False|
|96|candidate|3917.5887265891565|0.00013533512375313186|134.6936939753685|0.5154889603813589|True|
|102|candidate|4149.409952269577|0.00016550752165512354|139.21634217506164|0.5323670673128474|True|
|103|candidate|4162.118897564624|0.00013102313980751522|143.6036539208782|0.5162664544493346|True|
|104|candidate|4202.872636790822|0.00015669274124877248|149.02071177785834|0.5207790295517194|True|
|104|candidate|4190.161918070597|0.00018961154616091232|142.04472565592164|0.5282499713038299|True|

Local trapezoid usability is only a numeric quality flag: a fitted trough can be drift, an off-target eclipse or the wrong conjunction kind. It is not an eclipse verdict. Quality-zero finite positive SAP is the primary measurement; flagged finite core cadences are separately retained in the batch raw audit.

Published clock: {"period_d": 40.75489255006135, "epoch_btjd": 1337.3206986064904, "formal_period_error_d": 9.48515637504626e-05, "cycles": [0, 1, 45, 63, 69, 70], "times": [1337.3209230801074, 1378.0755881246405, 3171.2908653380523, 3904.878500246216, 4149.409952269577, 4190.161918070597], "residuals": [0.00022447361698141322, -3.031911319339997e-06, 1.9788012650678866e-06, -0.0004290141391720681, 0.0016677088533469941, -0.0012590401884153835], "duration_d": 0.529917241489798, "depth_ppt": 150.26965014971606, "max_residual_d": 0.0016677088533469941, "note": "WLS with cadence/2 or .003d floor; two-point errors conditional on integer count; period aliases tested separately. RS010 full orbital period conservatively twice successive equal minima; RS013 separate conjunction kinds."}

Clock from separate same-kind measured midpoints; opposite conjunction kinds are excluded. Formal clock errors use individual cadence/2 or0.003d floors and remain conditional on selected cycle counts. They are not calibrated coverage intervals. Raw-only alias coverage uses75%core sampling, valid sidebands and an interior-gap limit; absent or flagged coverage is not a null. The separate analytic Gaia-assisted audit tests every positive integer count under the stated source-orbit hypothesis.

## Reduction and source attribution

- [helper-localization-1-primary.json](helper-localization-1-primary.json): sector1, aperture loss0.14527181802460243, peak[4, 3], target[3.735145241130965, 3.4967134177723045].
- [helper-localization-1.json](helper-localization-1.json): sector1, aperture loss0.15201974158759646, peak[4, 3], target[3.735145241130965, 3.4967134177723045].

Custom7x7 TESScut/3x3 aperture and QLP KSPSAP are alternative reductions of the same TESS photons, not independent observing occasions. Aperture losses can be diluted and differ between reductions. Difference peaks, target and all returned Gaia neighbor positions were inspected spatially; centroid offsets alone do not exclude unresolved neighbors. G-band flux ratios are contextual and are not compared as intrinsic neighbor loss against a blended fractional deficit. No calibrated PRF or WCS systematic confidence interval is claimed. See each helper receipt and image, lead-neighbors.json and lead-reduction.json.

## Gaia geometry and catalogue scope

Full source-specific SB1 covariance uses lower-triangle parameters P,gamma,K,e,omega,Tp and subindices0,3,4,5. Nonlinear propagation uses100000 draws, seed50701, physical0<=e<1, and conjunction epoch unwrapping before fixed-cycle propagation. The separate RS013 pair test uses200000 draws, seed50702; the RS009/015 conditioned-period test uses200000 draws, seed50703. Edge-on conjunction geometry is an assumption, not an inclination measurement. The conditioning test shares Gaia information with alias selection and is not independent orbit confirmation.

Successful shared checks cover seven source groups defined in canonical methods2.7, with target-specific receipts, scoped exact/cone results, controls and hashes in lead-central-catalogue-receipts.json. Nearby EB entries are adjudicated against the measured signal rather than automatically assigned to the target. Generic non-eclipsing variability classifications do not establish prior EB identification. The literature check covers244 locally fetched eprints with exact queue TIC/Gaia identifiers and is not exhaustive priority evidence. Physical tier, source association, prior-known identity and eligibility remain distinct.

## Limitation and next check

Obtain a revised RV orbit or independent spectroscopy; keep both eclipse kinds spatially checked and do not report Gaia geometry as passed.

Evidence includes lead-context.json, lead-series.json, lead-timing.json, lead-reduction.json, raw/all-sector panels, helper-localization receipts/PNGs/FITS, Gaia-neighbor receipt, central catalogue receipt; batch clock, aliases, Gaia covariance, pair/conditioned tests, current-sector inventory, flagged-raw audit and identity/source hash audits. Exact7 queue; RS011 excluded before full review, no substitution. Parent is final fresh-band-reserve500 download cohort; no ledger/public edits. Lead and independent helper notes and final manifest accompany this report.
