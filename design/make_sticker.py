#!/usr/bin/env python3
"""Generate 'JESUS IS FAT PHOBIC' bumper sticker artwork.
Print size: 7.5 x 3.75 in @ 300 DPI = 2250 x 1125 px (StickerMule bumper sticker).
Classic Christian-fish bumper sticker format, black on yellow.
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 2250, 1125          # 7.5" x 3.75" @ 300dpi
BG   = (255, 204, 0)       # classic bumper yellow
INK  = (0, 0, 0)
FONT_PATH = "C:/Windows/Fonts/impact.ttf"

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# --- outer frame (classic sticker border) ---
m = 46  # outer margin
d.rectangle([m, m, W - m, H - m], outline=INK, width=14)

# --- Christian fish (ichthys), faces left ---
body = [168, 240, 1870, 885]                 # ellipse bbox
tail = [(1832, 562), (2108, 398), (2108, 726)]
outline_w = 16
d.ellipse(body, outline=INK, width=outline_w)
d.line([tail[0], tail[1], tail[2], tail[0]], fill=INK, width=outline_w, joint="curve")
# eye
d.ellipse([560, 430, 640, 510], fill=INK)

# --- text inside fish ---
f1 = ImageFont.truetype(FONT_PATH, 172)
f2 = ImageFont.truetype(FONT_PATH, 172)

def center_text(y, text, font):
    bbox = d.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (W - tw) / 2 - bbox[0]
    d.text((x, y), text, font=font, fill=INK)

center_text(408, "JESUS IS", f1)
center_text(598, "FAT PHOBIC", f2)

out_dir = "C:/Users/power/projects/jesus-fat-phobic/design"
os.makedirs(out_dir, exist_ok=True)
print_path = f"{out_dir}/bumper-sticker-print-300dpi.png"
preview_path = f"{out_dir}/bumper-sticker-preview.png"
img.save(print_path, dpi=(300, 300))
img.resize((900, 450), Image.LANCZOS).save(preview_path)
print("saved:", print_path)
print("saved:", preview_path)
