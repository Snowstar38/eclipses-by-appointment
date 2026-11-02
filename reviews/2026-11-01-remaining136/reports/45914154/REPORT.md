# TIC 45914154: CONFIRMED

Full bounded physical review: COMPLETE. Six narrow repeated primary eclipses and unequal secondary near0.4498; the initial near-half-phase secondary fit failed and was replaced using observed morphology. Capable43.95arcsec neighbor is separated from deficit core.

Raw QLP SAP_FLUX representative events and full-sector P/2P morphology were visually inspected. Quality-zero finite positive samples only; predictions guide windows and are never timings. 6 identifiable free-center timings define P=10.667224966865 +/- 0.000011479419d, reference BTJD=1551.834932386 +/- 0.002207357d. Epoch error meaning: Conservative linear timing-fit covariance under the stated cadence floor and scatter inflation; excludes uncalibrated shape and baseline systematics. Epoch kind: Deeper primary established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced chi square=0.33448381934669585; zero degrees of freedom is null. All errors retain their named meanings; no calibrated coverage is claimed. Selected same-kind recurring eclipse family; parity and P/2 coverage checked.

Depth=30.291826ppt is the median realized central trapezoid loss d*min(1,w/(2*k)); extrapolated amplitude and ingress remain separately in [measurements.json](../../campaign/batch10/45914154/measurements.json). Measured secondary phase 0.44978814, formal phase error 0.0001975221, realized depth 9.06765ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Secondary raw pooled windows, actual sectors/cycles and fitted phase are retained in [secondary-windows.csv](../../campaign/batch10/45914154/secondary-windows.csv) and [../secondary-phases.json](../../campaign/batch10/secondary-phases.json). No exhaustive blind alias search asserted. [../alias-audit.json](../../campaign/batch10/alias-audit.json) and [../half-period-coverage.json](../../campaign/batch10/half-period-coverage.json) retain recurrence/parity and sampled opposite-phase evidence. Flagged coverage is never a clean null.

Fresh TESScut difference image sector62 stacks3 core/bilateral-sideband events. Target pixel=[7.325906164591727, 7.868176405273294], deficit=[7.010100206327275, 8.045952524192558]; descriptive offset=0.36241pixel, field PSF residual=0.99046. No arbitrary centroid cut or calibrated localization error is imposed. Every capable neighbor below was inspected at its actual projected pixels; close overlapping neighbors retain probable ownership. Other capable sources are displaced from compact deficit core but crowding limits localization. All Gaia neighbors are retained in pixel JSON.

| Source | Separation arcsec | G | Required intrinsic loss proxy | Pixel coordinate | Diluted pixel loss |
|---|---:|---:|---:|---|---:|
| 5419779854563773184 | 43.95486704547451 | 16.304293 | 0.9694385641989272 | [9.273971241968145, 8.780659099326206] | -0.0003462748400213247 |

G-band pairwise brightness screen assumes approximate passband/aperture response; intrinsic required eclipse cannot be directly compared with diluted pixel loss. Unresolved unlisted companions are not excluded.

Alternative reduction: independently extracted background-subtracted TESScut1x1/3x3/5x5 depths=29.78637/27.75578/19.57276ppt; QLP median=30.29183ppt. Pixel sector62 is a distinct observing occasion on the same TESS instrument; no same-sector QLP comparison claimed. Independent processing is not an independent instrument. Different apertures respond differently to dilution/background.

Gaia source5419774189506366080: period=10.666312433+/-0.001434373d; e=0.0726193; omega=158.3442045deg; periastron BTJD=390.96497204. Closest conjunction offset=0.0423919d (0.0039744phase), source-specific full-covariance linear error=0.1580353d. Correlation order P,gamma,K,e,omega,Tp with subindices0,3,4,5. Linear propagation is descriptive, not a Gaussian veto or ownership proof. Both conjunctions retained in [../gaia-geometry.json](../../campaign/batch10/gaia-geometry.json). Mass function=0.08809977solar, assumed M1=1.38, minimum M2=0.732606; approximate central duration=8.8745h versus observed=5.0055h. TIC radius/main-sequence companion scaling, edge-on conjunction and stellar evolution are assumptions; this is a plausibility check, not a fitted physical solution.

| Sector | Same-kind cycle | Measured BTJD | Formal center error d | Conservative input error d | Realized depth ppt |
|---|---:|---:|---:|---:|---:|
| 9 | 0 | 1551.838413706 | 0.00117917629 | 0.01041665 | 29.19653 |
| 9 | 1 | 1562.502738903 | 0.0010803001 | 0.01041665 | 31.38712 |
| 63 | 138 | 3023.912638502 | 0.00113451408 | 0.00115739218 | 34.56799 |
| 63 | 139 | 3034.578401520 | 0.000936841378 | 0.00115739218 | 34.70781 |
| 99 | 234 | 4047.966147058 | 0.000752732181 | 0.00115747247 | 27.78180 |
| 99 | 236 | 4069.299542567 | 0.000873381377 | 0.00115747247 | 27.41253 |

Catalogue novelty is separate from this physical verdict. Shared coverage matrix and source identity checks are authoritative for catalogue recovery; period agreement alone cannot establish attribution.


Stable review key: R633.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch10/45914154/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch10/45914154/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch10/45914154/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch10/45914154/fresh-pixels/run.log)
- [historical/diff_s62.json](../../campaign/batch10/45914154/historical/diff_s62.json)
- [historical/diff_s62.png](../../campaign/batch10/45914154/historical/diff_s62.png)
- [historical/gaia.json](../../campaign/batch10/45914154/historical/gaia.json)
- [measurements.json](../../campaign/batch10/45914154/measurements.json)
- [phase-review.png](../../campaign/batch10/45914154/phase-review.png)
- [raw-events.png](../../campaign/batch10/45914154/raw-events.png)
- [raw-windows.csv](../../campaign/batch10/45914154/raw-windows.csv)
- [secondary-windows.csv](../../campaign/batch10/45914154/secondary-windows.csv)

[Batch audits and scripts](../../campaign/batch10/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
