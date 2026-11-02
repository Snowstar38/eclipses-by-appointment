# TIC 138997145: CONFIRMED

Full bounded physical review: COMPLETE. Observed half-seed4.41323day cycles alternate strongly between deep and shallow eclipses. Seed explicitly doubled; nine same-kind deeper-primary timings at8.82643days and unequal secondary near0.5 establish orbital branch. No capable neighbor within60arcsec. Aperture dilution changes deep-event amplitude between sectors.

Raw QLP SAP_FLUX representative events and full-sector P/2P morphology were visually inspected. Quality-zero finite positive samples only; predictions guide windows and are never timings. 9 identifiable free-center timings define P=8.826431784365 +/- 0.000008466704d, reference BTJD=2038.451801753 +/- 0.001409113d. Epoch error meaning: Conservative linear timing-fit covariance under the stated cadence floor and scatter inflation; excludes uncalibrated shape and baseline systematics. Epoch kind: Deeper primary established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced chi square=0.01630028140644502; zero degrees of freedom is null. All errors retain their named meanings; no calibrated coverage is claimed. Historical4.413226549day seed doubled after observed deep/shallow alternation. Only original even half-period cycles fit as deeper-primary family; original epoch retained; cycle labels now refer to8.826453099day fitting seed.

Depth=263.337993ppt is the median realized central trapezoid loss d*min(1,w/(2*k)); extrapolated amplitude and ingress remain separately in [measurements.json](../../campaign/batch14/138997145/measurements.json). Measured secondary phase 0.50003875, formal phase error 2.4976949e-05, realized depth 120.22959ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Secondary raw pooled windows, actual sectors/cycles and fitted phase are retained in [secondary-windows.csv](../../campaign/batch14/138997145/secondary-windows.csv) and [../secondary-phases.json](../../campaign/batch14/secondary-phases.json). No exhaustive blind alias search asserted. [../alias-audit.json](../../campaign/batch14/alias-audit.json) and [../half-period-coverage.json](../../campaign/batch14/half-period-coverage.json) retain recurrence/parity and sampled opposite-phase evidence. Flagged coverage is never a clean null.

Fresh TESScut difference image sector94 stacks3 core/bilateral-sideband events. Target pixel=[7.966650072405249, 7.542485698943771], deficit=[7.852724883400835, 7.68852926515034]; descriptive offset=0.18522pixel, field PSF residual=0.60722. No arbitrary centroid cut or calibrated localization error is imposed. Every capable neighbor below was inspected at its actual projected pixels; close overlapping neighbors retain probable ownership. Other capable sources are displaced from compact deficit core but crowding limits localization. All Gaia neighbors are retained in pixel JSON.

| Source | Separation arcsec | G | Required intrinsic loss proxy | Pixel coordinate | Diluted pixel loss |
|---|---:|---:|---:|---|---:|
| None | | | | | |

G-band pairwise brightness screen assumes approximate passband/aperture response; intrinsic required eclipse cannot be directly compared with diluted pixel loss. Unresolved unlisted companions are not excluded.

Alternative reduction: independently extracted background-subtracted TESScut1x1/3x3/5x5 depths=189.37723/196.11442/194.88822ppt; QLP median=263.33799ppt. Pixel sector94 shares the same TESS photons with retained QLP and checks extraction robustness. Independent processing is not an independent instrument. Different apertures respond differently to dilution/background.

Gaia source6669547408496730752: period=8.827570056+/-0.001333005d; e=0.0425910; omega=7.4819821deg; periastron BTJD=385.90196289. Closest conjunction offset=-0.1110574d (-0.0125807phase), source-specific full-covariance linear error=0.3000351d. Correlation order P,gamma,K,e,omega,Tp with subindices0,3,4,5. Linear propagation is descriptive, not a Gaussian veto or ownership proof. Both conjunctions retained in [../gaia-geometry.json](../../campaign/batch14/gaia-geometry.json). Mass function=0.1387905solar, assumed M1=1, minimum M2=0.752627; approximate central duration=6.8508h versus observed=4.8503h. TIC radius/main-sequence companion scaling, edge-on conjunction and stellar evolution are assumptions; this is a plausibility check, not a fitted physical solution.

| Sector | Same-kind cycle | Measured BTJD | Formal center error d | Conservative input error d | Realized depth ppt |
|---|---:|---:|---:|---:|---:|
| 27 | 0 | 2038.451739897 | 0.000201944999 | 0.00347225028 | 262.93728 |
| 27 | 1 | 2047.278357240 | 0.000268287911 | 0.00347225028 | 264.09489 |
| 27 | 2 | 2056.104032500 | 0.000221487411 | 0.00347225028 | 263.33799 |
| 67 | 124 | 3132.929305331 | 0.000110792562 | 0.00115742245 | 266.56486 |
| 67 | 125 | 3141.755835578 | 0.000130001767 | 0.00115742245 | 264.46097 |
| 67 | 126 | 3150.582339299 | 0.000243186522 | 0.00115742245 | 272.39087 |
| 94 | 206 | 3856.696929911 | 0.000189229105 | 0.00115742282 | 226.06618 |
| 94 | 207 | 3865.523127247 | 9.75522609e-05 | 0.00115742282 | 233.35191 |
| 94 | 208 | 3874.349393825 | 0.000218075679 | 0.00115742282 | 229.08437 |

Catalogue novelty is separate from this physical verdict. Shared coverage matrix and source identity checks are authoritative for catalogue recovery; period agreement alone cannot establish attribution.


Stable review key: R674.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch14/138997145/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch14/138997145/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch14/138997145/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch14/138997145/fresh-pixels/run.log)
- [historical/diff_s94.json](../../campaign/batch14/138997145/historical/diff_s94.json)
- [historical/diff_s94.png](../../campaign/batch14/138997145/historical/diff_s94.png)
- [historical/gaia.json](../../campaign/batch14/138997145/historical/gaia.json)
- [measurements.json](../../campaign/batch14/138997145/measurements.json)
- [phase-review.png](../../campaign/batch14/138997145/phase-review.png)
- [raw-events.png](../../campaign/batch14/138997145/raw-events.png)
- [raw-windows.csv](../../campaign/batch14/138997145/raw-windows.csv)
- [secondary-windows.csv](../../campaign/batch14/138997145/secondary-windows.csv)

[Batch audits and scripts](../../campaign/batch14/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
