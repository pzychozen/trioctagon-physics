"""Document-only offline compilation, PDF text QA and page rendering.

Never imports evidence code, a simulator, NumPy, or a scientific checker.
Run using Windows CMD after `conda activate torment`.
"""
from pathlib import Path
import hashlib, json, os, re, shutil, subprocess, sys, time

ROOT = Path(__file__).resolve().parent
RESEARCH = ROOT.parents[3]
BUNDLED = Path(r'C:\Users\Notandi\.cache\codex-runtimes\codex-primary-runtime\dependencies')
sys.path.append(str(BUNDLED / 'python/Lib/site-packages'))
from pypdf import PdfReader

def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def lp(p):
    s = str(Path(p).resolve())
    return Path(s if s.startswith('\\\\?\\') else '\\\\?\\' + s)

compiler = Path(os.environ.get('SRG_TECTONIC', r'C:\Program Files\WindowsApps\OpenAI.Codex_26.1007.9446.0_x64__2p2nqsd0c76g0\app\resources\tectonic\tectonic.exe'))
assert compiler.is_file(), 'Set SRG_TECTONIC to the existing Tectonic executable.'
cache = ROOT / 'cache'
if not (cache / 'tectonic').exists():
    source = ROOT.parent / 'v0.1/cache/tectonic'
    shutil.copytree(lp(source), lp(cache / 'tectonic'))
    (ROOT / 'CACHE_RECEIPT.json').write_text(json.dumps({'source': str(source), 'purpose': 'Compiler cache only; no scientific content imported', 'downloads': 0, 'distributed': False}, indent=2))
for q in ('cache/fontconfig', 'tmp', 'qa', 'renders', 'build'):
    (ROOT / q).mkdir(parents=True, exist_ok=True)
fc = ROOT / 'fontconfig.xml'
fc.write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>C:/Windows/Fonts</dir><cachedir>' + (cache / 'fontconfig').as_posix() + '</cachedir></fontconfig>')
env = os.environ.copy()
env.update(TECTONIC_CACHE_DIR=str(lp(cache / 'tectonic')), XDG_CACHE_HOME=str(cache), FONTCONFIG_FILE=str(fc), TEMP=str(ROOT / 'tmp'), TMP=str(ROOT / 'tmp'), PYTHONDONTWRITEBYTECODE='1')
attempt = len(list((ROOT / 'qa').glob('BUILD_*_RECEIPT.json'))) + 1
tag = f'BUILD_{attempt:02d}'
outdir = ROOT / 'build' / tag
outdir.mkdir(exist_ok=True)
fetch = '--fetch-tex-dependencies' in sys.argv
args = [str(compiler), '-X', 'compile'] + ([] if fetch else ['--only-cached']) + ['--untrusted', '--keep-intermediates', '--keep-logs', '--reruns', '2', '--outdir', str(outdir), str(ROOT / 'manuscript.tex')]
started = time.time()
r = subprocess.run(args, cwd=ROOT, env=env, capture_output=True, timeout=480)
(ROOT / 'qa' / (tag + '_OUTPUT.txt')).write_bytes(r.stdout + r.stderr)
receipt = {'command': args, 'exit_code': r.returncode, 'elapsed_seconds': time.time()-started, 'compiler_sha256': digest(compiler), 'tex_sha256': digest(ROOT / 'manuscript.tex'), 'offline': not fetch, 'new_simulations': 0, 'scientific_checker_runs': 0}
if r.returncode:
    (ROOT / 'qa' / (tag + '_RECEIPT.json')).write_text(json.dumps(receipt, indent=2))
    raise SystemExit((r.stdout+r.stderr).decode('utf-8', errors='replace'))
pdf = outdir / 'manuscript.pdf'
reader = PdfReader(pdf)
texts = [page.extract_text(extraction_mode='layout') for page in reader.pages]
(ROOT / 'qa' / (tag + '_TEXT.txt')).write_text('\n\f\n'.join(texts), encoding='utf-8')
log = (outdir / 'manuscript.log').read_text(encoding='utf-8', errors='replace')
receipt.update(pages=len(texts), pdf_sha256=digest(pdf), warnings=[s for s in log.splitlines() if re.search(r'Overfull|undefined|Missing character|multiply defined|LaTeX Warning', s)])
fonts = {}
for page in reader.pages:
    for ref in page['/Resources'].get('/Font', {}).values():
        f = ref.get_object()
        for item in f.get('/DescendantFonts', [f]):
            item = item.get_object()
            descriptor = item['/FontDescriptor'].get_object() if '/FontDescriptor' in item else {}
            fonts[str(item.get('/BaseFont'))] = any(k in descriptor for k in ('/FontFile', '/FontFile2', '/FontFile3'))
receipt['embedded_fonts'] = fonts
assert fonts and all(fonts.values()), fonts
renders = ROOT / 'renders' / tag
renders.mkdir(exist_ok=True)
args_render = [str(BUNDLED / 'native/poppler/Library/bin/pdftoppm.exe'), '-r', '115', '-png', str(pdf), str(renders / 'page')]
r = subprocess.run(args_render, env=env, capture_output=True, timeout=180)
assert r.returncode == 0, r.stderr
pages = sorted(renders.glob('page-*.png'))
assert len(pages) == len(texts)
receipt.update(render_command=args_render, page_renders={p.name:digest(p) for p in pages})
shutil.copyfile(pdf, ROOT / 'manuscript.pdf')
(ROOT / 'qa' / (tag + '_RECEIPT.json')).write_text(json.dumps(receipt, indent=2), encoding='utf-8')
print(json.dumps({'tag': tag, 'pages': len(texts), 'warnings': receipt['warnings'], 'renders': str(renders)}))
