# Independent bounded audit

Auditor: helper, 2026-11-05. Inspected lead raw-context and difference/aperture images, not independently observed photons. Recomputed SHA-256 for all 37 source files in lead-source-hashes.json: all matched. Exact queue identities and Gaia magnitudes were checked against identity-audit.json; final central catalogue receipts remain lead/root responsibility.

Z101: S17 pixel difference is target-centered and custom aperture exhibits shallow broad depression; baseline sensitivity remains. S84 QLP features are not recovered in custom pixel aperture, so do not count them as repeats.

Z102: deep event difference is visibly offset from target; neighbor pipeline shares photons and does not establish contaminant identity. Z104: difference is overwhelmingly at the cutout edge, far from target.

Z103: three event timing receipt yields 44.25378579 d; measured windows 3 covered, 0 null, divisor 2..6 null counts 2,2,5,4,6. Shallow 6.9 ppt loss and nearby 0.008 relative G-flux source leave an unresolved capable blend despite target-favored centroid; G flux and aperture fractional loss are not equivalent.

Z105 is a known recovery; physical classification remains separate from novelty. Z106: raw S18/S58/S84 show three similar deep eclipses; S84 difference image centered near target, 0.283 pixel positive-centroid offset. 45.015846 d timing and receipt measured windows 3/0 null, divisors 2..6 null counts 5,6,11,11,19. Shallow S57/S85 events are not used as same-kind primary timings.

Z107 27.788909 d and Z108 54.971976 d: divisor-two receipts have zero nulls (one and four covered windows respectively); halves remain unresolved. Z108 close capable neighbor remains source attribution uncertainty. Coverage with failed quality or gaps is unknown rather than a null. All timing and null counts above reproduce lead receipts, not independent photometry.

Final numeric extension: Z106 shallow same-kind events 2869.1329143, 3589.3902247, 3634.4039745 yield 45.016005 d with residuals <=0.00117 d. The last two differ by 45.013750 d. Separate shallow clock rejects surviving deep-primary integer alternatives 90.0317, 72.0254, 60.0212, 36.0127 d with respective residuals 45.015, 27.008, 15.004, 9.004 d. Deep and shallow event kinds were not mixed.
