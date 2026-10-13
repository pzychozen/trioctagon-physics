# Symbolic Resonance Geometry and Quantum Ring Spectra
## An Exact Discrete-to-Continuum Spectral Correspondence

**Hilmir Frímann Halldórsson · 13 October 2026 · Publication edition v0.1**

[Read the complete 14-page paper](SRG_QUANTUM_RING_v0.1.pdf) · [LaTeX source](SRG_QUANTUM_RING_v0.1.tex) · [Reading guide](READING_GUIDE.md) · [Theorem and proof ledger](THEOREM_PROOF_LEDGER.md)

## The spectral correspondence

For a periodic loop of circumference $L>0$ with $N\geq3$ equally spaced sites, the positive discrete Laplacian has eigenvalues

$$
\lambda_{N,k}=\frac{4N^2}{L^2}\sin^2\!\left(\frac{\pi k}{N}\right).
$$

The paper proves the exact zero-excluded trace limit

$$
\lim_{N\to\infty}\sum_{k=1}^{N-1}\lambda_{N,k}^{-3/2}
=\frac{L^3\zeta(3)}{4\pi^3}.
$$

The proof accounts for both Fourier directions and the even-$N$ midpoint. It gives an explicit finite-size error bound of order $L^3\log N/N^2$, as well as low-frequency dispersion bounds.

Under the paper's declared adoption of the standard quantum kinetic scale, the discrete Hamiltonian is $H_N=\hbar^2 A_{N,L}/(2m)$, with $m>0$ and $\hbar>0$. Its continuum counterpart is the free-particle ring Hamiltonian $H=-\hbar^2(d^2/dx^2)/(2m)$ with periodic boundary conditions. The spectral trace rescales exactly, while finite-band unitary phase estimates quantify convergence of the adopted quantum evolution. These connections are established spectral and quantum mathematics, presented with complete proofs and source attribution.

## SRG provenance and scope

The original SRG constant and its normalization are historical. The October 2026 periodic-loop spectral diagnostic is a subsequent mathematical construction, documented in [SRG Origins](../../../SRG_ORIGINS_FROM_GEOMETRY_TO_RECURSION/publication/v0.1/README.md). The kinetic scale, mass and $\hbar$ are adopted for the quantum comparison; they are not physically deduced from SRG.

This is a mathematical quantum-spectral correspondence. It is not a quantum entanglement, physical computation or faster-than-light theorem. SRG remains an independent research program; no Tri-Octagon kernel or QI dynamics enter this edition.

## Review, evidence and reuse

**Internal GPT disposition: ACCEPTED_WITHIN_STATED_MATHEMATICAL_AND_MANUSCRIPT_SCOPE; no scientific revisions required.** This is not external peer review.

The eleven reviewed payload files retain their original bytes. The saved [65/65 exact-check results](evidence/CHECK_RESULTS.json) and [verification report](MANUSCRIPT_QA_PRESERVATION.md) are inherited from the accepted review edition; no mathematical checks were rerun for publication. The [source map](SOURCE_PROVENANCE_MAP.md), [publication disposition](PUBLICATION_DISPOSITION.md) and [publication manifest](PUBLICATION_MANIFEST.json) record provenance, acceptance and the reduced edition's identities. Retained preparation-time notices are explained in the disposition.

[Standalone SRG research index](../../../../README.md) · [Repository license boundary](../../../../../LICENSE_SCOPE.md)

No new license grant is made.
