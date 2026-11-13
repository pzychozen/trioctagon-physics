from pathlib import Path
from fractions import Fraction as F
import zipfile,hashlib,json,sys,datetime
ROOT=Path(__file__).resolve().parent.parent
S=ROOT/'submitted'; V=ROOT/'reviewer'; IN=ROOT/'received'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(b):return hashlib.sha256(b).hexdigest()
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
checks={}
def check(name,test,detail=None):
 assert test,name
 checks[name]={'passed':True,'detail':detail}
p=IN/'NATIVE_ALTERNATING_BRANCH_CONNECTION_01_REVIEW.zip';b=p.read_bytes()
audit=read(IN/'NATIVE_ALTERNATING_BRANCH_CONNECTION_01_FINAL_DELIVERY_AUDIT.json')
check('archive_hash',sha(b)==audit['archive_sha256']==(IN/(p.name+'.sha256')).read_text().split()[0],sha(b))
with zipfile.ZipFile(p) as z:
 names=z.namelist()
 check('safe_unique_names',len(names)==len(set(names)) and all(not Path(n).is_absolute() and '..' not in Path(n).parts and '\\' not in n for n in names))
 check('archive_crc',z.testzip() is None)
 check('149_archive_members',len(names)==149)
 for n in names:check('member_bytes:'+n,z.read(n)==(S/n).read_bytes())
manifest=read(S/'REVIEW_MANIFEST.json')
check('manifest_set',set(names)==set(x['path'] for x in manifest['files'])|{'REVIEW_MANIFEST.json'})
for r in manifest['files']:
 b=(S/r['path']).read_bytes();check('manifest:'+r['path'],len(b)==r['bytes'] and sha(b)==r['sha256'])
check('external_audit_set',set(names)==set(x['path'] for x in audit['members']))
for r in audit['members']:
 b=(S/r['path']).read_bytes();check('external_audit:'+r['path'],len(b)==r['bytes'] and sha(b)==r['sha256'])
for r in read(S/'SOURCE_INVENTORY.json')['files']:
 b=(S/r['path']).read_bytes();check('source_inventory:'+r['path'],len(b)==r['bytes'] and sha(b)==r['sha256'])
for r in read(S/'packet/SOURCE_IDENTITIES.json')['sources']:
 b=(S/'packet'/r['packet_path']).read_bytes();check('source_registry:'+r['packet_path'],len(b)==r['bytes'] and sha(b)==r['sha256'])
 if r.get('git_blob'):check('source_blob:'+r['packet_path'],blob(b)==r['git_blob'])
for r in read(S/'logs/INPUT_IDENTITIES.json')['files']:
 b=(S/r['copied_path']).read_bytes();check('copied_source:'+r['copied_path'],len(b)==r['bytes'] and sha(b)==r['sha256'])
 if r.get('git_blob'):check('copied_blob:'+r['copied_path'],blob(b)==r['git_blob'])
orig=S/'received/NATIVE_ALTERNATING_BRANCH_CONNECTION_01_CODEX_PACKET.zip'
check('original_packet_hash',sha(orig.read_bytes())==read(S/'logs/INPUT_IDENTITIES.json')['packet_sha256'])
with zipfile.ZipFile(orig) as z:
 for n in z.namelist():check('original_packet_member:'+n,z.read(n)==(S/'packet'/n).read_bytes())
 original_packet_members=len(z.namelist())
for local,internal in [('PROOF_REPORT.md','PROOF_REPORT.md'),('RESULT_SUMMARY(4).md','RESULT_SUMMARY.md')]:
 check('standalone:'+local,(IN/local).read_bytes()==(S/internal).read_bytes())
# Source-independent exact comparisons of reported quantitative margins.
c=read(S/'data/CONNECTION_CERTIFICATE.json');patches=c['patches'];joins=c['joins']
pq=max(F(x) for row in patches for x in row['weighted_row_bounds']);jq=max(F(x) for row in joins for x in row['weighted_row_bounds'])
check('patch_bound',pq<F('0.614'),str(pq));check('join_bound',jq<F('0.583'),str(jq))
check('closed_cover',len(patches)==128 and all(list(map(F,p['mu']))==[F(i,25600),F(i+1,25600)] for i,p in enumerate(patches)))
mins={
 'slice':min(F(row['regularity']['slice'][0]) for row in patches),
 'prestage_real':min(F(v[0]) for row in patches for v in row['regularity']['prestage_reals']),
 'gauge_modulus':min(F(row['regularity']['gauge_modulus'][0]) for row in patches),
 'nu':min(F(row['regularity']['nu'][0]) for row in patches),
}
for k,q in {'slice':'8.884','prestage_real':'1.504','gauge_modulus':'8.882','nu':'0.02209'}.items():check('coarse_'+k,mins[k]>F(q),str(mins[k]))
maxkick=max(max(abs(F(v)) for v in w) for row in patches for w in row['regularity']['squared_kicks'])
check('squared_kick_bound',maxkick<F('0.0823'),str(maxkick))
end=c['endpoint'];margins=[min(F(z[0])-F(u[0]),F(u[1])-F(z[1])) for z,u in zip(end['quotient_enclosure'],end['Up'])]
check('endpoint_clearance',min(margins)>F('0.00001098'),[str(x) for x in margins])
strip=read(S/'data/ENDPOINT_STABILITY_STRIP.json')
check('strip_stability_bound',F(strip['stability']['norm_upper'])<F('0.9601'),strip['stability']['norm_upper'])
check('broad_stability_not_proved',len(read(S/'data/STABILITY_CERTIFICATE.json')['rows'])==128 and all(not r['certified_attracting'] for r in read(S/'data/STABILITY_CERTIFICATE.json')['rows']))
# Replays must be identical in stable scientific fields, not timestamps/durations.
for f in ['CERTIFICATE_CHECK.json','ALGEBRA_AND_SOURCE_CHECKS.json']:
 before=read(S/'data'/f);after=read(ROOT/'replay_work/data'/f)
 for o in (before,after):
  for k in ['checked_utc','elapsed_seconds']:o.pop(k,None)
 check('stable_replay:'+f,before==after)
# All submitted bytes still preserved after the replay.
for r in manifest['files']:assert sha((S/r['path']).read_bytes())==r['sha256']
summary={'status':'PASS','date':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'archive_members':len(names),'manifest_entries':len(manifest['files']),'external_audit_entries':len(audit['members']),
 'source_inventory_entries':len(read(S/'SOURCE_INVENTORY.json')['files']),
 'packet_source_entries':len(read(S/'packet/SOURCE_IDENTITIES.json')['sources']),
 'copied_source_identity_entries':len(read(S/'logs/INPUT_IDENTITIES.json')['files']),
 'original_packet_members':original_packet_members,'ledger_records':len(read(S/'CLAIM_LEDGER.json')['records']),
 'patches':128,'uniqueness_joins':127,'quantitative_display':{'patch_max':float(pq),'join_max':float(jq),'minimum_endpoint_clearance':float(min(margins)),'stability_norm_bound':float(F(strip['stability']['norm_upper']))},
 'stable_replays_match':True,'submitted_bytes_unchanged':True,'checks':checks,
 'scope':'File identities and exact certificate-report comparisons; independent reviewer organization. Not a new interval engine, old theorem replay, remote audit or repository operation.'}
(V/'SUBMISSION_AUDIT.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='checks'},indent=2))
