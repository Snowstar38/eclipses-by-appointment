# Q043 TIC 398073873: CONFIRMED

Sealed priority rank 193; repeat_sector_dip. Gaia DR3 532160780286346624, catalogue novelty UNKNOWN because four positive-control gates failed.

Five clear SAP eclipses in S18/S25/S58/S78/S79 fall at cycles 0/8/48/73/74 with local timing residuals under 0.0017 day; S78 was unflagged and supplies an odd cycle, establishing 22.429-day photometric recurrence. Nine covered P/2 windows and representative P/3, P/4 windows are flat. S18/S58 WCS losses center 0.041/0.126 pixel from the Gaia target, despite a capable G13.548 neighbor 39.022 arcsec away. TESSCut 3x3 depths 8.01/6.96 ppt independently reproduce the signal. Gaia SB1 P=22.421921±0.010315 d and target-specific conjunction geometry agree.

Limitations: Two similar eclipse kinds in a hypothetical 2P orbit are not excluded by photometry alone; the source-specific Gaia SB1 period supports P. Depth varies with extraction; the conditional period has no formal error. S59 is noisy. S78 broad-window pixel comparison was invalid and is not a null or localization. Novelty gates remain unavailable.

Next check: Obtain precision light-curve modeling and complete novelty catalogue gates before any new-system claim.

Evidence: `lead-context.json` (whole-sector raw SAP coverage, source FITS SHA256 and source packet SHA256), `lead-local-series.json`, `lead-raw-context.png`, `lead-dip-zooms.png`, and `lead-flag-diagnostics.json`. See batch `LEAD-AUDIT.md` and `helper-audit.txt` for the deciding WCS, alternate extraction, recurrence, and null checks. All computations use the hashed original files or hashed fresh TESSCut cutouts.
