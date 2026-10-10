# SRG-I v0.1.1 equation audit

R: recovered equation/static code transcription; D: deduction; N: new comparison or standard definition. All 60 labels and equation numbers are retained. The orientation in eq:patch-c is the sole labeled-equation content change. Unlabeled proof steps and the displays 3.5,3.6,4.1,6.2 retain their parent proof coverage.

| Equation | PDF page / TeX line | Class | Anchor | Review / revision |
|---|---|---|---|---|
| 2.1 (eq:glyph) | 2 / 162 | R | P03 p.2 §1.1; p.18 | Tuple indices/ID label normalized and disclosed. Equation retained; actual revision locator refreshed. |
| 2.2 (eq:explicit) | 3 / 184 | R | P03 p.2 §1.1 | Explicit expression; no temporal difference inserted. Equation unchanged. E02 adds the explicit P03 p.2 §1.1 cross-reference in §3.3. |
| 2.3 (eq:consistent) | 3 / 189 | R | P03 p.5 §2.2 | H outside sum; instantaneous equality retained. Equation retained; actual revision locator refreshed. |
| 2.4 (eq:implicit-source) | 3 / 195 | R | P03 p.7 §3.1 | F_i is shorthand for summed f; coefficient remains one. Equation retained; actual revision locator refreshed. |
| 2.5 (eq:feedback) | 3 / 216 | R | P03 p.7 §3.2 | Source cosine, H_i and 1+d_ij squared denominator retained. Equation unchanged. E01 corrects nearby coefficient symmetry to (H_i-H_j)a_ij=0, including zero edges. |
| 2.6 (eq:corridor) | 4 / 253 | R | P03 p.10 §§4.1–4.2 | All conditions treated as predicates, not update law. Equation retained; actual revision locator refreshed. |
| 2.7 (eq:fusion-predicate) | 4 / 259 | R | P03 p.10 §4.3 | Approximate resonance equality not silently replaced by tolerance. Equation retained; actual revision locator refreshed. |
| 3.1 (eq:temporal) | 4 / 298 | R | P03 p.8 §3.3 | Centered temporal difference, no time-step factor printed. Equation retained; actual revision locator refreshed. |
| 3.2 (eq:offset) | 4 / 309 | D | P03 pp.7–8; §3.1 proof | Substitution fixes current feedback and scalar carrier. Equation retained; actual revision locator refreshed. |
| 3.3 (eq:root) | 4 / 314 | D | P03 pp.7–8; §3.1 proof | Literal y+b cancellation, no coefficient change. Equation retained; actual revision locator refreshed. |
| 3.4 (eq:compressor) | 5 / 331 | R | P03 p.8 §3.4 | lambda renamed; equality belongs to compressed branch. Equation retained; actual revision locator refreshed. |
| 3.7 (eq:solution-set) | 5 / 351 | D | Theorem3.1; P03 p.8 §3.4 | Both branch conditions exhausted; includes preceding numbered 3.5–3.6. Equation retained; actual revision locator refreshed. |
| 4.2 (eq:positive-rpco) | 6 / 474 | R | P07 p.3 §2.1 | Sign inside exponential; source prose does not override equation/code. Equation retained; actual revision locator refreshed. |
| 4.3 (eq:signed-rpco) | 7 / 481 | R | Infinity lines49–53 | Sign outside exponential; zero maps to zero. Equation retained; actual revision locator refreshed. |
| 4.4 (eq:positive-branches) | 7 / 510 | D | P07 p.3; monotone exponential | Negative input reciprocal; zero separate. Equation retained; actual revision locator refreshed. |
| 4.5 (eq:signed-branches) | 7 / 527 | D | Infinity lines49–53 | Signed magnitude clamp, a_-/a_+ disclosed notation. Equation retained; actual revision locator refreshed. |
| 4.6 (eq:spatial-rpco) | 7 / 546 | R | RPCO lines5–13; P05 p.1 §2.2 | Default frequency5, decay0.05; field sampler. Equation retained; actual revision locator refreshed. |
| 4.7 (eq:velocity-damping) | 7 / 553 | R | Attractor lines29–31 | log1p absolute velocity retained. Equation retained; actual revision locator refreshed. |
| 5.1 (eq:patch-a) | 8 / 613 | R | Position lines31–40,65–69; P05 p.2 §3 | 0.05 graph plus0.15 componentwise tanh. Equation unchanged; E03 declares the N-by-3 row-array carrier and N-by-N graph action. |
| 5.2 (eq:patch-b) | 8 / 614 | R | Position lines45–51,70–73 | Fusion to updated mean then Gaussian noise. Equation unchanged; E03 declares the N-by-3 row-array carrier and N-by-N graph action. |
| 5.3 (eq:patch-c) | 8 / 617 | R | Position lines75–78 | E03: X_plus = Z diag(1,1,1-.001 sin(2pi .244 s)); right multiplication scales coordinate columns. Source coefficient, loop index and stage order unchanged. Only labeled equation whose content changed; orientation clarified to match Position rows/columns. |
| 5.4 (eq:radius-laplacian) | 9 / 657 | D | P11 p.1; direct differentiation | r>0 only; origin nonsmooth. Equation retained; actual revision locator refreshed. |
| 5.5 (eq:p07-spatial) | 9 / 673 | R | P07 p.4 §2.2 | Printed coefficients; omitted field argument in code remains a conflict. Equation retained; actual revision locator refreshed. |
| 5.6 (eq:torus-embedding) | 9 / 690 | N | §5.3 declared ring torus; comparison with P07 p.4 | New diagnostic coordinates; R>r>0. Equation retained; actual revision locator refreshed. |
| 5.7 (eq:torus-lb) | 9 / 703 | N | §5.3 metric derivation | Induced metric; not historical replacement. Equation retained; actual revision locator refreshed. |
| 5.8 (eq:minor-circle) | 10 / 719 | R | TGMO lines5–14; P05 p.1 §2.3 | Fixed azimuth pi/4, major radius2. Equation retained; actual revision locator refreshed. |
| 6.1 (eq:phase-pair) | 10 / 736 | R | P09 p.2 §2.3; P10 p.2 §2.3 | Shared T and phase; D=iQ. Equation retained; actual revision locator refreshed. |
| 6.3 (eq:quarter-cycle) | 10 / 764 | D | Proposition6.1 | Algebraic orbit, not simulated or observed cycle. Equation retained; actual revision locator refreshed. |
| 6.4 (eq:shift-reversal) | 10 / 797 | N | §6.2 standard signal definitions; P06 p.3 | Two-sided time domain; TS_tau T=S_-tau. Equation retained; actual revision locator refreshed. |
| 6.5 (eq:reflection) | 11 / 816 | N | §6.2 standard plane reflection; P14 p.10 motivation | Unit normal and specified plane; no unspecified g inferred. Equation retained; actual revision locator refreshed. |
| 6.6 (eq:reversor) | 11 / 829 | N | §6.2 definition | Autonomous bijection and involution required. Equation retained; actual revision locator refreshed. |
| 6.7 (eq:rd-block) | 11 / 857 | R | Infinity lines114–135 | Static code rewrite for frozen graph; empty-row mask. Equation retained; actual revision locator refreshed. |
| 6.8 (eq:rd-parameters) | 11 / 863 | R | Infinity lines70–91,114–135 | Actual0.08699 times0.01; half mixing coefficient for D; clocks distinct. Equation retained; actual revision locator refreshed. |
| 6.9 (eq:curvature-tensor) | 12 / 935 | R | P13 pp.3,5,8 | Literal differential expression; vector interpretation conditional. Equation retained; actual revision locator refreshed. |
| 6.10 (eq:phase-feedback) | 12 / 958 | R | P13 p.9 | Arguments suppressed; epsilon_theta renamed to distinguish regularizer. Equation retained; actual revision locator refreshed. |
| 7.1 (eq:H) | 13 / 981 | R | P07 p.6 §3.1; REFU lines5–13 | Four coefficients/decay rates checked. Equation retained; actual revision locator refreshed. |
| 7.2 (eq:H-bound) | 13 / 994 | D | Triangle inequality applied to7.1 | t>=0; bound tends to zero. Equation retained; actual revision locator refreshed. |
| 7.3 (eq:H-sign) | 13 / 1001 | D | Substitution in7.1 | Continuous-clock subsequence; no trajectory calculation. Equation retained; actual revision locator refreshed. |
| 7.4 (eq:embedding) | 13 / 1022 | R | P01 p.7 §3.5 | S_j/E shorthand; denominator and sign caveats. Equation retained; actual revision locator refreshed. |
| 7.5 (eq:memory-ode) | 14 / 1048 | R | P14 p.5 Eq.(10),p.17 Eq.(25) | I is shorthand for source spatial integral. Equation retained; actual revision locator refreshed. |
| 7.6 (eq:memory-solution) | 14 / 1057 | D | P14 p.17 Eq.(25) and displayed solution | Integrating-factor proof; integrability and initialization. Equation retained; actual revision locator refreshed. |
| 7.7 (eq:golden-tanh) | 14 / 1077 | R | P08 p.1 §2.1 | phi sqrt3/3 rewritten phi/sqrt3. Equation retained; actual revision locator refreshed. |
| 7.8 (eq:revolution) | 14 / 1103 | R | P13 pp.4,6 | Literal fixed Omega_X reading; no indexed update invented. Equation retained; actual revision locator refreshed. |
| 7.9 (eq:normal-map) | 14 / 1121 | R | P14 p.16 Eqs.(17)–(18) | Unit normal/positive length; Euclidean fixed-point test. Equation retained; actual revision locator refreshed. |
| 8.1 (eq:sixfold) | 15 / 1164 | R | P14 p.11 §4.4 | Sum-to-product identity; absolute magnitude not sixth harmonic. Equation retained; actual revision locator refreshed. |
| 8.2 (eq:finite-factorization) | 15 / 1191 | D | P15 pp.3–6; AppendixB proof | Only stated per-corridor action and consistent sector-major order. Equation retained; actual revision locator refreshed. |
| 9.1 (eq:new-contraction) | 17 / 1281 | N | §9.3; AppendixA.5 standard proof | New specified Lipschitz map, complete invariant domain; no adoption. Equation retained; actual revision locator refreshed. |
| A.1 (eq:min-branches) | 18 / 1338 | D | P03 p.6 §2.5; AppendixA.1 | Partner held fixed; m cap; full iff proof. Equation retained; actual revision locator refreshed. |
| A.2 (eq:log-roots) | 18 / 1382 | D | P07 p.3; AppendixA.2 | Quadratic roots filtered by sign, discriminant and clamp interval. Equation retained; actual revision locator refreshed. |
| A.3 (eq:chi) | 19 / 1435 | N | AppendixA.4; comparison with P03 pp.7–8 | New temporal coefficient chi; singular cases1 and1/q explicit. Equation retained; actual revision locator refreshed. |
| B.1 (eq:finite-C) | 20 / 1503 | R | P15 pp.3,5 §§2.3,3.1 | Normalized s; P=ss dagger; lambda_c distinct from threshold. Equation retained; actual revision locator refreshed. |
| B.2 (eq:finite-MD) | 20 / 1508 | R | P15 pp.5–6 §§3.2,3.4 | Spectral exponential of projector; angular phase varphi renamed. Equation retained; actual revision locator refreshed. |
| B.3 (eq:finite-factors) | 20 / 1517 | D | P15 pp.3–6 and p.24 | Per-corridor factors in declared order; literal AppendixC mismatch retained. Equation retained; actual revision locator refreshed. |
| B.4 (eq:finite-norm) | 20 / 1559 | D | AppendixB.2; P15 factors | varphi=2pi/3; real alpha,beta; s perpendicular to Ds. Equation retained; actual revision locator refreshed. |
| B.5 (eq:finite-exchange) | 21 / 1572 | D | AppendixB.2; P15 pp.5–6 | Parameter conjugacy alpha to -alpha; not fixed-parameter swap. Equation retained; actual revision locator refreshed. |
| B.6 (eq:generator-memory) | 21 / 1596 | D | P15 pp.8,31 and source exponential p.6 | U=exp(-iH), continuous branch from zero; opposite printed sign identified. Equation retained; actual revision locator refreshed. |
| C.1 (eq:constant-lock) | 22 / 1672 | R+D | P01 p.3 Eq.(1); P06 p.4 Eq.(2) | Solved gamma is derived, not measured; old arithmetic certificate reused. Equation retained; actual revision locator refreshed. |
| C.2 (eq:horizon) | 22 / 1700 | R | P06 p.4 Eq.(3) | No temporal cosine inserted; physical units not assigned. Equation retained; actual revision locator refreshed. |
| C.3 (eq:threshold-integral) | 22 / 1716 | R+D | P06 p.4 Eq.(5) | Single printed mode; alpha_n=0 limit explicit; no mode sum. Equation retained; actual revision locator refreshed. |
| C.4 (eq:entropy) | 23 / 1723 | D | P06 p.5 Eq.(7) | Rearrangement; conservation only at epsilon_f=0. Equation retained; actual revision locator refreshed. |
