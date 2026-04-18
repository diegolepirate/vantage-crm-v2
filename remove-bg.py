#!/usr/bin/env python3
"""Remove backgrounds from Vantage hero photos.

Usage: python remove-bg.py
Inputs:  super_hero_1.jpg, super_hero_4.jpg  (project root)
Outputs: super_hero_1.png, super_hero_4.png  (transparent bg)

Requires: pip install rembg onnxruntime pillow
"""
import sys, os

INPUTS = ['super_hero_1.jpg', 'super_hero_4.jpg', 'super_hero_5.jpg', 'super_hero_6.jpg']

try:
    from rembg import remove
    from PIL import Image
except ImportError:
    print("rembg not installed. Install with:")
    print("    pip install rembg onnxruntime pillow")
    sys.exit(1)

for src in INPUTS:
    if not os.path.exists(src):
        print(f"[SKIP] {src} not found in project root")
        continue
    dst = src.replace('.jpg', '.png').replace('.jpeg', '.png')
    print(f"[PROC] {src} -> {dst}")
    with open(src, 'rb') as f:
        input_bytes = f.read()
    output_bytes = remove(input_bytes)
    with open(dst, 'wb') as f:
        f.write(output_bytes)
    with Image.open(dst) as im:
        print(f"       {im.size} · {im.mode}")

print("Done.")
