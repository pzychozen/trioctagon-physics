"""Document and retained-byte audit; no scientific evidence is executed."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

try:
    from pypdf import PdfReader, __version__ as pypdf_version
except ImportError:
    sys.path.append('C:/Users/Notandi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/Lib/site-packages')
    from pypdf import PdfReader, __version__ as pypdf_version

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--review-baseline', required=True)
args = parser.parse_args()
baseline = Path(args.review_baseline).resolve()
sha = lambda data: hashlib.sha256(data).hexdigest()
build = json.loads((ROOT / 'verification/BUILD_RECEIPT.json').read_text())
pdf = ROOT / build['pdf']
reader = PdfReader(pdf)
texts = [p.extract_text() or '' for p in reader.pages]
tex = '\n'.join(p.read_text(encoding='utf-8') for p in sorted((ROOT / 'manuscript').glob('*.tex')))
labels = re.findall(r'\\label\{([^}]+)\}', tex)
refs = re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', tex)
bibs = re.findall(r'\\bibitem\{([^}]+)\}', tex)
cites = [key for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', tex) for key in group.split(',')]
warnings = [line for line in (ROOT / 'verification/main.log').read_text(encoding='utf-8', errors='replace').splitlines() if re.search(r'undefined|multiply defined|Overfull|Underfull|Missing character|LaTeX Warning|Package .* Warning', line)]
fonts = {}
for page in reader.pages:
    for ref in page['/Resources'].get('/Font', {}).values():
        font = ref.get_object()
        owner = font['/DescendantFonts'][0].get_object() if '/DescendantFonts' in font else font
        desc = owner.get('/FontDescriptor')
        desc = desc.get_object() if desc else {}
        fonts[str(font.get('/BaseFont'))] = any(k in desc for k in ('/FontFile', '/FontFile2', '/FontFile3'))
manifest = json.loads((ROOT / 'provenance/SOURCE_MANIFEST.json').read_text())
archival = []
for item in manifest:
    if 'packaged_path' in item:
        path = item['packaged_path']
        archival.append({'path': path, 'matches_recorded_identity': sha((ROOT / path).read_bytes()) == item['sha256'], 'matches_review_baseline': (ROOT / path).read_bytes() == (baseline / path).read_bytes()})
for path in ('provenance/SOURCE_MANIFEST.json', 'provenance/correction_receipt.json', 'provenance/originals/NATIVE_CLOSED_INFORMATION_01_PROOF_REVIEW.md'):
    archival.append({'path': path, 'matches_review_baseline': (ROOT / path).read_bytes() == (baseline / path).read_bytes()})
corr = json.loads((ROOT / 'provenance/correction_receipt.json').read_text())
before = (ROOT / corr['backup']).read_bytes()
after = (ROOT / 'evidence/NATIVE_CLOSED_INFORMATION_01/NATIVE_CLOSED_INFORMATION_01_PROOF_REVIEW.md').read_bytes()
offset = corr['comma_offset_zero_based']
local_links = [x for x in re.findall(r'\\href\{([^}]+)\}', tex) if not x.startswith(('https://', 'http://'))]
ledger = (ROOT / 'CLAIM_SOURCE_LEDGER.md').read_text(encoding='utf-8')
ledger_refs = [label for line in ledger.splitlines() if line.startswith('| ') for label in re.findall(r'`((?:eq|thm|prop|cor|lem|tab|sec|app):[^`]+)`', line.split('|')[1])]
unchanged = {p.name: p.read_bytes() == (baseline / 'manuscript' / p.name).read_bytes() for p in (ROOT / 'manuscript').glob('*.tex') if p.name not in ('main.tex', 'discussion.tex')}
checks = {
    'clean_final_log': not warnings, 'unique_labels': len(labels) == len(set(labels)),
    'references_resolve': set(refs) <= set(labels), 'citations_resolve': set(cites) <= set(bibs),
    'ledger_labels_exist': set(ledger_refs) <= set(labels), 'all_fonts_embedded': all(fonts.values()),
    'pages_nonblank_and_no_unresolved_refs': all(len(t.strip()) > 100 and '??' not in t for t in texts),
    'pdf_matches_build': sha(pdf.read_bytes()) == build['pdf_sha256'],
    'all_sources_match_build': all(sha((ROOT / p).read_bytes()) == h for p, h in build['source_sha256'].items()),
    'eight_other_manuscript_sources_unchanged': len(unchanged) == 8 and all(unchanged.values()),
    'all_retained_evidence_and_provenance_unchanged': all(all(v for k, v in x.items() if k != 'path') for x in archival),
    'comma_provenance_valid_without_new_edit': before[offset:offset+1] == b',' and after == before[:offset] + before[offset+1:] and sha(before) == corr['original_sha256'] and sha(after) == corr['corrected_sha256'],
    'relative_evidence_links_exist': all((ROOT / p).is_file() for p in local_links),
    'R1_present_once': tex.count(r'branch with \(g>0\), strict normal stability') == 1,
    'R1_in_abstract_pdf': 'branchwithg>0' in re.sub(r'\s+', '', texts[0]),
    'R2_present_once': tex.count(r'finite-return sector noted in \cite[Section~8]{energy}') == 1,
    'R2_pdf_citation_resolved': '[3,Section8]' in re.sub(r'\s+', '', ''.join(texts)),
    'active_publication_metadata': 'Author-authorized repository research edition v0.1' in str(reader.metadata.subject),
    'active_review_pending_wording_removed': 'awaits GPT' not in tex and 'Review draft v0.1' not in tex,
}
record = {
    'status': 'PASS' if all(checks.values()) else 'FAIL', 'checks': checks,
    'page_count': len(reader.pages), 'page_text_characters': [len(t) for t in texts],
    'labels': len(labels), 'reference_uses': len(refs), 'bibliography_entries': len(bibs),
    'fonts_embedded': fonts, 'log_warnings': warnings, 'archival_checks': archival,
    'unchanged_manuscript_sources': unchanged, 'pdf': pdf.name, 'pdf_sha256': sha(pdf.read_bytes()),
    'source_sha256': build['source_sha256'], 'metadata': dict(reader.metadata), 'pypdf_version': pypdf_version,
    'visual_inspection': 'Recorded separately after manually viewing every final rendered page.',
    'scope': 'Finalization checks only; no scientific executions or reinvestigation.',
}
(ROOT / 'verification/DOCUMENT_CHECKS.json').write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': record['status'], 'pages': len(reader.pages), 'checks': checks, 'warnings': warnings}, indent=2))
if not all(checks.values()):
    raise SystemExit(1)
