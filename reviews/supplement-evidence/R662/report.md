# TIC 11547648: CONFIRMED

Full bounded physical review: COMPLETE. Six repeated primary eclipses plus unequal secondary at phase0.500; no capable Gaia neighbor within60arcsec.

Raw QLP SAP_FLUX representative events and full-sector P/2P morphology were visually inspected. Quality-zero finite positive samples only; predictions guide windows and are never timings. 6 identifiable free-center timings define P=7.410395695858 +/- 0.000021364647d, reference BTJD=1849.517961025 +/- 0.003708065d. Epoch error meaning: Conservative linear timing-fit covariance under the stated cadence floor and scatter inflation; excludes uncalibrated shape and baseline systematics. Epoch kind: Deeper primary established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced chi square=0.09757598052374179; zero degrees of freedom is null. All errors retain their named meanings; no calibrated coverage is claimed. Selected same-kind recurring eclipse family; parity and P/2 coverage checked.

Depth=94.677778ppt is the median realized central trapezoid loss d*min(1,w/(2*k)); extrapolated amplitude and ingress remain separately in [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/11547648/measurements.json). Measured secondary phase 0.50001214, formal phase error 0.00011205012, realized depth 29.74132ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Secondary raw pooled windows, actual sectors/cycles and fitted phase are retained in [secondary-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/11547648/secondary-windows.csv) and [../secondary-phases.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/secondary-phases.json). No exhaustive blind alias search asserted. [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/alias-audit.json) and [../half-period-coverage.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/half-period-coverage.json) retain recurrence/parity and sampled opposite-phase evidence. Flagged coverage is never a clean null.

Fresh TESScut difference image sector20 stacks3 core/bilateral-sideband events. Target pixel=[7.379420324082043, 7.521193501031151], deficit=[7.581646557330426, 7.625706007137953]; descriptive offset=0.22764pixel, field PSF residual=0.40547. No arbitrary centroid cut or calibrated localization error is imposed. Every capable neighbor below was inspected at its actual projected pixels; close overlapping neighbors retain probable ownership. Every capable neighbor is assessed above and below; close overlapping cases retain unresolved attribution. All Gaia neighbors are retained in pixel JSON.

| Source | Separation arcsec | G | Required intrinsic loss proxy | Pixel coordinate | Diluted pixel loss |
|---|---:|---:|---:|---|---:|
| None | | | | | |

G-band pairwise brightness screen assumes approximate passband/aperture response; intrinsic required eclipse cannot be directly compared with diluted pixel loss. Unresolved unlisted companions are not excluded.

Alternative reduction: independently extracted background-subtracted TESScut1x1/3x3/5x5 depths=85.77257/86.04353/81.48312ppt; QLP median=94.67778ppt. Pixel sector20 shares the same TESS photons with retained QLP and checks extraction robustness. Independent processing is not an independent instrument. Different apertures respond differently to dilution/background.

Gaia source1004377178754043904: period=7.410293063+/-0.000985351d; e=0.0077322; omega=234.0733430deg; periastron BTJD=392.63288680. Closest conjunction offset=0.0122159d (0.0016485phase), source-specific full-covariance linear error=0.1612434d. Correlation order P,gamma,K,e,omega,Tp with subindices0,3,4,5. Linear propagation is descriptive, not a Gaussian veto or ownership proof. Both conjunctions retained in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/gaia-geometry.json). Mass function=0.09674742solar, assumed M1=1, minimum M2=0.637871; approximate central duration=7.3952h versus observed=4.8578h. TIC radius/main-sequence companion scaling, edge-on conjunction and stellar evolution are assumptions; this is a plausibility check, not a fitted physical solution.

| Sector | Same-kind cycle | Measured BTJD | Formal center error d | Conservative input error d | Realized depth ppt |
|---|---:|---:|---:|---:|---:|
| 20 | 0 | 1849.523376562 | 0.000287779272 | 0.0104165117 | 85.98434 |
| 20 | 2 | 1864.338296631 | 0.000391903483 | 0.0104165117 | 94.54878 |
| 60 | 148 | 2946.256564641 | 0.000308110837 | 0.0011573909 | 94.80677 |
| 60 | 150 | 2961.077005784 | 0.000329405784 | 0.0011573909 | 96.68156 |
| 73 | 195 | 3294.545365419 | 0.000366988028 | 0.00115742205 | 93.54370 |
| 73 | 197 | 3309.365877176 | 0.000317593186 | 0.00115742205 | 99.84711 |

Catalogue novelty is separate from this physical verdict. Shared coverage matrix and source identity checks are authoritative for catalogue recovery; period agreement alone cannot establish attribution.


Stable review key: R662.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/11547648/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/11547648/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/11547648/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/11547648/fresh-pixels/run.log)
- [historical/diff_s20.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/11547648/historical/diff_s20.json)
- [historical/diff_s20.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/11547648/historical/diff_s20.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/11547648/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/11547648/measurements.json)
- [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/11547648/phase-review.png)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/11547648/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/11547648/raw-windows.csv)
- [secondary-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/11547648/secondary-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch13/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
