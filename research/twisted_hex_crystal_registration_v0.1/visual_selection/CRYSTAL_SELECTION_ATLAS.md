# Twisted hex crystal visual selection atlas

Research visualization for Hilmir's visual selection. No t value or handedness has been designated canonical.

Open [the standalone interactive viewer](crystal_selection_viewer.html) in a browser. It has no network dependencies and opens at the t=0 reference, displaying both hands. The preset buttons reproduce the nine exact samples; the continuous slider explores the same verified family. Nothing is saved as a design choice.

## Comparison sheets

- [TWIST_PLUS: all nine samples](crystal_selection_sheet.png)
- [TWIST_MINUS: all nine samples](crystal_selection_sheet_minus.png)
- Side-by-side hands: [s/8](handedness_s_over_8.png), [s/4](handedness_s_over_4.png), [s/2](handedness_s_over_2.png).

Each individual render contains perspective, exact orthographic top and exact orthographic side projections. Camera, physical host scale, projected bounds, marker sizes and framing are fixed across the entire atlas. Each hand receives the same views and treatment.

Blue circles mark upper contacts; orange diamonds mark predicted lower contacts; hollow gray squares separately mark host edge centers. Orange dashed segments show the lower-center residual. Coincident markers are nested so both contact classes remain visible in the zero-reference top projection. Markers and wire lines are intentionally shown through translucent surfaces for comparison; they do not depict occlusion or new geometric edges.

## Values

Here s = sqrt(2)-1. Delta is the signed relative footprint offset: positive in TWIST_PLUS, negative in TWIST_MINUS. The table gives its magnitude. Alpha is the same for both hands.

| ID | t | t, width-one units | alpha | delta magnitude, degrees | Individual three-view renders |
|---|---|---:|---:|---:|---|
| 00 | 0 | 0.000000000 | 1.000000000 | 0.000000 | [PLUS](candidates/candidate_00_plus.png) · [MINUS](candidates/candidate_00_minus.png) |
| 01 | s/16 | 0.025888348 | 0.996002855 | 5.124569 | [PLUS](candidates/candidate_01_plus.png) · [MINUS](candidates/candidate_01_minus.png) |
| 02 | s/8 | 0.051776695 | 0.984293012 | 10.168436 | [PLUS](candidates/candidate_02_plus.png) · [MINUS](candidates/candidate_02_minus.png) |
| 03 | s/6 | 0.069035594 | 0.972575399 | 13.449476 | [PLUS](candidates/candidate_03_plus.png) · [MINUS](candidates/candidate_03_minus.png) |
| 04 | 3s/16 | 0.077665043 | 0.965662085 | 15.058275 | [PLUS](candidates/candidate_04_plus.png) · [MINUS](candidates/candidate_04_minus.png) |
| 05 | s/4 | 0.103553391 | 0.941270941 | 19.733898 | [PLUS](candidates/candidate_05_plus.png) · [MINUS](candidates/candidate_05_minus.png) |
| 06 | s/3 | 0.138071187 | 0.902123071 | 25.561446 | [PLUS](candidates/candidate_06_plus.png) · [MINUS](candidates/candidate_06_minus.png) |
| 07 | 3s/8 | 0.155330086 | 0.880611606 | 28.283771 | [PLUS](candidates/candidate_07_plus.png) · [MINUS](candidates/candidate_07_minus.png) |
| 08 | s/2 | 0.207106781 | 0.812519920 | 35.657130 | [PLUS](candidates/candidate_08_plus.png) · [MINUS](candidates/candidate_08_minus.png) |

## Scope and the zero reference

**t=0 means no relative footprint twist and no strict contraction:** alpha=1 and delta=0. The imported face list still contains the previously verified one-step ring-to-ring connections, including its declared tessellation diagonals. Those connections have not been rewired to manufacture an untwisted mesh. Consequently, a crossed band remains visible even at the zero reference. The t>0 geometric-chirality classification from the parent report is not asserted for this endpoint.

For every nonzero sample the existing candidate definition is used without modification. The upper tips coincide exactly with the three highest-horizontal-edge centers. The lower tips lie on the corresponding finite lower edges and remain a distance t from their centers. t=0 is an endpoint reference, not a selected answer; the earlier t=s/4 witness has no special standing.

This atlas compares the **existing proposed ring and face construction**. It does not establish that this construction or any member is uniquely prescribed by the host. Hilmir's visual selection is the next decision; no mathematical optimum has been invented.

## Reproducibility and verification

`render_selection_atlas.py` imports `canonical_points` and `candidate_faces` from the unchanged parent verifier without calling its `build()` routine. It reads the host, alpha/delta expressions, stored symbolic coordinates and face list from the verified JSON. The HTML embeds affine coordinate coefficients generated symbolically from that same function, plus alpha/delta expressions translated from SymPy to JavaScript. There are no manually redrawn crystal coordinates or external libraries in the viewer.

For all nine samples and both hands, exact symbolic checks cover upper equality, lower height, panel-plane membership, finite-edge bounds and residual squared=t². That is 54 upper contacts and 48 nonzero lower contacts, plus six lower endpoint-reference contacts. The generated affine renderer is compared against the imported coordinates for every sample and both hands. This is a bounded visualization sampling exercise, not a model trajectory or scientific parameter optimization.

See [candidate_values.json](candidate_values.json), [render evidence](RENDER_EVIDENCE.json), [viewer QA](VIEWER_QA.json), and [preservation receipt](FINAL_PRESERVATION.json). The parent packet's files, manifest and historical reconstruction remain unchanged; this subfolder has its own manifest.

The browser security policy blocked opening the local HTML URL. No alternate browser or navigation workaround was used. Viewer QA therefore consists of offline JavaScript/control tests, SVG-coordinate checks and parity against the Python projections. The static PNG layouts were visually inspected; live browser layout and mobile interaction are not claimed as browser-verified.

To rebuild only this atlas, use Python with NumPy, SymPy and Matplotlib:

```text
python -B render_selection_atlas.py
```

No staging, commit, push or accepted-paper changes. Stop for Hilmir's visual selection.
