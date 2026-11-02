# TIC 59955223: PROBABLE

Full bounded physical review: COMPLETE. Nine repeated shallow narrow eclipses in raw SAP. Historical SAP-depth cache has no row; photometric search P branch explicitly seeds free-center fitting. No secure secondary. Capable24.43arcsec neighbor at1.1pixel separation overlaps target footprint; ownership remains unresolved. Other capable46.88/49.91arcsec sources are further displaced.

Raw QLP SAP_FLUX representative events and full-sector P/2P morphology were visually inspected. Quality-zero finite positive samples only; predictions guide windows and are never timings. 9 identifiable free-center timings define P=7.646605695993 +/- 0.000030343475d, reference BTJD=1469.134751039 +/- 0.006871504d. Epoch error meaning: Conservative linear timing-fit covariance under the stated cadence floor and scatter inflation; excludes uncalibrated shape and baseline systematics. Epoch kind: Selected repeating eclipse; deeper/secondary identity not established. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced chi square=6.500084427670953; zero degrees of freedom is null. All errors retain their named meanings; no calibrated coverage is claimed. Selected same-kind recurring eclipse family; parity and P/2 coverage checked.

Depth=8.828826ppt is the median realized central trapezoid loss d*min(1,w/(2*k)); extrapolated amplitude and ingress remain separately in [measurements.json](../../campaign/batch12/59955223/measurements.json). No secure secondary; exploratory fit is not interpreted as an eclipse timing or counterpart. Secondary raw pooled windows, actual sectors/cycles and fitted phase are retained in [secondary-windows.csv](../../campaign/batch12/59955223/secondary-windows.csv) and [../secondary-phases.json](../../campaign/batch12/secondary-phases.json). No exhaustive blind alias search asserted. [../alias-audit.json](../../campaign/batch12/alias-audit.json) and [../half-period-coverage.json](../../campaign/batch12/half-period-coverage.json) retain recurrence/parity and sampled opposite-phase evidence. Flagged coverage is never a clean null.

Fresh TESScut difference image sector33 stacks4 core/bilateral-sideband events. Target pixel=[7.258624113654173, 7.773432037253507], deficit=[7.112567829467887, 7.7605356510558465]; descriptive offset=0.14662pixel, field PSF residual=0.60868. No arbitrary centroid cut or calibrated localization error is imposed. Every capable neighbor below was inspected at its actual projected pixels; close overlapping neighbors retain probable ownership. Other capable sources are displaced from compact deficit core but crowding limits localization. All Gaia neighbors are retained in pixel JSON.

| Source | Separation arcsec | G | Required intrinsic loss proxy | Pixel coordinate | Diluted pixel loss |
|---|---:|---:|---:|---|---:|
| 2937944895339705472 | 24.43253064552264 | 16.004097 | 0.20045523859646372 | [7.880499028698017, 6.797597998695929] | 0.007576786488439782 |
| 2937944826620226304 | 46.87860422531916 | 16.306564 | 0.2620162727588868 | [9.381452561374967, 7.118574349820252] | 0.0018220279852657504 |
| 2937944929699437568 | 49.91162411423837 | 16.777998 | 0.3996839133338027 | [8.803648167155401, 9.575826083636732] | 0.004896318556257513 |

G-band pairwise brightness screen assumes approximate passband/aperture response; intrinsic required eclipse cannot be directly compared with diluted pixel loss. Unresolved unlisted companions are not excluded.

Alternative reduction: independently extracted background-subtracted TESScut1x1/3x3/5x5 depths=8.48086/8.91036/8.31172ppt; QLP median=8.82883ppt. Pixel sector33 shares the same TESS photons with retained QLP and checks extraction robustness. Independent processing is not an independent instrument. Different apertures respond differently to dilution/background.

Gaia source2937944895339704320: period=7.649254403+/-0.001468547d; e=0.1513959; omega=135.7670018deg; periastron BTJD=391.69996046. Closest conjunction offset=-0.3817110d (-0.0499017phase), source-specific full-covariance linear error=0.2409343d. Correlation order P,gamma,K,e,omega,Tp with subindices0,3,4,5. Linear propagation is descriptive, not a Gaussian veto or ownership proof. Both conjunctions retained in [../gaia-geometry.json](../../campaign/batch12/gaia-geometry.json). Mass function=0.004520785solar, assumed M1=1.06, minimum M2=0.192085; approximate central duration=8.0151h versus observed=7.6534h. TIC radius/main-sequence companion scaling, edge-on conjunction and stellar evolution are assumptions; this is a plausibility check, not a fitted physical solution.

| Sector | Same-kind cycle | Measured BTJD | Formal center error d | Conservative input error d | Realized depth ppt |
|---|---:|---:|---:|---:|---:|
| 6 | 0 | 1469.127132794 | 0.00701917676 | 0.0104166767 | 9.52371 |
| 6 | 2 | 1484.489387392 | 0.00229461833 | 0.0104166767 | 7.71483 |
| 33 | 96 | 2203.204530452 | 0.0030736072 | 0.00347220546 | 9.67139 |
| 33 | 97 | 2210.853399480 | 0.00201740533 | 0.00347220546 | 8.82883 |
| 33 | 98 | 2218.503457255 | 0.00297708524 | 0.00347220546 | 8.71729 |
| 33 | 99 | 2226.141478921 | 0.00475569889 | 0.00475569889 | 9.03537 |
| 87 | 288 | 3671.365733022 | 0.00376214527 | 0.00376214527 | 8.46615 |
| 87 | 289 | 3679.001662313 | 0.00276466619 | 0.00276466619 | 8.91800 |
| 87 | 290 | 3686.650037204 | 0.00220590347 | 0.00220590347 | 8.23910 |

Catalogue novelty is separate from this physical verdict. Shared coverage matrix and source identity checks are authoritative for catalogue recovery; period agreement alone cannot establish attribution.


Stable review key: R657.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch12/59955223/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch12/59955223/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch12/59955223/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch12/59955223/fresh-pixels/run.log)
- [historical/diff_s33.json](../../campaign/batch12/59955223/historical/diff_s33.json)
- [historical/diff_s33.png](../../campaign/batch12/59955223/historical/diff_s33.png)
- [historical/gaia.json](../../campaign/batch12/59955223/historical/gaia.json)
- [measurements.json](../../campaign/batch12/59955223/measurements.json)
- [phase-review.png](../../campaign/batch12/59955223/phase-review.png)
- [raw-events.png](../../campaign/batch12/59955223/raw-events.png)
- [raw-windows.csv](../../campaign/batch12/59955223/raw-windows.csv)
- [secondary-windows.csv](../../campaign/batch12/59955223/secondary-windows.csv)

[Batch audits and scripts](../../campaign/batch12/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
