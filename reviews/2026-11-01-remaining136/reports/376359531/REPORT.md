# TIC 376359531: CONFIRMED

Full bounded physical review: COMPLETE. Six identifiable same-kind timings, including consecutive sector55 cycles2/3 and82 cycles134/135, plus unequal observed secondary near0.5. Two historical event fits have unidentifiable timing covariance and are excluded. No capable neighbor within60arcsec.

Raw QLP SAP_FLUX representative events and full-sector P/2P morphology were visually inspected. Quality-zero finite positive samples only; predictions guide windows and are never timings. 6 identifiable free-center timings define P=5.587737013729 +/- 0.000016034968d, reference BTJD=2801.930697619 +/- 0.002028476d. Epoch error meaning: Conservative linear timing-fit covariance under the stated cadence floor and scatter inflation; excludes uncalibrated shape and baseline systematics. Epoch kind: Deeper primary established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced chi square=0.1373511919157084; zero degrees of freedom is null. All errors retain their named meanings; no calibrated coverage is claimed. Selected same-kind recurring eclipse family; parity and P/2 coverage checked.

Depth=73.012502ppt is the median realized central trapezoid loss d*min(1,w/(2*k)); extrapolated amplitude and ingress remain separately in [measurements.json](../../campaign/batch14/376359531/measurements.json). Measured secondary phase 0.49964948, formal phase error 0.00037053477, realized depth 8.52461ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Secondary raw pooled windows, actual sectors/cycles and fitted phase are retained in [secondary-windows.csv](../../campaign/batch14/376359531/secondary-windows.csv) and [../secondary-phases.json](../../campaign/batch14/secondary-phases.json). No exhaustive blind alias search asserted. [../alias-audit.json](../../campaign/batch14/alias-audit.json) and [../half-period-coverage.json](../../campaign/batch14/half-period-coverage.json) retain recurrence/parity and sampled opposite-phase evidence. Flagged coverage is never a clean null.

Fresh TESScut difference image sector82 stacks3 core/bilateral-sideband events. Target pixel=[7.3124070643101575, 7.770191815637181], deficit=[7.2296148184937135, 7.8042847951310135]; descriptive offset=0.08954pixel, field PSF residual=0.18151. No arbitrary centroid cut or calibrated localization error is imposed. Every capable neighbor below was inspected at its actual projected pixels; close overlapping neighbors retain probable ownership. Other capable sources are displaced from compact deficit core but crowding limits localization. All Gaia neighbors are retained in pixel JSON.

| Source | Separation arcsec | G | Required intrinsic loss proxy | Pixel coordinate | Diluted pixel loss |
|---|---:|---:|---:|---|---:|
| None | | | | | |

G-band pairwise brightness screen assumes approximate passband/aperture response; intrinsic required eclipse cannot be directly compared with diluted pixel loss. Unresolved unlisted companions are not excluded.

Alternative reduction: independently extracted background-subtracted TESScut1x1/3x3/5x5 depths=70.73307/70.89453/66.96925ppt; QLP median=73.01250ppt. Pixel sector82 shares the same TESS photons with retained QLP and checks extraction robustness. Independent processing is not an independent instrument. Different apertures respond differently to dilution/background.

Gaia source1732755043189031040: period=5.588022491+/-0.000779717d; e=0.1090962; omega=260.0413444deg; periastron BTJD=390.66862379. Closest conjunction offset=-0.1606872d (-0.0287556phase), source-specific full-covariance linear error=0.3346143d. Correlation order P,gamma,K,e,omega,Tp with subindices0,3,4,5. Linear propagation is descriptive, not a Gaussian veto or ownership proof. Both conjunctions retained in [../gaia-geometry.json](../../campaign/batch14/gaia-geometry.json). Mass function=0.04760853solar, assumed M1=1, minimum M2=0.468182; approximate central duration=8.0545h versus observed=6.2111h. TIC radius/main-sequence companion scaling, edge-on conjunction and stellar evolution are assumptions; this is a plausibility check, not a fitted physical solution.

| Sector | Same-kind cycle | Measured BTJD | Formal center error d | Conservative input error d | Realized depth ppt |
|---|---:|---:|---:|---:|---:|
| 55 | 0 | 2801.931363300 | 0.000539631697 | 0.00347223956 | 73.52269 |
| 55 | 2 | 2813.105236448 | 0.000700386189 | 0.00347223956 | 73.50865 |
| 55 | 3 | 2818.694065630 | 0.0006067061 | 0.00347223956 | 74.71809 |
| 82 | 131 | 3533.924769084 | 0.000476516555 | 0.00115739494 | 72.51636 |
| 82 | 134 | 3550.686899473 | 0.000486035652 | 0.00115739494 | 71.61014 |
| 82 | 135 | 3556.275242298 | 0.000376384731 | 0.00115739494 | 71.95061 |

Catalogue novelty is separate from this physical verdict. Shared coverage matrix and source identity checks are authoritative for catalogue recovery; period agreement alone cannot establish attribution.


Stable review key: R672.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch14/376359531/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch14/376359531/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch14/376359531/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch14/376359531/fresh-pixels/run.log)
- [historical/diff_s82.json](../../campaign/batch14/376359531/historical/diff_s82.json)
- [historical/diff_s82.png](../../campaign/batch14/376359531/historical/diff_s82.png)
- [historical/gaia.json](../../campaign/batch14/376359531/historical/gaia.json)
- [measurements.json](../../campaign/batch14/376359531/measurements.json)
- [phase-review.png](../../campaign/batch14/376359531/phase-review.png)
- [raw-events.png](../../campaign/batch14/376359531/raw-events.png)
- [raw-windows.csv](../../campaign/batch14/376359531/raw-windows.csv)
- [secondary-windows.csv](../../campaign/batch14/376359531/secondary-windows.csv)

[Batch audits and scripts](../../campaign/batch14/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
