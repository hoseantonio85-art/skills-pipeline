#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
try:
    import yaml
except ImportError:
    print('PyYAML is required: pip install pyyaml', file=sys.stderr)
    raise

root = Path(__file__).resolve().parents[1]
manifest_path = root / 'product-system/context-manifest.yaml'
errors=[]
with manifest_path.open(encoding='utf-8') as f:
    manifest=yaml.safe_load(f)

paths=[]
def collect(obj):
    if isinstance(obj, str):
        if obj.startswith(('product-system/','sources/','.gigacode/','setup/')) and '*' not in obj:
            paths.append(obj)
    elif isinstance(obj, list):
        for x in obj: collect(x)
    elif isinstance(obj, dict):
        for x in obj.values(): collect(x)
collect(manifest.get('documents',{}))
collect(manifest.get('loading',{}))
for rel in sorted(set(paths)):
    if not (root/rel).exists(): errors.append(f'missing: {rel}')

for y in root.rglob('*.yaml'):
    try:
        yaml.safe_load(y.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'yaml: {y.relative_to(root)}: {e}')
for j in root.rglob('*.json'):
    try:
        json.loads(j.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'json: {j.relative_to(root)}: {e}')

for p in root.rglob('*'):
    if p.is_file() and p.suffix.lower() in {'.md','.yaml','.yml','.json','.py'}:
        text=p.read_text(encoding='utf-8')
        legacy_token = 'lova' + 'ble'
        if re.search(legacy_token, text, re.I): errors.append(f'forbidden legacy instruction reference: {p.relative_to(root)}')

result={
    'context_id': manifest.get('context_id'),
    'package_version': manifest.get('package_version'),
    'files_checked': sum(1 for p in root.rglob('*') if p.is_file()),
    'manifest_paths_checked': len(set(paths)),
    'errors': errors,
    'status': 'passed' if not errors else 'failed'
}
(root/'CONTEXT_VALIDATION.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if errors else 0)
