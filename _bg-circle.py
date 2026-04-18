#!/usr/bin/env python3
"""Bg removal for hero-circle video using rembg isnet-general-use (good on objects)."""
import os, subprocess, shutil, tempfile, time
from imageio_ffmpeg import get_ffmpeg_exe
from rembg import remove, new_session
FFMPEG = get_ffmpeg_exe()

SRC, DST = 'vantage-hero-circle.mp4', 'vantage-hero-circle.webm'
FPS, SCALE = 24, 640
MODEL = 'isnet-general-use'

workdir = tempfile.mkdtemp(prefix='vt_bg_')
fin, fout = os.path.join(workdir,'in'), os.path.join(workdir,'out')
os.makedirs(fin); os.makedirs(fout)

print('[1] extract frames')
subprocess.run([FFMPEG,'-y','-i',SRC,'-vf',f'fps={FPS},scale={SCALE}:-2',os.path.join(fin,'%05d.png')],check=True,capture_output=True)
frames = sorted(os.listdir(fin))
print(f'    {len(frames)} frames')

print(f'[2] rembg {MODEL}')
session = new_session(MODEL)
t0 = time.time()
for i, fn in enumerate(frames, 1):
    with open(os.path.join(fin,fn),'rb') as f: data = f.read()
    out = remove(data, session=session)
    with open(os.path.join(fout,fn),'wb') as f: f.write(out)
    if i % 20 == 0: print(f'    {i}/{len(frames)}  {time.time()-t0:.0f}s')

print('[3] encode webm vp9 alpha')
subprocess.run([FFMPEG,'-y','-framerate',str(FPS),'-i',os.path.join(fout,'%05d.png'),
    '-c:v','libvpx-vp9','-pix_fmt','yuva420p','-b:v','1800k','-auto-alt-ref','0','-an',DST],check=True,capture_output=True)
shutil.rmtree(workdir, ignore_errors=True)
print(f'[OK] {DST} {os.path.getsize(DST)//1024} KB')
