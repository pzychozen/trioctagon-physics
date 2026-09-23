# Symbols, results and hypothesis ledger

Paper E v0.1. These are manuscript results, not a new independent scientific acceptance. The exact proofs are in the manuscript; 66 symbolic predicates check selected algebraic identities only.

| Symbol | Meaning |
|---|---|
| K / H | Inspected staged exponential-envelope core / separate preserved committed EMA core |
| Ω=x+iy | Three complex channel amplitudes; x,y are ordered real channel triples |
| κ, ρ | Euclidean state norm; κ/(1+κ) |
| q,N,θ | Discrete clock, sector count and 2πq/N; θ is not mean channel phase |
| t,dt | Stored historical time and its increment; dt is absent from the complex recurrence |
| ε,g,k,δ | Cubic coefficient, graph coupling, on-site coefficient triple and complex forcing |
| L3 | Diagonal -2, off-diagonal +1: negative conventional complete-graph Laplacian |
| λ_phase | Strength of the additional simultaneous phase operation |
| λ_vp,γ,ℓ | Scalar amplitude coefficient, staged envelope rate and lock angle |
| A | Frozen λ_vp ρ exp(-γt), allowed to have either sign |
| z | Source scalar height, with K and H formulas kept separate |
| M,C,T | Macro vector, channel-area chirality and αM+βC total |
| α,β | Real blending coefficients, default 1 and 0.5 |
| Q(X) | X1²+X2²-X3², the macro-cone quadratic form |
| Uj,Lj | Frozen macro extrema paired at identical horizontal coordinates, A>0 |
| Rδ,H,S | Vertical-axis rotation; height reflection; reflection of coordinate 2 |
| J | Im(Ω1 conjugate(Ω2) Ω3), a cubic scalar distinct from C |
| m | H's EMA memory; unrelated to the temporary m=norm(M) in Section 9 |
| H_z | max over scalar history of abs(z), plus 1e-9 |
| r,R,χ | History-torus minor radius, major radius and normalized minor angle |
| D99 | Selected-history 99th-percentile norm denominator in the viewer |
| dZ,dφ,dq,dκ | Full diagnostic components per stored transition |
| I | Sum of channel intensities, norm(Ω)²; not a calibrated energy |
| D,V | Unforced pre-sync increment and pre-sync updated complex vector |
| 𝒱 | Real potential; distinct from the vector V and from historical “Z energy” |

| Named manuscript result | Hypotheses and exact content | Evidence class |
|---|---|---|
| Theorem 1 | Frozen A≠0: six isolated scalar extrema; sign cases; A=0 degeneration | Reproved accepted reconstruction |
| Proposition 2 | Nonzero A, twelve uniform sectors: exact extrema iff ℓ∈(π/6)Z | Reproved accepted reconstruction |
| Theorem 3 | Finite z,θ: Q(M)=0, norm(M)=sqrt(2)abs(z) | Reproved accepted reconstruction |
| Theorem 4 | Frozen A>0: U0,L2,U1,L0,U2,L1 order; no gap identification | Reproved accepted reconstruction |
| Theorem 5 | Frozen A: five transformation identities; sampled inherited reflection has separate grid condition | Expanded derivation for Paper E |
| Theorem 6 | Ordered channel coordinates: C=x cross y; complex scaling and conjugation | Accepted Paper B identity, rederived |
| Theorem 7 | Finite Ω: Gram identity and bound norm(C)≤κ²/2; equality exactly equal real/imaginary norms and perpendicularity | Bound reused; equality proof expanded |
| Proposition 8 | Real α,β: pointwise cancellation; dynamic attainability not asserted | Expanded derivation for Paper E |
| Proposition 9 | Known history normalization; R>rmax>0, finite κ>0 and chosen angle branch: conditional torus inverse | Expanded derivation for Paper E |
| Proposition 10 | Default changing clock and finite defined arithmetic: full v≥0.5 | Reproved source diagnostic consequence |
| Theorem 11 | Real coefficients, noiseless unforced pre-sync update: exact intensity increment including quadratic remainder | Exact budget derived for Paper E |
| Proposition 12 | Six real coordinates: unforced pre-sync increment equals minus real gradient of existing potential | Accepted potential relation, fully proved |
| Proposition 13 | abs(m0)≤1, finite J inputs: bounded EMA and explicit weighted-history formula | Boundedness reused; full formula proved |

Other exact results: product-to-sum planar decomposition; blend norm and cone defect; normalization derivative; staged pointwise conjugation; loss-of-information counterexample; separating diagnostic examples; intensity/potential increase witness. These are mathematical reasoning, not equations claimed to have been recovered from earlier papers.

Numerical results are separately identified in the manuscript and `evidence/plot_data_results.json`. Frozen geometry does not imply evolving-trajectory symmetry. Passing finite replays does not establish global stability. The six-gap spatial interface and a physical energy law are not supplied by any listed theorem.
