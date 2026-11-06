# E019 - TIC 382672776

Review complete; physical tier **CONFIRMED**. Gaia DR3 5854347501762384896; selection P=32.17247243932781d,G=11.805206.

Five same-kind raw flat-bottom events give32.2144744d at cycles0,1,23,76,78, with maximum residual0.00211d. The second eclipse kind is displaced about9.878d and is not mixed into the clock. All timing-compatible integer/divisor alternatives in the bounded scan reduce to this clock. Compact deficit is on the target; independent aperture recovers31% loss. Known neighbor TIC382672899/Gaia5854335746401121024 at53.4256arcsec is spatially distinct from the deficit. Source-specific Gaia period differs1.12sigma and conjunction offsets remain within covariance.

## Representative raw measurements

|Sector|midpoint BTJD|formal fit error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
|11|1618.4243432535245|0.0003482838264731902|255.05821604829026|0.6502812048601908|True|
|11|1615.621676932663|0.004086299306030256|19.201575866127225|0.4993232455759628|True|
|11|1607.2769038958886|0.007073022477421024|19.571959832718782|0.4734007060973144|True|
|11|1620.7180660199026|0.007471197408082455|14.191487605780425|0.541624236954994|True|
|12|1650.639175584482|0.00047616865419858133|265.8452406970536|0.6441394335080232|True|
|12|1628.300741940307|0.002245160543296812|260.3666366334536|0.4964239596116114|True|
|12|1632.3129986307283|0.0081474830082119|20.038347453790234|0.5251392743687828|True|
|38|2359.357607937292|0.00038899153039939535|295.7575463808307|0.6516266172513446|True|
|38|2337.0207567416214|0.00039134266739486196|286.72967186917356|0.5013751820673924|True|
|65|3077.952393370891|0.002567160869348282|232.45352406632048|0.49171317558671124|True|
|65|3092.4315653762756|0.031537789473428224|66.5511741252691|0.7109370508552921|True|
|65|3093.481707672321|0.03472404495908667|52.50434944166095|0.429500437285757|True|
|65|3091.442195402632|0.05855719244730359|21.129935045173088|0.41758397124978486|True|
|99|4066.830654710989|0.0003965132068806456|242.85181785331352|0.8680304745781883|False|
|100|4076.6034260797182|0.0001129212548002635|226.37917282020945|0.49938286738336596|True|
|101|4108.815672353472|0.00011728683147157513|224.89770570044652|0.49941764384000864|True|
|102|4131.151698185675|0.0001514805309580398|235.24678706797837|0.6505444887299665|True|
|102|4141.029967727404|0.00012588680217279677|225.4576046758585|0.4957144765720355|True|
|99|4066.7268892537954|0.00019901395844887972|250.7566581889596|0.6538634223565565|True|

Reported same-kind clock: {"period_d": 32.21447442035059, "epoch_btjd": 1618.4247324226076, "formal_period_error_d": 6.41776482896955e-05, "cycles": [0, 1, 23, 78, 76], "times": [1618.4243432535245, 1650.639175584482, 2359.357607937292, 4131.151698185675, 4066.7268892537954], "residuals": [-0.0003891690830641892, -3.1258476155926473e-05, -3.615337936935248e-05, -0.0020390242789289914, 0.0021008845428696077], "duration_d": 0.6505444887299665, "depth_ppt": 255.05821604829026, "max_residual_d": 0.0021008845428696077, "note": "Same-kind morphology; formal WLS error with cadence/2 or .003d floor; integer alias and geometry audits separately required."}

Formal midpoint errors are local trapezoid-fit uncertainties; clock fitting uses cadence/2 or0.003d floors. The period covariance is formal and conditional on the chosen cycle count; it is not a calibrated precision claim. Invalid fits, spikes and opposite conjunction kinds are not added as timing evidence.

## Reduction, attribution and geometry

Quality-zero finite positive raw SAP is primary evidence. QLP KSPSAP and custom7x7 TESScut/3x3 aperture are reductions of the same photons. Sector38 deficit offset 0.24943648935886276pixels; aperture core loss0.31341792688290426. The panel and Gaia neighbor positions were inspected; the centroid alone does not settle an unresolved neighbor. Bounded alias audit requires both sidebands,75% core sampling and no large interior gap. Missing or flagged predictions are not nulls. Source-specific fullSB1 covariance is propagated linearly and with100000 nonlinear draws, seed50701, with conjunction phase unwrapped about the nominal epoch before fixed-cycle propagation. Geometry assumes edge-on conjunction, not measured inclination.

## Catalogue and eligibility

Successful shared source checks are retained by source and hash. Nearby catalogued variables are adjudicated separately; a match near the target is not a target classification. Literature scope is244 locally fetched eprints with exact identifiers and is not exhaustive. E023's RV rejection is retained separately from novelty. Physical tier, source association and publication eligibility are separate.

## Limitation and next check

Refine the timing ephemeris with additional complete events.

Evidence: lead-context.json, lead-series.json, lead-timing.json, raw/context panels, helper-localization.json/png/fits, lead-neighbors.json, lead-central-catalogue-receipts.json; batch clocks, full covered-window alias audit and summary, Gaia covariance, nonlinear covariance, current sector inventory, identity/source hashes and independent helper audit. Exact8 queue, no substitutions; no ledger/public edits.

Independent spatial audit: audit-spatial-gaussian.json and audit_spatial_gaussian.py (E019/E021/E025). E019 exact known-neighbor adjudication: lead-known-neighbor-adjudication.json. E027 current-sector evidence: audit-s107.json/fits, audit-s003.fits (unusable) and lead-newsector-aliases.json. Helper final audit and freeze hashes complete the evidence chain.
