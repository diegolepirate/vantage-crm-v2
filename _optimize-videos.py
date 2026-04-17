#!/usr/bin/env python3
"""Optimize every MP4 in the resto template for instant web load.

For each source:
  - scale down to target width (keep aspect ratio)
  - h264 main profile, CRF 24 (good quality, small)
  - -movflags +faststart (moov atom at start → playback begins while downloading)
  - drop audio (all are decorative)
  - output prefixed 'opt_' so we can diff sizes

Mapping:
  source                          -> output           width  target_size
  vantage-resto-hero.mp4          -> hero             1920   ~4-5 MB
  vantage-resto-fish.mp4          -> fish             1280   ~1.5 MB
  vantage-resto-pizza.mp4         -> pizza            1280   ~2 MB (was 61 MB!)
  _carousel-1-pizza.mp4           -> carousel-pizza   1280   ~1.5 MB
  _carousel-2-fish.mp4            -> carousel-fish    1280   ~1 MB
  _carousel-3-burger.mp4          -> carousel-burger  1280   ~1 MB
  _carousel-4-seafood.mp4         -> carousel-seafood 1280   ~1 MB
"""
import subprocess, os, sys
from imageio_ffmpeg import get_ffmpeg_exe
FFMPEG = get_ffmpeg_exe()

JOBS = [
    ('vantage-resto-hero.mp4',   'vantage-resto-hero.opt.mp4',   1920, 23),
    ('vantage-resto-fish.mp4',   'vantage-resto-fish.opt.mp4',   1280, 25),
    ('vantage-resto-pizza.mp4',  'vantage-resto-pizza.opt.mp4',  1280, 25),
    ('_carousel-1-pizza.mp4',    'resto-carousel-1-pizza.mp4',   1280, 25),
    ('_carousel-2-fish.mp4',     'resto-carousel-2-fish.mp4',    1280, 25),
    ('_carousel-3-burger.mp4',   'resto-carousel-3-burger.mp4',  1280, 25),
    ('_carousel-4-seafood.mp4',  'resto-carousel-4-seafood.mp4', 1280, 25),
]

total_before = 0
total_after  = 0

for src, dst, width, crf in JOBS:
    if not os.path.exists(src):
        print(f'[SKIP] {src} not found'); continue
    before = os.path.getsize(src)
    total_before += before
    cmd = [
        FFMPEG, '-y', '-i', src,
        '-vf', f'scale={width}:-2',
        '-c:v', 'libx264',
        '-profile:v', 'main',
        '-preset', 'medium',
        '-crf', str(crf),
        '-pix_fmt', 'yuv420p',
        '-movflags', '+faststart',
        '-an',
        dst,
    ]
    print(f'[RUN] {src}  ({before//1024} KB) -> {dst}')
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print('    FAILED:', r.stderr[-400:]); continue
    after = os.path.getsize(dst)
    total_after += after
    print(f'      {before//1024} KB -> {after//1024} KB  ({100 - after*100//before}% smaller)')

print(f'\n[TOTAL] {total_before//1024} KB -> {total_after//1024} KB')
print(f'        saved {(total_before-total_after)//1024} KB  ({100 - total_after*100//max(total_before,1)}% smaller)')
