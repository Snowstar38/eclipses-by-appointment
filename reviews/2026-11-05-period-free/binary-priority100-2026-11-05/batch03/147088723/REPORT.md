# T029 — TIC 147088723

**Physical verdict:** REFUTED. **Full bounded review:** COMPLETE. **Catalogue novelty:** UNKNOWN; shared catalogue checks lack four VizieR gates (VSX, ASAS-SN, Kostov 2025 tables 3 and 4) after failed positive controls. This is not a negative catalogue match.

## Raw event and timing evidence

Across s9/10/36/63/90/99/100, repeated rounded troughs alternate with broad humps on about a 6.5 d scale. s63 alone has four troughs roughly 3.2 d apart; several selected flags are successive wave minima. The flux changes continuously before and after each minimum rather than entering and exiting an isolated eclipse, and Gaia P=25.95 d is not established by event timing.

Measured eclipse period: none supported. Epoch BTJD: none supported. Depth: none supported. Screening times in the source packet are not measured centers. See [numeric review](lead-numeric.json), [raw panels](lead-raw-01.png), [sector panels](lead-sector-01.png), and batch [gap evidence](../lead-gap-evidence.json).

## Attribution, reduction and orbit

Gaia DR3 5363594574160217600 has a spectroscopic orbit P=25.951466 d. At the evaluated event/screen epoch, the closest edge-on conjunction offset is -4.268 d, with a 1.384 d linear Gaia-covariance uncertainty. This geometry comparison is supportive only if the raw feature is an eclipse. Gaia neighbors inside 10 arcsec: 2.03 arcsec G=18.18; 3.95 arcsec G=19.39; 6.69 arcsec G=18.62. Neighbor flux ratios alone cannot assign a source.

The persistent smooth waveform across multiple sectors is a positive alternative explanation for the detector windows.

The MAST Tesscut footprint query lists 8 sectors, latest 100. Its response is in [current-sector receipt](../lead-current-sectors.json).

## Limits and next test

The raw dips belong to a continuous quasi-periodic wave, with no eclipse-like isolated floor or Gaia-period clock. Model the non-eclipse variability if astrophysically interesting.

Source packet SHA-256: `56a4e09e782f92ae2fafeab1b821c48623bebe2f919f8a14a5f900c421032279`. Every QLP FITS read by the numeric script was checked against its bulk packet hash; individual source paths and hashes are in `lead-numeric.json`. The shared Gaia neighbor and NSS catalogues were reused without new catalogue queries.
