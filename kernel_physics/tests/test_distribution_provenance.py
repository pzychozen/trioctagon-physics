"""K3b software gates; no mathematical oracle or scientific source mutation."""
import copy
from contextlib import contextmanager
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import tomllib
import unittest
import zipfile
from unittest.mock import patch

import _build_backend as build
from kernel_physics import api as a, _records as records
from tools import verify_distribution as verifier

ROOT = Path(__file__).resolve().parents[2]


def run_record():
    p = a.Parameters(eps=.05, g=.2, phase_strength=.001, k=(1, 1, 1))
    s = a.State(omega=(.2+.3j, -.4+.1j, .1-.2j), update_index=0)
    v = a.Provenance(kind="user_supplied", source_id="distribution test", source_revision=None,
                     locator="explicit test inputs", literal_values={}, notes="")
    return a.run(s, p, topology="triad", updates=1, parameter_provenance=v,
                 initialization_provenance=v, observers=(a.historical_observer("paper_e_ema_v1"),),
                 readouts=("z_chiral",), diagnostics=("chiral_area_accounting",))


class DistributionProvenanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inputs, cls.manifest = build.capture(ROOT)
        cls.source_run = run_record()
        cls.source_geometry = a.get_geometry("C01", options={"section_heights": []})
        cls.source_d = a.get_geometry("D03", options={"construction": "regular", "s": 1})

    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix="trioctagon-provenance-test-")
        self.addCleanup(temp.cleanup)
        self.parent = Path(temp.name)
        self.root = self.parent / "files-only"
        for name in build.PYTHON_FILES:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(self.inputs[name])
        self.data = copy.deepcopy(self.manifest)
        self.save()
        self.root_patch = patch.object(records, "_ROOT", self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)

    def save(self, reseal=False):
        if reseal:
            self.data["build_input_sha256"] = build.input_digest(self.data)
        (self.root / build.MANIFEST).write_bytes(build.canonical(self.data))

    def rejected(self, mutate, reseal=True):
        self.data = copy.deepcopy(self.manifest)
        mutate(self.data)
        self.save(reseal)
        with self.assertRaises((ValueError, TypeError, KeyError, OSError)):
            records._distribution_manifest()
        with self.assertRaises((ValueError, TypeError, KeyError, OSError)):
            build.validate_manifest(self.data, self.inputs)

    def test_valid_manifest_both_validators(self):
        self.assertEqual(records._distribution_manifest(), self.manifest)
        self.assertEqual(build.validate_manifest(self.data, self.inputs), self.manifest)

    def test_canonical_hash_and_key_order(self):
        payload = {k: v for k, v in self.data.items() if k != "build_input_sha256"}
        raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()
        self.assertEqual(hashlib.sha256(raw).hexdigest(), self.data["build_input_sha256"])
        (self.root / build.MANIFEST).write_text(json.dumps(dict(reversed(list(self.data.items()))), indent=3), encoding="utf-8")
        self.assertEqual(records._distribution_manifest(), self.manifest)

    def test_missing_manifest(self):
        (self.root / build.MANIFEST).unlink()
        with self.assertRaises(FileNotFoundError):
            records._implementation()

    def test_unknown_fields_at_all_levels(self):
        for key in (None, "source", "software", "build", "modules", "papers"):
            with self.subTest(key=key):
                def mutate(d):
                    target = d if key is None else d[key][0] if key in ("modules", "papers") else d[key]
                    target["unknown"] = True
                self.rejected(mutate)

    def test_missing_fields_at_all_levels(self):
        for key, field in ((None, "papers"), ("source", "commit"), ("software", "ledger_version"),
                           ("build", "backend"), ("modules", "sha256"), ("papers", "edition")):
            with self.subTest(key=key):
                def mutate(d):
                    target = d if key is None else d[key][0] if key in ("modules", "papers") else d[key]
                    del target[field]
                self.rejected(mutate)

    def test_wrong_type_and_version(self):
        for key, value in (("manifest_type", "other"), ("manifest_version", "2"), ("manifest_version", 1)):
            with self.subTest(key=key, value=value):
                self.rejected(lambda d: d.__setitem__(key, value))

    def test_source_commit_and_clean_attestation(self):
        for key, value in (("commit", "HEAD"), ("commit", "a"*39), ("commit", "A"*40),
                           ("tracked_dirty", True), ("tracked_dirty", 0), ("repository", "")):
            with self.subTest(key=key, value=value):
                self.rejected(lambda d: d["source"].__setitem__(key, value))

    def test_bad_sha256_and_digest(self):
        self.rejected(lambda d: d["modules"][0].__setitem__("sha256", "bad"))
        self.rejected(lambda d: d["papers"][0].__setitem__("sha256", "X"*64))
        self.rejected(lambda d: d.__setitem__("build_input_sha256", "0"*64), reseal=False)

    def test_module_set_and_order(self):
        self.rejected(lambda d: d["modules"].pop())
        self.rejected(lambda d: d["modules"].reverse())
        self.rejected(lambda d: d["modules"][0].__setitem__("path", "../escape.py"))

    def test_paper_set_identity_and_order(self):
        self.rejected(lambda d: d["papers"].pop())
        self.rejected(lambda d: d["papers"].reverse())
        for key, value in (("source_id", "PX"), ("edition", "new"), ("path", "papers/other.md")):
            self.rejected(lambda d: d["papers"][0].__setitem__(key, value))

    def test_all_software_namespaces(self):
        for key in self.data["software"]:
            with self.subTest(key=key):
                self.rejected(lambda d: d["software"].__setitem__(key, "99"))

    def test_build_facts_and_input_set(self):
        self.rejected(lambda d: d["build"].__setitem__("backend", "other"))
        self.rejected(lambda d: d["build"]["files"].reverse())
        self.rejected(lambda d: d["build"]["files"].pop())
        self.rejected(lambda d: d["build"]["files"][0].__setitem__("sha256", "bad"))

    def test_conflicting_module_and_input_hashes(self):
        name = self.data["modules"][0]["path"]
        self.rejected(lambda d: next(e for e in d["build"]["files"] if e["path"]==name).__setitem__("sha256", "0"*64))

    def test_duplicate_json_and_nonfinite_rejected(self):
        for raw in ('{"a":1,"a":2}', '{"a":NaN}', '{"a":Infinity}'):
            (self.root / build.MANIFEST).write_text(raw)
            with self.assertRaises(ValueError):
                records._distribution_manifest()
            with self.assertRaises(ValueError):
                build.parse(raw)

    def test_tampered_installed_module_no_cached_trust(self):
        records._implementation()
        (self.root / build.MODULES[0]).write_bytes(b"# altered\n")
        with self.assertRaisesRegex(ValueError, "installed module bytes"):
            records._implementation()

    def test_missing_installed_module(self):
        (self.root / build.MODULES[0]).unlink()
        with self.assertRaises(OSError):
            records._implementation()

    def test_cwd_independence(self):
        with patch("pathlib.Path.cwd", side_effect=AssertionError("cwd must not own provenance")):
            self.assertEqual(records._implementation()["commit"], self.manifest["source"]["commit"])

    def test_unrelated_containing_git(self):
        subprocess.run(["git", "init", "-q", str(self.parent)], check=True, capture_output=True)
        self.assertFalse(records._source_checkout())
        self.assertEqual(records._implementation()["repository"], self.manifest["source"]["repository"])

    def test_incomplete_exact_git_cannot_fall_back(self):
        subprocess.run(["git", "init", "-q", str(self.root)], check=True, capture_output=True)
        self.assertTrue(records._source_checkout())
        with self.assertRaises(ValueError):
            records._implementation()
        with self.assertRaises((ValueError, subprocess.CalledProcessError)):
            build.capture(self.root)

    def test_broken_git_cannot_fall_back(self):
        (self.root / ".git").write_text("invalid gitdir\n")
        with self.assertRaises(ValueError):
            records._implementation()

    def test_source_mode_remains_live(self):
        with patch.object(records, "_ROOT", ROOT), patch.object(records, "_distribution_manifest", side_effect=AssertionError("no fallback")):
            impl = records._implementation()
            self.assertEqual(impl["commit"], subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip())
            self.assertEqual(impl["modules"], self.manifest["modules"])

    def test_dirty_live_source_cannot_fall_back(self):
        real = records._provenance_git
        def git(*args):
            return " M kernel_physics/_records.py" if args[0]=="status" else real(*args)
        with patch.object(records, "_ROOT", ROOT), patch.object(records, "_provenance_git", side_effect=git):
            with self.assertRaisesRegex(ValueError, "clean, complete"):
                records._implementation()

    def test_missing_live_papers_cannot_fall_back(self):
        original = Path.is_file
        def is_file(path):
            return False if "papers" in path.parts else original(path)
        with patch.object(records, "_ROOT", ROOT), patch.object(Path, "is_file", is_file):
            with self.assertRaisesRegex(ValueError, "evidence is missing"):
                records._implementation()
            with self.assertRaises(ValueError):
                records._papers(("A",))

    def test_same_implementation_schema(self):
        impl = records._implementation()
        self.assertEqual(set(impl), {"repository", "commit", "package_version", "api_version", "modules", "tracked_dirty"})
        self.assertEqual(impl, dict(self.source_run.data["implementation"]) | {"modules": self.manifest["modules"]})
        self.assertEqual(len(records._MODULES), 14)

    def test_paper_metadata_without_paper_files(self):
        self.assertFalse((self.root / "papers").exists())
        self.assertEqual(records._papers("CAAC"), [p for p in self.manifest["papers"] if p["source_id"] in ("PA", "PC")])
        with self.assertRaises(ValueError):
            records._papers(("X",))

    def test_source_manifest_run_record_parity(self):
        installed = run_record()
        self.assertEqual(installed.to_json(), self.source_run.to_json())
        self.assertEqual(installed.deterministic_sha256, self.source_run.deterministic_sha256)

    def test_source_manifest_geometry_parity(self):
        for name, options, source in (("C01", {"section_heights": []}, self.source_geometry),
                                      ("D03", {"construction": "regular", "s": 1}, self.source_d)):
            record = a.get_geometry(name, options=options)
            self.assertEqual(record.to_json(), source.to_json())
            self.assertEqual(record.deterministic_sha256, source.deterministic_sha256)

    def test_decode_needs_neither_manifest_nor_repository(self):
        (self.root / build.MANIFEST).unlink()
        with patch.object(records, "_implementation", side_effect=AssertionError("decode must be inert")):
            self.assertEqual(a.RunRecord.from_json(self.source_run.to_json()).to_json(), self.source_run.to_json())
            self.assertEqual(a.GeometryRecord.from_json(self.source_geometry.to_json()).to_json(), self.source_geometry.to_json())

    def test_resume_same_identity_and_changed_commit(self):
        continued = a.resume(self.source_run, updates=1)
        self.assertEqual(continued.data["samples"][:-1], self.source_run.data["samples"])
        self.data["source"]["commit"] = "0"*40
        self.save(reseal=True)
        with self.assertRaisesRegex(ValueError, "matching source revision"):
            a.resume(self.source_run, updates=1)

    def test_resume_changed_module_identity(self):
        name = "kernel_physics/readouts.py"
        (self.root / name).write_bytes(self.inputs[name]+b"\n# changed implementation identity\n")
        sha = build.digest((self.root / name).read_bytes())
        for row in self.data["modules"]+self.data["build"]["files"]:
            if row["path"]==name:
                row["sha256"]=sha
        self.save(reseal=True)
        with self.assertRaisesRegex(ValueError, "matching source revision"):
            a.resume(self.source_run, updates=1)

    def test_fresh_package_only_process_boundary(self):
        code = """import json,pathlib,sys
from kernel_physics import api as a, _records as r
assert pathlib.Path(a.__file__).resolve().parents[1]==pathlib.Path.cwd()
p=a.Parameters(eps=.05,g=.2,phase_strength=.001,k=(1,1,1))
s=a.State(omega=(.2+.3j,-.4+.1j,.1-.2j),update_index=0)
v=a.Provenance(kind='user_supplied',source_id='test',source_revision=None,locator='test',literal_values={},notes='')
record=a.run(s,p,topology='triad',updates=0,parameter_provenance=v,initialization_provenance=v,observers=(),readouts=(),diagnostics=())
geometry=a.get_geometry('D03',options={'construction':'regular','s':1})
assert a.RunRecord.from_json(record.to_json()).to_json()==record.to_json()
assert not any('kernel_physics.'+n in sys.modules for n in ('face_state','srg','operating_region','boundary_response'))
print(json.dumps({'commit':r._implementation()['commit'],'record':record.deterministic_sha256,'geometry':geometry.deterministic_sha256}))
"""
        done = subprocess.run([sys.executable, "-B", "-c", code], cwd=self.root, text=True, capture_output=True, check=True)
        self.assertEqual(json.loads(done.stdout)["commit"], self.manifest["source"]["commit"])

    def test_license_standard_text_and_scope(self):
        self.assertEqual(hashlib.sha256(self.inputs["LICENSE"]).hexdigest(), "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30")
        build.validate_project(self.inputs)
        for name in ("LICENSE", "LICENSE_SCOPE.md"):
            bad = dict(self.inputs, **{name:b"not the approved license/scope"})
            with self.assertRaises(ValueError):
                build.validate_project(bad)

    def test_pyproject_contract(self):
        data = tomllib.loads(self.inputs["pyproject.toml"].decode())
        build.validate_project(self.inputs)
        self.assertEqual(data["project"]["dependencies"], (ROOT/"kernel_physics/requirements.txt").read_text().splitlines())
        self.assertEqual(data["tool"]["setuptools"]["packages"], ["kernel_physics"])
        self.assertEqual(data["tool"]["setuptools"]["dynamic"]["version"], {"attr":"kernel_physics.__version__"})

    def test_build_source_dirty_rejected(self):
        real = build.git
        def git(root,*args):
            return b" M kernel_physics/_records.py" if args[0]=="status" else real(root,*args)
        with patch.object(build, "git", side_effect=git):
            with self.assertRaisesRegex(ValueError, "clean complete"):
                build.capture(ROOT)

    def test_sdist_mode_checks_all_19_and_build_inputs(self):
        for name, raw in self.inputs.items():
            path=self.root/name
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_bytes(raw)
        self.assertEqual(build.capture(self.root)[1], self.manifest)
        (self.root/"kernel_physics/face_state.py").write_bytes(b"changed")
        with self.assertRaisesRegex(ValueError, "byte identity"):
            build.capture(self.root)

    def test_metadata_identity_change_rejected_before_delegate(self):
        metadata = self.parent/"metadata"/"trioctagon_physics-0.1.0.dist-info"
        metadata.mkdir(parents=True)
        (metadata/"build_input.sha256").write_text("0"*64)
        @contextmanager
        def stage():
            yield None, self.inputs, self.manifest
        with patch.object(build, "staged", stage):
            with self.assertRaisesRegex(ValueError, "identity changed"):
                build.build_wheel(self.parent/"wheels", metadata_directory=metadata)

    def test_output_and_configuration_boundaries(self):
        with self.assertRaises(ValueError):
            build.destination(ROOT/"dist")
        with self.assertRaises(ValueError):
            build.get_requires_for_build_wheel({"--global-option":"anything"})

    def test_verifier_accepts_canonical_metadata_order(self):
        raw = ("Metadata-Version: 2.4\nName: trioctagon-physics\nVersion: 0.1.0\n"
               "Author: Hilmir Frímann Halldórsson\nRequires-Python: <3.12,>=3.11\n"
               "License-Expression: Apache-2.0\nLicense-File: LICENSE\nLicense-File: LICENSE_SCOPE.md\n"
               "Project-URL: Source, https://github.com/pzychozen/trioctagon-physics\n"
               "Requires-Dist: numpy==2.4.4\nRequires-Dist: sympy==1.14.0\nRequires-Dist: mpmath==1.3.0\n\n").encode()
        verifier.verify_metadata(raw, "0.1.0")
        with self.assertRaises(ValueError):
            verifier.verify_metadata(raw.replace(b"<3.12", b"<3.13"), "0.1.0")

    def test_archive_rejects_leaked_files_and_directories(self):
        info = build.metadata_names(self.manifest["software"]["package_version"])[0]
        payload = {p: self.inputs[p] for p in build.PYTHON_FILES}
        payload[build.MANIFEST] = build.canonical(self.manifest)
        payload.update({info+"/"+p:b"" for p in ("METADATA","WHEEL","RECORD","top_level.txt","licenses/LICENSE","licenses/LICENSE_SCOPE.md")})
        path=self.parent/"test.whl"
        for forbidden in ("papers/source.md", "kernel_physics/tests/test.py", "research/", "../escape"):
            with self.subTest(path=forbidden):
                with zipfile.ZipFile(path,"w") as archive:
                    for name,raw in {**payload,forbidden:b""}.items():
                        archive.writestr(name,raw)
                with self.assertRaises(ValueError):
                    build.archive_contents(path,self.inputs,self.manifest)

    def test_archive_rejects_source_transformation(self):
        info = build.metadata_names(self.manifest["software"]["package_version"])[0]
        payload = {p: self.inputs[p] for p in build.PYTHON_FILES}
        payload[build.MANIFEST] = build.canonical(self.manifest)
        payload.update({info+"/"+p:b"" for p in ("METADATA","WHEEL","RECORD","top_level.txt","licenses/LICENSE","licenses/LICENSE_SCOPE.md")})
        payload["kernel_physics/readouts.py"] += b"\n"
        path=self.parent/"changed.whl"
        with zipfile.ZipFile(path,"w") as archive:
            for name,raw in payload.items():
                archive.writestr(name,raw)
        with self.assertRaisesRegex(ValueError,"changed Python bytes"):
            build.archive_contents(path,self.inputs,self.manifest)


if __name__ == "__main__":
    unittest.main()
