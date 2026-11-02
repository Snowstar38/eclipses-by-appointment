# TIC 116849606: CONFIRMED

Full bounded physical review: COMPLETE. Five deep repeated primary eclipses and unequal secondary. Capable36.35arcsec neighbor lies away from the compact deficit core.

Raw QLP SAP_FLUX representative events and full-sector P/2P morphology were visually inspected. Quality-zero finite positive samples only; predictions guide windows and are never timings. 5 identifiable free-center timings define P=12.440254466056 +/- 0.000023213922d, reference BTJD=1798.381352886 +/- 0.002566825d. Epoch error meaning: Conservative linear timing-fit covariance under the stated cadence floor and scatter inflation; excludes uncalibrated shape and baseline systematics. Epoch kind: Deeper primary established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced chi square=0.0012150626936853677; zero degrees of freedom is null. All errors retain their named meanings; no calibrated coverage is claimed. Selected same-kind recurring eclipse family; parity and P/2 coverage checked.

Depth=195.733208ppt is the median realized central trapezoid loss d*min(1,w/(2*k)); extrapolated amplitude and ingress remain separately in [measurements.json](../../campaign/batch10/116849606/measurements.json). Measured secondary phase 0.50777977, formal phase error 1.7891351e-05, realized depth 83.54695ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Secondary raw pooled windows, actual sectors/cycles and fitted phase are retained in [secondary-windows.csv](../../campaign/batch10/116849606/secondary-windows.csv) and [../secondary-phases.json](../../campaign/batch10/secondary-phases.json). No exhaustive blind alias search asserted. [../alias-audit.json](../../campaign/batch10/alias-audit.json) and [../half-period-coverage.json](../../campaign/batch10/half-period-coverage.json) retain recurrence/parity and sampled opposite-phase evidence. Flagged coverage is never a clean null.

Fresh TESScut difference image sector18 stacks2 core/bilateral-sideband events. Target pixel=[7.746564539683181, 7.159683402689835], deficit=[7.788126832769522, 7.198591681575559]; descriptive offset=0.05693pixel, field PSF residual=0.79657. No arbitrary centroid cut or calibrated localization error is imposed. Every capable neighbor below was inspected at its actual projected pixels; close overlapping neighbors retain probable ownership. Other capable sources are displaced from compact deficit core but crowding limits localization. All Gaia neighbors are retained in pixel JSON.

| Source | Separation arcsec | G | Required intrinsic loss proxy | Pixel coordinate | Diluted pixel loss |
|---|---:|---:|---:|---|---:|
| 435960659681725568 | 36.35277088311106 | 13.198205 | 0.5432508961537987 | [9.119610210435871, 6.01355863331133] | 0.019134450360127217 |

G-band pairwise brightness screen assumes approximate passband/aperture response; intrinsic required eclipse cannot be directly compared with diluted pixel loss. Unresolved unlisted companions are not excluded.

Alternative reduction: independently extracted background-subtracted TESScut1x1/3x3/5x5 depths=144.97444/121.69230/94.56094ppt; QLP median=195.73321ppt. Pixel sector18 shares the same TESS photons with retained QLP and checks extraction robustness. Independent processing is not an independent instrument. Different apertures respond differently to dilution/background.

Gaia source435960453523296000: period=12.442154531+/-0.002444407d; e=0.0350116; omega=308.9095390deg; periastron BTJD=387.72366373. Closest conjunction offset=-0.0931785d (-0.0074889phase), source-specific full-covariance linear error=0.3044548d. Correlation order P,gamma,K,e,omega,Tp with subindices0,3,4,5. Linear propagation is descriptive, not a Gaussian veto or ownership proof. Both conjunctions retained in [../gaia-geometry.json](../../campaign/batch10/gaia-geometry.json). Mass function=0.1492656solar, assumed M1=1.17, minimum M2=0.846749; approximate central duration=9.0052h versus observed=6.2537h. TIC radius/main-sequence companion scaling, edge-on conjunction and stellar evolution are assumptions; this is a plausibility check, not a fitted physical solution.

| Sector | Same-kind cycle | Measured BTJD | Formal center error d | Conservative input error d | Realized depth ppt |
|---|---:|---:|---:|---:|---:|
| 18 | 0 | 1798.381030875 | 0.000251335493 | 0.0104167496 | 188.36613 |
| 18 | 1 | 1810.821212280 | 0.000221772865 | 0.0104167496 | 197.85153 |
| 58 | 88 | 2893.123732608 | 0.00022014339 | 0.00115741827 | 195.73321 |
| 58 | 89 | 2905.564036479 | 0.000226294859 | 0.00115741827 | 197.42663 |
| 85 | 146 | 3614.658490959 | 0.000237635103 | 0.00115743017 | 195.56832 |

Catalogue novelty is separate from this physical verdict. Shared coverage matrix and source identity checks are authoritative for catalogue recovery; period agreement alone cannot establish attribution.


Stable review key: R632.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch10/116849606/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch10/116849606/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch10/116849606/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch10/116849606/fresh-pixels/run.log)
- [historical/diff_s18.json](../../campaign/batch10/116849606/historical/diff_s18.json)
- [historical/diff_s18.png](../../campaign/batch10/116849606/historical/diff_s18.png)
- [historical/gaia.json](../../campaign/batch10/116849606/historical/gaia.json)
- [measurements.json](../../campaign/batch10/116849606/measurements.json)
- [phase-review.png](../../campaign/batch10/116849606/phase-review.png)
- [raw-events.png](../../campaign/batch10/116849606/raw-events.png)
- [raw-windows.csv](../../campaign/batch10/116849606/raw-windows.csv)
- [secondary-windows.csv](../../campaign/batch10/116849606/secondary-windows.csv)

[Batch audits and scripts](../../campaign/batch10/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
