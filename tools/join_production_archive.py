"""Reassemble the archived production ZIP using only Python's standard library."""
from pathlib import Path
import hashlib, json, os

root=Path(__file__).resolve().parent.parent
parts=root/'outputs/shuangxu-production-files.zip.parts'
manifest=json.loads((parts/'manifest.json').read_text(encoding='utf-8'))
output=root/'outputs/shuangxu-production-files.zip'
if output.exists():
    actual=hashlib.sha256(output.read_bytes()).hexdigest()
    if actual==manifest['sha256']:
        print('Existing ZIP is already complete and verified.')
        raise SystemExit(0)
    raise SystemExit('Existing ZIP differs. Move it aside before running this script.')
temporary=output.with_suffix('.zip.partial')
digest=hashlib.sha256()
with temporary.open('wb') as destination:
    for part in manifest['parts']:
        name=part['file']
        if Path(name).name!=name:raise SystemExit('Invalid part filename')
        data=(parts/name).read_bytes()
        if len(data)!=part['bytes'] or hashlib.sha256(data).hexdigest()!=part['sha256']:
            raise SystemExit('Part validation failed: '+name)
        destination.write(data);digest.update(data)
if temporary.stat().st_size!=manifest['bytes'] or digest.hexdigest()!=manifest['sha256']:
    raise SystemExit('Complete archive checksum failed; .partial file retained for diagnosis.')
os.replace(temporary,output)
print('Production archive reassembled and SHA-256 verified:',output.name)
