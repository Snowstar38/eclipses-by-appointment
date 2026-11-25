"""Event-level known asteroid geometry in a two-minute SPOC target pixel file."""
import argparse
import csv
import hashlib
import json
import math
import os
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
import re
import time
from urllib.parse import urlparse
from uuid import uuid4

import numpy as np
import requests
from astropy.coordinates import SkyCoord
from astropy.io import fits
from astropy.time import Time
from astropy.wcs import WCS

SKYBOT = "https://ssp.imcce.fr/webservices/skybot/api/conesearch.php"
HORIZONS = "https://ssd.jpl.nasa.gov/api/horizons.api"
HERE = Path(__file__).resolve().parent


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def put(path, data):
    tmp = path.with_name(path.name + "." + uuid4().hex)
    tmp.write_bytes(data)
    os.replace(tmp, path)


@contextmanager
def serial_jpl(cache):
    # OS locks release automatically on process termination.
    lock = (cache / "jpl.lock").open("a+b")
    try:
        if os.name == "nt":
            import msvcrt

            if lock.tell() == 0:
                lock.write(b"0")
                lock.flush()
            lock.seek(0)
            msvcrt.locking(lock.fileno(), msvcrt.LK_LOCK, 1)
        else:
            import fcntl

            fcntl.flock(lock, fcntl.LOCK_EX)
        yield
    finally:
        lock.close()


def fetch(url, params, cache, suffix):
    full_url = requests.Request("GET", url, params=params).prepare().url
    key = hashlib.sha256(full_url.encode()).hexdigest()
    path = cache / (key + suffix)
    meta_path = cache / (key + ".json.meta")
    if not (path.exists() and meta_path.exists()):
        response = requests.get(full_url, timeout=(15, 50))
        response.raise_for_status()
        data = response.content
        put(path, data)
        put(
            meta_path,
            json.dumps(
                dict(
                    url=full_url,
                    retrieved_utc=utc_now(),
                    http_status=response.status_code,
                    sha256=hashlib.sha256(data).hexdigest(),
                    bytes=len(data),
                )
            ).encode(),
        )
    meta = json.loads(meta_path.read_text())
    if hashlib.sha256(path.read_bytes()).hexdigest() != meta["sha256"]:
        raise ValueError(f"cached response digest mismatch: {path}")
    return path, meta


def search(observer, jd, center, radius, cache):
    pars = {
        "TIME": f"{jd:.8f}",
        "RA": f"{center.ra.deg:.8f}",
        "DEC": f"{center.dec.deg:.8f}",
        "SR": f"{radius:.8f}",
        "-observer": observer,
        "-loc": observer,
        "-objFilter": "100",
        "-filter": "0",
        "-mime": "text",
        "-output": "basic",
    }
    query = dict(
        observer=observer,
        epoch_jd_utc=jd,
        center_deg=[center.ra.deg, center.dec.deg],
        radius_deg=radius,
        query_parameters=pars,
    )
    try:
        path, query["receipt"] = fetch(SKYBOT, pars, cache, ".txt")
        lines = path.read_text(encoding="utf8").strip().splitlines()
        if not lines:
            raise ValueError("empty HTTP response; no catalogue verdict")
        flag = next(
            (s.split(":", 1)[1].strip() for s in lines if s.startswith("# Flag:")), ""
        )
        if flag == "0" and any(
            "no " in s.lower() and ("object" in s.lower() or "asteroid" in s.lower())
            for s in lines
        ):
            return dict(query, status="ok", candidates=[])
        if flag != "1":
            raise ValueError(" ".join(lines)[:550])
        header = next(
            i for i, line in enumerate(lines) if line.startswith("# Num | Name |")
        )
        fields = [s.strip() for s in lines[header].lstrip("# ").split("|")]
        objects = []
        for line in lines[header + 1 :]:
            if not line.strip():
                continue
            values = [s.strip() for s in line.split("|")]
            if len(values) != len(fields):
                raise ValueError("unrecognized cone-search row " + line[:160])
            r = dict(zip(fields, values))
            try:
                mag = float(r["Mv"])
                if not np.isfinite(mag):
                    mag = None
            except ValueError:
                mag = None
            objects.append(
                dict(
                    id=r["Num"] if r["Num"].isdigit() else r["Name"],
                    name=r["Name"],
                    mv=mag,
                    skybot=r,
                )
            )
        return dict(query, status="ok", candidates=objects)
    except (ValueError, OSError, StopIteration, KeyError) as e:
        return dict(
            query,
            status="unavailable",
            error=str(e) or "unexpected response",
            candidates=[],
        )


def horizons(obj, jd, cache):
    pars = dict(
        format="json",
        COMMAND=f"'{obj};'",
        CENTER="'500@-95'",
        EPHEM_TYPE="OBSERVER",
        QUANTITIES="'1,9'",
        CSV_FORMAT="YES",
        ANG_FORMAT="DEG",
        EXTRA_PREC="YES",
        CAL_FORMAT="BOTH",
        TIME_TYPE="UT",
        TLIST="'" + ",".join(f"{t:.8f}" for t in jd) + "'",
    )
    with serial_jpl(cache):
        path, receipt = fetch(HORIZONS, pars, cache, ".json")
    response = json.loads(path.read_bytes())
    result = response.get("result", "")
    if (
        not re.search(r"Center body name:\s+TESS \(spacecraft\) \(-95\)", result)
        or "$$SOE" not in result
    ):
        raise ValueError(
            str(response.get("error", result))[:350]
            + " [response "
            + receipt["sha256"]
            + "]"
        )
    target = next(
        s.split(":", 1)[1].strip()
        for s in result.splitlines()
        if s.startswith("Target body name:")
    )
    if obj.isdigit() and not re.match(re.escape(obj) + r"\b", target):
        raise ValueError(f"unexpected target {target}")
    header = next(s for s in result.splitlines() if "Date__(UT)" in s and "R.A." in s)
    cols = [s.strip() for s in header.split(",")]
    indices = [
        next(i for i, k in enumerate(cols) if k.startswith(prefix))
        for prefix in ("Date_________JD", "R.A.", "DEC")
    ]
    rows = list(
        csv.reader(result.split("$$SOE")[1].split("$$EOE")[0].strip().splitlines())
    )
    array = np.array([[float(row[i]) for i in indices] for row in rows])
    if len(jd) != len(array) or np.max(abs(array[:, 0] - jd)) > 2e-7:
        raise ValueError("Horizons did not return all requested epochs")
    return target, array, receipt


def intersects(a, b, x, y):
    # Parametric clipping against closed detector pixel squares, vectorized over mask pixels.
    lo, hi = np.zeros(len(x)), np.ones(len(x))
    valid = np.ones(len(x), dtype=bool)
    for first, last, c in zip(a, b, (x, y)):
        delta = last - first
        if abs(delta) < 1e-10:
            valid &= abs(first - c) <= 0.5
        else:
            s0, s1 = (c - 0.5 - first) / delta, (c + 0.5 - first) / delta
            lo = np.maximum(lo, np.minimum(s0, s1))
            hi = np.minimum(hi, np.maximum(s0, s1))
    return valid & (lo <= hi)


def closest_square_distance(a, b, x, y, hit):
    """Minimum distance of a straight segment to each closed unit pixel square."""
    a, b = np.array(a), np.array(b)
    centers = np.column_stack([x, y])
    start_dist = np.linalg.norm(np.maximum(abs(centers - a) - 0.5, 0), axis=1)
    end_dist = np.linalg.norm(np.maximum(abs(centers - b) - 0.5, 0), axis=1)
    nearest = np.minimum(start_dist, end_dist)
    delta = b - a
    length_squared = delta @ delta
    if length_squared:
        for corner in ((-0.5, -0.5), (-0.5, 0.5), (0.5, -0.5), (0.5, 0.5)):
            vectors = centers + corner - a
            fraction = np.clip(vectors @ delta / length_squared, 0, 1)
            nearest = np.minimum(
                nearest, np.linalg.norm(vectors - fraction[:, None] * delta, axis=1)
            )
    nearest[hit] = 0
    return nearest


def predict(obj, jd, wcs, mask, tracks, exposure, cache, margin):
    target, chunks, receipts = "", [], []
    for start in range(0, len(jd), 45):
        target, arr, ref = horizons(obj["id"], jd[start : start + 45], cache)
        chunks.append(arr)
        receipts.append(ref)
    data = np.vstack(chunks)
    xp, yp = wcs.world_to_pixel_values(data[:, 1], data[:, 2])
    if not (np.isfinite(xp).all() and np.isfinite(yp).all()):
        raise ValueError("path outside finite WCS domain")
    masks = {}
    for name, bit in [("background", 4), ("stellar", 2), ("collected", 1)]:
        y, x = np.where(mask & bit)
        pixels, segments, sampled = set(), [], 0
        closest = None
        for i, (a, b) in enumerate(zip(zip(xp[:-1], yp[:-1]), zip(xp[1:], yp[1:]))):
            hits = intersects(a, b, x, y)
            if len(x):
                dist = closest_square_distance(a, b, x, y, hits)
                k = np.argmin(dist)
                if closest is None or dist[k] < closest["distance_pixels"]:
                    closest = dict(
                        distance_pixels=float(dist[k]),
                        mask_pixel_xy=[int(x[k]), int(y[k])],
                        bracket_jd_utc=[float(jd[i]), float(jd[i + 1])],
                    )
            if hits.any():
                pixels.update(zip(x[hits].tolist(), y[hits].tolist()))
                segments.append([float(jd[i]), float(jd[i + 1])])
        xt = np.interp(exposure, jd, xp)
        yt = np.interp(exposure, jd, yp)
        for a, b in zip(xt, yt):
            sampled += int(np.any((abs(x - a) <= 0.5) & (abs(y - b) <= 0.5)))
        proximity = (
            "unavailable"
            if closest is None
            else "center_hit"
            if pixels
            else "nearby"
            if closest["distance_pixels"] <= margin
            else "distant"
        )
        masks[name] = dict(
            n_mask_pixels=len(x),
            hit_pixels_xy=sorted(pixels),
            closest_approach=closest,
            proximity=proximity,
            crossing_brackets_jd_utc=segments,
            n_quality0_midpoints_in_mask=sampled,
        )
    residuals = []
    for row in tracks:
        j = int(np.argmin(abs(jd - row["jd_utc"])))
        pos = SkyCoord(data[j, 1], data[j, 2], unit="deg")
        measured = SkyCoord(row["ra_deg"], row["dec_deg"], unit="deg")
        residuals.append(
            dict(
                **row, residual_arcsec=round(float(pos.separation(measured).arcsec), 3)
            )
        )
    path = [
        dict(
            jd_utc=float(t), ra_deg=float(ra), dec_deg=float(de), x=float(x), y=float(y)
        )
        for (t, ra, de), x, y in zip(data, xp, yp)
    ]
    return dict(
        status="verified",
        horizons_target=target,
        receipts=receipts,
        masks=masks,
        track_residuals=residuals,
        path=path,
    )


def run(args):
    cache = args.cache
    cache.mkdir(parents=True, exist_ok=True)
    if urlparse(args.tpf).scheme in ("http", "https"):
        file, fits_ref = fetch(args.tpf, {}, cache, ".fits")
    else:
        file = Path(args.tpf)
        fits_ref = dict(
            path=str(file.resolve()),
            sha256=hashlib.sha256(file.read_bytes()).hexdigest(),
        )
    with fits.open(file) as h:
        ph = h[0].header
        tic, sector = int(ph["TICID"]), int(ph["SECTOR"])
        mask = h["APERTURE"].data.copy()
        w = WCS(h["APERTURE"].header)
        tab = h[1]
        t = np.asarray(tab.data["TIME"])
        corr = np.asarray(tab.data["TIMECORR"])
        q = tab.data["QUALITY"]
        good = np.isfinite(t) & np.isfinite(corr)
        base = tab.header["BJDREFI"] + tab.header.get("BJDREFF", 0)
        if (
            tab.header.get("TIMESYS", "").upper() != "TDB"
            or abs(tab.header["TIMEDEL"] * 86400 - 120) > 3
        ):
            raise ValueError("Input must be a two-minute SPOC TDB time series")
        lo, hi = args.btjd - args.half_hours / 24, args.btjd + args.half_hours / 24
        if lo < t[good].min() or hi > t[good].max():
            raise ValueError("event window extends outside the TPF time range")
        selected = good & (t >= lo) & (t <= hi)
        utc = lambda v: Time(
            v - np.interp(v, t[good], corr[good]) + base, format="jd", scale="tdb"
        ).utc
        interval = utc(np.array([lo, args.btjd, hi])).jd
        exposure = utc(t[selected & (q == 0)]).jd
    ny, nx = mask.shape
    center = w.pixel_to_world((nx - 1) / 2, (ny - 1) / 2)
    corners = w.pixel_to_world(
        [-0.5, nx - 0.5, nx - 0.5, -0.5], [-0.5, -0.5, ny - 0.5, ny - 0.5]
    )
    footprint = float(center.separation(corners).deg.max())
    pad = args.margin_pixels
    padded = w.pixel_to_world(
        [-0.5 - pad, nx - 0.5 + pad, nx - 0.5 + pad, -0.5 - pad],
        [-0.5 - pad, -0.5 - pad, ny - 0.5 + pad, ny - 0.5 + pad],
    )
    padded_radius = float(center.separation(padded).deg.max())
    radius = padded_radius + args.speed * args.half_hours / 3600
    searches = [search("@tess", interval[1], center, radius, cache)]
    if searches[-1]["status"] != "ok":
        searches.append(
            search("500", interval[1], center, radius + args.geo_pad, cache)
        )
    candidates = searches[-1]["candidates"]
    tracks = []
    if args.track:
        for r in csv.DictReader(
            args.track.read_text(encoding="utf-8-sig").splitlines()
        ):
            if r.get("tic") and int(r["tic"]) != tic:
                continue
            epoch = Time(r["utc"], scale="utc").jd
            if interval[0] <= epoch <= interval[-1]:
                tracks.append(
                    dict(
                        utc=r["utc"],
                        jd_utc=epoch,
                        ra_deg=float(r["ra_deg"]),
                        dec_deg=float(r["dec_deg"]),
                    )
                )
    ids = {r["id"] for r in candidates}
    candidates = candidates + [
        dict(id=s, name=s, mv=None, manual=True) for s in args.object if s not in ids
    ]
    jd = np.unique(
        np.round(
            np.r_[
                np.linspace(
                    interval[0],
                    interval[-1],
                    max(2, math.ceil(args.half_hours * 120 / args.step_minutes) + 1),
                ),
                interval[1],
                [r["jd_utc"] for r in tracks],
            ],
            8,
        )
    )
    verified = []
    drawn = 0
    for obj in sorted(
        candidates,
        key=lambda r: (
            r["id"] not in args.object,
            float("inf") if r["mv"] is None else r["mv"],
        ),
    ):
        if obj["id"] not in args.object and (
            drawn >= args.max_objects
            or obj["mv"] is not None
            and obj["mv"] > args.max_mag
        ):
            verified.append(
                dict(
                    id=obj["id"],
                    name=obj["name"],
                    mv=obj["mv"],
                    status="outside propagation budget or magnitude limit",
                )
            )
            continue
        drawn += 1
        try:
            verdict = predict(obj, jd, w, mask, tracks, exposure, cache, pad)
        except (ValueError, OSError, KeyError, StopIteration, IndexError) as e:
            verdict = dict(
                status="ephemeris unavailable", error=str(e) or "unexpected response"
            )
        verified.append(
            dict(
                id=obj["id"],
                name=obj["name"],
                mv=obj["mv"],
                candidate_source="supplied ID" if obj.get("manual") else "SkyBoT",
                **verdict,
            )
        )
    mode = (
        "TESS"
        if searches[0]["status"] == "ok"
        else "geocentric fallback"
        if searches[-1]["status"] == "ok"
        else "search unavailable"
    )
    coverage = (
        "unavailable"
        if mode == "search unavailable"
        else "partial"
        if mode != "TESS" or any(o["status"] != "verified" for o in verified)
        else "bounded TESS search"
    )
    return dict(
        tic=tic,
        sector=sector,
        input_fits=fits_ref,
        center_btjd=args.btjd,
        half_hours=args.half_hours,
        interval_jd_utc=interval.tolist(),
        interval_utc=Time(interval, format="jd", scale="utc").isot.tolist(),
        quality0_midpoints=len(exposure),
        total_finite_midpoints=int(selected.sum()),
        max_quality0_gap_min=float(
            np.diff(np.r_[interval[0], exposure, interval[-1]]).max() * 1440
        ),
        stamp_shape_yx=list(mask.shape),
        stamp_corners_deg=np.c_[corners.ra.deg, corners.dec.deg].tolist(),
        footprint_radius_deg=footprint,
        midpoint_speed_allowance_arcsec_hour=args.speed,
        margin_pixels=pad,
        margin_padded_stamp_radius_deg=padded_radius,
        coverage=coverage,
        geo_padding_deg=args.geo_pad,
        propagation_magnitude_limit=args.max_mag,
        propagation_object_limit=args.max_objects,
        maximum_track_step_minutes=args.step_minutes,
        measured_positions_input=str(args.track) if args.track else None,
        search_mode=mode,
        searches=searches,
        objects=verified,
        interpretation="Nominal astrometric center against fixed pixel squares. The advisory margin expands both the cone footprint and mask proximity checks. The extent of measurable wings depends on source brightness and local PSF. No pointing jitter, saturation, PSF or orbit-error convolution. Window geometry includes gaps; quality-zero cadence counts are separate. A coincidence alone does not identify the cause of a dip. Midpoint search is bounded by assumed speed; geocentric padding cannot guarantee spacecraft completeness. Unknown asteroids and incomplete catalogs, excluded or unpropagated bodies remain unresolved.",
    )


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("tpf")
    p.add_argument("--btjd", type=float, required=True)
    p.add_argument("--half-hours", type=float, default=1.5)
    p.add_argument(
        "--track", type=Path, help="CSV with utc,ra_deg,dec_deg and optional tic"
    )
    p.add_argument("--max-mag", type=float, default=19)
    p.add_argument("--max-objects", type=int, default=8)
    p.add_argument(
        "--speed",
        type=float,
        default=120,
        help="Maximum expected angular speed (arcsec/hour) for midpoint search",
    )
    p.add_argument(
        "--geo-pad",
        type=float,
        default=0.3,
        help="Additional geocentric fallback padding (deg)",
    )
    p.add_argument(
        "--margin-pixels",
        type=float,
        default=2,
        help="Advisory margin for cone footprint and proximity to mask pixel edges",
    )
    p.add_argument("--step-minutes", type=float, default=5)
    p.add_argument(
        "--object",
        action="append",
        default=[],
        help="Extra or mandatory known asteroid number/designation; repeatable",
    )
    p.add_argument("--cache", type=Path, default=HERE / "cache")
    p.add_argument("--out", type=Path, required=True)
    a = p.parse_args()
    if (
        a.half_hours <= 0
        or a.step_minutes <= 0
        or min(a.geo_pad, a.speed, a.max_objects, a.margin_pixels) < 0
    ):
        p.error("invalid interval, grid, search padding or candidate budget")
    report = run(a)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    put(a.out, json.dumps(report, indent=2, allow_nan=False).encode())
    print(
        f"TIC {report['tic']}; {report['search_mode']}; coverage {report['coverage']}; {len(report['objects'])} candidate(s), including any supplied IDs."
    )
    for obj in report["objects"]:
        if obj["status"] == "verified":
            detail = []
            for name, m in obj["masks"].items():
                edge = m["closest_approach"]
                detail.append(
                    f"{name} {m['proximity']}"
                    + (f" ({edge['distance_pixels']:.2f} px)" if edge else "")
                )
            print(obj["id"], obj["name"], ", ".join(detail))
        else:
            print(obj["id"], obj["name"], obj["status"])
