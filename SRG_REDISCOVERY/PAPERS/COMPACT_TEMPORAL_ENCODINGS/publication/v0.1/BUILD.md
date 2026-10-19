# Build and verify this edition

The accepted PDF is the authoritative published artifact. Its SHA-256 is:

    374b520ccf69a4ea56f5de93f9443d968385c0aa090d1c651fa3cf5e58a3dd20

## Verify the downloaded files

Using an existing Python 3 installation, run from this directory:

    python -B tools/verify_publication.py

The verifier reads only the declared files, checks their sizes and hashes, checks the manifest hash through SHA256SUMS.txt, and validates the fourteen claim locators. It does not execute a scientific model or benchmark. Its success confirms the file identities, not a new independent proof audit.

## Compile the editable manuscript

The input set is manuscript.tex, its nine TeX components, tables/*.tex and figures/*.pdf. Use an existing XeLaTeX installation with TeX Gyre Pagella and Latin Modern fonts and the packages named in manuscript.tex. No font binaries are bundled. In a working copy, create a build directory and run:

    mkdir build
    xelatex -interaction=nonstopmode -halt-on-error -output-directory=build manuscript.tex
    xelatex -interaction=nonstopmode -halt-on-error -output-directory=build manuscript.tex
    xelatex -interaction=nonstopmode -halt-on-error -output-directory=build manuscript.tex

This portable XeLaTeX alternative is documented, not represented as executed for the publication. The accepted PDF was compiled with Tectonic 0.17.0 using an existing offline cache. With a compatible populated cache, the equivalent Tectonic command is:

    tectonic --only-cached --untrusted --keep-logs --outdir build manuscript.tex

The original build used SOURCE_DATE_EPOCH=1792368000. TeX distributions, font versions and build tools may produce different PDF bytes or line breaks. The generated build/manuscript.pdf is a reconstruction; keep the accepted PDF unchanged. Inspect every rebuilt page before treating it as a new edition.

## Reproduction boundary

The editable tables and computed figure files are the retained presentation inputs. Public compilation requires no private archives, kernel, TORMENT installation, external service or native trajectory. SVG figure files are also supplied for inspection, but edits would create a different edition.

This minimal publication supports document reconstruction from accepted computed assets. It does not supply private raw measurements, historical benchmark programs or their review evidence, and does not claim that the empirical campaign can be rerun from this directory. No benchmark, simulation, new noise trial, decoder repair or figure recomputation was performed for publication.
