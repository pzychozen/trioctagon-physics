# Theorem-to-proof and assumption ledger

Review edition v0.1, 13 October 2026. H = history, D = deduction, A = adoption/diagnostic, U = unresolved. A declared adoption can have exact consequences. Checker assertion counts are not theorem counts.

| ID | Manuscript locator | Claim/status | Assumptions | Proof | Source/provenance |
|---|---|---|---|---|---|
| D01 | prop:positive: 2.2, PDF p. 3 | Self-adjointness, positivity and kernel; **D from A** | N>=3, L>0, periodic cycle; quadrature inner product | Expand differences; shift indices; connectedness | Origins section 5.1; standard graph geometry |
| D02 | prop:fourier: 2.3, PDF p. 3 | Finite spectrum and multiplicities; **D from A** | All N modes; even midpoint once | Fourier orthogonality; substitution; monotonicity on half-cycle | Origins Eq. (13); Friedli-Karlsson pp. 2-3 |
| D03 | thm:limit: 3.1, PDF p. 4 | Full inverse-power trace limit; **D reused from A** | Fixed L>0; real p>1/2; zero removed; full spectrum | Pair k,N-k; uniform summable majorant; dominated convergence; midpoint vanishes | Origins Eq. (16), L20; Friedli-Karlsson Eq. (1) |
| D04 | prop:error: 3.2, PDF p. 5 | Explicit trace error bound; **D supporting derivation** | N>=3, M=floor((N-1)/2)>=1 | Sine inequalities; cubic factorization; harmonic sum, integral tail and midpoint bounds | Complete proof here; no general novelty claim |
| D05 | eq:t3: 3.7, PDF p. 6 | Exact small-cycle traces; **D; finite illustrations** | N=3,4,5,6 | Trigonometric values; characteristic polynomials | New checker; Origins O05 already records N=6 |
| A01 | eq:ham: 4.1, PDF p. 6 | Conventional ring Hamiltonian; **A: external physics** | m,hbar,L>0; periodic H^2 value/derivative domain; free spinless zero-flux system | Operator definition; real Fourier multiplication on maximal domain | Zwiebach section 3; not a native SRG temporal operator |
| D06 | eq:energy: 4.3, PDF p. 7 | Continuum energies and degeneracy; **D within A** | Integer k; simple zero and paired nonzero energies | ODE plus periodic conditions; Fourier completeness | Zwiebach Eqs. (3.13)-(3.24); MIT problem 4(a) |
| D07 | prop:qtrace: 4.1, PDF p. 7 | Continuum inverse-energy trace; **D within A** | p>1/2, zero energy excluded | Substitute energies; pair signed integers | Friedli-Karlsson Eq. (2) circle formula |
| A02 | eq:adopt: 4.5, PDF p. 7 | Discrete kinetic adoption; **A** | Positive kinetic factor times the diagnostic | Explicit definition | Conventional quantum interpretation |
| D08 | cor:quantum: 4.2, PDF p. 7 | Quantum trace correspondence; **D within A** | p>1/2 for limit; all positive modes | Scalar functional calculus and Theorem 3.1 | Sections 4.1-4.2 |
| D09 | eq:unitary: 4.9, PDF p. 8 | Standard unitary phases; **A time law; D consequences** | Real time and energies; includes zero state | Unit-modulus diagonal factors; group law; differentiation | Schrodinger law adopted; Zwiebach section 1 |
| D10 | prop:band: 4.3, PDF p. 8 | Finite-band evolution bound; **D supporting derivation** | Fixed integer K>=0; N>2K and N>=3; real time | Sampling isometry; sinc-square inequality; phase Lipschitz bound | Complete proof here; no general novelty claim |
| H01 | eq:lock: 5.1, PDF p. 9 | Historical selected reference; **H, D solving equality** | Solved gamma_* distinct from Euler-Mascheroni | Original P01 p.3 Eq.(1), p.4 calibration; P06 p.4 Eq.(2), p.6 conflict | Origins L25-L27/O01; original PDFs inspected |
| A03 | cor:calibration: 5.1, PDF p. 9 | Calibrated SRG equality; **A multiplier; D identity** | Dimensionless unit L, or divide by L^3 | Multiply trace limit by 4pi^2/(e phi) | Origins Eq. (17), L22; not an independent spectral selector |
| D11 | eq:qcalibration: 5.4, PDF p. 9 | Mass cancellation; **D within A** | m,hbar,L>0 | Cancel kinetic scale and inverse-energy units | Section 5; no mass prediction |
| D12 | prop:inverse: 6.1, PDF p. 10 | Positive finite inverse trace; **D reused from A** | N>=3, p=1, zero removed | Finite sine product; cotangent differentiation; limit at zero | Origins Eqs. (14)-(15), L19 |
| D13 | prop:finitepart: 6.2, PDF p. 10 | Negative finite part; **A subtraction; D reused** | Specified dimensionless statistic and bulk | Finite sine sum; bulk integral; cotangent expansion | Origins Eqs. (18)-(20), L23; DLMF continued value |
| D14 | eq:mellin: 6.4, PDF p. 11 | Heat-trace Mellin representation; **D, standard** | Finite p>0; continuum p>1/2; sigma>0; zero removed | Gamma substitution; Tonelli and summability | Karlsson section 2.1; sigma is not native time |
| U01 | sec:discussion: 8, PDF p. 12 | Physical identifications remain additional; **U** | No mass, clock, detector or physical preparation selected by the trace | Distinguish spectral operator from state and measurement postulates | SRG-I and Mass-Shell dictionary methodology |

Written proofs establish the infinite limits, domains and inequalities. The checker supplies exact algebra and finite corroboration, not a formal proof-assistant certificate. Supporting deductions are not claimed as novel in general spectral mathematics.
