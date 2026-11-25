# Ten fold-only leads from the mixed-method backlog

None of these ten known Gaia spectroscopic binaries showed a securely repeating eclipse in this review. Three of the original leads traced to a particularly clear failure mode. On the same TESS exposure, dozens of unrelated stars on one camera appeared to lose about 14% of their light in the corrected light curves, while their aperture measurements stayed steady. The effect occurred on three specific camera/exposure pairs in sector 26. [Camera comparison](cadence-controls/camera-dips.png) · [Individual stars and decisions](sol/outcomes.csv)

## Which leads were tested

The November 5 mixed-method harvest contained 2,904 eligible targets and its dedicated register recorded 380 completed physical reviews. Subtracting reviewed TICs from the archived ranking left 2,524 outside that register, including 48 in the fold-only group. We took the first ten fold-only targets in historical priority order at declination −25° or higher after excluding earlier reviews, current project identities, Fable's active rosters, and nearby catalogue or collaborator positions. The northern cut favored ground follow-up. The targets are known single-lined spectroscopic binaries. The unresolved question was whether their light also shows eclipses. [Roster and historical ranks](batch.csv)

The ten TICs are now recorded in this separate review. Of the historical 2,904, 2,514 occur in neither the original 380-row register nor this ten-row assessment. Other surveys may have examined some of those stars. [Selection details and table hashes](selection.json)

## A field test for false eclipses

The archived fold for TIC 302399892 included a 14% drop on exposure **38482**. So did the fold for TIC 388584591, on another detector chip of camera 4. For both, uncorrected aperture measurements changed by less than 0.1% of baseline. TIC 390126467 showed a similar corrected-only dip on exposure **38490** on camera 2. Comparing the exposure numbers matters because barycentric timestamps for two stars can differ during the very same TESS exposure. [Cadence-level measurements](cadence-controls/measurements.csv)

We drew 192 other stars, twelve per detector chip across all four cameras, at least six arcminutes from each other and from the reviewed stars with sector 26 data. A control registers a loss when its corrected light drops by more than 5% while its aperture flux stays within 1% of its local baseline. We required usable measurements on both sides. These are correlated measurements of a shared exposure.

| Exposure | Camera | Field stars passing / measurable on that camera | Median apparent corrected loss |
| ---: | ---: | ---: | ---: |
| 38482 | 4 | 36 / 36 across three chips | 13.75% |
| 38490 | 2 | 48 / 48 across four chips | 13.74% |
| 38491 | 3 | 48 / 48 across four chips | 14.43% |

At the two initial exposures, none of the measurable controls on other cameras passed. Nor did any of the 2,748 usable star/exposure comparisons at 20 shifted exposures. After examining those two events, we searched every exposure in the sector. Requiring at least 12 measured controls, two chips with at least three measurements each, and 80% of stars passing selected **three of 3,084** sufficiently sampled camera/exposure pairs. The search recovered the first two and identified exposure 38491 on camera 3. The field measurements justify flagging those corrected measurements for review. The specific pipeline or instrumental cause remains open. A star with a dip on another date retains that evidence. [Full sector scan](cadence-controls/exposure-scan.csv) · [Reproduction and limits](cadence-controls/README.md)

## Stellar signals and remaining uncertainty

Sol measured the original predictions in 61 QLP sector products, searched alternative phases and compared both flux reductions. Terra independently inspected time series, folds and individual event shapes for all ten. Neither review found a convincing repeating eclipse. Two cases are worth distinguishing.

* **TIC 197243461** has two shallow dips, 13 trial periods apart at roughly 56.33 days. Both QLP and TESS-SPOC show losses of the same sign on those dates. The pipelines used the same exposures. The later dip is only about twice the local noise in QLP; the earlier window has a disturbed baseline. A third well-sampled event remains the discriminating observation. [Window plots](terra/197243461-windows.png) · [Other extraction](holdout/events.csv)
* **TIC 244201152** had a roughly 0.5% dip in sector 42. A well-covered sector 3 prediction lacked a comparable dip. Its isolated event remains in the record. [Window plots](terra/244201152-windows.png)

At fixed TESS predictions, ASAS-SN and ZTF provided 12,179 good measurements across nine targets. No star met the ground recovery rule. Three had adequate cycle and comparison-phase coverage, while seven were coverage-limited. An additional 45 SPOC-family light curves provided six sensitive empty predictions and no passing window on the alternate-extraction test. The two additional sector 1751 light curves contained no predicted core. [Ground report](ground/README.md) · [Alternate-extraction method](holdout/README.md)

For the original fold epoch of each star we also calculated the two expected edge-on conjunctions from the published Gaia orbit. For seven of ten stars, neither branch's approximate 95% timing interval overlapped the fold core at that epoch. This tests compatibility with the known orbit under an edge-on assumption. It does not exclude a different orbit or an eclipse hidden in a gap. Gaia also lists a possible pulsational variability class for TIC 14832729. We matched all ten positions to Gaia and ran eleven catalogue-cone queries with positive controls. These ten assessments are recorded separately from the historical mixed-method register. No systems were added to the accepted catalogue. [Orbit data and assumptions](orbits/README.md) · [Gaia matches](credit/all-sources.json) · [Catalogue queries](credit/wide.json) · [Timing review and archive replay](sol/README.md) · [Visual review](terra/README.md)
