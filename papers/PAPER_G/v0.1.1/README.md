# Paper G v0.1.1 - local review draft

**Geometry-Attached Axial Observables, Period-Doubling, and Certified Entrance Capture in the Tri-Octagon Map**  
Hilmir Frímann Halldórsson - 4 October 2026

**LOCAL REVIEW DRAFT.** Prepared for author/scientific review. Not externally peer reviewed; no publication, journal-acceptance or DOI claim. Internal acceptance of M1/M2/repaired M3 does not publish this paper or authorize software changes.

- [Complete review PDF](publication/PAPER_G_v0.1.1_LOCAL_REVIEW.pdf)
- [Editable complete LaTeX manuscript](source/paper_g.tex)
- [Claim/source/proof map](CLAIM_SOURCE_MAP.md)
- [Portable computational supplement and rebuild instructions](reproducibility/README.md)
- [Axial Observables file-level implementation contract - design only](OBSERVATION_IMPLEMENTATION_CONTRACT.md)
- [Build, validation and preservation report](BUILD_AND_REVIEW.md)

The paper proves an exact geometry-attached planar axial construction and finite-step source laws, presents M2's certified local supercritical flip, and separately presents repaired M3's fixed-parameter entrance capture. It preserves the squared-norm-three entrance, direct N=301 inclusion, q<=4789/5000 per two steps, separate H-symmetry certificate and phase-parity summability. **M2-to-M3 branch continuation remains unproved and is not a prerequisite.** Numerical illustrations are explicitly separated from interval certificates and exact algebra. No physical magnetic-field validation, M4, ring development or X01 adoption is claimed.

Four source-backed figures are included as vector PDFs and PNGs: geometry/decomposition, local onset, trap summary and signed trajectories. The source script and data are included. The minimal proof replay needs only Python3.11 and mpmath1.3.0; it recomputes enclosures, not just saved verdicts. Plotting and typesetting are optional additional dependencies.

The companion contract specifies actual files, proposed public signatures/result fields, zero-component and numerical policies, immutable parent-bound caches/exports, adjacency rules, static exact-model proof cards, tests, versions and installed kernel/UI pairing. It does not implement those features or activate the disabled detached-analysis attestation lane.

This edition revises only manuscript notation, editorial text and bibliography. The original v0.1 source, PDF and evidence remain preserved; its original README is archived as `../README_v0.1.md`, while the shared Paper G index points at both editions. Only Paper G documentation is authored. Existing papers, kernel/UI source and pre-existing work are preserved. Build/replay/render scratch is external. No staging, commit, push, root README change or publication is part of this task.

Redistribution decision: this is a local review assembly, including attributed evidence copies. Author publication approval and the scope for redistributing those copies remain for final review. The software Apache-2.0 license does not automatically license manuscripts, figures or research datasets; [repository license scope](../../../LICENSE_SCOPE.md) remains unchanged. No external full PDFs or their figures are redistributed.

## Proposed root index entry - not applied

```markdown
- [Paper G - Geometry-Attached Axial Observables, Period-Doubling, and Certified Entrance Capture (v0.1.1)](papers/PAPER_G/README.md)
```

Use only after review and explicit publication approval; retain whatever accepted status is then authorized.

## Revision records

- [Changes from v0.1](CHANGELOG.md)
- [Edition manifest](EDITION_MANIFEST.json)
- [Exact changed repository paths](CHANGED_FILES.txt)
- [Package checksums](SHA256SUMS.txt)
- [Preservation receipt](records/preservation.json)
- [Scientific/source consistency receipt](records/consistency.json)

This edition copies accepted scientific inputs, verifier code and figures unchanged. New replay outputs are stored separately from the v0.1 preparation outputs.
