# TIC 229563422: CONFIRMED

Full bounded physical review: COMPLETE. Five repeated primary eclipses and observed secondary-like dip near0.568 in sectors24/78. Sloped and offset sector baselines limit pooled secondary depth and phase reliability; formal errors are not total uncertainties. Capable39.52arcsec source is displaced from compact target deficit.

Raw QLP SAP_FLUX representative events and full-sector P/2P morphology were visually inspected. Quality-zero finite positive samples only; predictions guide windows and are never timings. 5 identifiable free-center timings define P=11.507252708231 +/- 0.000035573313d, reference BTJD=1966.353158239 +/- 0.004191194d. Epoch error meaning: Conservative linear timing-fit covariance under the stated cadence floor and scatter inflation; excludes uncalibrated shape and baseline systematics. Epoch kind: Deeper primary established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced chi square=0.1458482783872733; zero degrees of freedom is null. All errors retain their named meanings; no calibrated coverage is claimed. Selected same-kind recurring eclipse family; parity and P/2 coverage checked.

Depth=75.288250ppt is the median realized central trapezoid loss d*min(1,w/(2*k)); extrapolated amplitude and ingress remain separately in [measurements.json](../../campaign/batch13/229563422/measurements.json). Measured secondary phase 0.56857435, formal phase error 0.00027870082, realized depth 10.26889ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Secondary raw pooled windows, actual sectors/cycles and fitted phase are retained in [secondary-windows.csv](../../campaign/batch13/229563422/secondary-windows.csv) and [../secondary-phases.json](../../campaign/batch13/secondary-phases.json). No exhaustive blind alias search asserted. [../alias-audit.json](../../campaign/batch13/alias-audit.json) and [../half-period-coverage.json](../../campaign/batch13/half-period-coverage.json) retain recurrence/parity and sampled opposite-phase evidence. Flagged coverage is never a clean null.

Fresh TESScut difference image sector24 stacks2 core/bilateral-sideband events. Target pixel=[7.076658914874642, 7.892752549107424], deficit=[6.961479928460955, 8.068638828024678]; descriptive offset=0.21024pixel, field PSF residual=0.13566. No arbitrary centroid cut or calibrated localization error is imposed. Every capable neighbor below was inspected at its actual projected pixels; close overlapping neighbors retain probable ownership. Every capable neighbor is assessed above and below; close overlapping cases retain unresolved attribution. All Gaia neighbors are retained in pixel JSON.

| Source | Separation arcsec | G | Required intrinsic loss proxy | Pixel coordinate | Diluted pixel loss |
|---|---:|---:|---:|---|---:|
| 1203339747737969792 | 39.51630949715323 | 15.157707 | 0.7961845617175048 | [5.863792630171345, 9.567085211390598] | 0.035540402889291015 |

G-band pairwise brightness screen assumes approximate passband/aperture response; intrinsic required eclipse cannot be directly compared with diluted pixel loss. Unresolved unlisted companions are not excluded.

Alternative reduction: independently extracted background-subtracted TESScut1x1/3x3/5x5 depths=73.65179/70.86155/67.13093ppt; QLP median=75.28825ppt. Pixel sector24 shares the same TESS photons with retained QLP and checks extraction robustness. Independent processing is not an independent instrument. Different apertures respond differently to dilution/background.

Gaia source1203338996120545024: period=11.506971982+/-0.002851733d; e=0.1680296; omega=333.6707855deg; periastron BTJD=386.47260926. Closest conjunction offset=0.2888550d (0.0251026phase), source-specific full-covariance linear error=0.4890973d. Correlation order P,gamma,K,e,omega,Tp with subindices0,3,4,5. Linear propagation is descriptive, not a Gaussian veto or ownership proof. Both conjunctions retained in [../gaia-geometry.json](../../campaign/batch13/gaia-geometry.json). Mass function=0.07886812solar, assumed M1=1.0, minimum M2=0.582323; approximate central duration=10.9006h versus observed=9.5449h. TIC radius/main-sequence companion scaling, edge-on conjunction and stellar evolution are assumptions; this is a plausibility check, not a fitted physical solution.

| Sector | Same-kind cycle | Measured BTJD | Formal center error d | Conservative input error d | Realized depth ppt |
|---|---:|---:|---:|---:|---:|
| 24 | 0 | 1966.354463597 | 0.00190609079 | 0.0104167912 | 74.28968 |
| 24 | 1 | 1977.863500453 | 0.000689240843 | 0.0104167912 | 75.91111 |
| 51 | 64 | 2702.815521766 | 0.00204591859 | 0.00347229077 | 75.28825 |
| 51 | 65 | 2714.325436095 | 0.00155291585 | 0.00347229077 | 73.86239 |
| 78 | 128 | 3439.281557074 | 0.000672613204 | 0.00115741024 | 75.75584 |

Catalogue novelty is separate from this physical verdict. Shared coverage matrix and source identity checks are authoritative for catalogue recovery; period agreement alone cannot establish attribution.


Stable review key: R668.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch13/229563422/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch13/229563422/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch13/229563422/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch13/229563422/fresh-pixels/run.log)
- [historical/diff_s24.json](../../campaign/batch13/229563422/historical/diff_s24.json)
- [historical/diff_s24.png](../../campaign/batch13/229563422/historical/diff_s24.png)
- [historical/gaia.json](../../campaign/batch13/229563422/historical/gaia.json)
- [measurements.json](../../campaign/batch13/229563422/measurements.json)
- [phase-review.png](../../campaign/batch13/229563422/phase-review.png)
- [raw-events.png](../../campaign/batch13/229563422/raw-events.png)
- [raw-windows.csv](../../campaign/batch13/229563422/raw-windows.csv)
- [secondary-windows.csv](../../campaign/batch13/229563422/secondary-windows.csv)

[Batch audits and scripts](../../campaign/batch13/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
