THREE-WAY RECIPROCAL GEOMETRY — RECONSTRUCTION v0.1
5 October 2026

Start with output/pdf/three_way_reconstruction_v0.1.pdf.
Editable manuscript: source/main.tex and the six numbered section files.
This is a complete later reconstruction draft, not a rewrite of the historical papers.
It claims no mathematical novelty or priority. No publication is authorized by this edition.

CONTENTS
source/                 Editable multi-file LaTeX manuscript and rendered references
figures/                Ten mathematical figures, each PDF, SVG, and 300-dpi PNG
bibliography.bib        Structured bibliography, matching source/references.tex
verification/verify.py  Exact algebra, finite group, and high-precision checks
verification/results.json
provenance/source_manifest.json     Original locations, snapshots, hashes
provenance/historical/              Unmodified primary historical witnesses and code
provenance/reconstruction/          Unmodified external analytical reports R1–R5
provenance/modern_prior/            Earlier local plus-sign analytical notes
provenance/historical_index.txt     Formula, date, and label reconciliation
provenance/claim_ledger.csv         Important claims, proof locations, and evidence
records/BUILD_VERIFICATION_REPORT.txt
records/PRIOR_ART_AUDIT_CLAIMS.txt
records/artifact_manifest.json     Final deliverable checksums (excluding itself)
tools/                            Figure, evidence, build, and validation scripts
output/three_way_reconstruction_v0.1_bundle.zip   Complete portable delivery bundle

The ZIP contains the manuscript, PDF, figures, evidence snapshots, bibliography,
verification scripts/results, and build records. Its BUNDLE_CONTENTS_SHA256.json
verifies every member. The outer artifact_manifest.json and the ZIP itself are
excluded from the ZIP to avoid circular checksums. Original-location integrity
checks require the local originals; packaged snapshots remain independently
verifiable through the bundle manifest.

REPRODUCTION
1. Run verification/verify.py with Python, SymPy, and mpmath.
2. Run tools/make_figures.py with Python, NumPy, and Matplotlib.
3. Run tools/build_paper.py with Python and Tectonic. The script uses an isolated
   external build directory and a dedicated copied TeX cache. Set THREEWAY_TECTONIC,
   THREEWAY_TEX_CACHE, and THREEWAY_BUILD to override this machine's defaults.
   The default final build is --only-cached; --fetch-tex-dependencies is available
   for an initial dependency fetch on a new environment. Any standard XeLaTeX
   installation with the listed packages can also compile source/main.tex.
4. Run tools/audit_delivery.py with the bundled Python containing pypdf.
   This regenerates the claim ledger, checks links/labels/hashes, and records
   the final artifact manifest. Visual review remains a human/model task and is
   documented separately in the build report.
5. Run tools/package_delivery.py for a convenience ZIP, then rerun the audit to
   include the ZIP checksum in the outer artifact manifest.

Do not rerun tools/prepare_evidence.py over this edition's baseline: it deliberately
refuses to replace the original before-state record. Evidence snapshots are not
editable manuscript files. The external reports and historical originals remain
at their original locations as well.

LIMITS
Author/publication metadata await author review. Historical printed dates are
distinguished from unverified live deposition timestamps. Some historical coefficient
labels remain inconsistent. The old curvature/stability pipelines were not rerun.
The (pi,e) CM question remains unresolved and was not pursued. The standard chain
comparison supplies a reduced spectral quotient, not a full physical dictionary.
The next stage is a dedicated audit of the exact assembled claims, not a release.
