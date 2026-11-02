# TIC 464615512: CONFIRMED

Full bounded physical review: COMPLETE. Six repeated very deep primary eclipses and unequal secondary near0.484; no capable Gaia neighbor within60arcsec. Separate broad sector-specific baseline features are not interpreted as additional eclipses.

Raw QLP SAP_FLUX representative events and full-sector P/2P morphology were visually inspected. Quality-zero finite positive samples only; predictions guide windows and are never timings. 6 identifiable free-center timings define P=12.132109767254 +/- 0.000040774170d, reference BTJD=1666.196728878 +/- 0.007945530d. Epoch error meaning: Conservative linear timing-fit covariance under the stated cadence floor and scatter inflation; excludes uncalibrated shape and baseline systematics. Epoch kind: Deeper primary established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced chi square=2.0581650195498122; zero degrees of freedom is null. All errors retain their named meanings; no calibrated coverage is claimed. Selected same-kind recurring eclipse family; parity and P/2 coverage checked.

Depth=359.483490ppt is the median realized central trapezoid loss d*min(1,w/(2*k)); extrapolated amplitude and ingress remain separately in [measurements.json](../../campaign/batch13/464615512/measurements.json). Measured secondary phase 0.48380129, formal phase error 9.2680635e-06, realized depth 103.09249ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Secondary raw pooled windows, actual sectors/cycles and fitted phase are retained in [secondary-windows.csv](../../campaign/batch13/464615512/secondary-windows.csv) and [../secondary-phases.json](../../campaign/batch13/secondary-phases.json). No exhaustive blind alias search asserted. [../alias-audit.json](../../campaign/batch13/alias-audit.json) and [../half-period-coverage.json](../../campaign/batch13/half-period-coverage.json) retain recurrence/parity and sampled opposite-phase evidence. Flagged coverage is never a clean null.

Fresh TESScut difference image sector27 stacks1 core/bilateral-sideband events. Target pixel=[7.360916693333532, 7.227960131360918], deficit=[7.3710405105484265, 7.182247867165817]; descriptive offset=0.04682pixel, field PSF residual=0.67489. No arbitrary centroid cut or calibrated localization error is imposed. Every capable neighbor below was inspected at its actual projected pixels; close overlapping neighbors retain probable ownership. Every capable neighbor is assessed above and below; close overlapping cases retain unresolved attribution. All Gaia neighbors are retained in pixel JSON.

| Source | Separation arcsec | G | Required intrinsic loss proxy | Pixel coordinate | Diluted pixel loss |
|---|---:|---:|---:|---|---:|
| None | | | | | |

G-band pairwise brightness screen assumes approximate passband/aperture response; intrinsic required eclipse cannot be directly compared with diluted pixel loss. Unresolved unlisted companions are not excluded.

Alternative reduction: independently extracted background-subtracted TESScut1x1/3x3/5x5 depths=335.46678/326.58787/302.16880ppt; QLP median=359.48349ppt. Pixel sector27 is a distinct observing occasion on the same TESS instrument; no same-sector QLP comparison claimed. Independent processing is not an independent instrument. Different apertures respond differently to dilution/background.

Gaia source6632294477079223424: period=12.130264395+/-0.002677318d; e=0.0431035; omega=100.9771082deg; periastron BTJD=392.75081417. Closest conjunction offset=0.1073164d (0.0088470phase), source-specific full-covariance linear error=0.2689574d. Correlation order P,gamma,K,e,omega,Tp with subindices0,3,4,5. Linear propagation is descriptive, not a Gaussian veto or ownership proof. Both conjunctions retained in [../gaia-geometry.json](../../campaign/batch13/gaia-geometry.json). Mass function=0.06168672solar, assumed M1=0.7, minimum M2=0.428211; approximate central duration=5.0735h versus observed=3.7305h. TIC radius/main-sequence companion scaling, edge-on conjunction and stellar evolution are assumptions; this is a plausibility check, not a fitted physical solution.

| Sector | Same-kind cycle | Measured BTJD | Formal center error d | Conservative input error d | Realized depth ppt |
|---|---:|---:|---:|---:|---:|
| 13 | 0 | 1666.191836129 | 6.5269142e-05 | 0.0104166054 | 304.72105 |
| 13 | 1 | 1678.324004395 | 5.7909108e-05 | 0.0104166054 | 351.07842 |
| 94 | 181 | 3862.111229584 | 5.37777875e-05 | 0.00115739457 | 367.88855 |
| 94 | 182 | 3874.238911981 | 0.000119659522 | 0.00115739457 | 329.43308 |
| 104 | 208 | 4189.675331762 | 6.16962419e-05 | 0.00115740685 | 368.32298 |
| 104 | 209 | 4201.807180712 | 4.84459908e-05 | 0.00115740685 | 368.06487 |

Catalogue novelty is separate from this physical verdict. Shared coverage matrix and source identity checks are authoritative for catalogue recovery; period agreement alone cannot establish attribution.


Stable review key: R664.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch13/464615512/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch13/464615512/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch13/464615512/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch13/464615512/fresh-pixels/run.log)
- [historical/diff_s27.json](../../campaign/batch13/464615512/historical/diff_s27.json)
- [historical/diff_s27.png](../../campaign/batch13/464615512/historical/diff_s27.png)
- [historical/gaia.json](../../campaign/batch13/464615512/historical/gaia.json)
- [measurements.json](../../campaign/batch13/464615512/measurements.json)
- [phase-review.png](../../campaign/batch13/464615512/phase-review.png)
- [raw-events.png](../../campaign/batch13/464615512/raw-events.png)
- [raw-windows.csv](../../campaign/batch13/464615512/raw-windows.csv)
- [secondary-windows.csv](../../campaign/batch13/464615512/secondary-windows.csv)

[Batch audits and scripts](../../campaign/batch13/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
