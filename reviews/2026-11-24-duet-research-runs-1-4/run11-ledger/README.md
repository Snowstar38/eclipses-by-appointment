# Run 11: one ledger of the host-table changes runs 1–10 proposed, and where they contradict each other

Duet (Claude), scheduled research run 11, 2026 November 25, on main at `9334ec77` (run 10). Python 3 with pandas and NumPy. Run from the repository root:

```
D=reviews/2026-11-24-duet-research-runs-1-4/run11-ledger
python3 $D/ledger.py $D/ledger.csv > $D/ledger-output.txt
python3 $D/twins_premise.py > $D/twins-premise-output.txt
```

## 11a. The ledger, and eight rows where two runs disagree

**Summary.** Runs 1, 5, 6, 9 and 10 each suggested changes to `reviews/2026-11-23-pipeline-and-survey-review/host-stars.csv`, in five READMEs. [`ledger.csv`](ledger.csv) puts all 300 suggestions (192 rows) in one table, each with the cell's current value, the proposed value, the run that proposed it and why. None has been applied yet: the host table last changed in `ff8b6831` (November 24, 19:00 EST), and 0 of the 112 period proposals (89 rows) match the current `adopted_period_days`. Laying them side by side shows **eight rows where one run says the period is P and another says 2P**. Run 6b read the visual note's "secondary" as an occultation at P; runs 1, 5 and 10a read the same rows as twins at 2P. I went back to the evidence in the repository for each one:

| Row | Proposed by | What the evidence supports now |
|---|---|---|
| R1684 | run 6b: 2P | **P is the orbit.** Earthshine's fit finds an eclipse-shaped 1.7 ± 0.1 ppt secondary at phase 0.520 (3.9 h wide against a 3.6-h primary) and equal alternate primaries (28.5 and 28.6 ppt). The "shallower secondary visible in the 2P fold" is this secondary. Run 6b's doubling is withdrawn; fill the secondary columns. |
| R1253 | 10a strict: 2P | **2P stands** on Earthshine's parity test (37σ, odd deeper in 5 of 7 sectors), but the alternate eclipses differ by 2.5%, so it is not a twin. |
| R1697 | 10a strict: 2P | **2P stands.** Earthshine searched (best feature 0.7 ppt at phase 0.39, where P would need ≥ 44 ppt). The visual "secondary is shallower" is the alternate eclipse in the 2P fold (odd/even 99.9 against 76.0 ppt). Not a twin. |
| R1488 | 10a strict: 2P | **Leans 2P** (odd and even mid-times differ by 9.5 min at 49σ, but the per-sector offsets disagree in sign); Earthshine's secondary search locked on the primary. Keep as "2P favoured", not strict. |
| R1405 | 10a strict: 2P | **Open.** The review's own check measured phase-0.5 events at a median 26.6 ppt (20 of 21 above 3σ; 11.5 ppt stacked), against 14.6 ppt needed if P is the orbit. P cannot be excluded. |
| R1352 | 10a strict: 2P | **Open.** Earthshine's search locked on the primary; the reviewer saw "a shallower secondary between primaries". Needs the sheet. |
| R1042 | 10a strict: 2P | **Open.** The reviewer saw a "weaker secondary"; Earthshine's best feature (13.4 ppt at phase 0.60) is 78 h wide, so not an eclipse. Needs the sheet. |
| R1040 | run 1, 10a SB2 text: 2P | **Leave P.** Run 10a does not exclude P here (ratio 0.19). The SB2 argument says a secondary "should exist"; the reviewer saw "a weaker feature at the secondary phase", which is what that argument asks for. |

**What this changes in run 10a.** The strict list drops from 48 to 44 rows (R1042, R1352 and R1405 become open; R1488 moves to "2P favoured", which now has 21), and R1253 and R1697 keep 2P but lose the word "twin". The paper wording suggested in run 10 still holds, with one correction to its premise (11a(ii) below).

## 11a(ii). What stands behind "no secondary" in run 10a

[`twins_premise.py`](twins_premise.py), output [`twins-premise-output.txt`](twins-premise-output.txt) and [`twins-premise.csv`](twins-premise.csv).

Run 10a said that the absence of a secondary "rests on the review's own search and Earthshine's independent one, which found none in any of these rows". That overstates Earthshine's part. Earthshine's free secondary search sometimes locks on the primary eclipse itself (best feature at phase 0 or as deep as the primary), and run 10a noted the habit but did not count it. It happened in **33 of the 68 excluded rows (27 of the 48 strict)**. For those, the review's own search is the only evidence of no secondary. In the other 35, Earthshine's search ran properly, and none found an eclipse-shaped feature (duration within a factor two of the primary's) reaching half of run 10a's minimum prediction. Its larger features there are out-of-eclipse structure 7 to 20 times wider than the primary. So run 10a's conclusion holds where Earthshine searched, and in the locked rows it holds as far as the review's search does. The seven rows whose visual note mentions a secondary-like feature are the table above (plus R1120, whose note describes the alternate dip in the 2P fold, which matches its parity result).

**Ask for the house (light curves).** For the 27 strict rows where the search locked, a secondary search that masks the primary (± one duration) before looking would settle them. The list is `twins-premise.csv` with `strict` and `search_locked` both true.

## Also from the ledger

- **R1117** is no longer in `accepted-systems.csv` (excluded as a prior identification: Kounkel et al. 2021), but its host-table row still carries P = 1.318332 d. The physical record should still read 2.636664 d.
- Run 1's 15 rows with "2P adopted, secondary columns blank" are all still blank; Earthshine's fits now give the secondary depth for them (the 855-row table in `run10-twins-and-r1003/`).

## 11b. The five tabled secondaries run 10a called too shallow

[`shallow_secondaries.py`](shallow_secondaries.py), output [`shallow-secondaries-output.txt`](shallow-secondaries-output.txt). Run 10a listed R978, R1512, R1504, R1416 and R1225 as confirmed rows whose tabled secondary is shallower than any main-sequence companion able to make the primary allows. Two things run 10a's bound ignored settle four of them:

- **Eccentric orbits (R978, R1504, R1416).** Their secondaries sit at phases 0.245, 0.364 and 0.687 (e ≥ 0.39, 0.21 and 0.29). In an eccentric orbit the two conjunctions happen at different separations, so the transit can be central while the occultation is grazing and much shallower. The circular bound does not apply, and nothing here is wrong.
- **The primary depth (R1225).** Run 10a used Earthshine's fitted depth, 138 ppt; the table says 88.6. With the table's depth the tabled 17.9-ppt secondary is 1.3 times the bound, comfortably consistent. The 56% difference between the two depths is the largest case of the depth-column puzzle noted in run 10 (median fitted/tabled 1.135) and is worth one look at the sheet.
- **R1512 stays odd.** TIC 453098720, P = 3.380 d, a 1.39-R☉, 5,765-K host seen in 44 sectors with 310 primary eclipses, secondary at phase 0.501 (2.2 ppt, SNR 41). Its orbit is circular and the bound holds with either depth: a companion big enough for the 99-ppt primary (≥ 0.38 R☉) should give an occultation of at least 7.8 ppt, 3.5 times what is seen, and would have to be about 2,750 K, far cooler than any main-sequence star that size. Either the host is smaller than TIC says (at 1.0 R☉ the bound is still about twice the observed depth), the companion is a young, inflated M dwarf, or the eclipse belongs to a blended binary whose own stars set the depth ratio. Its difference images are on target in three sectors, but the row's own limitation says companions within 10″ are not excluded. It is a ground-survey spectroscopic binary, so the survey's radial-velocity amplitude, if the house has it, would give the companion's mass and decide between these.

## 11c. What the host table's depth column measures

[`depth_column.py`](depth_column.py), output [`depth-column-output.txt`](depth-column-output.txt). Run 10 left open why Earthshine's fitted depths are a median 1.135 times the table's `depth_ppt`. `methods.md` calls the column "the primary eclipse depth" and `duration_h` a duration; Earthshine has already shown that `duration_h` is a box width (here a median 0.675 of the fitted first-to-fourth-contact duration, IQR 0.64–0.71).

- **The depth is the mean inside that box.** The ratio depends on eclipse shape the way a box mean must: 1.24 for V-shaped eclipses (flat-bottom fraction T23/T14 < 0.1, 99 rows), 1.14 for the typical 0.1–0.3 (638 rows), 1.02–1.04 for flat-bottomed ones. A box of the tabled width laid on Earthshine's trapezoid predicts the same trend (1.35, 1.27, 1.07–1.14), about 10% high throughout; cadence does not matter (2, 3.3 and 10 min all 1.13). So the column is a box-mean depth, shallower than the deepest point by about 13% typically and 25% for V-shaped eclipses. Dilution by blended light comes on top, as the methods already say.
- **For `methods.md`** (one sentence): "`depth_ppt` is the mean depth inside the best-fitting box of width `duration_h`, which is about two-thirds of the first-to-last-contact duration; the deepest point of the eclipse is typically 10–25% deeper, more for V-shaped eclipses." Anyone comparing these depths with model eclipses, or using them for radius ratios, needs this.
- **23 rows disagree by more than 2.5×**, 21 of them probable and 16 from the ground-survey spectroscopic-binary search (list in the output). Three are Earthshine fits stuck at a 950-ppt cap (R1711, R1712, R1802), so the table is likelier right there. R1003's (28 against 87 ppt) is physical: its eclipses switched on during the baseline, so a depth averaged over all sectors is diluted by the eclipse-free ones. The rest need one look each at which sectors went into each number. In the capable-neighbour screen a too-shallow depth only makes more neighbours capable, so these errors make attribution more cautious, not less.

## 11d. A73: what TESS should see when it next looks, in 2028

[`a73_forecast.py`](a73_forecast.py) (rebound, NumPy; reuses run 9's `a73_fit.py` and its fits), output [`a73-forecast-output.txt`](a73-forecast-output.txt).

tess-point (0.9.5) puts A73 (TYC 4590-364-1) in sectors 17–19, 24–26, 40, 52–53, 57–60, 73, 77–80 and 84–86, and next in sectors 123–125 and 129; it has no sector in 2026–27. Sectors 123–124 are centred on BTJD 4985 and 5013 (about August–September 2028), so that is TESS's next look. The last secondary in the house table is BTJD 3650.9 (2025), at phase 0.474 and 79 ppt.

Every stable run-9 fit was integrated on to 2028:

| Fit family | m₃ (M☉) | Dark-tertiary a₀ (mas; Gaia 0.719) | Secondary phase, 2028 | Impact parameter | Secondary depth |
|---|---:|---:|---:|---:|---:|
| Heavy, e_out 0.10–0.25 (5 fits) | 0.69–0.95 | 0.60–0.78 | 0.491–0.520 | 0.09–0.26 | 0.121–0.130 |
| Light, e_out 0.25–0.30 (2 fits) | 0.17–0.26 | 0.17–0.25 | 0.512–0.516 | 0.39–0.48 | 0.086–0.107 |

- **Depth decides between the families; phase does not.** Both families put the secondary back near phase 0.51–0.52 (one heavy fit, 0.491). But the heavy tertiaries, the ones whose mass matches Gaia's photocentre orbit if the tertiary is dark, carry the pair back to nearly central eclipses (secondary 121–130 ppt, close to the 2019 maximum of 146), while the light ones leave it grazing at 86–107 ppt. The gap (20–40 ppt) is four to eight times run 9's per-event depth floor of 5 ppt, so one sector settles it, independently of Gaia DR4.
- **For the paper.** One sentence: "The N-body solutions predict that when TESS returns to A73 in 2028 (sectors 123–124) the secondary eclipse will lie near phase 0.51–0.52; a depth of about 125 ppt would confirm the heavy, dark tertiary that Gaia's photocentre orbit requires, and about 90–105 ppt the light one."
- **Sooner.** A73 is at declination +78°, in ZTF's footprint, so ground photometry at the predicted secondary times could test this before 2028 if the house has it.
- **Limits.** Uniform discs and run 9's assumed radii (1.4 + 1.0 R☉); depths scaled to the observed secondaries as in run 9. The spread within each family is the honest uncertainty; no fit outside run 9's families was tried. tess-point's sectors beyond about 125 are provisional.

## 11e. Gaia's period errors are calibrated for confirmed systems; the probable tier's periods are not

*Corrected in run 12a (`../run12-gaia-tiering/`): the confirmed-tier calibration below is circular, because a failed Gaia-geometry check is one of the named reasons a system was graded probable. Counted without tier, 7 of 199 (3.5%) are 3σ or more off, about one Gaia DR3 period in twenty. The sentence "about 0.5 of its 184 comparisons would be expected to fail by chance" is withdrawn; the paper's twenty contradictions stand as real disagreements.*

[`gaia_pulls.py`](gaia_pulls.py), output [`gaia-pulls-output.txt`](gaia-pulls-output.txt) and [`gaia-period-pulls.csv`](gaia-period-pulls.csv). The paper counts a Gaia orbit as contradicted when its period or e cos ω is 3σ or more from the eclipse value, in Gaia's quoted errors, and finds 20 (19 of 184 counted systems, plus A113). Whether 19 of 184 is a lot depends on whether Gaia's errors are honest, which the paper does not test. The repository's own copies of Gaia's NSS table (59 files, 1,321 sources with `period_error`) join to 199 accepted systems whose Gaia period is within 3% of the eclipse period (run 8's match list), mostly November 5 R systems, so this is a separate sample from the paper's 184. With z = (P_Gaia − P_eclipse)/σ_Gaia (eclipse periods are usually far more precise and their errors are left out; the review files give one for 63 of these, and adding it changes only R814, below):

- **Confirmed systems: Gaia's errors are exactly right.** 150 systems, robust width 0.99, none at |z| ≥ 3 (0.4 expected). This holds at every period, including 20–60 d (63 systems, width 0.98, none). So for Gaia SB1 orbits the paper's 3σ rule has a false-alarm rate near the nominal 0.3%, and about 0.5 of its 184 comparisons would be expected to fail by chance per quantity. Its 19 are real. The paper could say so in a sentence; it strengthens the "contradicted orbits" contribution.
- **Probable systems: the tail is all here.** 49 systems, width 1.54, and all eight |z| ≥ 3 cases: R729 (33σ) and R752 (8.7σ), both SB2 solutions, then R716 (5.3σ), R789 (4.5σ), R810 (3.7σ), R787 (3.5σ), R814 (3.4σ; 2.3σ once its own eclipse-period error of 0.0147 d is added) and R771 (3.3σ). So seven stand. Within 20–60 d alone it is 8 of 36 probable against 0 of 63 confirmed (Fisher p = 0.0002), so this is not a period effect. They come from the November 5 catalogue-recovery, final-night and faint-band reviews.
- **What it means.** For these eight either the eclipse period is less certain than its few events suggest, or Gaia's solution is wrong, or (less likely at a 0.1–0.5% period difference) the eclipse is not the Gaia binary's. Under the paper's own rule the seven would be more contradicted Gaia orbits, unless the eclipse periods are at fault, and none is in Table 4. Either the rule should be applied to the R systems too, or their period agreement should be quoted as a z, not as "within 3%". It also fits run 8's estimate that about one probable Gaia-fold system in seven may be mis-associated. The two SB2 cases join A167: Gaia's double-lined solutions understate their period errors (width 6.6 over four SB2s here).
- **Ask for the house.** The eclipse periods and event counts behind R716, R729, R771, R787 and R789 (the review files give no period error for them), to tell an eclipse-period problem from a Gaia one.

## Limits

Everything here is read from the repository's tables and Earthshine's 855-row measurements; no light curve was refitted. "Locked" is a heuristic (best feature within 0.05 in phase of the primary, or deeper than half the primary). The verdicts for R1042, R1352 and R1405 need someone to read the sheets.

## Reproducibility

Checked before handing over: every script here reproduces its output file byte for byte from the repository at `9334ec77` (`a73_forecast.py` needs `rebound`; the others pandas, NumPy and, for `gaia_pulls.py`, SciPy).

Rechecked when committed to main: `ledger.py`, `twins_premise.py`, `shallow_secondaries.py`, `depth_column.py` and `gaia_pulls.py` rerun from repository files and reproduce every output byte for byte with NumPy and pandas. SciPy is not installed on the committing machine, so `gaia_pulls.py` ran with a small stand-in for `fisher_exact`; its two p-values agree to the last digit and only their printed form differs. Not rerun then: `a73_forecast.py` (needs `rebound`, not installed then). Rechecked on 2026 November 26 with `rebound` 5.2.3 and SciPy 1.18.1: `a73_forecast.py` reproduces `a73-forecast-output.txt` byte for byte, and `gaia_pulls.py`, run with SciPy's own `fisher_exact`, reproduces `gaia-pulls-output.txt` and its CSV byte for byte.

## Credits

Earthshine (Opus 5.5) measured the 855 rows and ran the parity test used throughout; the review team wrote the visual notes and the `pdouble` checks quoted here. Run 9's A73 fits used Fable 5's Gaia orbits and secondary-eclipse table. Duet built the ledger, the cross-checks, the forecast and the pull analysis.
