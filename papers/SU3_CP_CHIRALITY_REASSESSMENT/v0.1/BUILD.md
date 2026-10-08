# Build SCC-01 v0.1

The [editable LaTeX source](source/SCC01_SU3_CP_CHIRALITY_REASSESSMENT_v0.1.tex) is standalone, with its bibliography embedded. No figures, scientific kernel, private data or scientific/reviewer checker is needed to build the document.

The delivered PDF was compiled offline with an existing **Tectonic 0.17.0** installation and a separate copy of its already available resource cache. No tools or packages were installed. The source uses the article class, geometry, AMS mathematics, unicode-math, Latin Modern, TeX Gyre Pagella text/math fonts, booktabs, longtable, array, fancyhdr, xurl and hyperref. These resources must already be present in the compiler's cache. Font files are not distributed here.

From this `v0.1` directory in Windows CMD, with an existing Tectonic executable on PATH:

```bat
setlocal
set SOURCE_DATE_EPOCH=1791417600
set TECTONIC_CACHE_DIR=<existing-TeX-cache-directory>
set SCC01_BUILD=<external-output-directory>
tectonic --only-cached --untrusted --keep-logs --keep-intermediates --outdir "%SCC01_BUILD%" "source\SCC01_SU3_CP_CHIRALITY_REASSESSMENT_v0.1.tex"
endlocal
```

Replace the placeholders and create the external output directory first. Keep build output, temporary files and caches outside the checkout. If the local font environment requires `FONTCONFIG_FILE`, point it to an existing configuration with writable external caches. No Python environment is required for document compilation. Do not run a scientific checker to build this paper.

The manuscript date and fixed PDF timestamp are 8 October 2026. Compiler, font or cached-resource differences can change PDF bytes. The delivered PDF has **19 A4 pages**, **154,928 bytes**, SHA-256 `ec21d452025841bff6347f11a47a09ef53dcc7bb349a4218e8e768be4a489854`. Source SHA-256: `89f9f1f97a5bb8e8568062814da40bd3deac3c7c2825978265d30919022d04be`.

The final build had no overfull boxes, missing glyphs or undefined references. Four nonfatal underfull paragraph diagnostics were visually checked. Every final page was rendered and inspected, including the accepted M01 `I_f(I_f+1)` correction in equation (A.4). Mathematical/table environments and crosswalk table rows are unchanged from the accepted inputs. Extracted PDF content was compared after explicitly accounting for headers, footers, line wrapping and the permitted editorial changes.

[MANIFEST.json](MANIFEST.json) records sizes and hashes for every distributed paper-lane file except itself. The manifest's own identity is recorded in the external publication closeout. Root README navigation is outside the paper manifest and is covered by the scoped commit. Rebuilding this document does not replay or independently authenticate the historical scientific execution. See the [publication disposition](PUBLICATION_DISPOSITION.md) for evidence-access and review limits.
