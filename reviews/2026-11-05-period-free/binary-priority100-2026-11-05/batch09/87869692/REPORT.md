# T084 / TIC 87869692: PLAUSIBLE

Queue stratum: repeat_sector_dip. Bounded physical review: complete. Catalogue novelty: UNKNOWN.

## Deciding evidence

Raw eclipse-shaped deficits near BTJD 2521.286 (s44) and 3243.049 (s71) are separated by 721.763 d; 22 Gaia-near cycles give a conditional 32.807395 d period. The s71 event is about 107 ppt in the raw fit and 70 ppt in the independent TESSCut aperture. The target is saturated, so the split bleed-pattern difference image does not locate a unique peak. Explicit 20-24-cycle aliases were checked against s72: the Gaia-near 22-cycle next window at 3275.856 has zero core cadences, while 20- and 21-cycle predictions are fully covered and flat. The 23- and 24-cycle predictions also fall in gaps.

## Measurement and scope

Gaia source 882872210352301568; selection orbit 32.80745139832254 d; Gaia G 6.919019. The raw QLP SAP analysis inspected 4 hash-verified FITS sectors and 6 retained dip windows, including actual quality and time coverage. Local trapezoid centers, event depths, sectors, and source hashes are in [lead-numeric.json](lead-numeric.json); representative profiles are in lead-raw-*.png. These retained detector windows were not taken as verdicts.
Source packet SHA-256: a8c862dfcacc15f6a7b9813003cd106e582ea4479f3eb62f10bbfbf9408c5a72. Bulk-result SHA-256: da161f95176fa48c682f5ccf1c939d698575de522ec90c6e0f4b1f6ad022ccdc.

No supported unique same-kind eclipse period is reported for this queued target.

The helper independently extracted the strongest event from TESSCut with a positive-flux target aperture and checked the difference pixels; see [helper audit](../helper-audit.md), [numeric pixel audit](../helper-pixel-audit.json), and helper-difference.png. It is a second reduction of the same TESS photons.

Explicit alias/coverage calculations: [lead-alias-t084.json](../lead-alias-t084.json). The zero-cadence predicted window is a gap, not a null. Gaia point geometry from [Thiele-Innes inversion](../lead-thiele.json) also supports a conjunction, but does not resolve the timing alias.

## Limits and next check

Only two secure same-kind centers exist; the principal Gaia-near alias and two shorter aliases remain untested by actual coverage. Saturation limits pixel attribution. The footprint lists an unusual s1751 record without a usable cached light curve; it is not counted as a confirming sector.

Obtain a fully covered same-kind repeat and saturation-aware difference image, then resolve the integer-cycle alias.

Catalogue status uses the [shared queue-wide audit](../../shared-catalogues/REPORT.md). Its four unavailable VizieR gates are unknown, not negative matches.
