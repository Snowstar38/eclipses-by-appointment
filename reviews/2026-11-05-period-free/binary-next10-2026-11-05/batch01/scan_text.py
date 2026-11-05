"""Reject replacement characters, C1 controls and common cp1252 mojibake heads."""
from pathlib import Path
B=Path(__file__).resolve().parent
bad=[];count=0
for p in B.rglob('*'):
    if p.is_file() and p.suffix.lower() in {'.py','.json','.md','.csv','.txt'}:
        count+=1;s=p.read_text(encoding='utf8')
        hits={hex(ord(c)):s.count(c) for c in set(s) if c in '\u00e2\u00c3\u00c2\ufffd' or 128<=ord(c)<160}
        if hits:bad.append((str(p),hits))
print('text_files',count,'suspect',bad)
assert not bad
