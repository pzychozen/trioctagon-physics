# K3a — Distribution and clean-install contract freeze (R1)

**26 September 2026 — PASS. SG8 resolved by explicit human authority.** K3a-R1 freezes the software-only Apache-2.0 decision, naming/metadata, engineering version/support lane, provenance/content, clean-install and CI contracts in exactly the two K3a receipts. K3b implementation has not started. No runtime, existing test, package metadata, license file, version, paper, research or CI file is changed or created by this freeze.

Authoritative starting HEAD and pre-publication observed origin/main: `d76321a54f6f3a8ee1f0175ac6a4db6d0c017117`. K0/K1 remain PASS and K2 remains FINAL PASS. Original K3a evidence is retained: **298 tracked tests passed in 200.097 seconds** under torment. R1 does not rerun broad archaeology, tests or build/install experiments. Final publication HEAD is the commit containing these two receipts; its actual SHA and remote equality are verified and returned in closeout.

## 1. Required return and authority transition

```text
ATTEMPT_1 = HOLD_SG8
R1 = HUMAN_DECISION_SUPPLIED
FINAL_K3A = PASS
```

The original K3a attempt correctly stopped because software licensing/publication authority was missing. It created only these two uncommitted receipts, made no implementation change and performed no commit/push. That historical HOLD is retained in JSON `history.ATTEMPT_1`, including its status, stop gate, licensing facts, decisions requested, conditional scope and preservation record. The original receipt SHA-256 values are `75ae53e8f390dd5fbb737e97baa5d12efd6c78cd16149089532f50439dcdd014` (Markdown) and `5ef264bc1561c47810098a6bc5e6e7ac5e7aaf1728785b70967c8e9d98df6ab7` (JSON). R1 resolves the authority decision; it does not retroactively change the first attempt or its evidence.

```text
STARTING_HEAD = d76321a54f6f3a8ee1f0175ac6a4db6d0c017117
FINAL_HEAD = CONTAINING_K3A_R1_COMMIT
ORIGIN_MAIN = POST_PUSH_MATCH_TO_CONTAINING_COMMIT_TO_BE_REPORTED_IN_CLOSEOUT
K3A_STATUS = PASS
CURRENT_PACKAGE_METADATA = ABSENT_BUILD_METADATA; KERNEL_REQUIREMENTS_AND_INHERITED_VERSION_PRESENT
CURRENT_WHEEL_BUILD = NOT_IMPLEMENTED
CURRENT_SDIST_BUILD = NOT_IMPLEMENTED
CURRENT_INSTALLED_PACKAGE_SMOKE = NOT_YET_IMPLEMENTABLE
PUBLIC_API_IMPORT_CLEAN_CHECKOUT = PASS
PUBLIC_API_IMPORT_INSTALLED = NOT_YET_IMPLEMENTABLE
RUNTIME_DEPENDENCIES = numpy, sympy, mpmath
TEST_ONLY_DEPENDENCIES = No additional third-party packages; unittest and other standard-library test tools; repository fixtures
NETWORK_REQUIRED = NO
MODEL_REQUIRED = NO
RUN_RECORD_WITHOUT_GIT = FAILS
RUN_RECORD_WITHOUT_PAPERS = FAILS
GEOMETRY_RECORD_WITHOUT_GIT = FAILS
GEOMETRY_RECORD_WITHOUT_PAPERS = FAILS
PACKAGED_PROVENANCE_MANIFEST_NEEDED = YES
RUN_RECORD_SCHEMA_CHANGE_NEEDED = NO
GEOMETRY_RECORD_SCHEMA_CHANGE_NEEDED = NO
O01_QUARANTINE_INSTALL_BOUNDARY = PASS
LICENSE_PRESENT = NO
HUMAN_DECISIONS_REQUIRED = NO for K3a freeze; a separate K3b work order and later registry/release decisions remain outside this phase
CLEAN_INSTALL_CONTRACT = FROZEN
CI_CONTRACT = FROZEN
K3B_SCOPE_DEFINED = YES
PRODUCTION_SOURCE_CHANGED = 0
EXISTING_TEST_CHANGED = 0
PACKAGE_METADATA_CHANGED = 0
K0_CHANGED = 0
K1_CHANGED = 0
K2_CHANGED = 0
PAPERS_CHANGED = 0
RESEARCH_CHANGED = 0
FIXTURE_CHANGED = 0
CI_CHANGED = 0
FILES_CREATED = 2
FILES_MODIFIED = 0
K3B_READY_FOR_AUTHORIZATION = YES
ATTEMPT_1 = HOLD_SG8
R1 = HUMAN_DECISION_SUPPLIED
FINAL_K3A = PASS
SG8 = RESOLVED_BY_HUMAN_AUTHORITY
SG8_RESOLUTION = HUMAN_AUTHORITY_SUPPLIED
SOFTWARE_LICENSE = Apache-2.0
SOFTWARE_LICENSE_SCOPE = SOFTWARE_ONLY
LICENSE_AUTHORIZED = YES
LICENSE_SELECTED = Apache-2.0
LICENSE_SCOPE = SOFTWARE_ONLY
LICENSE_CREATION = K3B
LICENSE_FILE_CREATION = DEFERRED_TO_K3B
LICENSE_CREATION_DEFERRED_TO_K3B = YES
DISTRIBUTION_NAME = trioctagon-physics
IMPORT_PACKAGE = kernel_physics
SOURCE_PACKAGE_DIRECTORY = kernel_physics/
GITHUB_REPOSITORY = pzychozen/trioctagon-physics
AUTHOR = Hilmir Frímann Halldórsson
PROJECT_URL = https://github.com/pzychozen/trioctagon-physics
DESCRIPTION_SOURCE = kernel_physics/README.md
PACKAGE_VERSION_POLICY = KEEP_0.1.0_FOR_K3_ENGINEERING
INITIAL_SUPPORT_LANE = Windows / CPython >=3.11,<3.12 / NumPy 2.4.4 / SymPy 1.14.0 / mpmath 1.3.0
PACKAGED_PROVENANCE_MANIFEST = APPROVED
K3B_IMPLEMENTATION_STARTED = NO
```

`LICENSE_PRESENT = NO` and `LICENSE_AUTHORIZED = YES` are intentional: the human decision is frozen now, while `LICENSE` and `LICENSE_SCOPE.md` creation belongs to K3b. The distribution and CI contracts are FROZEN; build/install certification remains NOT_YET_IMPLEMENTABLE until implementation exists. `K3B_READY_FOR_AUTHORIZATION = YES` is readiness for a separate work order, not authority to start it here.

The quarantine PASS remains source/import-graph and package-only evidence, not an installed-wheel result. The schema flags freeze the approved unchanged-schema design, with source/wheel/installed byte equality still requiring future tests. The receipt identifies its future containing commit symbolically because a file cannot embed its own commit SHA without circularity. Exact final HEAD and observed origin/main are returned after commit/push in the task closeout.


The census, dependency closure, experiments and hashes below describe the original K3a source/evidence at the authorized starting HEAD. R1 rechecked the tracked baseline and updates authority/contract status only. Approval of a future feature is not evidence that it has been implemented.

## 2. Complete bounded packaging census

All 706 tracked paths, including hidden paths; supplementary rg --files --hidden nonignored working-tree census. Existing ignored environments/caches are not package authority.

| Item | Current state |
| --- | --- |
| Build metadata/backend/distribution name | Absent: no pyproject.toml, setup.py, setup.cfg or MANIFEST.in |
| Import package/version source | kernel_physics; __init__.py:3 declares 0.1.0 |
| Dependency declaration | kernel_physics/requirements.txt: numpy==2.3.5, sympy==1.14.0, mpmath==1.3.0; not install metadata |
| Separate test dependencies | None declared; unittest is standard library |
| Wheel / sdist configuration | Neither exists; CURRENT_WHEEL_BUILD and CURRENT_SDIST_BUILD = NOT_IMPLEMENTED |
| Environment/test runner configuration | No environment*.yml/yaml, conda*.yml/yaml, tox.ini, noxfile.py or pytest.ini |
| CI | No .github/workflows entries |
| License | No tracked or nonignored license-named file found |
| Package description / project / authors metadata | No distribution fields; README/origin evidence below |
| Archival packaging | tools/package_archive.py transfers original source bytes into an archive; it is not a Python distribution backend and was not run |
| Existing build tools in torment | pip 26.1.2; setuptools 81.0.0; wheel 0.47.0; build module absent. Availability does not imply a tested backend |

The complete tracked requirements-file census is:

- `kernel_physics/requirements.txt`: numpy==2.3.5; sympy==1.14.0; mpmath==1.3.0.
- `papers/PAPER_B/requirements.txt`: sympy==1.14.0; numpy==2.5.3; matplotlib==3.10.7; contourpy==1.4.0; cycler==0.12.1; fonttools==4.65.0; kiwisolver==1.5.1; packaging==26.3; pillow==12.3.0; pyparsing==3.3.3; python-dateutil==2.9.0.post0; six==1.17.0; mpmath==1.3.0; pypdf==6.10.0.
- `papers/PAPER_B/reviewed_v0.1/requirements.txt`: sympy==1.14.0; numpy==2.5.3; matplotlib==3.10.7; contourpy==1.4.0; cycler==0.12.1; fonttools==4.65.0; kiwisolver==1.5.1; packaging==26.3; pillow==12.3.0; pyparsing==3.3.3; python-dateutil==2.9.0.post0; six==1.17.0; mpmath==1.3.0; pypdf==6.10.0.
- `papers/PAPER_D/requirements.txt`: sympy==1.14.0; numpy==2.5.3; matplotlib==3.10.7; Pillow==12.3.0; pypdf==6.10.0.
- `papers/PAPER_D/v0.1.1/requirements.txt`: sympy==1.14.0; numpy==2.5.3; matplotlib==3.10.7; Pillow==12.3.0; pypdf==6.10.0.

The supplementary working-tree census found only two further requirement files: `research_notes/reference_scaffold/requirements.txt` (reportlab, Pillow) and `research_files/verification/quantum_modes_phase1/requirements.lock.txt` (scientific/plotting environment). Both are untracked research material; neither is package authority. Full contents are retained in JSON. All tracked README locations are also enumerated there. No inferred historical requirement is installed or adopted.

## 3. Public runtime import closure

Starting only at `kernel_physics.api`, AST inspection resolves **14 project modules**, including package initialization and function-local imports. Every import statement, source line, target and classification appears in JSON. Internal project edges are classified as REQUIRED_RUNTIME_DEPENDENCY with project ownership, not as additional pip packages. This is the complete project import closure plus third-party distribution requirements, not an enumeration of every internal SymPy/NumPy standard-library import.

| Project module | Direct project imports | Direct third-party imports | Direct STDLIB imports |
| --- | --- | --- | --- |
| __init__ | none | none | none |
| _contract_types | _response_numeric, dynamics, z_manifold | numpy | collections.abc, dataclasses, numbers, types |
| _geometry_records | _contract_types, _records, geometry, reference_scaffold | sympy | collections.abc, fractions, functools, math, numbers |
| _presets | _contract_types | none | none |
| _records | __init__, _contract_types, _presets, z_diagnostics | mpmath, numpy, sympy | collections.abc, dataclasses, hashlib, json, math, pathlib, platform, re, subprocess, sys, types |
| _response_numeric | none | numpy | math, numbers, sys |
| _runner | _contract_types, _presets, _records, dynamics, readouts, z_diagnostics, z_manifold | none | dataclasses |
| api | _contract_types, _geometry_records, _presets, _records, _response_numeric, _runner, readouts, z_diagnostics, z_manifold | none | none |
| dynamics | none | numpy | dataclasses, math |
| geometry | none | sympy | collections, dataclasses |
| readouts | _response_numeric | numpy | none |
| reference_scaffold | none | sympy | dataclasses, fractions |
| z_diagnostics | _response_numeric, dynamics, readouts, z_manifold | numpy | dataclasses, math |
| z_manifold | _response_numeric, readouts | numpy | dataclasses, math, numbers |

**REQUIRED_RUNTIME_DEPENDENCY:** NumPy, SymPy, mpmath. Each was separately blocked in a fresh process; facade import failed in all three cases. mpmath is imported eagerly by `_records.py` for producer-version metadata and is also SymPy’s required dependency. It cannot honestly be called test-only in this implementation even though the recurrence does not evaluate with it.

**STDLIB:** `collections`, `collections.abc`, `dataclasses`, `fractions`, `functools`, `hashlib`, `json`, `math`, `numbers`, `pathlib`, `platform`, `re`, `subprocess`, `sys`, `types`.

**OPTIONAL_RUNTIME_DEPENDENCY:** no optional third-party dependency is selected by this facade. `covering` is an accepted internal opt-in module; `face_state` is legacy opt-in. **QUARANTINED:** `boundary_response`, `srg`, `operating_region`. **TEST_ONLY:** standard-library unittest/mock/AST/fixture support and test oracle modules; no extra third-party package. **RESEARCH_ONLY:** plotting/PDF/scipy/reportlab and other requirements outside kernel requirements; not imported by the public closure. Optional development/docs/gmpy extras in third-party metadata are not promoted to kernel runtime requirements.

| Operation | Direct work after facade import |
| --- | --- |
| import kernel_physics.api | Eagerly imports all three libraries through the 14-module closure. |
| Parameters / State | NumPy type checks and detached validated vectors; no Git or paper access. |
| step / raw z_chiral | NumPy numerical owners and shared checks; no symbolic recurrence or mpmath evaluation. |
| observers / diagnostics | NumPy accepted observer/readout/diagnostic owners. |
| RunRecord production | NumPy codec and numerical values; records versions of NumPy, SymPy and mpmath; requires Git and selected paper bytes today. |
| GeometryRecord production | SymPy exact constructors/codec; shared NumPy-aware codec; all three producer versions; Git and paper bytes today. |
| RunRecord decoding | Structural and binary64 validation, immutable value checks, no equations advanced or provenance files read. |
| GeometryRecord decoding | SymPy exact-tree and rendering validation; no geometry constructor run and no Git/paper reads. |

All operations through the facade require all three libraries to be installed because import is eager. This is distinct from which library evaluates a specific operation. NumPy 2.4.4 locally declares Python >=3.11; SymPy 1.14.0 declares Python >=3.9 and mpmath>=1.1.0,<1.4. NumPy has no further Requires-Dist entries; mpmath has no non-extra Requires-Dist entries. No new runtime dependency is needed for the approved JSON provenance fallback.

## 4. Quarantine, FaceState and network/model boundary

O01 remains CLOSED_OPTION_B_QUARANTINE_V1. A normal whole-package build would physically ship all **19 top-level Python files (150,914 raw bytes at this HEAD)**, including the three quarantined modules, covering and FaceState. The approved content contract retains them as internal files. SHIPPED_INTERNAL_FILE does not imply SUPPORTED_PUBLIC_API. The API and Runner expose no selection for the quarantined modules; none of the four forbidden modules appeared in any probe’s sys.modules.

FaceState can remain opt-in without an eager export. An explicit FaceState import reaches operating_region and its quarantine dependencies; this is existing internal behavior, not facade activation. Do not delete or split it during packaging. Existing tracked tests deliberately exercise internal/quarantine paths and do not confer public support.

NORMAL_KERNEL_RUNTIME_NETWORK_REQUIRED = NO; LLM_REQUIRED = NO; EMBEDDING_MODEL_REQUIRED = NO; GPU_REQUIRED = NO. Import and call inspection found no HTTP client, remote paper fetch, package installer, Git fetch/clone/pull, model loader or GPU subsystem in the facade closure. The only subprocess path reads local Git metadata. Four fresh-process probes installed a network audit guard and attempted zero network events. The task’s separate `git ls-remote` verified origin/main; it was not a kernel call. These observations are scoped to supported operations, not all research files.

## 5. Current provenance acquisition

| Field | Source classification | Evidence and meaning |
| --- | --- | --- |
| implementation.repository | GIT_METADATA | _records.py:250 — git remote get-url origin; local configuration only, no remote contact |
| implementation.commit | GIT_METADATA | _records.py:248 — git rev-parse HEAD; exact repository-root check first |
| implementation.tracked_dirty | GIT_METADATA | _records.py:249-255 — git status --porcelain --untracked-files=no OR any of the 14 required modules absent from git ls-files |
| implementation.modules[].sha256 | REPOSITORY_FILE | _records.py:252-253 — SHA-256 of raw .py bytes at _ROOT / frozen relative path; not Git blob SHA-1, pyc bytes or normalized text |
| implementation.modules[].path | HARDCODED/FROZEN DEFINITION | _records.py:29-33 — Sorted exact 14-path _MODULES list, also enforced by decoder |
| paper_references[].source_id/edition/path | HARDCODED/FROZEN DEFINITION | _records.py:34-41,258-261 — _PAPERS has six accepted locators; ID selection follows Runner definitions or C/D request |
| paper_references[].sha256 | REPOSITORY_FILE | _records.py:260 — Raw paper source bytes read at production time; not needed for decoding |
| implementation.package_version | HARDCODED/FROZEN DEFINITION | __init__.py:3; _records.py:251 — __version__, not distribution metadata; inherited 0.1.0 |
| API/schema/ledger versions | HARDCODED/FROZEN DEFINITION | _records.py:22,286-296; _runner.py:134-135; _geometry_records.py:206-207 — 1.0.0 / 1.0.0 / 0.1 |
| execution_metadata | RUNTIME_ENVIRONMENT | _records.py:264-278 — Python and all three library versions, platform, architecture and byte order |
| preset provenance | HARDCODED/FROZEN DEFINITION | _presets.py:4-5 — Frozen K0 revision and repo-relative locator strings; no file opened |
| construction_provenance.source_revision | GIT_METADATA | _geometry_records.py:202-205 — Uses implementation.commit; locator/literal definition metadata is frozen code |

`_ROOT = Path(__file__).resolve().parent.parent` assumes the package parent is its repository root. `_implementation()` first verifies the Git top-level equals this root. Thus installing inside some unrelated Git checkout does not legitimately provide provenance. Module hashes are currently raw repository-file hashes; the same bytes can be read in a package-only directory, but existing production fails before returning them when Git is absent.

The exact six paper references and raw source hashes at this HEAD are:

| Paper / edition | Repository-relative locator | SHA-256 |
| --- | --- | --- |
| A / publication | papers/PAPER_A/publication/paper_A_publication.md | 5fc388072d344c10d201b8eff255226b861014ff980e64c06811ae973bf7cd55 |
| B / 0.1.2 | papers/PAPER_B/publication/v0.1.2/PAPER_B_TRIADIC_CHIRALITY_AND_ORIENTATION_GEOMETRY_PUBLICATION_v0.1.2.md | fb4575120470e8d7143ebc1f475ee4635caf9f39f21f88308960308fb259e150 |
| C / 1.0.1 | papers/PAPER_C/publication/v1.0.1/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_PUBLICATION_v1.0.1.md | 5a0cbdae4aaf689cfe1f5b29305960e90c88e26d0db28834802ef70fc16549fb |
| D / 0.1.1 | papers/PAPER_D/v0.1.1/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md | 7bc87de09400ba1a37d5dc9ab7be38c9a978be31bb35ece56102d29ee2e5d25b |
| E / 0.1.1 | papers/PAPER_E/v0.1.1/PAPER_E_Z_MANIFOLD_v0.1.1.md | a79bc29d991c3af8bba546f0bc5e1ff7a6bbe5501d8adf2ef6d19c66b362978d |
| F / 0.2 | papers/PAPER_F/PAPER_F_PUBLICATION_v0.2.md | 8c9419b20a0899857e68f4b191e7321cfc99f5286f149504f5d82a3e75db4fd5 |

Paper A’s schema edition is literally `publication`, not an inferred PDF version. Hashes/locators are provenance; their paper source bytes need not be runtime data. Parameter/initialization/preset descriptors are already self-contained strings and values.

## 6. Clean checkout and missing-context experiments

Fresh detached tracked worktree: `C:\Users\Notandi\AppData\Local\Temp\kernel-k3a-oi85dcis\tracked-checkout`. It contains exactly the authorized 706 tracked files and no untracked material. All source bytes match the authoritative baseline; git status was clean before and after. Interpreter: `C:\Users\Notandi\miniconda3\envs\torment\python.exe`, Python 3.11.15, NumPy 2.4.4, SymPy 1.14.0, mpmath 1.3.0. The authoritative environment was not modified.

```text
python -B -m unittest discover -s kernel_physics/tests -t . -p "test_*.py" -v
298 tests; 200.097 seconds; OK
```

API_IMPORT_FROM_REPO_ROOT = PASS; RECORD_PRODUCTION_IN_CLEAN_GIT_CHECKOUT = PASS; GEOMETRY_RECORD_PRODUCTION_IN_CLEAN_GIT_CHECKOUT = PASS. Zero/one-update records, both observers, C01, D03, exact JSON round-trips and compatible resume passed. This is source-checkout validation, not installation.

Three separate external controls copied the raw package files or used a second disposable worktree. The package-only folder contains just the 19 Python files, without .git, papers, research or tests. A second copy adds only the six referenced paper sources but no Git. A separate temporary Git worktree has its papers moved outside that checkout (deliberately tracked-dirty); the original clean worktree remains unchanged. All import origins were checked. No PYTHONPATH was set and no copied folder is called an installation.

| Operation | Clean Git + papers | No Git, papers present | Git, no papers | Package only: neither |
| --- | --- | --- | --- | --- |
| api_import | WORKS | WORKS | WORKS | WORKS |
| Parameters | WORKS | WORKS | WORKS | WORKS |
| State | WORKS | WORKS | WORKS | WORKS |
| step | WORKS | WORKS | WORKS | WORKS |
| z_chiral | WORKS | WORKS | WORKS | WORKS |
| observe_staged | WORKS | WORKS | WORKS | WORKS |
| observe_ema | WORKS | WORKS | WORKS | WORKS |
| advance_clock | WORKS | WORKS | WORKS | WORKS |
| advance_ema | WORKS | WORKS | WORKS | WORKS |
| diagnostics | WORKS | WORKS | WORKS | WORKS |
| RunRecord_zero_update | WORKS | FAILS | FAILS | FAILS |
| RunRecord_one_update | WORKS | FAILS | FAILS | FAILS |
| RunRecord_observers | WORKS | FAILS | FAILS | FAILS |
| GeometryRecord_C01 | WORKS | FAILS | FAILS | FAILS |
| GeometryRecord_D03 | WORKS | FAILS | FAILS | FAILS |
| RunRecord_one_update_decode | WORKS | WORKS | WORKS | WORKS |
| resume | WORKS | FAILS | WORKS | FAILS |
| GeometryRecord_C01_decode | WORKS | WORKS | WORKS | WORKS |
| GeometryRecord_D03_decode | WORKS | WORKS | WORKS | WORKS |
| implementation_capture | WORKS | FAILS | WORKS | FAILS |
| paper_capture_all | WORKS | WORKS | FAILS | FAILS |

The `RunRecord_*` production rows are public `run` calls; the geometry rows are public `get_geometry` calls. No-Git production and resume raise `ValueError: record production requires an identifiable Git source checkout`. With Git but without papers, new RunRecords raise FileNotFoundError for Paper A, C01 for Paper C, and D03 for Paper D. With neither available, the Git error occurs first; the separate paper capture proves the second missing dependency. JSON includes the precise per-operation exceptions and paths.

RunRecord and GeometryRecord decoding succeeds in all controls, reading the serialized input alone (plus installed code/libraries). Resume succeeds without paper files when Git/commit/module bytes still match, because it reuses record paper references and compares only commit/modules. The deliberately dirty no-papers control does not become a clean-build certification: current resume’s dirty-flag behavior is simply recorded, not changed.

CURRENT_WHEEL_BUILD = NOT_IMPLEMENTED; CURRENT_SDIST_BUILD = NOT_IMPLEMENTED; CURRENT_INSTALLED_PACKAGE_SMOKE = NOT_YET_IMPLEMENTABLE. No build command or install was attempted because the required pre-existing metadata is absent. No build tool was downloaded. A package-only copy is expressly not a clean install.

## 7. Approved immutable distribution provenance

PACKAGED_PROVENANCE_MANIFEST = APPROVED. Use strict live Git plus raw source/paper provenance in a genuine source checkout. Use the immutable packaged manifest in an installed artifact or provenance-bearing sdist. No runtime network fetch, shipping Git/paper source/research, guessing provenance or schema changes. Both record schemas and the exact 14 authoritative identity paths remain unchanged.

1. Build from an exact clean committed source checkout with its recorded origin and six accepted paper sources; validate every required path, hash and frozen paper edition. Reject missing inputs and tracked dirty source for a certifiable release artifact.
2. Generate one versioned canonical JSON provenance manifest in external build staging. Never rewrite authoritative .py, paper, fixture or research bytes, and never generate new science. It contains source repository URL, full source commit, source tracked_dirty=false, package version, API/schema/ledger versions, exact sorted 14 module paths/raw source SHA-256 values, and all six paper IDs/editions/repository-relative locators/raw SHA-256 values.
3. The manifest may also carry a deterministic build-input identity (canonical manifest payload hash, excluding that identity field), backend/version facts and source receipt locators. Label it build-input identity, not wheel SHA-256. A wheel cannot contain its own full-file hash without circularity; record final wheel/sdist SHA-256 externally after building.
4. For a genuine source checkout, preserve live Git and raw source/paper provenance including dirty-state reporting. Do not silently fall back when an actual source checkout is incomplete, modified or has invalid provenance. An unrelated containing Git repository is not the kernel source checkout.
5. For an installed artifact or sdist without its original Git/paper tree, read and strictly validate the packaged manifest. Read actual installed .py bytes using paths anchored to the package, never cwd; compare all 14 raw hashes with manifest source hashes. Fail closed on missing manifest, malformed fields, missing/mutated modules or source/installed byte mismatch.
6. Populate the existing implementation object from source identity plus verified current module hashes; populate paper_references from the build-captured paper metadata. tracked_dirty describes the attested source checkout state at build time, not a guessed cleanliness state for nonexistent installed Git metadata. No missing-Git-to-false shortcut. Clean source, byte identity and recorded source context make false an honest source-provenance fact.
7. Use the same existing six implementation keys and paper-reference keys; do not add artifact identity, origin kind, manifest hash, source/installed duplicate hash arrays or extra module paths to 1.0.0 records. Additional distribution metadata stays in the manifest/distribution receipt.
8. Ship the same immutable manifest in the minimal sdist; rebuild a wheel from that sdist without Git/papers after revalidating source-file hashes and frozen metadata. Never replace the original source revision with a synthetic extraction commit or regenerate paper hashes from absent paper files.
9. Require source-blob = checked-out .py = wheel member .py = installed .py bytes for the existing 14 authoritative paths; capture all 19 shipped Python files in artifact-content verification as well. Bytecode/cache files and wheel RECORD are distinct. A .pyc-only or source-transforming build is outside this approved contract.
10. This is the approved frozen design, not a built or certified manifest implementation. Its checks establish consistency, not cryptographic authorship; no signing infrastructure or remote fetching is implied.

Missing or malformed manifests and tampered installed source must FAIL CLOSED. Hash actual installed .py bytes and compare them with attested source hashes; never substitute a manifest hash for changed runtime bytes. The exact identity contract is source Git blob = clean checked-out .py = wheel .py member = installed .py for all 14 authoritative paths. Other shipped internal modules must also be artifact-censused. K3b/K3c must test this; a transforming backend requires HOLD, not weaker resume semantics.

Shipping the entire repository, fetching provenance, omitting/guessing hashes and generating self-referential Python identity code remain rejected alternatives. A staged non-Python JSON manifest avoids extending the frozen runtime module list. No manifest is created or tracked in this phase.

## 8. Geometry, identity, replay and resume

geometry.py/reference_scaffold.py compute from code and SymPy; they import/read no papers or Git. _geometry_records.py:178-210 computes exact construction before provenance capture; production failures happen at _implementation or _papers. Exact-codec expression ordering/validation depends on producer SymPy; retain 1.14.0 reference. No SymPy source checkout is read or needed, only installed SymPy runtime. Fix shared provenance acquisition, not either constructor or the geometry codec.

| Identity | Existing field / absence | Meaning |
| --- | --- | --- |
| SOURCE_COMMIT_ID | implementation.commit; geometry construction_provenance.source_revision | Actual committed source that produced the distribution; required full Git ID, never artifact ID |
| PACKAGE_VERSION | implementation.package_version | Software distribution release label from __version__; not API/schema/paper version and not a unique artifact digest |
| DISTRIBUTION_ARTIFACT_IDENTITY | NONE | Final wheel/sdist filename plus raw SHA-256 in external build/release receipt; useful, new, not required by 1.0.0. A record alone cannot identify a unique wheel archive |
| INSTALLED_MODULE_HASHES | implementation.modules[].sha256 | Hash actual current .py bytes at production/resume. Approved contract requires equality with source hashes |
| SOURCE_MODULE_HASHES | No separate second array | Embedded manifest contains source hashes. With enforced equality, existing single module array honestly identifies both source and installed .py bytes |

For all 14 authoritative files, raw Git blob SHA-256 equals current worktree bytes and package-copy bytes. `.gitattributes` uses `* -text`. This proves the tested copies retain identity; it does **not** establish how a future wheel/sdist backend behaves. Source-to-wheel-to-installed byte identity must be tested in K3b/K3c before approval. Do not certify it from assumptions about wheels.

Existing _runner.py:156-177 compares commit and modules only, keeps prefix/parent digest and records environment segment. No paper re-read in resume. Approved contract must retain this rule; decode older valid records remains portable, resume into changed K3b source must reject. No _runner.py edit authorized by this freeze.

Compatible installed resume means the recorded commit and all sorted current module hashes equal the installed build’s source identity. A rebuild with identical source bytes can satisfy this even if ZIP metadata differs. A new K3b commit changes source identity; old records remain decodable but cannot be resumed under a different implementation. Use the existing explicit checkpoint-run route. Do not change this rule to compare package version alone or silently prefer manifest hashes over changed installed bytes.

## 9. Approved package-content classification

| Content | Classification | Wheel | sdist | Reason |
| --- | --- | --- | --- | --- |
| 14 public-closure kernel_physics/*.py files | MUST_SHIP_RUNTIME | YES | YES | Complete supported facade closure and exact 14-module schema identity |
| covering.py | MUST_SHIP_RUNTIME (retained internal software; support status unchanged) | YES, INTERNAL | YES, INTERNAL | Accepted internal mathematical owner outside facade import graph; retain existing opt-in behavior |
| face_state.py | MUST_SHIP_RUNTIME (retained internal software; support status unchanged) | YES, INTERNAL | YES, INTERNAL | Legacy opt-in; no eager re-export. Explicit import reaches quarantine, which is permitted only for opt-in internal callers |
| boundary_response.py, srg.py, operating_region.py | MUST_SHIP_RUNTIME (retained internal software; support status unchanged) | YES, INTERNAL | YES, INTERNAL | Whole-package build physically includes these; unsupported v1, not auto-imported and not Runner-selectable. Do not delete |
| kernel_physics/_distribution_provenance.json (future generated artifact) | MUST_SHIP_RUNTIME | YES | YES | Minimal immutable source/paper provenance, approved design; generated only in K3b external build staging |
| dist-info METADATA/WHEEL/RECORD and approved license metadata | MUST_SHIP_PACKAGE_METADATA | YES | CORRESPONDING PKG-INFO/LICENSE | Normal distribution identity/dependencies/license; currently absent |
| pyproject.toml and _build_backend.py (approved future build sources) | SOURCE_DISTRIBUTION_ONLY | NO raw build sources | YES | Build/rebuild mechanism, not runtime |
| kernel_physics/tests/* including parity_oracles | TEST_DISTRIBUTION_ONLY | NO | NO in minimal approved sdist | Repository/CI runs full tracked suite; tests use repository fixtures and provenance. No standalone test distribution created in K3a |
| kernel_physics/tests/fixtures/golden_388/* | TEST_DISTRIBUTION_ONLY | NO | NO | Repository/CI-only parity evidence, not runtime data; preserve bytes and receipt |
| Paper-F support, especially TRANSVERSE_AXIS_FALSIFICATION.csv | TEST_DISTRIBUTION_ONLY for exact P6 fixture; DO_NOT_SHIP remainder | NO | NO | P6 reads this source-relative CSV; retain full-source CI checkout for parity, not full papers tree in artifacts |
| K0 normative contract/ledger and K1/K2/current/historical receipts | SHOULD_SHIP_DOCUMENTATION (release evidence, separately from runtime) | NO | NO in minimal approved contract | Keep at recorded source commit; receipt identities and locators can be embedded, complete receipt bytes need not ship |
| papers/*, including six accepted source texts | DO_NOT_SHIP | NO | NO | Embed paper IDs, editions, locators and raw hashes; do not bundle paper bytes |
| research/* including research/twisted_hex_crystal_registration_v0.1/* | DO_NOT_SHIP | NO | NO | Outside supported runtime; no research execution or import |
| supporting_research/*, Claude outputs/*, research_files/*, research_notes/* | DO_NOT_SHIP | NO | NO | Historical/untracked research and publication work products |
| four local-only tests (30 methods) | DO_NOT_SHIP | NO | NO | Untracked predecessor tests remain a separate publication obligation; not promoted by K3 |
| kernel_physics/README.md | SHOULD_SHIP_DOCUMENTATION | AS METADATA DESCRIPTION | YES | Best description source after software-only installation/provenance guidance update |
| root README.md and archival manifests/tools | DO_NOT_SHIP in minimal runtime/sdist | NO | NO | Repository/publication/archive navigation rather than install documentation; retain in repository |
| LICENSE and LICENSE_SCOPE.md (both absent; K3b creation) | MUST_SHIP_PACKAGE_METADATA | APPROVED LICENSE TEXT AND SCOPE NOTICE | APPROVED LICENSE TEXT AND SCOPE NOTICE | Human-authorized Apache-2.0 for software only; standard unmodified license plus explicit exclusions prevents blanket repository licensing. |
| .git, build products, venvs, caches, scientific publication working files | DO_NOT_SHIP | NO | NO | No repository archaeology or environment bundled into runtime |

The runtime software includes the current internal modules. SHIPPED_INTERNAL_FILE != SUPPORTED_PUBLIC_API. boundary_response, srg and operating_region stay unsupported v1 internals; face_state stays legacy/internal opt-in. No eager facade import or Runner selection may activate them. Tests and parity evidence remain repository/CI material; golden_388, Paper-F support and other evidence datasets are neither runtime contents nor automatically software-licensed. K3b must preserve their current bytes and status.

## 10. Frozen version and support policy

| Namespace | Current / approved value |
| --- | --- |
| Engineering package | 0.1.0; __init__.py unchanged |
| Public API | 1.0.0 |
| KERNEL_RUN_RECORD schema | 1.0.0 |
| GEOMETRY_RECORD schema | 1.0.0 |
| Definition ledger | 0.1 |
| Paper editions | A publication; B 0.1.2; C 1.0.1; D 0.1.1; E 0.1.1; F 0.2 |

APPROVED: keep __version__ = 0.1.0 unchanged for K3 engineering/build certification. Package version is the software distribution release namespace, distinct from API/schema/ledger/paper versions. No __init__.py edit or public registry release/version bump is authorized; any later release decision follows K3 certification.

APPROVED first certification lane: Windows / CPython >=3.11,<3.12. Original observed environment remains CPython 3.11.15; no new cross-version test was run in R1 and no Python 3.12/Linux/macOS support is claimed.

Current requirements.txt still pins NumPy 2.3.5; approved K3b metadata/requirements target is NumPy 2.4.4, SymPy 1.14.0, mpmath 1.3.0. No dependency declaration or environment changed in this freeze.

Package version is the software distribution release namespace. It does not replace API/schema/ledger versions or paper editions. Approved first support target: **Windows / CPython >=3.11,<3.12 / NumPy 2.4.4 / SymPy 1.14.0 / mpmath 1.3.0**. This is a bounded certification target, not a new claim of successful installed testing on every 3.11 patch. Python 3.12, Linux, macOS and broad dependency compatibility are not claimed.

## 11. Frozen clean-install and CI contracts

- Import kernel_physics.api from an actual isolated installation with all origins under that environment.
- Construct explicit State and Parameters, delegate the accepted recurrence, compute raw z_chiral, and use supported passive observers/diagnostics without altering scientific meaning.
- Produce bounded trajectories and complete RunRecord records; preserve binary64 serialization, round-trip inertly, and resume only with matching source revision plus module hashes.
- Request C01 and explicitly selected D03 with exact SymPy inputs; preserve exact-tree producer ordering, metadata and coupling=none; round-trip GeometryRecord inertly.
- All operations work without source Git, papers, research, UI, network, LLM/embedding/GPU subsystem or quarantined option activation.
- No claim of universal cross-platform bitwise replay; retain existing environment qualification and strict precision behavior.

A certified installation must support import, explicit Parameters/State, step, raw z_chiral, accepted passive observers/diagnostics, bounded run/RunRecord production and round-trip, compatible resume, C01 and explicitly selected D03, and GeometryRecord round-trip. It must work without .git, papers, research, network, LLM, embedding model, GPU or source repository archaeology, while preserving all K0/K1/K2 boundaries.

**CI_CONTRACT = FROZEN as the K3c target.** No CI is created here.

1. Approved first certification lane: Windows / CPython >=3.11,<3.12 / NumPy 2.4.4 / SymPy 1.14.0 / mpmath 1.3.0. Exact observed reference remains Python 3.11.15. Historical Python 3.12 fixture production is not package support. No Linux/macOS or broad dependency compatibility is claimed.
2. Use a clean tracked checkout at the intended committed source HEAD. Run the full tracked unittest suite and existing facade/oracle boundary gates with repository fixtures present; local-only tests remain separate. Check the original 298 plus explicitly authorized new software distribution tests.
3. Use explicitly approved, available build/runtime dependency artifacts; no uncontrolled resolution in certification. Build wheel and sdist into external staging. Validate exact file allowlists, no science/research/paper/.git/test leakage, version/dependency/license metadata and immutable manifest.
4. Compare source Git-blob bytes, source worktree bytes, archive member bytes and installed .py bytes; verify all 14 authoritative identities and unchanged scientific owners. Any build transformation breaks the approved byte-identity contract and is a HOLD, not a reason to loosen resume.
5. Install the wheel in a disposable isolated environment with approved dependency wheels. Run python -I from an unrelated empty directory with the source checkout absent from import paths. Assert api.__file__ and every public-closure module resolve inside the installed environment; no PYTHONPATH or system-site-packages shortcut.
6. Without .git, papers, research, network or models: explicit Parameters/State, triad/ring steps in supported scopes, raw z_chiral, both passive observers and diagnostics, zero/one/bounded-update runs, RunRecord exact JSON round-trip, compatible resume and incompatible source/hash rejection, C01 and explicit D03, GeometryRecord exact JSON round-trips. Assert no face_state/quarantine/research imports and no Runner selection routes.
7. Exercise missing/corrupt manifests and tampered installed module rejection; decoding existing valid records remains portable and inert. Verify producer versions and source tracked_dirty meaning. Preserve original module-list and schema field validation.
8. Extract the sdist outside Git, rebuild a wheel offline from its embedded manifest, install and repeat the isolated smoke. Require matching source identity and .py bytes; do not promise identical complete wheel ZIP bytes before build testing.
9. Check source git diff --check, git diff/status and raw preservation hashes; report artifacts and dependency versions. No CI files are created in K3a. K3c must implement and certify this frozen target after separately authorized K3b implementation.

## 12. Frozen licensing, naming and publication authority

SG8 = RESOLVED_BY_HUMAN_AUTHORITY. Hilmir explicitly selected Apache License 2.0 for SOFTWARE_ONLY distribution scope through K3a-R1. No license was chosen by the agent, and no additional confirmation is required for the authorized receipt commit/push.

### Covered software scope

- kernel_physics runtime/software intended for distribution
- package/build tooling
- distribution verification tooling
- software installation/use documentation
- software distribution metadata

### Not automatically covered

- papers/
- research/
- research datasets
- figures
- publication manuscripts
- Twisted Hex Crystal research
- parity fixtures/evidence datasets (including golden_388 and Paper-F support datasets)
- historical research artifacts
- other scientific/publication materials

Those scientific/publication materials retain their existing licensing/publication status unless separately authorized or governed by a specific separate file/directory license notice. This is not a blanket license for the repository or every file under kernel_physics: parity fixtures/evidence remain excluded wherever stored.

K3b must create `LICENSE` containing the standard **unmodified Apache License 2.0 text**, plus `LICENSE_SCOPE.md` explicitly identifying the covered software/build/verification/install-documentation/metadata scope and excluded papers, research, figures, datasets/parity evidence, manuscripts and historical scientific artifacts. Include the scope notice with the distribution license presentation. `pyproject.toml` must identify the approved software license without falsely asserting a uniform repository-wide license. Neither legal file nor package metadata is created in K3a-R1.

The original census still finds no license file; the unchanged Paper A/C publication reports still record undecided paper/publication licensing. R1's software-only approval does not alter those documents or license their contents.

| Frozen field | Approved value |
| --- | --- |
| DISTRIBUTION_NAME | trioctagon-physics |
| IMPORT_PACKAGE | kernel_physics |
| SOURCE_PACKAGE_DIRECTORY | kernel_physics/ |
| GITHUB_REPOSITORY | pzychozen/trioctagon-physics |
| REPOSITORY_PROJECT_NAME | trioctagon-physics |
| AUTHOR | Hilmir Frímann Halldórsson |
| PROJECT_URL | https://github.com/pzychozen/trioctagon-physics |
| DESCRIPTION_SOURCE | kernel_physics/README.md |
| PACKAGE_VERSION_POLICY | KEEP_0.1.0_FOR_K3_ENGINEERING |
| ENGINEERING_PACKAGE_VERSION | 0.1.0 |

Distribution/project metadata name `trioctagon-physics` is the conceptual `pip install trioctagon-physics` name. The supported Python import remains `from kernel_physics.api import ...`, with source directory `kernel_physics/`. Do not rename it to `trioctagon_physics` or `kernel-physics`, or move source files to match the repository name. K3b install guidance must preserve this distinction.

Do not invent an author email, organization, affiliation, or copyright year/range beyond what approved license metadata requires. Registry-name availability is NOT_CERTIFIED and must be checked immediately before any future upload. No registry publication or public release/version bump is authorized by this phase; a later release-version decision may follow K3 certification.

SG1/SG2 were rechecked in R1. Original SG3/SG4 evidence is retained; no mathematics/schema/full-repository solution is required. SG7 remains a future build gate: transforming scientific implementation bytes must HOLD. SG10 is avoided here by no installs/environment mutation. No current K3a authority blocker remains.

| License implementation state | Value |
| --- | --- |
| LICENSE_PRESENT | False |
| LICENSE_REFERENCED_BY_PACKAGE | NO; package metadata absent |
| LICENSE_AUTHORIZED | True |
| LICENSE_SELECTED | Apache-2.0 |
| LICENSE_SCOPE | SOFTWARE_ONLY |
| LICENSE_FILE_CREATION | DEFERRED_TO_K3B |
| LICENSE_SCOPE_NOTICE_PRESENT | False |


## 13. Accepted K3b boundary — implementation not started

The following exact conceptual boundary is accepted by K3a-R1 with LICENSE_SCOPE.md added. A separate K3b work order must authorize implementation; these are not K3a-R1 edits. No other existing runtime file may be changed under this freeze.

### `pyproject.toml` — NEW

- WHY REQUIRED: No package metadata/backend/dependencies/content selection exists. Declare exact kernel_physics package, backend, package version source, approved project/license metadata and runtime dependencies. Exclude tests/subpackages and unrelated tree.
- WHY SOFTWARE-ONLY: Distribution configuration only.
- WHY MATHEMATICS UNCHANGED: No equations, constants, model defaults or scientific file generation.
- WHAT TEST PROVES IT: Build metadata/content census and isolated wheel/sdist install.

### `_build_backend.py` — NEW

- WHY REQUIRED: One bounded PEP 517 wrapper around available setuptools.build_meta can stage an allowlisted copy, capture immutable provenance, verify source bytes and build both wheel/sdist without changing authoritative source. No second build-helper file is proposed.
- WHY SOFTWARE-ONLY: Build-time file/identity management only.
- WHY MATHEMATICS UNCHANGED: Copies raw scientific bytes; rejects changes instead of transforming them.
- WHAT TEST PROVES IT: Clean source build, staged-manifest validation, byte comparisons, no-Git sdist rebuild and source cleanliness.

### `LICENSE` — NEW IN K3B; TERMS NOW APPROVED

- WHY REQUIRED: Create the standard unmodified Apache License 2.0 text for the approved software-distribution scope, accompanied by LICENSE_SCOPE.md.
- WHY SOFTWARE-ONLY: Legal/publication metadata, not runtime.
- WHY MATHEMATICS UNCHANGED: No scientific meaning changes.
- WHAT TEST PROVES IT: Compare standard unmodified license text and verify the scope notice plus correct software license metadata in artifacts; no blanket scientific-material grant.

### `LICENSE_SCOPE.md` — NEW IN K3B

- WHY REQUIRED: Explicitly bound Apache-2.0 to approved runtime/software, package/build/verification tooling, software installation/use documentation and distribution metadata. Exclude papers, research, figures, datasets/parity evidence, manuscripts, Twisted Hex and historical scientific/publication artifacts unless separately licensed.
- WHY SOFTWARE-ONLY: Scope notice for software distribution licensing; no automatic license grant to scientific/publication material.
- WHY MATHEMATICS UNCHANGED: No scientific source, claim, dataset, fixture or paper modification.
- WHAT TEST PROVES IT: Review exact included/excluded scope against R1 and verify license/scope notice inclusion with truthful pyproject software license metadata.

### `kernel_physics/_records.py` — MODIFY SOFTWARE PROVENANCE FUNCTIONS ONLY

- WHY REQUIRED: _implementation and _papers currently require live Git and paper files. Add strict same-schema manifest fallback/installed-byte verification in this existing module; avoid a new runtime .py module that would require changing the frozen 14-path identity set.
- WHY SOFTWARE-ONLY: Provenance acquisition and validation, not numerical or symbolic computation. Keep public signatures, decoder fields, _MODULES and schemas unchanged.
- WHY MATHEMATICS UNCHANGED: Mathematical owners and delegations untouched. No weakening of resume compatibility.
- WHAT TEST PROVES IT: New provenance tests, existing P12, record/geometry tests, full parity, missing-Git/papers installed smoke, tampered module rejection, same-source resume and mismatched-source refusal.

### `kernel_physics/requirements.txt` — MODIFY DEPENDENCY PINS ONLY

- WHY REQUIRED: Current NumPy 2.3.5 pin differs from approved first certification target 2.4.4. Align metadata and requirements to NumPy 2.4.4 / SymPy 1.14.0 / mpmath 1.3.0 in K3b only.
- WHY SOFTWARE-ONLY: Dependency declaration.
- WHY MATHEMATICS UNCHANGED: No equation/source change; numerical behavior remains subject to full parity.
- WHAT TEST PROVES IT: Metadata/requirements agreement and approved-environment parity; broad version ranges are not inferred.

### `kernel_physics/README.md` — MODIFY INSTALL/PROVENANCE GUIDANCE ONLY

- WHY REQUIRED: Add supported install/provenance guidance, the trioctagon-physics distribution versus kernel_physics import/source distinction, the approved engineering version/support lane, explicit software-only license scope and unchanged quarantine boundary.
- WHY SOFTWARE-ONLY: Usage and distribution documentation.
- WHY MATHEMATICS UNCHANGED: No reinterpretation of accepted scope.
- WHAT TEST PROVES IT: Documented wheel smoke and links/metadata review.

### `kernel_physics/tests/test_distribution_provenance.py` — NEW

- WHY REQUIRED: Validate software fallback, strict manifest acceptance, identity/dirty-source semantics, cwd independence and schema preservation.
- WHY SOFTWARE-ONLY: Software regression gates only.
- WHY MATHEMATICS UNCHANGED: No independent oracle or existing scientific test is edited.
- WHAT TEST PROVES IT: Run with existing tracked suite; assert malformed/missing/tampered inputs fail closed.

### `tools/verify_distribution.py` — NEW

- WHY REQUIRED: One external artifact-verification harness for build content, source/wheel/installed hashes and isolated installed API smoke; can be invoked by future CI.
- WHY SOFTWARE-ONLY: Packaging verification only; never a runtime dependency.
- WHY MATHEMATICS UNCHANGED: Calls existing facade and compares outputs/identity; no scientific regeneration.
- WHAT TEST PROVES IT: Runs outside checkout against built wheel and no-Git sdist rebuild, checks installed module origins and exclusions.

### `kernel_physics/_distribution_provenance.json` — GENERATED EXTERNALLY / IN PACKAGE STAGING ONLY; MUST NOT BECOME AUTHORITATIVE TRACKED SOURCE

- WHY REQUIRED: Minimum immutable provenance data unavailable in an installation.
- WHY SOFTWARE-ONLY: Source/paper identifiers and raw hashes only.
- WHY MATHEMATICS UNCHANGED: No scientific data regeneration, copied paper source or equation.
- WHAT TEST PROVES IT: Strict manifest verification, source identity equality, artifact inclusion, installed record smoke.

No mathematical owner, api.py, _contract_types.py, _runner.py, _geometry_records.py, _presets.py, __init__.py, existing test, frozen receipt, paper, fixture, research, root README or CI changes under this accepted boundary. Any later need requires explicit scope revision, not automatic widening.

K3a-R1 freezes authority in exactly the two receipts. Next: separately authorized K3b package/provenance implementation; then K3c clean build/install/sdist rebuild and CI certification. No registry publication, version bump, UI work or scientific phase authorized.

## 14. R1 bounded verification and publication

Before editing receipts, local HEAD, origin/main tracking ref and live remote main all matched `d76321a54f6f3a8ee1f0175ac6a4db6d0c017117`. All 706 pre-existing tracked files retain the original K3a baseline raw SHA-256. There were no staged or tracked changes. Only the two existing uncommitted K3a receipts are updated. Existing unrelated untracked material remains untouched.

R1 validation checks receipt JSON/Markdown consistency, approved values and licensing exclusions, unchanged original preflight evidence, the exact two-file addition allowlist, all baseline tracked hashes and git diff --check. The 298-test result and original no-Git/no-papers experiments are retained evidence, not rerun results. No new build/install attempt or environment modification is needed or performed.

The JSON retains full original import/census/probe/source/paper evidence and adds the historical HOLD-to-PASS transition, frozen authority and accepted K3b scope. Attempt_1 history retains its original no-commit/no-push facts; those do not describe R1 publication.

Publication authorized by R1 section 17: stage exactly `kernel_physics/K3A_DISTRIBUTION_PREFLIGHT.md` and `kernel_physics/K3A_DISTRIBUTION_PREFLIGHT.json`; commit on existing main with `freeze software distribution contract after K3a`; push normally to origin/main after validation. No force, reset, branch creation, cleanup or unrelated staging. These are **2 new files and 0 modified pre-existing tracked files** relative to the starting HEAD.

The exact final commit and matching remote main are verified after publication and returned in task closeout. This receipt uses CONTAINING_K3A_R1_COMMIT for its own publication identity to avoid circular commit hashing. That commit becomes the proposed next starting HEAD for a separately authorized K3b. **K3B_IMPLEMENTATION_STARTED = NO.** No pyproject, build backend, license/scope notice, provenance manifest, distribution test, verifier or CI has been created.
