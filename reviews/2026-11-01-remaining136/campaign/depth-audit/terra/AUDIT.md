# Independent depth correction audit

Checked the saved 70-target AST replay without rerunning the fits. For each recorded primary and secondary fit, independently evaluated `d*1000*min(1,w/(2*max(k,1e-5)))`; the replay values agree. The selected-event median calculation produces 11 changed primary events across 8 targets and exactly two changed medians: TIC 290749976, 2.406812247951338 to 2.383432477399884 ppt; TIC 47066501, 22.85721916675285 to 22.507649692484065 ppt. Saved exact replay checks cover 70 primary and 25 secondary records (131 secondary events). All checks pass.

All 24 staged original and corrected artifact hashes match the correction manifest. The eight corrected measurements match their original snapshots in every non-depth field after removing the added original-parameter and ingress provenance fields. Neighbor replay shows no capable-set change among the 60 targets for which fresh-pixel JSON is present; ten lack that input. Inspected the three corrected raw-event plots: the affected labels agree with corrected values and all plots are legible. Verification is bounded to the saved replay and staged artifacts; final applied files and freeze manifests require a subsequent check.

`check.py`, `independent-check.json`, and `preservation.py` contain the independent calculations. This audit directory should be excluded from the final receipt.

After application and freeze, independently hashed all 47 applied-manifest paths against their recorded after hashes: zero mismatches. Lead's post-correction verification records all five batch manifest hashes verified. See applied-check.json.
