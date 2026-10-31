"""Validate the four KELT .tbl files fetched for HD 282670 (untrusted downloads) and
write one plain table: bjd  orient(0=east,1=west)  proc(0=raw,1=tfa)  mag  err.
Stdlib only, meant to run as  python -I keltclean.py dl hd282670_kelt.txt
"""
import os, re, sys

NUM = re.compile(r"^[-+]?\d+(\.\d+)?$")

def main():
    src, out = sys.argv[1], sys.argv[2]
    rows = []
    for fn in sorted(os.listdir(src)):
        if not fn.endswith("_lc.tbl"):
            continue
        orient = 1 if "_west_" in fn else 0
        proc = 1 if "_tfa_" in fn else 0
        n = 0; bad = 0; shifted = 0
        with open(os.path.join(src, fn), encoding="ascii", errors="strict") as f:
            for line in f:
                if line.startswith(("\\", "|")) or not line.strip():
                    continue
                parts = line.split()
                if len(parts) != 3 or not all(NUM.match(p) for p in parts):
                    raise SystemExit(f"{fn}: bad line {line!r}")
                t, m, e = (float(p) for p in parts)
                if 4900000 < t < 4920000:     # S36 east TFA: TIME carries 2450000 twice; the raw file of the same source is fine
                    t -= 2450000; shifted += 1
                if not (2450000 < t < 2470000 and 5 < m < 25 and 0 < e < 1):
                    bad += 1; continue        # a corrupt row (seen once in S36: a JD of 4906428); counted, skipped
                rows.append((t, orient, proc, m, e)); n += 1
        if bad > max(3, n // 100):
            raise SystemExit(f"{fn}: {bad} out-of-range rows against {n} good: refusing the file")
        print(f"{fn}: {n} rows" + (f", {bad} out-of-range rows skipped" if bad else "") + (f", {shifted} times shifted by -2450000" if shifted else ""))
    rows.sort()
    with open(out, "w") as f:
        for t, o, p, m, e in rows:
            f.write(f"{t:.6f} {o} {p} {m:.5f} {e:.5f}\n")
    print(f"wrote {len(rows)} rows to {out}")

if __name__ == "__main__":
    main()
