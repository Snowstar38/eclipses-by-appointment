from PIL import Image,ImageOps,ImageDraw
from pathlib import Path
b=Path(__file__).parent.parent
files=sorted(b.glob('*/raw-events.png'))
for f in files:
 im=Image.open(f);print(f.parent.name,im.size)
