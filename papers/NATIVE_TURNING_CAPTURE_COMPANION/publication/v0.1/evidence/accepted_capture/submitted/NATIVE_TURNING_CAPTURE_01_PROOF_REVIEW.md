# NATIVE_TURNING_CAPTURE_01 — proof review

Investigator: Codex. Author/research direction: Hilmir Frímann Halldórsson (pzychozen). Date: 10 November 2026, Atlantic/Reykjavik. Status: **bounded investigation completed; returned for scientific review**. This report does not mark itself accepted or commission a paper.

## R1. Result and dispositions

**The exact original turning entrance reaches the interior of the existing coherent domain at update 50.** A connected dyadic interval certificate starts at the exact entrance and encloses all 50 full native updates. A separately implemented exact-rational checker verifies every link. Consequently the original trajectory, which has the inherited strict early turn, converges by the existing theorem to the unique aligned unequal amplitude profile, up to a limiting common phase. A qualitative open neighborhood of this entrance has both properties at the same coefficients.

| Package | Disposition | Evidence |
|---|---|---|
| N01 | DISTINCT_GAP, bounded to the inspected corpus | `PRIOR_WORK_COMPARISON.md`, `SOURCE_IDENTITIES.json`, timestamped `logs/PRIOR_GATE.json` |
| N02 | Completed, one seed, 50 updates; numerical only | `scripts/explore.py`, `data/EXPLORATION.json` |
| N03 | Certified strict entry at N=50 | `data/CERTIFICATE.json`, `data/CERTIFICATE_CHECK.json`, R3–R5 below |
| N04 | Inherited convergence applies; qualitative neighborhood proved | R6–R7; original `thm:convergence` |
| N05 | Same-trajectory connection explained with scope retained | R8 |

The first numerical domain hit was 41. This report neither certifies that as the earliest entry nor needs an earliest-entry result. The chosen update 50 has substantial terminal margins.

## R2. Frozen object, sources and prior-work gate

Use complex triples with the simultaneous ordered map

\[
v_i=\Omega_i+\epsilon\Omega_i(k_i-|\Omega_i|^2)
 +g\sum_{j\ne i}(\Omega_j-\Omega_i),\qquad
\delta_i=\lambda\sum_{j\ne i}\sin(3[\operatorname{Arg}_0v_j-\operatorname{Arg}_0v_i]),
\qquad F_i(\Omega)=v_i e^{i\delta_i}.
\]

Here Arg0(0)=0, every prestage uses the old triple, and every kick uses the completed prestage triple. The constants and initial singleton are exactly

\[
\epsilon=1/10,\quad g=1/60,\quad\lambda=1/300,\quad
k=(999/1000,1,1001/1000),\qquad
\Omega_0=(1+i,1+i,1-2i).
\]

The target D consists of triples with all moduli in [9/10,11/10] whose ordinary phases admit a common interval of width at most π/12, at any common angle. Only a common full turn is identified; phases separated by 2π/3 are not identified. The initial moduli √2,√2,√5 put the entrance outside D. The counter n counts updates, without a physical time assignment.

The controlling published source is preserved as `sources/collective/main.tex`, SHA-256 `40b6ca84ca136453b045386e2dead012fc8fcd7984b845d159ae6d6c8a6c2292`, matching the supplied blob identity `de060bd217261af9bc87a52f0a79fe6fa4f6495d`. Relevant locations are `eq:parameters`, `eq:entrance`, `eq:certturn`, `sec:domain`, `thm:convergence`, `eq:radialbound`, `eq:fullbound`, `eq:limits`, `eq:Cdecay`, and `sec:prior`. Blob identities were calculated directly from file bytes, without Git operations. `sources/dynamics.py` matches the supplied reference byte for byte; its `_advance`, `phase_sync`, and `arg0` were inspected for formula/order parity, not imported or executed. Its separate zero-lambda bypass is preserved as a source convention; lambda is nonzero here. At nonzero prestages, the implementation's modulus/phase reconstruction is mathematically equal to multiplication by exp(iδ). Binary64 rounding is not the exact map.

N01 inspected the primary claim/source map and evidence, the local catalog and atlas, and later native results on returns, potential/closure, phase reconstruction, natural core motion, response geometry, Paper G capture, drift, and strength-to-pattern conversion. The comparison records coefficients, entrance or domain, hypotheses, conclusion and the precise reason each does not supply this connection. In particular, existing attraction local to a branch, a theorem assuming D membership, and capture of a different seed at different coefficients do not establish entry here. Recent exchange/transport work evolves a different extended system. The disposition is DISTINCT_GAP within that stated search, not an exhaustive novelty claim. It was frozen before the first new trajectory evaluation.

## R3. Exploration and selection of the certificate target

One 90-decimal-digit mpmath run evaluated the direct Arg0 formula, with a simultaneous independent binary64 transcription of the source's modulus/phase form as a numerical consistency comparison. The archived records contain every complex state at n=0,...,50, moduli, ordinary phase width, and each evaluated prestage. The minimum ordinary containing arc is computed as 2π minus the largest circular gap among the three sorted arguments modulo 2π; this avoids a principal-argument branch cut creating spurious decoherence.

The administrative limit was 512 updates. The run stopped after 50 when all radii were between .95 and 1.05 and the arc width was below π/24. The numerical terminal width was about 0.1261005972 radians; the minimum prestage modulus was about 0.8716530117, and the largest discrepancy with the binary64 comparison was about 6.22×10^-16. These are exploratory observations, not interval bounds or additional theorem counts.

Exploration selected only N=50 and the rational direction a+ib=987395+158274i. The certificate did not adopt any floating intermediate state. Both generator and checker enforce the original exact singleton at n=0 and the frozen rational coefficients.

## R4. Exact finite certificate and independent verification

### R4.1. Regular chart and connected enclosures

For nonzero prestages, writing v_j conjugate(v_i)=|v_j||v_i| exp(i(θ_j−θ_i)) gives the exact identity

\[
\sin(3(\arg v_j-\arg v_i))
=\frac{\Im((v_j\overline{v_i})^3)}{|v_j|^3|v_i|^3}.
\]

It is independent of argument branches. The certificate checks positive lower moduli before division; it makes no continuation through a zero or silent replacement of Arg0. All 150 prestages in updates n=0,...,49 have modulus **strictly greater than 87/100**. Exact per-step rational lower bounds are retained in `data/CERTIFICATE_CHECK.json` under `step_results`; the full component enclosures are in the certificate.

`scripts/generate_certificate.py` uses rectangular complex intervals with integer endpoints divided by S=2^512. Rational constants are rounded downward/upward to this lattice. Addition and subtraction of endpoints are exact; multiplication takes the minimum/maximum of four integer products and applies floor/ceiling after division by S. A positive reciprocal is bounded by floor(S²/u) and ceiling(S²/l). Squaring includes zero when the interval crosses zero. Square roots use integer square root with the upper endpoint incremented unless its square is exact. No hardware floating operation controls these bounds.

Each prestage is formed from the original uncombined expression. Complex products give the cube in the regular-chart identity. Trigonometric values use interval Horner polynomials and the error bounds below. Documented padding enlarges prestage and next-state intervals by a radius factor 2, and kick and trigonometric intervals by a radius factor 4 (with one lattice unit added before scaling). This is widening for independent interval formulations, never numerical recentering or narrowing. The largest coordinate interval width over the 51 state boxes is

\[
\frac{346405153907508706600022909928010702983547509332064}{2^{512}}.
\]

The finite certificate contains the 51 successive state boxes plus prestage, modulus, kick, sine and cosine boxes for every step. Each next box is checked against the preceding box. There is no restart from a rounded state.

### R4.2. Elementary-function error rules

Every checked kick interval satisfies |δ|<1/100. Define

\[
P_s(x)=\sum_{j=0}^{23}\frac{(-1)^j x^{2j+1}}{(2j+1)!},\qquad
P_c(x)=\sum_{j=0}^{24}\frac{(-1)^j x^{2j}}{(2j)!}.
\]

Taylor's theorem, including the zero even coefficient for sine at order 48 and zero odd coefficient for cosine at order 49, gives

\[
|\sin x-P_s(x)|\le\frac{(1/100)^{49}}{49!}=:E_s,\qquad
|\cos x-P_c(x)|\le\frac{(1/100)^{50}}{50!}=:E_c.
\]

The generator rounds both errors upward to the dyadic lattice before widening the polynomial intervals.

The checker uses a different evaluation: for a kick interval of midpoint m and radius r it evaluates the scalar polynomials exactly as rational sums of powers. Since |sin'|≤1 and |cos'|=|sin|≤|x|, and B=max(|δ_lower|,|δ_upper|), its enclosures are

\[
[P_s(m)-E_s-r,\ P_s(m)+E_s+r],\qquad
[P_c(m)-E_c-Br,\ P_c(m)+E_c+Br].
\]

Every supplied sine/cosine box must contain these independently constructed enclosures. No transcendental floating library is a proof dependency.

### R4.3. What the separate checker proves

`scripts/check_certificate.py` uses standard-library exact Fraction arithmetic. It imports neither the generator nor any historical native implementation/checker. Its prestage uses the algebraically combined coefficient (1−2g+εk_i−ε|Ω_i|²)Ω_i+g(Ω_j+Ω_k). It expands the harmonic numerator as 3u²v−v³ for v_j conjugate(v_i)=u+iv instead of cubing a complex interval. Positive modulus witnesses are verified by exact squared inequalities, rather than by copying the generator's square-root algorithm. Trigonometry uses the midpoint construction above, not interval Horner arithmetic. Every computed interval must be contained in the corresponding supplied box.

Induction now supplies the proof: the exact seed is in box 0; the prestage, positive-modulus and kick tests enclose the exact native prestage and kick for any state in each admitted box; the Taylor tests and complex multiplication enclose its full update in the next box. Therefore the exact original F^50(Ω0) is in the terminal box. R5 checks every point of that box against a sufficient strict D-membership test. This explains the computational certificate's implication without treating precision or numerical agreement as proof.

The recorded checker execution returned **PASS** for 50 linked updates, 150 positive prestages and all terminal checks, exit status 0. It also checks the original first two mean increments and obtains a strict enclosure inside [0.0110760731,0.0110760732] for K_m=Im(conjugate(m1−m0)(m2−m1)), where m=(Ω1+Ω2+Ω3)/3. This is a dependency check of inherited turning on the connected orbit, not a new turning claim.

Five falsification controls were separately rejected: a wrong initial singleton, a zero lower modulus witness, zeroed kick boxes, a broken next-state link, and a false terminal amplitude bound. They check useful failure paths; they are not five new trajectories or a formal verification of the Python interpreter. The report preserves these separately from the mathematical entry result.

Certificate SHA-256: `1244cafe2e8aa6b646aa25b4784102f4ce085c90464e5087b3cf01bde43782a1`.

Checker SHA-256: `f7b01f38bd897399812c1adb748dd88de6d90a08da7d77136267350d49c6b32e`.

## R5. Explicit terminal inequalities

The checker verifies the following strict modulus bounds by rational squaring, not decimal approximation. Every displayed decimal in this table is an exact terminating rational.

| Channel | Strict lower bound | Strict upper bound | Lower margin above .9 | Upper margin below 1.1 |
|---|---:|---:|---:|---:|
| 1 (A) | .997219 | .997220 | .097219 | .102780 |
| 2 (B) | .997622 | .997623 | .097622 | .102377 |
| 3 (C) | .996782 | .996783 | .096782 | .103217 |

With w_i=(987395−158274i)Ω_i at n=50, rational interval evaluation verifies Re(w_i)>0 and the following conservative bounds:

| Channel | Lower bound for Re(w_i)−8|Im(w_i)| |
|---|---:|
| 1 | 492851 |
| 2 | 492769 |
| 3 | 492356 |

Thus every ordinary argument relative to the **same fixed direction** lies strictly between −arctan(1/8) and arctan(1/8). Their common ordinary interval has width less than

\[
2\arctan(1/8)<1/4<\pi/12.
\]

The first strict inequality follows from arctan(x)<x for x>0; the second from π>3. This elementary sufficient cone test avoids a numerical tangent evaluation. Multiplying by the fixed direction is only a diagnostic test and never changes the evolved state. Together with the strict annulus inequalities, it proves F^50(Ω0)∈int(D).

## R6. Reusing the inherited theorem at the correct time

Apply the original invariant-domain and convergence theorem to Ω50. Its coefficients, update order and domain match R2 exactly. Let t=n−50≥0, let Δ50 be the containing ordinary phase width at entry, and put

\[
c=1-\frac{3\sqrt2}{200},\quad\beta=\frac{8571}{10000},\quad
e_t=\big\|\,|\Omega_{50+t}|-r_*\,\big\|_\infty,\quad
B_\Delta=\frac{1.07701\Delta_{50}^2}{8}.
\]

The inherited estimates, with their time origin shifted rather than their hypotheses changed, are

\[
\Delta_{50+t}\le\Delta_{50}c^t,\qquad
e_t\le\beta^t e_0+B_\Delta\frac{c^{2t}-\beta^t}{c^2-\beta},
\]
\[
\|\Omega_{50+t}-e^{i\theta_\infty}r_*\|_\infty
\le\beta^t e_0+B_\Delta\frac{c^{2t}-\beta^t}{c^2-\beta}
+1.1\Delta_{50}c^t.
\]

Here c²>β, e0≤1/5 and the certificate gives Δ50<1/4. In particular the fully explicit valid upper bound is

\[
\frac15\beta^t+
\frac{107701}{12800000}\frac{c^{2t}-\beta^t}{c^2-\beta}
+\frac{11}{40}c^t\ \longrightarrow\ 0.
\]

The same original trajectory therefore converges to e^(iθ∞)r*. The profile r* is the unique positive fixed amplitude triple in [0.9,1.1]^3, satisfies εr_i(k_i−r_i²)+g(L3r)_i=0, and has pairwise unequal entries. Uniqueness outside this cube is not asserted. With P=I−11ᵀ/3, its residual spread is E*=||Pr*||2, with inherited bound 0<E*≤C_disp<.005270. The upper bound is not the actual value of E*.

The mean tends to e^(iθ∞) times the mean of r*. For cyclic (i,j,k), C_i=r_j r_k sin(θ_k−θ_j), so |C_i,50+t|≤1.21Δ50 c^t≤(121/400)c^t. The inherited fixed attachments W=TC and Γ=1ᵀC therefore tend to zero. These are consequences of the inherited theorem for the newly certified entrance, not separately discovered observable laws.

## R7. Qualitative robustness at the same coefficients

Identify the initial-state space with R^6. The finite orbit through update 50 has no zero prestages, with the certified positive lower bound in R4. Near each of its finitely many states the regular-chart formula is a smooth real map: the polynomial prestage, positive square roots, reciprocal positive moduli and sine/cosine functions are smooth. The expression agrees with the original Arg0-based map there, even if a principal argument crosses its cut.

By finite composition and continuity there is an open initial neighborhood on which all prestages through update 49 stay nonzero and F^50 varies continuously. The function K_m of the first two updates is continuous on this neighborhood and is strictly positive at Ω0. The three strict annulus tests and the fixed-direction cone inequalities of R5 define an open terminal set containing F^50(Ω0) and contained in D. Intersecting the regular-path neighborhood, the open condition K_m>0 and the inverse image of that terminal set gives an open set U containing Ω0. For every initial condition in this **same** U, early turning is strict and the orbit lies in D at update 50. The inherited convergence theorem then applies to each.

An open set containing Ω0 contains some positive-radius initial ball, but no numerical radius, quantitative perturbation allowance or largest basin is claimed here. The limiting common phase may vary with the entrance; the fixed coefficients give the same amplitude profile r*. No symmetry extension across singular prestages is used. This qualitative proof follows the exact-seed certificate and does not replace it.

## R8. What changes, and what remains outside the result

The old results supplied early turning and convergence after admission to D separately. The new fact is that the documented turning entrance itself reaches D under the unchanged full native map. Its demonstrated early bending belongs to an orbit that eventually approaches the aligned unequal regime. The amplitude and phase records describe how this occurs, while the connected exact certificate supplies the missing finite link.

The inherited mean accounting remains m_(n+1)−m_n=B_n+S_n: graph corrections cancel directly in the prestage mean, but redistribute the channels sampled by onsite response and synchronization. That accounting does not assign the observed capture to a single term. The published delayed-graph comparison has lambda=0 and is a different comparison; it is not a causal ablation of this nonzero-lambda trajectory.

Convergence does not prove finitely many remaining direction changes: diminishing increments can continue changing direction. The phase variable and area attachments remain native state observables, with no new physical position, force, gravity, magnetic field, receiver, transport channel, clock or geometry-feedback identification. No all-state basin, parameter continuation or new model was investigated. The exact earliest entry and an explicit neighborhood radius remain unassessed. The certificate method, strict early turn, D theorem, equilibrium profile and finite-entry-plus-invariance implication are inherited methods/results; new content is this finite connection and its narrowly justified initial-condition corollary.

## R9. Execution and delivery records

All Python ran through Windows Command Prompt and `run_python.cmd`, which calls `conda activate torment`. This run measured Python 3.11.15 and mpmath 1.3.0. NumPy 2.4.4 was version-probed during preparation; it is not used by the new numerical trajectory or exact certificate. Generation and verification use standard-library integer/Fraction arithmetic; exploration uses mpmath and a manual binary64 comparison. No dependencies were installed.

`logs/ENVIRONMENT.json`, `logs/EXECUTION_RECORDS.jsonl`, per-command stdout/stderr and `logs/INITIAL_EXECUTIONS.json` distinguish measured execution from the initial tool-observed commands. No old scientific suite or historical source module was executed. The checker controls are failure tests, and archive hashes are packaging checks, not independent mathematical claims. `SOURCE_IDENTITIES.json` records the actual sources, preserved copies and local instruction scope. `logs/PRESERVATION_AUDIT.json` compares the original source bytes and copies at closeout.

`README.md` gives replay commands. The final review manifest excludes itself. `DELIVERY_AUDIT.json` is generated by reopening every payload member before sealing; the external final audit additionally verifies every member of the final ZIP, including that audit and the manifest. The external SHA-256 sidecar binds the final ZIP. Research changes are confined to this new run and its review artifacts; no Git or publication operation is part of this investigation.
