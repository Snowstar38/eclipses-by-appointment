# E026 - TIC 1511057635

Review complete; physical tier **PLAUSIBLE**. Gaia DR3 5911896009055318016; selection P=36.04683271380443d,G=11.68204.

S39/S103 clear bounded~13ppt raw events are separated1803.13178d. A nominal36.0626355d clock is only one of several viable integer aliases, including72.12527,69.35122,60.10439,58.16554 and51.51805d; the apparent S93/S100/S104 features are gap/step structures, not precise recurrence measurements. Independent S39 pixels recover the event with0.032pixel deficit, but capable neighbors at0.34/0.60pixels remain unresolved.

## Representative raw measurements

|Sector|midpoint BTJD|formal fit error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
|39|2370.9725302023508|0.004841947177805666|13.405814730371608|0.34699223794404677|True|
|93|3849.684123101423|0.13972260989227955|17.785041698598462|0.6834269490901131|False|
|100|4085.821828850761|0.0559756504413346|0.9192217212101875|0.6965167663535775|False|
|103|4174.104305518475|0.001231089875063193|12.288471960754647|0.34040451318560705|True|
|104|4197.413738619585|0.017374512877274532|4.136723952281163|0.8999999998946426|False|

Reported same-kind clock: Unresolved; exploratory integer guide is not a published period.

Formal midpoint errors are local trapezoid-fit uncertainties; clock fitting uses cadence/2 or0.003d floors. The period covariance is formal and conditional on the chosen cycle count; it is not a calibrated precision claim. Invalid fits, spikes and opposite conjunction kinds are not added as timing evidence.

## Reduction, attribution and geometry

Quality-zero finite positive raw SAP is primary evidence. QLP KSPSAP and custom7x7 TESScut/3x3 aperture are reductions of the same photons. Sector39 deficit offset 0.03203689222250696pixels; aperture core loss0.009239994867008994. The panel and Gaia neighbor positions were inspected; the centroid alone does not settle an unresolved neighbor. Bounded alias audit requires both sidebands,75% core sampling and no large interior gap. Missing or flagged predictions are not nulls. Source-specific fullSB1 covariance is propagated linearly and with100000 nonlinear draws, seed50701, with conjunction phase unwrapped about the nominal epoch before fixed-cycle propagation. Geometry assumes edge-on conjunction, not measured inclination.

## Catalogue and eligibility

Successful shared source checks are retained by source and hash. Nearby catalogued variables are adjudicated separately; a match near the target is not a target classification. Literature scope is244 locally fetched eprints with exact identifiers and is not exhaustive. E023's RV rejection is retained separately from novelty. Physical tier, source association and publication eligibility are separate.

## Limitation and next check

Obtain another same-kind event and resolve the close neighbors; do not assign a precision period.

Evidence: lead-context.json, lead-series.json, lead-timing.json, raw/context panels, helper-localization.json/png/fits, lead-neighbors.json, lead-central-catalogue-receipts.json; batch clocks, full covered-window alias audit and summary, Gaia covariance, nonlinear covariance, current sector inventory, identity/source hashes and independent helper audit. Exact8 queue, no substitutions; no ledger/public edits.

Independent spatial audit: audit-spatial-gaussian.json and audit_spatial_gaussian.py (E019/E021/E025). E019 exact known-neighbor adjudication: lead-known-neighbor-adjudication.json. E027 current-sector evidence: audit-s107.json/fits, audit-s003.fits (unusable) and lead-newsector-aliases.json. Helper final audit and freeze hashes complete the evidence chain.
