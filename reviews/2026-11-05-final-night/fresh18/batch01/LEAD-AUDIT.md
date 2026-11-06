# Lead audit - fresh18 batch01



Exact queue: Y001-Y006, Y008-Y009, TIC 22559994, 65684549, 70554665, 93330962, 111230893, 122766753, 140777703, 156747165. No other batch was physically reviewed. The lead owns this bounded physical adjudication; supervisor owns novelty, acceptance and publication.



Definitions read: [workspace]/CLAUDE.md; Astra/made/candidate-review-delegation.txt; Fable 5.1/made/paper/short/sec_methods.html, sections 2.7-2.9. Frozen source cohort is fresh-band-next400, not the prior first100. No selection substitutions or outcome-dependent queue edits.



Completion is independent of physical outcome: eight COMPLETE reports and rows. Final physical tiers: four CONFIRMED (Y003/Y005/Y008/Y009), two PROBABLE (Y001/Y002), one PLAUSIBLE (Y004), one REFUTED selected-target attribution (Y006). Root separately adjudicates claims. A close uncertain uncatalogued blend is not automatically refuted; Y002 remains probable field eclipses with unresolved source. Y006 has positive spatial evidence favoring a specific neighbor across four events and is refuted as the selected target; this distinction is not a novelty decision.



## Deciding exceptions



- Y001: two deep and two shallow same-kind repeat tracks each recur separately. Deep 22-cycle and shallow 38-cycle spans agree at 47.12250 d, neighboring integer counts fail the second track. Timing-only 94.245 d family remains, and full source-specific Gaia covariance gives persistent 2.2-2.8 local linear-sigma timing offsets. Retain PROBABLE, not an unsupported unique orbital-period confirmation. Short P/2-P/6 windows were measured with actual quality-zero coverage. Y001 sidebands were narrowed to avoid contaminating the half-period baseline with the observed opposite eclipse one day away; final table uses uncontaminated sidebands.

- Y002: narrow 1.13719 d train recurs in three sectors, but a G9.82 neighbor at 6.46 arcsec is only 0.305 TESS pixel away. Structured local and stacked differences cannot select the owner. The selected 20.825 d Gaia orbit cannot describe this short train. This is PROBABLE with attribution/Gaia limitations, not a refutation based solely on close blending.

- Y004: one retained narrow S32 event, no secure narrow S98 repeat. Live sector inventory revealed S107-S109 and all three were fetched, independently extracted and visually inspected. S107 has essentially zero/no-stellar-PSF data and is unavailable as a sensitive test. S108-S109 show broad systematics; no comparable narrow repeat established. PLAUSIBLE after a completed bounded review, not an unperformed check.

- Y006: real 2.20928 d eclipse train, different from Gaia 27.6256 d. Four separate S59 local differences all peak (4,5) and have centroids near Gaia DR3 201206302856438528 at 19.74 arcsec/0.933 pixel from selected target. Each is about one pixel from target but 0.04-0.20 pixel from neighbor. Lead visually checked the local PSF and adjudicates REFUTED_SOURCE for the selected target. The structured phase stack is a less reliable localization because its baselines mix variable background states; its different centroid does not establish target ownership or override the four local images. PRF calibration or another orientation could revisit that adjudication. The neighbor is a separate characterization lead, not a newly reviewed or relabeled system. G-band intrinsic-depth arithmetic is explicitly conditional on throughput/bandpass/dilution.

- Y009: deep S40/S80 and shallow S53/S80 tracks each recur; opposite kinds were not counted as repeats. Deep and shallow baselines select the same 37.88714 d family over neighboring integer choices. A real S26 half-period prediction at BTJD2032.1208 has 12 quality-zero cadences, full core coverage and -0.143 ppt deficit against 0.757 ppt baseline scatter, unlike 54-57 ppt deep eclipses. Pixel difference has a uniform negative background change; removing exterior offset yields a target-centered positive deficit. Alternate 3x3 extraction reproduces 57 ppt loss. No unearned two-point precision error is reported.



## Evidence inspected and numerical freeze



Lead visually inspected all eight raw/whole-sector contexts (Y004 via whole-sector context), six long/single representative difference images, all corresponding independently extracted light curves, the newer Y004 sector plots, and both helper short-clock local difference images. Helper independently inspected all six long/single difference images and Y004 new-sector plots, then performed short-clock WCS/neighbor/event-local measurements. See helper-audit.md for exact scope. Both reducers reuse TESS photons; multiple reductions are not independent occasions. Many long-sector aperture trends are instrumental and not counted as eclipses.



All raw source SHA256 values were checked, FITS TIC/sector headers matched, Gaia identifiers and nested G magnitudes verified against exact queue. identity-audit.json was deterministically regenerated after supervisor noted a possible accidental other-batch rewrite: SHA256 remained e183c6f3fa52fec6cc464f156b529bcca294cb4fabe5e3feabc5a6e36e15eac9. identity-rerun-receipt.json documents this. Full SB1 source-specific correlation vectors were used for fixed-cycle local linear covariance propagation with indices P,e,omega,Tp from Gaia order P,gamma,K,e,omega,Tp. No mandatory Monte Carlo or exhaustive all-sector fitting was added. Mass functions support stellar-binary plausibility; no precision stellar characterization is claimed.



Shared catalogue source hashes and receipts are pinned in SOURCE-MANIFEST.json. No prior EB counterpart is assigned to these eight in that bounded scope, but nonmatches do not establish exhaustive priority or automatically transfer to a contaminating neighbor. No ledger or public files were changed.



LEAD-AUDIT, reports, source receipts, scripts, cutouts, images, and RESULTS are sealed by SHA256SUMS.json. Timing formal errors, cadence floors and residual inflation remain distinct. Current result periods are representative measured recurrences without a uniform total error.



Contributor note: the project coordinator's thanks were passed to the helper. The independent spatial audit was essential to distinguish Y006's real neighbor eclipses from a selected-target system.

