# E013 — TIC 313271160

Review **complete**. Physical tier: **PLAUSIBLE**. GaiaDR3 5854908591959231104; selection P=45.96015001767766d and G=11.964894.

Two complete compact target-supported dips in S12/S99 imply a nominal45.9870718d clock only if53cycles are assumed. Covered prediction tests leave several integer alternatives (26,28,32,33,38,52,53cycles over2437d). A S64 SAP dip near3054.568 supports the53cycle alias, but intermittent quality1073741824 and the downlink disturbance compromise it; it is not a clean third event or precision midpoint. The2clean events alone do not settle the period. Difference deficit is near target (0.192px), but neighbor EB20.18arcsec with P0.488901d is within one TESS pixel; target ownership is supported, finite-resolution limitation remains.

## Representative raw events

|Sector|local fitted BTJD|formal error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
|12|1628.9691146977295|0.002226391840053717|18.700489093134397|0.3435527487062521|True|
|99|4066.2839186558795|0.001393609128951341|15.581228328467938|0.36421705459842774|True|

Accepted target photometric period: unresolved/not assignedd; formal period error not assignedd. Local fit uncertainties are formal; accepted clock covariance includes cadence/2 and .002d floors and is not a calibrated systematic uncertainty. Rejected/nominal exploratory clocks remain in lead-clocks.json as provenance and do not override this report. Screen-selected local fits do not alone establish a physical event.

Raw quality-zero finite positive SAP is the primary extraction; flagged S64 E013 samples were explicitly reviewed as compromised context. KSPSAP and custom3x3 TESScut apertures reuse the same photons and are reduction checks, not independent observing occasions. All cached sector contexts and representative deciding events were reviewed; not an exhaustive all-sector fit. Missing/flagged predictions are not clean nulls. Alias scan tests divisors2–6 and endpoint integer periods about5–100d, keeping timing compatibility separate from coverage; E018 has a separate clean-pair scan. Full source-specific SB1 covariance uses parameter orderP,gamma,K,e,omega,Tp and subindices0,3,4,5; local fixed-cycle propagation and seeded100000draw nonlinear checks retain Gaussian-covariance and edge-on assumptions.

## Attribution and catalogues

Source association: target-supported-with-resolution-limit; selected Gaia association: unresolved-clock. Pixel receipt and independent FITS audit retained; use morphology and neighbors with the quantitative values, not centroid alone.

Shared successful scoped catalogue checks found no exact target prior EB; source-specific receipt includes local vetted-table comparisons. Non-eclipsing type entries and nearby EB matches are distinguished above. The seven required groups and root shared seal are preserved in lead-central-catalogue-receipts.json. A nonmatch is not exhaustive novelty proof, and no off-target source is a new target claim.

## Limitation and next check

Obtain another clean complete same-kind event to resolve integer cycles and improve source separation from the nearby known EB.

Evidence: per-target lead-context/series/timing.json, raw-context and allsector figures, applicable helper-localization.json/png and7x7FITS, lead-neighbors.json; batch source hashes, current-sector inventory, clocks, alias-covered windows/summary, E018 pair aliases, Gaia covariance/nonlinear diagnostics and independent helper audit. Exact8 reviewed without substitution. Completion is separate from tier. No ledger or public edits.
