# TIC 440522293: CONFIRMED

Full bounded physical review: COMPLETE. Seven repeated narrow eclipses despite large changing raw baselines. No secure secondary. Three capable sources at43.44/49.59/59.27arcsec are separated from compact target deficit.

Raw QLP SAP_FLUX representative events and full-sector P/2P morphology were visually inspected. Quality-zero finite positive samples only; predictions guide windows and are never timings. 7 identifiable free-center timings define P=6.260865037153 +/- 0.000022364799d, reference BTJD=1818.068911290 +/- 0.005238708d. Epoch error meaning: Conservative linear timing-fit covariance under the stated cadence floor and scatter inflation; excludes uncalibrated shape and baseline systematics. Epoch kind: Selected repeating eclipse; deeper/secondary identity not established. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced chi square=0.13515330383939334; zero degrees of freedom is null. All errors retain their named meanings; no calibrated coverage is claimed. Selected same-kind recurring eclipse family; parity and P/2 coverage checked.

Depth=60.978017ppt is the median realized central trapezoid loss d*min(1,w/(2*k)); extrapolated amplitude and ingress remain separately in [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/440522293/measurements.json). No secure secondary; exploratory fit is not interpreted as an eclipse timing or counterpart. Secondary raw pooled windows, actual sectors/cycles and fitted phase are retained in [secondary-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/440522293/secondary-windows.csv) and [../secondary-phases.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/secondary-phases.json). No exhaustive blind alias search asserted. [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/alias-audit.json) and [../half-period-coverage.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/half-period-coverage.json) retain recurrence/parity and sampled opposite-phase evidence. Flagged coverage is never a clean null.

Fresh TESScut difference image sector19 stacks4 core/bilateral-sideband events. Target pixel=[7.195044463550808, 7.402943412853364], deficit=[7.198913632123789, 7.367517699540319]; descriptive offset=0.03564pixel, field PSF residual=0.98464. No arbitrary centroid cut or calibrated localization error is imposed. Every capable neighbor below was inspected at its actual projected pixels; close overlapping neighbors retain probable ownership. Other capable sources are displaced from compact deficit core but crowding limits localization. All Gaia neighbors are retained in pixel JSON.

| Source | Separation arcsec | G | Required intrinsic loss proxy | Pixel coordinate | Diluted pixel loss |
|---|---:|---:|---:|---|---:|
| 961189805124299008 | 43.44342671941483 | 14.686691 | 0.4558854409374505 | [5.8765626148871135, 9.090413312774503] | 0.007585100171623949 |
| 961189839484038016 | 49.59189785163533 | 14.989554 | 0.5829419539402513 | [7.479707724015075, 9.819287430193889] | 0.005153184123461533 |
| 961189942563249664 | 59.2652208795125 | 10.849086 | 0.07249803886405261 | [5.801015495039102, 4.8027185533476] | -7.655452858734913e-05 |

G-band pairwise brightness screen assumes approximate passband/aperture response; intrinsic required eclipse cannot be directly compared with diluted pixel loss. Unresolved unlisted companions are not excluded.

Alternative reduction: independently extracted background-subtracted TESScut1x1/3x3/5x5 depths=45.38131/26.46948/9.69180ppt; QLP median=60.97802ppt. Pixel sector19 shares the same TESS photons with retained QLP and checks extraction robustness. Independent processing is not an independent instrument. Different apertures respond differently to dilution/background.

Gaia source961189976922990464: period=6.261849300+/-0.000862596d; e=0.1238615; omega=35.5538898deg; periastron BTJD=389.77342650. Closest conjunction offset=-0.1630120d (-0.0260326phase), source-specific full-covariance linear error=0.1914077d. Correlation order P,gamma,K,e,omega,Tp with subindices0,3,4,5. Linear propagation is descriptive, not a Gaussian veto or ownership proof. Both conjunctions retained in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/gaia-geometry.json). Mass function=0.06229506solar, assumed M1=1.24, minimum M2=0.593938; approximate central duration=5.5105h versus observed=3.1485h. TIC radius/main-sequence companion scaling, edge-on conjunction and stellar evolution are assumptions; this is a plausibility check, not a fitted physical solution.

| Sector | Same-kind cycle | Measured BTJD | Formal center error d | Conservative input error d | Realized depth ppt |
|---|---:|---:|---:|---:|---:|
| 19 | 0 | 1818.070537803 | 0.00106662542 | 0.0104169085 | 57.84351 |
| 19 | 1 | 1824.330393498 | 0.000681847298 | 0.0104169085 | 57.84571 |
| 19 | 2 | 1830.588833811 | 0.00116932993 | 0.0104169085 | 56.74498 |
| 19 | 3 | 1836.851599195 | 0.000793332926 | 0.0104169085 | 60.97802 |
| 73 | 235 | 3289.371359548 | 0.00213364001 | 0.00213364001 | 64.42739 |
| 73 | 236 | 3295.632635005 | 0.000883029663 | 0.00115741697 | 63.83076 |
| 73 | 238 | 3308.155454505 | 0.000943755438 | 0.00115741697 | 63.80221 |

Catalogue novelty is separate from this physical verdict. Shared coverage matrix and source identity checks are authoritative for catalogue recovery; period agreement alone cannot establish attribution.


Stable review key: R651.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/440522293/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/440522293/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/440522293/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/440522293/fresh-pixels/run.log)
- [historical/diff_s19.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/440522293/historical/diff_s19.json)
- [historical/diff_s19.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/440522293/historical/diff_s19.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/440522293/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/440522293/measurements.json)
- [phase-review.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/440522293/phase-review.png)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/440522293/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/440522293/raw-windows.csv)
- [secondary-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/440522293/secondary-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch12/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
