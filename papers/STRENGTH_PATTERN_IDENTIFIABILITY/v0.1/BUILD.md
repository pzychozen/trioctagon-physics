# Build the v0.1 paper

The editable source is [source/SPR01_STRENGTH_PATTERN_IDENTIFIABILITY_v0.1.tex](source/SPR01_STRENGTH_PATTERN_IDENTIFIABILITY_v0.1.tex). It is a standalone LaTeX article with an inline bibliography; no external images, local scientific checkout, private evidence file or native kernel execution is needed to compile its text. The response PNG remains a separate unchanged supporting asset.

The publication PDF was built with the existing **Tectonic 0.17.0** compiler and a private copy of an already available TeX cache. No toolchain installation was performed. The source uses the standard article class, Latin Modern fonts, geometry, AMS mathematics/theorems, booktabs, array, xcolor, fancyhdr and hyperref. Compiler binaries, fonts, dependency caches, rendered pages and build logs are not distributed.

Use an existing Tectonic installation with its required resources already cached. From this `v0.1` directory, Windows CMD:

```bat
setlocal
set SOURCE_DATE_EPOCH=1791331200
set TECTONIC_CACHE_DIR=<existing-TeX-cache-directory>
set SPR01_BUILD=<external-output-directory>
tectonic --only-cached --untrusted --keep-logs --outdir "%SPR01_BUILD%" "source\SPR01_STRENGTH_PATTERN_IDENTIFIABILITY_v0.1.tex"
endlocal
```

Replace the bracketed paths and ensure the external output directory exists. A locally required fontconfig configuration may be selected with `FONTCONFIG_FILE`; keep any writable cache and logs outside the checkout. The recorded manuscript date is 7 October 2026. `SOURCE_DATE_EPOCH` stabilizes the PDF creation timestamp for this build; a different compiler/font environment need not reproduce the PDF byte for byte.

Compare the delivered files with [MANIFEST.json](MANIFEST.json). Successful compilation reproduces the document rendering, not the original scientific executions. The public package intentionally omits internal execution prerequisites, and these build instructions do not claim turnkey reproduction of SPR/RFO/native checks.
