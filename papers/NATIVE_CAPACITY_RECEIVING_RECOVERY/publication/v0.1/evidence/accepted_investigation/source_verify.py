"""Independent source/locator reconciliation; no network, Git or scientific replay."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,sys,zipfile
W=Path(__file__).resolve().parent;I=W/"inputs"
def sha(b):return hashlib.sha256(b).hexdigest()
def ident(p):
    b=p.read_bytes();return {"bytes":len(b),"sha256":sha(b)}
def load(p):return json.loads(p.read_text(encoding="utf-8"))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
run=subprocess.run([sys.executable,"-I","-B",str(I/"verify_packet.py")],capture_output=True,check=True)
(W/"SUPPLIED_PACKET_VERIFICATION.json").write_bytes(run.stdout)
registry=load(I/"provenance/SELECTED_SOURCE_IDENTITIES.json")
manifest=load(I/"provenance/P4_PUBLICATION_MANIFEST.json")
remote=load(I/"provenance/P4_REMOTE_BYTE_COMPARISON.json")
mp={r["path"]:r for r in manifest["files"]}
rp={r["path"]:r for r in remote["files"]}
prefix="papers/NATIVE_FINITE_CAPACITY_ACCESS/publication/v0.1/"
prior=W.parent/"NATIVE_FINITE_CAPACITY_ACCESS_PUBLISH_01/output/NATIVE_FINITE_CAPACITY_ACCESS_FIX_PUBLISH_01_CLOSEOUT.zip"
assert sha(prior.read_bytes())==registry["source_archive_sha256"]
baseline=load(W/"INPUT_BASELINE.json")
if str(prior) in baseline["files"]:
    assert baseline["files"][str(prior)]==ident(prior)
else:
    baseline["files"][str(prior)]=ident(prior)
    baseline["scope"]+=" One separately retained prior publication closeout ZIP used for exact independent source-byte comparison."
save(W/"INPUT_BASELINE.json",baseline)
checked=[];mcount=rcount=archivecount=0
with zipfile.ZipFile(prior) as z:
    assert z.testzip() is None
    for r in registry["source_records"]:
        p=I/r["packet_path"];actual=ident(p)
        assert actual=={k:r[k] for k in ["bytes","sha256"]}
        item={**r,"actual":actual,"checks":["supplied registry hash and size"]}
        carried=r.get("carried_repository_path")
        if carried:
            assert carried.startswith(prefix)
            rel=carried[len(prefix):]
            if rel!="PUBLICATION_MANIFEST.json":
                assert {k:mp[rel][k] for k in ["bytes","sha256"]}==actual
                mcount+=1;item["checks"].append("retained P4 publication manifest")
            else:
                item["checks"].append("publication manifest self-exclusion respected")
            assert {k:rp[carried][k] for k in ["bytes","sha256"]}==actual
            rcount+=1;item["checks"].append("retained P4 remote-byte record")
        member=r.get("extracted_archive_member")
        if member and member in z.namelist():
            assert z.read(member)==p.read_bytes(),r["packet_path"]
            archivecount+=1;item["checks"].append("exact bytes in separately retained original publication closeout")
        checked.append(item)
    pdf=z.read("published_payload/"+prefix+"NATIVE_FINITE_CAPACITY_ACCESS_v0.1.pdf")
    assert len(pdf)==110500 and sha(pdf)=="e337a9b59488b7f1dc4ac1371150e7b5d69d168d7b230dcd665ccb61bade1318"
assert ident(I/"accepted/NATIVE_FINITE_CAPACITY_ACCESS_01_PROOF.md")["sha256"]=="05d962af8be00377212c96c63a2ae498e57b4912192dfad87e705b4aadd56cb7"
requested={
 "P1/manuscript/candidate.tex":["eq:registration","eq:drive","eq:tents","eq:ports","eq:storages","eq:system","tab:units"],
 "P1/manuscript/power.tex":["eq:jacobian","eq:core","eq:powers","eq:balances","eq:integrated"],
 "P1/manuscript/wellposed.tex":["thm:global","eq:strong","eq:profilenorms","eq:lipschitzbounds"],
 "P2/manuscript/theorem.tex":["thm:credit"],
 "P2/manuscript/comparison.tex":["eq:error","eq:finiteerror"],
 "P3/manuscript/projection.tex":["thm:projection","eq:kernel","eq:joint","eq:emptystock","eq:strictwitness"],
 "P3/manuscript/transfer.tex":["eq:constants","eq:cert","eq:ratiobounds","thm:transfer"],
 "P4/manuscript/theorem.tex":["eq:rates","eq:condition","thm:access","eq:certificate"],
 "P4/manuscript/proof.tex":["eq:regularity","eq:forced","eq:regularized","eq:reference","eq:residual"],
 "P4/manuscript/units.tex":["tab:units","eq:unitchecks"],
 "P4/manuscript/interpretation.tex":["eq:initialfraction","sec:priorlimits"]}
labels=[]
for rel,keys in requested.items():
    text=(I/"sources"/rel).read_text(encoding="utf-8")
    recfile=I/"sources"/rel.split("/")[0]/"verification/LABELS.json"
    rec=load(recfile) if recfile.exists() else {}
    for key in keys:
        assert "\\label{"+key+"}" in text,(rel,key)
        row={"source":"sources/"+rel,"label":key}
        if key in rec:row["printed_record"]=rec[key]
        labels.append(row)
save(W/"SOURCE_IDENTITIES.json",{"utc":datetime.now(timezone.utc).isoformat(),"status":"PASS",
 "scope":"64 exact selected-source entries, matched to supplied records and, where available, independently retained prior closeout bytes. No live remote request or Git operation.",
 "source_archive":ident(prior),"records":checked,"manifest_reconciled":mcount,"retained_remote_reconciled":rcount,
 "independent_prior_archive_byte_matches":archivecount,"source_label_checks":labels,
 "P4_PDF_identity_checked_as_archive_bytes":{"bytes":len(pdf),"sha256":sha(pdf),"rendered_or_inspected":False},
 "new_scientific_status":"Proposed result requires independent proof; source identity is not proof."})
print(json.dumps({"source_entries":len(checked),"manifest_matches":mcount,"retained_remote_matches":rcount,
 "prior_archive_exact_matches":archivecount,"verified_source_labels":len(labels),"protected_inputs":len(baseline["files"])},indent=2))
for row in labels:
    if row.get("printed_record"):print(json.dumps(row,ensure_ascii=False))
