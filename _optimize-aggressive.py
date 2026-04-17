#!/usr/bin/env python3
"""Aggressive second pass — reduce every resto video further for instant load."""
import subprocess, os, time
from imageio_ffmpeg import get_ffmpeg_exe
from concurrent.futures import ThreadPoolExecutor
FFMPEG = get_ffmpeg_exe()

# (source, width, crf, fps)
JOBS = [
    ('vantage-resto-hero.mp4',        1600, 25, 24),
    ('vantage-resto-fish.mp4',        1024, 26, 24),
    ('vantage-resto-pizza.mp4',       1024, 26, 24),
    ('vantage-resto-about.mp4',        720, 28, 24),
    ('vantage-resto-story.mp4',        720, 28, 24),
    ('resto-carousel-1-pizza.mp4',     960, 26, 24),
    ('resto-carousel-2-fish.mp4',      960, 26, 24),
    ('resto-carousel-3-burger.mp4',    960, 26, 24),
    ('resto-carousel-4-seafood.mp4',   960, 26, 24),
]

def encode(src, width, crf, fps):
    if not os.path.exists(src): return (src, 0, 0)
    tmp = src + '.tmp.mp4'
    before = os.path.getsize(src)
    cmd = [FFMPEG, '-y', '-i', src,
        '-vf', f'scale={width}:-2,fps={fps}',
        '-c:v', 'libx264', '-profile:v', 'main',
        '-preset', 'fast', '-crf', str(crf),
        '-pix_fmt', 'yuv420p',
        '-movflags', '+faststart', '-an', tmp]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f'  FAIL {src}: {r.stderr[-200:]}'); return (src, before, before)
    after = os.path.getsize(tmp)
    # only replace if smaller
    if after < before:
        os.replace(tmp, src)
        return (src, before, after)
    else:
        os.remove(tmp)
        return (src, before, before)

t0 = time.time()
total_b = total_a = 0
with ThreadPoolExecutor(max_workers=3) as ex:
    for src, b, a in ex.map(lambda j: encode(*j), JOBS):
        total_b += b; total_a += a
        if b and b != a:
            print(f'  {src}:  {b//1024} KB -> {a//1024} KB  ({100-a*100//b}% smaller)')
        elif b:
            print(f'  {src}:  skipped (already smaller)')

print(f'\nTOTAL: {total_b//1024} KB -> {total_a//1024} KB  ({100-total_a*100//max(total_b,1)}% saved) in {time.time()-t0:.0f}s')
