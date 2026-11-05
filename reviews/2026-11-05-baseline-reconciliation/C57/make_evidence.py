"""Hash exact reassessment inputs without altering the source directories."""
import hashlib
import json
from pathlib import Path

home = Path(__file__).resolve().parents[4]
paths = [
    "Fable 5.1/made/paper/paper.html",
    "Astra/made/cloud72-completion-2026-10-30/batch04/reports/402940895.md",
    "Astra/made/cloud72-completion-2026-10-30/shared-catalogues/coverage-matrix.csv",
    "Fable 5/made/sb1-scale/c9-402940895-persec.md",
    "Fable 5/made/sb1-scale/persec402.py",
    "Fable 5/made/sb1-scale/persec402-out.txt",
    "Fable 5/made/sb1-scale/persec402_gaia.py",
    "Fable 5/made/sb1-scale/persec402_gaia-out.txt",
    "Fable 5/made/sb1-scale/marg9-persec/402940895-windows.json",
    "Fable 5/made/sb1-scale/marg9-persec/402940895-gaia-nss.csv",
    "Fable 5/made/sb1-scale/marg9-persec/402940895-stack.png",
    "Fable 5/made/sb1-scale/marg9-persec/402940895.png",
    "Fable 5/made/sb1-scale/diffimg/c9-402940895-diffimg.md",
    "Fable 5/made/sb1-scale/diffimg/402940895/c9_diff402.json",
    "Fable 5/made/sb1-scale/diffimg/402940895-run.txt",
    "Fable 5/made/sb1-scale/diffimg/402940895/diff_s12.png",
    "Fable 5/made/sb1-scale/diffimg/402940895/diff_s39.png",
    "Fable 5/made/sb1-scale/diffimg/402940895/diff_s93.png",
    "Fable 5/made/sb1-scale/c710-xm-verdicts.md",
    "Astra/made/binary-extension-2026-11-04/catalogue-recovery/REPORT.md",
    "Astra/made/binary-extension-2026-11-04/catalogue-recovery/c57/coverage-matrix.csv",
    "Astra/made/binary-extension-2026-11-04/catalogue-recovery/c57/heartbeat-overlaps.json",
    "Astra/made/binary-extension-2026-11-04/catalogue-recovery/c57/chopard-overlaps.json",
    "Astra/made/binary-extension-2026-11-04/catalogue-recovery/c57/tarrants-mendes-overlaps.json",
    "Astra/made/binary-extension-2026-11-04/reassessment402940895/helper-audit.md",
    "Astra/made/binary-extension-2026-11-04/reassessment402940895/helper-audit.json",
    "sky/data/sb1-scale-c3/vet402940895/tesscut_s012.fits",
    "sky/data/sb1-scale-c3/vet402940895/tesscut_s039.fits",
    "sky/data/sb1-scale-c3/vet402940895/tesscut_s093.fits",
]
rows = []
for rel in paths:
    p = home / rel
    rows.append({"path": rel, "bytes": p.stat().st_size,
                 "sha256": hashlib.sha256(p.read_bytes()).hexdigest()})
result = {
    "target_tic": "402940895",
    "source_identity": "Gaia DR3 5816361019962769664, C57",
    "files": rows,
    "qlp_cache_at_reassessment": "Fable-reported %TEMP%/hunt-sb1-scale/402940895_s*.fits no longer present; no independent photometry rerun",
    "lead_checks": {
        "mean_of_five_window_depths_ppt": sum([5.361, 6.850, 7.885, 6.570, 7.286]) / 5,
        "on_phase_excess_empirical_units": (6790 - 47) / 527,
        "mean_deficit_east_arcsec": (3.84 - 6.43 + 1.11) / 3,
        "mean_deficit_north_arcsec": (-2.11 + 8.65 - 1.59) / 3,
        "inspected_panels": ["raw QLP window montage", "stacked profile/null/O-C", "s12/s39/s93 signed difference images"],
    },
}
out = Path(__file__).with_name("evidence.json")
out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(out)
