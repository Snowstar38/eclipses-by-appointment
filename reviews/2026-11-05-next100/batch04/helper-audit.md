# Independent helper audit, Q031–Q040

This audit used the unchanged sealed batch queue, source packets and their original QLP FITS. `helper-audit.py` verified the source-packet index SHA256, bulk-result SHA256, and every referenced FITS SHA256 before computing `helper-raw-metrics.json`. Screening times are not treated as measured eclipse centers. The fresh TESSCut ZIPs and Gaia TAP CSV are preserved with request and response hashes in `helper-pixels.json` and `helper-neighbors.json`; those cutouts are a separate extraction of the same TESS photons.

## Q031 / TIC 209429773

Three broad candidate same-kind raw SAP losses occur around BTJD 2123.10 (S30), 2165.64 (S31), and 3952.25 (S97), with 4.6–6.3 ppt simple local core losses in the independent QLP calculation. S31 has a 2165.306–2165.459 quality-zero gap near ingress, so its broad Gaussian center is diagnostic, not precision timing. S30 to S31 is approximately one Gaia-period cycle; S31 to S97 is conditionally 42 cycles, giving about 42.5383 d. The target Gaia SB1 period is 42.54056 d, but orbital association still needs the lead's source-specific conjunction assessment.

Fresh 11×11 TESSCut WCS cubes S30, S31, S97 have finite strongly positive target pixels (sky-subtracted medians about 14,023, 25,205, and 16,705 e/s). Independent 3×3 target-centered losses are 5.26, 4.28, and 6.17 ppt, with positive difference centroids 0.263, 0.138, and 0.116 pixel from the target WCS position. The nearest other Gaia DR3 star within 120 arcsec is G16.67 at 31.6 arcsec, versus target G8.61 (nominal G flux ratio about 0.0006); no catalogued neighbor is approximately capable of the observed 5–7 ppt total blended loss. The pixel maps visibly peak on the target in all three sectors. This strongly favors target ownership, subject to TESS PRF and Gaia-bandpass limits.

`helper-Q031-aliases.py` uses actual quality-zero positive cadences, requires full ±0.18 d core coverage with no >3-cadence internal gap, and uses bilateral 0.65–1.1 d sidebands. At the S97 P/2 extra prediction BTJD 3973.52, the full core is covered and the local loss is only +0.47 ppt with this sideband choice, versus roughly 5–7 ppt real events. Three fully covered P/3 extra windows show −0.32 to +0.32 ppt and six P/4 windows −0.58 to +0.92 ppt. The lead's alternative local baseline gives a slightly different P/2 value; both are far below the events. These nulls reject the tested short same-kind aliases, not arbitrary orbital configurations or shallow opposite-kind events.

## Q036 / TIC 250561084

The QLP raw SAP and KSPSAP S18 data show four sharp, nearly identical dips near 1792.516, 1798.661, 1804.807, and 1810.953, spaced about 6.1456 d. S85 raw SAP shows dips near 3618.002 and 3630.267 plus an unflagged dip fitted by the lead at 3624.14759. This is a real recurring blended-aperture eclipse train, distinct from the queued target's Gaia SB1 20.14331-d period. It must not be assigned to the queued star merely because QLP's target aperture contains it.

A successful bounded Gaia DR3 TAP cone query identifies a capable star 28.85427 arcsec north: **Gaia DR3 358527789513614336**, RA 31.72583458789421°, Dec +50.74872579645119°, G15.339438. The queued target is Gaia DR3 358526934817572608, RA 31.72932997639835°, Dec +50.74102194133833°, G11.463103. The neighbor's approximate G flux ratio to target is 0.028149. A deep eclipse of that star can supply an approximately 8–10 ppt blended loss; this flux budget is descriptive and bandpass dependent.

Fresh S18 and S85 TESSCut WCS images have positive target-pixel flux and show the deficit at the neighbor's location. The simple median S85 difference is invalid because a global background drift reverses the raw sign across the cutout. `helper-cutout-series.py` subtracts corner sky per cadence and fits a local linear sideband trend per pixel. Both corrected maps peak at (x=5,y=7). Neighbor WCS positions are (5.293,7.177) and (5.347,7.298); target positions are (5.034,5.803) and (5.173,5.898). The corrected positive difference centroids are (5.351,6.884) and (5.342,7.195): about 0.29/0.10 pixel from the neighbor versus 1.12/1.31 pixels from target. Disjoint x=4–6 stripes show neighbor-side y=7–8 losses of 37.69 and 39.99 e/s, while target-side y=5–6 loses only 8.43 and 4.00 e/s. This morphology repeats in both sectors. Their WCS orientations are similar, so this is repeated spatial evidence, not roll-angle diversity. 3×3 apertures centered on each star overlap at 1.4-pixel separation; their 11.0/11.8 ppt neighbor and 6.6/5.7 ppt target-aperture losses cannot be interpreted as independent source depths. The peak location and disjoint stripes support **off-target ownership** of the selected 6.145-d eclipse train. The queued target could still have a different binary signal.

## Remaining flags

| ID | Independent raw assessment |
| --- | --- |
| Q032 | S94 ~3874.88 and S104 ~4197.37 are broad asymmetric trough/recovery structures, with sector-common waveform and gap-linked level changes. S94 ~3869.64 begins exactly after a 3868.503–3869.644 gap; S102 ~4144.32 is shallow variation. No sharp repeated source-specific eclipse is established. |
| Q033 | S101 ~4113.26 descends into a 4113.263–4114.393 gap and resets high afterward. S103 ~4165.06 similarly enters the 4165.080–4166.129 gap; S102 ~4133.12 is a level step. Missing cores prevent eclipse centers. |
| Q034 | S9 ~1557.35 is a one-sided recovery shortly after a 1555.512–1557.304 gap and is largely removed in KSPSAP; S10 ~1571.49 is a step/slope. S37/S65 flagged contrasts are trend or edge dominated. |
| Q035 | S64 ~3054.74 is exactly at the 3054.743–3055.317 gap. S94 ~3874.87 has the same broad trough/recovery as Q032/Q037/Q038/Q039; S96/S97 flags are gaps and level offsets. |
| Q037 | S94 ~3874.94 has the shared trough/recovery; S104 ~4185.39 is a level step after 4184.807–4185.057 gap. |
| Q038 | S94 ~3874.81 is the same broad shared trough; ~3867.61 is a monotonic slope. S103 ~4166.54 is one-sided recovery from 4165.080–4166.129 gap; ~4159.66 is a step. |
| Q039 | S94 ~3874.89 is the shared trough; S101 ~4119.12 and S102 ~4145.38 are broad gap/level structures without a stable eclipse profile. |
| Q040 | S41 ~2431.83 is a SAP-only downward slope suppressed in KSPSAP. S74/S75/S76/S83 flags are long monotonic slopes with intervening gaps and level resets, not repeated measured minima. |

The repeated S94 structure in five spatially separate targets is a common-mode clue combined with each actual raw shape/gap context, not a categorical veto. The selected detector flags of these eight cases do not establish their queued Gaia sources as eclipsing binaries; this does not exclude other signals.

The most useful check in this batch was restoring the S85 cutout background trend: it exposed a repeatable off-target pixel deficit that the uncorrected difference map concealed.
