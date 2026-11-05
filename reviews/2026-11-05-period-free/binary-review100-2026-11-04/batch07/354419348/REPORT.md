# H070 — TIC 354419348

**Verdict:** REFUTED · **Review:** COMPLETE · **Catalogue novelty:** UNKNOWN

The actual selected s59 dip flag is centered at BTJD 2912.311. Direct quality-zero SAP values are about 0.004 near BTJD 2911.827, rise to about 0.56 near the alleged dip center, and continue toward 0.99 by BTJD 2914.142. Thus the flag lies on a monotonic recovery from near-zero extracted target flux, not at a local flux minimum. The two plotted s59 brightening flags are other slices of this recovery pattern.

The automated representative-window script omitted the exact dip panel because its side-sample requirement failed, so the direct FITS sequence and bulk flag receipt are decisive here. The s59 SAP_BKG and centroid positions evolve strongly during recovery. A zero or near-zero cutout/extraction flux cannot be treated as a sensitive eclipse null.

**Coverage and limits.** Hash-verified raw QLP SAP_FLUX, QUALITY=0, covers s17 (1766.2–1788.5), s19 (1816.9–1840.9), s24 (1955.9–1982.2), s25 (1984.0–2009.0), s52 (2720.3–2743.0), s58 (2882.4–2910.0), s59 (2911.8–2936.7), s73 (3285.8–3312.6), s78 (3434.3–3449.5), s79 (3452.5–3479.6), s85 (3610.6–3636.0), s86 (3636.5–3662.8) BTJD. The original s59 dip is positively contradicted by its rising raw flux and unstable extraction. The four shared VizieR novelty gates remain unqueried/unknown; a primary-table nonmatch is not novelty clearance.

**Next check.** Reassess only a complete target-centred event with positive stable flux and local baseline.

Evidence: [raw window numbers](raw-inspection.json), [raw panels](raw-windows.png), [full-sector and Gaia-prediction context](orbit-context.png), [alternate channels and pointing/background](qlp-alternate.png), [source hashes and original flags](source-receipt.json). The Gaia spectroscopic period is 45.131600 d, not a photometrically measured period here.
