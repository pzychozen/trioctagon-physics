"""Verify editorial-only revision against the immutable pre-revision snapshot.

Writes only revision documentation in this paper lane. No Git write, native
execution, checkpoint rerun, mathematical extension or network operation.
Run after paper verification/build/QA/seal, then finalize_package.py; use
--verify-final to confirm the resulting allowlist and package hashes.
"""
from pathlib import Path
import argparse, difflib, hashlib, json, re

L = Path(__file__).resolve().parents[1]
R = L.parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--verify-final', action='store_true')
args = parser.parse_args()
def sha(b): return hashlib.sha256(b).hexdigest()
def read(p): return json.loads((L/p).read_text(encoding='utf8'))
b = read('provenance/publication_revision_baseline.json')
tex = {p.name:p.read_text(encoding='utf8') for p in sorted((L/'manuscript').glob('*.tex'))}
for name, text in tex.items():
    blocks = re.findall(r'\\begin\{(equation\*?|align\*?|gather\*?|theorem|proposition|lemma|proof)\}(.*?)\\end\{\1\}', text, re.S)
    assert sha(json.dumps(blocks, ensure_ascii=False).encode()) == b['displayed_math_and_proof_blocks_sha256'][name], name
assert sha(tex['discussion.tex'].split(r'\section{Relation to established mathematics}')[0].encode()) == b['interpretation_section_sha256']
for p in ['manuscript/response.tex', 'manuscript/observables_closure.tex', 'manuscript/evidence_tables.tex',
          'provenance/PAPER_SOURCE_CROSSWALK.md', 'provenance/baseline.json', 'provenance/source_manifest.json',
          'verification/verify_paper.py', 'verification/retained_evidence.json', 'verification/retained_predicates.json']:
    assert sha((L/p).read_bytes()) == b['files'][p]['sha256'], p
for p,v in b['files'].items():
    if p.startswith(('tmp/', 'figures/')):
        assert sha((L/p).read_bytes()) == v['sha256'], p
assert tex['appendices.tex'] == b['before_text_for_editorial_diff']['manuscript/appendices.tex'].replace('This candidate uses the plus sign', 'This paper uses the plus sign')
old_spectral = b['before_text_for_editorial_diff']['manuscript/spectral.tex']
note = tex['spectral.tex'].splitlines()[1] + '\n\n'
assert 'Because ``symmetrizable' in note and r'\(GJ=J^TG\)' in note
assert tex['spectral.tex'].replace(note, '').replace('General SPD self-adjointness', 'General positive-definite symmetrizability').replace('arbitrary SPD self-adjointness', 'arbitrary SPD symmetrizability') == old_spectral
ledger = read('provenance/theorem_ledger.json')['records']
assert len(ledger) == 45
for rec in ledger:
    if rec['id'] == 'L45':
        rec['hypotheses'] = rec['hypotheses'].replace('publication synthesis.', 'publication candidate.')
        rec['interpretation_limit'] = rec['interpretation_limit'].replace('Research publication stops', 'Publication candidate stops')
    assert sha(json.dumps(rec, sort_keys=True, ensure_ascii=False).encode()) == b['ledger_records_sha256'][rec['id']], rec['id']
context = tex['discussion.tex'].split(r'\section{Relation to established mathematics}')[1].split(r'\section{Limitations, open questions and conclusion}')[0]
keys = {'LP', 'Chung', 'Kuchment', 'SW', 'GSS', 'MS'}
cites = set(re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', context))
assert keys <= cites
old_bib = b['before_text_for_editorial_diff']['manuscript/references.tex']
assert tex['references.tex'].startswith(old_bib.split(r'\end{thebibliography}')[0])
assert set(re.findall(r'\\bibitem\{([^}]+)\}', tex['references.tex'])) - set(re.findall(r'\\bibitem\{([^}]+)\}', old_bib)) == keys
for name,t in tex.items():
    assert not re.search(r'publication candidate|scientific review candidate|prepared for GPT scientific review', t, re.I), name
local = read('verification/paper_local_results.json')
assert local['passed'] and local['paper_local_predicate_count'] == 61
assert read('verification/retained_predicates.json')['total'] == 429
for p,h in local['inputs_sha256'].items(): assert sha((L/p).read_bytes()) == h, p
pres = read('provenance/preservation.json')
assert pres['protected_checkout_unchanged'] and not pres['changed_checkpoints']
assert pres['after']['head'] == b['head']
build = read('publication/build_record.json'); qa = read('publication/pdf_qa_results.json')
pdf = L/build['pdf']; h = sha(pdf.read_bytes())
assert h == build['pdf_sha256'] == qa['pdf_sha256']
assert qa['automated_checks_passed'] and qa['all_pages_rendered']
qa_text = (L/'publication/PDF_QA.md').read_text(encoding='utf8')
assert h in qa_text and '**38 A4 pages**' in qa_text

diff = []
for p,old in b['before_text_for_editorial_diff'].items():
    current = (L/p).read_text(encoding='utf8')
    diff.extend(difflib.unified_diff(old.splitlines(True), current.splitlines(True), fromfile='before/'+p, tofile='after/'+p))
(L/'provenance/EDITORIAL_DIFF.patch').write_text(''.join(diff), encoding='utf8')
planned = {'provenance/PUBLICATION_REVISION.md','provenance/COMMIT_ALLOWLIST.txt','provenance/package_manifest.json'}
current = {p.relative_to(L).as_posix():sha(p.read_bytes()) for p in L.rglob('*') if p.is_file()}
assert not set(b['files']) - set(current), 'An original lane file was removed'
changes = sorted({p for p,hp in current.items() if p not in b['files'] or hp != b['files'][p]['sha256']} | planned)
assert not any(p.startswith('tmp/') for p in changes)
new = [p for p in changes if p not in b['files']]
modified = [p for p in changes if p in b['files']]
rows = '\n'.join('| '+('Added' if p in new else 'Modified')+' | `papers/NATIVE_RESPONSE_GEOMETRY/'+p+'` |' for p in changes)
report = f'''# Final publication revision record

Research publication v0.1, 6 October 2026. The user-reported GPT scientific verdict was PASS WITH MINOR REQUIRED PUBLICATION CHANGES. This record covers those editorial changes only; final GPT publication approval remains pending. No stage, commit, push, tag, release, DOI registration or public post occurred.

## PDF identity

Title: Native Response Geometry and Spectral Circulation in the Tri-Octagon Map. Status: Research publication v0.1. Subtitle now uses SPD Self-Adjointness.

- File: `publication/Native_Response_Geometry_v0.1.pdf`
- Pages: **{qa['page_count']} A4 pages** (previously 36).
- Bytes: **{pdf.stat().st_size}**.
- SHA-256: `{h}`.
- Tectonic 0.17.0; exact command and inputs in `publication/build_record.json`.

## Required changes and validation

- Title-page, running-header, PDF and companion publication status changed to Research publication v0.1. No claim of external peer review, journal submission, DOI or repository release.
- Section 7 contains the requested distinction between diagonal balance and SPD self-adjointness. The subtitle, heading and natural prose uses follow that terminology; theorem variables and formulas are unchanged.
- The abstract and conclusion state N >= 9, three-distinct repeated backgrounds and the explicit nondegeneracy hypothesis; the six-ring statement remains separate. Section 9 retains the exact displayed nondegeneracy condition unchanged.
- Six new contextual bibliography entries, all cited in Section 15: Levin-Peres (2017, with Wilmer contributions); Chung (1997); Kuchment (2016); Singer-Wu (2012); Golubitsky-Stewart-Schaeffer II (1988); McKee-Smyth (2020). Full entries, primary URLs and inspected locators are in `LITERATURE_REVIEW_NOTE.md`. No model-specific attribution or priority claim.
- **61/61 paper-local checks PASS** using the unchanged verification script. The retained **429** checkpoint predicates remain separately counted and unchanged; no predecessor script was rerun.
- All original theorem/proposition/lemma/proof and equation/align/gather blocks match the pre-revision snapshot. The complete response, observable/closure and evidence-table source files are byte-identical.
- All 45 ledger records match, with only two publication-status phrases in L45 updated. The proof/source crosswalk is byte-identical. The 61-check suite validates proof anchors and references.
- The GR1 plus sign and its GR2 transcription reconciliation remain exactly as previously recorded; only “This candidate” became “This paper” in Appendix C. The response source and L13 ledger record are unchanged.
- Section 14 interpretation boundaries are unchanged. The updated contexts in the word audit introduce no physical identification.
- All **38** pages were rendered anew and visually inspected in contact sheets, with full-page inspection of PDF pages 1, 9, 20, 21, 22, 26, 31, 32, 37 and 38. No clipping, overlap, missing glyph, broken table or reference defect was found. Automated page-bounds/text checks and compiler diagnostics pass. See `publication/PDF_QA.md`.

## Preservation and Git state

Starting and final HEAD: `{b['head']}`. Branch: main. Original Git index and unrelated dirty status unchanged. The aggregate byte inventory of all {pres['after']['files']} protected repository files outside this lane ({pres['after']['bytes']} bytes) matches the original baseline. All 15 GR0/GR1/GR2/CM0/SA0 artifacts match their original hashes.

This covers kernel_physics, UI, existing Papers A-G, the Mathematical Atlas, fixtures, historical/production material and unrelated tracked/untracked files. All figure sources/exports are also unchanged. Three-Way remains PARKED; Paper G remains closed.

All **85 existing tmp files** are byte-identical and remain excluded from the commit allowlist. Fresh renders were written outside the repository, at the path recorded in the QA JSON. No cleanup of the blocked previews was attempted.

## Exact changed paths for this revision

Relative to the immutable pre-revision lane snapshot: **{len(modified)} modified**, **{len(new)} added**, **0 deleted**. This is the editorial revision delta, not a Git staged diff: the whole paper lane is still untracked. Generated build/QA/provenance records are included below. Historical “candidate” wording inside the immutable snapshot and before-side diff is evidence, not current publication metadata.

| Change | Repository-relative path |
|---|---|
{rows}

The before/after editorial text is retained in `EDITORIAL_DIFF.patch`. The snapshot is `publication_revision_baseline.json`; it does not replace the protected scientific baseline.

## Proposed publication action, awaiting authorization

The exact proposed commit allowlist is `COMMIT_ALLOWLIST.txt`; its file hashes are in `package_manifest.json`. It contains only this paper lane and excludes every `tmp/` preview and Python bytecode file. No protected or unrelated path is included.

Proposed commit message: `papers: add native response geometry research publication v0.1`.

The final proposed GitHub title/body and optional public-post drafts are in `../PUBLICATION_PROPOSAL.md`. They remain unpublished. **STOP: await GPT final publication approval.**
'''
(L/'provenance/PUBLICATION_REVISION.md').write_text(report, encoding='utf8')
if args.verify_final:
    expected = sorted('papers/NATIVE_RESPONSE_GEOMETRY/'+p.relative_to(L).as_posix() for p in L.rglob('*') if p.is_file() and 'tmp' not in p.relative_to(L).parts and '__pycache__' not in p.parts)
    assert (L/'provenance/COMMIT_ALLOWLIST.txt').read_text(encoding='utf8').splitlines() == expected
    for entry in read('provenance/package_manifest.json')['files']:
        assert sha((L/entry['path']).read_bytes()) == entry['sha256'], entry['path']
    actual = {p.relative_to(L).as_posix() for p in L.rglob('*') if p.is_file() and (p.relative_to(L).as_posix() not in b['files'] or sha(p.read_bytes()) != b['files'][p.relative_to(L).as_posix()]['sha256'])}
    assert actual == set(changes)
print(json.dumps({'editorial_preservation_passed':True, 'paper_local_checks':'61/61 PASS', 'retained_checkpoint_checks':429, 'changed_paths':len(changes), 'modified':len(modified), 'added':len(new), 'pages':qa['page_count'], 'pdf_sha256':h, 'final_manifest_verified':args.verify_final}, indent=2))
