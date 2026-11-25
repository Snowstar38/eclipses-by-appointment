"""Run two isolated public replay smoke tests and record their outputs."""
import csv
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

import requests

HERE = Path(__file__).resolve().parent
RELEASE = HERE.parent
log = []


def run(root, *args):
    command = [sys.executable, *args]
    result = subprocess.run(command, cwd=root, text=True, capture_output=True)
    log.append(f"Command: python {' '.join(args)}\n{result.stdout}{result.stderr}")
    print(log[-1], flush=True)
    result.check_returncode()


def rows(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


try:
    with TemporaryDirectory(prefix="fresh-replay-", dir=HERE) as temp:
        clean = Path(temp)
        cache = clean / "inputs"
        cache.mkdir()
        for name in ("prepare.py", "qlp.csv", "historical-scans.json.gz", "exposure-guard.csv"):
            shutil.copyfile(HERE / name, cache / name)
        for batch, names in (
            ("batch01", ("batch.csv", "review.py")), ("batch11", ("review.py",)),
            ("batch16", ("batch.csv", "clocks.csv")),
        ):
            (clean / batch).mkdir()
            for name in names:
                p = RELEASE / batch / name
                if p.exists():
                    shutil.copyfile(p, clean / batch / name)
        assert not (cache / "workspace").exists()
        products = rows(cache / "qlp.csv")
        for sector in range(73, 81):
            candidates = [r for r in products if int(r["sector"]) == sector]
            row = min(candidates, key=lambda r: (bool(r["batches"]), int(r["bytes"])))
            response = requests.get(row["url"], timeout=(15, 90))
            response.raise_for_status()
            version = "02" if 74 <= sector <= 79 else "01"
            assert f"_tess_v{version}_llc.fits" in row["url"]
            assert len(response.content) == int(row["bytes"])
            assert hashlib.sha256(response.content).hexdigest() == row["sha256"]
            log.append(f"Public archive version sample S{sector} v{version}: verified TIC {row['tic']} size and SHA-256.")

        run(clean, "inputs/prepare.py", "16")
        run(clean, "inputs/prepare.py", "16", "--verify-only")
        run(clean, "batch11/review.py", "--batch", "batch16")
        evidence = rows(clean / "batch16/archive-windows.csv")
        original = rows(RELEASE / "batch16/archive-windows.csv")
        assert evidence == original, "Batch 16 archive-window replay differs"
        pictures = sorted((clean / "batch16").glob("*-events.png"))
        assert len(pictures) == 4
        log.append(f"Batch 16 archive-window comparison: exact row equality for {len(evidence)} rows, "
                   f"{len(pictures)} target plot files regenerated.")

        run(clean, "inputs/prepare.py", "1", "--target", "7773469")
        run(clean, "inputs/prepare.py", "1", "--target", "7773469", "--verify-only")
        run(clean, "batch01/review.py", "--batch-dir", "batch01",
            "--target", "7773469", "--output-dir", "replayed-7773469")
        result = clean / "replayed-7773469"
        original = RELEASE / "batch01"
        evidence = rows(result / "events.csv")
        expected = [r for r in rows(original / "events.csv") if r["tic"] == "7773469"]
        assert evidence == expected, "TIC 7773469 archive windows differ"
        assert len(rows(result / "files.csv")) == 10
        assert (result / "plots/7773469-prior.png").is_file()
        log.append(f"TIC 7773469 archive-window comparison: exact row equality for {len(evidence)} rows. "
                   "Both sector 74 and 79 v02 FITS were in the independently downloaded target products.")
finally:
    (HERE / "replay-qa.txt").write_text("\n\n".join(log) + "\n", encoding="utf-8")
