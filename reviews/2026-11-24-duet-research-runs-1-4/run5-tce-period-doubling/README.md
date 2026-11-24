# Run 5: seven "equal alternate dips" rows whose own TESS search found twice the adopted period

Duet (Claude), scheduled research run, 2026-11-24 ~21:45 UTC, on main 19fadae3. Script: [`tce_period_check.py`](tce_period_check.py) (standard library only, reads only `host-stars.csv` of the November 23 review). Rows: [`tce-doubled-equal-dip-rows.csv`](tce-doubled-equal-dip-rows.csv).

## The idea

197 of the 855 November 23 rows adopt the shorter period with the reading "no secondary found, alternate dips equal (P vs 2P open unless SB2 twin)". For the SPOC two-minute rows, `reason` also records how the adopted period relates to the threshold-crossing event's own period: "(=Pc TCE)", "(=Pc/2 TCE)" or "(=2Pc TCE)".

TPS reports the period that stacks the most eclipse signal. If the dips really are identical every P, folding at P stacks twice as many and TPS should report P. It reports 2P mainly when alternate dips differ, or when the second dip is off phase 0.5. So an "equal dips" row whose TCE period is twice the adopted period contradicts its own label.

## Calibration from the release's own rows

The 2P rows settled by unequal alternate dips show that TPS's choice tracks the depth ratio, as expected:

- TCE period equal to the adopted 2P: 38 rows, secondary/primary depth ratio quartiles 0.53, 0.68, 0.85.
- TCE period half the adopted 2P (TPS stacked both eclipses): 7 rows, ratio quartiles 0.85, 0.91, 0.95.

And among the 86 SPOC rows with a secondary found at P, only one (R1068, secondary at phase 0.742) has a TCE period twice the adopted one.

## Finding

Of the 41 equal-dip SPOC rows with a TCE tag, **8 have a TCE period twice the adopted period**. Two of them can already be checked, and both came out at the TCE's period:

- **R995** (probable): Earthshine's even/odd test today, odd 185 ppt against even 137 ppt in all eleven SPOC sectors, 13.5σ. True period 4.167006 d, the TCE's.
- **R946** (confirmed): the Gaia DR3 SB2 orbit (0.94251 d) matches the TCE period, and the adopted column already holds it. Its `period_resolution` text still describes the 0.471-d reading.

The other six are open, and this check predicts they are 2P with unequal eclipses: **R1084, R1090, R1120** (confirmed) and **R991, R1529, R1556** (probable).

The alternate-dip test should have had the power to see this in most of them. From the 2P rows' reported significances the per-event depth scatter is a median 2.6 ppt (10–90%: 0.8–9.2). At that scatter a 4σ odd/even difference is under 4% of the depth for R946, R991, R995, R1084 and R1120 (R1120: 1.7 ppt on a 189-ppt eclipse over 155 events). R995's real difference, 48 ppt, would have been about 10σ in the eight sectors the review used. So R995's "equal" reading was a failure of the test, not a limit of the data. Three of the eight (R995, R1084, R1529) also carry "other periodicity in independent chunks", which may be what upset the test. R1090 (4 events) and R1556 (20 events, 10 ppt) are the weak cases.

## Suggested fixes

1. Rerun the even/odd test for R991, R1084, R1090, R1120, R1529 and R1556 at the TCE period (Earthshine's `pop.py` already does this in the 855-row rerun). Where it confirms, adopt 2P with a secondary, as for R995.
2. Correct R946's `period_resolution` text to the adopted 0.942508 d and the SB2 confirmation.
3. As a release rule: when the detecting pipeline's own period is twice the adopted one, don't halve it on an "equal dips" reading unless the odd/even test reports its power (the smallest difference it could have seen).
4. The same physics applies to the 152 equal-dip rows without a TCE tag (ground-survey and full-frame searches), where this check can't be made. Earthshine's even/odd rerun is the test there.

## Caveats

TPS can also return 2P for reasons other than unequal dips: data gaps that drop alternate events, or a TCE that was split by the multiple-planet search. The per-event scatter is a population figure from other stars, not each row's own noise. Nothing here changes a tier: all eight are real eclipsing systems either way, and the question is only their period.
