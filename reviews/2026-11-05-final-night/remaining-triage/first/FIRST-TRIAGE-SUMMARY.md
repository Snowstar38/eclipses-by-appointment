# First-arm visual screening, 2026-11-05

I viewed every raw SAP quality-0 plot on `sheet-001.png` through `sheet-042.png`, in frozen TIC order, covering M001-M336 (336 distinct TICs). `first-visual-triage.csv` has one screening disposition per target. `first-shortlist.csv` ranks exactly 20 targets for raw-source verification. `write_triage.py` preserves the visual transcription and checks the exact arm, ID sequence and sheet mapping.

| Screening category | Targets |
| --- | ---: |
| Repeated discrete trough | 3 |
| Ambiguous prospect | 26 |
| Broad variability | 75 |
| Step or gap dominated | 211 |
| Noise or rapid oscillation | 21 |
| **Total** | **336** |

The clearest displayed repeats are **M215 / TIC 185744410** (three narrow isolated troughs), **M168 / TIC 149316567** (narrow centered dips in sectors 7, 88 and 61) and **M271 / TIC 233405109** (three similar U-shaped depressions). These are visual leads for raw event and source checks, not astrophysical classifications. The lower ranked shortlist includes shallow, variable, sparsely sampled or reset-adjacent prospects; its rank expresses follow-up value, not a measured signal significance.

Each sheet shows at most three selected high-contrast retained windows from distinct sectors, not all events or all sector coverage. A selected window can contain an instrumental edge or unrelated variability. These views do not establish a period, lack of eclipses elsewhere, physical source, C/P classification or a null result for any target. `screening_*` labels are scheduling dispositions only. Verify the shortlisted events in the original bulk results and raw sector light curves before full review.

Source SHA-256: frozen `queue.csv` `d58e8743271e5729929028f1d49658af0b40e8cd341fa56ee7bad2d6db42e682`; `display-receipts.json` `599da96f7c92372e960ddbc3cab0db466b634609aff2554714ffd1b1b87dfc62`. The queue's seal records upstream source SHA-256 `24721af8b136d2484f05a8bcc1b838e25958a121373a54080fcc59e19518c1b4`.
