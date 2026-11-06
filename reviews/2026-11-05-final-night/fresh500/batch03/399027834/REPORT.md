# E021 - TIC 399027834

Review complete; physical tier **CONFIRMED**. Gaia DR3 6081971731808630400; selection P=28.21328975749298d,G=11.797306.

Six clear raw eclipses give28.1464334d and residuals<0.002d; adjacent-sector repeats and covered nulls reject timing-compatible integer aliases. Independent pixels recover4.8% compact deficit at0.054pixel from target. Gaia period differs2.42sigma; the same conjunctionA retains~2.5sigma tension, but is within the nonlinear3sigma interval after correctly unwrapping conjunction phase. Gaussian plus plane fit places the deficit0.036pixel from target and0.669pixel from the capable0.70pixel neighbor; 250 frame-resampled fits retain this target preference. This is spatial-model evidence, not brightness exclusion or a calibrated astrometric confidence interval.

## Representative raw measurements

|Sector|midpoint BTJD|formal fit error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
|11|1621.1443758640394|0.0004916767069021327|43.20462121304156|0.22001041597889356|True|
|37|2324.8075029110946|0.00045194871705218936|44.54594101865621|0.22410156818424906|True|
|38|2352.953177899537|0.00040013648513033395|46.3771056215586|0.21651501720376332|True|
|64|3056.6148521236505|0.0004037308765129877|46.3701710713445|0.21914396955215015|True|
|99|4069.88663495472|0.0002989386271860947|42.13533682390502|0.2165401931956179|True|
|100|4098.031618659945|0.00030852486146908467|39.116882935377795|0.21742851753317044|True|

Reported same-kind clock: {"period_d": 28.146433409425676, "epoch_btjd": 1621.1463171249695, "formal_period_error_d": 4.968352593373815e-05, "cycles": [0, 25, 26, 51, 87, 88], "times": [1621.1443758640394, 2324.8075029110946, 2352.953177899537, 3056.6148521236505, 4069.88663495472, 4098.031618659945], "residuals": [-0.0019412609301525663, 0.00035055048329013516, -0.00040787050011203974, 0.0004311179714022728, 0.0006112097166806052, -0.0008384944840145181], "duration_d": 0.2182862435426603, "depth_ppt": 43.875281115848885, "max_residual_d": 0.0019412609301525663, "note": "Same-kind morphology; formal WLS error with cadence/2 or .003d floor; integer alias and geometry audits separately required."}

Formal midpoint errors are local trapezoid-fit uncertainties; clock fitting uses cadence/2 or0.003d floors. The period covariance is formal and conditional on the chosen cycle count; it is not a calibrated precision claim. Invalid fits, spikes and opposite conjunction kinds are not added as timing evidence.

## Reduction, attribution and geometry

Quality-zero finite positive raw SAP is primary evidence. QLP KSPSAP and custom7x7 TESScut/3x3 aperture are reductions of the same photons. Sector38 deficit offset 0.05425682015996602pixels; aperture core loss0.04826921604389789. The panel and Gaia neighbor positions were inspected; the centroid alone does not settle an unresolved neighbor. Bounded alias audit requires both sidebands,75% core sampling and no large interior gap. Missing or flagged predictions are not nulls. Source-specific fullSB1 covariance is propagated linearly and with100000 nonlinear draws, seed50701, with conjunction phase unwrapped about the nominal epoch before fixed-cycle propagation. Geometry assumes edge-on conjunction, not measured inclination.

## Catalogue and eligibility

Successful shared source checks are retained by source and hash. Nearby catalogued variables are adjudicated separately; a match near the target is not a target classification. Literature scope is244 locally fetched eprints with exact identifiers and is not exhaustive. E023's RV rejection is retained separately from novelty. Physical tier, source association and publication eligibility are separate.

## Limitation and next check

Retain the source-specific2.5sigma geometry tension and uncalibrated PRF/WCS systematic limits; obtain more precise spectroscopy.

Evidence: lead-context.json, lead-series.json, lead-timing.json, raw/context panels, helper-localization.json/png/fits, lead-neighbors.json, lead-central-catalogue-receipts.json; batch clocks, full covered-window alias audit and summary, Gaia covariance, nonlinear covariance, current sector inventory, identity/source hashes and independent helper audit. Exact8 queue, no substitutions; no ledger/public edits.

Independent spatial audit: audit-spatial-gaussian.json and audit_spatial_gaussian.py (E019/E021/E025). E019 exact known-neighbor adjudication: lead-known-neighbor-adjudication.json. E027 current-sector evidence: audit-s107.json/fits, audit-s003.fits (unusable) and lead-newsector-aliases.json. Helper final audit and freeze hashes complete the evidence chain.
