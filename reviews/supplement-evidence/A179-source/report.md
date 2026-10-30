# TIC 384284045 (TYC 3616-2395-1, Gaia DR3 1980920834829359488): per-object vet

Opus 5.5 subagent, wave 5, 2026-10-21. Fresh folder; every number below comes from a file in it:
- Outputs: `vet-out.txt`, `ecl2-out.txt`, `sec2-out.txt`, `bkgreg-out.txt`, `indep-out.txt`, `indep2-out.txt`, `tpfdiff-out.txt`, `geom-out.txt`, `dips-out.txt`.
- Archive and query outputs: `gaiatap-out.txt`, `cats-out.txt`, `morecats-out.txt`, `extracats-out.txt`, `mastlc-*.txt`.
- Downloads, including the SPOC DV xml: `C:\Home\sky\data\qlp-sb-p20-60\pervet384284045\`. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## Verdict: CONFIRMED. A grazing, circular, near-twin G-type eclipsing **SB2**; both eclipses detected and both match Gaia's conjunctions.

Deciding numbers:
- **Two eclipses of similar depth, each fixed to one Gaia conjunction:**
  - The deeper one is **28.89 ± 0.06 ppt** (34 events) and falls at Gaia conjunction **B**, at −1.6σ in every sector.
  - The shallower one is **25.58 ± 0.05 ppt** (37 events) and falls at conjunction A.
  - Their phase separation is **0.50002 ± 0.00002**, against Gaia's predicted 0.5000 ± 0.0041.
  - The search's "P2" half-period alias (1.8935 d) came from these two near-equal eclipses. The batch period of 3.787 d is the right one.
- **Period:** 3.7870110 ± 0.0000007 d (mean of the two kinds), against Gaia's 3.787087 ± 0.000049 d. That is −1.5σ, which is also why the conjunction offset is −1.6σ.
- **Which star is which:** the RVs and the photometry agree independently.
  - Gaia's K1 (91.47) is larger than K2 (85.31), so Gaia's "primary" is the *less* massive star (q = 0.933).
  - The eclipse at A, where Gaia's primary is eclipsed, is the *shallower* one. Its depth ratio of 0.886 means that star has the lower surface brightness, about 200–250 K cooler.
  - So the more massive star is the hotter one, as it should be on the main sequence. Gaia's SB2 "primary" label went to the cooler star of a near-equal pair. That is a labelling note, not a conflict.
- **On target:** difference images (2-min SPOC s57, TESS-SPOC s76 and s83) put the flux loss on or adjacent to the target pixel at S/N 87–112.
  - The target beats every neighbour by Δχ² > 21,000.
  - The best neighbour, G 13.72, would need a 58% dip.
- **Prior detection (not a catalogue entry):** SPOC 2-min **s57 TCE** (DV `s0057-s0057`).
  - Found at the half period: P 1.893481 d, epoch 2855.1687, depth 26,927 ± 141 ppm, 2.31 h, b 0.95, "Rp" 36 R⊕.
  - Its odd/even depth statistic is **246**: SPOC saw the alternating depths.
  - It is not a TOI or CTOI.

## 1. Archives
- **cats.py --r 60** (APPOINTMENTS_DATA set):
  - VSX has only Gaia DR3 1980920078927243648 at 49.8″ (G 16.54, type S, 16.30–16.89 mag) — a neighbour, not the target; see §4.
  - ASAS-SN: none. Prša+2022, IJspeert+2024 and Kostov+2025: none.
  - SIMBAD has TYC 3616-2395-1, typed [SB*].
- **Gaia DR3 TAP:** vari_summary and vari_eclipsing_binary empty. RUWE 0.79. gspphot Teff 5744 K, logg 4.08. NSS flags 8388608.
- **SB9, WDS and J/AJ/160/111:** no entry.
- **ExoFOP:** no TOI, CTOI, imaging, spectroscopy or companions.
- **Extra VizieR cones at 30″:**
  - **2RXS J215010.4+514807** lies 8.6″ away with a positional error of 9.9″, so it is consistent with the target. That fits an active, tidally synchronized binary (§5).
  - The ATLAS row at 27″ is a G ≈ 17.6 "dubious" star, not the target.
  - ZTF, WISE, GCVS, VSX, ROSAT bright, 4XMM, ASAS-SN, LAMOST, APOGEE and Prša return nothing.
  - J/A+A/674/A16 is a Gaia source table, not an EB classification.
- **Web search** on "TYC 3616-2395-1" and "TIC 384284045": nothing relevant.
- **Gaia orbit:** SB2, P 3.787087(49) d, e 0.0025(81), ω 91(166)°, K1 91.47(91) km/s, K2 85.31 km/s, significance 100.
- **TIC** (treats the pair as one star): Teff 5776 K, R 1.47 R☉, M 1.04 M☉, L 2.18 L☉, d 207 pc, contratio 0.092.
- **Batch receipts:** c3-vetsum P2-tagged, dphi +0.488/−0.012 ATTR; diffrun s083 peak on target, deficit−target 4.3″, deficit−light 1.57″; c3-sapdepth alternating ~24/~28 ppt.

## 2. Eclipse measurements (QLP SAP, QUALITY==0, untrimmed; 6 sectors s056–s084, 200 s cadence)
- **Global trapezoid** (deeper eclipse): 28.6 ppt, T14 2.22 h, T12 0.89 h, flat bottom 0.44 h. A box shape is worse by Δχ² +1729 — V-like, grazing.
- **Deeper eclipse, conjunction B** (`ecl2-out.txt`): 28.89 ± 0.06 ppt, 34 events, χ²/dof 181/33. Per-sector means 27.8–29.3 ppt (s056 lowest). Odd 28.93 ± 0.07 and even 28.74 ± 0.07 ppt.
- **Shallower eclipse, conjunction A:** 25.58 ± 0.05 ppt, 37 events, χ²/dof 169/36.
- **Fold with harmonics** (`sec2-out.txt`): 28.9 ppt / 2.20 h and 25.5 ppt / 2.24 h. The equal durations again point to e sin ω ≈ 0.
- **Background:** |ΔF| ≤ 0.06 ppt in every sector, against a 17 ppt dip in the same windows.
- **Centroids:** dX +0.27 ± 0.08 mpix, dY −0.69 ± 0.05 mpix — negligible.
- **Quality flags and systematics:** one event has a bit-32 cadence, depth normal. No event near a listed sector-wide systematic; s083 does not touch 3564.5.
- **Control phases:** |depth| ≤ 0.17 ppt.
- **Blind dip census:** 87 dips at S/N ≥ 4; 36 on the deeper ephemeris and 36 are the other eclipse at phase ±0.500. The rest are not real:
  - 2845.86 (15.9 ppt, phase 0.041) is the baseline just after an eclipse, next to a bit-32 cadence. SAP inside the window is −2 ppt, and the same phase in other cycles is *brighter*.
  - The remaining dips are 1.5–2 ppt features in s084, the noisiest sector at 8.9 ppt rms.
- **Starspots:** the orbital-period cos φ and sin φ terms vary by ±6–15 ppt from sector to sector in both QLP and SPOC. This is spot modulation on synchronized G stars, consistent with the 2RXS detection. Spots also explain the depth-constancy χ² and s056's lower depth and A/B ratio.

## 3. Ephemerides (`ecl2-out.txt`; events with S/N > 3; the 5σ clip removed nothing)

| kind | P (d) | T0 (BTJD) | n | χ²/dof (scale) | O−C rms |
|---|---|---|---|---|---|
| deeper (conj. B) | 3.7870109 ± 0.0000007 | 3277.42043 ± 0.00006 | 34 | 227/32 (×2.67) | 0.59 min (median error 0.29 min) |
| shallower (conj. A) | 3.7870141 ± 0.0000007 | 3290.67506 ± 0.00006 | 37 | 180/35 (×2.27) | 0.46 min (median error 0.29 min) |

- **Period difference:** P(A) − P(B) = +0.27 s per cycle, +3.0σ. With e ≈ 0 this is not apsidal motion; the most likely cause is spot-induced timing noise, anti-correlated between the two kinds, going with the χ² excess. Worth a look if anyone revisits.
- **Phase separation:** 0.50002 ± 0.00002, so e cos ω = +0.00004 ± 0.00004. For twins the light-travel delay is about 0.
- **Comparison with Gaia** (Monte Carlo with corr_vec): the deeper eclipse is −1.23 h (s056) to −1.63 h (s084) from conjunction B, all −1.58σ to −1.62σ. Conjunction A is 43–56σ away from it. The drift between sectors is Gaia's P being 1.5σ long.

## 4. Independence
- **Other pipelines:** TESS-SPOC PDCSAP at the deeper eclipse gives 27.8–29.6 ppt in all six sectors; SPOC-SAP 25.2–27.6 ppt. The **SPOC 2-min s57** light curve gives 29.03 / 25.14 ppt. With both kinds in PDCSAP (`indep2-out.txt`), the A/B depth ratio is **0.87–0.90** in s057, s076, s077, s083 and s084, and 0.96 in the spotty s056.
- **SPOC DV** (s57): difference-image centroid offset from the TIC position 1.72 ± 2.50″.
- **Difference images** (`tpfdiff-out.txt`):

  | sector | max-loss pixel | S/N | χ² target | χ² best neighbour |
  |---|---|---|---|---|
  | s057 (2-min) | (4,5), next to target | 112 | 3975 | 31,584 |
  | s076 | target (5,5) | 87 | 3695 | 25,039 |
  | s083 | (5,6), adjacent | 105 | 8182 | 42,694 |

  The target's implied own dip is 21.5–23.1 ppt. The s083 fit overrides the batch's 4.3″ deficit−target figure: the target beats every neighbour by Δχ² 34,500 there.
- **Neighbour dilution table** (needed dip = 28.9 ppt × 10^(0.4ΔG); 24 Gaia sources with G < 17 within 90″): G 13.72 at 45.3″ → 577 ppt; G 13.83 at 57.7″ → 640 ppt; G 14.31 at 43.4″ → 0.99 (impossible); G 15.84 at 33.1″ → >1 (impossible); the VSX "S" star G 16.54 at 49.8″ → 7.8 (impossible). The difference images exclude every one.

## 5. Physics (`geom-out.txt`)
- **Masses from the SB2 solution:** M_A sin³i = 1.046 M☉ (Gaia "primary") and M_B sin³i = 1.122 M☉. a sin i = 13.23 R☉. At the fitted i ≈ 82.6–83.0°, **M_A ≈ 1.07 and M_B ≈ 1.15 M☉** — two early-G or late-F dwarfs. Their summed luminosity of ~2 L☉ matches TIC's single-star 2.18 L☉, and the single-star-equivalent R of 1.47 ≈ √2 × 1.04 R☉.
- **One geometry fits both eclipses:** two limb-darkened spheres, circular orbit, masses from the SB2 solution at each i → 28.9 ppt at B and 25.3 ppt at A, both ~2.26 h (χ² ≈ 1.3). Fitted: R_A ≈ R_B ≈ 0.95–1.05 R☉, **T_B − T_A ≈ 200–250 K**, i 82.6°, b ≈ 1.7 R☉ — a graze (a central chord would last ~4.8 h). SPOC DV independently gives b 0.95, radius ratio 0.23 in its planet model.
- **Which star is in front:** at conjunction A, star B (more massive, hotter) passes in front of star A, giving the shallower eclipse; at B the reverse. RVs and photometry agree.
- **Activity:** a 3.79-d synchronized pair of G dwarfs is expected to be spotted and X-ray bright. 2RXS and the ±10 ppt sector-to-sector rotational wave both bear this out (RS CVn / BY Dra-like).
- **Not a heartbeat:** e ≈ 0, short sharp eclipses at both conjunctions.

## Row fixes for the paper table

| field | batch | fix |
|---|---|---|
| P (d) | 3.787032 (P2-resolved) | **3.787011 ± 0.000002** (the two kinds give 3.7870109 and 3.7870141) |
| T0 (BTJD) | 2826.7648 | **3277.42043 ± 0.00006** (deeper eclipse, conjunction B) |
| depth (ppt) | 25.2 | **28.89 ± 0.06** (deeper) / **25.58 ± 0.05** (shallower); SPOC PDCSAP 27.8–29.6 / 25.1–26.5 |
| T14 (h) | 1.2 (search box) | **2.20 / 2.24** (grazing, T12/T14 0.40) |
| n events | 71 | 34 deeper + 37 shallower (Q0, all fitted) |
| dphi | +0.488 / −0.012 | the deeper eclipse is on **conjunction B** at −1.6σ; Gaia's "primary" is the cooler, less massive star |
| secondary | — | 25.58 ppt at phase 0.50002 ± 0.00002 (e cos ω ≈ 0) |
| prior art | — | **SPOC 2-min s57 TCE** at P/2 (26.9 ppt, odd/even statistic 246); not a TOI; 2RXS X-ray counterpart; not in any EB catalogue |
| note | — | spotted (RS CVn/BY Dra-like); spot timing noise gives an O−C χ² excess of about ×2.5 |

## Next predicted eclipses (BTJD)
- **Deeper eclipse** (conjunction B, hotter and more massive star eclipsed): **4402.1627, 4405.9497, 4409.7367**, then every 3.787011 d.
- **Shallower eclipse** (conjunction A): **4400.2702, 4404.0572, 4407.8442**.
- Formal error ±0.3 min. Allow ±3 min, because of the +0.27 s per cycle difference between the two kinds and spot timing noise.

## What would settle it further
Already settled as an eclipsing SB2. Two follow-ups would add value:
- A ground RV and light-curve joint fit would give full model-independent masses and radii to ~1–2%. It is a bright (V 10.5) double-lined G+G graze.
- A spot-modelled eclipse-timing analysis would test whether the 3σ period difference between the two kinds is spot noise.
