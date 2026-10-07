"""Bounded byte, preservation-of-formulas, and delivery checks; no science replay."""
from pathlib import Path
import argparse
import difflib
import hashlib
import json
import re
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--repository', type=Path, required=True)
args = parser.parse_args()
published = args.repository / 'papers/MEASUREMENT_AND_CHIRAL_DRIFT/v0.1'
checks = []


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(name, value):
    checks.append({'check': name, 'passed': bool(value)})


old_path = published / 'measurement/manuscript.tex'
new_path = ROOT / 'measurement/manuscript.tex'
old = old_path.read_text(encoding='utf-8')
new = new_path.read_text(encoding='utf-8')
check('published v0.1 manuscript bytes', sha(old_path) ==
      '267ed74d11c42668a65b4f0346097b1f91ab64a6d062153f7b01765044f1c2e6')
old_pdf = published / 'measurement/Measurement_Geometry_v0.1.pdf'
check('published v0.1 PDF bytes', sha(old_pdf) ==
      '117474240877e9eaa61faa041d6e362fbdb5ec9b6971569563d2d746674f0fed')
body = re.sub(r'% BEGIN V0.1.1 LINEAGE APPENDIX.*?% END V0.1.1 LINEAGE APPENDIX',
              '', new, flags=re.S)
pattern = r'(?<!\\)\\\[.*?\\\]|\\\(.*?\\\)'
old_math = re.findall(pattern, old, re.S)
new_math = re.findall(pattern, body, re.S)
expected_math = [m for m in old_math if m != r'\(0.544\)']
check('all inherited math retained except two requested decimal mentions',
      len(old_math) == 429 and len(new_math) == 427 and new_math == expected_math)
check('all inherited equation and theorem labels retained',
      set(re.findall(r'\\label\{([^}]+)\}', old)) <=
      set(re.findall(r'\\label\{([^}]+)\}', new)))
check('remembered decimal absent from revision manuscript', '0.544' not in new)
begin = '% BEGIN V0.1.1 LINEAGE APPENDIX'
end = '% END V0.1.1 LINEAGE APPENDIX'
appendix = new[new.index(begin):new.index(end) + len(end)]
stored_appendix = (ROOT / 'provenance/lineage_appendix.tex').read_text(encoding='utf-8')
check('lineage appendix matches provenance copy', appendix.strip() == stored_appendix.strip())
diff = ''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
               fromfile='published v0.1 measurement/manuscript.tex',
               tofile='candidate v0.1.1 measurement/manuscript.tex'))
(ROOT / 'provenance/manuscript_v0.1_to_v0.1.1.diff').write_text(diff, encoding='utf-8')

inherited = published / 'measurement/supplement'
copied = ROOT / 'measurement/supplement'
originals = [p for p in inherited.rglob('*') if p.is_file()]
check('entire inherited measurement supplement byte-identical',
      all((copied / p.relative_to(inherited)).is_file() and
          sha(p) == sha(copied / p.relative_to(inherited)) for p in originals))
geometry = copied / 'native/kernel_physics/geometry.py'
check('figure geometry equals authoritative repository data',
      sha(geometry) == sha(args.repository / 'kernel_physics/geometry.py'))
fig = json.loads((ROOT / 'results/figure_verification.json').read_text())
check('three ordered octagons, 18 welded vertices and complete edge rendering',
      fig['status'] == 'PASS' and fig['faces'] == 3 and
      fig['vertices_per_face'] == [8, 8, 8] and fig['welded_vertices'] == 18 and
      len(fig['rendered_edge_incidences']) == 24 and
      len(fig['rendered_local_vertex_incidences']) == 24 and
      fig['exact_panel_map_order_verified'] and
      fig['all_global_vertices_distinct_in_projection'] and
      not fig['hidden_edge_culling'] and not fig['polygon_fill_used'])
lineage = json.loads((ROOT / 'results/lineage_verification.json').read_text())
check('bounded lineage factorization verification retained',
      lineage['status'] == 'PASS' and
      lineage['maximum_entrywise_absolute_residual'] < lineage['tolerance'])
sources = json.loads((ROOT / 'provenance/lineage_sources.json').read_text())
check('all lineage primary sources match recorded original hashes',
      all(sha(args.repository.parent / row['original_project_locator']) ==
          row['original_sha256'] for row in sources))
for row in sources:
    if 'excerpt_path' in row:
        check('primary excerpt hash ' + row['id'],
              sha(ROOT / row['excerpt_path']) == row['excerpt_sha256'])
    elif 'copy_path' in row:
        check('primary snapshot hash ' + row['id'],
              sha(ROOT / row['copy_path']) == row['copy_sha256'])

pdf = ROOT / 'measurement/Measurement_Geometry_v0.1.1.pdf'
reader = PdfReader(pdf)
pdf_record = {'path': pdf.relative_to(ROOT).as_posix(), 'pages': len(reader.pages),
              'bytes': pdf.stat().st_size, 'sha256': sha(pdf)}
check('final PDF identity', pdf_record['pages'] == 20 and
      pdf_record['bytes'] == 411097 and pdf_record['sha256'] ==
      'fd7f60a4d1ea5e55c24aa692250e5976aff018a1ef76b724bfdecd39da5e8179')
build = json.loads((ROOT / 'results/build/build.json').read_text())
check('PDF agrees with build record', pdf_record['bytes'] == build['bytes'] and
      pdf_record['sha256'] == build['sha256'])
text = '\n'.join(p.extract_text() or '' for p in reader.pages)
check('PDF contains revision and lineage appendix, no remembered decimal',
      'v0.1.1' in text and 'Recursive lineage' in text and '0.544' not in text)
log = (ROOT / 'results/build/manuscript.log').read_text(encoding='utf-8')
check('no overfull, missing-character or undefined-reference build warnings',
      not re.search(r'Overfull|Missing character|undefined', log, re.I))
check('all final page renders retained',
      len(list((ROOT / 'qa/rendered_pages').glob('page-*.png'))) == 20)
check('candidate does not contain a replaced v0.1 PDF or drift lane',
      not (ROOT / 'measurement/Measurement_Geometry_v0.1.pdf').exists() and
      not (ROOT / 'drift').exists())
result = {'status': 'PASS' if all(c['passed'] for c in checks) else 'FAIL',
          'scope': 'Bounded correction checks only; no predecessor science suite replay',
          'checks_passed': sum(c['passed'] for c in checks), 'checks_total': len(checks),
          'inherited_math_expressions': len(new_math),
          'inherited_supplement_files_preserved': len(originals),
          'pdf': pdf_record, 'checks': checks}
(ROOT / 'results/candidate_checks.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))
raise SystemExit(0 if result['status'] == 'PASS' else 1)
