"""Render required proof from exact final atlas bytes; no new artwork."""
from PIL import Image, ImageDraw
from pathlib import Path
import importlib.util
import subprocess
import shutil
import json

run = Path(__file__).parent / 'shuangxu'
out = Path(__file__).parent.parent / 'outputs'
atlas = Image.open(run / 'final' / 'spritesheet-extended.png').convert('RGBA')
script = run.parent.parent / 'tools/work-pets/skills/create-pet/scripts/render_animation_previews.py'
spec = importlib.util.spec_from_file_location('pet_preview', script)
preview = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preview)
frames_root = run / 'final' / 'frames'
all_frames, all_durations = [], []
for row, (state, durations) in enumerate(preview.ROW_DURATIONS.items()):
    folder = frames_root / state
    folder.mkdir(parents=True, exist_ok=True)
    frames = []
    for col in range(len(durations)):
        frame = atlas.crop((col*192,row*208,(col+1)*192,(row+1)*208))
        frame.save(folder / f'{col:02}.png')
        frames.append(frame)
        shown = Image.new('RGBA',(384,256),(245,242,250,255))
        shown.alpha_composite(frame,(96,36))
        ImageDraw.Draw(shown).text((12,10),state,fill=(60,40,80))
        all_frames.append(shown.convert('RGB'))
        all_durations.append(durations[col])
    preview.save_preview(frames,durations,out / f'shuangxu-{state}.gif')
preview.save_preview(all_frames,all_durations,out / 'shuangxu-all-states.gif')
transition = [atlas.crop((c*192,0,(c+1)*192,208)) for c in range(6)]
transition += [atlas.crop((c*192,832,(c+1)*192,1040)) for c in range(5)]
transition += [atlas.crop((c*192,0,(c+1)*192,208)) for c in range(6)]
preview.save_preview(transition,[*preview.ROW_DURATIONS['idle'],*preview.ROW_DURATIONS['jumping'],*preview.ROW_DURATIONS['idle']],out / 'shuangxu-idle-jump-idle.gif')
look = [atlas.crop((c*192,r*208,(c+1)*192,(r+1)*208)) for r in (9,10) for c in range(8)]
preview.save_preview(look,[250]*16,out / 'shuangxu-look-loop.gif')
still = Image.new('RGB',(4*224,256),(245,242,250))
for i,(row,col,label) in enumerate([(0,0,'idle'),(3,1,'wave'),(4,2,'jump peak'),(7,2,'working')]):
    fr=atlas.crop((col*192,row*208,(col+1)*192,(row+1)*208))
    still.paste(fr,(i*224+16,32),fr)
    ImageDraw.Draw(still).text((i*224+16,10),label,fill=(60,40,80))
still.save(out / 'shuangxu-motion-stills.png')
subprocess.run([shutil.which('ffmpeg') or 'ffmpeg','-y','-i',str(out/'shuangxu-all-states.gif'),'-c:v','libx264','-pix_fmt','yuv420p','-movflags','+faststart',str(out/'shuangxu-all-states.mp4')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
(run/'qa'/'preview-manifest.json').write_text(json.dumps({'atlas':str(run/'final'/'spritesheet-extended.png'),'source':'Exact final encoded atlas','outputs':[p.name for p in out.glob('shuangxu-*')]},indent=2),encoding='utf-8')
