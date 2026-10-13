# SRG and Quantum Ring Spectra — reading guide

**Complete review edition v0.1, 13 October 2026. Author: Hilmir Frímann Halldórsson. Prepared for GPT scientific review; not published.**

The paper proves
\[
\lim_{N\to\infty}T_N(L)=\frac{L^3\zeta(3)}{4\pi^3}.
\]
The proof includes both Fourier directions and the unpaired midpoint for even N. This is the exact relation between the October SRG periodic-loop diagnostic and the corresponding continuum circle spectral moment.

Adopting the standard factor \(\hbar^2/(2m)\) produces a discrete quantum kinetic Hamiltonian. Its inverse-energy trace converges to the continuum quantum-ring trace. The paper derives energies, degeneracy and unitary phases and proves a finite-band phase-error bound. This adoption is explicitly separated from historical SRG.

The historical reference \(\gamma_*=\zeta(3)/(\pi e\varphi)\) is exactly \(4\pi^2/(e\varphi)\) times the unit-circle trace limit. This multiplier is an explicit calibration, not an independently selected spectral or measured factor.

## Reading route

| Question | Location |
|---|---|
| What is the scientific connection? | Abstract and §1, pp. 1–2 |
| What geometry and operator are specified? | §2, pp. 2–4; paired-mode diagram p. 4 |
| Why does the full trace converge? | Theorem 3.1, pp. 4–5 |
| What is the finite-size error bound? | Proposition 3.2, p. 5 |
| What happens for small odd/even cycles? | §3.3 and Table 1, p. 6 |
| How does quantum theory enter? | §4, pp. 6–8 |
| What does the standard time law add? | §4.3 and Proposition 4.3, p. 8 |
| Where is the historical calibration introduced? | §5, p. 9 |
| Why is the negative finite part different? | §6, pp. 9–11 |
| What is history, reconstruction or adoption? | §7 and Table 2, pp. 11–12 |
| What is its scientific significance? | §§8–9, pp. 12–13 |

## Deliverables

- SRG_QUANTUM_RING_v0.1.pdf: complete 14-page manuscript.
- SRG_QUANTUM_RING_v0.1.tex: self-contained source, original vector diagram and bibliography.
- THEOREM_PROOF_LEDGER.md: claims, assumptions and proofs mapped to compiled labels/pages.
- SOURCE_PROVENANCE_MAP.md: exact source identities and verified external references.
- MANUSCRIPT_QA_PRESERVATION.md: QA and preservation summary.
- evidence/check_exact.py and evidence/CHECK_RESULTS.json: 65 exact checks and six fixed finite illustrations, separated by category.
- Source-state receipts, final compiler log, compiled labels and literature verification.
- SRG_QUANTUM_RING_v0.1_GPT_REVIEW.zip: complete reviewer package with a member-hash manifest.

## Rechecking

Use Windows Command Prompt in this directory:

~~~cmd
conda activate torment
python -B evidence\check_exact.py
~~~

The checker verifies the displayed table from 60-digit arithmetic and writes its result. It imports no existing SRG or production code. Infinite-limit, domain and inequality proofs remain in the manuscript.

The standalone TeX uses standard LaTeX packages. The supplied local build helper uses this Windows host's Tectonic and a copied cache confined to the new draft; paths may need adjustment on another machine:

~~~cmd
conda activate torment
python -B evidence\build_manuscript.py
~~~

Compiler caches, old builds, full historical source texts and complete external PDFs are excluded from the review bundle. The original figure is in the TeX and needs no separate asset.

SRG remains an independent program. No QI recurrence, synchronizer or entanglement claim is used. No previous research or production files were modified, and no publication action was taken.
