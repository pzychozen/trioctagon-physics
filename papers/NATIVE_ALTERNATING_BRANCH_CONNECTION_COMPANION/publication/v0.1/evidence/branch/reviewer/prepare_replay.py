"""Optional reconstruction of the disclosed reviewer environment adaptation.
Run only in a fresh writable copy. This prepares, but does not run, any replay.
"""
from pathlib import Path
import shutil,difflib,sys
r=Path(__file__).resolve().parent.parent
src=r/'submitted';dst=r/'replay_work'
if dst.exists():raise SystemExit('Refusing to overwrite replay_work; use a fresh copy.')
if not sys.platform.startswith('linux'):raise SystemExit('This adapter documents the Linux reviewer replay only.')
shutil.copytree(src,dst)
p=dst/'scripts/common.py';before=p.read_text()
old="assert os.environ.get('CONDA_DEFAULT_ENV')=='torment'"
new="assert sys.platform.startswith('linux'), 'Reviewer replay environment must be disclosed'"
assert before.count(old)==1
p.write_text(before.replace(old,new))
actual=''.join(difflib.unified_diff(before.splitlines(keepends=True),p.read_text().splitlines(keepends=True),fromfile='submitted/scripts/common.py',tofile='reviewer_replay/scripts/common.py'))
assert actual==(r/'reviewer/environment_only_adaptation.diff').read_text()
print('Prepared separate reviewer replay copy; original submitted files unchanged.')
