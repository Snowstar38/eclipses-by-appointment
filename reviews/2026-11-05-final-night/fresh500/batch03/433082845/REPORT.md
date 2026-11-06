# E024 - TIC 433082845

Review complete; physical tier **PLAUSIBLE**. Gaia DR3 6075466814881601920; selection P=31.807163419414206d,G=11.957566.

S10/S11 have sparse few-cadence depressions with no demonstrated coherent same-kind recurrence; S101 selection is a gap-start recovery and excluded as a timing event. Independent S10 difference image is broad/off-target, offset1.65pixels, and does not identify the target as eclipser. Nearby VSX EB Gaia6075466608713257728 at31.95arcsec has0.338608d period and is retained as a possible contaminant, not assigned as prior target EB.

## Representative raw measurements

|Sector|midpoint BTJD|formal fit error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
|10|1577.3485204193337|0.0020408575101125872|8.037925467431457|0.12956245699826924|True|
|10|1591.666920284236|0.0034775872916792024|8.019143949748528|0.15899364403765223|True|
|10|1592.7647981183727|0.003826610745531757|8.606000853962959|0.1765554477246519|True|
|10|1574.0486301466176|0.002996005993671519|7.948651277921591|0.11010778867017111|True|
|11|1622.481432140203|0.004772038059722838|6.319559089884667|0.19079320986226123|True|
|101|4107.435852170624|0.007275112632303623|8.568198444652582|0.8999996887663332|False|

Reported same-kind clock: Unresolved; exploratory integer guide is not a published period.

Formal midpoint errors are local trapezoid-fit uncertainties; clock fitting uses cadence/2 or0.003d floors. The period covariance is formal and conditional on the chosen cycle count; it is not a calibrated precision claim. Invalid fits, spikes and opposite conjunction kinds are not added as timing evidence.

## Reduction, attribution and geometry

Quality-zero finite positive raw SAP is primary evidence. QLP KSPSAP and custom7x7 TESScut/3x3 aperture are reductions of the same photons. Sector10 deficit offset 1.649227484144691pixels; aperture core loss0.0015349029458932018. The panel and Gaia neighbor positions were inspected; the centroid alone does not settle an unresolved neighbor. Bounded alias audit requires both sidebands,75% core sampling and no large interior gap. Missing or flagged predictions are not nulls. Source-specific fullSB1 covariance is propagated linearly and with100000 nonlinear draws, seed50701, with conjunction phase unwrapped about the nominal epoch before fixed-cycle propagation. Geometry assumes edge-on conjunction, not measured inclination.

## Catalogue and eligibility

Successful shared source checks are retained by source and hash. Nearby catalogued variables are adjudicated separately; a match near the target is not a target classification. Literature scope is244 locally fetched eprints with exact identifiers and is not exhaustive. E023's RV rejection is retained separately from novelty. Physical tier, source association and publication eligibility are separate.

## Limitation and next check

Establish a coherent clock from resolved raw events and determine their spatial source.

Evidence: lead-context.json, lead-series.json, lead-timing.json, raw/context panels, helper-localization.json/png/fits, lead-neighbors.json, lead-central-catalogue-receipts.json; batch clocks, full covered-window alias audit and summary, Gaia covariance, nonlinear covariance, current sector inventory, identity/source hashes and independent helper audit. Exact8 queue, no substitutions; no ledger/public edits.

Independent spatial audit: audit-spatial-gaussian.json and audit_spatial_gaussian.py (E019/E021/E025). E019 exact known-neighbor adjudication: lead-known-neighbor-adjudication.json. E027 current-sector evidence: audit-s107.json/fits, audit-s003.fits (unusable) and lead-newsector-aliases.json. Helper final audit and freeze hashes complete the evidence chain.
