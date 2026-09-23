# Bounded revision build, verification and preservation

Date: 23 September 2026. Execution attribution: Codex. Scope: E-01 through E-04 and publication preparation only. GPT's central-mathematics acceptance is recorded separately from final-byte approval, which remains pending.

## Build and visual inspection

The synchronized Markdown/LaTeX/PDF build completed with Pandoc 3.11 and cached/offline Tectonic 0.17.0 on Python 3.12.14. The actual executable hashes, manuscript hash, TeX hash and PDF hash are in `publication/build_record.json`; actual stdout and the raw TeX log are preserved beside it. No environment was installed or upgraded.

The output has **28 A4 pages**, 40 displayed equations and all 11 unchanged figures. The existing AST transformation retained every display body. The new equation/theorem comparison confirms all 40 display bodies and all 13 named theorem/proposition statements match the reviewed v0.1. The final log has no overfull box or missing-character warning. Benign package notices concern unicode-math command selection and caption hyperlink behavior, as in the predecessor.

Every final page was rendered using the existing Poppler `pdftoppm` at 110 dpi and inspected in four contact sheets. Definition pages 4 and 14, the cancellation paragraph on page 19 and references on page 28 were also inspected at individual-page size. The revised phase conventions, source names, formulas and corrected locator are legible; no clipping or missing mathematical glyph was found. Natural reflow retains the existing figure layout; no figure redesign was performed and the old page count was not forced.

Final PDF SHA-256: `1187d63125e8970abcf96a505dce792aa2ce84de45af7c468fc56d09abd85438`.

## New bounded checks and reused evidence

`check_revision.py` passed **52 checks**. It extracts and executes only two inspected functions from the bundled originals in an isolated namespace: historical phase synchronization and channel-torus embedding. It imports no historical GUI or model runner. Static AST checks read the two cylinder angle divisors and the alternate torus divisor. The remaining checks verify source/review hashes, predecessor manifest entries, unchanged equations/statements/figure references, corrected wording and revised build identities.

The fixed witness uses the same numerical complex state with two representations of zero, zero-strength bypass and positive phase strength 0.001. NumPy reports zero phases `[0, pi, -0, -pi]`, with the negative-zero sign bit retained. The nonzero neighbour's output differs by `0.0019999996666666877`, consistent with `2*sin(0.001)` within the fixed ordinary-rounding tolerance 1e-14. The zero channel's displayed points are `(2.6,0,0)` and `(1.4,0,approximately 7.35e-17)`. These witness checks document the historical numerical rule; they do not replace it or prove global continuity/equivariance.

Static source results are `12.0` for `geometry_3d.history_to_xyz`, `12` for `geometry_embeddings.history_to_xyz`, and `config.n_sectors` for the alternate torus. The exact original bytes and hashes remain unchanged.

The predecessor's 66 symbolic predicates, 51 package checks and four fixed source replays are reused at their actual v0.1 identities. The earlier 23-configuration study is not rerun. GPT's supplied 27 groups / 147 conditions remain GPT-attributed; its checker is retained without execution. No saved historical datasets, failure tails or diagnostic thresholds were regenerated or adjusted.

## Minimal-copy reproduction

A fresh disposable repository-shaped tree under `.build/minimal_copy/` received the **116 actual proposed files present at build-check time**, containing the complete predecessor and then-current revision/build inputs. Late change/closeout documentation is reconciled into that tree by the final inventory gate without repeating scientific work. Input identities and the exact three executed commands are in `evidence/minimal_copy_results.json`.

The isolated edition PDF rebuild returned exit 0 and was **byte-identical** to the canonical revised PDF. The isolated revision checker returned exit 0 with the same 52 checks. The parent's frozen-data figure generator returned exit 0: all **11 PDF and 11 PNG figure files matched byte-for-byte**; all **11 SVG files differed only in their generated `dc:date` timestamp**. The comparison recorded both hashes and checked equality after removing only that timestamp for the SVG comparison. No source, array, tolerance or reference asset was altered to force equality. The original figures and NPZ stayed unchanged.

Declared external dependencies were the existing Python runtime/libraries, Pandoc/Tectonic executables and populated TeX cache/fonts. The copy did not contain an environment or unrelated research archive. `PYTHONPATH` was cleared and user-site packages disabled for subprocesses; the declared `PAPER_E_PYTHON_PATH` directories supplied existing libraries. No model trajectory, optional four-run replay, old GUI, GPT checker or unrelated archived script was executed.

This establishes the stated paper build and frozen-data rendering paths. It does not certify every historical archived script as fresh-clone runnable. Already-committed Paper B/D PDFs are separately listed reference dependencies and are not build prerequisites. The remaining executable prerequisites are the declared compatible libraries, tools and cache; final-byte acceptance and publication authorization are separate workflow prerequisites.

## Preservation, whitespace and Git

The baseline contains **603 existing identities**. The final receipt verifies **600 byte-unchanged files** and **three explicitly authorized append-only external records**, with all previous bytes retained as exact prefixes. All **90 reviewed predecessor publication paths**, including its original manifest, are byte-preserved. Source kernels, old diagnostic packages, earlier reconstruction evidence and Papers A-D are unchanged.

Local HEAD remains `505821a77c3aa1df89a2c400c65ba33149e635c8`; the index identity and status outside the new edition remain unchanged. Tracked files are clean and no files are staged. The new edition is untracked. Existing unrelated untracked material was neither cleaned nor added.

`WHITESPACE_REPORT.json` reports exact paths and diagnostic lines from a read-only CRLF-aware `git diff --no-index --check`, with automatic line-ending conversion disabled for that command only. There are **19 paths with findings**: 17 preserved predecessor files, the preserved supplied GPT review and the new raw TeX log. Newly authored administrative files pass. Preserved sources, SVGs, GPT review evidence and raw logs are not reformatted to satisfy that gate. **No publication whitespace exception is assumed or requested in this revision task**. An unrestricted clean-whitespace result is not claimed.

The combined proposed allowlist contains **123 explicit paths**, all under `papers/PAPER_E/`: 90 preserved predecessor paths and 33 revision paths. The combined repository-relative SHA-256 manifest covers 122 files, excluding only its own self-hash and including the unchanged predecessor manifest. The final minimal-copy inventory gate copies late metadata and verifies every final listed hash; its execution receipt is retained in ignored `.build/` alongside the rendered page QA. No staging, commit, push, fetch, cleanup, release, tag or DOI action occurred.
