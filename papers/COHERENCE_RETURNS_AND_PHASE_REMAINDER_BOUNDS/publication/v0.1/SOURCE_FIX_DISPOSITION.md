# Supplied source-formatting correction

Author-authorized under NCM-PUBLISH-01 on 31 October 2026. The supplied candidate bytes are installed exactly; no additional source editing is included.

| File | Original SHA-256 | Corrected SHA-256 |
|---|---|---|
| manuscript/main.tex | aee31123b1385197baeb77551b97ef8e662d01d18ce8315a55b8de8e5b142099 | 5d0f384b3774dac3d3fc24c8f5262533f26d48f16f07ba270f4693ea2091d604 |
| manuscript/build_manuscript.py | 509d66bdb39b706ef9242d17f4fe05f0672f1cf095dacd6949825cc319d675c0 | badecc9a7b69c59a69523c3732e3e6d5710ebd2a49102e7b3f2096a2e2567e4b |

The generator adds a paragraph terminator after the TeX table-caption string. The generated TeX has exactly seven corresponding paragraph-break insertions, one after each table caption. Main.tex retains CRLF; the builder retains LF. Removing only those insertions, or reversing only the one generator-string change, recovers the original bytes exactly. No equation, theorem, table value, citation or shared content snapshot changes.

Originals are preserved at [provenance/source_before_fix/main.tex](provenance/source_before_fix/main.tex) and [provenance/source_before_fix/build_manuscript.py](provenance/source_before_fix/build_manuscript.py). The [reviewer diff](review/gpt_20261031/source_fix/TABLE_CAPTION_PARAGRAPH_FIX.diff), [review](review/gpt_20261031/GPT_REVIEW.md) and compiler evidence retain their chronology and qualifications.

The canonical 19-page [REVIEW.pdf](manuscript/REVIEW.pdf) remains SHA-256 44aa1a14fabbf0b1230fcb724d18de1e34b833f7ade04735b756e674f8f301f7. It was neither rebuilt nor metadata-edited. The prior isolated 20-page XeLaTeX build is not substituted. Current publication checks compare source bytes and text; they do not execute the builder, compiler or scientific code.

OUTPUT_HASHES.json remains the original pre-fix snapshot. PUBLICATION_MANIFEST.json is the new edition manifest, excluding itself. This correction changes formatting only and does not reopen the investigation.
