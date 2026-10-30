from pathlib import Path
p=Path('[local working path omitted]');s=p.read_text().replace(",(80,3505.734)","");s=s.replace("out=old.copy()", "out=old.copy()")
p.write_text(s)
