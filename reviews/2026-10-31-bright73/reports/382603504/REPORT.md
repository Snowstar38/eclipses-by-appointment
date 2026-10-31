# TIC 382603504: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 40 distinct eclipse events in selected sectors[30, 97]. The representative raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 17 same-kind midtimes give P=2.8391421780 +/-0.0000023540d, reference eclipse epoch BTJD2118.3611320, kind: Deeper eclipse; even historical half-period cycles. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S97 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation1.862arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.283. Capable neighbours: Gaia 4701453381830346240: 25.74 arcsec, G16.574, required fractional eclipse0.169; Gaia 4701453381830346368: 26.90 arcsec, G15.507, required fractional eclipse0.064; Gaia 4701453205735853312: 57.51 arcsec, G17.719, required fractional eclipse0.480
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths2.222/2.431/2.231ppt, with 36 stacked events. QLP selected-kind fitted median3.568ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR34701453381830347008, P=2.8391342975+/-0.0000612090d, e=0.037138, omega=190.6897deg. Closest edge-on conjunction offset-0.008284d (-0.002918phase), full-SB1-covariance linear propagated Gaia uncertainty0.045358d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.013083d (photometric period projection allowance0.001434d). The approximate central duration5.86h vs observed median1.48h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Persistent unequal alternating eclipses: even historical half-period cycles are deeper; only those17 measured events define the orbital ephemeris. Half-period is rejected by unequal parity depths in both sectors. Target deficit0.089pixel versus capable neighbor1.360pixels.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 30 | 557 | 2116.9378844 | 0.003758 | 2.072 | measured; excluded from primary fit (secondary event) |
| 30 | 558 | 2118.3597039 | 0.003472 | 4.113 | used in ephemeris |
| 30 | 559 | 2119.7816907 | 0.004166 | 1.532 | measured; excluded from primary fit (secondary event) |
| 30 | 560 | 2121.2007854 | 0.003472 | 4.068 | used in ephemeris |
| 30 | 562 | 2124.0383936 | 0.003472 | 4.503 | used in ephemeris |
| 30 | 563 | 2125.4597016 | 0.006833 | 1.717 | measured; excluded from primary fit (secondary event) |
| 30 | 564 | 2126.8761905 | 0.003472 | 3.570 | used in ephemeris |
| 30 | 567 | 2131.1425483 | 0.005153 | 2.342 | measured; excluded from primary fit (secondary event) |
| 30 | 568 | 2132.5576719 | 0.003472 | 3.353 | used in ephemeris |
| 30 | 569 | 2133.9644958 | 0.004286 | 1.806 | measured; excluded from primary fit (secondary event) |
| 30 | 570 | 2135.3999099 | 0.003472 | 3.358 | used in ephemeris |
| 30 | 572 | 2138.2347111 | 0.003472 | 4.889 | used in ephemeris |
| 30 | 573 | 2139.6588831 | 0.005267 | 1.546 | measured; excluded from primary fit (secondary event) |
| 30 | 574 | 2141.0778246 | 0.003472 | 4.348 | Singular or unidentifiable center covariance: formal timing uncertainty exceeds search duration; excluded from ephemeris. |
| 97 | 1840 | 3938.2487732 | 0.003216 | 3.871 | used in ephemeris |
| 97 | 1841 | 3939.6756944 | 0.003363 | 1.648 | measured; excluded from primary fit (secondary event) |
| 97 | 1842 | 3941.0895928 | 0.001790 | 3.568 | used in ephemeris |
| 97 | 1843 | 3942.5043977 | 0.004681 | 2.193 | measured; excluded from primary fit (secondary event) |
| 97 | 1844 | 3943.9321240 | 0.002265 | 2.729 | used in ephemeris |
| 97 | 1845 | 3945.3436402 | 0.007403 | 0.645 | measured; excluded from primary fit (secondary event) |
| 97 | 1849 | 3951.0188889 | 0.006166 | 1.966 | measured; excluded from primary fit (secondary event) |
| 97 | 1850 | 3952.4482325 | 0.002438 | 2.956 | used in ephemeris |
| 97 | 1851 | 3953.8646719 | 0.004702 | 2.938 | measured; excluded from primary fit (secondary event) |
| 97 | 1852 | 3955.2835655 | 0.002459 | 3.667 | used in ephemeris |
| 97 | 1853 | 3956.7028101 | 0.003161 | 2.344 | measured; excluded from primary fit (secondary event) |
| 97 | 1854 | 3958.1239220 | 0.002032 | 3.463 | used in ephemeris |
| 97 | 1855 | 3959.5446403 | 0.003948 | 2.026 | measured; excluded from primary fit (secondary event) |
| 97 | 1859 | 3965.2198753 | 0.001157 | 0.985 | Singular or unidentifiable center covariance: formal timing uncertainty exceeds search duration; excluded from ephemeris. |
| 97 | 1860 | 3966.6448092 | 0.002995 | 3.349 | used in ephemeris |
| 97 | 1861 | 3968.0605634 | 0.002046 | 2.121 | measured; excluded from primary fit (secondary event) |
| 97 | 1862 | 3969.4843390 | 0.002114 | 2.838 | used in ephemeris |
| 97 | 1863 | 3970.9024741 | 0.001759 | 1.788 | measured; excluded from primary fit (secondary event) |
| 97 | 1864 | 3972.3225758 | 0.003392 | 3.452 | used in ephemeris |
| 97 | 1865 | 3973.7357642 | 0.002947 | 2.138 | measured; excluded from primary fit (secondary event) |
| 97 | 1869 | 3979.4232988 | 0.007569 | 0.968 | measured; excluded from primary fit (secondary event) |
| 97 | 1871 | 3982.2492902 | 0.010649 | 0.965 | measured; excluded from primary fit (secondary event) |
| 97 | 1872 | 3983.6787296 | 0.001157 | 3.062 | Singular or unidentifiable center covariance: formal timing uncertainty exceeds search duration; excluded from ephemeris. |
| 97 | 1873 | 3985.0974385 | 0.003611 | 3.079 | measured; excluded from primary fit (secondary event) |
| 97 | 1874 | 3986.5136329 | 0.002738 | 4.700 | used in ephemeris |
| 97 | 1875 | 3987.9432722 | 0.004322 | 2.474 | measured; excluded from primary fit (secondary event) |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s97.json, historical/diff_s97.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R378. [Deciding evidence](../../evidence/382603504/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/382603504/measurements.json), [raw eclipse plots](../../evidence/382603504/raw-events.png), [raw flux windows](../../evidence/382603504/raw-windows.csv), [Gaia geometry](../../analysis/batch05/gaia-geometry.json), [independent audit](../../analysis/batch05/helper-audit.md), [difference image](../../evidence/382603504/historical/diff_s97.png).
