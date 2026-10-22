# Manuscript source and publication PDF

[volume_i.pdf](volume_i.pdf) is the separately rebuilt publication copy of accepted edition v0.1.1. Its [editable source](volume_i.tex) includes eight section files, references, 17 figure includes and 35 image assets. Only cover/PDF metadata, running-header, C07 manuscript-status sentence and closing review-status text change from the accepted manuscript. The scientific text, equations, numerical results, captions, figures and historical source copies retain the accepted content.

The [exact diff](../provenance/PUBLICATION_CHANGES.diff) and [verification](../PUBLICATION_VERIFICATION.md) identify every change. The accepted R1 archive and its subsequent GPT closure receipt remain preserved under provenance/.

Follow the [publication build guide](../REPRODUCIBILITY.md) for Windows Command Prompt, conda activation, short-path independent build copies, pinned compiler acquisition and the existing-compiler exception. Fresh compiler acquisition must precede the builder; it needs network access, and the first build may fetch uncached TeX dependencies. No compiler or build cache is distributed. A compatible XeLaTeX installation is a separate alternative; cross-environment byte identity is not promised.

The build and acquisition scripts are unchanged from the accepted edition. They do not import original simulation programs or execute scientific checkers. The preparation used a verified compiler and an independent copied cache. The PDF was built from the exact distributed TeX and figure inputs.

F03 and F04 retain their accepted exact pixel crops; all other scientific figure assets retain their accepted bytes. See the [figure register](../FIGURE_AND_MEDIA_REGISTER.md) and [evidence index](../EXTERNAL_EVIDENCE_INDEX.md) for included original media, logs and provenance. Appendix A/B workspace paths and original review-package descriptions are retained historical context; this publication directory is self-contained.
