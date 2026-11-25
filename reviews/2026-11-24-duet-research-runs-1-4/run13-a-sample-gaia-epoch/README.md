# Run 13: Gaia's correlated errors tested on the paper's own sample; the wide windows were needed; R729, GD1 and GD2

Duet (Claude), scheduled research run 13, 2026 November 25, on main at `64fbde89` (with runs 11 and 12 unpacked beside it; this run imports only run 4's `window_covariance.py`). Python 3 with pandas and NumPy (no SciPy needed). Run from the repository root:

```
D=reviews/2026-11-24-duet-research-runs-1-4/run13-a-sample-gaia-epoch
python3 $D/a_epoch_test.py > $D/a-epoch-test-output.txt
python3 $D/r729_epoch.py   > $D/r729-epoch-output.txt
python3 $D/r_tension_vs_a.py > $D/r-tension-vs-a-output.txt     # needs run 12's gaia-epoch-test.csv
python3 $D/search_window_budget.py > $D/search-window-budget-output.txt
python3 $D/sb1_vs_sb2_periods.py > $D/sb1-vs-sb2-periods-output.txt
python3 $D/gd_fold.py <folder with Fable 5.1's GD1/GD2 CSVs> <its gaia-orbits.csv> > $D/gd-fold-output.txt
```

Inputs: Fable 5.1's `fable51-nss-appointments.csv` (Gaia NSS rows with `corr_vec` for the A labels, on main), the paper's own ephemeris and discovery-method tables in `paper.html` (CHECKCARD.csv as fallback), Fable 5.1's R729 event times (copied here as `r729-events-fable51.csv`) and Fable 5.1's GD1/GD2 light curves (house folder `Duet\2026-11-25-fable51-gd1-gd2-windows-nss\`; not copied into the repo, 2.3 MB). The GD fold expects them named `GDn_sNNN_qlp.csv`.

## 13a. Gaia's conjunction errors, tested on the appointment sample itself

[`a_epoch_test.py`](a_epoch_test.py), output [`a-epoch-test-output.txt`](a-epoch-test-output.txt), table [`a-epoch-test.csv`](a-epoch-test.csv).

Runs 4, 11 and 12 calibrated Gaia's errors on R systems, whose tiers partly depended on agreeing with Gaia (run 12a). With Fable 5.1's export the same test can now be run on the paper's own A sample: 188 A systems have an SB1 or SB2 orbit with `corr_vec`; 184 have an eclipse period within 2% of Gaia's (the four others are A9 and A54, Table 4's wrong and spurious periods, and the by-catch A45 and A46). For each, the eclipse ephemeris is carried back to Gaia's epoch and compared with the nearer predicted conjunction, with the conjunction-time σ propagated through `corr_vec` and, for comparison, with independent errors.

- **Check.** The code gives A167's primary 0.123 d (2.95 h) after conjunction A at Gaia's epoch; the paper says 2.9 h.
- **At Gaia's own epoch** the offsets in full-covariance σ have robust width **1.66** (SB1 1.54, SB2 2.95), and 20 of 184 are 3σ or more. For the 104 systems not found through the windows (Batch, Fold, MD, Ast), which are not selected on Gaia agreement at all, the width is 1.48 (SB1 alone 1.31). With independent errors the width is 0.21: those errors are about five times too big here, the published correlations about 1.3 to 1.7 times too small (about 3 for SB2s).
- **At the eclipse epoch** (Gaia's ephemeris carried forward, where the period term dominates) the width is 1.26 with the covariance (1.16 for the non-App systems) and 0.57 with independent errors.
- **The paper's three uncounted conjunction offsets.** With the published `corr_vec`: A87 −4.8σ, A89 +6.3σ, A104 +8.2σ at Gaia's epoch, but −0.4σ, +3.4σ and +0.2σ at the eclipse epoch. At Gaia's epoch one A system in nine is 3σ off with the covariance, so a conjunction offset by itself is weak evidence against an orbit. This backs the paper's decision not to count them, and gives the reason in a number.
- **A29** (already in Table 4 for its period) also fails at Gaia's own epoch: its eclipse at conjunction B is 1.67 d (0.056 in phase, 32σ) from Gaia's prediction, so for A29, unlike A147 and A167, the orbit's geometry is off as well as its period. This could go in its Table 4 row ("and its conjunction B misses by 1.7 d at Gaia's epoch").

## 13b. The wide windows were a safety margin, not only a cost

Same script, table [`a-window-coverage.csv`](a-window-coverage.csv).

The Methods paragraph (Section 2.2) says the search's independent draws made the windows wider than Gaia allows (median half-width 6.1 d against 3.5 d with the correlations) "which costs sensitivity rather than correctness". I tested this on the systems we actually found, with windows min(max(kσ, 0.25 d), 7 d) at each system's eclipse epoch:

| Window | Median half-width | Found eclipses outside, all 184 | App (80) | Other methods (104) |
|---|---:|---:|---:|---:|
| 3σ, independent (the search) | 1.76 d | 2 (A12, A147) | 0 | 2 |
| 3σ, `corr_vec` | 0.64 d | 11 | 6 (A28, A33, A43, A52, A110, A117) | 5 (A12, A86, A89, A147, A167) |
| 4.5σ, `corr_vec` | 0.97 d | 5 (A12, A28, A110, A147, A167) | 2 | 3 |
| 6σ, `corr_vec` | 1.29 d | 0 | 0 | 0 |

- Built from the published correlations at 3σ, the windows would have excluded **11 of the 184 real eclipses, 7 of them Table 4's contradicted orbits** (A12, A28, A52, A86, A110, A147, A167). The systems the narrower windows lose are exactly the ones where Gaia is wrong, which are among the paper's most interesting results. The App column is biased (those were found inside the independent windows), but the other-method column is not, and it loses 5 of 104.
- Even the search's own windows miss 2 of 104 eclipses found by other means (A12 and A147, both Gaia period failures), so the appointment method's completeness is about 98% against Gaia's period errors, not 99.7%.
- A 6σ window with the correlations would have contained all 184 and is still smaller in total (797 window-days against 924 for the search's 3σ independent windows).
- **For the 20–60 d search itself** ([`search_window_budget.py`](search_window_budget.py), output [`search-window-budget-output.txt`](search-window-budget-output.txt), from Fable 5.1's half-width table at mid-mission, where the period term dominates): 3σ with the correlations would be 79% of the search's total window time, 4.5σ 97%, 6σ 108%. So the search's windows were in effect about a 4.5–6σ correlated window: about as wide as Gaia's real errors need, not twice too wide. The sensitivity cost the Methods sentence describes is close to nothing against a window that would have kept every system.
- **Suggested replacement for the clause in Section 2.2.** "…and the windows were wider than the published correlations alone would give (median half-width 6.1 d against 3.5 d). That margin mattered: Gaia's correlated conjunction errors are about 1.2–1.7 times too small for these systems, and 3σ windows built from them would have excluded 11 of the 184 eclipses found, 7 of them orbits in Table 4. The search's windows correspond to about 4.5–6σ with the correlations, which contains all 184."
- This also corrects my own run 4 finding 4, which on R systems read the windows as about twice as wide as needed. The core of the distribution says that; the tails, which are where the Gaia contradictions live, do not.

## 13c. R729 with Fable 5.1's event times: not the R716 pattern

[`r729_epoch.py`](r729_epoch.py), output [`r729-epoch-output.txt`](r729-epoch-output.txt).

Run 12 could not test R729 (no event times in the repo). With Fable 5.1's seven QLP times, a joint fit gives P = 35.2356 ± 0.0033 d (Gaia's SB2 35.3747 ± 0.0041, 30σ), with the second family 0.191 ± 0.003 in phase before the deep one.

- Carried back 38 cycles, the deep eclipse lands 2.19 d after Gaia's conjunction A and the other 1.42 d before conjunction B (0.06 and 0.04 in phase; 16σ and 7σ even with the ephemeris error included). That is not on Gaia's conjunctions in the sense of R716, R752, R787 and R789 (1 to 5 h).
- Gaia's e and ω put conjunction B 0.092 ± 0.006 before A; the eclipses are 0.191 apart. Only a very eccentric orbit can do that: e ≥ 0.50 at any ω. Gaia's e = 0.747 is in that range, but would need ω ≈ 58° against Gaia's 27.8 ± 1.8°.
- So the eclipses need an orbit as eccentric as Gaia's, which fits the association, but Gaia's period, ω and conjunction times are all far off. R729 stays undecided, and the R reviewers' "association unresolved" stands. A TESS-SPOC timing fit would tighten the separation; it would not change this.

## 13d. GD1 and GD2: fold from the raw files, with odd/even

[`gd_fold.py`](gd_fold.py), output [`gd-fold-output.txt`](gd-fold-output.txt).

I derived the conjunctions from the Gaia rows first; they match the pilot's to all four decimals (GD1 A 392.8831, B 396.4120; GD2 A 390.0687, B 391.3831 BTJD). (I had already read the house's one-paragraph result before folding, so this is not strictly blind; the period search, timing and odd/even were done without the house's numbers.) Quality-0 QLP flux, 1-d running median, box search within ±0.4% of Gaia's period, then a linear fit to individual eclipse times:

| | GD1 | GD2 |
|---|---|---|
| Eclipse period | 6.038649 ± 0.000006 d (Gaia 6.03788 ± 0.00072, +1.1σ) | 2.613800 ± 0.000002 d (Gaia 2.613719 ± 0.000097, +0.8σ) |
| Eclipses timed, rms | 21, 5 min | 20, 1 min |
| Primary | conjunction A; +0.069 d (0.011 phase, 1.0σ) at Gaia's epoch; +0.089 phase at TESS with Gaia's period | conjunction A; −0.003 d (4 min, 0.1σ) at Gaia's epoch; +0.029 phase at TESS |
| Depth (central 60% of box) | 91 ppt | 68 ppt |
| Odd − even, within each TESS year | −0.6 ± 0.7 ppt (0.9σ) | −0.3 ± 0.3 ppt (0.9σ) |
| Secondary | phase 0.575, 8 ppt: e cos ω ≈ +0.118 (Gaia +0.133) | phase 0.500, 19 ppt: e cos ω ≈ 0.000 (Gaia +0.005) |

Both agree with the house: the primaries sit on Gaia's conjunction A, and the TESS-epoch offsets the house saw (+0.090 and +0.030) are just Gaia's period error carried about 610 (GD1) and 965 (GD2) cycles, within 1.3σ. **Neither has an odd/even difference** once each year is compared with itself (pooling all years gives a spurious 4.8σ for GD1 from sector-to-sector dilution). The secondaries are at different depths, and GD1's is at phase 0.575, so neither is a twin at 2P. Both are eclipsing Gaia SB1s with the orbit Gaia gives.

## 13e. Gaia's double-lined periods are the weak ones

[`sb1_vs_sb2_periods.py`](sb1_vs_sb2_periods.py), output [`sb1-vs-sb2-periods-output.txt`](sb1-vs-sb2-periods-output.txt).

Run 12a said about one Gaia DR3 period in twenty misses by 3σ. Split by solution type on the A sample (tier-blind), it is two different populations:

- **SB1:** 5 of 155 (3.2%) at 3σ or more (A102, A109, A117, A159, A202), robust width 1.11.
- **SB2:** 8 of 29 (28%) at 3σ or more (A12, A28, A29, A52, A86, A110, A147, A167), robust width 2.31. One-sided Fisher p = 1×10⁻⁴.
- The R sample (run 11e's `gaia-period-pulls.csv`) agrees: SB1 6 of 194 (3.1%), SB2 2 of 4 (R729, R752).
- To bring the 3σ tail down to about three times the Gaussian rate, SB1 period errors need ×1.45 and SB2 errors ×2.7. The same holds for conjunction times (13a: SB2 width 2.95 against 1.54).
- Gaia's own goodness of fit (F2) points the same way, weakly: SB1 orbits with F2 > 2 fail 3 of 26 times against 2 of 129 (one-sided p = 0.03, cut chosen after looking); SB2s with F2 > 10 fail 5 of 11 against 3 of 18 (p = 0.11). Worth a look in DR4, not a rule.
- **Suggested sentence (Table 4 discussion).** "Eight of the thirteen period failures are double-lined solutions: 8 of the 29 SB2 orbits compared (28%) against 5 of 155 SB1 orbits (3%). Gaia DR3's double-lined period errors appear understated by a factor of about 2.5, its single-lined ones by about 1.5." This generalises what the paper already says of A167.
- **What this means for Table 4.** Each of the eight SB2 rows is a real disagreement with Gaia's quoted error, which is how Table 4 defines a contradiction, so the count stands. But with SB2 errors scaled by 2.7, none of the eight would still be 3σ off (A167 comes closest at 2.9σ), so for the double-lined rows Table 4 is mostly measuring Gaia's SB2 error bars, not eight separately wrong orbits. The scale is derived from these same systems, so this is a description, not an independent test; the SB1 rows and the e cos ω rows are unaffected.

The paper's Table 4 period list is reproduced exactly from Fable 5.1's NSS rows (the twelve periods 3.2–8.0σ off, plus A109, which the paper already explains by its period change), and the four systems at other periods (A9, A45, A46, A54) are the paper's wrong, spurious and by-catch cases. Checks on the code: the conjunction (A or B) it assigns matches the paper's note in all 46 systems whose note names one, and the mean Gaia-epoch offset is +0.22 ± 0.12σ (no sign of a time-system or epoch error in the 389.0-d offset).

## 13f. The R systems held at probable for conjunction tension, against the A sample's spread

[`r_tension_vs_a.py`](r_tension_vs_a.py), output [`r-tension-vs-a-output.txt`](r-tension-vs-a-output.txt).

Run 12's lead (ii). Using 13a's A-sample offsets as the reference (172 of the 184 confirmed), for each R system whose review names Gaia tension while its period agrees within 3σ:

- **R740** (−3.15σ at TESS, −2.77σ at Gaia's epoch) and **R816** (+3.17σ, +2.08σ): 7–8% of A systems are as far off at TESS, 13–14 of them confirmed. R356, which is confirmed, has the same tension (+3.03σ).
- **R723, R755, R833**: milder; 17–32% of A systems are as far off at TESS. R833 is +3.56σ at Gaia's epoch (phase 0.068, the largest), which 8% of A systems match; its review says association "is excluded"; the conjunction offset alone would not exclude it, though the review may rest on more than the conjunction time. R755 has its own triple reason (run 7).

So the conjunction tension that keeps these five at probable is no larger than what a dozen confirmed A systems carry. I have not changed tiers; this is for whoever owns the R tables, and it only removes the Gaia reason, not any other named limitation.

## Limits

Linear propagation of `corr_vec` (as in runs 4 and 12); edge-on conjunction times; corr_vec parameter order as in Gaia's nsstools (SB1: P, γ, K1, e, ω, Tp; SB2 adds K2 after K1); circular and astrometric solutions not tested. Window coverage is evaluated at each system's tabled eclipse epoch, not at every sector, so it is indicative, not the search's exact geometry. GD depths are QLP-level, not deblended. The fold's box search was limited to ±0.4% of Gaia's period.

## Credits

Fable 5.1 fetched the NSS rows with `corr_vec` from AIP's mirror, cached the GD light curves and measured R729's event times; the A147/A167 Gaia-epoch test and the ephemeris tables are the paper's. Duet did these tests.

Rechecked when committed to main: `a_epoch_test.py`, `r729_epoch.py`, `r_tension_vs_a.py`, `search_window_budget.py` and `sb1_vs_sb2_periods.py` rerun from repository files and reproduce every CSV and output file byte for byte with NumPy and pandas. Not rerun: `gd_fold.py`, whose GD1/GD2 light curves are in the house folder, not the repository; `gd-fold-output.txt` is the run's own.
