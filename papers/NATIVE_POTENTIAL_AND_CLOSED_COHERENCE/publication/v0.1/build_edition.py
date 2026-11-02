"""Build the publication PDF using an installed, cached Tectonic toolchain."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--tectonic', default=shutil.which('tectonic'))
parser.add_argument('--work-dir', required=True, help='External directory for temporary TeX/font files')
args = parser.parse_args()
if not args.tectonic:
    parser.error('Provide --tectonic with an already installed compiler path')
work = Path(args.work_dir).resolve()
assert work != ROOT and ROOT not in work.parents, 'Build scratch must be outside the edition'
work.mkdir(parents=True, exist_ok=True)
(work / 'fontcache').mkdir(exist_ok=True)
verification = ROOT / 'verification'
verification.mkdir(exist_ok=True)
env = os.environ.copy()
if os.name == 'nt':
    fonts = Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts'
    config = work / 'fonts.conf'
    config.write_text('<?xml version="1.0"?>\n<!DOCTYPE fontconfig SYSTEM "fonts.dtd">\n<fontconfig><dir>' + fonts.as_posix() + '</dir><cachedir>' + (work / 'fontcache').as_posix() + '</cachedir></fontconfig>\n', encoding='utf-8')
    env['FONTCONFIG_FILE'] = str(config)
    env['FONTCONFIG_PATH'] = str(work)
env['SOURCE_DATE_EPOCH'] = '1793577600'
compiler = str(Path(args.tectonic).resolve())
version = subprocess.run([compiler, '--version'], capture_output=True, text=True, check=True).stdout.strip()
command = [compiler, '--only-cached', '--untrusted', '--keep-logs', '--keep-intermediates', '--outdir', str(work), 'manuscript/main.tex']
run = subprocess.run(command, cwd=ROOT, env=env, capture_output=True)
(verification / 'compiler_final.txt').write_bytes(run.stdout + run.stderr)
if run.returncode:
    print((run.stdout + run.stderr).decode('utf-8', errors='replace'))
    raise SystemExit(run.returncode)
pdf = ROOT / 'NATIVE_POTENTIAL_AND_COHERENCE_v0.1.pdf'
shutil.copyfile(work / 'main.pdf', pdf)
shutil.copyfile(work / 'main.log', verification / 'main.log')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
record = {
    'edition': 'Author-authorized repository research edition v0.1',
    'built_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'compiler': compiler, 'compiler_version': version, 'command': command,
    'working_directory': str(ROOT), 'external_build_directory': str(work),
    'return_code': run.returncode, 'python_executable': sys.executable, 'python_version': sys.version,
    'pdf': pdf.name, 'pdf_bytes': pdf.stat().st_size, 'pdf_sha256': sha(pdf),
    'source_sha256': {p.relative_to(ROOT).as_posix(): sha(p) for p in sorted((ROOT / 'manuscript').glob('*.tex'))},
    'process_only_environment': {key: env[key] for key in ('FONTCONFIG_FILE', 'FONTCONFIG_PATH', 'SOURCE_DATE_EPOCH') if key in env},
    'scope': 'Document build only; cached resources, no shell escape, no scientific helpers or repository imports.',
}
(verification / 'BUILD_RECEIPT.json').write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'compiler': version, 'pdf': str(pdf), 'bytes': record['pdf_bytes'], 'sha256': record['pdf_sha256']}, indent=2))
print((run.stdout + run.stderr).decode('utf-8', errors='replace'))
