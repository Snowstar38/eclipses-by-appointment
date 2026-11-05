from pathlib import Path
root=Path(__file__).resolve().parent
bad=[];replacement=[]
for path in root.rglob('*'):
 if path.suffix.lower() not in ('.md','.py'):continue
 try:
  text=path.read_text(encoding='utf-8')
  if '\ufffd' in text:replacement.append(str(path.relative_to(root)))
 except UnicodeDecodeError:bad.append(str(path.relative_to(root)))
print('invalid_utf8',bad)
print('replacement_characters',replacement)
