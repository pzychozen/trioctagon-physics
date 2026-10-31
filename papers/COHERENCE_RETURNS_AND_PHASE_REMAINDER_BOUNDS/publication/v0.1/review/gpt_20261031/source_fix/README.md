# Optional source-only table repair — reviewer candidate

Status: prepared and tested in an isolated Linux sandbox; NOT applied to the received package or the Windows checkout.

The scientific content and original 19-page REVIEW.pdf need no correction from this review. XeLaTeX testing found that the generated captions do not end their paragraph before tabularx. This starts some tables alongside the caption and puts columns beyond the page edge.

The single generator edit appends \par to the end of each table caption. The supplied main.tex candidate contains the corresponding seven paragraph breaks. No equation, result, table cell, citation, or scientific content changes. Original main.tex CRLF line endings are preserved. The builder retains its LF convention.

Files:
- TABLE_CAPTION_PARAGRAPH_FIX.diff: explanatory unified diff; no Git command is required or authorized.
- main.tex: proposed generated-source replacement, only the seven paragraph breaks changed.
- build_manuscript.py: proposed generator replacement, only its table-caption string changed.
- SOURCE_FIX_HASHES.json: required before-byte and candidate identities.

Before integration, compare the actual two source-file identities with the before hashes. Do not overwrite a different local file or alter unrelated edits. Preserve the received package as historical evidence. After incorporating the correction in a successor document package, record it, refresh relevant output hashes, and retain original scientific evidence unchanged. No solver, native map, observer, or old scientific checker needs to run. No publication is authorized by this repair note.

The original 19-page PDF can be retained byte-for-byte. The isolated TeX test produced 20 pages because pagination differs. The large table-caption overflow is repaired; minor table-cell/long-filename warnings and title pagination remain to be polished if a TeX-produced PDF is later chosen as the release artifact. No compiled alternative PDF is supplied as a replacement here. The original Windows statement that TeX was not compiled remains true of that task; record the later sandbox test separately.
