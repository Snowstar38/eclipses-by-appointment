# E012 — TIC 293514968

Review **complete**. Physical tier: **CONFIRMED**. GaiaDR3 3391378061790588928; selection P=24.30136998787383d and G=11.558994.

Deep primaries appear in six sectors; five usable fits yield 24.2977718 d from cycles 0/43/44/74/105; shallow opposite-kind eclipses are kept separate. Covered divisor nulls and timing exclude competing clocks. Raw S32 deep-fit covariance was flagged unusable, but its position is consistent and the other five usable deep events independently establish the same clock. Difference deficit is centered on target (0.084px), and custom aperture recovers eclipse. Source-specific full Gaia covariance supports geometry. VSX target type DSCT|GDOR|SXPHE is not a prior eclipsing identification; neighbor54.57arcsec with P0.368401d and G17.33 is distinct in period, amplitude and deficit location.

## Representative raw events

|Sector|local fitted BTJD|formal error d|depth ppt|duration d|fit usable|
|---|---|---|---|---|---|
|5|1445.8346578539201|0.0010179805326876856|143.75619776024791|0.4550591923970449|True|
|5|1458.4234936355795|0.004342635150911113|22.439167508653377|0.43285311021631717|True|
|32|2174.767992692021|0.0003927781488278555|144.45876221535596|0.4549402210144989|False|
|32|2187.3588222962367|0.002162794746313542|21.38471098100509|0.4453524443467757|True|
|43|2490.6358797234693|0.000525381694548417|147.16419102295356|0.4574307358404357|True|
|43|2478.930411488867|0.0024391087345917778|18.535552287100806|0.3736423221498373|True|
|44|2514.934103267801|0.00039509001193745093|152.51166905335631|0.45767910378944326|True|
|44|2503.2283262179685|0.002804533394264186|22.488901486972463|0.44121914742952895|True|
|71|3243.867619847678|0.0003580844404507597|149.94509511691714|0.4546908455147854|True|
|71|3256.4598804104294|0.0022593984420911342|21.753777083479275|0.44390683005257137|True|
|98|3997.098292736463|0.00027028138465791087|129.72803663062265|0.45243228584776907|True|
|98|4009.7671952312544|0.00503151299926692|16.947910005503797|0.6159609483316151|True|

Accepted target photometric period: 24.297771773016866d; formal period error 4.7723698118682306e-05d. Local fit uncertainties are formal; accepted clock covariance includes cadence/2 and .002d floors and is not a calibrated systematic uncertainty. Rejected/nominal exploratory clocks remain in lead-clocks.json as provenance and do not override this report. Screen-selected local fits do not alone establish a physical event.

Raw quality-zero finite positive SAP is the primary extraction; flagged S64 E013 samples were explicitly reviewed as compromised context. KSPSAP and custom3x3 TESScut apertures reuse the same photons and are reduction checks, not independent observing occasions. All cached sector contexts and representative deciding events were reviewed; not an exhaustive all-sector fit. Missing/flagged predictions are not clean nulls. Alias scan tests divisors2–6 and endpoint integer periods about5–100d, keeping timing compatibility separate from coverage; E018 has a separate clean-pair scan. Full source-specific SB1 covariance uses parameter orderP,gamma,K,e,omega,Tp and subindices0,3,4,5; local fixed-cycle propagation and seeded100000draw nonlinear checks retain Gaussian-covariance and edge-on assumptions.

## Attribution and catalogues

Source association: target-supported; selected Gaia association: consistent. Pixel receipt and independent FITS audit retained; use morphology and neighbors with the quantitative values, not centroid alone.

Shared successful scoped catalogue checks found no exact target prior EB; source-specific receipt includes local vetted-table comparisons. Non-eclipsing type entries and nearby EB matches are distinguished above. The seven required groups and root shared seal are preserved in lead-central-catalogue-receipts.json. A nonmatch is not exhaustive novelty proof, and no off-target source is a new target claim.

## Limitation and next check

Additional sectors can refine representative event timings and extraction dilution.

Evidence: per-target lead-context/series/timing.json, raw-context and allsector figures, applicable helper-localization.json/png and7x7FITS, lead-neighbors.json; batch source hashes, current-sector inventory, clocks, alias-covered windows/summary, E018 pair aliases, Gaia covariance/nonlinear diagnostics and independent helper audit. Exact8 reviewed without substitution. Completion is separate from tier. No ledger or public edits.
