# F027 TIC 64696566: PLAUSIBLE

**Completion:** COMPLETE bounded review. **Selection:** repeat_sector_dip; Gaia DR3 5609502995422286592 (SB 25.57505884366424 d).

**Physical assessment.** Raw SAP in S7, S33/34, S61 and S87/88 shows persistent broad, changing-amplitude waves. A bounded short-period diagnostic favors about 1.2609 d, far from Gaia SB1 25.5751 d. The local minima are broad parts of the wave, without a discrete ingress, flat core and egress that would establish eclipses. The nearest Gaia G18.32 neighbor at 3.28 arcsec is far too faint to explain the 1-3 percent modulation by total disappearance, so the variability is likely on the target.

**Catalogue status.** SCOPED_NONMATCH; no target EB identification in checked tables. The exact queue catalogue evidence is in `../../shared-catalogues/target-evidence.json`; a primary-table nonmatch alone would not establish novelty.

**Limits.** A contact binary or ellipsoidal interpretation remains possible, but spots/pulsation or a multi-period signal is not excluded. The 1.2609-d diagnostic is not an adopted orbital period. No isolated same-kind eclipse timing or Gaia orbital geometry link exists.

**Next check.** Obtain multicolor/high-cadence photometry or radial velocities to distinguish a contact/ellipsoidal binary from non-eclipse variability.

**Evidence and reproduction.** The packet at `../../source-packets/64696566/sources.json` identifies and SHA256-verifies every source QLP FITS file. `lead-measurements.json` has actual quality-zero cadence coverage, source hashes and the raw local windows; `lead-event-panels.png`, `lead-alternative.json` and `lead-alternative.png` show raw and alternate QLP extraction of the same photons. The bounded scripts and shared source catalogue receipts are in the batch root. A predicted window is never treated as a fitted eclipse center.

- [lead-shortperiod.json](lead-shortperiod.json)
- [lead-gaia-fold.json](lead-gaia-fold.json)
