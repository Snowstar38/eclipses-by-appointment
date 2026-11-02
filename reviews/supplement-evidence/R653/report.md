# TIC 376539517: CONFIRMED

Full bounded physical review: COMPLETE. Eleven repeated primary eclipses plus observed unequal secondary; substantial sector normalization differences do not remove the eclipse. No capable neighbor within60arcsec.

Raw QLP SAP_FLUX representative events and full-sector P/2P morphology were visually inspected. Quality-zero finite positive samples only; predictions guide windows and are never timings. 11 identifiable free-center timings define P=5.109546881245 +/- 0.000008596683d, reference BTJD=1819.713329927 +/- 0.002789204d. Epoch error meaning: Conservative linear timing-fit covariance under the stated cadence floor and scatter inflation; excludes uncalibrated shape and baseline systematics. Epoch kind: Deeper primary established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced chi square=0.44049179083476947; zero degrees of freedom is null. All errors retain their named meanings; no calibrated coverage is claimed. Selected same-kind recurring eclipse family; parity and P/2 coverage checked.

Depth=73.102931ppt is the median realized central trapezoid loss d*min(1,w/(2*k)); extrapolated amplitude and ingress remain separately in [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/376539517/measurements.json). Measured secondary phase 0.48186639, formal phase error 0.00020141761, realized depth 19.15961ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Secondary raw pooled windows, actual sectors/cycles and fitted phase are retained in [secondary-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/376539517/secondary-windows.csv) and [../secondary-phases.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/secondary-phases.json). No exhaustive blind alias search asserted. [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/alias-audit.json) and [../half-period-coverage.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/half-period-coverage.json) retain recurrence/parity and sampled opposite-phase evidence. Flagged coverage is never a clean null.

Fresh TESScut difference image sector26 stacks5 core/bilateral-sideband events. Target pixel=[7.205273409649651, 7.163492880968329], deficit=[7.138102923090409, 7.246464861133381]; descriptive offset=0.10675pixel, field PSF residual=0.33815. No arbitrary centroid cut or calibrated localization error is imposed. Every capable neighbor below was inspected at its actual projected pixels; close overlapping neighbors retain probable ownership. Other capable sources are displaced from compact deficit core but crowding limits localization. All Gaia neighbors are retained in pixel JSON.

| Source | Separation arcsec | G | Required intrinsic loss proxy | Pixel coordinate | Diluted pixel loss |
|---|---:|---:|---:|---|---:|
| None | | | | | |

G-band pairwise brightness screen assumes approximate passband/aperture response; intrinsic required eclipse cannot be directly compared with diluted pixel loss. Unresolved unlisted companions are not excluded.

Alternative reduction: independently extracted background-subtracted TESScut1x1/3x3/5x5 depths=72.95821/73.51253/67.73488ppt; QLP median=73.10293ppt. Pixel sector26 is a distinct observing occasion on the same TESS instrument; no same-sector QLP comparison claimed. Independent processing is not an independent instrument. Different apertures respond differently to dilution/background.

Gaia source503038050157132928: period=5.108145924+/-0.000724087d; e=0.1841026; omega=168.6275935deg; periastron BTJD=390.13818497. Closest conjunction offset=0.1258294d (0.0246331phase), source-specific full-covariance linear error=0.1776026d. Correlation order P,gamma,K,e,omega,Tp with subindices0,3,4,5. Linear propagation is descriptive, not a Gaussian veto or ownership proof. Both conjunctions retained in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/gaia-geometry.json). Mass function=0.04695988solar, assumed M1=1.1, minimum M2=0.491866; approximate central duration=7.3448h versus observed=7.1793h. TIC radius/main-sequence companion scaling, edge-on conjunction and stellar evolution are assumptions; this is a plausibility check, not a fitted physical solution.

| Sector | Same-kind cycle | Measured BTJD | Formal center error d | Conservative input error d | Realized depth ppt |
|---|---:|---:|---:|---:|---:|
| 19 | 0 | 1819.713651287 | 0.000478078568 | 0.0104167832 | 73.33910 |
| 19 | 1 | 1824.822082273 | 0.000339148736 | 0.0104167832 | 73.10293 |
| 19 | 3 | 1835.042522355 | 0.000395136086 | 0.0104167832 | 73.03915 |
| 19 | 4 | 1840.151754657 | 0.000704202731 | 0.0104167832 | 72.45720 |
| 53 | 181 | 2744.537262535 | 0.00254763379 | 0.00347223585 | 75.81973 |
| 53 | 182 | 2749.647982243 | 0.000795887432 | 0.00347223585 | 75.18473 |
| 53 | 183 | 2754.760985111 | 0.000508438675 | 0.00347223585 | 78.28945 |
| 53 | 184 | 2759.872174616 | 0.00106153697 | 0.00347223585 | 74.08675 |
| 53 | 185 | 2764.983689300 | 0.00102988611 | 0.00347223585 | 70.74449 |
| 86 | 357 | 3643.821660490 | 0.000465494754 | 0.00115742984 | 71.05484 |
| 86 | 358 | 3648.931010241 | 0.000417157438 | 0.00115742984 | 70.23268 |

Catalogue novelty is separate from this physical verdict. Shared coverage matrix and source identity checks are authoritative for catalogue recovery; period agreement alone cannot establish attribution.


Stable review key: R653.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/376539517/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/376539517/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/376539517/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/376539517/fresh-pixels/run.log)
- [historical/diff_s26.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/376539517/historical/diff_s26.json)
- [historical/diff_s26.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/376539517/historical/diff_s26.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/376539517/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/376539517/measurements.json)
- [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/376539517/phase-review.png)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/376539517/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/376539517/raw-windows.csv)
- [secondary-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/376539517/secondary-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
