# TIC 48879301: CONFIRMED

Full bounded physical review: COMPLETE. Ten repeated narrow primary eclipses and unequal secondary; no capable neighbor within60arcsec.

Raw QLP SAP_FLUX representative events and full-sector P/2P morphology were visually inspected. Quality-zero finite positive samples only; predictions guide windows and are never timings. 10 identifiable free-center timings define P=7.907623484062 +/- 0.000014706680d, reference BTJD=1551.541058787 +/- 0.004370981d. Epoch error meaning: Conservative linear timing-fit covariance under the stated cadence floor and scatter inflation; excludes uncalibrated shape and baseline systematics. Epoch kind: Deeper primary established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced chi square=0.22443573518765553; zero degrees of freedom is null. All errors retain their named meanings; no calibrated coverage is claimed. Selected same-kind recurring eclipse family; parity and P/2 coverage checked.

Depth=51.991549ppt is the median realized central trapezoid loss d*min(1,w/(2*k)); extrapolated amplitude and ingress remain separately in [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/48879301/measurements.json). Measured secondary phase 0.48947999, formal phase error 7.7574893e-05, realized depth 21.03836ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Secondary raw pooled windows, actual sectors/cycles and fitted phase are retained in [secondary-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/48879301/secondary-windows.csv) and [../secondary-phases.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/secondary-phases.json). No exhaustive blind alias search asserted. [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/alias-audit.json) and [../half-period-coverage.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/half-period-coverage.json) retain recurrence/parity and sampled opposite-phase evidence. Flagged coverage is never a clean null.

Fresh TESScut difference image sector90 stacks4 core/bilateral-sideband events. Target pixel=[7.70322522876198, 7.2910002827836315], deficit=[7.819900956250759, 7.3099259957680305]; descriptive offset=0.11820pixel, field PSF residual=0.49719. No arbitrary centroid cut or calibrated localization error is imposed. Every capable neighbor below was inspected at its actual projected pixels; close overlapping neighbors retain probable ownership. Other capable sources are displaced from compact deficit core but crowding limits localization. All Gaia neighbors are retained in pixel JSON.

| Source | Separation arcsec | G | Required intrinsic loss proxy | Pixel coordinate | Diluted pixel loss |
|---|---:|---:|---:|---|---:|
| None | | | | | |

G-band pairwise brightness screen assumes approximate passband/aperture response; intrinsic required eclipse cannot be directly compared with diluted pixel loss. Unresolved unlisted companions are not excluded.

Alternative reduction: independently extracted background-subtracted TESScut1x1/3x3/5x5 depths=48.84132/48.17366/45.73593ppt; QLP median=51.99155ppt. Pixel sector90 shares the same TESS photons with retained QLP and checks extraction robustness. Independent processing is not an independent instrument. Different apertures respond differently to dilution/background.

Gaia source5449918297210471680: period=7.906795576+/-0.001631973d; e=0.0678617; omega=274.4254178deg; periastron BTJD=385.28528032. Closest conjunction offset=0.1145074d (0.0144821phase), source-specific full-covariance linear error=0.3026588d. Correlation order P,gamma,K,e,omega,Tp with subindices0,3,4,5. Linear propagation is descriptive, not a Gaussian veto or ownership proof. Both conjunctions retained in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/gaia-geometry.json). Mass function=0.08287888solar, assumed M1=1.19, minimum M2=0.656129; approximate central duration=6.0924h versus observed=3.6149h. TIC radius/main-sequence companion scaling, edge-on conjunction and stellar evolution are assumptions; this is a plausibility check, not a fitted physical solution.

| Sector | Same-kind cycle | Measured BTJD | Formal center error d | Conservative input error d | Realized depth ppt |
|---|---:|---:|---:|---:|---:|
| 9 | 0 | 1551.538674240 | 0.000341772729 | 0.0104167647 | 46.68939 |
| 9 | 1 | 1559.445941015 | 0.000266195098 | 0.0104167647 | 45.64270 |
| 9 | 2 | 1567.352194049 | 0.000299355157 | 0.0104167647 | 47.83335 |
| 90 | 278 | 3749.861423151 | 0.000504221854 | 0.00115739967 | 54.14251 |
| 90 | 279 | 3757.768612656 | 0.00061005499 | 0.00115739967 | 52.84572 |
| 90 | 280 | 3765.675403923 | 0.000523942663 | 0.00115739967 | 53.63835 |
| 90 | 281 | 3773.582665958 | 0.000837821149 | 0.00115739967 | 53.33722 |
| 100 | 320 | 4081.980196125 | 0.000341766601 | 0.00115740685 | 50.47596 |
| 100 | 321 | 4089.888027434 | 0.000432011612 | 0.00115740685 | 52.38482 |
| 100 | 322 | 4097.795666630 | 0.000424969085 | 0.00115740685 | 51.59828 |

Catalogue novelty is separate from this physical verdict. Shared coverage matrix and source identity checks are authoritative for catalogue recovery; period agreement alone cannot establish attribution.


Stable review key: R656.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/48879301/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/48879301/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/48879301/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/48879301/fresh-pixels/run.log)
- [historical/diff_s90.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/48879301/historical/diff_s90.json)
- [historical/diff_s90.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/48879301/historical/diff_s90.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/48879301/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/48879301/measurements.json)
- [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/48879301/phase-review.png)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/48879301/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/48879301/raw-windows.csv)
- [secondary-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/48879301/secondary-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
