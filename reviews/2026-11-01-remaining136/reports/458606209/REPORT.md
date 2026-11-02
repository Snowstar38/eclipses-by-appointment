# TIC 458606209: PROBABLE

Full bounded physical review: COMPLETE. Four repeated broad eclipses including consecutive sector63 cycles137/138; unequal observed secondary near0.444. Crowded field: capable20.03arcsec and25.27arcsec neighbors share target footprint, leaving attribution unresolved despite target-centered deficit. All seven capable neighbors inspected. Sector64 pixel events are a distinct occasion from selected QLP sectors10/63/99.

Raw QLP SAP_FLUX representative events and full-sector P/2P morphology were visually inspected. Quality-zero finite positive samples only; predictions guide windows and are never timings. 4 identifiable free-center timings define P=10.507616353469 +/- 0.000055223821d, reference BTJD=1592.428884738 +/- 0.011213982d. Epoch error meaning: Conservative linear timing-fit covariance under the stated cadence floor and scatter inflation; excludes uncalibrated shape and baseline systematics. Epoch kind: Deeper primary established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced chi square=8.204770542837087; zero degrees of freedom is null. All errors retain their named meanings; no calibrated coverage is claimed. Selected same-kind recurring eclipse family; parity and P/2 coverage checked.

Depth=42.918457ppt is the median realized central trapezoid loss d*min(1,w/(2*k)); extrapolated amplitude and ingress remain separately in [measurements.json](../../campaign/batch14/458606209/measurements.json). Measured secondary phase 0.44400184, formal phase error 8.2247796e-05, realized depth 31.38429ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Secondary raw pooled windows, actual sectors/cycles and fitted phase are retained in [secondary-windows.csv](../../campaign/batch14/458606209/secondary-windows.csv) and [../secondary-phases.json](../../campaign/batch14/secondary-phases.json). No exhaustive blind alias search asserted. [../alias-audit.json](../../campaign/batch14/alias-audit.json) and [../half-period-coverage.json](../../campaign/batch14/half-period-coverage.json) retain recurrence/parity and sampled opposite-phase evidence. Flagged coverage is never a clean null.

Fresh TESScut difference image sector64 stacks3 core/bilateral-sideband events. Target pixel=[7.416264869931146, 7.968078315482648], deficit=[7.2206932843191245, 8.052592505505219]; descriptive offset=0.21305pixel, field PSF residual=0.71034. No arbitrary centroid cut or calibrated localization error is imposed. Every capable neighbor below was inspected at its actual projected pixels; close overlapping neighbors retain probable ownership. Other capable sources are displaced from compact deficit core but crowding limits localization. All Gaia neighbors are retained in pixel JSON.

| Source | Separation arcsec | G | Required intrinsic loss proxy | Pixel coordinate | Diluted pixel loss |
|---|---:|---:|---:|---|---:|
| 5351360235266445568 | 20.031799303421252 | 12.864673 | 0.09148702558972747 | [6.429879696783621, 7.84715444702729] | 0.009128277718474069 |
| 5351360308314513920 | 25.266545586944385 | 16.100832 | 0.9997134682855747 | [8.588842941994933, 8.381180445620192] | 0.011911246711458824 |
| 5351360308314513152 | 40.20503249539216 | 15.429647 | 0.5585564416742173 | [9.05482424327354, 9.059711612616049] | 0.0022979583005877267 |
| 5351360273954774144 | 42.52706020587213 | 14.337115 | 0.23142746267309955 | [8.768348177909699, 9.556810807833772] | -3.8042757881768166e-05 |
| 5351360273954774528 | 50.378965526762386 | 14.809184 | 0.3340972238670255 | [6.848135128632469, 10.476786078243428] | 0.017607220973876504 |
| 5351360239594430208 | 54.75049290670513 | 15.872371 | 0.8181554748712525 | [4.698622064769106, 8.420438086653014] | 0.007765753473322694 |
| 5351360205234688384 | 55.6239933495734 | 13.928894 | 0.17235106524699373 | [4.7167434970293645, 8.772644367694706] | 0.004781832745643519 |

G-band pairwise brightness screen assumes approximate passband/aperture response; intrinsic required eclipse cannot be directly compared with diluted pixel loss. Unresolved unlisted companions are not excluded.

Alternative reduction: independently extracted background-subtracted TESScut1x1/3x3/5x5 depths=21.14934/22.18539/17.98584ppt; QLP median=42.91846ppt. Pixel sector64 is a distinct observing occasion on the same TESS instrument; no same-sector QLP comparison claimed. Independent processing is not an independent instrument. Different apertures respond differently to dilution/background.

Gaia source5351360308313918848: period=10.511668418+/-0.005780592d; e=0.0347176; omega=194.7570037deg; periastron BTJD=386.66479107. Closest conjunction offset=-0.1320267d (-0.0125600phase), source-specific full-covariance linear error=0.7689467d. Correlation order P,gamma,K,e,omega,Tp with subindices0,3,4,5. Linear propagation is descriptive, not a Gaussian veto or ownership proof. Both conjunctions retained in [../gaia-geometry.json](../../campaign/batch14/gaia-geometry.json). Mass function=0.09367283solar, assumed M1=1.4, minimum M2=0.758539; approximate central duration=13.4862h versus observed=12.5296h. TIC radius/main-sequence companion scaling, edge-on conjunction and stellar evolution are assumptions; this is a plausibility check, not a fitted physical solution.

| Sector | Same-kind cycle | Measured BTJD | Formal center error d | Conservative input error d | Realized depth ppt |
|---|---:|---:|---:|---:|---:|
| 10 | 1 | 1592.433631788 | 0.00386248075 | 0.0104166481 | 42.54572 |
| 63 | 137 | 3021.495209608 | 0.00782261169 | 0.00782261169 | 45.65452 |
| 63 | 138 | 3031.970695563 | 0.00163565665 | 0.00163565665 | 43.29120 |
| 99 | 235 | 4051.211210360 | 0.00121567333 | 0.00121567333 | 38.60979 |

Catalogue novelty is separate from this physical verdict. Shared coverage matrix and source identity checks are authoritative for catalogue recovery; period agreement alone cannot establish attribution.


Stable review key: R673.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch14/458606209/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch14/458606209/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch14/458606209/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch14/458606209/fresh-pixels/run.log)
- [historical/diff_s64.json](../../campaign/batch14/458606209/historical/diff_s64.json)
- [historical/diff_s64.png](../../campaign/batch14/458606209/historical/diff_s64.png)
- [historical/gaia.json](../../campaign/batch14/458606209/historical/gaia.json)
- [measurements.json](../../campaign/batch14/458606209/measurements.json)
- [phase-review.png](../../campaign/batch14/458606209/phase-review.png)
- [raw-events.png](../../campaign/batch14/458606209/raw-events.png)
- [raw-windows.csv](../../campaign/batch14/458606209/raw-windows.csv)
- [secondary-windows.csv](../../campaign/batch14/458606209/secondary-windows.csv)

[Batch audits and scripts](../../campaign/batch14/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
