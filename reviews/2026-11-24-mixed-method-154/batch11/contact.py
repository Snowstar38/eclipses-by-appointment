"""Make compact sheets of each target's local light-curve panels."""
import argparse
from pathlib import Path
from PIL import Image


def make(batch):
    files = sorted(batch.glob("*-events.png"))
    for offset in range(0, len(files), 5):
        sheet = Image.new("RGB", (1320, 1000), "white")
        for slot, filename in enumerate(files[offset:offset+5]):
            with Image.open(filename) as source:
                panel = source.convert("RGB")
            panel.thumbnail((650,328))
            sheet.paste(panel, (slot%2*660, slot//2*333))
        sheet.save(batch/f"visual-guide-{offset//5+1}.jpg", quality=90)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=Path, required=True)
    make(parser.parse_args().batch)
