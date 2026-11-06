# RS010 — TIC 187242860

Review **complete**; physical tier **REFUTED**; source **off-target-neighbor**; Gaia association **not-associated**; publication eligible **false**.

Gaia DR35635502902062072320, selection G=11.906066, P=48.45043840622837d.

Repeated ~9ppt minima follow a0.78114d cadence (conservative double-minimum guide1.562282d), unrelated to the48.45044d Gaia orbit. S35 difference peak(6,3) lies on Gaia5635500054501795712 at(6.218,3.284), while target is(3.894,3.712). Target-centered3x3 aperture recovers only0.26% loss. The short signal disappears in S99; a clean covered prediction at4066.30471 has only1.13ppt depth. Spatial ownership, rather than the sector-dependent depth alone, refutes a target eclipsing claim.

## Raw events and clock

|Sector|Kind guide|Midpoint BTJD|Formal midpoint error d|Depth ppt|Duration d|Local fit usable|
|---|---|---|---|---|---|---|
|8|candidate|1538.5342851794785|0.01990986720742432|8.987334277754647|0.2051772695705792|True|
|8|candidate|1539.315398596668|0.016000225402669235|8.268933498645547|0.21694576769189042|True|
|8|candidate|1519.0047631361472|0.013909891251843136|8.688085173495416|0.21355357804893146|True|
|8|candidate|1520.5680093303497|0.016220828255132998|9.318254048516238|0.2182596954969375|True|
|35|candidate|2273.5904661497293|0.011714635105921299|9.564755762736718|0.2323883420779878|True|
|35|candidate|2278.2753477753718|0.009423277554977464|10.894905671339892|0.2370655509135476|True|
|35|candidate|2258.7401072318858|0.010232851910109055|9.268450977827026|0.20077828681665658|True|
|35|candidate|2275.933350982484|0.012573854508483064|8.828015870775944|0.21097702819335182|True|
|62|candidate|3003.952902821998|0.005831400287307509|8.87859659883322|0.21653040030827933|True|
|62|candidate|2996.9254685414185|0.00518636960662813|8.592622020728776|0.21754783611850748|True|
|62|candidate|3010.984197884844|0.005365884859609557|9.086445798973603|0.21804062380318484|True|
|62|candidate|3003.176043021716|0.00533128331499527|9.84707037071997|0.25046488003228135|True|

Local trapezoid usability is only a numeric quality flag: a fitted trough can be drift, an off-target eclipse or the wrong conjunction kind. It is not an eclipse verdict. Quality-zero finite positive SAP is the primary measurement; flagged finite core cadences are separately retained in the batch raw audit.

Published clock: None; screening/contaminant clock is not a target ephemeris.

No target period is inferred from the selected pattern. Formal clock errors use individual cadence/2 or0.003d floors and remain conditional on selected cycle counts. They are not calibrated coverage intervals. Raw-only alias coverage uses75%core sampling, valid sidebands and an interior-gap limit; absent or flagged coverage is not a null. The separate analytic Gaia-assisted audit tests every positive integer count under the stated source-orbit hypothesis.

## Reduction and source attribution

- [helper-localization-35.json](helper-localization-35.json): sector35, aperture loss0.0026080120104486904, peak[6, 3], target[3.894416053596359, 3.7115094584624693].

Custom7x7 TESScut/3x3 aperture and QLP KSPSAP are alternative reductions of the same TESS photons, not independent observing occasions. Aperture losses can be diluted and differ between reductions. Difference peaks, target and all returned Gaia neighbor positions were inspected spatially; centroid offsets alone do not exclude unresolved neighbors. G-band flux ratios are contextual and are not compared as intrinsic neighbor loss against a blended fractional deficit. No calibrated PRF or WCS systematic confidence interval is claimed. See each helper receipt and image, lead-neighbors.json and lead-reduction.json.

## Gaia geometry and catalogue scope

Full source-specific SB1 covariance uses lower-triangle parameters P,gamma,K,e,omega,Tp and subindices0,3,4,5. Nonlinear propagation uses100000 draws, seed50701, physical0<=e<1, and conjunction epoch unwrapping before fixed-cycle propagation. The separate RS013 pair test uses200000 draws, seed50702; the RS009/015 conditioned-period test uses200000 draws, seed50703. Edge-on conjunction geometry is an assumption, not an inclination measurement. The conditioning test shares Gaia information with alias selection and is not independent orbit confirmation.

Successful shared checks cover seven source groups defined in canonical methods2.7, with target-specific receipts, scoped exact/cone results, controls and hashes in lead-central-catalogue-receipts.json. Nearby EB entries are adjudicated against the measured signal rather than automatically assigned to the target. Generic non-eclipsing variability classifications do not establish prior EB identification. The literature check covers244 locally fetched eprints with exact queue TIC/Gaia identifiers and is not exhaustive priority evidence. Physical tier, source association, prior-known identity and eligibility remain distinct.

## Limitation and next check

The neighboring eclipser may be characterized separately; no new target EB claim or target by-catch is established.

Evidence includes lead-context.json, lead-series.json, lead-timing.json, lead-reduction.json, raw/all-sector panels, helper-localization receipts/PNGs/FITS, Gaia-neighbor receipt, central catalogue receipt; batch clock, aliases, Gaia covariance, pair/conditioned tests, current-sector inventory, flagged-raw audit and identity/source hash audits. Exact7 queue; RS011 excluded before full review, no substitution. Parent is final fresh-band-reserve500 download cohort; no ledger/public edits. Lead and independent helper notes and final manifest accompany this report.
