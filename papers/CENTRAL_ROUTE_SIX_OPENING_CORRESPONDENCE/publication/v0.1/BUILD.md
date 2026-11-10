# Building the publication edition

Title: Central-Route Accounting and Six-Opening Geometry in the Reciprocal Chiral Exchange Candidate  
Author: Hilmir Frímann Halldórsson (pzychozen)  
Edition: v0.1, prepared 10 November 2026, Atlantic/Reykjavik  
Status: Research edition v0.1 — accepted mathematics; author-authorized repository publication

All content needed to build the PDF is in this edition directory. The bibliography is editable in `references.tex`; the two vector figures and their Python source are under `figures/`. No content is read from Downloads, the inputs archive, or other research workspaces during compilation.

In **Command Prompt**, activate the requested environment and work in this edition directory:

```bat
conda activate torment
python build.py --tectonic "C:\path\to\cached\tectonic.exe" --build-dir "C:\path\outside\this\edition\build"
```

The recorded tool is Tectonic 0.17.0 at `C:\TORMENT\TRIOCTAGON_new\reconstruction\publication\paper_C\build\tools\tectonic\tectonic.exe`. Supply that executable on this machine or an existing equivalent cached installation elsewhere. `build.py` uses `--only-cached --untrusted --keep-logs --keep-intermediates`; it does not enable shell escape or fetch TeX packages. The default build directory is a new system temporary directory. The helper rejects intermediate paths inside the edition. It uses relative content paths, writes the canonical PDF here, and leaves the compiler log, auxiliary labels and build receipt in the external directory. Cached packages/fonts must already be available to Tectonic.

The canonical output is `CENTRAL_ROUTE_SIX_OPENING_CORRESPONDENCE_v0.1.pdf`. `SOURCE_DATE_EPOCH` is fixed to the preparation date; the receipt separately records actual UTC build timestamps and input identities. The existing figures are sufficient for a TeX rebuild. To regenerate them, in the same activated environment run:

```bat
python figures\render_figures.py
```

This requires NumPy and Matplotlib and regenerates PDF/SVG/PNG figures from accepted formulas. It is explanatory plotting, not a scientific verification suite or trajectory simulation. Original input assets are preserved in the complete review package; the new script adapts their notation and presentation.

The complete package's `verification/` directory records interpreter/compiler/Poppler versions, PDF metadata and font checks, text extraction, resolved labels, exact-page renders and individual inspection. Any content-changing rebuild requires fresh PDF checks and inspection of every final page; the original inspection receipt certifies only its recorded PDF hash. `audit_candidate.cmd` shows the local document-check command. Python uses the torment environment, including the installed pypdf 7.0.0 document inspection dependency.
