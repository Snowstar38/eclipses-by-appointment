# T026 — TIC 341688154

**Physical verdict:** PROBABLE. **Full bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; shared catalogue checks lack four VizieR gates (VSX, ASAS-SN, Kostov 2025 tables 3 and 4) after failed positive controls. This is not a negative catalogue match.

## Raw event and timing evidence

Sharp raw SAP dips occur in s14 at 1703.34705, s21 at 1877.82516, s48 at 2633.87057 and s74 at 3331.75814. Their cycle counts 0,3,16,28 yield P=58.157443 d with residuals at most 0.0034 d. Local depths are 5.2–6.6 ppt and durations 0.13–0.15 d. The s48 event was absent from retained flags and s74 from the initial ranking; both were recovered at the measured clock.

Measured eclipse period: 58.157443 ± 0.000349 d. Epoch BTJD: 1703.35043. Depth: 5.8 ppt. Screening times in the source packet are not measured centers. See [four-event timing](lead-timing.json), [tested alias windows](../lead-t026-alias.json), [numeric review](lead-numeric.json), [raw panels](lead-raw-01.png), [sector panels](lead-sector-01.png), and batch [gap evidence](../lead-gap-evidence.json).

## Attribution, reduction and orbit

Gaia DR3 1682702323250248704 has a spectroscopic orbit P=58.170918 d. At the evaluated event/screen epoch, the closest edge-on conjunction offset is -0.962 d, with a 3.252 d linear Gaia-covariance uncertainty. This geometry comparison is supportive only if the raw feature is an eclipse. Gaia neighbors inside 10 arcsec: 6.17 arcsec G=16.52; 6.66 arcsec G=12.36. Neighbor flux ratios alone cannot assign a source.

QLP KSPSAP shows s14/s21/s48 dips of ~4.0/4.9/4.3 ppt in the same photons. Terra independently extracted a 2.68 ppt s48 deficit from a TESScut 3x3 aperture; its difference image is on the target/neighbor blend, 0.317 TESS pixel apart, and cannot distinguish them. These are alternative reductions of the same photons, not additional observing occasions. Current TESS footprint has no newer sector than s75.

The MAST Tesscut footprint query lists 9 sectors, latest 75. Its response is in [current-sector receipt](../lead-current-sectors.json).

## Limits and next test

Four same-kind eclipses and a tested clock, but the Gaia neighbor 6.66 arcsec away at G 12.36 could produce the diluted loss. TESScut s48 difference imaging places the deficit on their unresolved blend. Resolve target versus the 6.66 arcsec neighbor with high-resolution in-eclipse imaging or spectroscopy.

Source packet SHA-256: `d422452ea9ff4711f4a3fec713caf12d60d235187e4ff82ad07e9cc192432394`. Every QLP FITS read by the numeric script was checked against its bulk packet hash; individual source paths and hashes are in `lead-numeric.json`. The shared Gaia neighbor and NSS catalogues were reused without new catalogue queries.

The full-window alias checks reject 87.237 d (two cycles), 43.618 d (four cycles), 34.895 d (five cycles), 29.079 d (P/2) and 19.386 d (P/3) through cadence-complete raw nulls. The 58.157 d fit uses conservative timing-error floors rather than formal trapezoid errors alone. A 6.66 arcsec G=12.36 neighbor is capable: its Gaia-G flux ratio is ~0.403, implying only ~2% intrinsic eclipse depth for the observed ~5.8 ppt blended loss. See [helper audit](../helper-audit.txt), [difference image](helper-pixels-s48.png) and [numeric pixels](../helper-pixels.json).
