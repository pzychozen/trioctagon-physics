"""Record claim provenance and closeout integrity; no trajectory evaluation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, sys, zipfile

R = Path(__file__).resolve().parents[1]
assert os.environ.get('CONDA_DEFAULT_ENV') == 'torment'
assert sys.flags.optimize == 0, 'Validation must run with assertions enabled'

def sha(b): return hashlib.sha256(b).hexdigest()
def read(p): return json.loads((R / p).read_text(encoding='utf-8'))
def write(p, obj): (R / p).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
def locate(path, marker):
    b = (R / path).read_bytes()
    lines = b.decode('utf-8').splitlines()
    hits = [i for i, line in enumerate(lines, 1) if marker in line]
    assert hits, (path, marker)
    return {'path': path, 'locator': marker, 'line': hits[0], 'sha256': sha(b)}

primary = 'sources/collective/main.tex'
report = 'NATIVE_TURNING_CAPTURE_01_PROOF_REVIEW.md'
claims = []
def claim(id, status, statement, refs, limit=None):
    row = {'id': id, 'status': status, 'statement': statement,
           'locators': [locate(p, m) for p, m in refs]}
    if limit: row['qualification'] = limit
    claims.append(row)

claim('I01', 'inherited', 'Exact simultaneous ordered native map, fixed rational coefficients and original seed.',
      [(primary, r'\label{eq:parameters}'), (primary, r'\label{eq:entrance}'), ('sources/dynamics.py', 'def _advance'), (report, '## R2.')])
claim('I02', 'inherited', 'Strict positive two-step collective turning at the original entrance.',
      [(primary, r'\label{eq:turn}'), (primary, r'\label{eq:certturn}'), ('scripts/check_certificate.py', 'turn=sub')],
      'Fresh early-step evaluation is a dependency check inside the connected certificate, not rediscovery.')
claim('I03', 'inherited', 'D is forward invariant and every orbit admitted to D converges to an aligned positive amplitude profile unique in the stated cube.',
      [(primary, r'\label{sec:domain}'), (primary, r'\label{thm:convergence}'), (primary, r'\label{eq:fixed}')])
claim('I04', 'inherited', 'Quantitative convergence, unequal residual amplitude spread and decay of C,W,Gamma after D admission.',
      [(primary, r'\label{eq:radialbound}'), (primary, r'\label{eq:fullbound}'), (primary, r'\label{eq:limits}'), (primary, r'\label{eq:Cdecay}')],
      'The residual bound below .005270 is not the actual limiting value.')
claim('I05', 'inherited', 'Exact mean accounting separates onsite and synchronization contributions; graph cancellation does not imply graph independence of full dynamics.',
      [(primary, r'\label{eq:budget}'), (report, '## R8.')],
      'The phase-off delayed-graph comparison is not a causal ablation of this nonzero-lambda orbit.')
claim('N01', 'newly proved/certified', 'DISTINCT_GAP in the bounded inspected source corpus; gate completed before new trajectory evaluation.',
      [('PRIOR_WORK_COMPARISON.md', 'Outcome:'), ('logs/PRIOR_GATE.json', 'frozen_utc'), (report, '## R2.')],
      'A source-comparison disposition, not an exhaustive novelty theorem or revalidation of old proofs.')
claim('E01', 'numerical only', 'One-seed exploration found a first numerical D hit at 41 and selected the comfortably interior target 50.',
      [('data/EXPLORATION.json', 'first_numerical_D_entry'), ('scripts/explore.py', 'def arc'), (report, '## R3.')],
      '90-digit and binary64 results are neither enclosures nor certified earliest-entry claims.')
claim('N02', 'newly proved/certified', 'All 50 updates from the original exact seed are connected by valid enclosures; all 150 prestages have modulus greater than 87/100.',
      [('scripts/check_certificate.py', 'def validate'), ('data/CERTIFICATE_CHECK.json', 'linked_updates_verified'), (report, '## R4.')],
      'Computational proof checked by a separate exact-rational implementation; no claim of formal interpreter verification.')
claim('N03', 'newly proved/certified', 'F^50 of the exact entrance lies strictly inside D, with the three listed rational amplitude intervals and a common ordinary phase width below 1/4 < pi/12.',
      [(report, '## R5.'), ('data/CERTIFICATE_CHECK.json', 'terminal'), ('scripts/check_certificate.py', 'margin=real')])
claim('N04', 'newly proved/certified', 'The same original trajectory exhibits inherited early turning and subsequently converges to exp(i theta_infinity) r_star, with inherited estimates reindexed from update 50.',
      [(report, '## R6.'), (primary, r'\label{thm:convergence}')],
      'New application enabled by finite entry; the theorem and elementary finite-entry implication are inherited.')
claim('N05', 'newly proved/certified', 'An open neighborhood of the original entrance at the same coefficients has strict early turning and D membership at update 50.',
      [(report, '## R7.'), ('data/CERTIFICATE_CHECK.json', 'early_turn_enclosure')],
      'Qualitative continuity proof only; limiting common phases can differ.')
claim('U01', 'unresolved', 'The exact earliest entry time was not certified.',
      [(report, '## R1.'), (report, '## R8.')])
claim('U02', 'unresolved', 'No explicit radius or box size for the initial-condition neighborhood was computed.',
      [(report, '## R7.')])
claim('X01', 'excluded', 'No global basin, new coefficient regime, replacement seed, parameter scan or all-state convergence claim.',
      [(report, '## R8.')])
claim('X02', 'excluded', 'Convergence does not establish finitely many remaining changes of direction.',
      [(report, '## R8.'), (primary, 'finitely many diminishing directional changes')])
claim('X03', 'excluded', 'No new physical force, position, gravity, magnetism, clock, transport, receiver or geometry-feedback correspondence.',
      [(report, '## R8.')])
write('CLAIM_LEDGER.json', {
    'task': 'NATIVE_TURNING_CAPTURE_01', 'status': 'Investigation completed and returned for scientific review; no external acceptance asserted',
    'counts_are_not_theorem_counts': True, 'claims': claims,
    'administrative_checks_separate_from_claims': ['input/source hashes', 'five invalid-certificate controls', 'execution exit codes', 'review manifest', 'archive reopening audit']})

write('logs/INITIAL_EXECUTIONS.json', {
    'scope': 'Initial scientific preparation/exploration invocations before execute.py was created; tool-observed exit results, not reconstructed automatic logs',
    'shell': 'Windows Command Prompt', 'activation': 'run_python.cmd calls conda.bat activate torment',
    'commands': [
        {'wrapper_invocation': r'run_python.cmd scripts\prepare.py', 'exit_status_observed': 0,
         'stdout': 'Tool output, not separately persisted', 'process_start_utc': None, 'process_finish_utc': None,
         'internal_records': ['logs/ENVIRONMENT.json', 'logs/INPUT_CHECKS.json', 'SOURCE_IDENTITIES.json']},
        {'wrapper_invocation': r'run_python.cmd scripts\explore.py > logs\explore.stdout.txt 2> logs\explore.stderr.txt',
         'exit_status_observed': 0, 'stdout': 'logs/explore.stdout.txt', 'stderr': 'logs/explore.stderr.txt',
         'process_start_utc': None, 'process_finish_utc': None,
         'internal_gate_timestamp': read('logs/PRIOR_GATE.json')['frozen_utc'],
         'internal_completion_timestamp': read('data/EXPLORATION.json')['completed_utc']}],
    'timestamp_note': 'Internal script timestamps are not claimed to be measured shell process start/end times.'})

source_checks = []
for item in read('SOURCE_IDENTITIES.json')['sources']:
    original = Path(item['original_path']).read_bytes()
    preserved = (R / item['path']).read_bytes()
    assert original == preserved and sha(original) == item['sha256'] and len(original) == item['bytes'], item['id']
    source_checks.append({'path': item['path'], 'sha256': item['sha256'], 'original_and_copy_unchanged': True})
packet = R / 'received/NATIVE_TURNING_CAPTURE_01_CODEX_PACKET.zip'
assert sha(packet.read_bytes()) == read('logs/INPUT_CHECKS.json')['packet_sha256']
packet_checks = []
with zipfile.ZipFile(packet) as z:
    assert z.testzip() is None
    for n in z.namelist():
        if n.endswith('/'): continue
        b = z.read(n); assert b == (R / 'packet' / n).read_bytes()
        packet_checks.append({'path': n, 'sha256': sha(b), 'unchanged': True})
received_checks = []
for p in sorted((R / 'received').iterdir()):
    original = Path(r'C:\Users\Notandi\Downloads') / p.name
    assert p.read_bytes() == original.read_bytes()
    received_checks.append({'path': p.relative_to(R).as_posix(), 'sha256': sha(p.read_bytes()), 'download_unchanged': True})
cert = read('data/CERTIFICATE.json'); checked = read('data/CERTIFICATE_CHECK.json'); controls = read('data/CHECKER_NEGATIVE_CONTROLS.json')
assert checked['status'] == controls['status'] == 'PASS'
assert checked['certificate_sha256'] == controls['certificate_sha256'] == sha((R / 'data/CERTIFICATE.json').read_bytes())
assert checked['checker_sha256'] == controls['checker_sha256'] == sha((R / 'scripts/check_certificate.py').read_bytes())
assert cert['generator_sha256'] == sha((R / 'scripts/generate_certificate.py').read_bytes())
assert checked['linked_updates_verified'] == 50 and checked['nonzero_prestages_verified'] == 150
assert len(controls['controls']) == 5 and all(x['rejected'] for x in controls['controls'])
assert read('logs/PRIOR_GATE.json')['frozen_utc'] < read('data/EXPLORATION.json')['completed_utc'] < cert['created_utc'] < checked['checked_utc']
for line in (R / 'logs/EXECUTION_RECORDS.jsonl').read_text().splitlines():
    record = json.loads(line); assert record['exit_status'] == 0
    assert sha(Path(record['command'][2]).read_bytes()) == record['script_sha256']
write('logs/PRESERVATION_AUDIT.json', {
    'status': 'PASS', 'checked_utc': datetime.now(timezone.utc).isoformat(), 'python_optimization_flag': sys.flags.optimize,
    'scope': 'Byte comparisons of the 59 registered read-only originals and their preserved copies, incoming packet and supplied Downloads files; no Git operations',
    'source_count': len(source_checks), 'source_checks': source_checks,
    'packet_member_count': len(packet_checks), 'packet_checks': packet_checks, 'received_checks': received_checks,
    'certificate_checker_generator_hashes_match': True, 'linked_update_count': 50, 'positive_prestage_count': 150,
    'rejected_invalid_certificates': 5, 'source_label_and_report_locators_resolve': True,
    'certificate_was_not_rerun_for_this_packaging_check': True})
print(json.dumps({'status': 'PASS', 'claim_records': len(claims), 'source_files_unchanged': len(source_checks),
                  'packet_members_unchanged': len(packet_checks), 'download_inputs_unchanged': len(received_checks),
                  'scientific_record_hashes_match': True}, indent=2))
