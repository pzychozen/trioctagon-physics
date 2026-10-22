# SRG Simulation Reconstruction — Volume I

*Three-Point Attraction and Eight-Body Tetrahedral Dynamics*

**Author:** Hilmir Frímann Halldórsson  
**Scientific lead:** GPT  
**Research engineering and manuscript preparation:** Codex  
**Edition:** v0.1.1 · **Date:** 22 October 2026

[Read the 53-page manuscript](MANUSCRIPT/volume_i.pdf). Scientific and editorial review is complete. This repository copy is prepared for final publication authorization; no GitHub push or publication is claimed by this preparation record.

The volume explains three historical programs in execution order: three interacting points in `recursive_attractor.py`, eight centers with tetrahedral displays in `3Dtriangles.py`, and the switching interactions and numerical logs of `plot_1.py`. Its 17 figures and 102 mapped claims connect the code to preserved observations.

The mathematical reconstruction retains sequential updates, carried velocities, the prescribed time-dependent gain, componentwise damping, wrapped coordinates, and the later programs' response factor and binary interaction sign. It establishes an exact drive–damping bookkeeping identity, explains the erroneous unsigned-modulo “teleport” diagnostic, and distinguishes native motion from coordinate seam jumps. Original callback logs show that frame labels can restart while state continues and that velocity reversal can lag an interaction switch. The separately authorized three-point seed-0 replay shows a near-contact followed by separation; it does not recover a lost historical path-inheritance event.

This publication reconstructs historical SRG simulation mathematics. **It does not claim to establish a physical theory of gravity or a theory of everything.** The displayed geometry is a representation of the program's state, not evidence of an additional physical force or container.

- [Construction and mathematical mechanism map](CROSS_STUDY_MECHANISM_MAP.md), [claim/evidence matrix](CLAIM_EVIDENCE_MATRIX.md), and [open questions](OPEN_QUESTIONS_AND_NEXT_VOLUMES.md).
- [Complete LaTeX source](MANUSCRIPT/volume_i.tex), [figure provenance](FIGURE_AND_MEDIA_REGISTER.md), and [build/inspection instructions](REPRODUCIBILITY.md).
- [Evidence index](EXTERNAL_EVIDENCE_INDEX.md) and [source provenance/access guide](SOURCE_PROVENANCE.md): original programs, historical images, both historical movies, both original numerical logs, and complete manifest-listed evidence from the four accepted study packages are included here. Reproduced records remain explicitly distinguished from historical records.
- [GPT editorial acceptance](provenance/editorial_closure/SRG_VOLUME_I_v0.1.1_GPT_EDITORIAL_CLOSURE.md), [exact publication-copy diff](provenance/PUBLICATION_CHANGES.diff), [verification](PUBLICATION_VERIFICATION.md), and [SHA-256 manifest](PUBLICATION_FILE_MANIFEST.json).

Missing historical seeds, the exact original movie/log join, the second simulation's missing numerical trajectory, and broader SRG questions remain unresolved. The third movie/log relationship remains formally **UNLINKED**, despite the accepted content correspondence. Project-internal GPT review is not external peer review.

The manuscript's appendices and preserved study records describe their historical preparation context. Their original workspace paths, review-stage notices and compact-review-ZIP descriptions remain provenance records. For this self-contained publication copy, use the evidence index and reproducibility guide above; no untracked local research folder is required. No original equations, observations, evidence classifications or conclusions were changed.

The repository's existing research-rights boundary applies: scientific manuscripts, figures, datasets and historical research are not automatically covered by its Apache-2.0 software license. This preparation grants no new reuse license. See the preserved [license-scope notice](provenance/REPOSITORY_LICENSE_SCOPE.md).
