# E017 — TIC 332915881

Review **complete**. Physical tier: **CONFIRMED**. GaiaDR3 3010307599552752512; selection P=29.864954608729914d and G=11.566395.

Three deep bounded target eclipses in S32/S98 (the latter two consecutive) yield29.8438577d, cycles0/61/62. Covered divisor nulls and timing exclude competing integer aliases. Difference deficit is centered on target, independently extracted aperture recovers event, and source-specific full Gaia covariance places nearest conjunctions within3sigma; nonlinear residual tails .0079–.0094 retain modest2.6sigma tension without failing that bound. Available sector109 is recorded but not required for this representative bounded review.

## Representative raw events

|Sector|local fitted BTJD|formal error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
|32|2179.647134557299|0.00020823609469882326|95.51857862363664|0.28642244766632124|True|
|98|4000.122606631059|0.0001745504392415451|84.68116234340138|0.2898282970697963|True|
|98|4029.966174049718|0.00029025895997512847|84.66062419062044|0.2898672182648628|True|

Accepted target photometric period: 29.843857682763076d; formal period error 6.094945733384328e-05d. Local fit uncertainties are formal; accepted clock covariance includes cadence/2 and .002d floors and is not a calibrated systematic uncertainty. Rejected/nominal exploratory clocks remain in lead-clocks.json as provenance and do not override this report. Screen-selected local fits do not alone establish a physical event.

Raw quality-zero finite positive SAP is the primary extraction; flagged S64 E013 samples were explicitly reviewed as compromised context. KSPSAP and custom3x3 TESScut apertures reuse the same photons and are reduction checks, not independent observing occasions. All cached sector contexts and representative deciding events were reviewed; not an exhaustive all-sector fit. Missing/flagged predictions are not clean nulls. Alias scan tests divisors2–6 and endpoint integer periods about5–100d, keeping timing compatibility separate from coverage; E018 has a separate clean-pair scan. Full source-specific SB1 covariance uses parameter orderP,gamma,K,e,omega,Tp and subindices0,3,4,5; local fixed-cycle propagation and seeded100000draw nonlinear checks retain Gaussian-covariance and edge-on assumptions.

## Attribution and catalogues

Source association: target-supported; selected Gaia association: consistent-within-covariance. Pixel receipt and independent FITS audit retained; use morphology and neighbors with the quantitative values, not centroid alone.

Shared successful scoped catalogue checks found no exact target prior EB; source-specific receipt includes local vetted-table comparisons. Non-eclipsing type entries and nearby EB matches are distinguished above. The seven required groups and root shared seal are preserved in lead-central-catalogue-receipts.json. A nonmatch is not exhaustive novelty proof, and no off-target source is a new target claim.

## Limitation and next check

New sector109 can refine timing and modest Gaia residual tension.

Evidence: per-target lead-context/series/timing.json, raw-context and allsector figures, applicable helper-localization.json/png and7x7FITS, lead-neighbors.json; batch source hashes, current-sector inventory, clocks, alias-covered windows/summary, E018 pair aliases, Gaia covariance/nonlinear diagnostics and independent helper audit. Exact8 reviewed without substitution. Completion is separate from tier. No ledger or public edits.
