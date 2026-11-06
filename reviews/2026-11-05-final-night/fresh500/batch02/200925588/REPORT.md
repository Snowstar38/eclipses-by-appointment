# E011 — TIC 200925588

Review **complete**. Physical tier: **REFUTED**. GaiaDR3 224600474320803968; selection P=49.36792900184605d and G=11.694737.

A real narrow eclipse train repeats about2.3448325d, far from selection Gaia49.37d. The deficit lies toward the7x7cutout edge, positive centroid1.779px from target; target-centered3x3 loss is0.00155 versus fitted SAP depth0.0395. Independent pixel review supports off-target contamination. The clipped source is not assigned a unique neighboring TIC. The selected target-eclipse claim is refuted; this does not refute the real contaminating binary.

## Representative raw events

|Sector|local fitted BTJD|formal error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
|18|1809.5254148248916|0.001748101054267126|33.337153299983065|0.15090482338908442|True|
|18|1807.1887657644365|0.000992863084148394|32.1571759940687|0.14147848811686342|True|
|18|1793.1208185379367|0.000662750748151113|31.983096805502285|0.13843884394478945|True|
|18|1811.8799918326627|0.0009812628195492693|33.45505116504993|0.13606309124811042|True|
|58|2902.214469859691|0.0005822414273036622|39.53464539879127|0.14180481052469884|True|
|58|2909.2603229134497|0.0005820631829630406|38.6943202686454|0.14382648896157907|True|
|58|2899.880447889027|0.000506369387956456|38.521861076153215|0.13980314392218882|True|
|58|2883.457405037061|0.0005080854122722522|37.56466881702622|0.1408801150910106|True|
|86|3650.224373828952|0.001046821617828866|17.826176970817027|0.12559413457281957|True|
|86|3659.6032196829924|0.0012449261031705083|20.533205641420484|0.14477808268582923|True|
|86|3645.5300645022407|0.0009568596864762182|17.30188043156228|0.12672817201223374|True|
|86|3640.842145840441|0.0020525956421738427|16.797644158401454|0.1368116369813312|True|

Accepted target photometric period: unresolved/not assignedd; formal period error not assignedd. Local fit uncertainties are formal; accepted clock covariance includes cadence/2 and .002d floors and is not a calibrated systematic uncertainty. Rejected/nominal exploratory clocks remain in lead-clocks.json as provenance and do not override this report. Screen-selected local fits do not alone establish a physical event.

Raw quality-zero finite positive SAP is the primary extraction; flagged S64 E013 samples were explicitly reviewed as compromised context. KSPSAP and custom3x3 TESScut apertures reuse the same photons and are reduction checks, not independent observing occasions. All cached sector contexts and representative deciding events were reviewed; not an exhaustive all-sector fit. Missing/flagged predictions are not clean nulls. Alias scan tests divisors2–6 and endpoint integer periods about5–100d, keeping timing compatibility separate from coverage; E018 has a separate clean-pair scan. Full source-specific SB1 covariance uses parameter orderP,gamma,K,e,omega,Tp and subindices0,3,4,5; local fixed-cycle propagation and seeded100000draw nonlinear checks retain Gaussian-covariance and edge-on assumptions.

## Attribution and catalogues

Source association: off-target-signal; selected Gaia association: not-associated. Pixel receipt and independent FITS audit retained; use morphology and neighbors with the quantitative values, not centroid alone.

Shared successful scoped catalogue checks found no exact target prior EB; source-specific receipt includes local vetted-table comparisons. Non-eclipsing type entries and nearby EB matches are distinguished above. The seven required groups and root shared seal are preserved in lead-central-catalogue-receipts.json. A nonmatch is not exhaustive novelty proof, and no off-target source is a new target claim.

## Limitation and next check

A wider bounded cutout could identify the contaminating short-period source; no target addition is warranted.

Evidence: per-target lead-context/series/timing.json, raw-context and allsector figures, applicable helper-localization.json/png and7x7FITS, lead-neighbors.json; batch source hashes, current-sector inventory, clocks, alias-covered windows/summary, E018 pair aliases, Gaia covariance/nonlinear diagnostics and independent helper audit. Exact8 reviewed without substitution. Completion is separate from tier. No ledger or public edits.
