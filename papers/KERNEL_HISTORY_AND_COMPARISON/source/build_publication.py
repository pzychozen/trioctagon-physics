"""Existing repository Markdown -> Pandoc AST -> Tectonic workflow, locally scoped.
Requires installed tools and an existing offline TeX cache; installs nothing.
"""
from pathlib import Path
import argparse, datetime, hashlib, json, os, re, shutil, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
STEM = 'KERNEL_HISTORY_AND_COMPARISON_v0.1'
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--workspace', type=Path, required=True, help='Fresh build directory outside the repository')
args = p.parse_args()
WORK = args.workspace.resolve()
REPO = ROOT.parents[1]
if WORK == REPO or REPO in WORK.parents:
    raise SystemExit('Keep disposable build files outside the repository.')
if WORK.exists():
    raise SystemExit('Use a fresh build directory; pre-existing files are never deleted.')
PANDOC = Path(os.environ['PAPER_HISTORY_PANDOC']).resolve()
TECTONIC = Path(os.environ['PAPER_HISTORY_TECTONIC']).resolve()
CACHE = Path(os.environ['PAPER_HISTORY_TEX_CACHE']).resolve()
assert PANDOC.is_file() and TECTONIC.is_file() and CACHE.is_dir()
WORK.mkdir(parents=True)
STAGE = WORK / 'source'
STAGE.mkdir()
for name in [STEM + '.md', 'publication_style.tex']:
    shutil.copyfile(ROOT / 'source' / name, STAGE / name)
shutil.copytree(ROOT / 'figures', WORK / 'figures')

def run(argv):
    return subprocess.run([str(x) for x in argv], cwd=STAGE, check=True, capture_output=True)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def nodes(value, kind):
    if isinstance(value, dict):
        if value.get('t') == kind:
            yield value
        for item in value.values():
            yield from nodes(item, kind)
    elif isinstance(value, list):
        for item in value:
            yield from nodes(item, kind)

fmt = 'markdown+tex_math_dollars+tex_math_single_backslash+pipe_tables+raw_tex-smart'
md = STAGE / (STEM + '.md')
ast = json.loads(run([PANDOC, md, '--from=' + fmt, '--to=json']).stdout)
for node in list(nodes(ast, 'Code')):
    value = node['c'][1]
    if len(value) >= 20:
        # xurl supplies safe line breaks in long identifiers, hashes and paths.
        assert not any(c in value for c in '{}\\')
        node.clear()
        node.update({'t': 'RawInline', 'c': ['latex', r'\nolinkurl{' + value + '}']})
equations = []
for node in list(nodes(ast, 'Math')):
    if node['c'][0]['t'] != 'DisplayMath':
        continue
    raw = node['c'][1]
    tag = re.search(r'\\tag\{([^}]+)\}', raw)
    body = re.sub(r'\\tag\{[^}]+\}', '', raw).strip()
    equations.append({'tag': tag.group(1) if tag else '', 'body': body})
    node.clear()
    node.update({'t': 'RawInline', 'c': ['latex', r'\paperdisplay[' + equations[-1]['tag'] + ']{' + body + '}']})
assert [x['tag'] for x in equations] == [str(i) for i in range(1, 16)]
astpath = WORK / 'manuscript_ast.json'
astpath.write_text(json.dumps(ast, ensure_ascii=False), encoding='utf-8')
tex = STAGE / (STEM + '.tex')
run([PANDOC, astpath, '--from=json', '--to=latex', '--standalone', '--shift-heading-level-by=-1',
     '--include-in-header=' + str(STAGE / 'publication_style.tex'),
     '--variable=documentclass:article', '--variable=fontsize:11pt', '--variable=papersize:a4',
     '--variable=geometry:margin=23mm', '--variable=mainfont:texgyrepagella-regular.otf',
     '--variable=mainfontoptions:BoldFont=texgyrepagella-bold.otf,ItalicFont=texgyrepagella-italic.otf,BoldItalicFont=texgyrepagella-bolditalic.otf',
     '--variable=mathfont:texgyrepagella-math.otf', '--variable=monofont:lmmono10-regular.otf',
     '--variable=colorlinks:true', '--variable=linkcolor:MidnightBlue', '--variable=urlcolor:MidnightBlue',
     '--wrap=preserve', '--output=' + str(tex)])
assert all(x['body'] in tex.read_text(encoding='utf-8') for x in equations)
fc = WORK / 'fontconfig.xml'
fontdir = os.environ.get('PAPER_HISTORY_SYSTEM_FONTS', 'C:/Windows/Fonts')
fc.write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>'
              + fontdir + '</dir><cachedir>' + (WORK / 'fontconfig-cache').as_posix()
              + '</cachedir></fontconfig>', encoding='utf-8')
env = os.environ.copy()
env.update(TECTONIC_CACHE_DIR=str(CACHE), FONTCONFIG_FILE=str(fc),
           SOURCE_DATE_EPOCH=str(int(datetime.datetime(2026, 10, 1, tzinfo=datetime.timezone.utc).timestamp())))
result = subprocess.run([str(TECTONIC), '-X', 'compile', '--only-cached', '--keep-logs',
                         '--keep-intermediates', '--outdir', str(WORK), str(tex)],
                        cwd=STAGE, env=env, capture_output=True)
(WORK / 'build_console.log').write_bytes(result.stdout + result.stderr)
if result.returncode:
    print((result.stdout + result.stderr).decode(errors='replace')[-8000:])
    raise SystemExit(result.returncode)
pdf = ROOT / 'publication' / (STEM + '.pdf')
shutil.copyfile(WORK / (STEM + '.pdf'), pdf)
shutil.copyfile(tex, ROOT / 'source' / (STEM + '.tex'))
log = (WORK / (STEM + '.log')).read_text(encoding='utf-8', errors='replace')
warnings = [line for line in log.splitlines() if any(t in line for t in ('Warning', 'Overfull', 'Missing character'))]
record = {'status': 'BUILT_PENDING_VISUAL_REVIEW', 'isolated_build': True, 'tex_network': False,
          'python': sys.version, 'pandoc': run([PANDOC, '--version']).stdout.decode().splitlines()[0],
          'tectonic': run([TECTONIC, '--version']).stdout.decode().strip(),
          'pandoc_sha256': digest(PANDOC), 'tectonic_sha256': digest(TECTONIC),
          'source_sha256': digest(md), 'style_sha256': digest(STAGE / 'publication_style.tex'),
          'tex_sha256': digest(tex), 'pdf_sha256': digest(pdf),
          'source_date_epoch': env['SOURCE_DATE_EPOCH'], 'equations': equations,
          'figures': {p.name: digest(p) for p in (ROOT / 'figures').glob('*.pdf')},
          'warnings': warnings, 'scratch_workspace': str(WORK), 'exit_code': result.returncode}
(ROOT / 'evidence' / 'build_record_publication.json').write_text(json.dumps(record, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({k: v for k, v in record.items() if k not in ('equations', 'figures')}, indent=2))
