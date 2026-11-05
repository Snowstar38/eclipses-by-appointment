"""Lead-owned encoding repair of finished Terra helper audit, with byte receipt."""
import hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent;p=B/'helper-audit.md';raw=p.read_bytes();before=hashlib.sha256(raw).hexdigest();backup=B/'helper-audit.cp1252.raw';backup.write_bytes(raw)
s=raw.decode('cp1252').replace('\u00b1','+/-').replace('\u2013','-')
p.write_text(s,encoding='utf-8');after=hashlib.sha256(p.read_bytes()).hexdigest()
(B/'lead-helper-encoding.json').write_text(json.dumps({'author':'Sol lead after Terra helper completed','file':str(p),'backup':str(backup),'before_sha256':before,'after_sha256':after,'reason':'Terra audit was CP1252 with non-UTF-8 bytes; only text encoding and two symbols converted to ASCII.'},indent=2)+'\n',encoding='utf-8')
print(before,after)
