import hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent
files=[Path('[local-path-redacted] 5.1/made/appointments/vet20/REPORT.md'),Path('[local-path-redacted] 5.1/made/appointments/vet20/s5_diff.py'),Path('[local-path-redacted] 5.1/made/appointments/vet20/s7_nbr17238865.py'),Path('[local-path-redacted] 5.1/made/appointments/vet20/diff_17238861_s21.png'),Path('[local-path-redacted] 5.1/made/appointments/vet20/diff_17238861_s48.png'),Path('[local-path-redacted] 5.1/made/appointments/vet20/nbr_17238865.txt'),B/'raw-montage.jpg',B/'236223193/lead-event-panels.png',B/'28059397/helper-alias.json',B/'helper_alias.py']
(B/'helper-source-hashes.json').write_text(json.dumps([{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files],indent=2)+'\n',encoding='utf-8')
