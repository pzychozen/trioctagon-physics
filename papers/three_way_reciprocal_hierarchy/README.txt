THREE-WAY RECIPROCAL HIERARCHY / PAPER II / v0.1
5 October 2026

READ: output/pdf/three_way_reciprocal_hierarchy_v0.1.pdf
EDIT: source/main.tex and its six main section files plus evidence appendix.
BIBLIOGRAPHY: bibliography.bib; typeset entries in source/references.tex.
FIGURES: five figures, PDF/SVG/PNG; tools/make_figures.py regenerates them.
VERIFY: run verification/hierarchy/verify_hierarchy.py, verification/cubic/verify_cubic_elliptic.py, verification/verify_bridge.py with Python plus SymPy/mpmath. The two older scripts are byte-identical copies and write only beside themselves. They retain local repository integrity checks; adapt REPO explicitly if rebuilding elsewhere.
BUILD: python tools/build_paper.py. Uses the existing Tectonic executable and copied dedicated cache; environment overrides THREEWAY2_TECTONIC, THREEWAY2_TEX_CACHE, THREEWAY2_BUILD are supported. Cached-only by default. No kernel imports.
AUDIT: python tools/write_evidence.py after a build, then python tools/audit_delivery.py using Python with pypdf/pdfplumber. tools/render_review.py renders pages with Poppler and makes visual review sheets.
PROVENANCE: claim_ledger.csv, bridge_source_map.csv, source_manifest.json, numbered source snapshots, exact work order.
RECORDS: build log, command/tool identity, visual audit, protected-file hash audit and final artifact manifest.

RESULT: Generic Mon(F_n)=S_n; closure genus 1+n!(n-3)/2 over the unchanged F_n target. Generic n=2,3,4 genera are 0,1,13. Cubic marked moduli: X0(6), or X0(3) after forgetting reciprocal 2-torsion.
FINAL BRIDGE STATUS: FINITE S3 BRIDGE ONLY. The exact patch incidence equivalence is retained. No independently justified continuous modular dictionary was supplied by inspected definitions; this is not a universal impossibility claim.

THREE-WAY RECIPROCAL HIERARCHY = PARKED
Paper I, production code, kernel/UI and external source reports remain unchanged. No commits or publication performed.
