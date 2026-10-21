# Publication build

The canonical source is `manuscript.tex`; `tools/build_publication.py` typesets it and synchronizes Markdown using the compiled labels. All six figure files are already supplied. No scientific code is imported or executed.

On the author's Windows environment, use Command Prompt and `call conda activate torment`, then `python -B tools\build_publication.py --tectonic PATH_TO_EXISTING_TECTONIC --cache-dir EXISTING_TECTONIC_CACHE --work-dir EXTERNAL_BUILD_DIRECTORY` from this publication directory. The work directory must be outside the payload. Tectonic is invoked with `--only-cached`; no resources are downloaded or installed. The original build used TeX Gyre Pagella text/math fonts and existing Arial and Consolas. Another complete XeLaTeX installation with the same fonts and packages can also typeset the TeX; identical PDF bytes across toolchains are not promised.

Build logs, AUX files and a synchronization record are written outside the payload. After any rebuild or edit, inspect rendered pages and regenerate the publication manifest before redistribution. The scientific verifier retained within the accepted CA04 archive is evidence, not part of this editorial build command, and was not run for publication.
