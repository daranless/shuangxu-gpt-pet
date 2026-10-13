"""Correct source-row scale uniformly before bundled shared-transform assembly."""
from pathlib import Path
from PIL import Image
import json
run=Path(__file__).parent/'shuangxu'
atlas=Image.open(run/'final'/'spritesheet-extended.png').convert('RGBA')
def height(row,col):
    bbox=atlas.crop((col*192,row*208,(col+1)*192,(row+1)*208)).getchannel('A').point(lambda a:255 if a>16 else 0).getbbox()
    return bbox[3]-bbox[1]
ratio=height(9,0)/height(10,7)
source=Image.open(run/'decoded'/'look-row-10.png').convert('RGBA')
output=run/'decoded'/'look-row-10-normalized-source.png'
source.resize((round(source.width*ratio),round(source.height*ratio)),Image.Resampling.LANCZOS).save(output)
(run/'qa'/'look-source-normalization.json').write_text(json.dumps({'ratio':ratio,'source_size':source.size,'output_size':Image.open(output).size,'reason':'Uniform complete-strip resize corrects generated source scale; all eight poses retain one transform and source relative registration'},indent=2),encoding='utf-8')
