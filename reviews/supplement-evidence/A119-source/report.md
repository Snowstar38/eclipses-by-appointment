# TIC 280129511: per-object vet
Opus-model subagent for Fable 5, 2026-10-18 (saved by Fable from the agent's final message; the write tool refused in-agent). Batch row: G 10.93, P 6.34879 d, 2.7 ppt, 36 events, dphi +0.022.

## Verdict: CONFIRMED, a grazing eclipsing binary of near-twin stars, with both eclipses present.

**Deciding numbers**
1. **Both eclipses, at both of Gaia's conjunctions.** In the clean QLP sectors (s18/19/52/58/59/86) the joint fits are:

   | Eclipse | Events | Depth | Duration | Δχ² vs no eclipse | Period (d) | O−C rms |
   |---|---|---|---|---|---|---|
   | I | 18 | 2.82 ppt | 2.88 h | 1921 | 6.348801 ± 0.000016 | 7.5 min |
   | II | 16 | 3.38 ppt | 3.12 h | 1744 | 6.348792 ± 0.000015 | 7.8 min |

   The timings match Gaia's predicted conjunctions to 0.7σ and about 1σ.
2. **An independent pipeline sees both.** TESS-SPOC SAP and PDCSAP in s58/59/78/79 give eclipse I at 2.4–2.9 ppt and eclipse II at 3.2–3.8 ppt in every sector. That includes s78/s79, where QLP is wrecked by background.
3. **The geometry is self-consistent.** From the Gaia double-lined orbit, the total mass × sin³i is 2.855 M☉ (mass ratio 1.02) and a sin i is 20.47 R☉.
   - Twins of about 3.1–3.6 R☉ near i ≈ 70–75° (just at the grazing limit) give about 3 ppt and about 3 h.
   - The ellipsoidal variation is 1.59 ± 0.02 ppt, with its minima locked to the eclipses.
   - Eclipse II falls at phase 0.49768 after eclipse I, giving e cos ω ≈ −0.004. Gaia predicts a separation of 0.5048, which agrees to about 1.5σ given Gaia's ±13.8° on ω.

**Location:** the batch difference image (s58) puts the flux loss 2.4″ (0.12 px) from the target, peaked on the target pixel. The three neighbours that could fake it (G 15.6, 16.1 and 16.9 at 30–42″, needing 21–67% eclipses) are excluded. Archives show nothing beyond SIMBAD's spectroscopic-binary flag.

**Row notes (none disqualifying)**
- The 6.34879 d period is right. Equal-looking eclipses could suggest the search's half period (3.17 d), but the depth difference (2.8 vs 3.4 ppt, steady in every sector) and the off-half separation rule it out.
- TESS P is 2.8σ from Gaia's 6.348166 ± 0.000223. Gaia's fit quality is poor (goodness of fit 23.5, RUWE 2.2), so its error bar is probably understated.
- The batch's 36-event count includes QLP s25/s78/s79 events that are background-dominated (one in s79 comes out at −4.6 ppt). Only the six clean sectors were used for depth and timing.

**Next predicted times (BTJD)**
- Eclipse I: 4333.442, 4339.791 (σ ≈ 0.015 d).
- Eclipse II: 4336.598, 4342.947 (σ ≈ 0.01 d).

**Would settle it further:** a two-star light-curve model of eclipses plus ellipsoidal variation, with the Gaia velocities, for masses and radii. That is not needed for the confirmation itself.
