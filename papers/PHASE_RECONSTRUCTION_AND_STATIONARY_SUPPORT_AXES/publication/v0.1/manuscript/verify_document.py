"""Document and focused source-byte checks only; no scientific execution."""
import argparse
import hashlib
import importlib
import json
from pathlib import Path
import re
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--python-packages', help='Optional existing directory containing pypdf; never installed here.')
args = parser.parse_args()
if args.python_packages:
    sys.path.append(str(Path(args.python_packages).resolve()))
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
out = ROOT/'verification'
out.mkdir(exist_ok=True)
sha = lambda data:hashlib.sha256(data).hexdigest()
pdf = ROOT/'NATIVE_PHASE_SPATIAL_v0.1.pdf'
reader = PdfReader(pdf)
texts = [page.extract_text() or '' for page in reader.pages]
(out/'extracted_text.txt').write_text('\n\n'.join(f'PAGE {i+1}\n{text}' for i,text in enumerate(texts)),encoding='utf-8')
tex = '\n'.join(p.read_text(encoding='utf-8') for p in sorted((ROOT/'manuscript').glob('*.tex')))
labels = re.findall(r'\\label\{([^}]+)\}',tex)
refs = re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',tex)
bibs = re.findall(r'\\bibitem\{([^}]+)\}',tex)
cites = [key for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',tex) for key in group.split(',')]
log = (ROOT/'build/main.log').read_text(encoding='utf-8',errors='replace')
bad = [line for line in log.splitlines() if re.search(r'undefined|multiply defined|Overfull|Underfull|Missing character|LaTeX Warning|Package .* Warning',line)]
fonts = {}
internal_links = []
named = reader.named_destinations
for number,page in enumerate(reader.pages,1):
    for ref in page['/Resources'].get('/Font',{}).values():
        font = ref.get_object()
        owner = font['/DescendantFonts'][0].get_object() if '/DescendantFonts' in font else font
        desc = owner.get('/FontDescriptor')
        desc = desc.get_object() if desc else {}
        fonts[str(font.get('/BaseFont'))] = any(key in desc for key in ('/FontFile','/FontFile2','/FontFile3'))
    for annotation in page.get('/Annots',[]):
        obj = annotation.get_object()
        action = obj.get('/A')
        action = action.get_object() if action else {}
        if action.get('/S') == '/GoTo' and isinstance(action.get('/D'),str):
            target = action['/D']
            internal_links.append({'page':number,'target':target,'resolved':target in named})
manifest = json.loads((ROOT/'provenance/source_manifest.json').read_text(encoding='utf-8'))
source_matches = []
for item in manifest['sources']:
    source_matches.append({'id':item['id'],'copy_matches':sha((ROOT/item['package_path']).read_bytes())==item['sha256'],
                           'original_unchanged':sha(Path(item['original_path']).read_bytes())==item['sha256']})
build = json.loads((ROOT/'build/build_receipt.json').read_text(encoding='utf-8'))
local = [{'target':target,'exists':(ROOT/target).is_file()} for target in re.findall(r'\\href\{([^}]+)\}',tex) if not target.startswith(('https://','http://'))]
checks = {
 'unique_labels':len(labels)==len(set(labels)),
 'cross_references_resolved':set(refs)<=set(labels),
 'citations_resolved':set(cites)<=set(bibs),
 'clean_final_compiler_log':not bad,
 'all_pages_have_text':all(len(t.strip())>100 for t in texts),
 'no_unresolved_question_marks':all('??' not in t for t in texts),
 'all_fonts_embedded':bool(fonts) and all(fonts.values()),
 'all_internal_PDF_destinations_resolved':all(x['resolved'] for x in internal_links),
 'all_relative_PDF_links_exist':all(x['exists'] for x in local),
 'source_and_evidence_copies_preserved':all(x['copy_matches'] and x['original_unchanged'] for x in source_matches),
 'pdf_matches_build_receipt':sha(pdf.read_bytes())==build['pdf_sha256'],
 'manuscript_matches_build_receipt':all(sha((ROOT/path).read_bytes())==value for path,value in build['source_sha256'].items()),
 'research_edition_status_in_metadata':'Author-authorized repository research edition v0.1' in str(reader.metadata.subject) and 'author publication approval granted' in str(reader.metadata.subject),
 'author_metadata_correct':reader.metadata.author=='Hilmir Frímann Halldórsson',
 'full_state_wording_corrected':'physical-state relation' not in tex and 'full-state relation' in tex,
 'witness_described_as_analytic':'numerical native-step evaluation' in tex and 'analytically differentiates the native map' in tex,
 'overlap_unit_factor_normalized':r'\frac{B_{{\rm sec},h}}{|B_{{\rm sec},h}|}' in tex,
 'separate_EMA_dependency_rows':'EMA memory update &' in tex and 'EMA observation from current memory &' in tex,
}
record = {'status':'PASS' if all(checks.values()) else 'FAIL','checks':checks,'page_count':len(reader.pages),
          'pdf_sha256':sha(pdf.read_bytes()),'pdf_bytes':pdf.stat().st_size,
          'page_text_lengths':[len(t) for t in texts], 'fonts_embedded':fonts,
          'internal_PDF_links':internal_links,'relative_PDF_links':local,'source_checks':source_matches,
          'label_count':len(labels),'reference_count':len(refs),'bibliography_count':len(bibs),
          'final_log_warnings':bad,'pypdf_version':importlib.import_module('pypdf').__version__,
          'python_executable':sys.executable,'source_sha256':build['source_sha256'],
          'scope':'Document/provenance checks, not mathematical revalidation. Visual inspection recorded separately.'}
(out/'DOCUMENT_CHECKS.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'status':record['status'],'pages':record['page_count'],'pdf_sha256':record['pdf_sha256'],
                  'checks':checks,'pypdf_version':record['pypdf_version'],'embedded_fonts':len(fonts),
                  'internal_links':len(internal_links),'local_links':len(local)},indent=2))
if not all(checks.values()):
    raise SystemExit(1)
