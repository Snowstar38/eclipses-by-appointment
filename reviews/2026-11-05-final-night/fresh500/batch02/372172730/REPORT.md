# E018 — TIC 372172730

Review **complete**. Physical tier: **PLAUSIBLE**. GaiaDR3 6376404040731165952; selection P=38.02425200648938d and G=11.708208.

S13/S27 narrow dips at1669.94738/2056.90166 are credible; S102 event4146.44694 lies just after a segment restart and is less secure, while4140.0676 is an instrumental ramp. Later S101–104 boundary ramps are excluded as eclipses. A forced38d triple fit fails badly (6.09d residual); it is an explicitly rejected exploratory clock. Clean-pair integer tests over~5–100d retain96.73857d and77.39086d, so no unique period is established. S27 difference peak is near target and3x3 aperture loss0.00893; saved positive centroid is NaN and is not a valid localization measurement.

## Representative raw events

|Sector|local fitted BTJD|formal error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
|13|1669.9473844469494|0.004732573720960363|7.703720923457401|0.17664077424102398|True|
|27|2056.9016622032736|0.0020383561397303122|12.167981892831293|0.15110818593641273|True|
|102|4146.44694130616|0.0012460873036733843|9.935559456717945|0.1620013397377206|True|
|102|4140.067632892193|18425.09866158594|11.190617531166673|0.666394260837082|False|

Accepted target photometric period: unresolved/not assignedd; formal period error not assignedd. Local fit uncertainties are formal; accepted clock covariance includes cadence/2 and .002d floors and is not a calibrated systematic uncertainty. Rejected/nominal exploratory clocks remain in lead-clocks.json as provenance and do not override this report. Screen-selected local fits do not alone establish a physical event.

Raw quality-zero finite positive SAP is the primary extraction; flagged S64 E013 samples were explicitly reviewed as compromised context. KSPSAP and custom3x3 TESScut apertures reuse the same photons and are reduction checks, not independent observing occasions. All cached sector contexts and representative deciding events were reviewed; not an exhaustive all-sector fit. Missing/flagged predictions are not clean nulls. Alias scan tests divisors2–6 and endpoint integer periods about5–100d, keeping timing compatibility separate from coverage; E018 has a separate clean-pair scan. Full source-specific SB1 covariance uses parameter orderP,gamma,K,e,omega,Tp and subindices0,3,4,5; local fixed-cycle propagation and seeded100000draw nonlinear checks retain Gaussian-covariance and edge-on assumptions.

## Attribution and catalogues

Source association: target-supported-but-limited; selected Gaia association: unresolved-clock. Pixel receipt and independent FITS audit retained; use morphology and neighbors with the quantitative values, not centroid alone.

Shared successful scoped catalogue checks found no exact target prior EB; source-specific receipt includes local vetted-table comparisons. Non-eclipsing type entries and nearby EB matches are distinguished above. The seven required groups and root shared seal are preserved in lead-central-catalogue-receipts.json. A nonmatch is not exhaustive novelty proof, and no off-target source is a new target claim.

## Limitation and next check

Another complete same-kind event, robust clock and clean source localization are required.

Evidence: per-target lead-context/series/timing.json, raw-context and allsector figures, applicable helper-localization.json/png and7x7FITS, lead-neighbors.json; batch source hashes, current-sector inventory, clocks, alias-covered windows/summary, E018 pair aliases, Gaia covariance/nonlinear diagnostics and independent helper audit. Exact8 reviewed without substitution. Completion is separate from tier. No ledger or public edits.
