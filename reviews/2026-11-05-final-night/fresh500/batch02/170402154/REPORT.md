# E010 — TIC 170402154

Review **complete**. Physical tier: **PROBABLE**. GaiaDR3 5562108100023118080; selection P=37.178496158314374d and G=11.667651.

Four deep bounded raw eclipses at1488.82130,2233.15085,2977.47873,3684.59290 yield37.2164764d with cycles0/20/40/59. Divisors and timing-compatible competing integer aliases are rejected by timing or covered nulls. Target-centered deficit (0.127px centroid offset) and custom extraction support target. However source-specific Gaia covariance retains about3sigma conjunction tension: nonlinear residual tails .00150–.00278. This is a real repeated target eclipser with unresolved selected-orbit geometry, rather than a fully passed geometry check.

## Representative raw events

|Sector|local fitted BTJD|formal error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
|6|1488.8213025853752|0.0010397450471084596|60.831101650087696|0.31509846556512666|True|
|34|2233.1508463424043|0.00029850201505319076|69.1591632898118|0.31137316946966764|True|
|61|2977.478725087448|0.0003424543302553401|71.20678299590705|0.310497048893204|True|
|87|3684.592898204683|0.00028183521521225923|66.89913751325034|0.3126338448743628|True|

Accepted target photometric period: 37.21647641528023d; formal period error 8.920874088573466e-05d. Local fit uncertainties are formal; accepted clock covariance includes cadence/2 and .002d floors and is not a calibrated systematic uncertainty. Rejected/nominal exploratory clocks remain in lead-clocks.json as provenance and do not override this report. Screen-selected local fits do not alone establish a physical event.

Raw quality-zero finite positive SAP is the primary extraction; flagged S64 E013 samples were explicitly reviewed as compromised context. KSPSAP and custom3x3 TESScut apertures reuse the same photons and are reduction checks, not independent observing occasions. All cached sector contexts and representative deciding events were reviewed; not an exhaustive all-sector fit. Missing/flagged predictions are not clean nulls. Alias scan tests divisors2–6 and endpoint integer periods about5–100d, keeping timing compatibility separate from coverage; E018 has a separate clean-pair scan. Full source-specific SB1 covariance uses parameter orderP,gamma,K,e,omega,Tp and subindices0,3,4,5; local fixed-cycle propagation and seeded100000draw nonlinear checks retain Gaussian-covariance and edge-on assumptions.

## Attribution and catalogues

Source association: target-supported; selected Gaia association: geometry-tension. Pixel receipt and independent FITS audit retained; use morphology and neighbors with the quantitative values, not centroid alone.

Shared successful scoped catalogue checks found no exact target prior EB; source-specific receipt includes local vetted-table comparisons. Non-eclipsing type entries and nearby EB matches are distinguished above. The seven required groups and root shared seal are preserved in lead-central-catalogue-receipts.json. A nonmatch is not exhaustive novelty proof, and no off-target source is a new target claim.

## Limitation and next check

Reconcile source-specific spectroscopic orbit/conjunction geometry with measured eclipse clock.

Evidence: per-target lead-context/series/timing.json, raw-context and allsector figures, applicable helper-localization.json/png and7x7FITS, lead-neighbors.json; batch source hashes, current-sector inventory, clocks, alias-covered windows/summary, E018 pair aliases, Gaia covariance/nonlinear diagnostics and independent helper audit. Exact8 reviewed without substitution. Completion is separate from tier. No ledger or public edits.
