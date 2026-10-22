"""Read-only comparison of SRG Volume I review archives; never runs scientific code.

Usage:
  python verify_editorial_review.py BASELINE.zip EDITORIAL.zip --output result.json \
      [--standalone-pdf corrected.pdf] [--standalone-report REVIEW_REPORT.md]

The output path must be separate from the input artifacts. Rendering/visual
inspection is performed separately and is not asserted by this script.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path, PurePosixPath


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compact(value):
    if isinstance(value, str):
        return re.sub(r'\s+', '', value)
    if isinstance(value, list):
        return [compact(x) for x in value]
    if isinstance(value, dict):
        return {k: compact(v) for k, v in value.items()}
    return value


def inspect_archive(path: Path):
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        assert len(names) == len(set(names)), 'Duplicate ZIP paths'
        assert all(not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts for n in names), 'Unsafe ZIP path'
        assert z.testzip() is None, 'ZIP CRC failure'
        payload = {n: z.read(n) for n in names if not n.endswith('/')}
    manifest = json.loads(payload['MANIFEST.json'])
    listed = manifest['package_files']
    assert {x['path'] for x in listed} == set(payload) - {'MANIFEST.json'}, 'Manifest coverage differs'
    assert len(listed) == len({x['path'] for x in listed}), 'Duplicate manifest paths'
    for item in listed:
        content = payload[item['path']]
        assert len(content) == item['bytes'], item['path']
        assert sha(content) == item['sha256'], item['path']
    return payload, manifest, {
        'filename': path.name, 'bytes': path.stat().st_size,
        'sha256': sha(path.read_bytes()), 'members': len(payload),
        'payloads_verified': len(listed), 'manifest_sha256': sha(payload['MANIFEST.json']),
        'crc_passed': True, 'manifest_exact_coverage': True,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('baseline', type=Path)
    parser.add_argument('candidate', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--standalone-pdf', type=Path)
    parser.add_argument('--standalone-report', type=Path)
    args = parser.parse_args()
    inputs = [args.baseline, args.candidate, args.standalone_pdf, args.standalone_report]
    assert args.output.resolve() not in {p.resolve() for p in inputs if p}, 'Refuse to overwrite input'
    a, am, ai = inspect_archive(args.baseline)
    b, bm, bi = inspect_archive(args.candidate)
    common = set(a) & set(b)
    changed = sorted(n for n in common if a[n] != b[n])
    result = {'review_scope': 'Narrow E01-E02 editorial comparison; no scientific execution',
              'baseline': ai, 'candidate': bi, 'common_changed_paths': changed}
    frozen = {
        'chapter_sources': sorted(n for n in a if re.fullmatch(r'MANUSCRIPT/sections/0[1-6]_.+\.tex', n)),
        'historical_program_copies': sorted(n for n in a if n.startswith('MANUSCRIPT/sources/')),
        'figure_include_files': sorted(n for n in a if re.fullmatch(r'MANUSCRIPT/figures/F\d+\.tex', n)),
        'figure_image_assets': sorted(n for n in a if n.startswith('MANUSCRIPT/figures/') and n.lower().endswith(('.png','.jpg','.jpeg'))),
        'bibliography_sources': ['MANUSCRIPT/references.tex'],
        'build_scripts': ['tools/acquire_typesetter.py','tools/build_pdf.py'],
        'unchanged_evidence_registers': ['EXTERNAL_EVIDENCE_INDEX.md','FIGURE_AND_MEDIA_REGISTER.md'],
    }
    for category, paths in frozen.items():
        assert paths, category
        for name in paths:
            assert a[name] == b[name], f'Substantive change: {name}'
    assert len(frozen['chapter_sources']) == 6
    assert len(frozen['historical_program_copies']) == 3
    assert len(frozen['figure_include_files']) == 17
    assert len(frozen['figure_image_assets']) == 35
    result['byte_identical_groups'] = {k: {'count': len(v), 'paths': v} for k,v in frozen.items()}
    manuscript_changes = [n for n in changed if n.startswith('MANUSCRIPT/') and n.endswith(('.tex','.md'))]
    assert manuscript_changes == sorted(['MANUSCRIPT/README.md','MANUSCRIPT/sections/07_provenance.tex','MANUSCRIPT/sections/08_reproducibility.tex','MANUSCRIPT/volume_i.tex'])
    result['changed_manuscript_documents'] = manuscript_changes
    whitespace_only = ['MANUSCRIPT/sections/07_provenance.tex','CLAIM_EVIDENCE_MATRIX.md','CROSS_STUDY_MECHANISM_MAP.md','OPEN_QUESTIONS_AND_NEXT_VOLUMES.md']
    for n in whitespace_only:
        assert compact(a[n].decode()) == compact(b[n].decode()), f'Non-spacing difference: {n}'
    result['whitespace_only_documents'] = whitespace_only
    # Separate the B.2 build section from the rest of the appendix.
    token1 = '\\section{Manuscript build}'
    token2 = '\\section{Figures and presentation}'
    old = a['MANUSCRIPT/sections/08_reproducibility.tex'].decode()
    new = b['MANUSCRIPT/sections/08_reproducibility.tex'].decode()
    assert compact(old.split(token1)[0]) == compact(new.split(token1)[0])
    assert old.split(token2)[1] == new.split(token2)[1]
    build_section = new.split(token1)[1].split(token2)[0]
    for phrase in ['python -B tools\\acquire_typesetter.py','python -B tools\\build_pdf.py','build/toolchain/tectonic.exe','network access','excluded from the','XeLaTeX','byte identity']:
        assert phrase in build_section, phrase
        assert phrase in b['MANUSCRIPT/README.md'].decode(), 'README missing '+phrase
    assert build_section.index('tools\\acquire_typesetter.py') < build_section.index('tools\\build_pdf.py')
    result['E01'] = {'status': 'CLOSED', 'all_specified_source_replacements_present': True}
    replacements = {
      'MANUSCRIPT/sections/07_provenance.tex': [('800 by800','800 by 800'),('60fps','60 fps'),('20fps','20 fps'),('rows /1,092','rows / 1,092'),('rows /440','rows / 440')],
      'MANUSCRIPT/sections/08_reproducibility.tex': [('All2,000','All 2,000'),('relations;31','relations; 31'),('independent20','independent 20'),('All18','All 18')],
    }
    for name,pairs in replacements.items():
        for before,after in pairs:
            assert before in a[name].decode(), (name,before)
            assert before not in b[name].decode() and after in b[name].decode(), (name,after)
    result['E02'] = {'status':'CLOSED','explicit_compiler_acquisition_precedes_build':True,'scripts_unchanged':True,'instruction_review_only_no_acquisition_or_build_run':True}
    oldclaims=json.loads(a['records/claims.json']);newclaims=json.loads(b['records/claims.json'])
    assert compact(oldclaims)==compact(newclaims), 'Claim content differs beyond whitespace'
    assert len(newclaims)==102 and len({c['id'] for c in newclaims})==102
    for c in newclaims:
        for loc in c['manuscript_locations']:
            text=b[loc['file']].decode().splitlines()[loc['line']-1]
            assert '\\claim{'+c['id']+'}' in text, (c['id'],loc)
    result['claim_entries_verified']=102
    tex='\n'.join(v.decode() for n,v in b.items() if n.startswith('MANUSCRIPT/') and n.endswith('.tex'))
    labels=re.findall(r'\\label\{([^}]+)\}',tex)
    refs=re.findall(r'\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}',tex)
    assert len(labels)==len(set(labels))==63
    assert set(refs)<=set(labels)
    result['source_labels']={'unique':len(labels),'reference_occurrences':len(refs),'unresolved':sorted(set(refs)-set(labels))}
    # Check that all displayed math-environment bodies remain identical.
    envpat=re.compile(r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}(.*?)\\end\{\1\}',re.S)
    equations={}
    for n in sorted(set(a)&set(b)):
        if n.startswith('MANUSCRIPT/') and n.endswith('.tex'):
            ae=envpat.findall(a[n].decode());be=envpat.findall(b[n].decode())
            assert ae==be, 'Math environment differs: '+n
            if ae: equations[n]=len(ae)
    result['unchanged_display_math_environments']={'total':sum(equations.values()),'per_file':equations}
    # Baseline receipts carried into R1 must match their actual old counterparts.
    frozen_receipts={}
    for n in b:
        if n.startswith('baseline/'):
            bare=n[len('baseline/'):]
            target=bare if bare in a else 'records/'+bare
            assert target in a and b[n]==a[target], ('Baseline receipt differs',n,target)
            frozen_receipts[n]=target
    result['preserved_baseline_receipts']=frozen_receipts
    for field,path in [('standalone_pdf_matches',args.standalone_pdf),('standalone_report_matches',args.standalone_report)]:
        if path:
            target='MANUSCRIPT/volume_i.pdf' if 'pdf' in field else 'REVIEW_REPORT.md'
            assert path.read_bytes()==b[target], field
            result[field]=True
    pdf=b['MANUSCRIPT/volume_i.pdf']
    result['accepted_pdf']={'bytes':len(pdf),'sha256':sha(pdf),'archive_path':'MANUSCRIPT/volume_i.pdf'}
    assert len(pdf)==bm['pdf']['pdf_bytes'] and sha(pdf)==bm['pdf']['pdf_sha256']
    log=b['review/typeset.log'].decode(errors='replace')
    result['supplied_build_log']={'overfull_messages':len(re.findall(r'Overfull \\[hv]box',log)), 'underfull_messages':len(re.findall(r'Underfull \\[hv]box',log)), 'undefined_reference_messages':len(re.findall(r'Reference .* undefined',log)), 'missing_character_messages':log.count('Missing character:')}
    assert not result['supplied_build_log']['overfull_messages']
    assert not result['supplied_build_log']['undefined_reference_messages']
    assert not result['supplied_build_log']['missing_character_messages']
    result['windows_preservation']={'independently_live_verified':False,'codex_reported_files':939,'codex_reported_canonical_ledger_unchanged':True,'codex_reported_head_index_status_unchanged':True}
    result['all_assertions_passed']=True
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['baseline','candidate','E01','E02','claim_entries_verified','source_labels','unchanged_display_math_environments','accepted_pdf','supplied_build_log','all_assertions_passed']},indent=2))

if __name__=='__main__':
    main()
