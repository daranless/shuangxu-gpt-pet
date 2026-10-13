"""Register already extracted generated pixels; no new artwork or cell slicing."""
from pathlib import Path
import json
from PIL import Image

run = Path(__file__).parent / 'shuangxu'
root = run / 'frames'
manifest = json.loads((root / 'frames-manifest.json').read_text(encoding='utf-8'))
target_height = 146
baseline = 203
report = []
for row in manifest['rows']:
    state = row['state']
    files = sorted((root / state).glob('*.png'))
    frames = [Image.open(p).convert('RGBA') for p in files]
    bounds = [im.getchannel('A').point(lambda a: 255 if a > 16 else 0).getbbox() for im in frames]
    shared_top = min(b[1] for b in bounds)
    shared_bottom = max(b[3] for b in bounds)
    factor = 0.85 if state == 'jumping' else target_height / (shared_bottom - shared_top)
    # One transform per complete row; preserve all within-row scale and motion.
    canvas_size = (round(192 * factor), round(208 * factor))
    dy = baseline - round(shared_bottom * factor)
    dx = (192 - canvas_size[0]) // 2
    for path, frame in zip(files, frames):
        scaled = frame.resize(canvas_size, Image.Resampling.LANCZOS)
        dest = Image.new('RGBA', (192, 208))
        dest.alpha_composite(scaled, (dx, dy))
        dest.save(path)
    report.append({'state': state, 'scale': factor, 'source_bounds': [shared_top, shared_bottom], 'translation': [dx,dy]})
(run / 'qa' / 'standard-registration.json').write_text(json.dumps({'target_height': target_height, 'baseline': baseline, 'rows': report}, indent=2), encoding='utf-8')
