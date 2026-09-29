"""Static v0.2 census validation. No scientific imports or theorem execution.

Use conda torment with -B. Required output must be a new external path.
All source/check/result inputs and before/after inventories are read only.
Coverage judgments belong to the review; this program checks their identities,
consistency, evidence links, recorded qualifications and integrity.
"""
import argparse
import ast
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

HEAD = "34c21830e7e7c4b5f4a5a940d084c37feaf1f82c"
KINDS = ("DIRECTLY_REDERIVED", "DERIVED_AS_PART_OF_LARGER_ENTRY",
         "BOUNDARY_ONLY", "PAPER_PROOF_OWNER_RETAINED",
         "SOFTWARE_ONLY_NOT_MATHEMATICAL_OWNER", "HISTORICAL_LITERAL_ONLY",
         "OPEN_BY_DEFINITION", "MISSING_MATHEMATICAL_COVERAGE")
CLASSES = {"CORE":24, "OPTIONAL":27, "RESEARCH_ONLY":13, "HISTORICAL":8, "OPEN":3}
DEPTHS = {"FULL", "SUFFICIENT", "PARTIAL", "NOT_APPLICABLE"}
TARGETS = {"SUPPLEMENT_A":["A07","A08","A09"],
           "SUPPLEMENT_F":["F02","F03","F04","F05","F06"]}
TREE_ROOTS = {
    "current":r"C:\TORMENT\TRIOCTAGON_new\trioctagon-physics",
    "old":r"C:\TORMENT\TRIOCTAGON_new\kernel_TO",
    "torment_kernel":r"C:\TORMENT\TORMENT_repo\TORMENT-fabric_v2\torment_fabric\torment_service\kernel",
    "torment_checkout":r"C:\TORMENT\TORMENT_repo\TORMENT-fabric_v2\torment_fabric"}

def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(1048576),b""): h.update(block)
    return h.hexdigest()

def map_sha(files):
    return hashlib.sha256(json.dumps(files,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def parse_ledger(path):
    rows,duplicates={},[]
    for line_number,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
        if not re.match(r"^\| [A-Z]\d{2} ",line): continue
        fields=[x.strip() for x in line.strip("|").split("|")]
        if len(fields)!=11: raise ValueError(f"Unexpected K0 row at {line_number}")
        ident,name=fields[0].split(" ",1)
        if ident in rows: duplicates.append(ident)
        rows[ident]={"NAME":name,"CLASS":fields[1].split("/")[-1].strip(),
                     "MATHEMATICAL_CONTENT":fields[2],"owner_text":fields[3]}
    return rows,duplicates

def sections(path):
    text=path.read_text(encoding="utf-8")
    matches=list(re.finditer(r"^## (\d+)\. .+$",text,re.M))
    return {int(m.group(1)):{"heading":m.group(0),
        "sha256":hashlib.sha256(text[m.start():matches[i+1].start() if i+1<len(matches) else len(text)].encode()).hexdigest()}
        for i,m in enumerate(matches)}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for option in ("crosswalk","review","output","integrity-directory"):
        parser.add_argument("--"+option,type=Path,required=True)
    parser.add_argument("--repo",type=Path)
    parser.add_argument("--reports",type=Path)
    args=parser.parse_args()
    if not sys.dont_write_bytecode: parser.error("-B is required")
    output=args.output.resolve()
    if output.exists() or output.is_relative_to(Path(r"C:\TORMENT").resolve()):
        parser.error("--output must be unused and outside protected C:/TORMENT")
    if not output.parent.is_dir(): parser.error("output parent must already exist")
    inputs=[args.crosswalk,args.review,Path(__file__)]
    if output in [x.resolve() for x in inputs]: parser.error("output may not overwrite inputs")
    data=read(args.crosswalk)
    roots={k:Path(v).resolve() for k,v in data["roots"].items()}
    if args.repo: roots["CURRENT_REPO"]=args.repo.resolve()
    if args.reports: roots["REPORTS"]=args.reports.resolve()
    repo=roots["CURRENT_REPO"]
    if output.is_relative_to(repo): parser.error("output must be outside repository")
    artifacts=data["artifacts"]
    checks=[]
    def check(name,passed,evidence):
        checks.append({"name":name,"passed":bool(passed),"evidence":evidence})
    def path(key):
        item=artifacts[key];root=roots[item["root"]]
        p=(root/item["path"]).resolve()
        if not p.is_relative_to(root): raise ValueError("Artifact escapes root: "+key)
        return p
    def git(*arguments):
        return subprocess.check_output(["git","--no-optional-locks","-C",str(repo),*arguments],
            text=True,stderr=subprocess.PIPE).strip()

    prior=read(path("PRIOR_CROSSWALK"))
    previous=read(path("PRIOR_RESULT"))
    oldrows={x["LEDGER_ID"]:x for x in prior["ledger_rows"]}
    rows=data["ledger_rows"];byid={x["LEDGER_ID"]:x for x in rows}
    identifiers=[x["LEDGER_ID"] for x in rows]
    targets={x for scope in TARGETS.values() for x in scope}
    frozen,duplicates=parse_ledger(path("K0"))
    check("authority and schema",git("rev-parse","HEAD")==HEAD==data["expected_head"]==data["observed_head"]
          and data["schema"]=="TRIOCTAGON_CURRENT_KERNEL_ATLAS_CROSSWALK/0.2",HEAD)
    check("75 exact K0 IDs once; no extras or duplicates",len(rows)==75==len(frozen)
          and len(set(identifiers))==75 and not duplicates and set(identifiers)==set(frozen),
          {"count":len(rows),"missing":sorted(set(frozen)-set(identifiers)),"extras":sorted(set(identifiers)-set(frozen))})
    classes=dict(Counter(x["CLASS"] for x in rows))
    counts=Counter(x["COVERAGE_KIND"] for x in rows)
    coverage={k:counts[k] for k in KINDS}
    check("frozen class totals",classes==CLASSES==data["class_counts"],classes)
    check("coverage vocabulary and recomputed totals",all(x["COVERAGE_KIND"] in KINDS and x["DEPTH"] in DEPTHS for x in rows)
          and sum(coverage.values())==75 and coverage==data["coverage_counts"],coverage)
    check("prior HOLD receipt remains valid historical authority",
          previous["validation_status"]=="PASS" and previous["LANE1_COMPLETENESS"]=="HOLD"
          and previous["checks_total"]==previous["checks_passed"]==len(previous["checks"])
          and previous["crosswalk_sha256"]==sha(path("PRIOR_CROSSWALK"))
          and previous["review_sha256"]==sha(path("PRIOR_REVIEW"))
          and previous["checker_sha256"]==sha(path("PRIOR_CHECKER"))
          and set(prior["decision"]["missing_ledger_ids"])==targets,
          {"prior_decision":previous["LANE1_COMPLETENESS"],"prior_checks":previous["checks_total"]})
    check("predecessor artifact pins are preserved",
          all(artifacts.get(k)==v for k,v in prior["artifacts"].items()),
          {"prior_artifact_count":len(prior["artifacts"])})
    checked_hashes=[];hash_errors=[]
    for key,item in artifacts.items():
        p=path(key)
        if not p.is_file():
            hash_errors.append([key,"missing"]);continue
        digest=sha(p)
        ok=digest==item["sha256"] and p.stat().st_size==item["bytes"]
        if item.get("previously_recorded_sha256",digest)!=digest: ok=False
        if not ok: hash_errors.append([key,"hash_or_size"])
        checked_hashes.append({"artifact":key,"sha256":digest,"bytes":p.stat().st_size})
    check("every registered artifact exists and matches pinned bytes",not hash_errors,
          {"count":len(checked_hashes),"errors":hash_errors})

    # One independently parsed identity/evidence/coverage check per frozen row.
    revalidations={x["LEDGER_ID"]:x for x in data["row_revalidations"]}
    check("75 explicit row revalidations",len(data["row_revalidations"])==75
          and set(revalidations)==set(frozen),len(revalidations))
    for row in rows:
        ident=row["LEDGER_ID"];authority=frozen.get(ident,{})
        refs=row["OWNER"]["artifacts"]+[x["artifact"] for x in row["EVIDENCE"]]
        identity=all(row.get(k)==authority.get(k) for k in ("NAME","CLASS","MATHEMATICAL_CONTENT"))
        identity &= row["OWNER"]["frozen_ledger_text"]==authority.get("owner_text")
        evidence=bool(row["OWNER"]["artifacts"]) and bool(row["EVIDENCE"]) and all(k in artifacts for k in refs)
        evidence &= all(x.get("locator") for x in row["EVIDENCE"])
        evidence &= set(row["ATLAS_COVERAGE"]) <= {f"{n:02}" for n in range(1,10)}
        rr=revalidations.get(ident,{})
        consistency=rr.get("contradiction_found") is False and set(rr.get("evidence_artifacts",[]))==set(refs)
        if ident not in targets:
            consistency &= row==oldrows[ident] and rr.get("prior_row_preserved") is True
        else:
            supplement="SUPPLEMENT_A" if ident[0]=="A" else "SUPPLEMENT_F"
            consistency &= (row["COVERAGE_KIND"]=="DIRECTLY_REDERIVED" and row["DEPTH"]=="FULL"
                and row["MISSING_REASON"] is None and row["ATLAS_RECONSTRUCTION_COMPLETE"] is True
                and row.get("SUPPLEMENT_COVERAGE")==[supplement]
                and supplement in refs and supplement+"_RESULT" in refs
                and row["OWNER"]==oldrows[ident]["OWNER"])
        check("row "+ident+" frozen identity, evidence and reassessment",
              identity and evidence and consistency and bool(row["DISPOSITION"]),
              {"coverage":row["COVERAGE_KIND"],"depth":row["DEPTH"],
               "references":sorted(set(refs)),"unchanged_from_v01":row==oldrows[ident]})
    changed=[x["LEDGER_ID"] for x in rows if x!=oldrows[x["LEDGER_ID"]]]
    check("only the eight authorized row objects changed",set(changed)==targets and len(changed)==8,changed)

    closure=data["closure_reassessments"]
    check("eight precise closure reassessments",set(closure)==targets,len(closure))
    for ident,c in closure.items():
        source_sections=sections(path(c["supplement"]))
        errs=[]
        for item in c["requirements"]:
            if not item["requirement"] or not item["assessment"] or item["disposition"]!="CLOSED": errs.append("incomplete requirement")
            if [x["section"] for x in item["evidence"]]!=item["sections"]: errs.append("section mismatch")
            for ref in item["evidence"]:
                actual=source_sections.get(ref["section"],{})
                if (ref["artifact"]!=c["supplement"] or ref["heading"]!=actual.get("heading")
                    or ref["section_sha256"]!=actual.get("sha256")): errs.append(ref)
        check(ident+" written omission-to-section identity",
              not errs and c["prior_omission"]==oldrows[ident]["MISSING_REASON"]
              and c["written_coverage_review"]=="FULL" and c["proof_is_not_predicate_count"] is True
              and c["contradiction_found"] is False,
              {"requirements":len(c["requirements"]),"errors":errs,"qualification":"Section identity and review metadata; not theorem execution"})

    registers={x["ID"]:x for x in data["supplement_register"]}
    check("both supplement registry entries once",len(data["supplement_register"])==2 and set(registers)==set(TARGETS),list(registers))
    supplement_summary={}
    for key,scope in TARGETS.items():
        reg=registers[key];result=read(path(reg["RESULT"]))
        rc=result["checks"];n=len(rc)
        expected=31 if key=="SUPPLEMENT_A" else 89
        groups=dict(Counter(x["group"] for x in rc))
        stated=result["check_summary"]["total"] if key=="SUPPLEMENT_A" else result["check_count"]
        check(key+" recorded checker state and identity",result["passed"] is True and result["closeout_ready"] is True
              and n==stated==expected==reg["CHECK_COUNT"]==reg["CHECKS_PASSED"]
              and all(x["passed"] for x in rc) and result["checker_sha256"]==sha(path(reg["CHECKER"]))
              and result["head"]==HEAD and reg["SOURCE_HEAD"]==HEAD
              and reg["STATUS"]=="PASS" and reg["CLOSEOUT_READY"] is True
              and reg["PUBLICATION_STATE"]=="EXTERNAL_UNPUBLISHED",
              {"recorded_checks":n,"groups":groups,"executed_in_v02":False})
        check(key+" scope and FULL owners",result["scope"]==scope==reg["SCOPE"]
              and result["owner_status"]=={i:"FULL" for i in scope}==reg["OWNER_STATUS"],scope)
        check(key+" registry source/check/result hashes",
              all(reg["SHA256"][role]==artifacts[reg[role]]["sha256"] for role in ("SOURCE_PACKET","CHECKER","RESULT")),reg["SHA256"])
        src_errors=[p for p,h in result["source_sha256"].items() if not Path(p).is_file() or sha(p)!=h]
        check(key+" recorded source identities still current",not src_errors,src_errors)
        receipts=result["receipts"]
        receipt_errors=[]
        for name,receipt in receipts.items():
            rp=Path(receipt["path"])
            if (not rp.is_file() or sha(rp)!=receipt["sha256"] or read(rp)!=receipt["data"]
                or receipt["data"].get("passed") is not True): receipt_errors.append(name)
        check(key+" separate embedded receipts match originals",
              set(receipts)=={"test","packaging","integrity"} and not receipt_errors,receipt_errors)
        test=receipts["test"]["data"];tq=reg["TEST_QUALIFICATION"]
        tests,subtests=(10,40) if key=="SUPPLEMENT_A" else (8,0)
        stdout_ok=f"{tests} passed" in test["stdout"] and (not subtests or f"{subtests} subtests passed" in test["stdout"])
        check(key+" recorded focused test qualification",
              test["exit_code"]==0 and test["stderr"]=="" and stdout_ok
              and hashlib.sha256(test["stdout"].encode()).hexdigest()==test["stdout_sha256"]
              and hashlib.sha256(test["stderr"].encode()).hexdigest()==test["stderr_sha256"]
              and tq["tests"]==tests and tq["subtests"]==subtests and tq["exit_code"]==0
              and tq["stderr_empty"] is True and tq["rerun_in_v02"] is False
              and tq["clears_atlas_07_08_caveat"] is False,
              {"tests":tests,"subtests":subtests,"exit_code":test["exit_code"],"stderr_empty":test["stderr"]==""})
        qualification=reg["ANALYTIC_PROOF_QUALIFICATION"]
        analytic_ok=qualification["finite_predicates_certify_analytic_theorems"] is False
        analytic_ok &= qualification["written_proof_owner"]==key and bool(qualification["qualification"])
        if key=="SUPPLEMENT_A":
            analytic_ok &= result["finite_audits_are_universal_proofs"] is False and bool(result["universal_proof_owner"])
        else:
            analytic_ok &= result["analytic_proofs_certified_by_predicate_count"] is False and bool(result["analytic_proof_owner"])
            analytic_ok &= result["prior_atlas_07_08_runtime_caveat"]=="UNRESOLVED_NOT_INVESTIGATED"
        check(key+" written-proof/count separation",analytic_ok,qualification)
        # Parse source as text only; no exec, importlib or theorem invocation.
        ast.parse(path(reg["CHECKER"]).read_text(encoding="utf-8"))
        supplement_summary[key]={"scope":scope,"recorded_checks":n,"recorded_passed":sum(x["passed"] for x in rc),
                                  "test_qualification":tq,"analytic_proof_qualification":qualification}

    atlas=data["atlas_register"];atlas_by={x["ENTRY"]:x for x in atlas}
    check("Atlas 01–09 entire registry and statuses unchanged",atlas==prior["atlas_register"]
          and sorted(atlas_by)==[f"{i:02}" for i in range(1,10)] and len(atlas)==9,len(atlas))
    atlas_errors=[]
    for entry in atlas:
        if entry["ENTRY"]=="01":
            if any(entry[k] is not None for k in ("CHECKER","RESULT","CHECK_COUNT")): atlas_errors.append("01 invented count")
            continue
        result=read(path(entry["RESULT"]))
        n=result.get("total",result.get("check_count",result.get("scientific_summary",{}).get("total",result.get("summary",{}).get("total"))))
        if n is None:n=len(result.get("checks",[]))
        if n!=entry["CHECK_COUNT"]:atlas_errors.append([entry["ENTRY"],"count"])
        digest=result.get("checker_sha256",result.get("script_sha256"))
        if digest and digest!=artifacts[entry["CHECKER"]]["sha256"]:atlas_errors.append([entry["ENTRY"],"checker"])
        for role in ("SOURCE_PACKET","CHECKER","RESULT"):
            if entry["SHA256"][role]!=artifacts[entry[role]]["sha256"]:atlas_errors.append([entry["ENTRY"],role])
    check("Atlas recorded evidence identities",not atlas_errors,atlas_errors)
    caveats={x["entry"]:x for x in data["runtime_caveat_register"]}
    check("Atlas 07/08 caveats persist; clean F does not clear them",
          all(atlas_by[i]["STATUS"]=="PASS_WITH_RUNTIME_CAVEAT" and "OPEN" in atlas_by[i]["RUNTIME_QUALIFICATION"]
              and caveats[i]["status"]=="PASS_WITH_RUNTIME_CAVEAT" and caveats[i]["caveat_status"]=="OPEN_RUNTIME_CAVEAT"
              and caveats[i]["investigated_in_v02"] is False for i in ("07","08"))
          and caveats["SUPPLEMENT_F"]["clears_prior_caveats"] is False,data["runtime_caveat_register"])
    check("open interfaces and prior caveats are preserved",
          data["open_interfaces"]==prior["open_interfaces"]
          and all(x in data["known_caveats"] for x in prior["known_caveats"]),data["open_interfaces"])
    check("retained software/historical/open distinctions",
          all(byid[i]==oldrows[i] for i in identifiers if oldrows[i]["COVERAGE_KIND"] in
              ("SOFTWARE_ONLY_NOT_MATHEMATICAL_OWNER","HISTORICAL_LITERAL_ONLY","OPEN_BY_DEFINITION"))
          and frozen["O01"]["CLASS"]==frozen["O03"]["CLASS"]=="OPEN",
          {"O01":"RESOLVED_OPTION_B with frozen OPEN","O03":"CLOSED_BY_K2B with frozen OPEN"})
    arch_text=path("ARCHAEOLOGY").read_text(encoding="utf-8")
    arch_ids=re.findall(r"^### (M\d{2}) — .*? \[A\]",arch_text,re.M)
    arch=data["archaeology_current_science"];represented=[x["ARCHAEOLOGY_ID"] for x in arch]
    check("all 15 archaeology CURRENT_SCIENCE systems",
          arch==prior["archaeology_current_science"] and len(arch)==len(set(represented))==15
          and set(represented)==set(arch_ids)
          and all(x["DISPOSITION"] in ("ATLAS_COVERED","PAPER_PROOF_OWNER_RETAINED")
              and set(x["LEDGER_IDS"])<=set(frozen) and x["REASON"] for x in arch),
          dict(Counter(x["DISPOSITION"] for x in arch)))
    git_files=git("ls-tree","-r","--name-only","HEAD").splitlines()
    actual=sorted(p.name for p in (repo/"kernel_physics").glob("*.py"))
    tracked=sorted(Path(p).name for p in git_files if p.startswith("kernel_physics/") and p.count("/")==1 and p.endswith(".py"))
    arch_section=arch_text.split("### Current kernel: 19 referenced source files",1)[1].split("### Production source identity evidence",1)[0]
    archived=sorted(set(re.findall(r"\*\*\[([_\w]+\.py)\]",arch_section)))
    census=data["module_census"]
    k0files=sorted(p for p in git("ls-tree","--name-only",census["k0_authority_head"]+":kernel_physics").splitlines() if p.endswith(".py"))
    check("19-module current/Git/archaeology/K0 census",
          actual==tracked==archived==census["current_top_level_files"] and len(actual)==19
          and k0files==census["k0_existing_files"]
          and sorted(set(actual)-set(k0files))==census["added_since_k0"],census)
    module_errors=[]
    for item in data["runtime_modules"]+data["software_support_modules"]:
        syntax=ast.parse(path(item["artifact"]).read_text(encoding="utf-8"))
        definitions=[{"name":node.name,"line":node.lineno} for node in syntax.body if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef))]
        if definitions!=item["definitions"]:module_errors.append(item["artifact"])
    check("runtime and UI/build AST inventories/classifications unchanged",
          not module_errors and data["runtime_modules"]==prior["runtime_modules"]
          and data["software_support_modules"]==prior["software_support_modules"]
          and Counter(x["classification"] for x in data["runtime_modules"])==
              {"MATHEMATICAL_OWNER":11,"SOFTWARE_ONLY_NOT_MATHEMATICAL_OWNER":8}
          and len(data["software_support_modules"])==16,module_errors)
    local={}
    for name in ("test_operating_region.py","test_boundary_pipeline.py"):
        rel="kernel_physics/tests/"+name
        local[rel]={"exists":(repo/rel).is_file(),"tracked":rel in git_files,"sha256":sha(repo/rel)}
    check("Option-B local-only tests remain qualified",all(x["exists"] and not x["tracked"] for x in local.values()),local)
    check("current O01/O03 software resolution evidence",
          "O01 is resolved as Option B" in path("README").read_text(encoding="utf-8")
          and "O03 = CLOSED" in path("K2B").read_text(encoding="utf-8")
          and "kernel_physics/tests/fixtures/golden_388/TRAJECTORIES.csv" in git_files,
          {"historical_K0_classes_preserved":True})

    w=args.integrity_directory.resolve()
    before,after=read(w/"before.json"),read(w/"after.json")
    integrity={}
    for label,expected_root in TREE_ROOTS.items():
        a,b=before[label],after[label]
        valid=all(x["count"]==len(x["files"]) and x["tree_sha256"]==map_sha(x["files"]) for x in (a,b))
        valid &= Path(a["root"]).resolve()==Path(b["root"]).resolve()==Path(expected_root).resolve()
        detail={"root":a["root"],"before_count":a["count"],"after_count":b["count"],
          "before_sha256":a["tree_sha256"],"after_sha256":b["tree_sha256"],
          "added":sorted(set(b["files"])-set(a["files"])),"removed":sorted(set(a["files"])-set(b["files"])),
          "modified":sorted(p for p in set(a["files"])&set(b["files"]) if a["files"][p]!=b["files"][p]),
          "before_completed_utc":a["end_utc"],"after_completed_utc":b["end_utc"]}
        detail["unchanged"]=valid and a["files"]==b["files"]
        integrity[label]=detail
        check("fresh full tree inventory "+label,detail["unchanged"],detail)
    git_before,git_after=read(w/"git_before.json"),read(w/"git_after.json")
    git_ok=git_before==git_after and git_after["current"]["head"]==HEAD
    check("Git HEAD and tracked status unchanged",git_ok,git_after)
    external_before=read(w/"external_before.json");external={}
    for label,files in external_before.items():
        actual_map={p:sha(p) if Path(p).is_file() else None for p in files}
        external[label]={"files":len(files),"before_sha256":map_sha(files),"after_sha256":map_sha(actual_map),
                         "unchanged":files==actual_map,"changed_paths":[p for p in files if files[p]!=actual_map[p]]}
        check("external protected set "+label,external[label]["unchanged"],external[label])
    check("external protected set census",set(external)=={"prior_atlas","completeness_review","supplement_a","supplement_f"}
          and {k:v["files"] for k,v in external.items()}=={"prior_atlas":27,"completeness_review":4,"supplement_a":3,"supplement_f":3},
          {k:v["files"] for k,v in external.items()})
    subsets={}
    for label,predicate in [("papers_a_f",lambda p:bool(re.match(r"papers/PAPER_[A-F]/",p))),
                            ("published_atlas",lambda p:p.startswith("research/mathematical_atlas/"))]:
        a={k:v for k,v in before["current"]["files"].items() if predicate(k)}
        b={k:v for k,v in after["current"]["files"].items() if predicate(k)}
        subsets[label]={"count":len(a),"before_sha256":map_sha(a),"after_sha256":map_sha(b),"unchanged":a==b}
        check("protected subset "+label,a==b,subsets[label])
    missing=[x["LEDGER_ID"] for x in rows if x["COVERAGE_KIND"]=="MISSING_MATHEMATICAL_COVERAGE"]
    partial=[x["LEDGER_ID"] for x in rows if x["DEPTH"]=="PARTIAL" and x["COVERAGE_KIND"] not in
             ("SOFTWARE_ONLY_NOT_MATHEMATICAL_OWNER","HISTORICAL_LITERAL_ONLY","OPEN_BY_DEFINITION")]
    mathematical_kinds=set(KINDS)-{"SOFTWARE_ONLY_NOT_MATHEMATICAL_OWNER","HISTORICAL_LITERAL_ONLY","OPEN_BY_DEFINITION"}
    adequate=all(x["DEPTH"] in ("FULL","SUFFICIENT") for x in rows if x["COVERAGE_KIND"] in mathematical_kinds)
    coverage_pass=not missing and not partial and adequate
    check("PASS coverage gate: no missing or unqualified partial owner",
          coverage_pass and data["decision"]["missing_ledger_ids"]==missing
          and data["decision"]["partial_mathematical_ids"]==partial,
          {"missing":missing,"partial":partial,"adequate_roles":adequate})
    check("completed bounded followups are retained with owners",
          data["bounded_followups"]==[] and {i for x in data["completed_followups"] for i in x["ledger_ids"]}==targets
          and all(x["status"]=="CLOSED" for x in data["completed_followups"]),data["completed_followups"])
    recommendation=data["publication_recommendation"]
    check("publication recommendation only; caveat metadata retained",
          recommendation["status"]=="RECOMMENDED_NOT_EXECUTED" and recommendation["execute_now"] is False
          and recommendation["manifest_requirements"]["runtime_caveat"]==
              {"Atlas07":"OPEN_RUNTIME_CAVEAT","Atlas08":"OPEN_RUNTIME_CAVEAT","cleared_by_supplement_f":False}
          and len(recommendation["contents"])==3,recommendation)
    check("companion readiness is scoped and provisional",
          len(data["companion_readiness"])==7
          and all(x["DEPENDENCIES"] and x["READINESS"]!="BLOCKED_BY_MISSING_ATLAS" for x in data["companion_readiness"])
          and all(x["READINESS"]=="JOINT_SYNTHESIS_ASSESSMENT" for x in data["companion_readiness"] if x["ORIGINAL_PAPER"] in ("C","D")),
          data["companion_readiness"])
    review=args.review.read_text(encoding="utf-8")
    ledger_table=review.split("## 4. Recomputed coverage and complete 75-row disposition",1)[1].split(
        "## 5. Atlas registry, archaeology and module census",1)[0]
    table_ids=re.findall(r"^\| ([A-Z]\d{2}) \|",ledger_table,re.M)
    check("review has complete unique row table and proof/caveat qualifications",
          len(table_ids)==75 and set(table_ids)==set(frozen) and len(set(table_ids))==75
          and "LANE1_COMPLETENESS = PASS" in review
          and "finite predicates do not certify analytic theorems by count" in review
          and "INTEGRITY_FINAL_RECORD" not in review
          and "PASS_WITH_RUNTIME_CAVEAT" in review,
          {"sha256":sha(args.review),"ledger_table_count":len(table_ids)})
    local_links=re.findall(r"\]\(<(C:/[^>]+)>\)",review)
    check("review local artifact links resolve",all(Path(p).is_file() for p in local_links),{"links":len(local_links)})
    module_names=set(sys.modules)
    check("static execution boundary",not any(x=="sympy" or x=="numpy" or x.startswith("kernel_physics")
          or x.startswith("paper_f_") for x in module_names),
          {"scientific_code_executed":False,"method":"Standard-library file/Git/AST/JSON metadata only"})
    ok=all(x["passed"] for x in checks)
    decision="PASS" if ok and coverage_pass else "HOLD"
    check("final decision includes metadata and integrity gates",decision==data["decision"]["LANE1_COMPLETENESS"],
          {"derived":decision,"crosswalk":data["decision"]["LANE1_COMPLETENESS"]})
    ok=all(x["passed"] for x in checks)
    flags={
        "CURRENT_REPO_CHANGED":"NO" if integrity["current"]["unchanged"] and git_ok else "YES",
        "OLD_KERNEL_CHANGED":"NO" if integrity["old"]["unchanged"] else "YES",
        "TORMENT_CHANGED":"NO" if integrity["torment_kernel"]["unchanged"] and integrity["torment_checkout"]["unchanged"] and git_ok else "YES",
        "PAPERS_A_F_CHANGED":"NO" if subsets["papers_a_f"]["unchanged"] else "YES",
        "PRIOR_ATLAS_CHANGED":"NO" if subsets["published_atlas"]["unchanged"] and external["prior_atlas"]["unchanged"] else "YES",
        "COMPLETENESS_V0_1_CHANGED":"NO" if external["completeness_review"]["unchanged"] else "YES",
        "SUPPLEMENT_A_CHANGED":"NO" if external["supplement_a"]["unchanged"] else "YES",
        "SUPPLEMENT_F_CHANGED":"NO" if external["supplement_f"]["unchanged"] else "YES",
        "COMMITS":0,"PUSHES":0,"PUBLICATION":"NO"}
    result={
      "schema":"TRIOCTAGON_CURRENT_KERNEL_COMPLETENESS_RESULTS/0.2",
      "created_utc":datetime.now(timezone.utc).isoformat(),
      "validation_status":"PASS" if ok else "FAIL","LANE1_COMPLETENESS":decision,
      "checks_total":len(checks),"checks_passed":sum(x["passed"] for x in checks),"checks":checks,
      "ledger_rows_total":len(rows),"class_counts":classes,"coverage_counts":coverage,
      "missing_ledger_ids":missing,"partial_mathematical_ids":partial,
      "changed_ledger_ids":changed,"unchanged_ledger_rows":len(rows)-len(changed),
      "target_owner_status":{i:byid[i]["DEPTH"] for i in sorted(targets)},
      "artifact_hash_verification":checked_hashes,"supplement_summary":supplement_summary,
      "integrity":integrity,"external_integrity":external,"subset_integrity":subsets,
      "integrity_manifest_sha256":{p.name:sha(p) for p in [w/"before.json",w/"after.json",w/"git_before.json",w/"git_after.json",w/"external_before.json"]},
      "runtime_caveat_register":data["runtime_caveat_register"],
      "publication_recommendation":recommendation,"required_flags":flags,
      "crosswalk_sha256":sha(args.crosswalk),"review_sha256":sha(args.review),"checker_sha256":sha(__file__),
      "python":sys.version,"executable":sys.executable,"command":sys.argv,
      "scientific_code_executed":False,
      "qualification":"Static census consistency and integrity only. The written source/coverage review supplies mathematical ownership judgments; no predicate count proves analytic theorems. No prior scientific checker or tests were rerun. Action flags are operator attestations supported by unchanged inventories/HEADs."}
    with output.open("x",encoding="utf-8") as stream:
        json.dump(result,stream,indent=2,ensure_ascii=False);stream.write("\n")
    print(json.dumps({k:result[k] for k in ("validation_status","LANE1_COMPLETENESS","checks_total","checks_passed","missing_ledger_ids","partial_mathematical_ids")}))
    print(json.dumps({"failed":[x["name"] for x in checks if not x["passed"]]}))
    return 0 if ok else 1

if __name__=="__main__":
    raise SystemExit(main())
