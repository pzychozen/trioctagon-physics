"""Read-only comparison with the private pre-edit inventory; writes candidate records only."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import subprocess

OUT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--project-root', type=Path, required=True)
args = parser.parse_args()
ROOT = args.project_root.resolve()
baseline_path = OUT / 'qa/private/baseline.json'
baseline = json.loads(baseline_path.read_text(encoding='utf-8'))


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT / 'trioctagon-physics'),
                                    *args], encoding='utf-8').strip()


collections = {}
for name, row in baseline['inventory'].items():
    folder = ROOT / name
    seen = set()
    for current, dirs, files in os.walk(folder):
        dirs[:] = [d for d in dirs if d != '.git' and
                   (Path(current) / d).resolve() != OUT.resolve()]
        seen.update((Path(current) / f).relative_to(folder).as_posix() for f in files)
    expected = set(row['entries'])
    changed = [rel for rel in sorted(expected & seen)
               if (folder / rel).stat().st_size != row['entries'][rel]['bytes'] or
               sha(folder / rel) != row['entries'][rel]['sha256']]
    collections[name] = {
        'baseline_files': len(expected), 'current_files': len(seen),
        'baseline_files_unchanged': len(expected & seen) - len(changed),
        'changed': changed, 'removed': sorted(expected - seen),
        'added_outside_candidate': sorted(seen - expected)}

now_git = {'head': git('rev-parse', 'HEAD'),
           'branch': git('branch', '--show-current'),
           'staged': git('diff', '--cached', '--name-only'),
           'status': git('status', '--porcelain=v1', '--untracked-files=all')}
git_matches = {k: str(baseline['git'][k]).strip() == str(v).strip()
               for k, v in now_git.items()}
preserved = all(not row['changed'] and not row['removed']
                for row in collections.values()) and all(git_matches.values())
added = sum(len(row['added_outside_candidate']) for row in collections.values())
status = ('PASS_BASELINE_WITH_UNRELATED_ADDITIONS' if added else 'PASS') if preserved else 'FAIL'
private = {'status': status, 'collections': collections,
           'git_matches_baseline': git_matches, 'git': now_git}
(OUT / 'qa/private/final_preservation.json').write_text(
    json.dumps(private, indent=2) + '\n', encoding='utf-8')
public = {
    'status': status, 'baseline_files_checked': sum(r['baseline_files'] for r in collections.values()),
    'baseline_files_unchanged': sum(r['baseline_files_unchanged'] for r in collections.values()),
    'changed_baseline_files': sum(len(r['changed']) for r in collections.values()),
    'removed_baseline_files': sum(len(r['removed']) for r in collections.values()),
    'unrelated_files_added_since_baseline': added,
    'added_file_collection_counts': {n: len(r['added_outside_candidate']) for n, r in collections.items()
                                     if r['added_outside_candidate']},
    'addition_note': 'Unrelated additions are recorded, left untouched, and excluded from this candidate. No attribution is inferred.',
    'git_matches_baseline': git_matches, 'head': now_git['head'],
    'branch': now_git['branch'], 'index_empty': now_git['staged'] == '',
    'scope': 'All inventoried pre-existing bytes, including tmp, research predecessors and published v0.1; candidate workspace and .git excluded.',
    'collections': {n: {'baseline_files': r['baseline_files'],
                        'baseline_files_unchanged': r['baseline_files_unchanged']}
                    for n, r in collections.items()}}
(OUT / 'results/preservation.json').write_text(json.dumps(public, indent=2) + '\n', encoding='utf-8')
print(json.dumps(public, indent=2))
raise SystemExit(0 if preserved else 1)
