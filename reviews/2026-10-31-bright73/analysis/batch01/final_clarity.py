from pathlib import Path
p=Path('[local path omitted]');s=p.read_text().replace("else 'usable; same-kind selection applies'", "else 'measured; excluded from primary fit (secondary)' if tic in ('48752905','351335839') and e['cycle']%2 else 'used in ephemeris'");p.write_text(s);exec(compile(s,str(p),'exec'))
