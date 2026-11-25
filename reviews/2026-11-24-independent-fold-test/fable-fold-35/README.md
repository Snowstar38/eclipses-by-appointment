# Independent review of Fable's 35 fold-flagged TESS apertures

Nineteen of the 35 apertures showed visually distinct, repeating eclipse-like dips on a different schedule from the pipeline prediction. Four of the 19 have competing periods. For eight stars, ground-based ZTF photometry dimmed at the times predicted from TESS, and TESS difference images placed the missing light at the nominal star in at least two sectors. All eight were already listed as machine-selected targets by Kostov et al. This review supplies timing, source localization and independent photometry for those candidates. [All 35 outcomes](outcomes.csv) · [Eight ground light curves](ground/recoveries.png) · [Kostov et al. Table 2](https://vizier.cfa.harvard.edu/viz-bin/VizieR-3?-source=J/ApJS/279/50/table2)

## Which preliminary flag helped?

Fable screened 688 previously unadjudicated TESS full-frame apertures with threshold-crossing events. These 35 showed two adjacent bins in a phase fold that were much deeper than the depth recorded by the pipeline. We reviewed the supplied roster in groups of 10, 10, 10 and 5. All 35 had the adjacent-bin flag. The other piece of information available before this review was whether the aperture had also appeared in the published machine-selected list.

| Prior machine selection | Reviewed | Repeated eclipse shapes seen visually | Repeats with a supported alternative timing solution | Also recovered from the ground |
| --- | ---: | ---: | ---: | ---: |
| Yes | 25 | 22 | 19, including four with aliases | 8 |
| No | 10 | 0 | 0 | 0 |

For a similar backlog, a first pass can start where both flags agree. The ten stars in the second row are too few to establish a general exclusion rule. This enriched transfer had no comparison group without the adjacent-bin flag. The highest-return change here was searching for another period and testing whether eclipses actually occurred at its predictions. [Frozen roster](batch.csv) · [Individual visual calls](terra/assessment.csv) · [Timing decisions](sol/outcome.csv)

## What the light curves show

Sol's independent search examined 0.60–40 days and counted sampled eclipse windows, including sensitive windows with missing dips. Terra separately inspected time-series plots and individual event shapes. The independent timing review found 15 supported alternatives, four alternatives with competing periods, nine inconsistent pipeline clocks with no strong replacement, six inconclusive results and one star with limited coverage. All 19 timing recoveries were also called repeated in the visual review. Three further stars were visual repeats without a supported replacement in that timing search. Overlapping SAP and corrected flux are measurements from the same instrument. [Timing methods and aliases](sol/README.md) · [Visual review](terra/README.md)

| TIC | TESS period tested successfully on ZTF (days, rounded) | TESS hits / covered windows at Sol's preferred period | ZTF bands passing |
| --- | ---: | ---: | --- |
| 51271205 | 21.6076 | 4 / 4 | g |
| 199572139 | 16.6370 | 29 / 29 | g |
| 219113068 | 21.7757 | 10 / 10 | g, r |
| 219433150 | 17.4927 | 16 / 16 | g, r |
| 243241330 | 20.5489 | 3 / 3 | r |
| 345352706 | 21.9246 | 3 / 3 | g, r |
| 376993642 | 13.1994 | 39 / 39 | g, r |
| 416116421 | 11.4490 | 9 / 9 | g, r |

TIC 376993642 supplied the most opportunities to check a prediction. TESS sampled all 39 qualifying windows in 20 sectors. In sectors 21 and 77, difference images of both eclipse families place the lost light within 1.25 arcseconds of the nominal Gaia star. The closest screened competitor is over 63 arcseconds from the fitted centers. For TIC 51271205, the ZTF test passed at Fable's 21.6076-day period. Sol's slightly different 21.6122-day fit recovered four TESS windows. These tabulated periods are timing hypotheses and some admit orbital harmonics. [Four difference images](pixels/376993642.png) · [Ground measurements by period and filter](ground/phase-checks.csv)

Across the 16 stars examined in the original target pixels, 48 of 51 event windows favored the nominal Gaia position. Two lacked a usable baseline on one side and one moved appreciably when the reference baseline changed. Selected stars with compact losses can still contain close unresolved companions. Two extreme dips in other apertures, TIC 52157743 and TIC 218233922, largely disappeared when the estimated sky was restored. The latter also had an observing gap. The background test explains why those events carry little weight as eclipses. [Pixel evidence by star](pixels/README.md) · [Signed flux and sky measurements](background/README.md)

## Prior work and replay

Eleven catalogue cone searches with positive controls covered 15 arcminutes around each position. Every target also received an exact Villanova lookup and a Gaia source check. The live Villanova service has a record for TIC 237115356, where the signal is marked outside its EB catalogue and has no published period on the detail page. Gaia already reports a 42.09-day spectroscopic orbit for TIC 302671930 and a 750.9-day astrometric orbit for TIC 468333801. These prior identifications matter even where the TESS eclipsing period remains open. This is an event-and-source review packet. It makes no additions to the accepted-systems ledger. [Catalogue receipts and limits](credit/README.md) · [Villanova record](https://tessebs.villanova.edu/0237115356)

The 283 TESS sector products contain 953,501 quality-zero, finite-time cadences before the reviewers' additional filtering. To reproduce the photometry cache, run `python cadences.py CACHE` from this directory with NumPy, Astropy and Requests. The script checks the archived arrays against the signed-off time and flux hashes. Pass the resulting directory to the timing and visual scripts. The pixel analysis uses original target-pixel files, and the ground test uses its own archive queries and independent measurements. Run `python summary.py` to regenerate the joined outcome table from the review results. [TESS product manifest](cadences.csv) · [ZTF method and replay](ground/README.md)
