"""Offline artifact verifier; optional isolated-interpreter smoke for K3c.

Run from the repository. This tool is neither runtime code nor sdist content.
It never installs dependencies, fetches provenance or edits the source tree.
"""
import argparse
from email import policy
from email.parser import BytesParser
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile


def backend_module():
    path = Path(__file__).resolve().parents[1] / "_build_backend.py"
    spec = importlib.util.spec_from_file_location("_distribution_verifier_backend", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_metadata(raw, version):
    data = BytesParser(policy=policy.default).parsebytes(raw)
    expected = {"Name": "trioctagon-physics", "Version": version,
                "Requires-Python": ">=3.11,<3.12", "License-Expression": "Apache-2.0",
                "Author": "Hilmir Frímann Halldórsson"}
    for field, value in expected.items():
        actual = str(data[field])
        # Setuptools canonically reorders equivalent Requires-Python clauses.
        matches = (sorted(actual.split(",")) == sorted(value.split(","))
                   if field == "Requires-Python" else actual == value)
        if not matches or len(data.get_all(field, [])) != 1:
            raise ValueError("distribution metadata mismatch: " + field)
    if data["Metadata-Version"] != "2.4":
        raise ValueError("expected PEP 639 metadata 2.4")
    if set(data.get_all("License-File", [])) != {"LICENSE", "LICENSE_SCOPE.md"}:
        raise ValueError("missing software license/scope metadata")
    if sorted(str(x).replace(" ", "") for x in data.get_all("Requires-Dist", [])) != sorted(
            ("numpy==2.4.4", "sympy==1.14.0", "mpmath==1.3.0")):
        raise ValueError("unexpected runtime dependencies")
    if data.get_all("Project-URL", []) != ["Source, https://github.com/pzychozen/trioctagon-physics"]:
        raise ValueError("project URL mismatch")
    if any(str(x).startswith("License ::") for x in data.get_all("Classifier", [])):
        raise ValueError("deprecated license classifier")
    return {k: str(data[k]) for k in (*expected, "Metadata-Version")}


def verify(source, wheels, sdist):
    backend = backend_module()
    inputs, manifest = backend.capture(Path(source))
    result = {"source": str(Path(source).resolve()), "source_identity": manifest["source"],
              "manifest": manifest, "license_text_sha256": backend.digest(inputs["LICENSE"]),
              "artifacts": [], "installed_package_certified": False, "ci_implemented": False}
    for path in [*wheels, *([] if sdist is None else [sdist])]:
        path = Path(path).resolve()
        contents = backend.archive_contents(path, inputs, manifest)
        wheel = path.suffix == ".whl"
        info, egg, _ = backend.metadata_names(manifest["software"]["package_version"])
        raw_metadata = contents[info + "/METADATA"] if wheel else contents["PKG-INFO"]
        metadata = verify_metadata(raw_metadata, manifest["software"]["package_version"])
        if not wheel:
            verify_metadata(contents[egg + "/PKG-INFO"], manifest["software"]["package_version"])
        for name in ("LICENSE", "LICENSE_SCOPE.md"):
            key = info + "/licenses/" + name if wheel else name
            if contents[key] != inputs[name]:
                raise ValueError("archive changed license/scope text")
        if wheel and info + "/build_input.sha256" in contents:
            if contents[info + "/build_input.sha256"] != manifest["build_input_sha256"].encode("ascii"):
                raise ValueError("prepared metadata provenance mismatch")
        backend.validate_manifest(backend.parse(contents[backend.MANIFEST]), inputs)
        result["artifacts"].append({"path": str(path), "sha256": backend.digest(path.read_bytes()),
            "bytes": path.stat().st_size, "kind": "wheel" if wheel else "sdist", "metadata": metadata,
            "content": sorted(contents), "python_files": [{"path": name, "authoritative": name in backend.MODULES,
                "source_sha256": backend.digest(inputs[name]), "archive_sha256": backend.digest(contents[name])}
                for name in backend.PYTHON_FILES], "content_and_byte_identity": "PASS"})
    return result


INSTALLED_SMOKE = r'''
import hashlib,json,pathlib,sys
from kernel_physics import api as a, _records as records
root=pathlib.Path(a.__file__).resolve().parents[1]
if not root.is_relative_to(pathlib.Path(sys.prefix).resolve()):
    raise RuntimeError("API is not installed under the supplied interpreter prefix")
if (root/'.git').exists() or (root/'papers').exists() or (root/'research').exists():
    raise RuntimeError("installed smoke must be repository independent")
p=a.Parameters(eps=.05,g=.2,phase_strength=.001,k=(1,1,1))
s=a.State(omega=(.2+.3j,-.4+.1j,.1-.2j),update_index=0)
v=a.Provenance(kind='user_supplied',source_id='distribution smoke',source_revision=None,
 locator='explicit software smoke',literal_values={},notes='')
observers=tuple(a.historical_observer(n) for n in ('paper_e_staged_v1','paper_e_ema_v1'))
def run(n):
 return a.run(s,p,topology='triad',updates=n,parameter_provenance=v,initialization_provenance=v,
 observers=observers,readouts=('z_chiral',),diagnostics=('chiral_area_accounting','readout_accounting'))
assert a.step(s,p,topology='triad').update_index==1
a.z_chiral(s.omega)
zero,one=run(0),run(1)
assert a.RunRecord.from_json(one.to_json()).to_json()==one.to_json()
continued=a.resume(one,updates=1)
assert continued.data['samples'][:-1]==one.data['samples']
geometry={}
for name,options in [('C01',{'section_heights':[]}),('D03',{'construction':'regular','s':1})]:
 record=a.get_geometry(name,options=options)
 assert a.GeometryRecord.from_json(record.to_json()).to_json()==record.to_json()
 geometry[name]=record.deterministic_sha256
for name in ('face_state','boundary_response','srg','operating_region'):
 assert 'kernel_physics.'+name not in sys.modules
origins={name:str(pathlib.Path(module.__file__).resolve()) for name,module in sys.modules.items()
 if name.startswith('kernel_physics') and getattr(module,'__file__',None)}
assert all(pathlib.Path(p).is_relative_to(root/'kernel_physics') for p in origins.values())
print(json.dumps({'api_origin':str(a.__file__),'origins':origins,'source':records._implementation(),
 'environment':records._producer_environment(),'zero_update_digest':zero.deterministic_sha256,
 'one_update_digest':one.deterministic_sha256,'geometry_digests':geometry,
 'installed_module_hashes':{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in records._MODULES},
 'smoke':'PASS'}))
'''


def installed_smoke(python):
    with tempfile.TemporaryDirectory(prefix="trioctagon-installed-smoke-") as cwd:
        done = subprocess.run([str(Path(python).resolve()), "-I", "-B", "-c", INSTALLED_SMOKE],
                              cwd=cwd, text=True, capture_output=True, check=True)
        return json.loads(done.stdout)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--wheel", action="append", default=[], type=Path)
    parser.add_argument("--sdist", type=Path)
    parser.add_argument("--report", required=True, type=Path)
    parser.add_argument("--installed-python", type=Path)
    args = parser.parse_args()
    if not args.wheel and args.sdist is None:
        parser.error("provide at least one wheel or sdist")
    report_path = args.report.resolve()
    if report_path.is_relative_to(args.source.resolve()) or report_path.is_relative_to(Path(__file__).resolve().parents[1]):
        parser.error("report must be outside source and the verifier repository")
    result = verify(args.source, args.wheel, args.sdist)
    if args.installed_python:
        smoke = installed_smoke(args.installed_python)
        if smoke["source"]["commit"] != result["source_identity"]["commit"] or smoke["installed_module_hashes"] != {
                m["path"]: m["sha256"] for m in result["manifest"]["modules"]}:
            raise ValueError("installed identity differs from verified artifacts")
        result["installed_smoke"] = smoke
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(json.dumps({"report": str(report_path), "artifacts": len(result["artifacts"]), "verification": "PASS"}))


if __name__ == "__main__":
    main()
