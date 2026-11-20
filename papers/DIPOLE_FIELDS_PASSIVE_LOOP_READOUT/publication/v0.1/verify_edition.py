"""Portable publication document checks; does not execute any scientific suite."""
from pathlib import Path
import os,json,hashlib,re,math
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parent
assert os.environ.get("CONDA_DEFAULT_ENV")=="torment"
def read(p):return (ROOT/p).read_text("utf-8")
def load(p):return json.loads(read(p))
def sha(b):return hashlib.sha256(b).hexdigest()
checks=[]
def check(name,result):
    checks.append(dict(name=name,passed=bool(result)))
    if not result:raise AssertionError(name)
science=load("SCIENTIFIC_SOURCE_SELECTION.json")
for r in science["files"]:
    b=(ROOT/r["path"]).read_bytes()
    check("Accepted scientific bytes: "+r["path"],len(b)==r["bytes"] and sha(b)==r["sha256"])
sources=load("SOURCE_VERIFICATION.json")
for r in sources["sources"]:
    b=(ROOT/r["saved_as"]).read_bytes()
    check("Primary SHA-256 and Git blob: "+r["saved_as"],
          sha(b)==r["sha256"] and hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()==r["git_blob"])
tex={p.relative_to(ROOT).as_posix():p.read_text("utf-8") for p in (ROOT/"manuscript").rglob("*.tex")}
alltex="\n".join(tex.values())
baseline=load("provenance/MATHEMATICAL_BASELINE.json")
pat=r"\\begin\{(?:equation|align|tabular|tabularx)\}.*?\\end\{(?:equation|align|tabular|tabularx)\}"
for name,hashes in baseline["blocks"].items():
    check("Unchanged displayed math/tables: "+name,[sha(s.encode()) for s in re.findall(pat,tex[name],re.S)]==hashes)
reviewed=read("provenance/04_receiver_REVIEWED.tex")
check("Reviewed replacement identity",sha(reviewed.encode())=="f737d69e898d251fcd3f5e1f04a786b3d4c12ab6a89d703677fa23a3b35383a0")
check("Receiver retains both edits with layout-only scaling",tex["manuscript/04_receiver.tex"]==reviewed.replace(
    r"\centering\resizebox{\textwidth}{!}{\input{figures/native}}",r"\centering\resizebox{0.90\textwidth}{!}{\input{figures/native}}"))
check("Publication status is current","Author-approved repository research edition." in tex["manuscript/main.tex"] and
      "pending" not in tex["manuscript/main.tex"] and "Review draft" not in alltex)
doc=load("DOCUMENT_VERIFICATION.json");build=load("BUILD_RECORD.json")
pdf=ROOT/build["pdf"];reader=PdfReader(pdf)
check("Final PDF and source identity",sha(pdf.read_bytes())==doc["pdf_sha256"]==build["pdf_sha256"] and
      all(sha((ROOT/n).read_bytes())==h for n,h in build["sources"].items()))
check("Clean Windows torment build",build["returncode"]==0 and build["conda"]=="torment" and
      "Windows" in build["platform"] and doc["status"]=="PASS" and not doc["warnings"])
check("Metadata, pages and fonts",len(reader.pages)==15 and reader.metadata.author=="Hilmir Frímann Halldórsson" and
      reader.metadata.title=="Dipole Fields and Passive Loop Readout in the Tri-Octagon Model" and
      "author-approved" in reader.metadata.subject and all(r["embedded"] for r in doc["fonts"].values()))
labels=re.findall(r"\\label\{([^}]+)\}",alltex);refs=re.findall(r"\\(?:eqref|ref)\{([^}]+)\}",alltex)
cites=[s.strip() for g in re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}",alltex) for s in g.split(",")]
bibs=re.findall(r"\\bibitem\{([^}]+)\}",alltex)
check("81 unique labels and resolved references",len(labels)==len(set(labels))==81 and set(refs)<=set(labels))
check("10 bibliography entries and resolved citations",len(bibs)==len(set(bibs))==10 and set(cites)<=set(bibs))
visual=load("VISUAL_INSPECTION.json")
check("Every final page inspected",visual["status"]=="PASS" and visual["pdf_sha256"]==doc["pdf_sha256"] and
      [r["page"] for r in visual["pages"]]==list(range(1,16)) and all(r["status"]=="PASS" and
      sha((ROOT/r["path"]).read_bytes())==r["sha256"] for r in visual["pages"]))
cross=load("CLAIM_SOURCE_CROSSWALK.json")
check("Crosswalk covers every label",cross["pdf_sha256"]==doc["pdf_sha256"] and
      {m["label"] for c in cross["claims"] for m in c["manuscript"]}==set(labels))
for c in cross["claims"]:
    check("Public evidence links and hashes: "+c["id"],all(sha((ROOT/e["file"]).read_bytes())==e["sha256"] for e in c["evidence"]))
for name in ("README.md","BUILD.md","CURRENT_STATUS.md","CLAIM_SOURCE_CROSSWALK.md"):
    links=re.findall(r"\]\(([^)]+)\)",read(name))
    check("Edition links resolve: "+name,all("://" in t or t=="PUBLICATION_MANIFEST.json" or (ROOT/t.split("#")[0]).exists() for t in links))
saved=load("evidence/GM06/CHECK_RESULTS.json")
field=tex["manuscript/02_field.tex"];receiver=tex["manuscript/04_receiver.tex"]
rows=re.findall(r"(?m)^([248])&([.0-9]+)&([.0-9]+)&([.0-9]+)\\\\",field)
check("All coaxial saved rows",len(rows)==3 and all(float(a[0])==b["z_over_width"] and all(math.isclose(float(v),b[k],rel_tol=5e-12) for v,k in zip(a[1:],["contour","center_curl_component","center_error_bound"])) for a,b in zip(rows,saved["coaxial"])))
rows=[s for s in receiver.splitlines() if re.match(r"^(100|200)&",s)]
check("Both native saved rows",len(rows)==2 and all(all(math.isclose(float(m)*10**int(e),v,rel_tol=5e-14) for (m,e),v in zip(
    re.findall(r"(-?[\d.]+)\\,10\^\{(-?\d+)\}",r),[s["contour_by_N"]["256"],s["leading_component"],s["absolute_error_bound"]])) for r,s in zip(rows,saved["native"])))
num,den=saved["rational_far_bound"].split("/")
check("Exact range certificate transcribed",r"\frac{"+num+"}{"+den+"}" in receiver)
report=dict(status="PASS",checks=checks,count=len(checks),pdf_sha256=doc["pdf_sha256"],pages=15,
    selected_scientific_files=len(science["files"]),flat_primary_sources=len(sources["sources"]),
    mathematical_blocks=sum(len(x) for x in baseline["blocks"].values()),scientific_suites_rerun=False,
    scope="Publication document/source verification and saved-value transcription, carrying the corrected edition's 114-check record forward through exact math/table identity.")
(ROOT/"PUBLICATION_VERIFICATION.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n","utf-8")
print(json.dumps({k:report[k] for k in ["status","count","pages","selected_scientific_files","mathematical_blocks","pdf_sha256"]}))
