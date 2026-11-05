from pathlib import Path
for p in Path(__file__).parent.rglob('*'):
 if p.is_file() and p.suffix.lower() in ('.md','.json','.csv','.py','.txt'):
  try:p.read_text(encoding='utf8')
  except UnicodeError as e:print(p,e)
