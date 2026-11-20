from pathlib import Path
import json, re
ROOT=Path(__file__).resolve().parent
# Public provenance is a faithful excerpt of the local manuscript order.
MAP={
"GM01":{
"INH-01":["eq:native-pre","eq:native-full","eq:tuple"],
"INH-02":["eq:native-V","app:accounts"],
"INH-03":["eq:attachment","prop:bound"],
"INH-04":[],
"DED-01":["sec:fields","app:accounts"],
"DED-02":["prop:bound","eq:sharp"],
"DED-03":["eq:gravity-obstruction"],
"DED-04":[],
"DED-05":[],
"EXT-01":["eq:dictionary","eq:source-bound"],
"EXT-02":["eq:gravity-field","eq:mag-field","eq:force","eq:kinetic"],
"COND-01":["eq:gravity-field","eq:mag-field","eq:self"],
"COND-02":["prop:radial","eq:pair","eq:force","app:accounts"],
"COND-03":["eq:source-bound","eq:fourier"],
"DED-06":["eq:gravity-obstruction","eq:mag-obstruction"],
"OPEN-01":["sec:observation","app:accounts"],
},
"GM02":{
"GM02-P1":["sec:native","sec:fields"],
"GM02-A1":["eq:frozen","eq:feedback","eq:energy"],
"GM02-01":["eq:fourier","eq:endpoint","eq:mag-obstruction"],
"GM02-02":["prop:radial"],
"GM02-03":["eq:finite-work"],
"GM02-04":["thm:energy","eq:residual"],
"GM02-05":["sec:feedback","prop:off"],
"GM02-06":["eq:contraction","eq:gravity-load","eq:mag-box-range","app:bounds"],
"GM02-07":["eq:scalar","eq:ordering"],
"GM02-08":["eq:gravity-cubic"],
"GM02-09":["app:accounts"],
"GM02-O1":["sec:observation"],
},
"GM03":{
"GM03-P1":["sec:fields","sec:feedback"],
"GM03-01":["eq:neutral","eq:fourier-certificate"],
"GM03-02":["eq:neutral-exact","tab:benchmark"],
"GM03-03":["eq:vector-test","eq:doubling","prop:off"],
"GM03-04":["eq:nonzero"],
"GM03-05":["eq:switch-work","eq:geometry-work"],
"GM03-06":["eq:projection","eq:amplitude","eq:component-test"],
"GM03-07":["eq:energy-scale"],
"GM03-08":["eq:ratios","eq:scale"],
"GM03-09":["sec:observation"],
"GM03-10":["eq:vector-test","sec:observation"],
}}
qual={
"GM01/INH-04":"Background response and SRG lineage retained in evidence, not retold in this bounded paper.",
"GM01/DED-01":"Only its distinction between native and extra mechanical laws is used; no new mechanics is proposed.",
"GM01/DED-04":"Naive pointwise magnetic-field counterexample remains in evidence; paper instead states the solenoidal field law and its solution.",
"GM01/DED-05":"Independent-phase gauge counterexample remains in evidence; no local gauge interpretation is adopted.",
"GM01/COND-03":"Bound, Fourier silence and body-plane restriction used; conjugation test remains in original evidence.",
"GM01/OPEN-01":"GM02 closes a specified mathematical backreaction account; physical calibration, carrier and causal completion remain open.",
"GM03/GM03-06":"First-step scalar amplitude and necessary B-component test refine older all-coordinate wording. Full registered state still needed for full vector test.",
}
labels={}
aux=(ROOT/"build/tex/main.aux").read_text("utf-8")
compiled={label:{"number":number,"page":int(page)} for label,number,page in
          re.findall(r"\\newlabel\{([^}]+)\}\{\{([^}]+)\}\{(\d+)\}",aux)}
for f in (ROOT/"manuscript").glob("*.tex"):
    for n,line in enumerate(f.read_text("utf-8").splitlines(),1):
        for label in re.findall(r"\\label\{([^}]+)\}",line):
            assert label not in labels, label
            labels[label]={"file":f.relative_to(ROOT).as_posix(),"line":n,**compiled[label]}
rows=[]; locators={}
for study,mapping in MAP.items():
    ledger_path=ROOT/f"evidence/{study}/CLAIM_LEDGER.json"
    ledger=json.loads(ledger_path.read_text("utf-8"))
    result_name="VERIFICATION_RESULTS.json" if study=="GM01" else "CHECK_RESULTS.json"
    result=json.loads((ROOT/f"evidence/{study}/{result_name}").read_text("utf-8"))
    checkids={c["id"] for c in result["checks"]}
    report={"GM01":"GRAVITY_AND_MAGNETISM.md","GM02":"GM02_DERIVATIONS.md","GM03":"GM03_DERIVATIONS.md"}[study]
    for row in ledger["claims"]:
        id=row.get("id",row.get("claim_id")); selected=mapping[id]
        assert set(row["check_ids"]) <= checkids, (study,id)
        locations=[{"label":label,**labels[label]} for label in selected]
        rows.append(dict(study=study,claim_id=id,statement=row["statement"],
            original_status=row["status"],source=f"evidence/{study}/{report}",
            source_locations=row.get("note_locations",row.get("report_section",row.get("sections"))),
            preserved_claim_ledger=ledger_path.relative_to(ROOT).as_posix(),
            saved_check_file=f"evidence/{study}/{result_name}",saved_check_ids=row["check_ids"],
            manuscript_locations=locations,coverage="represented" if selected else "retained_background",
            limits=row.get("limits"),qualification=qual.get(f"{study}/{id}")))
    for p in json.loads((ROOT/f"evidence/{study}/PRIMARY_LOCATORS.json").read_text("utf-8")):
        src=p.get("path",p.get("source")); key=(src,p["label"])
        f=ROOT/"sources"/src
        assert f.exists(), src
        assert p["label"] in f.read_text("utf-8"),key
        locators[key]=dict(p,path=src,local_path="sources/"+src)
rows.extend([
dict(study="Manuscript refinement",claim_id="MR01",statement="Middle-channel amplitude identifies first gain on specified path.",
     source="provenance/MEASUREMENT_REFINEMENT.md",
     source_locations="Measurement wording refinement; GM03 (4)",
     manuscript_locations=[dict(label="eq:amplitude",**labels["eq:amplitude"])],
     saved_check_file="MANUSCRIPT_CHECKS.json",saved_check_ids=["M01_unit_omega","M03_amplitude_positivity","M04_amplitude_squared","M05_amplitude_inversion"],
     coverage="represented",qualification="Not a full-vector path verification."),
dict(study="Manuscript refinement",claim_id="MR02",statement="Nonzero registered B-component gives a necessary switch-off test.",
     source="provenance/MEASUREMENT_REFINEMENT.md",
     source_locations="Measurement wording refinement; GM03 (1), (20)",
     manuscript_locations=[dict(label="eq:component-test",**labels["eq:component-test"])],
     saved_check_file="MANUSCRIPT_CHECKS.json",saved_check_ids=["M06_component_test","M07_nonzero_component"],
     coverage="represented",qualification="Failure rejects vector prediction under controls; agreement in B alone leaves other components unchecked.")
])
(ROOT/"CLAIM_SOURCE_CROSSWALK.json").write_text(json.dumps({"status":"PASS","rows":rows,"manuscript_labels":labels},indent=2,ensure_ascii=False)+"\n","utf-8")
(ROOT/"SOURCE_LOCATORS.json").write_text(json.dumps(list(locators.values()),indent=2,ensure_ascii=False)+"\n","utf-8")
md=["# Claim/source crosswalk","",
    "All historical claims remain in unchanged evidence. Preparation-era statuses in those files are preserved; the supplied writing order records subsequent mathematical acceptance. No physical validation is inferred.","",
    "| Claim | Source locator | Manuscript labels | Scope note |","|---|---|---|---|"]
for r in rows:
    md.append("| "+r["study"]+"/"+r["claim_id"]+" | "+str(r["source_locations"])+" | "+
              ", ".join(x["label"] for x in r["manuscript_locations"])+" | "+(r.get("qualification") or r.get("limits") or "As in source")+" |")
(ROOT/"CLAIM_SOURCE_CROSSWALK.md").write_text("\n".join(md)+"\n","utf-8")
print(json.dumps({"status":"PASS","claims":len(rows),"labels":len(labels),"primary_locators":len(locators)}))
