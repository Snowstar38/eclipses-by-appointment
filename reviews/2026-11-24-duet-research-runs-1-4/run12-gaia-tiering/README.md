# Run 12: run 11e's Gaia calibration was circular; the eclipses that "disagree" with Gaia sit on Gaia's own conjunctions

Duet (Claude), scheduled research run 12, 2026 November 25, on main at `9334ec77` with run 11's `run11-ledger/` in place (committed with this run). Python 3 with pandas, NumPy and SciPy. Run from the repository root:

```
D=reviews/2026-11-24-duet-research-runs-1-4/run12-gaia-tiering
python3 $D/tier_reasons.py > $D/tier-reasons-output.txt
python3 $D/gaia_epoch_test.py > $D/gaia-epoch-test-output.txt
```

`tier_reasons.py` must run first (`gaia_epoch_test.py` reads its `tier-reasons.csv`). `gaia_epoch_test.py` imports run 4's `window_covariance.py` for the conjunction formula and the linear covariance propagation.

## 12a. Run 11e's "Gaia's errors are exactly right for confirmed systems" is circular

[`tier_reasons.py`](tier_reasons.py), output [`tier-reasons-output.txt`](tier-reasons-output.txt), table [`tier-reasons.csv`](tier-reasons.csv).

Run 11e found that among 199 accepted R systems with a Gaia period error in the repository, none of the 150 confirmed ones has its Gaia period 3σ or more from the eclipse period, while 8 of the 49 probable ones do, and concluded that Gaia's errors are honest and the paper's 3σ rule sound. That reasoning does not hold. The paper defines probable as "a real repeating eclipse with one named limitation", and in the R reviews **a failed Gaia-geometry check is one of the named limitations**. Every one of the eight outliers says so in its own review:

- R789: "Association: GAIA_ASSOCIATION_TENSION".
- R810: "final physical tier is PROBABLE because Gaia-orbit association remains uncertain".
- R787: "Real target eclipses are established, but spectroscopic association is not fully passed".
- R814: "do not erase measured primary tension".
- R716: "Both period and conjunction disagree by about five formal Gaia standard deviations".
- R752: "Gaia-orbit tension keeps PROBABLE".
- R729: "the Gaia SB2 orbital association and source-specific conjunction geometry are unresolved".
- R771: "Gaia orbital association and close-source ownership remain unresolved".

So the confirmed tier was graded partly on agreeing with Gaia, and 0 of 150 there is what the grading produced, not a test of Gaia. Counted without regard to tier, 7 of 199 (3.5%) are at 3σ or more once the review's own eclipse-period error is included where it gives one (R814 drops to 2.3σ), and 26 of 199 (13%) at 2σ or more, against 0.3% and 4.6% for Gaussian errors. The paper's own appointment sample, where tiers did not depend on Gaia, gives the same picture: Table 4 has 12 of 184 periods 3σ or more off apart from the three aliases (A12, A28, A29, A52, A86, A102, A110, A117, A147, A159, A167, A202), 6.5%. The two rates agree (Fisher p = 0.24); the R confirmed tier alone does not (p = 0.0007).

**What to say instead.** Gaia DR3's core errors are fine (robust width 1.06, run 11e), but about one orbit in twenty to thirty has a period 3σ or more off its quoted error. This does not weaken the paper's twenty contradictions; each is a real disagreement. It means a contradiction is an ordinary event for a Gaia orbit, roughly 1 in 20, and not a 0.3% surprise. Run 11e's paper sentence ("about 0.5 of its 184 comparisons would be expected to fail by chance") should be withdrawn.

## 12b. The eclipses fall on Gaia's conjunctions at Gaia's own epoch

[`gaia_epoch_test.py`](gaia_epoch_test.py), output [`gaia-epoch-test-output.txt`](gaia-epoch-test-output.txt), table [`gaia-epoch-test.csv`](gaia-epoch-test.csv).

The R reviews read a period disagreement as doubt that the eclipse belongs to the Gaia binary. The paper reads the same kind of disagreement in the appointment sample as Gaia's orbit being wrong, and for A147 and A167 it shows why: carried back to Gaia's own epoch, the eclipses fall on the predicted conjunctions, so the orbit is the right one and only its period is off. I ran that test on every system it could be run on: 167 of the 199, using Gaia's full covariance (`corr_vec`) at Gaia's reference epoch and the eclipse ephemeris carried back with its own period error. An eclipsing binary that is not the Gaia binary would land at a random phase there; the chance of landing within a given offset of either conjunction is about 4 × offset / P.

| Row | Period z | Offset at Gaia's epoch | Phase | Chance if unrelated | Offset at TESS (Gaia's period carried forward) |
|---|---:|---:|---:|---:|---:|
| R716 | +5.3 | −0.10 d (2.0σ) | 0.005 | 2% | −1.01 d (5.1σ) |
| R752 (SB2) | +8.7 | +0.12 d (4.4σ) | 0.003 | 1% | −1.67 d (8.7σ) |
| R787 | −3.5 | +0.08 d (0.3σ) | 0.003 | 1% | +1.81 d (3.1σ) |
| R789 | −4.5 | −0.21 d (2.5σ) | 0.006 | 2% | +0.83 d (3.9σ) |
| R814 | −3.4 (−2.3 with its own error) | −0.05 d (0.3σ) | 0.001 | 0.6% | +1.45 d (3.3σ) |
| R771 | +3.3 | +0.91 d (2.6σ) | 0.039 | 16% | −2.26 d (3.1σ) |
| R810 | −3.7 | −2.33 d (3.6σ) | 0.090 | 36% | +9.58 d (3.5σ) |

- **Five of the seven are the Gaia binary with a wrong Gaia period.** R716, R752, R787, R789 and R814 land within 0.001 to 0.006 in phase (1 to 5 hours) of Gaia's predicted conjunction at Gaia's own epoch. Each has a 0.6–2% chance of doing that by accident, about 10⁻⁹ for all five. Their offsets at TESS's epoch, 0.8 to 1.8 days, are just Gaia's period error multiplied by the 33 to 58 orbits between Gaia's epoch and the tabled eclipse epoch. This is the A147 and A167 pattern exactly. The 2–4σ left at Gaia's epoch for R716, R752 and R789 is within what 12c finds for Gaia's conjunction errors (and SB2 errors run large, as for A167).
- **R771** (phase 0.039, 2.6σ) leans the same way but is not decisive; its close-neighbour question stays open anyway. **R810** does not fit: 0.09 in phase and 3.6σ off at Gaia's epoch. Its eclipse period comes from two eclipses one cycle apart (sectors 91–92), so its period, not Gaia's, may be the weak one; it stays probable. R729 could not be tested (its review tables give no epoch, and its linked report page has no event times).
- **What this means for the paper.** Under the paper's own rule and its own reading of A147 and A167, **R716, R752, R787 and R789 are contradicted Gaia orbits** (period 3.5–8.7σ off, eclipses on Gaia's conjunctions at Gaia's epoch), which would make the Table 4 count 24. For them, and for R814, whose period agrees within 2.3σ once its eclipse-period error is counted, the Gaia tension that keeps them at probable is explained by Gaia's period, not by a doubtful association. Where Gaia is their only named limitation (R716, R787, R789, R814; R752's review also mentions cadence-limited early timing), they meet the confirmed standard the appointment sample uses. I have not changed any tier; that is for whoever owns the R tables. The two samples should at least use one reading of the same evidence.
- **Suggested sentence (Gaia contradictions section).** "The same comparison in the R sample finds four more: R716, R752, R787 and R789, whose eclipses fall within 1–5 h of Gaia's predicted conjunctions at Gaia's own epoch while their periods differ by 3.5–8.7σ. Across both samples about one Gaia DR3 period in twenty differs from the eclipse period by 3σ or more."

## 12c. Gaia's conjunction times at its own epoch: how big are the errors really?

Same script. At Gaia's epoch the period error barely matters, so the offset tests Gaia's e, ω and Tp with their correlations. Over all 167 systems the offsets in full-covariance σ have robust width 1.29 (1.04 for e < 0.1, 1.43 for e ≥ 0.1), and 5 are 3σ or more (R810, P025, R720, R833, R752). Ignoring the correlations gives a width of 0.22: the independent errors are four to five times too large at Gaia's epoch, because Tp and ω are strongly correlated. So with the correlations, Gaia's conjunction errors are about 30–40% too small for eccentric orbits, which is roughly what run 4 found at TESS epochs (robust sd 0.73 there, with the period error dominating). This matters only for how strict "on Gaia's conjunction" should be; it does not affect 12b's five, whose offsets are hours against periods of weeks.

## Limits

Read from the repository's tables, review reports and Gaia NSS copies; no light curve was refitted. Event times came from the review tables, `measurements.json`, or the first event in a review's report, so a few systems use a secondary-kind epoch; the test takes the nearer conjunction, which handles that. Edge-on conjunction times, linear covariance propagation (as in run 4). The appointment-sample rate is counted from Table 4's text, not recomputed. Tier reasons are matched by keyword, then read by hand for every outlier.

## Credits

The R review teams wrote the limitation texts and Gaia geometry files used here; the A147 and A167 test is the paper's. Run 4's covariance code (Duet) and Fable 5.1's corr_vec work underlie the propagation. Duet did the tier audit and the Gaia-epoch test.

Rechecked when committed to main: `tier_reasons.py` then `gaia_epoch_test.py` rerun from repository files and reproduce both CSVs and both output files byte for byte (NumPy and pandas; SciPy is not installed on the committing machine, so `tier_reasons.py` ran with a small stand-in for `fisher_exact`, whose two p-values agree and only print differently).
