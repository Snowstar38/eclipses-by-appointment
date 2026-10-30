from pathlib import Path
p=Path('[local working path omitted]');s=p.read_text();s=s.replace("for sec in secs[:2]:jobs.append((tic,sec))", "if not secs: secs=[int(p.stem[-3:]) for p in sorted((r/tic).glob('qlp*.fits'))][-2:]\n for sec in secs[:2]:jobs.append((tic,sec))")
s=s.replace("tic,sec=job;d=targets[tic];", "tic,sec=job;d=targets[tic];")
p.with_name('tesscut_all.py').write_text(s)

