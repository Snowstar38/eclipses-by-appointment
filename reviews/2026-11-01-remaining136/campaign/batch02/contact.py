from pathlib import Path
import csv,json
from PIL import Image,ImageOps,ImageDraw
B=Path('local-source/Astra/made/remaining136-2026-11-01/batch02');S=Path('local-source/Fable 5/made/sb1-scale/diffimg')
rows=list(csv.DictReader(open(B/'queue.csv')))
for kind in ['raw','pixel']:
 canvas=Image.new('RGB',(1400,5*520),'white')
 for i,r in enumerate(rows):
  p=B/r['tic']/'raw-events.png' if kind=='raw' else next((S/r['tic']).glob('diff_s*.png'))
  im=Image.open(p).convert('RGB');im.thumbnail((690,490));x=(i%2)*700;y=(i//2)*520;canvas.paste(im,(x,y+25));ImageDraw.Draw(canvas).text((x+10,y+5),r['tic'],fill='black')
 canvas.save(B/(kind+'-contact.png'))


