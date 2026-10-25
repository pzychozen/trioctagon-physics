"""R1 intake and two exact editorial edits; no historical/scientific imports."""
from pathlib import Path
import json,hashlib,zipfile,shutil,difflib
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/"v0.1"
DOWNLOAD=Path("C:/Users/Notandi/Downloads")
ZIP="SRG_VOLUME_III_SIM06_SIM07_v0.1_CANDIDATE_REVIEW.zip"
def sha(b):return hashlib.sha256(b).hexdigest()
def ident(p):
    b=p.read_bytes()
    return {"bytes":len(b),"sha256":sha(b)}
def dump(p,o):
    (ROOT/p).parent.mkdir(parents=True,exist_ok=True)
    (ROOT/p).write_text(json.dumps(o,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
assert ident(OLD/ZIP)["sha256"]=="3d23ed7375b069913f7ac562c855d181ccd5f36c90147f1c090545e3540a95cd"
assert not (ROOT/"manuscript.tex").exists(),"Do not overwrite prepared R1"
baseline=[]
with zipfile.ZipFile(OLD/ZIP) as z:
    assert z.testzip() is None
    assert len(z.namelist())==206
    for name in z.namelist():
        b=z.read(name)
        assert (OLD/name).read_bytes()==b, name
        baseline.append({"path":name,"bytes":len(b),"sha256":sha(b)})
        if name.startswith(("evidence/","handoff/")) or name in [
            "manuscript.tex","universe_sections.tex","closing_sections.tex","references.bib",
            "CLAIM_EVIDENCE_MATRIX.md","EVIDENCE_INDEX.md","EVIDENCE_COPY_MANIFEST.json",
            "RECONSTRUCTION_SCOPE_AND_REMAINING_GAPS.md",
            "methods/build_pdf.py","methods/render_pdf.py"]:
            dest=ROOT/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
        # Preserve old manuscript, source and all old root-level review records.
        if "/" not in name or name.startswith("qa/"):
            dest=ROOT/"baseline"/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
inputs=[]
for name in ["SRG_SIM06_SIM07_MANUSCRIPT_CODEX_HANDOFF_20261025.zip","SOURCE_READBACK_E01_E02.md"]:
    f=DOWNLOAD/name;inputs.append({"path":str(f),**ident(f)})
(ROOT/"r1_input").mkdir(exist_ok=True)
shutil.copyfile(DOWNLOAD/"SOURCE_READBACK_E01_E02.md",ROOT/"r1_input/SOURCE_READBACK_E01_E02.md")
dump("R1_INPUT_BASELINE.json",{
    "scope":"All 206 prior review ZIP members against existing candidate files, prior ZIP and two actual external attachments; no whole-repository audit",
    "prior_directory":str(OLD),"prior_zip":{"path":str(OLD/ZIP),**ident(OLD/ZIP)},
    "prior_review_files":baseline,"external_inputs":inputs,
    "new_revision_directory":str(ROOT),"initial_revision_directory_status":"Absent at CMD listing before preparation",
    "authority":"Current explicit user request authorizes E01-E02. Supplied ZIP is original manuscript order, not a separate R1 order; SOURCE_READBACK_E01_E02.md supplies correction evidence.",
    "cmd_from_first_read":True,"scientific_execution":0
})
p=ROOT/"closing_sections.tex"
b=p.read_bytes()
old=(
    b"Both sources' GRF observer is\r\n"
    b"\\begin{equation}\\label{eq:grf}\r\n"
    b"\\overline{\\mathrm{GRF}}=\\frac1N\\sum_i\\frac1{1+\\norm{V_i}},\r\n"
    b"\\end{equation}\r\n"
    b"not \\(1/(1+\\mean_i\\norm{V_i})\\)."
)
new=(
    b"Both sources use the pointwise diagnostic \\(g_i=1/(1+\\norm{V_i})\\). Universe records its whole-field mean (\\src{U}{243--255}), while Tower II records a separate mean for each nonempty assigned band \\(G_b\\) (\\src{T}{223--237}):\r\n"
    b"\\begin{equation}\\label{eq:grf}\r\n"
    b"\\overline{\\mathrm{GRF}}_{\\mathrm{Universe}}=\\frac1N\\sum_{i=0}^{N-1}g_i,\r\n"
    b"\\qquad \\overline{\\mathrm{GRF}}_{\\mathrm{Tower},b}=\\frac1{|G_b|}\\sum_{i\\in G_b}g_i.\r\n"
    b"\\end{equation}\r\n"
    b"Tower II does not record a whole-field GRF in its global metrics. Each recorded mean averages pointwise reciprocals, not the reciprocal of one plus mean speed over that set."
)
assert b.count(old)==1
p.write_bytes(b.replace(old,new))
p=ROOT/"references.bib";b=p.read_bytes()
lines=b.splitlines(keepends=True)
sel=[i for i,l in enumerate(lines) if l.startswith(b"@misc{s7creview,")]
assert len(sel)==1
i=sel[0];assert lines[i].count(b"note={24 October.")==1
lines[i]=lines[i].replace(b"note={24 October.",b"note={25 October.")
p.write_bytes(b"".join(lines))
diff=[]
changes=[]
for name in ["manuscript.tex","universe_sections.tex","closing_sections.tex","references.bib"]:
    a=(OLD/name).read_bytes();b=(ROOT/name).read_bytes()
    if a!=b:
        changes.append({"path":name,"before":{"bytes":len(a),"sha256":sha(a)},"after":{"bytes":len(b),"sha256":sha(b)}})
        diff.extend(difflib.unified_diff(a.decode("utf-8").splitlines(keepends=True),b.decode("utf-8").splitlines(keepends=True),fromfile="v0.1/"+name,tofile="v0.1-R1/"+name))
assert [x["path"] for x in changes]==["closing_sections.tex","references.bib"]
(ROOT/"R1_EXACT_DIFF.patch").write_bytes("".join(diff).encode("utf-8"))
dump("R1_SOURCE_CHANGE_RECORD.json",{"changed_manuscript_sources":changes,"unchanged":["manuscript.tex","universe_sections.tex"],
    "limits":"E01 GRF aggregation and E02 S7C review date only; title/version and historical preparation disclosure retained",
    "byte_preserving_edits":True,"diff":"R1_EXACT_DIFF.patch"})
# Copy existing document-only toolchain/cache; never modify old cache.
build=ROOT/"build";build.mkdir(exist_ok=True)
for name in ["toolchain","tectonic-cache","cache"]:
    if (OLD/"build"/name).exists():shutil.copytree(OLD/"build"/name,build/name,dirs_exist_ok=False)
print(json.dumps({"prior_review_members_verified":len(baseline),"edited":[x["path"] for x in changes],"external_inputs":inputs},indent=2))

