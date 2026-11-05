# F024 TIC 238926302: REFUTED

**Completion:** COMPLETE bounded review. **Selection:** repeat_sector_dip; Gaia DR3 5500666290750087552 (SB 23.77145862961961 d).

**Physical assessment.** The flagged long dips track spacecraft gaps and baseline resets. S61 2981 ends before the 2982.19-2982.41 gap; S88 3703.5 aligns with F021; S94 3875.1 has the same asymmetric gap event seen in F021/F026/F029. S96 3926 follows a 3920.01-3924.41 missing interval and S98 4010 sits beside the 4009.81-4010.06 gap. The raw Gaia-period fold has no phase-coherent eclipse.

**Catalogue status.** SCOPED_NONMATCH; no target EB identification in checked tables. The exact queue catalogue evidence is in `../../shared-catalogues/target-evidence.json`; a primary-table nonmatch alone would not establish novelty.

**Limits.** Artifact evidence refutes this detection sequence, not the Gaia SB1 star or all possible faint eclipses. Local trapezoid widths often hit the 1.5-d bound and are not physical durations.

**Next check.** Recheck only after an independent phase-coherent dip occurs away from a gap.

**Evidence and reproduction.** The packet at `../../source-packets/238926302/sources.json` identifies and SHA256-verifies every source QLP FITS file. `lead-measurements.json` has actual quality-zero cadence coverage, source hashes and the raw local windows; `lead-event-panels.png`, `lead-alternative.json` and `lead-alternative.png` show raw and alternate QLP extraction of the same photons. The bounded scripts and shared source catalogue receipts are in the batch root. A predicted window is never treated as a fitted eclipse center.

- [lead-gaia-fold.json](lead-gaia-fold.json)
