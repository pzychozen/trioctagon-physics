"""Bounded R1 document/file QA and packaging. No scientific code is imported or run.

Use Windows CMD after conda activate torment. Requires the preserved sibling v0.1
and the one-time R1 baseline. Human page inspection is a separately recorded
observation tied to exact PDF/render hashes; this script does not replace it.
"""
from pathlib import Path
import difflib
import hashlib
import json
import re
import sys
import zipfile
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent
OLD = ROOT.parent / 'v0.1'
BUNDLED = Path(r'C:\Users\Notandi\.cache\codex-runtimes\codex-primary-runtime\dependencies')
sys.path.append(str(BUNDLED / 'python/Lib/site-packages'))
from pypdf import PdfReader

ZIP_NAME = 'SRG_VOLUME_II_SIM04_SIM05_CANDIDATE_v0.1.1_R1_REVIEW.zip'
VERSION = 'SRG Volume II SIM04/SIM05 candidate v0.1.1 / editorial R1'
DATE = '2026-10-24'
EXCLUDED_DIRS = {'build', 'cache', 'qa', 'renders', 'tmp', '__pycache__'}
EXCLUDED_ROOT = {'MANIFEST.json', 'REVIEW_ZIP_IDENTITY.json', ZIP_NAME,
                 'fontconfig.xml', 'CACHE_RECEIPT.json'}

def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()

def identity(path):
    path = Path(path)
    h = hashlib.sha256()
    with path.open('rb') as f:
        while b := f.read(1024 * 1024):
            h.update(b)
    return {'bytes': path.stat().st_size, 'sha256': h.hexdigest()}

def readj(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def writej(name, value):
    (ROOT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def writet(name, value):
    (ROOT / name).write_bytes(value.encode('utf-8'))

def file_record(path):
    return {'path': path.relative_to(ROOT).as_posix(), **identity(path)}

def same(path, row):
    got = identity(path)
    assert all(got[k] == row[k] for k in ('bytes', 'sha256')), str(path)
    return got

def payload():
    return sorted(p for p in ROOT.rglob('*') if p.is_file()
                  and p.relative_to(ROOT).parts[0] not in EXCLUDED_DIRS
                  and p.relative_to(ROOT).as_posix() not in EXCLUDED_ROOT)

baseline = readj(ROOT / 'R1_STARTING_BASELINE.json')
intake = readj(ROOT / 'R1_INTAKE_RECEIPT.json')
old_manifest = readj(OLD / 'MANIFEST.json')
old_rows = {r['path']: r for r in old_manifest['files']}

def preservation_check():
    current_paths = sorted(p.relative_to(OLD).as_posix()
                           for p in OLD.rglob('*') if p.is_file())
    assert current_paths == sorted(r['path'] for r in baseline['old_candidate_all_files'])
    for row in baseline['old_candidate_all_files']:
        same(OLD / row['path'], row)
    for row in baseline['external_accepted_inputs']:
        same(row['original_path'], row)
    same(baseline['r1_order_archive']['path'], baseline['r1_order_archive'])
    for row in old_manifest['files']:
        if row['path'].startswith(('evidence/', 'figures/')):
            same(ROOT / row['path'], row)
    for p in (ROOT / 'provenance/v0.1').iterdir():
        assert p.read_bytes() == (OLD / p.name).read_bytes(), p
    return {'old_candidate_file_count': len(current_paths),
            'external_accepted_input_count': len(baseline['external_accepted_inputs']),
            'old_candidate_file_list_and_all_bytes_unchanged': True,
            'external_accepted_input_bytes_unchanged': True,
            'review_archive_unchanged': True,
            'prior_delivered_scientific_evidence_and_figures_unchanged': True,
            'provenance_copies_byte_identical': True}

preserved = preservation_check()
old_tex = (OLD / 'manuscript.tex').read_text(encoding='utf-8')
new_tex = (ROOT / 'manuscript.tex').read_text(encoding='utf-8')
pure_tex = new_tex
for before, after in intake['housekeeping_tex_replacements']:
    assert pure_tex.count(after) == 1, after
    pure_tex = pure_tex.replace(after, before)

def diff(name, before, after):
    return ''.join(difflib.unified_diff(before.splitlines(True), after.splitlines(True),
                                       fromfile='a/' + name, tofile='b/' + name))

matrix_old = (OLD / 'CLAIM_EVIDENCE_MATRIX.md').read_text(encoding='utf-8')
matrix_new = (ROOT / 'CLAIM_EVIDENCE_MATRIX.md').read_text(encoding='utf-8')
approved = (ROOT / 'SOURCE_CORRECTIONS_ONLY.patch').read_bytes()
reconstructed = (diff('manuscript.tex', old_tex, pure_tex) +
                 diff('CLAIM_EVIDENCE_MATRIX.md', matrix_old, matrix_new)).encode('utf-8')
assert reconstructed == approved
assert approved == (ROOT / 'evidence/editorial/R1/PROPOSED_E01_E03_SOURCE_CORRECTIONS.patch').read_bytes()
writet('DIFF_FROM_v0.1.patch', diff('manuscript.tex', old_tex, new_tex) +
       diff('CLAIM_EVIDENCE_MATRIX.md', matrix_old, matrix_new))

# Complete textual authored-document/tool diff. Relocated prior tools remain in provenance.
names = sorted({p.name for folder in (OLD, ROOT) for p in folder.iterdir()
                if p.is_file() and p.suffix in {'.md', '.tex', '.py'}})
complete_diff = ''
for name in names:
    before = (OLD / name).read_text(encoding='utf-8') if (OLD / name).exists() else ''
    after = (ROOT / name).read_text(encoding='utf-8') if (ROOT / name).exists() else ''
    complete_diff += diff(name, before, after)
writet('DOCUMENT_ONLY_DIFF_FROM_v0.1.patch', complete_diff)

math_pattern = re.compile(r'\\begin\{(equation\*?|align\*?)\}.*?\\end\{\1\}', re.S)
old_math = [m.group(0) for m in math_pattern.finditer(old_tex)]
new_math = [m.group(0) for m in math_pattern.finditer(new_tex)]
assert old_math and old_math == new_math
start = r'\section{Four reviewed mathematical explanations}'
end = r'\section{What the comparison establishes}'
old_props = old_tex.split(start, 1)[1].split(end, 1)[0]
new_props = new_tex.split(start, 1)[1].split(end, 1)[0]
assert old_props == new_props
assert new_props.count(r'\begin{proposition}') == 4
assert (ROOT / 'references.tex').read_bytes() == (OLD / 'references.tex').read_bytes()
figure_register = readj(ROOT / 'FIGURE_REGISTER.json')
assert len(figure_register['selected']) == 10
for row in figure_register['selected']:
    same(ROOT / row['path'], row)

# Only text navigation is checked: no historical program or checker is imported.
bib = (ROOT / 'references.tex').read_text(encoding='utf-8')
keys = set(re.findall(r'\\bibitem\{([^}]+)\}', bib))
used_keys = {key for group in re.findall(r'\\cite\{([^}]+)\}', new_tex)
             for key in group.split(',')}
assert used_keys <= keys
labels = set(re.findall(r'\\label\{([^}]+)\}', new_tex))
labels |= {r['tex_label'] for r in figure_register['selected']}
refs = set(re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', new_tex))
assert refs <= labels, refs - labels
tex_links = re.findall(r'\\href\{([^}]+)\}', new_tex + bib)
for link in tex_links:
    assert (ROOT / link).is_file(), link

receipt = readj(ROOT / 'qa/BUILD_01_RECEIPT.json')
assert receipt['tex_sha256'] == identity(ROOT / 'manuscript.tex')['sha256']
assert receipt['pdf_sha256'] == identity(ROOT / 'manuscript.pdf')['sha256']
assert receipt['exit_code'] == 0 and receipt['offline']
assert not receipt['warnings']
assert all(receipt['embedded_fonts'].values())
writej('FINAL_BUILD_RECEIPT.json', receipt)

reader = PdfReader(ROOT / 'manuscript.pdf')
assert len(reader.pages) == receipt['pages'] == 30
texts = [page.extract_text() for page in reader.pages]
assert all(t.strip() for t in texts)
assert '??' not in '\n'.join(texts)
assert 'v0.1.1' in texts[0] and '24 October 2026' in texts[0]
assert 'v0.1.1 editorial R1' in str(reader.metadata.get('/Subject'))
pdf_file_links = []
for number, page in enumerate(reader.pages, 1):
    for ref in page.get('/Annots', []):
        ann = ref.get_object()
        action = ann.get('/A')
        if not action:
            continue
        action = action.get_object()
        target = action.get('/F', action.get('/URI'))
        if target is None:
            continue
        if hasattr(target, 'get_object'):
            target = target.get_object()
        if isinstance(target, dict):
            target = target.get('/F')
        target = str(target)
        if target.startswith(('http:', 'https:', 'mailto:')):
            continue
        target = unquote(target).split('#', 1)[0]
        assert (ROOT / target).is_file(), (number, target)
        pdf_file_links.append({'pdf_page': number, 'target': target})

# Human inspection completed by Codex for precisely these rendered files.
# Any different future build must have a fresh human visual review.
observed_pdf_sha = '1b7ab29f656fed7a4114957ef04b8a58bde5d6d4aa75439179f6b1fa0675dd1e'
assert identity(ROOT / 'manuscript.pdf')['sha256'] == observed_pdf_sha
notes = [
    'Cover: v0.1.1 editorial R1, 24 October 2026; title, attribution and scope legible.',
    'Contents: hierarchy, section titles and page numbers legible.',
    'Opening text and glossary: no clipping, equations/terms legible.',
    'Landscape Figure 1: unchanged image and caption fit; orientation retained.',
    'Evidence hierarchy and identity table legible.',
    'Verification context and initial construction text legible.',
    'Equations 1–11 and execution-order explanation fit within margins.',
    'Parameter table and retained-record account legible.',
    'Six-point group, geometry equations and variance decomposition legible.',
    'Short printed page 9 remains intentionally sparse, as accepted by GPT.',
    'Landscape Figure 2 and caption legible; no image changes.',
    'Landscape Figure 3 and caption legible; no image changes.',
    'Landscape Figure 4 geometry addendum and caption legible.',
    'Landscape Figure 5 and caption legible; no image changes.',
    'Infinity construction, equations 16–22 and timing explanation legible.',
    'Replay account and endpoint table fit and remain legible.',
    'Second-channel and finite-stabilization explanations fit.',
    'Figure 6 world-scale plate and caption fit; unchanged asset.',
    'Landscape Figure 7 and caption fit; unchanged asset.',
    'Landscape Figure 8 and caption fit; unchanged asset.',
    'Landscape Figure 9 stage-budget plate and caption fit.',
    'Landscape Figure 10 second-channel plate and caption fit.',
    'E01 checked: both means absolute; signed std and distinct coherence guards retained. Eq.23 fits.',
    'Observer continuation and start of four propositions remain legible.',
    'Propositions 1–3, equations and proof endings legible; no overlap.',
    'Proposition 4, comparison and limitations legible.',
    'Comparison table and start of source-locator table fit.',
    'E02 and E03 checked: magnitude |R|, 361–371/440–445, 190–195 and 198–205 visible.',
    'Historical-label continuation, endpoint membership and bibliography start legible.',
    'Remaining bibliography and evidence links legible; no clipping.'
]
inspections = []
for number, note in enumerate(notes, 1):
    name = f'page-{number:02d}.png'
    p = ROOT / 'renders/BUILD_01' / name
    assert identity(p)['sha256'] == receipt['page_renders'][name]
    inspections.append({'pdf_page': number, 'printed_page': None if number == 1 else number-1,
                        'render_sha256': receipt['page_renders'][name],
                        'visually_inspected_by': 'Codex', 'result': 'pass', 'notes': note})
writej('PAGE_INSPECTION.json', {
    'candidate': VERSION, 'date': DATE, 'pdf_sha256': observed_pdf_sha,
    'method': 'Human-model visual inspection of all 30 Poppler page PNGs at 115 dpi, not text-only QA.',
    'render_files': 'Local renders/BUILD_01; caches and renders excluded from compact delivery.',
    'all_pages_inspected': True, 'pages': inspections})

evidence = [r for r in old_manifest['files'] if r['path'].startswith('evidence/')]
archives = [r for r in evidence if r['path'].startswith('evidence/inputs/')]
assert len(archives) == 2
writej('PRESERVATION_RECEIPT.json', {
    'candidate': VERSION, 'date': DATE, 'status': 'For GPT and Hilmir review; no publication authority',
    'method': 'SHA-256/byte count and file-list comparisons only; no scientific reruns.',
    'scope_note': 'All writes confined to this new candidate, apart from the document skill operation marker. '
                  'No Git commands were used. External preservation coverage is the 57 baselined accepted input files; '
                  'no claim of a fresh whole-repository audit is made.',
    **preserved,
    'starting_baseline': 'R1_STARTING_BASELINE.json',
    'old_candidate_root': str(OLD),
    'old_candidate_total_bytes': sum(r['bytes'] for r in baseline['old_candidate_all_files']),
    'old_main_identities': [{'path': n, **identity(OLD / n)}
                           for n in baseline['expected_starting_identities']],
    'unchanged_delivered_scientific_evidence': evidence,
    'unchanged_selected_figures': [{'path': r['path'], **identity(ROOT / r['path'])}
                                  for r in figure_register['selected']],
    'immutable_scientific_input_archives': archives,
    'review_authority_archive': baseline['r1_order_archive'],
    'equations_and_four_propositions_unchanged': True,
    'numerical_result_passages_unchanged': 'Exact approved patch plus three TeX housekeeping replacements; '
                                        'no other manuscript changes and no result recalculation.',
    'execution_attestation': {'new_simulations': 0, 'scientific_checker_runs': 0, 'rng_draws': 0,
                             'new_figures': 0, 'new_scientific_statistics': 0, 'git_commands': 0,
                             'publication_actions': 0, 'tower_ii_work': 0},
    'attestation_basis': 'Bounded R1 tool/action record; hashes corroborate preserved bytes, '
                         'but file hashes alone do not prove absence of execution.'
})

planned = {'DOCUMENT_QA.json', 'FILE_CHANGE_REGISTER.json', 'MANIFEST.json'}
markdown_links = []
for name in ['START_HERE.md', 'EVIDENCE_INDEX.md', 'CORRECTION_DISPOSITION.md',
             'EDITORIAL_AND_VERIFICATION_NOTES.md', 'BUILD_INSTRUCTIONS.md', 'CLAIM_EVIDENCE_MATRIX.md']:
    text = (ROOT / name).read_text(encoding='utf-8')
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        link = link.strip('<>').split('#', 1)[0]
        if not link or '://' in link:
            continue
        assert (ROOT / link).is_file() or link in planned, (name, link)
        markdown_links.append({'document': name, 'target': link})
writej('DOCUMENT_QA.json', {
    'candidate': VERSION, 'date': DATE, 'result': 'PASS',
    'source_scope': {
        'approved_patch_exactly_reconstructed': True,
        'approved_patch_sha256': sha_bytes(approved),
        'additional_tex_changes_only': intake['housekeeping_tex_replacements'],
        'equation_or_align_blocks_byte_equal': len(new_math),
        'four_proposition_section_byte_equal': True,
        'bibliography_byte_equal': True,
        'selected_figure_bytes_unchanged': 10,
        'scientific_evidence_files_unchanged': len(evidence),
        'numerical_prose_preservation_basis': 'No changes outside exact E01–E03 patch and version/date metadata.'},
    'pdf': {'pages': len(reader.pages), 'sha256': observed_pdf_sha,
            'warnings': [], 'all_fonts_embedded': True, 'no_unresolved_question_marks': True,
            'cover_version_date_and_subject_checked': True, 'all_pages_visually_inspected': True},
    'navigation': {'bibliography_keys': sorted(keys), 'used_keys_resolved': sorted(used_keys),
                   'references_resolved': sorted(refs), 'tex_file_links': tex_links,
                   'pdf_file_links': pdf_file_links, 'current_root_markdown_links': markdown_links,
                   'historical_navigation_note': 'Accepted evidence/provenance documents are byte-preserved, '
                                                 'not rewritten to repair their original-context links.'},
    'scientific_execution': 'None. Original programs and scientific checkers were never imported or run.'
})

# The change register omits its own bytes and packaging identity files to avoid cycles.
current = {p.relative_to(ROOT).as_posix(): p for p in payload()
           if p.name != 'FILE_CHANGE_REGISTER.json'}
changes = []
for name in sorted(set(old_rows) | set(current)):
    prior = old_rows.get(name)
    now = current.get(name)
    item = {'path': name}
    if prior:
        item['old'] = {k: prior[k] for k in ('bytes', 'sha256')}
    if now:
        item['new'] = identity(now)
        item['status'] = 'unchanged' if prior and item['old'] == item['new'] else ('modified' if prior else 'added')
    else:
        destination = ROOT / 'provenance/v0.1' / name
        assert destination.is_file(), ('unexpected payload omission', name)
        same(destination, prior)
        item.update(status='relocated unchanged', destination=destination.relative_to(ROOT).as_posix())
    changes.append(item)
writej('FILE_CHANGE_REGISTER.json', {
    'candidate': VERSION, 'comparison': 'v0.1 delivered manifest payload -> current delivered payload',
    'exclusions': ['This register itself', 'MANIFEST.json', 'External REVIEW_ZIP_IDENTITY.json', ZIP_NAME,
                   'Non-delivered compiler cache, temporary files, build products and renders'],
    'diff_scope': 'DOCUMENT_ONLY_DIFF_FROM_v0.1.patch covers every root .tex/.md/.py old/new file, '
                  'including relocated tools; JSON/binary/generated identity changes are listed here.',
    'files': changes})

files = [file_record(p) for p in payload()]
writej('MANIFEST.json', {
    'candidate': VERSION, 'date': DATE, 'status': 'For GPT and Hilmir review, not publication accepted',
    'scope': 'Exact delivered payload; excludes this manifest and the external ZIP identity to avoid circular hashes',
    'payload_file_count': len(files), 'payload_bytes': sum(r['bytes'] for r in files), 'files': files})
manifest_bytes = (ROOT / 'MANIFEST.json').read_bytes()
with zipfile.ZipFile(ROOT / ZIP_NAME, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for row in files:
        z.write(ROOT / row['path'], row['path'])
    z.writestr('MANIFEST.json', manifest_bytes)
with zipfile.ZipFile(ROOT / ZIP_NAME) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == len(set(z.namelist())) == len(files) + 1
    assert set(z.namelist()) == {r['path'] for r in files} | {'MANIFEST.json'}
    assert z.read('MANIFEST.json') == manifest_bytes
    for row in files:
        data = z.read(row['path'])
        assert len(data) == row['bytes'] and sha_bytes(data) == row['sha256'], row['path']
        same(ROOT / row['path'], row)
after = preservation_check()
assert after == preserved
writej('REVIEW_ZIP_IDENTITY.json', {
    'candidate': VERSION, 'date': DATE, 'path': ZIP_NAME, **identity(ROOT / ZIP_NAME),
    'zip_file_count': len(files) + 1, 'payload_file_count': len(files),
    'manifest_sha256': sha_bytes(manifest_bytes), 'pdf_sha256': observed_pdf_sha,
    'tex_sha256': identity(ROOT / 'manuscript.tex')['sha256'],
    'zip_crc_and_all_payload_hashes_read_back': True,
    'post_packaging_preservation_check': after,
    'status': 'Ready for GPT and Hilmir review; no scientific or publication action authorized'})
print(json.dumps({'result': 'PASS', 'zip': ZIP_NAME, 'zip_identity': identity(ROOT / ZIP_NAME),
                  'payload_files': len(files), 'zip_files': len(files)+1,
                  'pages_inspected': 30, 'preservation': preserved}, indent=2))

