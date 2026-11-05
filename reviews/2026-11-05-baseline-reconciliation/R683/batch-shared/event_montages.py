from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
here=Path(__file__).resolve().parent
for d in sorted(p for p in here.iterdir() if p.is_dir() and p.name.isdigit()):
    paths=sorted(d.glob('event-*.png'))
    page=Image.new('RGB',(1600,((len(paths)+1)//2)*470),'white')
    for j,p in enumerate(paths):
        im=ImageOps.contain(Image.open(p).convert('RGB'),(780,440))
        x=j%2*800+10;y=j//2*470+10
        page.paste(im,(x,y))
    page.save(d/'event-montage.png')
    print(d.name,len(paths))
