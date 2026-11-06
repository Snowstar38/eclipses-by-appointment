# E020 - TIC 398556213

Review complete; physical tier **PLAUSIBLE**. Gaia DR3 2707813980608692992; selection P=33.25723213451981d,G=11.885117.

Two clear~105ppt bounded raw events at2819.64770 and3548.08668 are recovered in independent pixels on target. Their728.43898d separation admits many integer periods, including33.11086 and16.55543d with no covered null. Gaia33.25723d alone cannot settle the photometric cycle ambiguity. Current sector inventory55/82 provides no new observing sector.

## Representative raw measurements

|Sector|midpoint BTJD|formal fit error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
|55|2819.647702476669|0.0003242922731105525|104.84734291190439|0.3291412344686394|True|
|82|3548.0866830219716|0.0002040202796491678|105.3814611719981|0.3289183153625552|True|
|82|3535.2929467598306|0.0021685588529926476|8.429546870595944|0.27732143613643767|True|

Reported same-kind clock: Unresolved; exploratory integer guide is not a published period.

Formal midpoint errors are local trapezoid-fit uncertainties; clock fitting uses cadence/2 or0.003d floors. The period covariance is formal and conditional on the chosen cycle count; it is not a calibrated precision claim. Invalid fits, spikes and opposite conjunction kinds are not added as timing evidence.

## Reduction, attribution and geometry

Quality-zero finite positive raw SAP is primary evidence. QLP KSPSAP and custom7x7 TESScut/3x3 aperture are reductions of the same photons. Sector82 deficit offset 0.13167158265337556pixels; aperture core loss0.10331041838255417. The panel and Gaia neighbor positions were inspected; the centroid alone does not settle an unresolved neighbor. Bounded alias audit requires both sidebands,75% core sampling and no large interior gap. Missing or flagged predictions are not nulls. Source-specific fullSB1 covariance is propagated linearly and with100000 nonlinear draws, seed50701, with conjunction phase unwrapped about the nominal epoch before fixed-cycle propagation. Geometry assumes edge-on conjunction, not measured inclination.

## Catalogue and eligibility

Successful shared source checks are retained by source and hash. Nearby catalogued variables are adjudicated separately; a match near the target is not a target classification. Literature scope is244 locally fetched eprints with exact identifiers and is not exhaustive. E023's RV rejection is retained separately from novelty. Physical tier, source association and publication eligibility are separate.

## Limitation and next check

Obtain a third same-kind event to test integer aliases.

Evidence: lead-context.json, lead-series.json, lead-timing.json, raw/context panels, helper-localization.json/png/fits, lead-neighbors.json, lead-central-catalogue-receipts.json; batch clocks, full covered-window alias audit and summary, Gaia covariance, nonlinear covariance, current sector inventory, identity/source hashes and independent helper audit. Exact8 queue, no substitutions; no ledger/public edits.

Independent spatial audit: audit-spatial-gaussian.json and audit_spatial_gaussian.py (E019/E021/E025). E019 exact known-neighbor adjudication: lead-known-neighbor-adjudication.json. E027 current-sector evidence: audit-s107.json/fits, audit-s003.fits (unusable) and lead-newsector-aliases.json. Helper final audit and freeze hashes complete the evidence chain.
