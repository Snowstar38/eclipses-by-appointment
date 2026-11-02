# TIC 133392449: PROBABLE

Full bounded physical review: COMPLETE. Six repeated broad deep primary eclipses and a secondary near phase0.604, most cleanly visible in sector12; large sector baselines limit secondary depth accuracy. Inner capable16.69/18.70arcsec sources share the target footprint: ownership remains unresolved. Outer43.15/49.36arcsec sources are displaced.

Raw QLP SAP_FLUX representative events and full-sector P/2P morphology were visually inspected. Quality-zero finite positive samples only; predictions guide windows and are never timings. 6 identifiable free-center timings define P=18.021654636300 +/- 0.000210656372d, reference BTJD=1631.745566269 +/- 0.028701204d. Epoch error meaning: Conservative linear timing-fit covariance under the stated cadence floor and scatter inflation; excludes uncalibrated shape and baseline systematics. Epoch kind: Deeper primary established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced chi square=15.848209438029008; zero degrees of freedom is null. All errors retain their named meanings; no calibrated coverage is claimed. Selected same-kind recurring eclipse family; parity and P/2 coverage checked.

Depth=151.294349ppt is the median realized central trapezoid loss d*min(1,w/(2*k)); extrapolated amplitude and ingress remain separately in [measurements.json](../../campaign/batch13/133392449/measurements.json). Measured secondary phase 0.60406219, formal phase error 0.00019665178, realized depth 93.22618ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Secondary raw pooled windows, actual sectors/cycles and fitted phase are retained in [secondary-windows.csv](../../campaign/batch13/133392449/secondary-windows.csv) and [../secondary-phases.json](../../campaign/batch13/secondary-phases.json). No exhaustive blind alias search asserted. [../alias-audit.json](../../campaign/batch13/alias-audit.json) and [../half-period-coverage.json](../../campaign/batch13/half-period-coverage.json) retain recurrence/parity and sampled opposite-phase evidence. Flagged coverage is never a clean null.

Fresh TESScut difference image sector12 stacks2 core/bilateral-sideband events. Target pixel=[7.74163513205823, 7.260115530009859], deficit=[7.8658115741010155, 7.29564787217059]; descriptive offset=0.12916pixel, field PSF residual=0.69050. No arbitrary centroid cut or calibrated localization error is imposed. Every capable neighbor below was inspected at its actual projected pixels; close overlapping neighbors retain probable ownership. Every capable neighbor is assessed above and below; close overlapping cases retain unresolved attribution. All Gaia neighbors are retained in pixel JSON.

| Source | Separation arcsec | G | Required intrinsic loss proxy | Pixel coordinate | Diluted pixel loss |
|---|---:|---:|---:|---|---:|
| 5888148722604706304 | 16.68707135704292 | 13.586701 | 0.5034549026825209 | [7.085597591154146, 7.8227538159093175] | 0.020918346998512995 |
| 5888148722604706432 | 18.696270339135605 | 11.349322 | 0.19614710257740012 | [6.810385805314335, 7.4795628653223964] | 0.03615427770127481 |
| 5888143053247419136 | 43.14941916259565 | 13.891616 | 0.6176386866712941 | [9.92691803964027, 7.130815210335037] | 0.012606213008692102 |
| 5888148756964450688 | 49.356004685888024 | 13.705976 | 0.5443469802802722 | [7.728820979670219, 4.785614338550957] | 0.005110266236690588 |

G-band pairwise brightness screen assumes approximate passband/aperture response; intrinsic required eclipse cannot be directly compared with diluted pixel loss. Unresolved unlisted companions are not excluded.

Alternative reduction: independently extracted background-subtracted TESScut1x1/3x3/5x5 depths=80.60458/47.54593/32.97453ppt; QLP median=151.29435ppt. Pixel sector12 shares the same TESS photons with retained QLP and checks extraction robustness. Independent processing is not an independent instrument. Different apertures respond differently to dilution/background.

Gaia source5888148722604708352: period=18.016804588+/-0.008917450d; e=0.2068520; omega=208.8248923deg; periastron BTJD=386.24612181. Closest conjunction offset=0.2394776d (0.0132919phase), source-specific full-covariance linear error=0.7160614d. Correlation order P,gamma,K,e,omega,Tp with subindices0,3,4,5. Linear propagation is descriptive, not a Gaussian veto or ownership proof. Both conjunctions retained in [../gaia-geometry.json](../../campaign/batch13/gaia-geometry.json). Mass function=0.2273762solar, assumed M1=1.0, minimum M2=0.953945; approximate central duration=19.4475h versus observed=18.5673h. TIC radius/main-sequence companion scaling, edge-on conjunction and stellar evolution are assumptions; this is a plausibility check, not a fitted physical solution.

| Sector | Same-kind cycle | Measured BTJD | Formal center error d | Conservative input error d | Realized depth ppt |
|---|---:|---:|---:|---:|---:|
| 12 | 0 | 1631.734854338 | 0.00182644157 | 0.0104164414 | 153.99416 |
| 12 | 1 | 1649.754323936 | 0.000998046982 | 0.0104164414 | 148.16914 |
| 99 | 134 | 4046.654240944 | 0.000992455644 | 0.00115748098 | 148.59454 |
| 99 | 135 | 4064.668325979 | 0.00142490495 | 0.00142490495 | 146.88252 |
| 103 | 140 | 4154.771926493 | 0.000618720924 | 0.00115740685 | 159.29043 |
| 103 | 141 | 4172.793812212 | 0.00264886574 | 0.00264886574 | 162.09690 |

Catalogue novelty is separate from this physical verdict. Shared coverage matrix and source identity checks are authoritative for catalogue recovery; period agreement alone cannot establish attribution.


Stable review key: R660.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch13/133392449/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch13/133392449/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch13/133392449/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch13/133392449/fresh-pixels/run.log)
- [historical/diff_s12.json](../../campaign/batch13/133392449/historical/diff_s12.json)
- [historical/diff_s12.png](../../campaign/batch13/133392449/historical/diff_s12.png)
- [historical/gaia.json](../../campaign/batch13/133392449/historical/gaia.json)
- [measurements.json](../../campaign/batch13/133392449/measurements.json)
- [phase-review.png](../../campaign/batch13/133392449/phase-review.png)
- [raw-events.png](../../campaign/batch13/133392449/raw-events.png)
- [raw-windows.csv](../../campaign/batch13/133392449/raw-windows.csv)
- [secondary-windows.csv](../../campaign/batch13/133392449/secondary-windows.csv)

[Batch audits and scripts](../../campaign/batch13/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
