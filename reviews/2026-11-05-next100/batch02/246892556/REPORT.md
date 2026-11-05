# Q011 — TIC 246892556

**Physical verdict: PROBABLE.** Bounded review of the selected eclipse claim; full review completion: COMPLETE. **Novelty: UNKNOWN.** The exact-queue shared catalogue leaves VSX, ASAS-SN, and Kostov table 3/4 gates unavailable; prior nonmatches cannot establish novelty.

## Evidence

Seven narrow raw SAP losses in S29 and S69 have measured minima at 2089.5918, 2096.1545, 2109.2588, 3184.6399, 3191.2002, 3197.7466, and 3204.3092 BTJD. Local raw depths are 6.3–6.8 ppt. The sequence fits a 6.557-day photometric spacing with 5.75-minute residual RMS. A separate fixed 3×3 sky-subtracted WCS aperture recovers 3.7–5.2 ppt losses at all seven occasions. The three fully sampled extra windows at half that spacing, 2092.8707, 2105.9851, and 3201.0311, have local SAP losses +0.11, −0.17, and +0.14 ppt against about 6.5 ppt events; their core counts are 17, 15, and 44.

Real repeated eclipse-like losses are strongly supported. The 6.557-day interval is a photometric step; equal-depth alternating kinds allow a 13.114-day orbital period. Gaia SB2 P=35.673188 d does not provide source-specific conjunction timing for these losses. WCS difference peaks lie close to the target, but Gaia DR3 2319058524800146688 (G=15.02) is only 21.74 arcsec away and has enough approximate G flux for a deep blended eclipse. Target attribution and orbital geometry are unresolved.

## Limits and next check

Orbital period, eclipse kind, target ownership, and compatibility with the Gaia SB2 orbit are unresolved; no precision period or primary epoch is adopted.

Obtain resolved photometry or source-specific PSF difference fitting for the 21.74-arcsec neighbor, then test 6.557 versus 13.114 d and conjunction geometry.

## Reproducibility

`lead-inventory.json` records the actual quality-zero, finite positive SAP ranges, >0.2-day gaps, retained windows, source paths and SHA256 hashes. `lead-raw-overview.png` shows every cached sector. `lead-review.json` records this bounded interpretation and packet hash. The batch scripts reproduce raw overviews and the Q011/Q015 deciding checks. `lead-q011-clock.json`, `lead-q011-event-zooms.png`, `cutouts/lead-pixel-evidence.json`, `cutouts/lead-alt-evidence.json`, and the helper Gaia cone receipt record measured recurrence, tested null coverage, alternative extraction and capable neighbor.
