from pathlib import Path
from PIL import Image, ImageDraw
import csv

B=Path(__file__).resolve().parent
Q=list(csv.DictReader((B/'queue.csv').open()))
for source,name in [(B.parent/'source-packets','source-preview-contact.png'),(B,'raw-window-contact.png')]:
    canvas=Image.new('RGB',(1800,5*620),'white')
    d=ImageDraw.Draw(canvas)
    for i,q in enumerate(Q):
        p=(source/q['tic']/('raw-preview.png' if source!=B else 'raw-windows.png'))
        im=Image.open(p).convert('RGB')
        im.thumbnail((880,580))
        x=(i%2)*900+(900-im.width)//2;y=(i//2)*620+32
        canvas.paste(im,(x,y))
        d.text(((i%2)*900+10,(i//2)*620+5),f"{q['sample_id']} TIC {q['tic']}",fill='black')
    canvas.save(B/name)
