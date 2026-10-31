"""Current manuscript evidence reconciliation. ZERO science executions."""
import collections,hashlib,json,pathlib,zipfile
ROOT=pathlib.Path(__file__).resolve().parent
P=ROOT/'packet/NCM_PAPER_01_Codex_Packet_v0.1'
def fp(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def save(n,o):(ROOT/n).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
manifest=json.loads((P/'MANIFEST.json').read_text());rows=manifest['members']
if isinstance(rows,dict):rows=[{'path':k,**v} for k,v in rows.items()]
for row in rows:
 d=fp((P/row['path']).read_bytes());assert d=={k:row[k] for k in ('bytes','sha256')},row['path']
assert (P/'WORK_ORDER.txt').read_bytes()==next((ROOT/'inputs').glob('*.txt')).read_bytes()
lineage=json.loads((P/'CONTEXT_LINEAGE.json').read_text())
for row in lineage['files']:
 assert fp((P/row['packet_path']).read_bytes())=={k:row[k] for k in ('bytes','sha256')}
 if row['kind']=='exact_archive_member_copy' and (P/'evidence'/row['source_archive']).exists():
  with zipfile.ZipFile(P/'evidence'/row['source_archive']) as z:assert z.read(row['source_member'])==(P/row['packet_path']).read_bytes()
prior=json.loads((P/'context/NCM_DUAL_02_SOURCE_MANIFEST.json').read_text())
before=json.loads((ROOT/'SOURCE_MANIFEST.before.json').read_text())
comparisons={}
for key in ('DYNAMICS','OBSERVABLES','COHERENT','D1','Z','M3','BRIDGE'):
 comparisons[key]={'current':before['sources'][key]['sha256'],'prior':prior['files'][key]['after']['sha256']}
 comparisons[key]['match']=comparisons[key]['current']==comparisons[key]['prior']
 assert comparisons[key]['match'],key
summary=json.loads((P/'context/NCM_DUAL_03_discovery_summary.json').read_text())
ledger=[json.loads(line) for line in (P/'context/NCM_DUAL_03_attempt_ledger.jsonl').read_text().splitlines()]
assert ledger==summary['attempts']
analysis=json.loads((P/'context/NCM_DUAL_03_analysis_results.json').read_text())
counts=dict(collections.Counter(x['classification'] for x in ledger))
assert counts==analysis['classification_counts']=={'solver_failed':18,'lower_period_one_numerical':42}
assert sum(x['F_attempts'] for x in ledger)==8211
details={};groups=None
with zipfile.ZipFile(P/'evidence/NCM_DUAL_03_v0.1_REVIEW.zip') as z:
 frozen=json.loads(z.read('phase_b/PLAN_FREEZE.json'))
 for name,digest in frozen['sha256'].items():assert hashlib.sha256(z.read('phase_b/'+name)).hexdigest()==digest
 for small in ledger:
  raw=z.read('phase_b/attempts/'+small['id']+'.json');r=json.loads(raw)
  assert r['classification']==small['classification'] and r['F_attempts']==small['F_attempts']
  assert len(r['iterations'])==small['iterations']
  details[r['id']]={'source_member':'phase_b/attempts/'+r['id']+'.json','member_sha256':fp(raw)['sha256'],
    'classification':r['classification'],'stop_reason':r['stop_reason'],'metrics':r['metrics']}
 groups=json.loads(z.read('phase_b/numerical_groups.json'))
 save('evidence/RETAINED_GROUPS_EXTRACT.json',groups)
save('evidence/RETAINED_ATTEMPT_METRICS.json',details)
save('evidence/RECONCILIATION.json',{'packet_manifest_members_verified':len(rows),'source_comparisons':comparisons,
 'sixty_attempts_read_as_json_only':60,'outcomes':counts,'historical_discovery_F_attempts':8211,
 'historical_independent_F_attempts':151,'historical_completed':8361,'current_native_F_evaluations':0,
 'old_script_solver_checker_executions':0,'source_conflicts':[]})
print(json.dumps({'packet_members_verified':len(rows),'scientific_sources_match':len(comparisons),'attempts_reconciled':60,'groups':len(groups['groups']),'current_native_calls':0},indent=2))
