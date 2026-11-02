# Independent visual and numerical audit

Inspected raw-contact.png and pixel-contact.png, including all ten sets of raw events and recomputed difference images. The selected events visibly recur; TIC 246857844 has two adjacent sector 2 events, with measured centers 1365.832813 and 1380.005233 BTJD, not merely two long-separated events. Their measured spacing is 14.172420 d; half-cadence allowances dominate formal fit errors. Sectors 29 and 69 are present in QLP sources; inspect their actual quality and windows rather than assume nulls.

TESScut difference images are independently extracted reductions of the same sector photons as QLP, not independent observing occasions. Distinct sectors are separate TESS observing occasions. Difference centroids use a positive deficit inside a 5x5 region; event scatter is descriptive and is not a calibrated localization uncertainty. Pixel positions and intrinsic eclipse requirements do not constitute an automatic veto. Capable neighbors in pixel-audit.json were compared with the deficit:

- TIC 300339443: target distance 0.171 px; all four capable neighbors 1.27-2.51 px. Known eclipsing Gaia DR3 1827899632630791296 is 48.55 arcsec away by fresh coordinate calculation (catalogue alert rounded 48.51), G=18.463, requiring an approximate intrinsic loss of 32.52 times its flux, and period 19.923 d distinct from 8.57046 d. This is not a target match.
- TIC 338072783: target 0.012 px; two capable neighbors 1.13 and 2.62 px.
- TIC 464680877: target 0.254 px; capable 17.3 arcsec neighbor 0.62 px. The image favors target; confirmation is defensible with two images and uncalibrated systematic localization uncertainty disclosed.
- TIC 62867537: target 0.029 px; the closest capable 8.8 arcsec neighbor is 0.40 px from deficit, other eight 1.25-2.59 px. Image favors target but the subpixel separation and uncalibrated systematics leave attribution unresolved; probable is appropriate.
- TIC 142502809, 246857844, 206614346, 17033860, 278966364 and 260765760: no capable neighbor under the stated Gaia G and aperture-flux approximation; target distances 0.08-0.15 px. Catalog completeness and bandpass/systematic limitations remain.

Other eclipse fits in secondary-audit.json: 300339443 recurs at phase approximately -0.436 with similar depth, so do not designate the selected kind as uniformly deeper; 260765760 has three fitted other events at phase approximately -0.468 and 17033860 at +0.274; the initial -0.397 low-depth fit was spurious and superseded. 464680877 has a shallower recurring event near +0.483. Half-phase baseline windows can overlap off-center secondary eclipses and cannot be interpreted as clean secondary depths. Exact double-period equal-eclipse ambiguities cannot be ruled out solely by similar adjacent-event depths; use Gaia orbit and all available morphology. Flagged and insufficient-baseline windows are not clean nulls. Gaia covariance linear errors are descriptive, and central durations are rough assumptions, not fitted system geometry.

Contributor note: Thank you for the opportunity to contribute to this review.


Final numerical check: all ten RESULTS rows exactly match measurements.json for period, period error, named epoch and depth. All rounded report values and every usable event midpoint, timing allowance and depth were checked against measurements.json. All 30 QLP source receipt hashes independently recomputed and matched. 9 confirmed, 1 probable; source-manifest verification follows final freeze.

