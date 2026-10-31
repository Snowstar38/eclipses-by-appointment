# Independent helper audit — batch 01

Scope: independent weighted regression of selected fitted raw-SAP eclipse centers; examination of raw-event contact sheet and four historical pixel maps; identity and centroid/neighbor inventory for all ten. Reproduce `python helper/timing_audit.py` and `python helper/pixel_audit.py`. Their JSON files hash each measurement or deciding historical pixel JSON, figure, Gaia receipt and cutout. QLP timings and TESScut apertures share TESS photons; the latter tests extraction robustness, not an independent observing occasion. Historical image-window centers are ephemeris-guided and are not measured times. Flux-budget capability uses approximate Gaia G; intrinsic neighbor loss required and blended pixel loss are different quantities, not a valid direct comparison. Unlisted/unresolved sources remain possible.

Ten periods, timing errors and epochs were independently recalculated by centered weighted linear regression; all period differences are under 5e-13 d. This verifies fit arithmetic, not cycle or systematic uncertainty. Error floors and scatter inflation are approximate, not calibrated total uncertainty. All ten target IDs match selected Gaia identifiers, WCS target positions, and cutout sector headers.

- 135362193: S79 deficit 0.11 px from target, capable sources at 18.9 and 22.9 arcsec, 0.91 and 1.06 px from deficit. Visually target-centered core favors target at image resolution; close sources retain uncertainty.
- 346865542: S42 deficit 0.03 px from target, no listed capable neighbors.
- 131331287: S64 deficit 0.06 px, no listed capable neighbors.
- 48752905: S33 deficit 0.08 px; three capable sources 40.3–47.2 arcsec. Even half-period cycles are deeper (~36–41 ppt versus ~16–21 ppt), so the adopted 1.72209 d period times same-kind events, not the ~0.861 d photometric interval.
- 337881909: S13 deficit 0.06 px, eight capable neighbors, nearest 17.8 arcsec and 0.80 px from deficit; PSF fractional residual 0.83. Map favors target but crowded field and residual limit uniqueness.
- 274578846: S23 deficit 0.15 px; capable source at 28.9 arcsec and 1.44 px from deficit. Map favors target at pixel resolution.
- 14291901: S43 deficit 0.05 px, no listed capable neighbors.
- 180179209: S64 deficit 0.23 px; eleven capable neighbors, nearest 16.6 arcsec and 1.00 px from deficit; PSF residual 0.82. Map favors target but crowded field and residual limit uniqueness. Partial/singular cycle 399 is excluded from timing.
- 351335839: S13 deficit 0.14 px and no listed capable neighbors, though PSF residual 0.99 limits fit quality. Even half-period cycles are deeper (~357–412 ppt versus ~166–174 ppt): fitted 14.83995 d is the orbital-scale doubled interval with same-kind timings. Wider fitting bounds avoid truncating the V-shaped primary.
- 89553209: S14 deficit 0.05 px; one capable source at 53.5 arcsec, 2.60 px from deficit. Partial early cycle -1 has been excluded from the period fit.

Centroid differences are not calibrated localization uncertainties. The highlighted crowded cases should include residual and neighbor caveats, with resolved follow-up if attribution remains material. Catalogue novelty and full Gaia NSS provenance are separate central checks. Contributor: independent helper audit.

Final freeze audit: helper/final-hashes.json records SHA-256 hashes of final RESULTS, ten reports, measurements, plots, raw windows, geometry, alias and lead audit, and independent audit products. All result numeric fields exactly match measurements; the final reports now distinguish secondary events excluded from primary ephemerides. The lead's final manifest should hash this audit and all helper files after freeze.
