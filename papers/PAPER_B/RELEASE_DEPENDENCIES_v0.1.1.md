# Paper B release dependencies v0.1.1

The proposed release is the committed baseline a0875c493b23b7d1aaa718ea2b40aa17af9adcd2 plus two explicit allowlists. Neither list has been staged. The paper list alone is not a complete implementation release.

| Claim | Actual requirements | Scope |
|---|---|---|
| A: read the mathematics | Current manuscript/PDF | Self-contained proofs; no execution or earlier discussion required |
| B: regenerate figures/PDF and paper checks | Paper sources, committed kernel_physics/geometry.py and __init__.py, Python libraries, Pandoc, Tectonic and populated TeX resource cache | accepted_coordinates.py imports only geometry; generated figures use its exact coordinates. Full public verification also checks the declared source/provenance hashes |
| C: execute Appendix A implementation | Baseline geometry/dynamics/package init, the six optional modules and two cited test files below; current README for its executed fixture | One-step replay and existing cited tests; no general claim about every broader subsystem |

## Additional supporting allowlist

The exact paths are in [the supporting allowlist](PROPOSED_SUPPORTING_ALLOWLIST_v0.1.1.txt). All implementation/test/README bytes already existed and remain unchanged.

| Path | Concrete reason |
|---|---|
| kernel_physics/face_state.py | Appendix A API; directly imported by the runtime smoke |
| kernel_physics/readouts.py | Imported by face_state and cited as the raw chirality implementation |
| kernel_physics/operating_region.py | Unconditional face_state import, even when plain step3 is selected |
| kernel_physics/srg.py | operating_region imports handoff_area_response; readout tests import fourier_basis |
| kernel_physics/boundary_response.py | srg imports RESPONSE_ID, _theta and lens_area_gain; tests import its precision-error type |
| kernel_physics/_response_numeric.py | Checked numeric primitives imported throughout the optional modules |
| kernel_physics/tests/test_face_state.py | Cited tests; immutable original |
| kernel_physics/tests/test_readouts.py | Cited tests; immutable original |
| kernel_physics/README.md | The face-state test executes its existing Python example and checks face_runs. Baseline README lacks that fixture |
| research/folded_face_state/FOLDED_FACE_STATE_ATTACHMENT_v0.1.md | Exact [FA] repository copy including the controlling §10 |

The original [FA] report remains at its original local path; the one repository copy has the same SHA-256, ab5d572ca11bb8d8ecb2236f8521cc25e7b90b7569942303568bfa93d01b52e7. Its absolute/relative historical references are preserved source evidence, not public build commands. The kernel README is likewise an unchanged historical implementation record; use the publication commands below for this release's scoped replay. No bulk research copy is proposed.

Baseline files already supply geometry.py, dynamics.py, __init__.py, tests/__init__.py and test_dynamics.py, as well as Paper A/C and Bridge I/II references. These do not need duplicate additional-release entries. The supporting manifest records hashes and reasons for all ten added/overlaid paths.

Transitive boundary/SRG imports are present because the existing architecture requires them. Their inclusion does not adopt those subsystems as Paper B's physics. No optional implementation was refactored to reduce this list.

## Tool and library prerequisites

No tools or environments are installed or upgraded by these commands. Python 3.12.14 was available. Paper generation uses SymPy 1.14.0, mpmath 1.3.0, NumPy 2.5.3, Matplotlib 3.10.7 and pypdf 6.10.0 with the versions in requirements.txt. Runtime replay uses the existing kernel dependency versions: NumPy 2.3.5, SymPy 1.14.0 and mpmath 1.3.0. The two environments are deliberately distinguished.

PDF generation requires existing Pandoc 3.11 and Tectonic 0.17.0, with the TeX Gyre Pagella resource files available in a populated Tectonic cache. Set PAPER_B_PANDOC and PAPER_B_TECTONIC to those executables (or make them available on PATH), and PAPER_B_TEX_CACHE to the existing cache. The builder uses --only-cached and fails clearly if a required resource is absent; it does not fetch or install it. Fontconfig uses the system font directory. Tools, caches, environments, fonts and binaries are not release files.

If the paper's third-party libraries are already available in an explicit separate directory, PAPER_B_PYTHON_PATH may list existing library directories separated by the platform path separator. It must not point to a kernel checkout. The isolated check receipt names the actual local tool prerequisites; these are external tools, not undeclared scientific inputs.

## Public commands

Run these from the repository root, using the appropriate existing interpreter. “paper-python” and “runtime-python” below denote those declared interpreter environments, not programs supplied in the repository.

~~~text
paper-python -B papers/PAPER_B/check_manuscript_algebra.py
paper-python -B papers/PAPER_B/generate_figures.py
paper-python -B papers/PAPER_B/build_publication.py
paper-python -B papers/PAPER_B/verify_publication.py
runtime-python -B papers/PAPER_B/runtime_smoke.py
runtime-python -B -m unittest kernel_physics.tests.test_face_state kernel_physics.tests.test_readouts kernel_physics.tests.test_dynamics -v
~~~

build.ps1 with -PythonExecutable runs the first four commands. They do not depend on the UI or an out-of-repository scientific archive. Before rebuilding a saved package, check_package.py verifies its exact shipped hashes and both allowlists. A rebuild rewrites production logs with the local tool paths; that does not make the delivered manifest a manifest of those later log bytes.

## Local-only checks and qualification

closeout.py is a maintainer's original-preservation and manifest refresh command. It requires the original local protected paths and historical Git repository; it is intentionally not a public reproduction prerequisite. The reviewed_v0.1 archive preserves the prior 44-file package and earlier validation evidence. Its old scripts and old README are historical, not the active commands above.

The isolated test uses git archive of the stated commit plus the two proposed file lists, never a copy of the full local archive. Kernel imports are required to resolve inside that minimal checkout. The tools and already installed third-party libraries remain explicit external prerequisites. This is not a remote clone or a clean-machine dependency-installation test. The exact result is recorded in evidence/v0.1.1/isolated_release_check.json and appended to the existing Codex publication validation report.
