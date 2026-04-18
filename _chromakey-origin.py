#!/usr/bin/env python3
"""Chromakey bg removal for vantage-origin.mp4 (green screen → alpha)."""
import subprocess, os, sys
from imageio_ffmpeg import get_ffmpeg_exe
FFMPEG = get_ffmpeg_exe()

SRC, DST = 'vantage-origin.mp4', 'vantage-origin.webm'

# Sample the bg green, pick a central key color, then chromakey + despill
# 0x1BD743 is a typical bright green chroma key
# Tolerance 0.18, blend 0.12 gives soft edges
filter_complex = (
    'chromakey=0x1BD743:0.20:0.08,'           # knock out green
    'despill=type=green:mix=0.4:expand=0.05,' # remove green fringe (if available)
    'format=yuva420p'
)

# Some ffmpeg builds don't have despill — fallback to colorkey
simple_filter = 'colorkey=0x1BD743:0.35:0.12,format=yuva420p'

print('[1] try chromakey + despill')
r = subprocess.run([
    FFMPEG, '-y', '-i', SRC,
    '-vf', filter_complex,
    '-c:v', 'libvpx-vp9', '-pix_fmt', 'yuva420p',
    '-b:v', '2000k', '-auto-alt-ref', '0', '-an',
    DST
], capture_output=True, text=True)
if r.returncode != 0:
    print('    despill unavailable, using colorkey only')
    r = subprocess.run([
        FFMPEG, '-y', '-i', SRC,
        '-vf', simple_filter,
        '-c:v', 'libvpx-vp9', '-pix_fmt', 'yuva420p',
        '-b:v', '2000k', '-auto-alt-ref', '0', '-an',
        DST
    ], capture_output=True, text=True)

if r.returncode != 0:
    print('ERROR:'); print(r.stderr[-2000:]); sys.exit(1)

print(f'[OK] {DST} {os.path.getsize(DST)//1024} KB')
