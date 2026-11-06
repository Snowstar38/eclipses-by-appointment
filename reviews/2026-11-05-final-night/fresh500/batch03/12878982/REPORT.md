# E027 - TIC 12878982

Review complete; physical tier **PLAUSIBLE**. Gaia DR3 2417221028846511872; selection P=57.23742245600483d,G=11.974112.

S29 raw event2094.06631 is recovered on target; current-sector check finds a second clearS107 eclipse at4271.548735 (formal fit error0.00114d,30.3ppt,0.361d duration). The2177.48243d separation admits many integer aliases, including57.30217d at38cycles and28.65108d at76cycles. Coverage scan overS29/S107 does not discriminate these. S3 cutout is unusable with no valid stellar image and is not a covered null.

## Representative raw measurements

|Sector|midpoint BTJD|formal fit error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
|29|2094.066313554758|0.0008538560649856283|31.475936554512543|0.3554588236064915|True|

Reported same-kind clock: Unresolved; exploratory integer guide is not a published period.

Formal midpoint errors are local trapezoid-fit uncertainties; clock fitting uses cadence/2 or0.003d floors. The period covariance is formal and conditional on the chosen cycle count; it is not a calibrated precision claim. Invalid fits, spikes and opposite conjunction kinds are not added as timing evidence.

## Reduction, attribution and geometry

Quality-zero finite positive raw SAP is primary evidence. QLP KSPSAP and custom7x7 TESScut/3x3 aperture are reductions of the same photons. Sector29 deficit offset 0.27861734437274566pixels; aperture core loss0.03089066793383688. The panel and Gaia neighbor positions were inspected; the centroid alone does not settle an unresolved neighbor. Bounded alias audit requires both sidebands,75% core sampling and no large interior gap. Missing or flagged predictions are not nulls. Source-specific fullSB1 covariance is propagated linearly and with100000 nonlinear draws, seed50701, with conjunction phase unwrapped about the nominal epoch before fixed-cycle propagation. Geometry assumes edge-on conjunction, not measured inclination.

## Catalogue and eligibility

Successful shared source checks are retained by source and hash. Nearby catalogued variables are adjudicated separately; a match near the target is not a target classification. Literature scope is244 locally fetched eprints with exact identifiers and is not exhaustive. E023's RV rejection is retained separately from novelty. Physical tier, source association and publication eligibility are separate.

## Limitation and next check

Obtain a third same-kind event to distinguish integer-cycle aliases.

Evidence: lead-context.json, lead-series.json, lead-timing.json, raw/context panels, helper-localization.json/png/fits, lead-neighbors.json, lead-central-catalogue-receipts.json; batch clocks, full covered-window alias audit and summary, Gaia covariance, nonlinear covariance, current sector inventory, identity/source hashes and independent helper audit. Exact8 queue, no substitutions; no ledger/public edits.

Independent spatial audit: audit-spatial-gaussian.json and audit_spatial_gaussian.py (E019/E021/E025). E019 exact known-neighbor adjudication: lead-known-neighbor-adjudication.json. E027 current-sector evidence: audit-s107.json/fits, audit-s003.fits (unusable) and lead-newsector-aliases.json. Helper final audit and freeze hashes complete the evidence chain.
