# TIC 396248369: REFUTED

Queue position 53; batch06. Review credits: GPT-6.1 Sol, fresh GPT-6.1 Terra review, supervised by Astra. This is AI review, not human validation.

1. Raw morphology and repeat assessment

QLP sectors13,94,103 include apparent sharp dips near rapid baseline changes, but the original-phase fits fail to establish real repeat eclipses. In the fresh custom extraction, the S94/S103 apparent dips correspond to large positive ramps or segment-level changes; a detached negative eclipse is not independently recovered. Original covered phases have sub-millimagnitude or negative short-window signed deficits. The search period is not a measured binary eclipse period.

Three cached QLP SAP_FLUX FITS sectors were checked with QUALITY=0 and target/sector header verification. Local quadratic baseline plus trapezoid fits are in raw-events.json, including failed or boundary fits. No non-boundary fit exceeds three local residual RMS; no repeat eclipse series establishes a period. Original search period 18.390769704 d is retained only as a conditional alias, not a derived ephemeris. The full morphology overview explicitly checks features away from that alias; raw-event fits alone do not decide the result. Covered conditional phases: [{"sector": 13, "cycle": 0, "nominal_tc": 1663.3432, "n_in": 4, "n_pre": 8, "n_post": 8, "covered": true, "signed_depth": -0.0002053380012512207, "local_rms": 0.0014788307016715407}, {"sector": 13, "cycle": 1, "nominal_tc": 1681.7339697044129, "n_in": 6, "n_pre": 9, "n_post": 8, "covered": true, "signed_depth": 0.0006639957427978516, "local_rms": 0.000878628867212683}, {"sector": 94, "cycle": 120, "nominal_tc": 3870.23556452954, "n_in": 46, "n_pre": 78, "n_post": 78, "covered": true, "signed_depth": 0.00036269426345825195, "local_rms": 0.005096118431538343}, {"sector": 103, "cycle": 136, "nominal_tc": 4164.4878798001455, "n_in": 40, "n_pre": 69, "n_post": 51, "covered": true, "signed_depth": -0.0019028186798095703, "local_rms": 0.028664467856287956}].

2. Source and independent reduction

Fresh 11x11 TESScut images and TIC 60-arcsec cones were obtained in two sectors. Signed candidate-phase difference images and fixed-coordinate target/capable-neighbour comparisons were attempted using the original search phase. Since no real repeating eclipse exists to localize, these candidate-only fits do not establish an eclipse host or an off-target EB. They are retained as failed candidate tests, not localization detections. Capability limits use the original claimed depth and ignore aperture throughput/bandpass uncertainty.

Fresh cutout sectors: 94,103. Candidate capability counts: 94: 4,103: 4. Source comparisons are descriptive signed-image Gaussian fits, with no calibrated PRF confidence. Neighbour catalogue identity can include unresolved or duplicate records. The independent extraction subtracts each frame's lowest-30-pixel median background then sums a central 3x3 aperture, with QUALITY=0. It uses the same TESS photons through a distinct reduction, and is not SPOC. custom-morphology.png and custom-extraction.json preserve its deciding morphology.

3. Gaia orbit

Gaia NSS orbit metadata were inspected, but no photometric eclipse ephemeris was established; an eclipse/conjunction geometry comparison is therefore inapplicable. Nearness of the original search alias to the Gaia period cannot establish eclipses.

Gaia source 6367733051516351360; NSS P=18.380294812 +/- 0.012093988 d; e=0.26564, omega=257.6767 degrees. No eclipse timing or geometry is inferred from this metadata. No photometric eclipse orbit established; Gaia spectroscopic binarity not refuted.

4. Scoped prior EB coverage

no identified prior EB; coverage complete: yes. Reused centrally completed seven scopes: VSX, SIMBAD primary type, Gaia DR3 eclipsing binaries, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4, ASAS-SN. SB* and ROT alone are not EB identifications; Kostov table2 is unvetted. This is a scoped catalogue result, not an exhaustive discovery claim. Physical and novelty verdicts are separate.

5. Completion and limitations

The representative full review is complete. Scientific outcome: submitted eclipse interpretation refuted by a demonstrated smooth/systematic explanation. Missing eclipse geometry reflects the absence of a valid eclipse series, not unfinished execution. Representative three QLP sectors and two independent custom-extraction sectors; no exhaustive all-sector search, calibrated PRF/noise model, physical fit or sensitivity upper limit. Refutation applies to the submitted eclipse interpretation, not to binarity or all possible shallow eclipses.

Next check: No missing deciding gate for this candidate. Reopen only if new data supply distinct, repeated detached events.

Provenance: raw-evidence/cache-manifest.json preserves original cache paths and SHA256; identity-checks.json verifies all 15 QLP inputs; tesscut-downloads.json stores fresh URLs and zip hashes; TIC raw cones and adapted scripts are retained. manifest.json hashes deliverables. No paper edits, commits or publication were performed.
