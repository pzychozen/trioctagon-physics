"""Write and verify an exact candidate payload manifest; never modify repository files."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_FILES = {'manifest.json', 'manifest.sha256', 'results/build/manuscript.pdf'}
EXCLUDED_PARTS = {'qa', '.git', '__pycache__'}


def record(path):
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


checks = json.loads((ROOT / 'results/candidate_checks.json').read_text())
preservation = json.loads((ROOT / 'results/preservation.json').read_text())
visual = json.loads((ROOT / 'results/visual_review.json').read_text())
assert checks['status'] == 'PASS'
assert preservation['changed_baseline_files'] == preservation['removed_baseline_files'] == 0
assert all(preservation['git_matches_baseline'].values())
assert visual['status'] == 'PASS' and visual['pdf_sha256'] == checks['pdf']['sha256']
files = {}
for path in sorted(ROOT.rglob('*')):
    rel = path.relative_to(ROOT)
    if path.is_file() and not (set(rel.parts) & EXCLUDED_PARTS) and rel.as_posix() not in EXCLUDED_FILES:
        files[rel.as_posix()] = record(path)
manifest = {
    'schema': 'measurement-revision-candidate-byte-manifest-1',
    'status': 'EXTERNAL CANDIDATE; awaiting approval; not committed or published',
    'title': 'Measurement Geometry, Perspective, and Vesica Interfaces in the Tri-Octagon Model',
    'revision': 'v0.1.1', 'candidate_build_date': '2026-10-06',
    'delivery_verification_date': '2026-10-07',
    'published_baseline_commit': '0332fdd6aa3dd10d78dee77f70f910295e6d32a9',
    'scientific_baseline_commit': '82cab10cbe550f58c43163fb8b05fabdad1b05ae',
    'proposed_repository_destination': 'papers/MEASUREMENT_AND_CHIRAL_DRIFT/v0.1.1/',
    'published_v0.1_pdf_sha256': '117474240877e9eaa61faa041d6e362fbdb5ec9b6971569563d2d746674f0fed',
    'pdf': checks['pdf'],
    'bounded_checks': {'passed': checks['checks_passed'], 'total': checks['checks_total'],
                       'record': 'results/candidate_checks.json'},
    'figure_verification': 'results/figure_verification.json',
    'lineage_verification': 'results/lineage_verification.json',
    'source_lineage': 'provenance/lineage_sources.json',
    'preservation': 'results/preservation.json', 'visual_review': 'results/visual_review.json',
    'payload_file_count': len(files), 'payload_bytes': sum(r['bytes'] for r in files.values()),
    'exclusions': {'directories': sorted(EXCLUDED_PARTS), 'files': sorted(EXCLUDED_FILES)},
    'manifest_self_hash': 'omitted to avoid circularity; see detached manifest.sha256',
    'files': files}
dest = ROOT / 'manifest.json'
dest.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
identity = record(dest)
(ROOT / 'manifest.sha256').write_text(identity['sha256'] + '  manifest.json\n', encoding='ascii')
written = json.loads(dest.read_text(encoding='utf-8'))
assert all(record(ROOT / rel) == expected for rel, expected in written['files'].items())
print(json.dumps({'status': 'PASS', 'payload_file_count': len(files),
                  'manifest': identity, 'pdf': checks['pdf']}, indent=2))
