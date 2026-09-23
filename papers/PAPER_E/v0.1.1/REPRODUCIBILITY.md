# Reproduction scope for v0.1.1

The revision reuses the parent's 11 figure sets, frozen figure data, historical source snapshots and earlier evidence. The combined proposed allowlist includes the complete 90-path predecessor plus this edition. It does not include local environments, rendering scratch or unrelated archives.

## Commands and prerequisites

From this directory, `python -B check_revision.py` uses NumPy and pypdf plus the standard library. It runs only the inspected `apply_phase_triad_sync` and `embed_on_torus` function bodies extracted from bundled, hash-checked originals; static AST inspection checks the embedding divisors. It does not import the historical modules as applications, run trajectories, invoke the supplied GPT checker or write to the predecessor. Its separately attributed JSON result is written here.

`python -B build_publication.py` requires existing Pandoc, Tectonic, cached TeX resources and fonts. Set `PAPER_E_PANDOC`, `PAPER_E_TECTONIC` and `PAPER_E_TEX_CACHE`; the build uses `--only-cached`. It reads the unchanged figure PDFs at `../figures/` and writes this edition's LaTeX, PDF and logs. The complete Markdown is retained through the same AST transformation used for v0.1.

The runtime accepts `PAPER_E_PYTHON_PATH` as a platform-separated list of existing third-party library directories. The actual environment and executable hashes are recorded in the build/check results. No installation or upgrade is required or was performed. Matplotlib is needed only to redraw figures from frozen data, not to build a PDF from supplied figures. SymPy is required for the preserved symbolic checker only; it was not rerun for this revision.

`minimal_copy_check.py` creates a fresh disposable tree under this edition's ignored `.build/`. It copies only the explicit proposal paths, preserves their repository-relative layout and uses declared external tools/libraries. It builds the revised PDF, executes the small revision checker, and redraws the figures from frozen data inside that copy. It does not run the four historical replays or the GPT checker. Figure/PDF identities and any metadata-only differences are reported, not hidden by source repair. The final inventory reconciliation separately copies late closeout metadata and verifies every final manifest hash in the minimal tree.

## Verification versus replay

The reviewed v0.1 PDF and supplied allowlist were confirmed against GPT's stated SHA-256 values before authoring. All 89 original manifest entries are rechecked without invoking the old root inventory checker, whose historical whole-directory scope would reject the newly added revision directory. That old checker is preserved unchanged; the revised closeout tool understands the combined edition inventory.

The new zero-phase witness uses a fixed absolute tolerance of 1e-14 for ordinary trigonometric rounding, with zero relative tolerance. This is not a change to any model/checker tolerance, saved diagnostic baseline or historical source. The full signed-zero angle values and sign bits are reported. The phase-off bypass is checked by object identity before any polar operation.

The 66-predicate and four-replay evidence retains its original v0.1 attribution, inputs and output identities. No saved historical data are regenerated. The supplied GPT checker/results remain separate, hash-preserved evidence; its counts are not added to Codex's counts. Reading an archived script does not establish that its original GUI/import paths work on a fresh clone.

## Closeout checks

`python -B closeout.py finalize` is local authoring machinery requiring the pre-edit baseline. It verifies unchanged protected files and exact-prefix preservation for only the three authorized continuity appends, then emits the preservation receipt, explicit combined allowlist and combined manifest. It also records whitespace findings without reformatting preserved source/log/SVG bytes. `python -B closeout.py verify` checks the final public inventory and hashes and has no Git mutation.

After finalization, `python -B closeout.py verify_copy` reconciles the final listed files into the already-existing disposable build tree and verifies every copied byte and manifest entry. It does not repeat the build or scientific checks. Its receipt stays in ignored `.build/minimal_copy_final_receipt.json` to avoid a manifest self-reference cycle.

The combined manifest uses repository-relative paths and excludes only its own self-hash. The original predecessor manifest is included and verified. Already-committed Paper B/D PDFs are reference dependencies with explicit hashes; they are not required by the PDF builder and are not duplicated in the minimal copy or new allowlist. No fresh remote state or publication approval is asserted by a local build.

The only remaining build prerequisites are the declared compatible Python libraries and existing Pandoc/Tectonic/cached fonts. Final-byte GPT acceptance and separately authorized publication remain workflow prerequisites. Six-gap placement and an original saved-run environment identity remain scientific/provenance limits, not hidden build dependencies.
