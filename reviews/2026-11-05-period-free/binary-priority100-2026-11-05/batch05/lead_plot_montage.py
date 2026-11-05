import csv
from pathlib import Path
from PIL import Image,ImageDraw
B=Path(__file__).resolve().parent
q=list(csv.DictReader((B/'queue.csv').open(encoding='utf-8',newline='')))
can=Image.new('RGB',(1800,1800),'white')
for i,row in enumerate(q[2:]):
    p=B/row['tic']/'lead-raw-01.png'
    if not p.exists():continue
    im=Image.open(p).convert('RGB');im.thumbnail((880,420))
    if im.height>420:im=im.crop((0,0,im.width,420))
    x=i%2*900;y=i//2*450
    can.paste(im,(x,y+24));ImageDraw.Draw(can).text((x+5,y+5),row['sample_id']+' TIC '+row['tic'],fill='black')
can.save(B/'lead-plot-montage.png')
