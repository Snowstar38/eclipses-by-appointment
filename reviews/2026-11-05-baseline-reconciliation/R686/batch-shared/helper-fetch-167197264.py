"""Adaptive older-sector check of a preserved single; frozen screening unchanged."""
import hashlib
import json
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np
from astropy.io import fits

HERE = Path(__file__).resolve().parent
SEARCH = HERE.parent / "search256"
TIC = "167197264"
TARGET = json.loads((SEARCH / "fresh-targets-256.json").read_text())[TIC]
SECTORS = (15, 55, 56, 75)
SOURCE_HASHES = {
    name: hashlib.sha256((SEARCH / name).read_bytes()).hexdigest()
    for name in ("fresh-targets-256.json", "screening.jsonl", "downloads.json")
}
OUT = []
for sector in SECTORS:
    uris = [uri for s, uri in TARGET["qlp_all"] if s == sector]
    receipt = {
        "tic": TIC,
        "sector": sector,
        "selection_reason": "Preserved credible s88 single; older available QLP sector could show an independent recurrence.",
        "uri": uris[0] if len(uris) == 1 else None,
    }
    try:
        if len(uris) != 1:
            raise ValueError("Nonunique archive product")
        url = "https://mast.stsci.edu/api/v0.1/Download/file?" + urllib.parse.urlencode({"uri": uris[0]})
        with urllib.request.urlopen(url, timeout=120) as response:
            raw = response.read(15_000_001)
        if len(raw) > 15_000_000:
            raise ValueError("FITS exceeds size cap")
        path = HERE / f"helper-{TIC}_s{sector:03d}.fits"
        path.write_bytes(raw)
        with fits.open(path) as h:
            hdr = h[0].header
            identity = {k: str(hdr.get(k)) for k in ("TICID", "TIC_ID", "SECTOR", "OBJECT", "TELESCOP")}
            t = np.asarray(h[1].data["TIME"], float)
            q = np.asarray(h[1].data["QUALITY"], int)
            good = np.isfinite(t) & (q == 0)
        if TIC not in (identity["TICID"], identity["TIC_ID"], identity["OBJECT"].removeprefix("TIC ")):
            raise ValueError(f"TIC mismatch: {identity}")
        if identity["SECTOR"] != "None" and int(identity["SECTOR"]) != sector:
            raise ValueError(f"Sector mismatch: {identity}")
        receipt.update(status="ok", path=str(path), sha256=hashlib.sha256(raw).hexdigest(), bytes=len(raw),
                       fits_identity=identity, q0_n=int(good.sum()),
                       q0_btjd_span=[float(t[good].min()), float(t[good].max())] if good.any() else None)
    except Exception as exc:
        receipt.update(status="error", error=repr(exc))
    OUT.append(receipt)
    print(sector, receipt["status"], receipt.get("q0_btjd_span"), receipt.get("error", ""), flush=True)
(HERE / "helper-downloads-167197264.json").write_text(json.dumps({"source_sha256": SOURCE_HASHES, "products": OUT}, indent=2))

