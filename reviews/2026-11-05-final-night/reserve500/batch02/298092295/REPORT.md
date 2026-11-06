# RS014 — TIC 298092295

Review **complete**; physical tier **REFUTED**; source **no-established-eclipse-source**; Gaia association **not-established**; publication eligible **false**.

Gaia DR31665388584229668224, selection G=11.684077, P=27.932082000052453d.

The selected S14 SAP depressions at~1690.4/1694.5 sit in structured drift and smooth changing minima, without a secure discrete same-kind eclipse train. Local fitted trough depths8–10ppt are descriptive fits, not established eclipses; KSPSAP attenuates corresponding core contrasts to2.3/5.0ppt. The wider raw context includes strong rising ramps and resets. Seven other extracted sectors show no secure matching raw eclipse morphology. Completed review refutes the selected eclipse interpretation, while making no exhaustive all-sector nondetection or on-target variability claim.

## Raw events and clock

|Sector|Kind guide|Midpoint BTJD|Formal midpoint error d|Depth ppt|Duration d|Local fit usable|
|---|---|---|---|---|---|---|
|14|candidate|1690.4023107724709|0.0076269381330928985|8.044166735992253|0.349265504675732|True|
|14|candidate|1694.4734463101042|0.019850108512522075|9.515401891231788|0.23351060894923972|True|

Local trapezoid usability is only a numeric quality flag: a fitted trough can be drift, an off-target eclipse or the wrong conjunction kind. It is not an eclipse verdict. Quality-zero finite positive SAP is the primary measurement; flagged finite core cadences are separately retained in the batch raw audit.

Published clock: None; screening/contaminant clock is not a target ephemeris.

No target period is inferred from the selected pattern. Formal clock errors use individual cadence/2 or0.003d floors and remain conditional on selected cycle counts. They are not calibrated coverage intervals. Raw-only alias coverage uses75%core sampling, valid sidebands and an interior-gap limit; absent or flagged coverage is not a null. The separate analytic Gaia-assisted audit tests every positive integer count under the stated source-orbit hypothesis.

## Reduction and source attribution

No new cutout was required for the refuted morphology interpretation.

Custom7x7 TESScut/3x3 aperture and QLP KSPSAP are alternative reductions of the same TESS photons, not independent observing occasions. Aperture losses can be diluted and differ between reductions. Difference peaks, target and all returned Gaia neighbor positions were inspected spatially; centroid offsets alone do not exclude unresolved neighbors. G-band flux ratios are contextual and are not compared as intrinsic neighbor loss against a blended fractional deficit. No calibrated PRF or WCS systematic confidence interval is claimed. See each helper receipt and image, lead-neighbors.json and lead-reduction.json.

## Gaia geometry and catalogue scope

Full source-specific SB1 covariance uses lower-triangle parameters P,gamma,K,e,omega,Tp and subindices0,3,4,5. Nonlinear propagation uses100000 draws, seed50701, physical0<=e<1, and conjunction epoch unwrapping before fixed-cycle propagation. The separate RS013 pair test uses200000 draws, seed50702; the RS009/015 conditioned-period test uses200000 draws, seed50703. Edge-on conjunction geometry is an assumption, not an inclination measurement. The conditioning test shares Gaia information with alias selection and is not independent orbit confirmation.

Successful shared checks cover seven source groups defined in canonical methods2.7, with target-specific receipts, scoped exact/cone results, controls and hashes in lead-central-catalogue-receipts.json. Nearby EB entries are adjudicated against the measured signal rather than automatically assigned to the target. Generic non-eclipsing variability classifications do not establish prior EB identification. The literature check covers244 locally fetched eprints with exact queue TIC/Gaia identifiers and is not exhaustive priority evidence. Physical tier, source association, prior-known identity and eligibility remain distinct.

## Limitation and next check

Any future claim requires resolved bounded raw eclipses, demonstrated recurrence and source attribution.

Evidence includes lead-context.json, lead-series.json, lead-timing.json, lead-reduction.json, raw/all-sector panels, helper-localization receipts/PNGs/FITS, Gaia-neighbor receipt, central catalogue receipt; batch clock, aliases, Gaia covariance, pair/conditioned tests, current-sector inventory, flagged-raw audit and identity/source hash audits. Exact7 queue; RS011 excluded before full review, no substitution. Parent is final fresh-band-reserve500 download cohort; no ledger/public edits. Lead and independent helper notes and final manifest accompany this report.
