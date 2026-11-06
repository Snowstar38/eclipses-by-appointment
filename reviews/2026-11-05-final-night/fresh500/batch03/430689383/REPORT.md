# E023 - TIC 430689383

Review complete; physical tier **PLAUSIBLE**. Gaia DR3 2000733415898027264; selection P=53.7967946442452d,G=11.856688.

S56 apparent~56ppt deficit has missing ingress and a structured detector/background neighborhood; custom pixels do not reproduce a clean bounded target eclipse. S84 shallow minimum3590.51108 has only~5.3ppt fitted depth against variable baseline and is not an established same-kind repeat. The published source-specific APF check arXiv2603.20371 rejects Gaia53.80d orbit after three spectra without RV change over20d at~4km/s precision. This is an orbital-association contradiction, not a prior EB identification.

## Representative raw measurements

|Sector|midpoint BTJD|formal fit error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
|56|2832.089559357228|0.0038553981310858088|56.31036386977979|0.7074814779943984|True|
|84|3590.5110825008646|0.02430320333358058|5.307989469085026|0.5778391929582253|True|

Reported same-kind clock: Unresolved; exploratory integer guide is not a published period.

Formal midpoint errors are local trapezoid-fit uncertainties; clock fitting uses cadence/2 or0.003d floors. The period covariance is formal and conditional on the chosen cycle count; it is not a calibrated precision claim. Invalid fits, spikes and opposite conjunction kinds are not added as timing evidence.

## Reduction, attribution and geometry

Quality-zero finite positive raw SAP is primary evidence. QLP KSPSAP and custom7x7 TESScut/3x3 aperture are reductions of the same photons. Sector56 deficit offset 1.1433614612473102pixels; aperture core loss0.030015448453622695. The panel and Gaia neighbor positions were inspected; the centroid alone does not settle an unresolved neighbor. Bounded alias audit requires both sidebands,75% core sampling and no large interior gap. Missing or flagged predictions are not nulls. Source-specific fullSB1 covariance is propagated linearly and with100000 nonlinear draws, seed50701, with conjunction phase unwrapped about the nominal epoch before fixed-cycle propagation. Geometry assumes edge-on conjunction, not measured inclination.

## Catalogue and eligibility

Successful shared source checks are retained by source and hash. Nearby catalogued variables are adjudicated separately; a match near the target is not a target classification. Literature scope is244 locally fetched eprints with exact identifiers and is not exhaustive. E023's RV rejection is retained separately from novelty. Physical tier, source association and publication eligibility are separate.

## Limitation and next check

Obtain a clean repeat and spatial attribution independently of the rejected Gaia orbit.

Evidence: lead-context.json, lead-series.json, lead-timing.json, raw/context panels, helper-localization.json/png/fits, lead-neighbors.json, lead-central-catalogue-receipts.json; batch clocks, full covered-window alias audit and summary, Gaia covariance, nonlinear covariance, current sector inventory, identity/source hashes and independent helper audit. Exact8 queue, no substitutions; no ledger/public edits.

Independent spatial audit: audit-spatial-gaussian.json and audit_spatial_gaussian.py (E019/E021/E025). E019 exact known-neighbor adjudication: lead-known-neighbor-adjudication.json. E027 current-sector evidence: audit-s107.json/fits, audit-s003.fits (unusable) and lead-newsector-aliases.json. Helper final audit and freeze hashes complete the evidence chain.
