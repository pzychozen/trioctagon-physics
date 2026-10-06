# Verification summary

## Retained checkpoint evidence

| Authority | Exact/source predicates retained |
|---|---:|
| GR0 | 45 |
| GR1 | 38 |
| GR2 | 42 |
| CM0 | 78 |
| SA0 | 226 |
| Total | **429** |

These are heterogeneous predicates/checks, not theorems. The five original `verification` objects are retained without alteration in `retained_evidence.json`. `retained_predicates.json` lists every predicate by its original name and ordinal. Original report, script and results hashes are in the source manifest. No predecessor writer script was rerun.

All original numerical evidence is retained with method and quantity. `NUMERICAL_EVIDENCE.md` includes all stored digits from native and high-precision difference tests, weak-branch residuals, block eigenvalues, the constructed SPD metric, observable changes and quotient/preparation comparisons. The PDF rounds its separate tables for readability. Native complex128 errors do not certify arbitrarily small spectral imaginary parts; GR2's exact coefficient criterion and high-precision data are separate authorities.

## Paper-local checks

`python -B verification/verify_paper.py` passes **61** named predicates, separately from the retained 429. They check:

- exact branch row sum, diagonal balance and weighted Dirichlet identity;
- full triad cycle factor, Bloch coefficients, triad quotient polynomial and discriminant expansion;
- exact N=6/N=12 Fourier injections and distance-one obstruction;
- generic six-ring nilpotent block, rank, square, unfolding coefficients and exact rational discriminant signs;
- D3h character-projection multiplicities, frame/chiral identities and rational closure witnesses;
- original checkpoint/native source hashes, unchanged retained verification objects, ledger proof anchors, manuscript labels and bibliography citations.

Matrix identities are counted as named groups, not one check per scalar entry. These bounded checks validate transcription and evidence links; written mathematical arguments remain essential. No parameter scan, new research result, native test-suite modification or kernel execution is added.

The final result file records Python/SymPy versions, elapsed time, every check, and the manuscript hashes checked. The PDF build record independently hashes every TeX and figure input.

## Publication and preservation checks

The hostile consistency pass is documented in `provenance/CONSISTENCY_AUDIT.md`, with all requested word contexts separately inventoried. The ledger records hypotheses, prior ownership and qualifications, including diagonal versus general SPD balance and the zero-stratum exception.

The final compiler log has no unresolved references, missing characters or overfull boxes. Every PDF page was rendered and visually inspected; see `publication/PDF_QA.md`. This is editorial/typesetting QA, not peer review. The publication revision reruns the same 61 paper-local checks; they remain separate from the retained 429. Editorial preservation checks are recorded separately in `provenance/PUBLICATION_REVISION.md`.

`provenance/preservation.json` compares HEAD, branch, index, status and an aggregate byte hash of every existing repository file outside this new lane. It also compares the fifteen checkpoint files. The baseline is retained, not replaced. No staging, commit, push, release, tag or DOI action is part of verification.
