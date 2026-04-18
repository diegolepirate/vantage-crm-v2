#!/usr/bin/env python3
"""Remove the background from vantage-hero.mp4 frame-by-frame.

Pipeline:
  1. Extract every frame as PNG using ffmpeg (from imageio_ffmpeg).
  2. Run rembg on every frame (in-memory, no disk roundtrip per frame).
  3. Re-encode as WebM with alpha channel (VP9 yuva420p).

Output: vantage-hero.webm  (transparent background, loopable)
Keep:   vantage-hero.mp4    (fallback — still referenced as secondary source)

Usage: python remove-bg-video.py
"""
import os, sys, subprocess, shutil, tempfile, time

SRC      = 'vantage-hero.mp4'
DST      = 'vantage-hero.webm'
FPS      = 24               # reduce from source fps if needed to keep size sane
SCALE    = 512              # downscale longest side to keep processing fast
MODEL    = 'u2net_human_seg' # faster than default, optimised for humans

from imageio_ffmpeg import get_ffmpeg_exe
FFMPEG = get_ffmpeg_exe()

from rembg import remove, new_session
from PIL import Image
import io

if not os.path.exists(SRC):
    print(f"ERROR: {SRC} not found"); sys.exit(1)

print(f"[1/4] Probing {SRC}...")
info = subprocess.run([FFMPEG, '-i', SRC], capture_output=True, text=True).stderr
print("      " + [l for l in info.splitlines() if 'Duration' in l][0].strip())

workdir = tempfile.mkdtemp(prefix='vt_bg_')
frames_in  = os.path.join(workdir, 'in')
frames_out = os.path.join(workdir, 'out')
os.makedirs(frames_in);  os.makedirs(frames_out)

print(f"[2/4] Extracting frames to {frames_in}")
t0 = time.time()
subprocess.run([
    FFMPEG, '-y', '-i', SRC,
    '-vf', f'fps={FPS},scale={SCALE}:-2',
    os.path.join(frames_in, '%05d.png')
], check=True, capture_output=True)
frames = sorted(os.listdir(frames_in))
print(f"      {len(frames)} frames in {time.time()-t0:.1f}s")

print(f"[3/4] Removing bg with rembg (model={MODEL})...")
t0 = time.time()
session = new_session(MODEL)
for i, fn in enumerate(frames, 1):
    with open(os.path.join(frames_in, fn), 'rb') as f:
        data = f.read()
    out = remove(data, session=session)
    with open(os.path.join(frames_out, fn), 'wb') as f:
        f.write(out)
    if i % 10 == 0 or i == len(frames):
        eta = (time.time()-t0) / i * (len(frames)-i)
        print(f"      {i}/{len(frames)}  ETA {eta:.0f}s")
print(f"      done in {time.time()-t0:.1f}s")

print(f"[4/4] Encoding {DST} (VP9 yuva420p alpha)...")
t0 = time.time()
subprocess.run([
    FFMPEG, '-y',
    '-framerate', str(FPS),
    '-i', os.path.join(frames_out, '%05d.png'),
    '-c:v', 'libvpx-vp9',
    '-pix_fmt', 'yuva420p',
    '-b:v', '1500k',
    '-auto-alt-ref', '0',
    '-an',
    DST
], check=True, capture_output=True)
print(f"      wrote {DST} in {time.time()-t0:.1f}s ({os.path.getsize(DST)//1024} KB)")

shutil.rmtree(workdir, ignore_errors=True)
print("Done.")
