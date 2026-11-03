"""Document/source/package checks only; no scientific computation or Git."""
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlsplit, unquote
import hashlib, json, re, zipfile

W=Path(__file__).resolve().parent
PROOF='NATIVE_SAME_TRAJECTORY_RETURN_01_PROOF.md'
LEDGER='NATIVE_SAME_TRAJECTORY_RETURN_01_CLAIM_SOURCE_LEDGER.md'
ARCHIVE='NATIVE_SAME_TRAJECTORY_RETURN_01_REVIEW_PACKAGE.zip'
def ident(p):
    b=p.read_bytes();return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def dump(name,data):(W/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def read(name):return json.loads((W/name).read_text(encoding='utf-8'))
assert not (W/ARCHIVE).exists(),'Do not overwrite a review package'
registry=read('SOURCE_IDENTITIES.json')
preserved=[]
for row in registry['sources']:
    expected={k:row[k] for k in ('bytes','sha256')}
    original=ident(Path(row['path']));copy=ident(W/row['retained_as'])
    assert original==copy==expected,row['id']
    preserved.append({'path':row['path'],'retained_as':row['retained_as'],**expected,'original_unchanged':True,'copy_matches':True})
for role,row in registry['context'].items():
    expected={k:row[k] for k in ('bytes','sha256')}
    assert ident(Path(row['path']))==ident(W/row['retained_as'])==expected,role
    preserved.append({'path':row['path'],'retained_as':row['retained_as'],**expected,'original_unchanged':True,'copy_matches':True})
dump('PRESERVATION_CHECK.json',{'checked_utc':datetime.now(timezone.utc).isoformat(),'pass':True,
    'scope':'Only the seven used defining files and two supplied order/context files; exact originals and retained-copy identities. No repository-wide audit or Git operations.',
    'files':preserved,'count':len(preserved)})

proof=(W/PROOF).read_text(encoding='utf-8');ledger=(W/LEDGER).read_text(encoding='utf-8')
labels=re.findall(r'\\tag\{(R\d+)\}',proof)
assert labels==['R'+str(i) for i in range(1,31)],labels
references=re.findall(r'\((R\d+)\)',proof)
assert set(references)<=set(labels)
claims=re.findall(r'^\| (STR\d+) \|',ledger,re.M)
assert claims==['STR'+str(i).zfill(2) for i in range(1,29)]
checks=read('EXACT_CERTIFICATE_RESULTS.json')
assert checks['all_passed'] and checks['total']==checks['passed']==len(checks['checks'])==25
assert checks['helper_sha256']==ident(W/'exact_certificate_checks.py')['sha256']
assert [r['id'] for r in checks['checks']]==['S'+str(i).zfill(2) for i in range(1,26)]
assert all(r['pass'] for r in checks['checks'])
assert not checks['historical_checks_reexecuted']
assert not any(ord(c)<32 and c not in '\r\n\t' for c in proof+ledger)
assert '\ufffd' not in proof+ledger and '\\$' not in proof

# Check delimiters, environment nesting and braces in every authored math span.
display=False;buffer=[];math_spans=[]
for line in proof.splitlines():
    if line.strip()==r'\[':
        assert not display;display=True;buffer=[];continue
    if line.strip()==r'\]':
        assert display;display=False;math_spans.append('\n'.join(buffer));continue
    if display:buffer.append(line);continue
    assert line.count('$')%2==0,line
    parts=line.split('$')
    math_spans.extend(parts[1::2])
    prose=''.join(parts[::2])
    assert not re.search(r'\\[a-zA-Z]',prose),line
assert not display
for expression in math_spans:
    depth=0
    for i,char in enumerate(expression):
        if i>0 and expression[i-1]=='\\':continue
        if char=='{':depth+=1
        elif char=='}':depth-=1;assert depth>=0,expression
    assert depth==0,expression
    stack=[]
    for action,name in re.findall(r'\\(begin|end)\{([^}]+)\}',expression):
        if action=='begin':stack.append(name)
        else:assert stack.pop()==name,expression
    assert not stack,expression

links=[]
for name in [PROOF,LEDGER,'README.md','EXECUTION_RECORD.md']:
    text=(W/name).read_text(encoding='utf-8')
    for link in re.findall(r'\]\(([^)]+)\)',text):
        parsed=urlsplit(link)
        if parsed.scheme:continue
        p=(W/unquote(parsed.path)).resolve()
        assert p.is_relative_to(W.resolve())
        assert p.exists() or p.name=='REVIEW_CHECKS.json',link
        links.append({'from':name,'to':link})
dump('DOCUMENT_CHECKS.json',{'checked_utc':datetime.now(timezone.utc).isoformat(),'pass':True,
    'proof':ident(W/PROOF),'ledger':ident(W/LEDGER),'equation_tags':labels,'claim_ids':claims,
    'equation_references_resolve':True,'math_delimiters_braces_environments_pass':True,'math_spans_checked':len(math_spans),
    'portable_relative_links':links,'exact_helper_binding_pass':True,
    'scope':'Markdown/source-consistency checks, not a new mathematical proof or PDF inspection.'})

gates=[
 ('Fixed baseline','R1-R4 retain the seven hash-pinned definitions; finite constant parameters, empty launch, no native jumps.'),
 ('Quantifiers','Other parameters and one nonzero phi fixed first; one finite computable sufficient threshold; every fixed finite kappa above it.'),
 ('Nonzero preparation','R10-R13 give the correct K norm, yaw-dependent drive, nonzero two-port vector, operator norms and ball bounds.'),
 ('Regularity','R9 invokes the published global strong theorem for empty H1 preparation; error is actual-minus-explicit strong fields.'),
 ('Forced energy','R16-R19 retain receiver loading in the weighted skew block, use periodic H1 products and regularize the norm at zero.'),
 ('Core drift','R20 has the exact one-fourth coefficient, a convex-ball Lipschitz estimate and no coherent-domain invariance assumption.'),
 ('Residual','R23 has negative propagation residual in the r component only; first weak derivative in L2 is sufficient.'),
 ('Finite comparison','R24-R25 integrate absolute sine to 3/omega, retaining both drift and propagation errors; no operator-norm limit.'),
 ('Total power','R26-R27 retain the exact y in the first term and bound the complete signed two-port sum with C1 and C2.'),
 ('Threshold and interval','R5-R7 and section 5 preserve the D/2 witness and D/4 neighborhood margin, positive interval gain and chronology.'),
 ('Initial activity','R28 uses the published fixed-finite-coupling asymptotics, including positive exact receiver power/storage; no uniform remainder assumed.'),
 ('Units','Section 6 checks A, norm and power units and both dimensionless threshold ratios; no physical calibration.'),
 ('Meaning','R8 and R30 keep cumulative debit nonnegative and capacity qualified; comparison receiver backflow is not asserted as an exact witness sign.'),
 ('Scope','Fast collocated exchange, small storage window, geometry distinctions and absent physical circuit retained; no second regime investigated.'),
 ('Provenance','Seven defining sources match; standalone context report of later old-paper review distinguished from absent review text; new GPT review pending.')
]
dump('REVIEW_CHECKS.json',{'reviewed_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'Codex','status':'PASS',
    'disposition':'Established within the unchanged candidate for the explicit sufficient finite-coupling regime; proposed constants unchanged.',
    'proof':ident(W/PROOF),'ledger':ident(W/LEDGER),'source_identity_record':ident(W/'SOURCE_IDENTITIES.json'),
    'supporting_exact_results':ident(W/'EXACT_CERTIFICATE_RESULTS.json'),
    'gates':[{'gate':name,'finding':finding,'pass':True} for name,finding in gates],
    'review_scope':'Manual analytical/source review by Codex plus separate document checks, not GPT acceptance or external peer review.'})

names=[PROOF,LEDGER,'README.md','EXECUTION_RECORD.md','SUPPLIED_WORK_ORDER.md','START_HERE_CONTEXT.md',
    'SOURCE_IDENTITIES.json','ENVIRONMENT.json','AGENTS_CHECK.json','PRESERVATION_CHECK.json',
    'EXACT_CERTIFICATE_RESULTS.json','exact_certificate_checks.py','prepare_sources.py','finish_report.py',
    'EDITORIAL_FORMATTING.json','DOCUMENT_CHECKS.json','REVIEW_CHECKS.json','package_review.py']
names.extend(row['retained_as'] for row in registry['sources'])
assert len(names)==len(set(names))
members={name:W/name for name in sorted(names)}
assert all(p.is_file() for p in members.values())
manifest={'created_utc':datetime.now(timezone.utc).isoformat(),'scope':'One bounded same-trajectory return investigation review package.',
    'self_exclusion':'MEMBER_MANIFEST.json is included but excludes its own hash. ZIP checksum and final PACKAGE_VERIFICATION.json are external to avoid circular identities.',
    'payloads':{name:ident(p) for name,p in members.items()}}
dump('MEMBER_MANIFEST.json',manifest)
members['MEMBER_MANIFEST.json']=W/'MEMBER_MANIFEST.json'
archive=W/ARCHIVE
with zipfile.ZipFile(archive,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for name,p in sorted(members.items()):
        info=zipfile.ZipInfo(name,date_time=(2026,11,3,0,0,0))
        info.compress_type=zipfile.ZIP_DEFLATED;info.create_system=3;info.external_attr=0o100644<<16
        z.writestr(info,p.read_bytes(),compresslevel=9)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert sorted(z.namelist())==sorted(members)
    for name,expected in manifest['payloads'].items():
        data=z.read(name)
        assert {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}==expected
        assert data==members[name].read_bytes()
    assert z.read('MEMBER_MANIFEST.json')==(W/'MEMBER_MANIFEST.json').read_bytes()
archive_id=ident(archive)
(W/(ARCHIVE+'.sha256')).write_text(archive_id['sha256']+'  '+ARCHIVE+'\n',encoding='utf-8')
assert (W/(ARCHIVE+'.sha256')).read_text().split()[0]==ident(archive)['sha256']
for row in preserved:assert ident(Path(row['path']))=={k:row[k] for k in ('bytes','sha256')}
result={'verified_utc':datetime.now(timezone.utc).isoformat(),'archive':str(archive),**archive_id,
    'members_including_manifest':len(members),'hashed_payloads':len(manifest['payloads']),
    'exact_member_set_crc_sizes_sha256_pass':True,'archive_checksum_pass':True,
    'source_preservation_pass':True,'defining_sources':len(registry['sources']),'new_exact_checks':25,
    'document_checks_pass':True,'analytical_review':'Codex PASS; subsequent GPT/author review pending',
    'git_operations':False,'publication_performed':False}
dump('PACKAGE_VERIFICATION.json',result)
print(json.dumps(result,indent=2))
