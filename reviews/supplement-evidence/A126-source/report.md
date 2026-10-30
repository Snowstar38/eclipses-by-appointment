# TIC 279648140 (CD-61 607): per-object vet
Opus-model subagent for Fable 5, 2026-10-18 (saved by Fable from the agent's final message; the write tool refused in-agent). Batch row: G 10.24, P 3.35025 d, 5.4 ppt, 53 events, dphi +0.021.

## Verdict: CONFIRMED (grazing EB, plus ellipsoidal variation and Doppler beaming, M-dwarf companion)

**Deciding numbers**
- **Period and conjunction:** P = 3.3502765 ± 0.0000006 d from 64 fitted events, against Gaia 3.3504026 ± 0.000058 (2.2σ). Mid-eclipse is −0.011 phase from Gaia conjunction A (companion in front) at the Gaia epoch, which is −1.9σ using the full Gaia covariance (corr(ω, t_p) = 0.9996). Conjunction B is 0.5 phase away, so it cannot be the match.
- **Secondary eclipse:** phase 0.50186 ± 0.00040, depth 710 ± 38 ppm (SNR 26), present in every season. This gives e cos ω = +0.0029 ± 0.0006, against Gaia −0.009 ± 0.015.
- **Light curve follows the orbit:** raw SAP shows an ellipsoidal wave of −6.1 ppt at P/2 in all 10 sectors. It also shows a Doppler-beaming term of +450 ppm at the correct phase and sign; Gaia's K = 41.9 km/s predicts about 560 ppm. A blend cannot do this.

**Archives**
- VSX lists only Gaia's DSCT|GDOR|SXPHE at 0″. That is a type revision to eclipsing plus ellipsoidal, not prior art.
- Kostov t2 (unvetted) is the only EB-table hit. SIMBAD has CD-61 607 [SB*] with 4 refs (RAVE ×3, Gaia multiplicity). No TOI or CTOI; web search found nothing.
- **SPOC multi-sector DV (s56–s69) has TCE_1 at P 3.3502547, 6040 ppm, SNR 75, and TCE_2 at phase 0.501, 661 ppm, SNR 11.** So a pipeline caught both eclipses before us, but nothing was published and it never became a TOI. Say so in the paper.

**Eclipses and ephemeris**
- T0 = BTJD 2829.361644 ± 0.000167. O−C rms 1.9 min, jackknife max 0.34σ. T14 = 3.42 h (constant), T12 ≈ 1.3 h, so nearly V-shaped.
- No momentum-dump cadences in any event core. Background and centroids are clean through every event, and no event falls near a listed sector-wide systematic.
- A blind phase scan finds only the primary and the secondary. Odd/even differ by 2.0σ after per-sector normalisation, which is not significant.

**Depth drop in the latest sectors**
- QLP depth falls from 6.0–6.35 ppt to 5.3–5.7 ppt in s95–97.
- The ellipsoidal amplitude (6.1 → 5.2 ppt) and the secondary (≈760 → 658 ppm) drop by the same factor in the same sectors.
- That points to extra dilution in that year's QLP processing, not a change in the eclipse.

**Independence**
- TESS-SPOC PDCSAP depth is 5.91–6.04 ppt across s3, s28, s29, s68 and s69, with timing within 1 min.
- TGLC PSF photometry in s2 gives 6.03 ± 0.24 ppt.
- The batch difference image (s97) is on target. The only neighbour brighter than G 17 is G 16.64 at 1.45″, which would need a 197% dip, so no neighbour can host the signal.

**Physics**
- f(m) = 0.0255 M☉. With M1 = 1.19, m2 = 0.40–0.42 M☉ (an early-M dwarf); a = 11.0 R☉.
- The secondary-to-primary depth ratio implies T2 ≈ 3600 K, which fits that M dwarf.
- The geometry is grazing, i ≈ 70–76°. A central transit would last 9.8 h; the observed 3.4 h only fits a grazing chord.
- **Open tension:** the ellipsoidal amplitude implies R1 ≈ 2.7 R☉, but the TIC gives 3.71 R☉, which would predict about 17 ppt instead of the observed 6.1. This does not affect the eclipse claim; a joint light-curve and RV model would resolve it.

**Changes to the paper row**
- P should be **3.3502765(6)**. The row's 3.35025 is 39σ off; that only adds up to 19 min over the baseline, but the fitted value should be quoted.
- Undiluted depth is **6.0 ppt** (the row's 5.4 is the folded box value).
- Add the secondary: 0.71 ppt at phase 0.502.
- Note the VSX type revision and the SPOC TCE.

**Next eclipses (BTJD)**
- Primary (±0.5 min): 4333.6358, 4336.9861, 4340.3363, 4343.6866.
- Secondary (±2 min): 4335.3172, 4338.6674, 4342.0177, 4345.3680.
