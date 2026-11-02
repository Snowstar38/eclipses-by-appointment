# TIC 66503432: CONFIRMED

Full bounded physical review: COMPLETE. Physical verdict and scoped catalogue novelty are separate. The epoch column names the selected repeating eclipse kind; deeper-primary rank is not assumed.

**Deciding evidence:** Nine deep selected eclipses and eight measured secondaries establish unequal spacings: secondary phase0.47448, then0.52552 back to selected kind. Half period cannot represent this event sequence. Compact target deficit has no capable Gaia neighbor within60arcsec. Source-specific Gaia predicts other phase0.51951 +/-0.01607 (linear allowance), a0.0450phase tension (~2.8 allowances). Argument-of-periastron and A/B conventions were checked against methods; observed centers, not Gaia predictions, define secondary phase. Primary conjunction agrees within0.0374d versus0.0965d allowance. This modest secondary geometry tension is retained as a limitation, not a calibrated rejection. Approximate minimum-mass central-duration model also remains a plausibility screen.

9 free-center quality-zero raw QLP SAP_FLUX timings in sectors[7, 61, 88] give P=8.3303238499 +/-0.0000193548d and selected-kind reference BTJD=1499.0390880. Median fitted diluted QLP depth=245.421ppt. Predicted windows guide the fit; they are not measured timings. Flagged/uncovered windows are not clean nulls. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Zero-degree-of-freedom reduced chi square is null, and singular center covariance is rejected. Representative raw plots and full raw phase plots were visually inspected. Within-sector consecutive same-kind counts and parity are recorded in [../alias-audit.json](../../campaign/batch05/alias-audit.json); half/double alternatives were checked against actual recurrence/secondary morphology. A double orbit with identical unseen labels cannot be exhaustively excluded; no exhaustive blind alias search is claimed.

Observed secondary check: 8 accepted secondary-candidate free-center fits, median actual phase0.4744845. Eccentric Gaia other conjunction is phase0.519507 +/-0.016070 descriptive linear allowance. This is evaluated at its actual phase, never assumed0.5. Weak/noisy box maxima in phase-review.json are search candidates, not detections.

Fresh TESScut S7 difference stack contains3 actually covered events. Deficit minus target=[-0.1339344344676583, -0.01917256934034217]pixel (radial0.135); target pixel coordinate=[7.4242021642934155, 7.498721557408501]; deficit=[7.290267729825757, 7.479548988068159]. Global PSF residual=0.855 is not a localization uncertainty. Actual target rounded-pixel signed deficit/baseline=90.161/382.86 electron/s. All0 capable Gaia neighbors within60arcsec are assessed below from real pixels. Required intrinsic loss is a pairwise Gaia G passband proxy; it must not be compared directly with diluted fractional pixel loss. Actual deficit and baseline are reported in common electron/s units. Colors, aperture response, PSF overlap, and unlisted faint/unresolved sources limit this screen; no calibrated centroid confidence or full PSF deblend is claimed.

|Gaia source|sep arcsec|G|required intrinsic loss proxy|signed pixel deficit e/s|pixel baseline e/s|distance to deficit px|attribution assessment|
|---|---:|---:|---:|---:|---:|---:|---|
|None capable within60arcsec||||||||

Alternative background-subtracted fixed target-centered TESScut1x1/3x3/5x5 depths=235.493/182.499/100.071ppt. Faintest40percent per-cadence background, symmetric local pre/post windows and actual covered cores provide an alternative extraction. Retained pixel-arrays.npz contains actual deficit/baseline. This is a reused numerical primitive with fresh ephemeris/duration, not independent-code replication. QLP and custom extractions share TESS photons in overlapping sectors; differing sectors are separate observing occasions on one instrument. Aperture/sector depth differences are dilution and reduction limitations, not intrinsic depth agreement.

Gaia DR3 source5616340171040985088 has P=8.331321017d, e=0.255453, omega=83.3363deg, Tp=390.922279BTJD. Both edge-on eccentric conjunctions and source-specific full NSS covariance are retained in [../gaia-geometry.json](../../campaign/batch05/gaia-geometry.json). Closest selected-kind offset=-0.037390d (-0.004488phase), linear covariance allowance=0.096489d. The SB1 lower triangle uses P,gamma,K,e,omega,Tp, and selected subindices0,3,4,5; minimum full correlation eigenvalue=0.011791. This descriptive linear approximation is not a calibrated rejection threshold. Mass function=0.17756solar masses; assumed TIC/adopted M1=1.250, minimum M2=0.951; TIC/adopted radius=3.074solar radii. Approximate central duration=8.802h versus measured6.875h. Main-sequence minimum-mass companion and TIC mass/radius make this a plausibility screen, not a fitted geometry. Orbital agreement alone cannot establish source ownership.

|Sector|same-kind search cycle|measured midpoint BTJD|formal center error d|timing input allowance d|depth ppt|
|---|---:|---:|---:|---:|---:|
|7|0|1499.0403290|0.00052515|0.0104166|245.421|
|7|1|1507.3650109|0.000934794|0.0104166|244.399|
|7|2|1515.7001850|0.000967621|0.0104166|242.915|
|61|176|2965.1775934|0.000232527|0.00115739|251.223|
|61|177|2973.5050634|0.000238581|0.00115739|247.312|
|61|178|2981.8367346|0.000337039|0.00115739|259.418|
|88|264|3698.2400203|0.000524037|0.00115739|223.748|
|88|265|3706.5768666|0.00042712|0.00115739|251.049|
|88|266|3714.9077080|0.000443278|0.00115739|228.439|

**Limitations and next check:** Refine spectroscopic eccentric geometry and compare measured secondary phases; resolved physical modeling. Representative events suffice for this bounded review; no all-sector/all-event precision campaign is claimed. Sector-dependent dilution, finite cadence, baseline choice, color proxy, and linear Gaia propagation remain material limitations.

Catalogue checks use [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv) and the shared receipt manifest; known recovery is separated from physical classification and no exhaustive priority claim is made. Evidence: measurements.json/raw-windows.csv/raw-events.png; fresh-pixels/diff_fresh.json/png/pixel-arrays.npz; [neighbor-assessment.json](../../campaign/batch05/66503432/neighbor-assessment.json); batch phase, secondary, alias, identity/source receipts, methods snapshot and audits. SHA256SUMS.json freezes exact sources and outputs.


Stable review key: R584.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch05/66503432/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch05/66503432/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch05/66503432/fresh-pixels/gaia.json)
- [fresh-pixels/pixel-arrays.npz](../../campaign/batch05/66503432/fresh-pixels/pixel-arrays.npz)
- [fresh-pixels/run.log](../../campaign/batch05/66503432/fresh-pixels/run.log)
- [historical/diff_s07.json](../../campaign/batch05/66503432/historical/diff_s07.json)
- [historical/diff_s07.png](../../campaign/batch05/66503432/historical/diff_s07.png)
- [historical/gaia.json](../../campaign/batch05/66503432/historical/gaia.json)
- [measurements.json](../../campaign/batch05/66503432/measurements.json)
- [neighbor-assessment.json](../../campaign/batch05/66503432/neighbor-assessment.json)
- [raw-events.png](../../campaign/batch05/66503432/raw-events.png)
- [raw-windows.csv](../../campaign/batch05/66503432/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch05/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
