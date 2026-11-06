# E025 - TIC 451669009

Review complete; physical tier **CONFIRMED**. Gaia DR3 5342912927946223360; selection P=44.25415989405746d,G=11.649421.

Three bounded raw rounded eclipses at3063.48548/3771.83684/4081.73730 give44.2718429d, cycles0/16/23; residual<0.0015d and timing-compatible integer alternatives are rejected by third-event timing or covered nulls. Custom aperture independently recovers~29ppt eclipse and compact0.150pixel deficit. Gaia conjunction agrees~0.6sigma. A0.51pixel neighbor withG flux ratio0.0347 is assessed spatially: Gaussian plus plane deficit fit is0.036pixel from target and0.490pixel from neighbor.250 frame-resampled fits retain target preference; temporal bootstrap does not include PRF/WCS systematics. Attribution is supported by this measured spatial separation rather than intrinsic-flux versus blended-loss comparison.

## Representative raw measurements

|Sector|midpoint BTJD|formal fit error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
|64|3063.485478537176|0.0009033495433667859|41.798396179227424|0.2900592984446998|True|
|90|3771.8368419691124|0.001162897852523023|36.839508134645996|0.2777167699083143|True|
|100|4081.737300827253|0.0007314340618832475|32.66073746071604|0.27840707269987564|True|

Reported same-kind clock: {"period_d": 44.27184285322513, "epoch_btjd": 3063.4859166859187, "formal_period_error_d": 0.00017992804317122011, "cycles": [0, 16, 23], "times": [3063.485478537176, 3771.8368419691124, 4081.737300827253], "residuals": [-0.0004381487428872788, 0.0014396315914382285, -0.0010014828435487289], "duration_d": 0.27840707269987564, "depth_ppt": 36.839508134645996, "max_residual_d": 0.0014396315914382285, "note": "Same-kind morphology; formal WLS error with cadence/2 or .003d floor; integer alias and geometry audits separately required."}

Formal midpoint errors are local trapezoid-fit uncertainties; clock fitting uses cadence/2 or0.003d floors. The period covariance is formal and conditional on the chosen cycle count; it is not a calibrated precision claim. Invalid fits, spikes and opposite conjunction kinds are not added as timing evidence.

## Reduction, attribution and geometry

Quality-zero finite positive raw SAP is primary evidence. QLP KSPSAP and custom7x7 TESScut/3x3 aperture are reductions of the same photons. Sector64 deficit offset 0.14986993417362776pixels; aperture core loss0.029032300249378085. The panel and Gaia neighbor positions were inspected; the centroid alone does not settle an unresolved neighbor. Bounded alias audit requires both sidebands,75% core sampling and no large interior gap. Missing or flagged predictions are not nulls. Source-specific fullSB1 covariance is propagated linearly and with100000 nonlinear draws, seed50701, with conjunction phase unwrapped about the nominal epoch before fixed-cycle propagation. Geometry assumes edge-on conjunction, not measured inclination.

## Catalogue and eligibility

Successful shared source checks are retained by source and hash. Nearby catalogued variables are adjudicated separately; a match near the target is not a target classification. Literature scope is244 locally fetched eprints with exact identifiers and is not exhaustive. E023's RV rejection is retained separately from novelty. Physical tier, source association and publication eligibility are separate.

## Limitation and next check

Calibrated PRF or higher-resolution photometry can improve the bounded spatial discrimination; retain WCS/model systematic limits.

Evidence: lead-context.json, lead-series.json, lead-timing.json, raw/context panels, helper-localization.json/png/fits, lead-neighbors.json, lead-central-catalogue-receipts.json; batch clocks, full covered-window alias audit and summary, Gaia covariance, nonlinear covariance, current sector inventory, identity/source hashes and independent helper audit. Exact8 queue, no substitutions; no ledger/public edits.

Independent spatial audit: audit-spatial-gaussian.json and audit_spatial_gaussian.py (E019/E021/E025). E019 exact known-neighbor adjudication: lead-known-neighbor-adjudication.json. E027 current-sector evidence: audit-s107.json/fits, audit-s003.fits (unusable) and lead-newsector-aliases.json. Helper final audit and freeze hashes complete the evidence chain.
