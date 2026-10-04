# Portable Paper G supplement - v0.1.1 edition

**Local review only.** Recomputes accepted M2/M3 enclosures without `kernel_physics`, UI, Historical/TORMENT, services, databases, network or private Downloads folders. Python3.11 and mpmath1.3.0 suffice for proof replay. Requirements are in [requirements-proof.txt](requirements-proof.txt); the author's `torment` environment already supplies them.

From this paper directory, in Command Prompt:

```bat
conda activate torment
python -I -B -X utf8 reproducibility\replay.py --output "%TEMP%\paper-g-replay-01"
```

Use a fresh external output directory each time. The wrapper refuses to overwrite one and executes copies there. An installation on another system uses that system's Python3.11 with the pinned dependency and any new external path. No absolute author path is required to run the supplement; original paths in manifests are provenance only.

The entry point first validates supplied source bytes, **then actually recomputes** M2's integer Krawczyk/jet certificate and M3's interval trajectory, strict trap, derivative and H-equation enclosures. It compares exact regenerated objects to accepted receipts. It also replays the independent nominal formulation at130 digits as a numerical consistency check. It is not a saved-Boolean checker and not a second independently implemented interval engine.

Fresh preparation replay: M2 integer certificate identical, repaired M3 verdicts28/28, support predicates23/23, nominal enclosure-membership checks2/2. [Results](results/replay_summary.json) identify this run. Counts include documentary/identity checks, not independent theorem counts. Proof logic remains in the manuscript and source review, with mpmath interval arithmetic and Python integer operations in the trusted numerical base; no formal proof-assistant certification is claimed.

## Files and authority

- `verifiers/gpt_m2_analytic_interval_review.py`: unchanged original analytic certificate script; exact integer interval operations at scale2^-240. Original status labels precede final joint acceptance.
- `verifiers/m3_claude_review_v0_2.py`: unchanged repaired interval engine; uses exact rational endpoints from internal interval tuples. It writes beside its execution copy, so always run via the wrapper or from external scratch.
- `verifiers/m3_support_publication.py`: explicit publication adaptation of Codex's accepted support checks. [ADAPTATIONS.json](ADAPTATIONS.json) documents the small I/O and historical-comparison changes. Mathematical predicates are retained. The original evidence was not edited.
- `verifiers/m3_nominal_crosscheck_v0_2.py`: unchanged supplied nominal formulation; numerical consistency only.
- `inputs/m2_accepted_certificate.json`: exact certified host/spectral/jet endpoints; original frozen output. It is checked against the newly recomputed certificate before being used as an authority comparison.
- `inputs/m3_nominal_seed.json`: original M3 record read only for fixed candidate-center selection by the repaired script. Its old assertions are **not** accepted proof premises; the candidate is validated afresh. Superseded index300 conclusions and remote branch identification must not be repeated.
- `inputs/m3_accepted_support.json`: exact `values.exact_receipts.Up`, `positive_weights`, centers and other accepted rational intervals. `Um` is historical key notation for E_minus, an outer enclosure.
- `inputs/m2_nominal_onset.json`: original finite observations. Old certificate/multiplier labels do not supersede final M2 corrections. The figure reads only the amplitude-law table.
- `authorities/`: unchanged final acceptance/correction records and M1 core. Full provenance is in [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json). Original personal source paths are informational, never execution requirements.
- `results/`: this paper preparation's fresh outputs, distinguishable from accepted inputs; nominal CSV and figure receipt are numerical illustration data.

Nothing here asserts that every historic local investigation archive is public. The included subset is sufficient for these paper claims and replay; it does not replay all old studies or original hardware. External literature PDFs and old magnet-control archives are not included. The root paper's local-review/redistribution note governs the assembled package.

## Figures

Figure generation additionally uses NumPy and Matplotlib. Pinned observed versions are recorded in `results/environment.json`. Rebuild in external scratch:

```bat
python -I -B -X utf8 source\make_figures.py --output "%TEMP%\paper-g-figures-01"
```

This performs only321 nominal updates from the squared-norm-three entrance at130 digits and compares q300/q301 to accepted exact enclosures. It reads three existing M2 onset points; it does not rerun the old long onset experiments. Output CSV preserves65 displayed significant digits. The script creates PDF and PNG assets with fixed plotting choices. The output folder is new; selected final assets are copied to `figures/` only as an explicit preparation step.

## PDF build

The editable manuscript is a multi-file LaTeX project using four included figure PDFs. `source/build_pdf.py` stages a copy outside the repository and uses an existing offline Tectonic cache; it installs/downloads nothing. Set your own tool/cache locations (the author's local paths are examples, not executable supplement requirements):

```bat
conda activate torment
set "PAPER_G_TECTONIC=C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\tectonic\tectonic.exe"
set "PAPER_G_TEX_CACHE=%USERPROFILE%\.codex\reports\kernel_history_paper_20261001\tectonic-cache"
python -I -B -X utf8 source\build_pdf.py --workspace "%TEMP%\paper-g-pdf-01"
```

Alternatively compile `source/paper_g.tex` with a compatible XeLaTeX installation and the stated TeX Gyre Pagella text/math fonts, keeping working files outside the repository and preserving `source/` beside `figures/`. Different TeX/font builds can change PDF bytes without changing mathematics; the final PDF hash identifies the visually inspected artifact, not a promised cross-platform byte-reproducible PDF. Figure/PDF builds are optional for the minimal proof replay.

After an edit, render and visually inspect every page; the saved visual receipt does not cover future changes. Do not run original verifier scripts in-place because their output locations are adjacent to their own file by historical design.

## v0.1.1 revision replay

Accepted inputs, all four verifier scripts, the replay wrapper, figure-generation code, figures and historical v0.1 results are unchanged. A new replay of this edition is recorded separately in [results/v0.1.1/replay_summary.json](results/v0.1.1/replay_summary.json). It recomputes the enclosures; it does not refresh any expected value. The edition's build/review report supplies the exact executed command and preservation comparison.
