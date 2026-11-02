# Native Potential Descent and Closed Coherence Coordinates in the Tri-Octagon Map

**Author:** Hilmir Frímann Halldórsson  
**Status:** Review draft v0.1, 2 November 2026; 16 pages. Underlying results have project-internal mathematical acceptance. The assembled manuscript awaits GPT/author review; no external peer review is claimed.

Open [the PDF](NATIVE_POTENTIAL_AND_COHERENCE_v0.1_REVIEW.pdf). The complete editable source is [manuscript/main.tex](manuscript/main.tex) plus the nine companion `.tex` files in that directory. No external figures, bibliography database, project runtime, or scientific helper is needed to compile it.

The [claim/source ledger](CLAIM_SOURCE_LEDGER.md) maps the paper to the accepted proofs and inherited results. The [preparation report](PREPARATION_REPORT.md) records the exact comma deletion, input identities, build commands, final hashes, and the complete page inspection. [SOURCE_MANIFEST.json](provenance/SOURCE_MANIFEST.json) records the actual source copies. The two notes and their existing helper/result pairs are kept in separate directories under `evidence/`.

## Build on the preparation machine

Run in **Command Prompt** using the existing `torment` environment:

```bat
call conda activate torment
cd /d C:\TORMENT\TRIOCTAGON_new\research\NATIVE_POTENTIAL_INFORMATION_PAPER_01
python -I -B build_review.py --tectonic C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\tectonic\tectonic.exe
```

This uses the already installed Tectonic 0.17.0 and its cached resources with `--only-cached --untrusted`. It writes `build/main.pdf`, the named review PDF at the package root, and build receipts/logs under `build/`. No package installation, downloads, shell escape, project imports, or scientific computation is part of this build. The wrapper's Fontconfig configuration and cache stay under `build/`; environment settings apply only to the compiler subprocess, not the user's persistent environment.

If the package is extracted elsewhere on Windows, change the `cd /d` path and pass the path to an already installed Tectonic executable. The source itself is portable: from the extracted package root, with an existing compatible TeX installation and its required resources already available, the equivalent compiler invocation is:

```text
tectonic --only-cached --untrusted --keep-logs --keep-intermediates --outdir build manuscript/main.tex
```

Create `build/` first when using the direct invocation. It writes `build/main.pdf`; copy that file to `NATIVE_POTENTIAL_AND_COHERENCE_v0.1_REVIEW.pdf` at the package root so the packaged evidence links resolve relative to the PDF. The supplied wrapper performs both steps. The complete source is portable; the installed compiler and its resource cache are not bundled. A different toolchain can produce different PDF bytes even when the rendered content is identical.

## Inspection and evidence

The final PDF was rendered with the existing Poppler 26.07.0 and every page was visually inspected. `inspection/DOCUMENT_CHECKS.json` records the document/byte checks, and `inspection/VISUAL_INSPECTION.json` records the final page pass tied to the PDF's SHA-256. Temporary rendered pages remain in the preparation workspace and are omitted from the ZIP.

`inspect_document.py` is the preparation-machine audit: it checks the manuscript, PDF, archived copies, and original local input paths. Its recorded results are included. It is not required for compilation; after relocation, original Windows input paths may be unavailable. `verify_package.py` performs a portable, standard-library-only verification of the ZIP CRCs and the entry hashes in its manifest:

```bat
python -I -B verify_package.py NATIVE_POTENTIAL_INFORMATION_PAPER_01_REVIEW_PACKAGE.zip
```

The archived `evidence/*/exact_algebra.py` files and their JSON results belong to the accepted investigations. **Do not run them as part of the document build.** They were copied without execution. Primary-source snapshots under `provenance/primary_sources/` are reading evidence, not extra compilation dependencies. The unchanged proof-note bodies retain their historical local links; manuscript references instead use packaged evidence paths and the supplied stable reading-edition references.

The original information note is preserved under `provenance/originals/`. Only the specified comma in its equation (24) was removed from the original local note; the [correction receipt](provenance/correction_receipt.json) identifies both versions and verifies the one-byte relationship.

## Package boundary

`PACKAGE_MANIFEST.json` hashes every payload file except the manifest itself. `package_review.py` builds the review ZIP, verifies its contents, and writes its final SHA-256 to the adjacent `.zip.sha256` file. The archive does not contain its own final checksum. Keep the ZIP and checksum together when passing the package for review.

This task ends at manuscript preparation. No scientific helper reruns, native evaluations, trajectories, profile solves, Git operations, repository adoption, commit, push, release, DOI deposit, or publication were performed.
