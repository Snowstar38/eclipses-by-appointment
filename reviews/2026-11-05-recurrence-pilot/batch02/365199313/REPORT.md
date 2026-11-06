# V017 TIC 365199313: PLAUSIBLE

Selected stratum: repeat_sector_dip. Bounded physical review: COMPLETE. Catalogue novelty: UNKNOWN; the independent catalogue audit is not a new-system assignment.

## Raw observations and alternative explanation

S50 shows a strong repeatable ~0.28-d waveform with narrow minima and broad maxima, 40-55 ppt in local flagged-window fits. S23 has a much weaker broad depression and a gap; no matching long-period signal is seen in the other sectors. Local minimum spacing has median 0.28472 d; the S50 QLP SAP periodogram peaks at 0.279419 d, both waveform diagnostics rather than an adopted eclipse clock. A TESSCut pixel regression at the QLP period peaks at (9,8), 1.78 pixels from the target WCS (7.22,7.96), while static target flux peaks near (7,8) and a bright column appears at x=9.

## Timing, attribution and geometry

The S50 morphology could be a short-period contact binary or a non-eclipse variable in the aperture. The offset suggests contamination but does not securely assign the variable; the independent Gaia cone returned no usable rows and is UNKNOWN rather than a nonmatch. A secure source and eclipse-kind identification are not established, so the screen cannot promote it to PROBABLE or assign the Gaia 30.81626-d SB1 as its clock.

## Limits and next check

No orbital/eclipse period, epoch or depth is adopted for the queued long-period target. The periodogram and minima spacing are approximate short-waveform diagnostics. Next: Obtain target-centered difference photometry and test alternating minima and a second sector before assigning an eclipsing source.

## Evidence

Original cached scan: `../../../binary-exploration-2026-11-04/bulk-results/365199313.json`. `screen.json` and `all-sectors.png` cover every cached sector's quality-zero finite positive raw SAP; `ranked-windows.png` shows representative context. `window-audit.json` gives actual core cadence coverage, endpoints, gaps, local side/core medians and FITS source hashes for every flagged dip. `fitted-windows.json` and `fitted-windows.png` are provisional flagged-window trapezoids, not adopted eclipse timings; singular/bound-hitting fits have no precision standing. `fold-gaia.json` and `fold-gaia.png` are diagnostic only and the three-day detrend can attenuate broad events. Where present, `short-clock.json` measures waveform minima, not verified eclipses. S94 common-time comparison is in `../cross-target.json` and `../cross-target-s94.png`. Exact target catalogue receipts are indexed at `../../novelty-audit/live/target-results.json`; catalogued *variable* status is separate from novel *binary* status. Every cached FITS was checked against its original SHA-256 and TIC header. The helper's independent pixel/source audit and its caveats are in `../HELPER-AUDIT.md`. No precision eclipse parameters or new-system claims are made.
