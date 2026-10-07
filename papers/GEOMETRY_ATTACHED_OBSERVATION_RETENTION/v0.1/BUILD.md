# Build SGO-01 v0.1

The [editable LaTeX source](source/SGO01_GEOMETRY_ATTACHED_OBSERVATION_RETENTION_v0.1.tex) compiles with the two unchanged PNGs in [figures](figures). Keep the `source/` and `figures/` directory relationship intact. The bibliography is inline. No scientific kernel import, native recurrence, private data file or verifier is required to build the document.

The delivered PDF was compiled offline using an existing **Tectonic 0.17.0** installation and a separate copy of its already available TeX resource cache. No toolchain or package was installed. Standard dependencies are the article class, Latin Modern, geometry, AMS mathematics/theorems, booktabs, array, graphicx, xcolor, fancyhdr and hyperref. Build logs, caches and page renders remain outside the publication package.

From this `v0.1` directory in Windows CMD, with an existing Tectonic executable on PATH and its resources already cached:

```bat
setlocal
set SOURCE_DATE_EPOCH=1791331200
set TECTONIC_CACHE_DIR=<existing-TeX-cache-directory>
set SGO01_BUILD=<external-output-directory>
tectonic --only-cached --untrusted --keep-logs --outdir "%SGO01_BUILD%" "source\SGO01_GEOMETRY_ATTACHED_OBSERVATION_RETENTION_v0.1.tex"
endlocal
```

Create the external build directory before running. If the local font environment needs `FONTCONFIG_FILE`, point it to an existing configuration with writable caches outside the checkout. No machine-specific path is required by the distributed source. The manuscript date and PDF timestamp are 7 October 2026; compiler/font differences may change PDF bytes even when the scientific text is the same.

The final PDF has **14 A4 pages**, **560,211 bytes**, SHA-256 `27bd8783537344d987f53d32d646f76598e8a07095603ddf3f104f2087578613`. Its source SHA-256 is `f516f43d2e4f363deafcec8dabb76765c772453d62ea3c6800d96c0d1ad9724f`. The final build has no overfull boxes, missing glyphs or undefined references; two nonfatal underfull paragraph diagnostics in the source-note area were visually checked. Every page was rendered and inspected. Embedded figure pixels match the distributed v02 PNGs exactly.

[MANIFEST.json](MANIFEST.json) binds every distributed paper-lane file except the manifest itself. Rebuilding the PDF reproduces the presentation, not the historical scientific execution or its private preservation checks. The accepted exact derivations and numerical evidence retain their distinct source identities and scopes.
