#!/usr/bin/env python3
"""Extract hero video as a JPG frame sequence for smooth cursor scrubbing.
Apple-style: preloaded <img> swap is buttery-smooth vs video seek.
"""
import subprocess, os, shutil, sys
from imageio_ffmpeg import get_ffmpeg_exe
FFMPEG = get_ffmpeg_exe()

SRC       = 'vantage-resto-hero.mp4'
OUT_DIR   = 'resto-frames'
FPS       = 15          # 15fps — smooth scrub without oversize payload
WIDTH     = 1920        # full HD — matches hero section on 2K displays
QUALITY   = 3           # ffmpeg mjpeg quality (2=best, 31=worst) → ~q94, very high

if os.path.isdir(OUT_DIR): shutil.rmtree(OUT_DIR)
os.makedirs(OUT_DIR)

cmd = [
    FFMPEG, '-y', '-i', SRC,
    '-vf', f'fps={FPS},scale={WIDTH}:-2',
    '-q:v', str(QUALITY),
    os.path.join(OUT_DIR, 'f_%03d.jpg'),
]
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode != 0: print(r.stderr[-2000:]); sys.exit(1)

frames = sorted(os.listdir(OUT_DIR))
total_kb = sum(os.path.getsize(os.path.join(OUT_DIR, f)) for f in frames) // 1024
print(f'[OK] {len(frames)} frames  ~{total_kb} KB total  (avg {total_kb//len(frames)} KB/frame)')
print(f'     paths: {OUT_DIR}/f_001.jpg ... f_{len(frames):03d}.jpg')
