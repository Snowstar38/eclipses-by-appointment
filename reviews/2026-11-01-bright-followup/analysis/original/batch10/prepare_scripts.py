from pathlib import Path

B=Path(__file__).parent
S=B.parent/'batch01'
for name in ['review_measure.py','alias_audit.py','geometry.py','freeze_hashes.py']:
    t=(S/name).read_text(encoding='utf-8')
    if name=='review_measure.py':
        t=t.replace("c6-sapdepth.json", "c7-sapdepth.json")
        t=t.replace("(5 if tic=='351335839' else 3)*dur", "3*dur")
        a=t.index(" for e in event[local path omitted]  if tic=='89553209'")
        b=t.index(" good=[e for e in events", a)
        t=t[:a]+t[b:]
        a=t.index(" if tic in ('48752905','351335839'):")
        b=t.index(" summary['timing_event_count']", a)
        t=t[:a]+" summary['epoch_kind']='Selected repeating eclipse; primary by convention; deeper/secondary identity not independently established'\n"+t[b:]
    if name=='alias_audit.py':
        t=t.replace("tic not in ('48752905','351335839') or e['cycle']%2==0", "True")
        t=t.replace("(2 if tic in ('48752905','351335839') else 1)", "1")
    if name=='freeze_hashes.py':
        t=t.replace("c6-sapdepth.json", "c7-sapdepth.json").replace("c6-catrows.md", "c7-catrows.md")
    (B/name).write_text(t,encoding='utf-8')
