# TIC 453601725 — per-object vet (pervet wave 6, Opus subagent, 2026-10-21)

(Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

**Verdict: CONFIRMED** — a detached, partially eclipsing near-twin solar-type SB2 (Gaia DR3 5871568499564025472, TYC 8675-1668-1), P = 5.566684 d. Both eclipses are present, and each one lands on its own Gaia RV conjunction. The source is on target in two independent pipelines and in the TESS-SPOC pixels.

Batch row: 28.1 ppt, G 10.88, P 5.56669 d, 22 events, dphi −0.007, diffimg 0.72″.

## Row fixes
| field | batch | this vet |
|---|---|---|
| P | 5.56669 | **5.5666840 ± 0.0000021 d** (pri). Sec: 5.5666831 ± 0.0000022. Gaia: 5.566740 ± 0.000155 (−0.37σ) |
| T0 (pri) | 1605.6571 | **3765.53158 ± 0.00026 BTJD**. Sec T0 3790.66947 ± 0.00028 |
| depth | 28.1 ppt | QLP SAP: **pri 30.4 ± 0.1, sec 29.4 ± 0.1 ppt** (sector-dependent dilution, 27.4–34.6). Undiluted (TESS-SPOC PDCSAP s11+s38): **pri ~36.3, sec ~35.2 ppt** |
| event count | 22 | **25 pri + 27 sec = 52**. s011 (30-min) adds 3 pri; the batch counted only one kind |
| dphi | −0.007 | **pri −0.0075 to −0.013 phase vs Gaia conj A** (−0.74 to −1.22σ). **Sec −0.001 phase vs conj B** (s065, ~−0.1σ). The sign is correct |
| sec phase | — | 0.51577 ± 0.00007 → e cos ω = +0.0248 |

## 1. Archives and web
- `cats.py --r 60` (`APPOINTMENTS_DATA` set):
  - VSX lists the target itself as **ROT**, with Gaia DR3 as the source. That is a type revision, not prior art: Gaia's classifier called the eclipses rotation. There is also a ROT neighbour at 57″, G 16.20.
  - ASAS-SN: none.
  - SIMBAD: TYC 8675-1668-1 [SB*] at 0.0″.
- Batch sweeps (c3/c4 ebcats): "none of the vetted/unvetted EB tables". That covers Prša+2022, IJspeert+2024 and Kostov.
- Gaia DR3 TAP:
  - NSS **SB2**: P 5.566740(155), e 0.0136(97), ω 39(36)°, K1 77.87(87), K2 76.03, γ −17.0, gof 1.57, significance 89.9.
  - vari_summary row exists (in_vari_classification_result true), but in_vari_eclipsing_binary is false and vari_eclipsing_binary is empty.
  - RUWE 0.91, ipd_frac_multi_peak 0.
- SB9, WDS, J/AJ/160/111 (VizieR): none.
- ExoFOP json: HTTP 503 twice, so not checked tonight. The batch TOI/CTOI sweep found nothing.
- Web search on "TYC 8675-1668-1" / "TIC 453601725": no paper names the star.
- **No prior eclipse claim found.** The only catalogue entry is Gaia's ROT classification.

## 2. Eclipse measurements (QLP SAP_FLUX, Q==0, no trimming)
Scripts: `vet.py`, `ecl2.py`, `persector.py`.
- **Global trapezoid:** depth 31.1 ppt, T14 2.58 h, T12 1.03 h. A V shape fits badly: Δχ² +11317 at T12/T14 = 0.1.
- **Per event:** all 25 primaries and 27 secondaries have S/N 40–136.
  - Odd/even primary: 30.59 / 30.31 ppt.
  - Only 2 events have any bit-32 cadence in the window.
  - None is within 0.5 d of a listed sector-wide systematic.
- **Background:** the in–out excursion is −2 e⁻/s (−0.2 ppt equivalent), where a fake eclipse would need +306 e⁻/s. The ecl2 dBKG(rel) column has the known broken units and is not used.
- **Centroids:** dX +0.17 ± 0.12 mpix, dY +0.10 ± 0.17 mpix, both null.
- **Control phases** 0.125–0.875 are null (|d| < 0.11 ppt). The exception is 0.500, at −9 ppt, which is the wing of the secondary at 0.516.
- **Blind dip census:** 51 dips with S/N ≥ 4. 25 are the primaries and the other 26 are all the secondary (phase −0.484). Nothing else is in the data.
- **Depth vs sector:** the QLP depth drifts from 34.6 (s065) to 27.4 (s102), with χ²/dof 1355/24. **T14 stays constant** at 2.50–2.64 h in free per-sector fits, for both kinds.
  - The sec/pri ratio is also stable: 0.93–0.99.
  - So the drift is aperture dilution, not a change in inclination. QLP has no crowding correction, while TESS-SPOC PDCSAP gives 36–37 ppt.

## 3. Ephemeris, O−C and comparison with Gaia
- **Per kind:**
  - pri: P 5.5666840(21), O−C rms 1.80 min.
  - sec: P 5.5666831(22), O−C rms 1.89 min.
  - P(sec) − P(pri) = −0.08 s (−0.3σ), so no apsidal motion is visible.
- **Gaia conjunctions:** Monte Carlo with this star's own corr_vec, through `vetlib.gaia_draws`.
  - The primary sits at **conj A**, −0.74 to −1.22σ across the seven sectors.
  - The secondary sits at **conj B**, ~−0.1σ.
  - Gaia predicts phase(B) − phase(A) = 0.5054 ± 0.0053; measured 0.51577 ± 0.00007, a 1.96σ difference.
- **e cos ω:** the eclipse value is +0.0248. Gaia gives +0.0085 ± 0.0083, a 1.9σ difference in the *more*-eccentric direction (like 1260529 and 191146789).
- **e sin ω:** `geom.py` (two limb-darkened spheres, numerical overlap, e cos ω fixed at +0.0248) gives **+0.005 to +0.010** as the only acceptable range.
  - Best χ² by e sin ω: 0.5 at +0.010, 5.1 at 0, 77 at +0.015.
  - Gaia: +0.0071 ± 0.0087, so it agrees.
  - Combined: eclipse e ≈ 0.026, ω ≈ 17°, against Gaia e 0.0136(97) (1.2σ) and ω 39(36)° (0.6σ). Consistent.
- **Common-mode ETV (open):**
  - Both kinds show the *same* O−C pattern inside s099–s102: about +2.5…+3 min at s099, falling to −3…−3.7 min at s102, a swing of ~6 min in ~100 d.
  - s011–s065 sit near 0. TARS and TESS-SPOC reproduce s011/s038/s065, but s099–s102 are QLP-only.
  - Apsidal motion and spots would anti-correlate the two kinds; this does not. It could be light-travel time from a third body or a QLP timing or systematic effect in those sectors.
  - It does not affect the verdict. Flagged for follow-up, in the same family as 324273420's common-mode ETV.

## 4. Independence
- **Second pipelines** (`persector.py`; both kinds in every file):
  - TESS-SPOC PDCSAP: s11 pri 37.3 / sec 34.4, s38 35.7 / 35.7 ppt.
  - CDIPS IRM1: s11 43.3 / 40.9, s38 37.5 / 37.2.
  - TARS: s11 33.9 / 31.3, s38 30.8 / 31.8, s65 33.2 / 31.9.
  - In every pipeline T14 is 2.50–2.64 h and the timing agrees within 1.4 min.
  - Also at MAST but not downloaded: GSFC-ELEANOR-LITE, PATHOS and TGLC (s11).
- **TESS-SPOC difference images** (`tpfdiff.py`):
  - s38: 5 events, peak loss in the target pixel at S/N 40.6. The target PSF fits with χ² 1593, against 6319 for the next-best star (G 13.99 at 27.7″).
  - s11: 1 event, S/N 60.9, χ² 1429 vs 6583.
  - The batch diffimg for s65 has deficit−light 0.26″ and deficit−target 0.72″, peak on target. Clean.
- **Neighbour dilution:** dip each neighbour would need to make the 30 ppt seen in QLP.
  - G 13.99 at 27.7″: ×17.6 → **53%** (and the tpfdiff fit wants 106–120 ppt of it).
  - G 14.49 at 47.5″: ×27.6 → 84%.
  - G 15.19 at 26.3″: ×53 → impossible.
  - G 15.70 at 13.8″: ×85 → impossible.
  - Every fainter star is impossible. None survives the pixel test.

## 5. Physics
- **Masses:** Gaia's K1/K2 give M_A sin³i 1.039 and M_B sin³i 1.064 M☉, with q = M_A/M_B = 0.976 and a sin i 16.93 R☉.
- **Geometry** (`geom.py`, best solutions):
  - i ≈ 84.0–85.0°, so M_A ≈ 1.05 and M_B ≈ 1.08 M☉, a ≈ 17.0 R☉.
  - R ≈ 0.9–1.05 R☉ each, which fits the TIC combined radius of 1.40 ≈ √2 × 1.0. Teff 5900–6000 K each (TIC combined 6093).
  - Both eclipses are **partial**: a cos i ≈ 1.5–1.8 R☉ against R_A + R_B ≈ 2. The trapezoid's 0.52-h "flat" is not totality.
- **Which star is in front:**
  - Gaia's primary (star A, higher K, slightly lower mass) is eclipsed at conj A, the deeper eclipse.
  - Star B is eclipsed at conj B.
  - The depth difference (B/A = 0.966) and duration ratio (0.982) are explained by e sin ω ≈ +0.0075 (a smaller impact parameter at A) with T_A ≤ T_B, rather than by a hotter low-mass star.
- **Consistency:** with ~50/50 light, the undiluted depths of ~36/35 ppt and the 2.6-h durations all fit one geometry. Nothing needs third light beyond what PDCSAP already removes.

## 6. Verdict
**CONFIRMED.** The deciding numbers:
- 52 eclipses of both kinds, each at S/N 40–136, with zero events unexplained in the blind census.
- P agrees with Gaia's SB2 RV period to −0.37σ.
- The primary is at Gaia conj A (≤1.2σ) and the secondary at conj B (~0.1σ).
- e sin ω from geometry (+0.005…+0.010) matches Gaia's +0.0071. e cos ω is in 1.9σ tension in the eccentric direction, which is soft below e ~ 0.05.
- The difference image is on target (Δχ² ≈ 4700–5150 against the best neighbour). The only plausible neighbour would need a 53% dip.
- Depth and timing are reproduced by TESS-SPOC, CDIPS and TARS.

**Next predicted eclipses (BTJD; formal ±0.5 min, but allow ±5 min given the ETV):**
- Primary (conj A): **4400.1336, 4405.7002, 4411.2669**
- Secondary (conj B): **4403.0046, 4408.5713, 4414.1380**

**What would settle it further:**
- Fresh TESS sectors, or ground timings, to test whether the ~6-min common-mode ETV is real (a third body via LTTE) or a QLP systematic.
- An independent light curve for s099–s102: TESScut photometry or TGLC.
- A joint RV + light-curve fit to sharpen e and ω.

## Files
All in `C:\Home\Fable 5\made\sb1-scale\pervet\vet453601725\`:
- Outputs: `vet-out.txt`, `vet-results.json`, `ecl2-out.txt`, `persector-out.txt`/`.json`, `geom-out.txt`, `gaiatap-out.txt`, `gaia.json`, `cats-out.txt`, `morecats-out.txt`, `mastlc-list.txt`, `mastlc-dl.txt`.
- Figures: `events.png`, `fold_oc.png`, `tpfdiff_11.png`, `tpfdiff_38.png`.
- Downloads: `C:\Home\sky\data\qlp-sb-p20-60\vet453601725\`.
