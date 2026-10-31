"""Bounded after-hash audit and evidence indexing. No project imports."""
from pathlib import Path
import json,hashlib,zipfile,datetime,collections
ROOT=Path(__file__).resolve().parent
P=ROOT/'packet/NCM_PAPER_01_Codex_Packet_v0.1'
def digest(p):
    b=p.read_bytes()
    return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def save(p,obj): (ROOT/p).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
before=json.loads((ROOT/'SOURCE_MANIFEST.before.json').read_text(encoding='utf-8'))
reads=json.loads((ROOT/'source_reads.json').read_text(encoding='utf-8'))
records={}
for key,entry in before['sources'].items():
    now=digest(Path(entry['path']))
    was={k:entry[k] for k in ('bytes','sha256')}
    assert now==was,key
    ranges=sorted(set((r['first'],r['last']) for r in reads if r['source']==key))
    records[key]={'path':entry['path'],'before':was,'after':now,'unchanged':True,'passages_read_inclusive':ranges}
packetafter=digest(Path(before['packet']['path']))
assert packetafter=={k:before['packet'][k] for k in ('bytes','sha256')}
packetmembers=json.loads((ROOT/'PACKET_MEMBERS.before.json').read_text(encoding='utf-8'))
print('packet member before schema',type(packetmembers).__name__)
if isinstance(packetmembers,dict):
    entries=packetmembers.items()
else:
    entries=((r['path'],r) for r in packetmembers)
checked=[]
for name,entry in entries:
    path=ROOT/'packet'/name
    if not path.exists(): path=P/name
    now=digest(path)
    assert now=={k:entry[k] for k in ('bytes','sha256')},name
    checked.append({'path':str(path.relative_to(ROOT)).replace('\\','/'),'before':entry,'after':now,'unchanged':True})
out={'scope':'Seven inspected scientific source files, standalone order, supplied packet ZIP and its extracted members; not a whole-repository audit.',
     'before_utc':before['utc'],'after_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'environment_before':before['environment'],'tools_before':before['tools'],
     'sources':records,'packet_zip':{'path':before['packet']['path'],'before':{k:before['packet'][k] for k in ('bytes','sha256')},'after':packetafter,'unchanged':True},
     'packet_members':checked,'unavailable_sources':[],'mismatched_sources':[],
     'source_comparison_to_prior':json.loads((ROOT/'evidence/RECONCILIATION.json').read_text())['source_comparisons'],
     'qualification':'Hashes establish byte identity, not scientific correctness, authorship or authenticated execution.',
     'native_F_evaluations':0,'old_scientific_scripts_executed':0}
save('SOURCE_MANIFEST.json',out)

aliases={'DYN':'DYNAMICS','OBS':'OBSERVABLES','COH':'COHERENT','D1':'D1','Z':'Z','M3':'M3','BRIDGE':'BRIDGE'}
titles={
 'DYN':'Native deterministic nonlinear map. Tri-Octagon project source, 2026.',
 'OBS':'Equivariant spatial observables. Hilmir Frímann Halldórsson, Native Response Geometry chapter, 2026.',
 'COH':'Transient Collective Turning and Coherent Relaxation in the Native Triad. Hilmir Frímann Halldórsson, research edition v0.1, 28 October 2026.',
 'D1':'Cubic Common-Phase Drift on a Chiral Branch of the Tri-Octagon Map. Hilmir Frímann Halldórsson, research publication v0.1, 6 October 2026.',
 'Z':'Staged and EMA Z observers. Tri-Octagon project source, 2026.',
 'M3':'Geometry-Attached Axial Observables, Period-Doubling, and Certified Entrance Capture in the Tri-Octagon Map. Hilmir Frímann Halldórsson, Paper G v0.1.1, 4 October 2026; retained M3 results.',
 'BRIDGE':'SRG Final Mathematical Bridge: From lens geometry to recurrence and known equations. Project synthesis prepared for Hilmir Frímann Halldórsson, publication edition v0.1, 27 October 2026.'}
lines=['# Evidence index','',
 'The package uses inspected local project sources and byte-preserved retained evidence. IDs resolve the manuscript bibliography without relying only on absolute Windows links. Selected source files are referenced, not repackaged. No whole repository or environment is included.','',
 '## Provenance layers','',
 '1. Original Windows research: DUAL-01, DUAL-02 and final DUAL-03 phase_b evidence. Native call counts belong here.',
 '2. Prior GPT internal reviews: retained review Markdown. These report reviewer checks and proposals; they are not original Windows execution records.',
 '3. Current manuscript work: packet/JSON reconciliation, 29 exact algebra checks, independent written sector proof, document build and visual QA. Zero native F calls and zero old scientific script executions.','',
 'Known original roots (reading locators, not current execution locations):',
 '- C:/TORMENT/TRIOCTAGON_new/research/NATURAL_CORE_MOTION_DUALITY_01',
 '- C:/TORMENT/TRIOCTAGON_new/research/NATURAL_CORE_MOTION_DUALITY_BRIDGE_01',
 '- C:/TORMENT/TRIOCTAGON_new/research/NATURAL_CORE_MOTION_NATIVE_RETURN_01/phase_b','',
 'The final phase_b report controls DUAL-03 outcomes. The earlier missing-packet snapshot remains history. This work order authorizes the manuscript now; old administrative “no manuscript” statements do not block drafting. Scientific findings are unchanged.','']
for alias,key in aliases.items():
    r=records[key]
    lines += [f'<a id="{alias.lower()}"></a>',f'## {alias}', '',titles[alias],'',
              'Checkout-relative locator: '+r['path'].split('trioctagon-physics\\',1)[1].replace('\\','/'),
              'Absolute reading path: '+r['path'],
              'Passages inspected (inclusive line ranges): '+', '.join(f'{a}–{b}' for a,b in r['passages_read_inclusive']),
              f"Bytes: {r['before']['bytes']}. SHA-256: {r['before']['sha256']}.",
              'Before/after identical; current bytes also match the retained DUAL-02 source manifest. See SOURCE_MANIFEST.json.','']
packetrefs=[
 ('D01','context/NCM_DUAL_01_REPORT.md','Completed prescribed-cone investigation; retained report only, no private sketch reproduced.'),
 ('D02','context/NCM_DUAL_02_REPORT.md','Completed correspondence/return investigation; full unchanged archive included.'),
 ('D03','context/NCM_DUAL_03_REPORT.md','FINAL phase_b report; byte-identical to phase_b/REPORT.md in the included archive.'),
 ('REV02','reviews/NCM_DUAL_02_GPT_REVIEW.md','Prior GPT internal review; conditional cubic diagnostic.'),
 ('REV03','reviews/NCM_DUAL_03_GPT_REVIEW.md','Prior GPT internal review; Section 5 is the proposal independently accepted in the current proof review.')]
for key,rel,descr in packetrefs:
    path=P/rel;d=digest(path);link=path.relative_to(ROOT).as_posix()
    lines += [f'<a id="{key.lower()}"></a>',f'## {key}','',descr,'',f'[{rel}]({link})',
              f"Bytes: {d['bytes']}. SHA-256: {d['sha256']}.",'']
lines += ['## Immutable archives and frozen plan','']
for rel in ['evidence/NCM_DUAL_02_v0.1_REVIEW.zip','evidence/NCM_DUAL_03_v0.1_REVIEW.zip',
            'context/NCM_DUAL_03_PLAN.md','context/NCM_DUAL_03_PLAN_FREEZE.json',
            'context/NCM_DUAL_03_attempt_ledger.jsonl','context/NCM_DUAL_03_discovery_summary.json']:
    path=P/rel;d=digest(path)
    lines += [f'[{rel}]({path.relative_to(ROOT).as_posix()})',
              f"Bytes: {d['bytes']}. SHA-256: {d['sha256']}.",'']
with zipfile.ZipFile(P/'evidence/NCM_DUAL_03_v0.1_REVIEW.zip') as z:
    names=z.namelist()
    tests=[n for n in names if n.startswith('phase_b/') and ('test' in n or 'analysis_results' in n)]
    print('Retained test/analysis member paths:',json.dumps(tests))
    metrics=json.loads((ROOT/'evidence/RETAINED_ATTEMPT_METRICS.json').read_text())
    stops=dict(collections.Counter(r['stop_reason'] for r in metrics.values() if r['classification']=='solver_failed'))
    print('Retained failed stop reasons:',json.dumps(stops))
    assert len([n for n in names if n.startswith('phase_b/attempts/') and n.endswith('.json')])==60
    for rel in ['phase_b/REPORT.md','phase_b/PLAN.md','phase_b/PLAN_FREEZE.json','phase_b/numerical_groups.json','phase_b/analysis_results.json']:
        assert rel in names,rel
    lines += ['Relevant DUAL-03 ZIP members:',
              '- phase_b/REPORT.md, PLAN.md, PLAN_FREEZE.json, resolved_plan.json.',
              '- phase_b/attempts/S01.json through S60.json: every original attempt and failure.',
              '- phase_b/attempt_ledger.jsonl, discovery_summary.json, analysis_results.json, numerical_groups.json.']
    lines += ['- '+n for n in tests]
lines += ['','The current evidence/RETAINED_GROUPS_EXTRACT.json is a parsed copy of the retained group data. RETAINED_ATTEMPT_METRICS.json identifies each original member and its hash; RECONCILIATION.json records classifications and freeze/lineage checks. These are current extractions, not new scientific outcomes.','',
          '## Current proof and document review','',
          '- proof_review/SECTOR_60_REVIEW.md: ACCEPTED continuous proof.',
          '- proof_review/check_symbolic.py, SYMBOLIC_RESULTS.json, SYMBOLIC_LOG.txt: 29 exact supporting checks, zero F.',
          '- qa/BUILD_RECORD.json, PDF_STRUCTURE.json, PDFINFO.txt and final page PNGs: document construction/inspection.',
          '- MANUSCRIPT_QA.md and CORRECTIONS_AND_DISPOSITION.md: scope, corrections and final page review.',
          '- SOURCE_MANIFEST.json: bounded before/after identities.',
          '- OUTPUT_HASHES.json and external ARCHIVE_RECEIPT.json: packaged files and ZIP verification.','',
          'No external novelty assessment or producer attestation is implied. This is not publication approval.']
(ROOT/'EVIDENCE_INDEX.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'Preserved {len(records)} bounded files, packet ZIP, and {len(checked)} extracted packet members.')
