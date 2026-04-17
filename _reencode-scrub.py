#!/usr/bin/env python3
"""Re-encode vantage-resto-hero.mp4 for smooth cursor scrubbing.
  - GOP = 1  (every frame is a keyframe → instant seek)
  - no B-frames
  - faststart (moov atom at start)
  - downscaled to 1280 wide (keep quality, cut size)
"""
import subprocess, os, sys
from imageio_ffmpeg import get_ffmpeg_exe
FFMPEG = get_ffmpeg_exe()

SRC = 'vantage-resto-hero.mp4'
DST = 'vantage-resto-hero-scrub.mp4'

cmd = [
    FFMPEG, '-y', '-i', SRC,
    '-vf', 'scale=1280:-2,fps=24',
    '-c:v', 'libx264',
    '-preset', 'fast',
    '-g', '1',         # keyframe every frame
    '-bf', '0',        # no B-frames
    '-movflags', '+faststart',
    '-crf', '22',      # quality
    '-pix_fmt', 'yuv420p',
    '-an',
    DST
]
print('re-encoding for scrub...')
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode != 0:
    print(r.stderr[-2000:]); sys.exit(1)
print(f'[OK] {DST} {os.path.getsize(DST)//1024} KB')
