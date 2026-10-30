# TIC 275022619: PLAUSIBLE

Queue position 51; batch06. Review credits: GPT-6.1 Sol, fresh GPT-6.1 Terra review, supervised by Astra. This is AI review, not human validation.

1. Raw morphology and repeat assessment

QLP sectors 12,65,103 show smooth slopes and broad variability. The sharp-looking sector103 changes occur at segment edges. At the covered original nominal phase, the short-window signed depth is negative (brightening), and the template fit hits its timing/duration bounds. The fresh custom aperture shows smooth variability and segment offsets without a repeat narrow eclipse. Independent Terra audit retains PLAUSIBLE: the available representative data fail to establish recurring eclipses, but sparse/compromised coverage does not tie the original search detection to a specific demonstrated artifact. This is not a secure eclipse identification.

Three cached QLP SAP_FLUX FITS sectors were checked with QUALITY=0 and target/sector header verification. Local quadratic baseline plus trapezoid fits are in raw-events.json, including failed or boundary fits. No non-boundary fit exceeds three local residual RMS; no repeat eclipse series establishes a period. Original search period 17.575404492 d is retained only as a conditional alias, not a derived ephemeris. The full morphology overview explicitly checks features away from that alias; raw-event fits alone do not decide the result. Covered conditional phases: [{"sector": 103, "cycle": 143, "nominal_tc": 4153.2634422981155, "n_in": 68, "n_pre": 113, "n_post": 113, "covered": true, "signed_depth": -0.012590765953063965, "local_rms": 0.027302270755171776}].

2. Source and independent reduction

Fresh 11x11 TESScut images and TIC 60-arcsec cones were obtained in two sectors. Signed candidate-phase difference images and fixed-coordinate target/capable-neighbour comparisons were attempted using the original search phase. Since no real repeating eclipse exists to localize, these candidate-only fits do not establish an eclipse host or an off-target EB. They are retained as failed candidate tests, not localization detections. Capability limits use the original claimed depth and ignore aperture throughput/bandpass uncertainty.

Fresh cutout sectors: 65,103. Candidate capability counts: 65: 19,103: 19. Source comparisons are descriptive signed-image Gaussian fits, with no calibrated PRF confidence. Neighbour catalogue identity can include unresolved or duplicate records. The independent extraction subtracts each frame's lowest-30-pixel median background then sums a central 3x3 aperture, with QUALITY=0. It uses the same TESS photons through a distinct reduction, and is not SPOC. custom-morphology.png and custom-extraction.json preserve its deciding morphology.

3. Gaia orbit

Gaia NSS orbit metadata were inspected, but no photometric eclipse ephemeris was established; an eclipse/conjunction geometry comparison is therefore inapplicable. Nearness of the original search alias to the Gaia period cannot establish eclipses.

Gaia source 5984329116365907584; NSS P=17.538395407 +/- 0.010265369 d; e=0.05981, omega=247.3903 degrees. No eclipse timing or geometry is inferred from this metadata. No photometric eclipse orbit established; Gaia spectroscopic binarity not refuted.

4. Scoped prior EB coverage

no identified prior EB; coverage complete: yes. Reused centrally completed seven scopes: VSX, SIMBAD primary type, Gaia DR3 eclipsing binaries, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4, ASAS-SN. SB* and ROT alone are not EB identifications; Kostov table2 is unvetted. This is a scoped catalogue result, not an exhaustive discovery claim. Physical and novelty verdicts are separate.

5. Completion and limitations

The representative full review is complete. Scientific outcome: eclipse morphology and repetition remain unresolved; this is not a secure eclipse identification. Missing eclipse geometry reflects the absence of a valid eclipse series, not unfinished execution. Representative three QLP sectors and two independent custom-extraction sectors; no exhaustive all-sector search, calibrated PRF/noise model, physical fit or sensitivity upper limit. No secure eclipse identification or exclusion of all possible shallow eclipses follows. Repetition and eclipse morphology remain scientifically uncertain; no calibrated sensitivity or propagated ephemeris-error analysis was performed.

Next check: Obtain a well-covered predicted candidate event in a distinct reduction and establish a second coherent detached eclipse before claiming an eclipse period or host.

Provenance: raw-evidence/cache-manifest.json preserves original cache paths and SHA256; identity-checks.json verifies all 15 QLP inputs; tesscut-downloads.json stores fresh URLs and zip hashes; TIC raw cones and adapted scripts are retained. manifest.json hashes deliverables. No paper edits, commits or publication were performed.
