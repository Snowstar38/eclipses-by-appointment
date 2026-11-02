# Independent helper audit: batch 07

I examined the representative raw-event, phase, secondary-window, and fresh difference-image contact sheets and individual crowded-field pixel maps, together with timing, alias, coverage, and geometry artifacts. These are independent checks of the lead's measurements, not independent observations. QLP and TESSCut are different reductions of the same TESS photons; distinct sectors are distinct observing occasions on one instrument.

- 287756198: repeated shallow raw events in sectors 11, 64 and 102; target-centered deficit and capable distant neighbours warrant source-specific discussion, with no secure secondary. Measured 15.659843 d recurrence is supported by within-sector events and the examined cycle alternatives.
- 301986385: repeated raw events in 56 and 83, compact target-centered deficit and no G-proxy capable neighbour inside 60 arcsec. A secondary-like dip at phase 0.50004 is visible; the pooled model's formal uncertainty does not account for red noise and normalization.
- 164660905: three fitted events in 27, 92 and 94, consistent morphology, tested nearby integer counts and half-period coverage. The deficit is near target, whereas the brighter off-target source shifts the light centroid south. Capable G14.24 neighbour 32.9 arcsec away lies to the right and the loss image favors target, without a formal PRF exclusion. No secure secondary.
- 374606776: repeated events, but spatial attribution is unresolved: capable G16.27 and G16.11 neighbours within about a pixel and a brighter G10.77 source 22.2 arcsec away overlap the target response; the difference image alone cannot uniquely separate them. Probable is justified despite real periodic eclipses. No secure secondary.
- 376669046: four measured centers: sector 13 pair and sectors 93 and 104. Same-sector pair directly constrains recurrence; nearby integer cycle fits favor 144 cycles across the long baseline, maximum residual 0.00832 d versus 1.33 d for next candidate reported in tested range. Half-period windows/coverage must be distinguished from flagged windows; no secure secondary. Target-centered deficit, with a flux-capable neighbour at 59 arcsec.
- 338069871: strong repeated 3.962546 d events, target-centered deficit; capable neighbours must be assessed individually. The known EW at 45.14 arcsec is a nearby source, not target recovery. Rounded VSX coordinates match Gaia 2205143893189353088 to 0.070 arcsec, G20.066; its 0.3798394 d period differs greatly from the measured period and G-proxy required intrinsic depth is about 12.16, above unity. Both the G/TESS conversion and throughput are approximate. The G16.23 neighbour at similar radius is a different source and is flux-capable. See helper-ew-identity.json.
- 21411263: two convincing fitted S47 eclipses separated by 12.715567 d. Only two fitted centers imply zero degrees of freedom, so a zero chi-square is not evidence of fit quality. Current QLP S21 and S47: predicted S21 primary windows have only one and zero usable points, with two and three flagged respectively; no clean S21 null. S47 half-period extra windows disfavor equal events at P/2, subject to flagged cadences. Target-centered deficit; G15.17 neighbour 27 arcsec requires about 91% eclipse under a G proxy, with spatial information favoring target. No secure secondary.
- 395396499: repeated raw eclipses, target-centered loss in crowded S65 image, while baseline light centroid is displaced by other bright stars. Capable southwest neighbours at 29–34 arcsec are not categorically excluded; target is favored by morphology but source mixing remains a limitation. Nearby cycle alternatives and phase/parity inspected; no secure secondary.
- 73023909: four fitted events across S19 and S59, two per sector; 13.620320 d recurrence and cross-sector cycle alternatives support timing, rather than an isolated two-event interpretation. Target-centered deficit; G14.05 neighbour at 52.6 arcsec is flux-capable but spatially separated. No secure secondary.
- 337004236: repeated eclipses and stable timing, but G14.85 at 17.4 arcsec and G14.43 at 21.9 arcsec are flux-capable near-pixel alternatives, as is bright G11.88 at 36.9 arcsec. Loss is near target but the close sources are blended; probable is warranted without source-resolved evidence. No secure secondary.

Gaia geometry uses source-specific orbit/covariance and is supporting physical consistency, not proof of source attribution. Central duration assumes stellar properties and geometry and is not a fitted radius constraint. The actual secondary is distinct from a predicted Gaia conjunction. The numerical neighbour depth is an intrinsic required loss based on a G-band proxy and cannot be compared directly to diluted per-pixel loss. Pixel maps are descriptive, not calibrated centroid significance; no universal offset threshold was used. Formal fit uncertainties do not include all photometric and model systematics.

The user and coordinator's appreciation is warmly received. This anonymous note records the independent review.

Independent weighted linear refit of saved usable centers, using saved timing allowances and covariance inflation max(1, reduced chi-square), reproduced all ten periods and period errors. Columns: TIC, number of events, period d, reported error d, chi-square/degrees of freedom. For two points chi-square is an algebraic zero with zero degrees of freedom, so goodness of fit is undefined.

```
164660905  3  18.063195670039  0.000035776421848  0.004636/1
21411263   2  12.715567269730  0.00491058014562   undefined/0
287756198  5  15.659843071955  0.000045212290418  3.431311/3
301986385 15   3.416145875984  0.000003334283635 17.621056/13
337004236 21   3.513578326574  0.000002742790178  9.480602/19
338069871 18   3.962546381080  0.000004322642696 11.385968/16
374606776  8   8.855801164641  0.000021865495140  7.042424/6
376669046  4  17.598785473509  0.000062049778973  3.648407/2
395396499 26   2.134725893363  0.000001753071051 37.923938/24
73023909   4  13.620320142574  0.000092487252458  0.073968/2
```
