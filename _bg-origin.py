#!/usr/bin/env python3
"""One-shot: remove bg from vantage-origin.mp4 → vantage-origin.webm"""
import os, sys, subprocess, shutil, tempfile, time
from imageio_ffmpeg import get_ffmpeg_exe
from rembg import remove, new_session
FFMPEG = get_ffmpeg_exe()

SRC, DST = 'vantage-origin.mp4', 'vantage-origin.webm'
FPS, SCALE, MODEL = 24, 512, 'u2net_human_seg'

workdir = tempfile.mkdtemp(prefix='vt_bg_')
fin, fout = os.path.join(workdir,'in'), os.path.join(workdir,'out')
os.makedirs(fin); os.makedirs(fout)
print('[1] extract frames')
subprocess.run([FFMPEG,'-y','-i',SRC,'-vf',f'fps={FPS},scale={SCALE}:-2',os.path.join(fin,'%05d.png')],check=True,capture_output=True)
frames = sorted(os.listdir(fin))
print(f'    {len(frames)} frames')
print('[2] rembg')
session = new_session(MODEL)
t0 = time.time()
for i, fn in enumerate(frames, 1):
    with open(os.path.join(fin,fn),'rb') as f: data = f.read()
    out = remove(data, session=session)
    with open(os.path.join(fout,fn),'wb') as f: f.write(out)
    if i % 20 == 0: print(f'    {i}/{len(frames)}  elapsed {time.time()-t0:.0f}s')
print('[3] encode webm vp9 alpha')
subprocess.run([FFMPEG,'-y','-framerate',str(FPS),'-i',os.path.join(fout,'%05d.png'),
    '-c:v','libvpx-vp9','-pix_fmt','yuva420p','-b:v','1500k','-auto-alt-ref','0','-an',DST],check=True,capture_output=True)
shutil.rmtree(workdir, ignore_errors=True)
print(f'[OK] {DST} {os.path.getsize(DST)//1024} KB')
