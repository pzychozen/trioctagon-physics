"""Bounded document/source verification and nonrecursive investigation delivery.

No Git, network, scientific replay, source edits, installations or trajectory
calculations. Run without arguments for document checks, then with --package
to create the final archive and its external post-write verification receipt.
"""
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
import argparse, ast, hashlib, json, re, sys, zipfile

W=Path(__file__).resolve().parent
I=W/"inputs"
TASK="NATIVE_CAPACITY_RECEIVING_RECOVERY_01"
PROOF=TASK+"_PROOF.md"
LEDGER=TASK+"_CLAIM_SOURCE_LEDGER.md"
def utc(): return datetime.now(timezone.utc).isoformat()
def sha(b): return hashlib.sha256(b).hexdigest()
def ident(p):
    b=p.read_bytes()
    return {"bytes":len(b),"sha256":sha(b)}
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def save(p,obj):
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

ap=argparse.ArgumentParser()
ap.add_argument("--package",action="store_true")
args=ap.parse_args()
assert sys.flags.isolated and sys.dont_write_bytecode

# Compare each explicitly inventoried input. No inference about unrelated files.
baseline=load(W/"INPUT_BASELINE.json")
assert len(baseline["files"])==82
preserved=[]
for name,before in baseline["files"].items():
    after=ident(Path(name))
    assert before==after,name
    preserved.append({"path":name,"before":before,"after":after,"status":"PASS"})
input_files=sorted(p for p in I.rglob("*") if p.is_file())
assert len(input_files)==77
assert all(str(p) in baseline["files"] for p in input_files)
input_manifest=load(I/"PACKET_MANIFEST.json")
assert {r["path"] for r in input_manifest["files"]}|{"PACKET_MANIFEST.json"}=={
    p.relative_to(I).as_posix() for p in input_files}
for r in input_manifest["files"]:
    assert ident(I/r["path"])=={k:r[k] for k in ("bytes","sha256")}
save(W/"INPUT_PRESERVATION.json",{
    "utc":utc(),"status":"PASS","baseline":ident(W/"INPUT_BASELINE.json"),
    "scope":baseline["scope"],"inventoried_files":82,
    "composition":{"Downloads_inputs":4,"extracted_members":77,"prior_closeout_archive":1},
    "all_before_after_equal":True,"files":preserved,
    "limit":"Explicitly inventoried inputs only; no machine-wide or unrelated repository audit."})

proof=(W/PROOF).read_text(encoding="utf-8")
ledger=(W/LEDGER).read_text(encoding="utf-8")
tags=re.findall(r"\\tag\{(RR\d\d)\}",proof)
assert tags==[f"RR{i:02}" for i in range(1,37)]
assert set(re.findall(r"\bRR\d\d\b",proof+ledger))<=set(tags)
ledger_pr=re.findall(r"^\| (PR\d\d) \|",ledger,re.M)
assert ledger_pr==[f"PR{i:02}" for i in range(1,24)]
for name in (PROOF,LEDGER,"COMPLETION_REPORT.md","READ_ME_REVIEW.md"):
    txt=(W/name).read_text(encoding="utf-8")
    assert "\ufffd" not in txt and "\x00" not in txt
    assert txt.count(r"\[")==txt.count(r"\]"),name
    assert txt.count(r"\(")==txt.count(r"\)"),name
    assert not re.search(r"\b(?:TODO|TBD|FIXME)\b",txt),name
for name in ("prepare_inputs.py","source_verify.py","exact_checks.py","audit_and_package.py"):
    ast.parse((W/name).read_text(encoding="utf-8"),filename=name)

results=load(W/"EXACT_ALGEBRA_RESULTS.json")
execution=load(W/"EXACT_CHECK_EXECUTION.json")
ec=[f"EC{i:02}" for i in range(1,15)]
assert [r["id"] for r in results["groups"]]==ec
assert results["status"]==execution["status"]=="PASS"
assert all(r["status"]=="PASS" for r in results["groups"])
assert execution["check_groups"]==results["independent_check_groups"]==14
assert execution["script_sha256"]==results["script_sha256"]==ident(W/"exact_checks.py")["sha256"]
assert execution["results_sha256"]==ident(W/"EXACT_ALGEBRA_RESULTS.json")["sha256"]
assert execution["isolated_mode"]==1 and execution["dont_write_bytecode"]
assert execution["sympy_version"]=="1.14.0"
assert not execution["preparatory_or_historical_scientific_code_executed"]

source=load(W/"SOURCE_IDENTITIES.json")
assert source["status"]=="PASS" and len(source["records"])==64
assert source["manifest_reconciled"]==60
assert source["retained_remote_reconciled"]==source["independent_prior_archive_byte_matches"]==61
for r in source["records"]:
    assert ident(I/r["packet_path"])==r["actual"]=={k:r[k] for k in ("bytes","sha256")}
labels=source["source_label_checks"]
assert len(labels)==41
source_groups=[]
for label in labels:
    path=I/label["source"]
    assert "\\label{"+label["label"]+"}" in path.read_text(encoding="utf-8")
    if label.get("printed_record"):
        paper=label["source"].split("/")[1]
        rec=load(I/"sources"/paper/"verification/LABELS.json")
        assert rec[label["label"]]==label["printed_record"]
    if not source_groups or source_groups[-1]["path"]!=label["source"]:
        source_groups.append({"id":f"S{len(source_groups)+1:02}",
                              "path":label["source"],"identity":ident(path),"labels":[]})
    source_groups[-1]["labels"].append({k:v for k,v in label.items() if k!="source"})
assert len(source_groups)==11
for group in source_groups:
    assert re.search(r"^\| "+group["id"]+r" \|",ledger,re.M)
    assert group["path"].removeprefix("sources/") in ledger
    assert all(label["label"] in ledger for label in group["labels"])

# Explicit proof/evidence mapping, in the same order as the human ledger.
mapping=[
 ("PR01",["RR09"],["EC01"],["S03","S07","S08"]),
 ("PR02",["RR04","RR34"],["EC13"],["S01","S08"]),
 ("PR03",["RR04","RR17","RR23","RR24"],["EC05","EC09","EC10"],["S06","S08"]),
 ("PR04",["RR04","RR10","RR24"],["EC02","EC10"],["S01","S08"]),
 ("PR05",["RR05","RR29","RR30"],["EC11"],["S01","S02","S03"]),
 ("PR06",["RR31"],["EC01"],["S08"]),
 ("PR07",["RR10"],["EC02"],["S01","S06"]),
 ("PR08",["RR11","RR12","RR13"],["EC04"],["S01","S02"]),
 ("PR09",["RR12","RR13","RR14"],["EC04"],["S02","S03","S09"]),
 ("PR10",["RR15"],["EC03"],["S01","S02"]),
 ("PR11",["RR16"],["EC04"],["S03"]),
 ("PR12",["RR17"],["EC05"],["S06"]),
 ("PR13",["RR18","RR24"],["EC08"],["S03","S09"]),
 ("PR14",["RR19","RR20"],["EC05","EC06","EC07"],["S01","S02","S03"]),
 ("PR15",["RR21"],["EC06"],[]),
 ("PR16",["RR22"],["EC05","EC06","EC11"],[]),
 ("PR17",["RR25"],["EC07"],["S03","S05","S09"]),
 ("PR18",["RR26","RR27"],["EC07","EC08"],[]),
 ("PR19",["RR23","RR24"],["EC09","EC10"],[]),
 ("PR20",["RR28"],["EC10"],[]),
 ("PR21",["RR29","RR30","RR31","RR32"],["EC11","EC12"],["S02"]),
 ("PR22",["RR33"],["EC12"],["S02","S08"]),
 ("PR23",["RR34","RR35","RR36"],["EC13","EC14"],["S01","S10"])]
assert [r[0] for r in mapping]==ledger_pr
for pr,rr,checks,sources in mapping:
    assert set(rr)<=set(tags) and set(checks)<=set(ec)
    assert set(sources)<={g["id"] for g in source_groups}
assert set().union(*(set(x[2]) for x in mapping))==set(ec)

obligations={
 "known_global_strong_solution":"Proof section 2; P1 thm:global and eq:strong",
 "periodic_first_derivative":"Proof section 1 and RR02; no H2 tent assumption",
 "zero_norm_regularization":"Proof section 4, immediately before RR14",
 "scalar_positive_denominator":"Proof section 5 and section 7.1, RR18/RR24",
 "exact_negative_initial_mode_and_static_components":"Proof section 6, RR19/RR20",
 "strong_difference_before_residual":"Proof section 7.2, RR25",
 "receiver_retained_and_only_first_derivative":"Proof section 7.2, RR25/RR26",
 "phase_uniform_fixed_coefficients":"Proof sections 1, 7.3 and 9",
 "positive_reverse_triangle_before_squaring":"Proof section 8, RR29/RR30",
 "all_positive_ratio_denominators":"Proof section 8, before RR32",
 "upper_recovery_bound_one":"Proof section 8, after RR33",
 "sign_intervals_not_simultaneity":"Proof section 8 final paragraph",
 "amplitude_units_and_Astar_over_R":"Proof section 10, RR35/RR36",
 "small_absolute_capacity_and_geometry_limits":"Proof section 11"}
bindings={name:ident(W/name) for name in
          (PROOF,LEDGER,"exact_checks.py","EXACT_ALGEBRA_RESULTS.json",
           "EXACT_CHECK_EXECUTION.json","SOURCE_IDENTITIES.json")}
save(W/"CLAIM_CROSSWALK.json",{
    "utc":utc(),"status":"PASS","bindings":bindings,
    "proof_displayed_locators":tags,"inherited_groups":source_groups,
    "proposal_groups":[{"proposal":pr,"proof_locators":rr,"exact_check_groups":checks,
                       "inherited_source_groups":sources,"status":"established at ledger's stated scope"}
                      for pr,rr,checks,sources in mapping],
    "written_analytical_obligations":obligations,
    "limits":"The mapping establishes coverage and artifact identity, not mathematical truth by itself."})
save(W/"DOCUMENT_CHECKS.json",{
    "utc":utc(),"status":"PASS",
    "bindings":{name:ident(W/name) for name in
       (PROOF,LEDGER,"COMPLETION_REPORT.md","READ_ME_REVIEW.md","CLAIM_CROSSWALK.json",
        "INPUT_PRESERVATION.json","audit_and_package.py")},
    "proof_displayed_groups":36,"proposal_ledger_rows":23,"inherited_source_groups":11,
    "source_label_bindings":41,"independent_algebra_groups":14,"inventoried_inputs_unchanged":82,
    "checks":{"displayed_tags_unique_and_complete":True,"proof_references_resolve":True,
       "all_PR01_to_PR23_rows_present":True,"all_exact_check_groups_mapped":True,
       "source_labels_and_supplied_printed_records_match":True,
       "UTF8_and_math_delimiters":True,"no_draft_placeholders":True,
       "Python_scripts_parse_without_execution":True,"execution_script_and_result_hashes_match":True,
       "incoming_manifest_remains_exhaustive":True},
    "manual_analytical_review_record":{
       "status":"Assessed in the written independent investigation, awaiting GPT review",
       "scope":obligations,
       "not_an_automated_claim":"The code checks document structure, identities and coverage; it does not formally verify these analytical arguments."},
    "scientific_script_reexecuted_by_this_audit":False})
print(json.dumps({"document_checks":"PASS","PR_groups":23,"proof_tags":36,
                  "source_labels":41,"algebra_groups":14,"preserved_inputs":82}))
if not args.package:
    sys.exit(0)

top_names=[
    "READ_ME_REVIEW.md",PROOF,LEDGER,"COMPLETION_REPORT.md",
    "prepare_inputs.py","INPUT_BASELINE.json","INPUT_VERIFICATION.json",
    "source_verify.py","SOURCE_IDENTITIES.json","SUPPLIED_PACKET_VERIFICATION.json",
    "exact_checks.py","EXACT_ALGEBRA_RESULTS.json","EXACT_CHECK_EXECUTION.json",
    "audit_and_package.py","INPUT_PRESERVATION.json","CLAIM_CROSSWALK.json","DOCUMENT_CHECKS.json"]
files={name:W/name for name in top_names}
files.update({"inputs/"+p.relative_to(I).as_posix():p for p in input_files})
assert len(files)==94
assert not any(name.lower().endswith((".zip",".pdf",".pyc")) for name in files)
assert not any("__pycache__" in name for name in files)
manifest={"utc":utc(),"self_excluded":"PACKAGE_MANIFEST.json",
          "scope":"Complete compact investigation payload; exact source packet carried once.",
          "files":[{"path":name,**ident(path)} for name,path in sorted(files.items())]}
save(W/"PACKAGE_MANIFEST.json",manifest)
files["PACKAGE_MANIFEST.json"]=W/"PACKAGE_MANIFEST.json"

delivery=W/"delivery"
delivery.mkdir(exist_ok=True)
archive=delivery/(TASK+"_REVIEW_PACKAGE.zip")
assert not archive.exists(),"Final archive already exists; do not silently overwrite a delivery."
with zipfile.ZipFile(archive,"x",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for name,path in sorted(files.items()):
        z.write(path,arcname=name)

verified=[]
with zipfile.ZipFile(archive) as z:
    names=z.namelist()
    assert len(names)==len(set(names))==len({n.casefold() for n in names})==95
    assert set(names)==set(files)
    assert z.testzip() is None
    actual_manifest=json.loads(z.read("PACKAGE_MANIFEST.json").decode("utf-8"))
    assert actual_manifest==manifest
    assert {r["path"] for r in actual_manifest["files"]}|{"PACKAGE_MANIFEST.json"}==set(names)
    for item in z.infolist():
        name=item.filename
        pp=PurePosixPath(name)
        assert str(pp)==name and not pp.is_absolute()
        assert ".." not in pp.parts and "\\" not in name and ":" not in name
        assert not item.is_dir() and ((item.external_attr>>16)&0o170000)!=0o120000
        b=z.read(name)
        actual={"bytes":len(b),"sha256":sha(b)}
        assert b==files[name].read_bytes()
        assert len(b)==item.file_size
        verified.append({"path":name,**actual,"CRC32":f"{item.CRC:08x}",
                         "equals_standalone_bytes":True})
    actuals={r["path"]:r for r in verified}
    for r in manifest["files"]:
        assert all(r[k]==actuals[r["path"]][k] for k in ("bytes","sha256"))
    # The input manifest is independently exhaustive inside the final ZIP.
    nested=json.loads(z.read("inputs/PACKET_MANIFEST.json").decode("utf-8"))
    assert {"inputs/"+r["path"] for r in nested["files"]}|{"inputs/PACKET_MANIFEST.json"}=={
        n for n in names if n.startswith("inputs/")}
    for r in nested["files"]:
        assert all(r[k]==actuals["inputs/"+r["path"]][k] for k in ("bytes","sha256"))

final_id=ident(archive)
sidecar=archive.with_name(archive.name+".sha256")
sidecar.write_text(final_id["sha256"]+"  "+archive.name+"\n",encoding="utf-8")
assert sidecar.read_text(encoding="utf-8").split()[0]==ident(archive)["sha256"]
for r in preserved:
    assert ident(Path(r["path"]))==r["before"],r["path"]
receipt=delivery/(TASK+"_PACKAGE_VERIFICATION.json")
save(receipt,{
    "utc":utc(),"status":"PASS","archive":{"path":str(archive),**final_id},
    "checksum_sidecar":{"path":str(sidecar),**ident(sidecar),"matches_final_zip":True},
    "unique_safe_file_members":95,"manifest_payloads":94,"CRC":"PASS",
    "exhaustive_self_excluded_manifest":"PASS","every_member_size_and_hash":"PASS",
    "all_standalone_payloads_byte_identical_to_archive":"PASS",
    "nested_original_input_manifest":"PASS","post_write_input_preservation":{"files":82,"status":"PASS"},
    "verification_script":ident(Path(__file__)),
    "files":verified,
    "noncircularity":"This receipt and the final ZIP checksum are outside the archive. The archive contains no self-referential container hash.",
    "limits":"No network, Git, scientific rerun or machine-formal proof was part of packaging."})
assert ident(archive)==final_id
print(json.dumps({"package":"PASS",**final_id,"members":95,"manifest_payloads":94,
                  "archive":str(archive),"receipt":str(receipt)},indent=2))
