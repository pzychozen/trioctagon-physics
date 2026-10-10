# Public reading copy of F01

This is a derived navigation/privacy copy of the cited prior reconstruction record. The local original is unchanged, SHA-256 `8b612680727c7b7a59154333e1edb1485dab78e42e52a2c8eca39c467ffcf198`. The text's mathematical and historical claims are retained; local workspace hyperlinks are retargeted to included records where possible, otherwise shown as inactive historical identifiers. Absolute machine roots are removed. For actual public originals and exact identities use [the source index](../../SOURCE_INDEX.md).

The old report is prior evidence, not a new review. F01's equal-memory reciprocity wording is qualified by accepted SRG-I v0.1.1 E01: equal memories are necessary only on nonzero-weight edges. Local working-file references and historical execution records describe the earlier investigation and do not promise those entire collections in this public subset.

The prior text follows.

---

# SRG FOUNDATIONS-01 Original Recursion and Dual-Sector Mathematics

Prepared for GPT mathematical review, 10 October 2026.

The original sources determine several distinct mathematical constructions, not one fully specified evolution law. The strongest recoverable results are an exact branch classification of the July implicit recursion, the distinction between temporal and spatial operators, and precise identities for phase rotation, time shift, reciprocal graph links and later sector coupling. These can support a mathematical source-reconstruction manuscript. They do not yet establish a unique original dynamics, a general attractor theorem, physical time reversal, or a derivation of matter and dark matter.

**Principal result.** Combining the formation paper's update with its own trail-Laplacian definition gives \(y=C(y+b)\). With its printed threshold compressor and positive threshold \(\lambda_c\), the relation has infinitely many solutions at \(b=0\), no solution for \(b<0\) or \(0<b<\lambda_c/\phi^2\), and exactly one solution \(y=\phi b\) for \(b\geq\lambda_c/\phi^2\). This conclusion is conditional on a real scalar interpretation of the incompletely typed glyph state; it is not a repaired historical recurrence.

## 1 Scope and source conventions

R0–R3 are accepted prior work and remain closed. This investigation reads manuscripts and code, derives mathematics, and evaluates finite algebraic examples. It generates no trajectories, imports no historical program, and runs no simulation, preflight, native kernel, UI, or earlier audit.

References P01–P19 retain R0's source IDs. Page numbers are **physical PDF pages**, with section/equation labels added where present. The principal cited pages also display matching printed page numbers. Complete PDF copies, original operator scripts, numbered code, page images and SHA-256 provenance accompany the report. [SOURCE_CATALOG.md](C_SOURCE_CATALOG.md) maps every ID to its full title, date and original location; SOURCE_MANIFEST.json (historical local identifier `SOURCE_MANIFEST.json`; not an active link in this reading copy) distinguishes originals from retained R0 text/context copies.

The source hierarchy here is: printed equation or operative code; explanatory prose; earlier recovery findings; new deduction. An equation's occurrence establishes that it was written, not that its physical interpretation or reported experiment was proved. “New proposal” always means a present completion choice, not recovered authorial intent.

| Source | Date and role |
|---|---|
| P08–P10 | 29 June 2025 covers: tensor/phase modules, complex quarter-turn pair, phase feedback |
| P11 | PDF metadata 29 June 2025; no cover date: scalar-versus-field Laplacian failure |
| P13 | PDF metadata 29 June 2025; no cover date: collected dual-phase tensor recursion |
| P07 | 11 July 2025: numerical RPCO, spatial TGMO and REFU definitions |
| P06 | 13 July 2025: time-shifted quanta/dark pair and horizon-reversal hypothesis |
| P03 | 14 July 2025: glyph tuple, explicit/implicit updates, temporal curvature, compression |
| P01–P02 | 15 July 2025: fusion narrative, observer formulas and pipeline descriptions |
| P05 | 15 July 2025: explicitly labeled reconstruction and position-only engine |
| P14–P15 | 24 November 2025: later geometric memory and six-component dual-core models |
| Infinity code | Internal date 14 March 2026: two independently initialized real R/D arrays |

P16–P17 are August simulation notes, not June manuscripts. P19 is later URF context. Copy timestamps do not establish composition dates. No pre-existing FOUNDATIONS-01 output directory was found before this investigation.

## 2 State and feedback definitions

### 2.1 State and temporal recursion

P03 (historical local identifier `sources/pdf/P03.pdf`; not an active link in this reading copy), p.2 §1.1, defines
\[
 Q_i=(\mathrm{ID}_i,R_i(t),\mathbf X_i(t),H_i(t),\mathcal E_i).
 \tag{F1}
\]
The ID is persistent; \(R_i\) is resonance amplitude; \(\mathbf X_i\) is position in three dimensions; \(H_i\) is memory; \(\mathcal E_i\) is an echo set. Passes are computation indices, explicitly distinguished from continuous physical time on p.7.

This is a useful **state schema**, but not a closed state space. No algebra on IDs and sets, common norm, or rule for adding scalar feedback to the whole symbolic state \(\Theta_i\) is specified. P03 p.18 says \(\Theta_i\) stores resonance, trail direction and identity. It does not identify \(\Theta_i=R_i\), or give a typed update for every tuple component. Scalar compression of a tuple containing an immutable ID is undefined until its evolving numeric part is selected.

Three distinct formulas occur in the same paper:
\[
 R_i(t+\Delta t)=C\!\left[R_i(t)+
 \sum_{j\in\mathcal E_i} f(R_j(t),d_{ij},H_i(t))\right]
 \quad\text{(p.2 §1.1)},                                    \tag{F2}
\]
\[
 R_i(t)=H_i(t)\sum_{j\in\mathcal E_i}f(R_j(t),d_{ij})
 \quad\text{(p.5 §2.2)},                                    \tag{F3}
\]
\[
 \Theta_i(t+1)=C\!\left[\Theta_i(t)+\nabla_T^2\Theta_i(t)+F_i(t)\right]
 \quad\text{(p.7 §3.1)},                                    \tag{F4}
\]
with feedback on p.7 §3.2:
\[
 F_i(t)=H_i(t)\sum_{j\in\mathcal E_i(t)}
 \frac{R_j(t)\cos\varphi_{ij}(t)}{1+d_{ij}(t)^2}.              \tag{F5}
\]

F2 is first order if all right-hand data and a scalar compressor are specified. F3 is an instantaneous self-consistency formula, not the same update. With an empty echo set F3 forces \(R_i=0\), whereas F2 allows a nonzero amplitude below the compression threshold to persist. They cannot both govern arbitrary initial amplitudes without another interpretation.

F4 becomes implicit under the p.8 temporal Laplacian. It needs at least previous and current numeric states, rather than one seed configuration. No initialization rule for \(t-1\) is given.

### 2.2 Spatial coupling and phase

F5 is a recoverable scalar expression once its arguments are supplied. Its denominator needs dimensionless distance, or an unstated scale in \(1+(d/\ell)^2\). P03 permits “spatial or symbolic” distance and “phase difference or angular alignment between glyph trails”; it selects neither a metric, a phase state/update, nor a direction at a stationary trail.

If \(d_{ij}=d_{ji}\), \(\varphi_{ji}=-\varphi_{ij}\), and echo membership is mutual, then
\[
 a_{ij}=\cos\varphi_{ij}/(1+d_{ij}^2)
\]
is symmetric. The actual feedback coefficient is \(H_i a_{ij}\), symmetric only if the corresponding memory factors also agree. Even symmetric \(a_{ij}\) does not make F5 conservative: there is no compensating \(-R_i\) term. For a mutual pair with positive amplitudes, aligned phase and positive H, both feedback contributions are positive. Total-resonance conservation does not follow.

Positivity also needs assumptions: cosine can be negative, and the supplied H eventually takes both signs. No global bound on echo-set size/strength is supplied. F5 alone proves neither contraction nor an attractor.

### 2.3 Echo and memory

P03 pp.3,5,10 defines reciprocal links:
\[
 A\in\mathcal E_B(t),\qquad B\in\mathcal E_A(t).               \tag{F6}
\]
Resonance, proximity and angle thresholds are additional §4.1 conditions. This determines a directed graph with a two-way connection. A graph cycle does **not** prove alternating evolution or a periodic orbit. “\(f(\Theta_A,\Theta_B)\) is cyclic” in §4.2 has no period, state equality or phase-space definition.

The surviving **Simulations_Trash/Simulations_part_4/echo_map_2.py**, lines 10–43, instead selects one glyph, compares its positions at different steps, min–max normalizes the distance matrix, and accepts off-diagonal pairs below 0.1. This is a **single-trail recurrence-distance observer**, not mutual causal feedback between two glyphs. Its normalization is undefined when the distance matrix has zero range. P02 p.6 names a separate missing tracker; P05 p.3 leaves advanced echo-set logic open.

Four meanings of memory must remain distinct:

1. **Stored history:** a trail attached to a persistent ID, P01 p.2 and P03 p.2.
2. **Prescribed clock modulation:** P07 p.6 and **Reading material/REFU.py**, lines 5–13:
   \[
   H(t)=2e^{-t/2}\cos t+e^{-0.3t}\sin t+1.5e^{-0.7t}+e^{-0.4t}.
   \tag{F7}
   \]
   H has no evolving-glyph input. It is nonautonomous forcing, not an accumulated record of the field.
3. **Observer embedding:** P01 p.7 §3.5 gives \(w_j=S_j/\sum_kS_k\), \(S_j=\sum_{t\in j}R_{\rm norm,t}\), and \(E=\sum_jw_jv_j\).
4. **Later dynamical memory:** P14 pp.5,17 equations (10),(25) gives a field-driven memory ODE (§7).

For \(t\geq0\),
\[
 |H(t)|\leq2e^{-t/2}+e^{-0.3t}+1.5e^{-0.7t}+e^{-0.4t}\to0.
 \tag{F8}
\]
It is not everywhere nonnegative. At \(t_n=3\pi/2+2\pi n\),
\[
 e^{0.3t_n}H(t_n)=-1+1.5e^{-0.4t_n}+e^{-0.1t_n}\to-1.       \tag{F9}
\]
An always-positive sensitivity would require another convention. P07's separate factor \(1+\lambda H/\max(H)\) needs a normalization domain and insertion order; p.5 does not give a fully composed equation with that factor. Later code makes choices without retroactively settling this manuscript.

The embedding is defined for a nonzero denominator; convex weights additionally require nonnegative \(S_j\). \(R/\max R\in[0,1]\) requires nonnegative R and positive maximum. A weighted average is not lossless memory: equal-weight pairs \((-1,1)\) and \((0,0)\) both embed as zero, and summation discards temporal ordering. These are valid observer definitions with domains, not a proof that fusion preserves all ancestral information.

### 2.4 Fusion criteria, observers and drift correction

P03 p.10 §4.3 prints the merge implication
\[
 d_{AB}<\lambda_{\rm VP},\quad R_A\approx R_B
 \quad\Longrightarrow\quad Q^{\rm fused}_{AB}=\mathrm{ProtoSRG}.
\]
Page 12 §5.2 similarly labels a cluster an attractor when every pair is close and both resonances exceed \(\rho_c\). These are snapshot predicates, not a defined fusion map or an attractor theorem. They give no resulting amplitude, position, ID, memory, echo set, deletion rule or update order. The approximation tolerance in the merge formula can be related to the nearby \(\epsilon_R\) criterion only by explicitly choosing that convention.

P01 pp.5–7 instead defines an analysis pipeline: normalize resonance events, cluster \((X,Y,Z,R_{\rm norm})\), connect events by ID and pass, then form weighted embeddings. Section 3.3 relates the DBSCAN radius to \(\lambda_{\rm VP}\), but a joint spatial/amplitude distance needs a chosen scaling. Section 3.4's narrative of different IDs converging to one ID is not an algorithm that updates or merges those IDs. Density clustering of finitely many events does not establish an invariant set attracting a neighborhood under a specified evolution.

Two further source formulas are recoverable without granting that missing theorem. P03 p.12 gives \(H_{\rm shell}(r)=H_0e^{-\gamma r}\), a prescribed spatial profile rather than a time-memory equation. Page 13 §5.4 gives
\[
 \Delta\Theta_i=\alpha(\Theta_{\rm ref}-\Theta_i).
\]
**Conditional deduction:** if this increment is added to a numeric state, the reference is fixed, and real \(\alpha\) is fixed with \(0<\alpha<2\), then the error after the update is \((1-\alpha)(\Theta_i-\Theta_{\rm ref})\), a strict contraction in any norm. The paper does not specify this composition with F4, the reference rule, or a bound on its memory-modulated \(\alpha\). The isolated identity therefore cannot establish stability of the full recursion.

## 3 The original implicit next-state equation

### 3.1 Exact reduction

P03 p.8 §3.3 prints
\[
 \nabla_T^2\Theta_i(t)=\Theta_i(t+1)-2\Theta_i(t)+\Theta_i(t-1).
 \tag{F10}
\]
There is no coefficient or time-step denominator here or before this term in F4. Substitution without alteration gives
\[
 y_i=C(y_i+b_i),\qquad b_i=\Theta_i(t-1)-\Theta_i(t)+F_i(t).
 \tag{F11}
\]

**Typing assumption for the theorem:** all these quantities are real scalars, current-pass feedback data are fixed, and C acts on that scalar. This is the minimal scalar reading needed to evaluate the expression, not a uniquely prescribed source choice. The result also applies componentwise to a declared numeric vector, but not to the untyped tuple F1.

### 3.2 Complete branch theorem

P03 p.8 §3.4 gives \(q=\phi^{-1}\in(0,1)\) and
\[
 C_\lambda(x)=
 \begin{cases}x,&x<\lambda,\\qx,&x\geq\lambda.\end{cases}     \tag{F12}
\]
For **any real** \(\lambda\), the complete solution set of F11 is
\[
 \mathcal S(b,\lambda)=
 \begin{cases}\{y:y<\lambda\},&b=0,\\\varnothing,&b\ne0\end{cases}
 \ \cup\
 \begin{cases}\{\phi b\},&\phi^2b\geq\lambda,\\
 \varnothing,&\phi^2b<\lambda.\end{cases}                    \tag{F13}
\]

**Proof.** If the input \(y+b<\lambda\), then \(y=y+b\), requiring \(b=0\) and \(y<\lambda\). If \(y+b\geq\lambda\), then \((1-q)y=qb\). Since \(q/(1-q)=\phi\), \(y=\phi b\); its input is \((\phi+1)b=\phi^2b\). These branches exhaust all real inputs and include the threshold in the compressed branch. Both necessity and sufficiency follow.

For the natural but **not explicitly bounded by the paper** assumption \(\lambda>0\):

| Offset \(b\) | All real next states |
|---|---|
| \(b<0\) | None |
| \(b=0\) | Every \(y<\lambda\) |
| \(0<b<\lambda/\phi^2\) | None |
| \(b\geq\lambda/\phi^2\) | Exactly \(y=\phi b\) |

For nonnegative amplitudes, intersect F13 with \([0,\infty)\). At positive threshold the continuum becomes \([0,\lambda)\); the other rows are unchanged. At \(\lambda=0,b=0\), the real solution set is \((-\infty,0]\), with nonnegative restriction \(\{0\}\). For \(\lambda<0\), F13 still applies; a nonnegative restriction excludes the lower branch and negative compressed candidates.

For finitely many components with feedback frozen at the current pass, existence requires each scalar solution set to be nonempty; uniqueness requires each to be a singleton. Their product is the componentwise solution set. If feedback or echo membership depends on the unknown next state, F13 is not a full coupled-system solution; that dependence itself is an additional model choice.

### 3.3 Counterexamples and compression limits

Let \(\lambda=1\) and previous/current scalar states both be zero:

* \(F=0\): both \(y=0.2\) and \(y=0.7\) solve the equation; every \(y<1\) does.
* \(F=0.1\): the lower branch requires \(b=0\); the compressed candidate has input \(\phi^2(0.1)\approx0.2618<1\). No solution exists.
* \(F=1\): the sole solution is \(y=\phi\).

Zero feedback defeats universal uniqueness. Small positive feedback defeats universal existence even for nonnegative state and feedback. A solver tolerance or initial guess cannot create a root in an empty solution set.

F12 is not a bounded cap: \(qx\to\infty\). For \(\lambda>0\) its downward jump is \((1-q)\lambda\), so it is not globally Lipschitz or a contraction. It is noninjective: every \(z\in[q\lambda,\lambda)\) has distinct preimages \(z,z/q\). A branch selector needs an explicit rule; the term compression supplies none. These are properties of the printed relation, not of every SRG implementation.

### 3.4 Intended solver and historical alternatives

No intended solver for F11 was identified in the bounded source set:

* P03 supplies F4, F10, F12 but no predictor, implicit iteration, branch selection, previous-state initialization or solver tolerance.
* P01 pp.22–24 labels its listing pseudocode. Its resonance-update function copies and returns its input, with the dynamical rule omitted in comments. Page 24 explicitly acknowledges placeholders.
* P09 p.6 and P13 p.17 mention Runge–Kutta generically for differential equations, without connecting it to F11 or resolving its branches.
* P05 p.2 and the surviving **recursive_field_evolve.py** use an explicit spatial neighbor difference.
* Surviving helper and velocity/position programs use other operators (§4). No historical solver was invoked here.
* P19 pp.12–14 has a later numerical-reporting checklist and schematic algorithms, not a July implicit-recursion solver.

F2 is a **surviving alternate explicit formula within the same paper**. The position patch is a **surviving alternate executable model**. Neither is documented as the uniquely intended correction to F4/F10. Selecting one is a model/editorial decision, not source recovery.

## 4 Compression and operator names across sources

### 4.1 Incompatible compressors

| Source | Literal operation | Consequence |
|---|---|---|
| P03 p.6 §2.5 | \(C[R]=\min(R,qR_{\rm partner})\) | Partner-dependent cap; partner selection and timing needed |
| P03 p.8 §3.4 | F12 | Discontinuous threshold scaling, unbounded range |
| P07 p.3 §2.1 | \(\exp(\operatorname{clip}(\operatorname{sign}(x)\log(|x|+\epsilon),-L,L))\) | Always positive; sign is inside the exponential |
| Reading material/RPCO.py 5–13; P05 p.1 §2.2 | \(\sin(5\operatorname{atan2}(y,x))e^{-0.05(x^2+y^2)}\) | Generated spatial field, not an amplitude update |
| recursive_attractor.py 29–31 | \(v/(1+\log(1+|v|))\), componentwise | Odd, strictly increasing, magnitude reducing, unbounded |
| helicity_REFU_TGMO_RPCO_field_evolution.py 28–32 | Vector unchanged below magnitude 5; otherwise multiplied by 0.2 | Radial threshold filter, unbounded for arbitrarily large input |
| Infinity code 49–53 | \(\operatorname{sign}(x)\exp(\operatorname{clip}(\log(|x|+\epsilon),-L,L))\) | Odd signed magnitude clamp; \(C(0)=0\) |
| P15 p.5 | \((1-\lambda_c)I+\lambda_c P_{\rm core}\) | Linear partial projection on a different state carrier |

Within P03, at \(R=0.5,R_{\rm partner}=0.1,\lambda=1\), p.6 gives approximately \(0.0618\), whereas p.8 gives \(0.5\). They could be different stages, but no composition or activation rule establishes that interpretation.

For P07, put \(a=e^{-L}, A=e^L\). Its exact branches are
\[
 C_+(x)=
 \begin{cases}
 \operatorname{clip}(x+\epsilon,a,A),&x>0,\\
 1,&x=0,\\
 \operatorname{clip}((|x|+\epsilon)^{-1},a,A),&x<0.
 \end{cases}                                               \tag{F14}
\]
Thus \(C_+(-2)=1/(2+\epsilon)>0\) at its defaults, and \(C_+(0)=1\). The equation and Python listing agree, but both contradict the adjacent claim “Retains the sign of input values.” This is a prose/formula inconsistency, not a transcription correction.

The later signed operator is
\[
 C_s(x)=
 \begin{cases}
 \operatorname{sign}(x)\operatorname{clip}(|x|+\epsilon,a,A),&x\ne0,\\
 0,&x=0.
 \end{cases}                                               \tag{F15}
\]
It preserves sign but is discontinuous at zero and loses magnitude information at plateaus. Neither F14 nor F15 restates F12. Nor does the signed operator automatically cure an implicit relation: \(y=C_s(y)\) has at least the three solutions \(0,\pm A\).

[IMPLICIT_BRANCH_APPENDIX.md](B_IMPLICIT_BRANCH_APPENDIX.md) gives all root candidates for substituting F14 into F11, the partner-cap case, and a coefficient-generalized relation. These are mathematical comparisons only; no substituted recurrence was executed.

### 4.2 Surviving original operators

**Reading material/REFU.py** only evaluates and plots F7. **TGMO.py**, lines 5–14, returns
\[
 ((2+r\cos\theta)\cos(\pi/4),(2+r\cos\theta)\sin(\pi/4),r\sin\theta).
 \tag{F16}
\]
The azimuth is fixed. This is one minor circle on a parametrized torus, repeated three times by the parameter interval, not a two-dimensional torus field or a Laplacian. Identically named copies under **Simulations_Trash/Simulations_part_2** are retained as original aliases.

**recursive_attractor.py**, lines 33–56, uses modular wrapping on a square torus and carries velocity. It updates particles in place, applying force, damping velocity and wrapping position. The early helicity/TGMO/RPCO animation, lines 23–40,57–63, evaluates a prescribed vector field at the new clock value; it does not feed the previously rendered field back into itself. These are distinct surviving constructions, not interchangeable implementations of F4.

P05's engine is explicit. With initial directed neighbor averaging \(P\), \(\Delta X=(P-I)X\) on nonempty rows and zero on empty rows, it implements
\[
 Y=X+0.05\Delta X+0.15\tanh(\Delta X),\qquad
 Z=0.95Y+0.05\overline Y+\xi,
\]
\[
 X^+=\operatorname{diag}(1,1,1-0.001\sin(2\pi\,0.244\,s))Z.
 \tag{F17}
\]
The diagonal acts on each position vector, \(\xi\) is the prescribed Gaussian position perturbation, and the step index starts at zero. See **recursive_field_evolve.py**, lines 31–40,45–78. The graph is built once at lines 52–57. Its GAMMA, LAMBDA_VP and computed breathing amplitude do not enter F17; no resonance array or echo-set update is present. It cannot supply the missing full tuple update.

For row-stochastic P, \((P-I)\mathbf1=0\). Unweighted-sum conservation additionally requires \(\mathbf1^TP=\mathbf1^T\), which a directed nearest-neighbor graph need not satisfy. Temporal F10 acts along pass index and annihilates affine temporal sequences; it is not this graph operator. Replacing one with the other changes the recurrence.

## 5 Toroidal Laplacian and geometry

P11 p.1 correctly distinguishes constant radius from a spatial radius field. Constant derivatives vanish. Promoting radius to \(\rho(x,y)=\sqrt{x^2+y^2}\) changes the model, giving
\[
 \Delta\rho=1/\rho\quad(\rho>0).                             \tag{F18}
\]
Indeed \(\rho_{xx}=y^2/\rho^3,\rho_{yy}=x^2/\rho^3\). The origin needs separate treatment because \(\rho\) is not classically differentiable there. Field promotion is not a globally smooth numerical repair. The reported IndexError is a source account, not an error rerun here.

The manuscript spatial operators differ:

* P08 p.2 §2.3 differentiates the array named theta twice along two axes, with coefficients \(a^{-2},r^{-2}\). Its phi argument is unused; it declares neither spacing nor periodic endpoints. Calling np.gradient twice does not itself impose wrapping.
* P07 p.4 §2.2 writes \(a^{-2}\nabla_\theta^2f+b^{-2}\nabla_\varphi^2f+\nabla_r^2f\), but its code applies laplacian to theta, phi and r, with no f argument or definition of laplacian. Differentiating coordinates and differentiating a field with respect to coordinates are different operations.

**Conditional geometric comparison, newly derived:** for an embedded ring torus with major radius \(R>r>0\),
\[
 \mathbf x(u,v)=((R+r\cos u)\cos v,(R+r\cos u)\sin v,r\sin u),
\]
the metric is \(g=\operatorname{diag}(r^2,(R+r\cos u)^2)\). Substitution into
\(\Delta_g f=(\det g)^{-1/2}\partial_a((\det g)^{1/2}g^{ab}\partial_bf)\) gives
\[
 \Delta_g f=\frac{f_{uu}}{r^2}
 -\frac{\sin u}{r(R+r\cos u)}f_u
 +\frac{f_{vv}}{(R+r\cos u)^2}.                              \tag{F19}
\]
For \(f=\cos u\) at \(u=\pi/2\), F19 gives \(1/(rR)\), while a flat constant-coefficient two-angle second-derivative expression gives zero. A flat product torus can legitimately have a constant-coefficient Laplacian, but needs a different declared metric. Neither wrapping nor F16 selects that metric. F19 is a comparison under explicit geometry, not a recovered replacement.

The failure involves both type and unspecified geometry/discretization. No unique toroidal operator is determined by silently replacing the printed expressions with F19.

## 6 Dual sectors and meanings of reversal

### 6.1 June complex phase pair

P09 p.2 §2.3 and P10 p.2 §2.3 state
\[
 \Phi_Q=e^{i\theta}T,\qquad \Phi_D=e^{i(\theta+\pi/2)}T=i\Phi_Q.
 \tag{F20}
\]
This determines a quarter-turn \(Jz=iz\), with \(J^2=-I,J^4=I\). It is not an involutive reflection, complex conjugation or time reversal.

In a complex Hilbert interpretation the fields are linearly dependent and
\[
 \langle\Phi_Q,\Phi_D\rangle=i\|\Phi_Q\|^2\ne0
\]
for a nonzero field. In the realification, with inner product \(\operatorname{Re}\langle\cdot,\cdot\rangle\), they are orthogonal. Thus “orthogonal” is supportable as real quadrature, not as two orthogonal complex states without another sector carrier. If global phase is physically quotiented, F20 gives the same ray; the source gives no measurement theory making them different particles.

Even the constrained pair \((z,iz)\) is not closed under plain exchange: \((iz,z)\) lacks the required relation unless \(z=0\). Advancing the common phase by \(\pi/2\) gives \((iz,-z)\), a signed exchange.

P09/P13 phase feedback is
\[
 \theta_{n+1}=\theta_n+\epsilon\,\operatorname{mean}|Q_{\rm RDPTF}|.
 \tag{F21}
\]
For fixed \(\epsilon\geq0\), the unwrapped phase is nondecreasing. This supplies no negative corrective increment or upper bound. Constant nonzero magnitude gives linear growth. A modulo-\(2\pi\) convention bounds an angular coordinate, not the evolving tensor amplitude.

### 6.2 June tensor ambiguities

P13 pp.3,5,8–9 gives
\[
 \kappa(T)=\nabla(\nabla\cdot T)-\Delta T.                    \tag{F22}
\]
For a smooth three-dimensional vector field with Euclidean operators, this equals \(\nabla\times(\nabla\times T)\), as follows by expanding component derivatives. For a scalar in several dimensions divergence is not defined by those conventions; for a higher tensor, contractions/components must be declared. This is a conditional identity, not a unique “collapse curvature.”

For spatially constant phase, \(\kappa(e^{i\theta}T)=e^{i\theta}\kappa(T)\); spatially variable phase creates extra product-rule terms. The p.5 master formula floors a generally complex curvature expression while taking a real part only of a separate coupling term. There is no canonical ordered-real floor of a complex number. Real projection, component rules or a restriction to real curvature would be new choices.

The real base expression on p.3 and complex-curvature master formula on p.5 need reconciliation. So do the prescribed schedule \(\theta_n=n\pi/(2N_{\rm iter})\) on p.8 and feedback F21 on p.9. Neither is selected as the other's approximation.

P13 pp.4,6 also prints the earlier “Revolution” expression
\[
 \operatorname{Revolution}(X)=
 \sum_{n=1}^{\infty}\Omega_X
 \left(1+\frac{\beta_n}{\alpha_n}\Omega_X\right).             \tag{F22a}
\]
For its literal fixed nonzero \(\Omega_X\), nonzero \(\alpha_n\) are necessary even to form the terms. Convergence requires the summand to tend to zero, hence \(\beta_n/\alpha_n\to-1/\Omega_X\). If that ratio instead tends to zero, or is nonnegative with positive \(\Omega_X\), the series diverges. The necessary limit alone is insufficient: writing \(\beta_n/\alpha_n=-1/\Omega_X+a_n\) reduces the sum to \(\Omega_X^2\sum_n a_n\). For example \(a_n=1/n\) still diverges. No coefficient law, convergence prescription or indexed update for the described “self-modifying” \(\Omega_X\) is supplied. Treating it as an evolving \(\Omega_n\) needs a new recurrence, not a notational inference.

One bounded module *can* support a standalone theorem: P08 p.1 defines \(G(x)=(\phi/\sqrt3)\tanh x\) on the real line. Its derivative has magnitude at most \(\phi/\sqrt3<1\). Thus G is a global contraction with sole fixed point zero. This does not prove stability of the full unspecified tensor stack. Likewise the printed potential \(V(\theta)=\sin3\theta+\sin5\theta\) has derivative \(3\cos3\theta+5\cos5\theta\); a term proportional to V in the p.5 breathing update is not the \(V'\) force in the p.4 second-order phase equation.

For real Q, \(A(Q)=|Q|/(1+|Q|)\in[0,1)\) is bounded, even and noninjective. It discards sign before a two-sector interpretation. Added breathing/fusion/tunneling in P12 p.3 or P13 p.5 is not bounded by this fact. State typing and the floor must be defined before global existence or stability can be considered.

### 6.3 July time shift and horizon reversal

P06 p.3 equation (1), repeated p.8, instead gives
\[
 D(t)=Q(t+\tau),\qquad \tau=\pi/(2\omega).                   \tag{F23}
\]
For \(Q(t)=e^{i\omega t}\) this is multiplication by i. A real single-frequency sinusoid gives quadrature orthogonal over a full period. Orthogonality is not general: \(Q(t)=1\) yields \(D=Q\), and a \(2\omega\) component receives a phase of \(\pi\).

The shift \(S_\tau\) is invertible on an appropriate two-sided function space, but \(S_\tau^2=S_{2\tau}\ne I\) in general. It is not time reversal \(Tf(t)=f(-t)\); rather \(TS_\tau T=S_{-\tau}\). An integer-pass recursion cannot evaluate advanced, usually noninteger \(t+\tau\) without domain/continuation/interpolation choices. F23 can relate complete functions without specifying a causal next-step algorithm.

P06 pp.4–5 equations (3)–(7) contain a damped spatial cosine, vacuum modulation, threshold integral, expansion and entropy-rate balance. None defines a scattering boundary condition or a transformation reversing an evolution map. At fixed r, the printed
\(\Psi_H=A_He^{-\Gamma t}\cos(\omega_r r-\varphi_0)\) decays and has no temporal cosine. “Horizon reversal” remains a physical hypothesis beyond this expression. The coefficient multiplying radius is labeled Hz; a spatial scale and units are missing.

For one specified mode the threshold integral gives
\[
 \Lambda_{\rm VP}=\lambda_n(1-e^{-\alpha_nR_c})/\alpha_n
 \quad(\alpha_n\ne0),\qquad
 \Lambda_{\rm VP}=\lambda_nR_c\quad(\alpha_n=0).              \tag{F24}
\]
No sum over n is printed; adding one is a choice. The entropy balance only implies
\[
 \frac{d}{dt}(S_{\rm child}+S_{\rm parent})=\epsilon_f.       \tag{F25}
\]
Conservation follows for \(\epsilon_f=0\), not generally. Neither identity proves reversed microscopic time.

### 6.4 Later real R/D coupled field

**srg_infinity.py**, lines 70–91, initializes two independent real arrays; dark amplitude starts at 0.01 times its own random draw. It does not enforce \(D=iR,D=-R\), or F23.

For fixed current geometry let W be the inverse-distance row-normalized neighbor matrix. For nonempty rows, lines 114–135 give
\[
 \binom{R'}{D'}=B_p\binom{R}{D},\quad
 B_p=\begin{pmatrix}
 0.85I+0.15W&c_pI\\c_pI&0.925I+0.075W
 \end{pmatrix},\quad c_p=0.0008699\sin(0.244p+\pi/2).         \tag{F26}
\]
Empty rows retain both amplitudes and skip cross terms; use identity averaging rows and zero cross diagonal entries there. Every right-hand amplitude is from the old state.

The later stages, lines 162–202, apply H factors to R and D with \(H(p+\pi/2)\) for D, position fusion using **R only**, sine modulation of **R only**, signed RPCO on both, position noise and velocity readout. Cross coupling uses \(0.244p\); R-only modulation uses \(2\pi\,0.244p\), a different numerical frequency.

For \(S=\begin{pmatrix}0&I\\I&0\end{pmatrix}\), with diagonal blocks \(A_R,A_D\),
\[
 SB_pS=\begin{pmatrix}A_D&c_pI\\c_pI&A_R\end{pmatrix}.        \tag{F27}
\]
This stage commutes with exchange only when \(A_R=A_D\), i.e. \(0.075(W-I)=0\) on the relevant state/subspace. General nonuniform fields fail. A real quarter-turn \(J(R,D)=(-D,R)\) additionally requires zero symmetric cross block. Unequal H factors, R-only forcing and fusion subsequently break exchange even where averaging agrees on a uniform subspace.

Simultaneous amplitude sign inversion is a symmetry of the **conditional fixed-geometry amplitude map**: the precompression stages are linear and F15 is odd. It is not a symmetry of the full position/amplitude update, since the center uses \(|R|\) but fusion multiplies displacement by signed R.

Spatial inversion \(\mathbf X\mapsto-\mathbf X\), R,D unchanged and noise negated, is an exact covariance of the Infinity update: distances stay fixed, tanh is odd and center/displacements invert. Symmetric Gaussian noise gives symmetry in distribution; the same nonzero noise realization does not give pathwise equality. General rotations are not implied because componentwise tanh is not rotationally equivariant.

Nonnegative amplitudes are not an invariant cone for arbitrary input: if \(c_p<0\), a row with \(R=0,D>0\) and zero R-neighbor average has \(R'<0\). Signed RPCO keeps its sign. This global counterexample does not alter the accepted positive baseline trajectories.

Lastly \(H(t+\pi/2)\) shifts every exponential as well as each sinusoid. Each decay acquires a different attenuation factor; nonoscillating terms remain. The comment “90° phase shifted” proves neither quadrature nor orthogonality of these H signals.

## 7 Later mirrored geometry and finite dual-core operators

### 7.1 November geometric source

P14 p.10 §4.2 introduces \(Q^*=(g(C),H)\), leaving \(g_i\) unspecified. Its star is not defined as complex conjugation. Separately it describes spatial reflection of a tetrahedron across a central plane. For specified unit normal \(\mathbf n\), the affine reflection
\[
 P(\mathbf x)=\mathbf x-2\mathbf n[\mathbf n\cdot(\mathbf x-\mathbf x_0)]
\]
is an involution; this does not determine g, a field update or time reversal.

P14 p.11 §4.4 supplies the exact identity
\[
 |\sin(3\theta+\delta)+\sin(3\theta-\delta)|
 =2|\sin(3\theta)\cos\delta|.                               \tag{F28}
\]
For \(\cos\delta\ne0\), this magnitude has period \(\pi/3\); at \(\delta=\pi/2\) modulo \(\pi\) it vanishes. Sixfold magnitude comes from taking an absolute value of a third harmonic. It does not prove a sixth-harmonic field or dynamical emergence of tetrahedra.

Reflection alone does not force a Star-of-David projection. Take a regular tetrahedron with base
\[
 (\cos(2\pi k/3),\sin(2\pi k/3),-1/\sqrt8),\quad k=0,1,2,
\]
and apex \((0,0,3/\sqrt8)\). All six edges have length \(\sqrt3\). Reflection in \(z=0\) gives the opposite orientation and exactly the same XY projection: one triangle and its center. This is a geometric counterexample, not a modification of any existing geometry.

P14 pp.5,17 equations (10),(25) does specify state-dependent memory:
\[
 \dot H=\eta\int_\Omega u(\mathbf r,t)w(\mathbf r)\,d^3r-\kappa H,
\]
\[
 H(t)=e^{-\kappa t}H(0)+\eta\int_0^t e^{-\kappa(t-s)}
       \left(\int_\Omega u(\mathbf r,s)w(\mathbf r)\,d^3r\right)ds.
 \tag{F29}
\]
Multiplication by \(e^{\kappa t}\) and integration proves the second line, subject to integrability. This is memory as weighted field history, a later formulation rather than the source of July's prescribed H.

Integrating P14's drift–diffusion equation also proves mass conservation if periodic/wrapped boundary terms cancel and the source \(F(u,H)\) has zero spatial integral. Those are explicit p.17 assumptions; they must be retained.

The contraction argument on pp.16–18 is not established:

* The pullback \(u\mapsto u\circ\Phi\), with onto \(\Phi:\Omega\to\Omega\), preserves the sup norm of differences rather than contracting strictly. L2 involves the Jacobian and is not generally preserved.
* For \(\Phi(\mathbf r)=\mathbf r-\lambda_c\mathbf n(\mathbf r)\), smooth unit normal implies \(\mathbf n^TD\mathbf n=0\). Thus \(D\mathbf n\) is singular, \(D\Phi\) has eigenvalue 1, and its operator norm cannot be below 1. For the printed \(\lambda_c>0\) map in Euclidean coordinates, a fixed point would require \(\mathbf n=0\), inconsistent with a unit normal. A field that vanishes at the aperture could avoid this obstruction, but is not the printed unit-normal map.
* Eigenvalues inside the unit circle do not alone prove contraction in an already selected norm for a general nonnormal matrix.
* A contraction on a complete invariant domain has one fixed point, not a nontrivial cycle. If \(F^mx=x\), then \(d(x,Fx)\leq\rho^m d(x,Fx)\) for contraction factor \(\rho<1\), so \(Fx=x\). The p.18 parenthetical “or a small set of limit cycles” does not follow from the cited theorem.

The memory solution and conditional mass balance survive. Attractor construction needs a domain, boundaries, actual nonlinearities and a corrected stability proof.

### 7.2 Six-component sector mathematics

P15 pp.3–6 defines a new complex carrier in order \((0+,1+,2+,0-,1-,2-)\), independent of the glyph tuple. Following the **per-corridor helicity action** in §3.3, this is sector-major \(\mathbb C^2\otimes\mathbb C^3\). Define
\[
 P=ss^\dagger,\ s=(1,1,1)^T/\sqrt3,\quad
 C=(1-\lambda_c)I+\lambda_cP,\quad
 M=e^\gamma P+e^{-\eta}(I-P),\quad
 D=\operatorname{diag}(1,e^{-i\varphi},e^{-2i\varphi}).
\]
Multiplication of the four source factors gives
\[
 U=A\otimes B,\qquad
 A=e^{-i\alpha\sigma_z}e^{-i\beta\sigma_x},\quad B=MDC.       \tag{F30}
\]
This product operation cannot create corridor/helicity entanglement from a product input. Local phase dependence is not an entangling controlled gate.

There is an indexing inconsistency: Appendix C p.24 writes \(I_3\otimes e^{-i\beta\sigma_x}\), coupling adjacent entries in the printed order rather than \((0,3),(1,4),(2,5)\). For the stated per-corridor action in sector-major order, it is \(e^{-i\beta\sigma_x}\otimes I_3\). They are related by reordering **all** basis-indexed operators, not by changing one factor alone. F30 is conditional on the stated per-corridor action; it does not certify every P15 table or override earlier accepted fixed-operator audits.

For \(\varphi=2\pi/3\), \(Ds\perp s\). Thus
\[
 \|U(h\otimes s)\|^2=e^{-2\eta}\|h\|^2.                     \tag{F31}
\]
At \(\eta=0.423\), this is approximately \(0.4291\|h\|^2\), not norm preservation. Appendix C p.24 and Appendix M pp.44–45 explicitly supply renormalization, resolving how normalized outputs can be produced but contradicting the earlier raw-norm claim. The normalized map \(U\psi/\|U\psi\|\) is distinct from a linear unitary map.

For sector exchange \(S=\sigma_x\otimes I\),
\[
 SU(\alpha,\beta)S=U(-\alpha,\beta).                         \tag{F32}
\]
This is parameter conjugacy, not fixed-parameter symmetry at \(\alpha=2\pi(0.244)\). The isolated flip is a complete swap, up to phase, only at \(\beta=\pi/2\) modulo \(\pi\); the source's \(\beta=\pi(0.244)\) gives partial mixing. At \(0\leq\lambda_c<1\), every factor is invertible, but the algebraic inverse is not automatically conjugation, exchange or physical time reversal. At \(\lambda_c=1\), C is singular.

Generator signs can be settled algebraically. Taking the generator continuously from zero strength gives
\[
 H_{\rm mem}=i[\gamma P-\eta(I-P)],\qquad
 e^{-iH_{\rm mem}}=e^{\gamma P-\eta(I-P)}.                   \tag{F33}
\]
Other logarithm branches require separate choices; the exponential alone does not uniquely specify H. P15 pp.8,31 prints the opposite sign, which reverses the stated amplification and damping. If \(\lambda_c=\kappa_c\Delta t\), expanding C likewise gives \(H_{\rm comp}=i\kappa_c(P-I)\), not the p.7 expression \(-i\kappa_c(P-I/3)\). The complete finite-step generator is \(i\log U\) under a specified logarithm branch; Appendix H p.34 pseudocode uses \(-i\log U\). Noncommuting finite-step factors do not in general have an exact generator equal to the sum of their separate generators. A small-step approximation needs appropriately scaled strengths.

These concern the printed equations, without rerunning or changing any accepted operator.

The wider representation claim also fails as printed: P15 p.49 identifies three spin-half tensor factors with six dimensions, but their product has dimension \(2^3=8\). Their total magnetic weights are \(\pm3/2,\pm1/2\); there is no weight-zero invariant vector and hence no singlet intertwiner of the asserted type. A direct sum of three doublets has dimension six but is a different representation. This blocks that specific spin-network identification as an established foundation.

## 8 Constants and manuscript readiness

P01 p.3 equation (1), and P06 p.4 equation (2), give
\[
 \pi e\phi=\gamma^{-1}\zeta(3)
 \quad\Longleftrightarrow\quad
 \gamma=\frac{\zeta(3)}{\pi e\phi}\approx0.08699.             \tag{F34}
\]
This is fixed when those constants are fixed. P06 p.6 identifies gamma with Euler–Mascheroni, approximately 0.577, incompatible with F34. The reconstruction's GAMMA=0.577, finite-core reinforcement 0.577 and Infinity cross-coupling 0.08699 have different roles; a shared symbol does not derive their relationship.

P19 pp.8–9 calls gamma inferred from spectra and tuned per run; p.13 leaves GammaEstimate undefined. Solving F34 for gamma cannot independently verify F34. R0's accepted provenance conclusion remains in force; no independent dynamical estimator is recovered here.

The sources also use lambda_VP as overlap length, clustering scale, numerical 0.618 and other geometry-related quantities. Likewise 0.244 is not automatically both radians/pass and cycles/pass or Hz. Each selected model needs its own parameter dictionary, nondimensionalization and provenance.

| Claim | Supportable now | Still required |
|---|---|---|
| Glyph state | F1 as historical schema | Numeric carrier and rules for every evolving component |
| Implicit recursion | F11–F13 and counterexamples as new theorems about the printed equations | A choice of dynamics; replacements must be declared |
| Feedback | F5 on specified arguments; conditional symmetry/nonconservation | Echo rule, metric, phase extraction, units, initialization |
| Compression | Exact distinct formulas and domain/branch properties | Selected operator, placement and negative/zero conventions |
| Memory | H as forcing; embedding identities; later F29 as field history | Meaning/observable of retention and any stability proof |
| Toroidal coupling | Constant derivative, F18 and geometry-conditional F19 | Carrier, metric, boundaries, mesh and singularity treatment |
| Mirrored sectors | Quarter-turn, shift, reflection, sixfold magnitude and conjugacy identities | Declared symmetry action and proof for full chosen dynamics |
| Attractor/fusion | Source hypotheses and well-defined observers | Closed map, invariant domain, basin/attractor definition and proof/evidence |
| Six-component model | Projector algebra and conditional factorization | Basis and generator consistency before further interpretation |
| Physical particles, horizons, dark matter | Historical motivation | Physical observable map, units, predictions and independent tests |
| Constant lock | F34 as parameter identity | Independent estimator and causal/theoretical link |

The defensible manuscript is a **mathematical reconstruction and well-posedness analysis of historically distinct SRG models**. It can present branch theorems, operator distinctions and conditional symmetry/memory results without claiming a recovered model already proves the broader physical narrative.

## 9 Candidate completions for review only

These are **new proposals**, neither executed nor presented as original intent.

1. **Select an explicit historical formula to formalize.** F2 exists in P03. Declare resonance, position, phase and echo rules; it then gives a unique algebraic next step wherever its ingredients are defined. Selecting F2 over F4/F10 is a new editorial decision, and still requires stability/geometry proofs.
2. **Retain an implicit structure with a proved contraction.** On a complete normed state space use a declared globally Lipschitz \(\widetilde C\) and \(y=\widetilde C(a y+d)\). If \(|a|\operatorname{Lip}(\widetilde C)<1\) and the domain is invariant, there is exactly one root. The original threshold operator fails this hypothesis. Adding a coefficient alone does not remove its jump or guarantee a root.
3. **Separate temporal curvature from the evolution law.** Treat it as an observer or introduce an explicit velocity state. Either requires a new equation. A backward difference or spatial graph replacement is a substantive change, not an implementation detail.

The next decision is mathematical: select a state carrier and one source-identified update family, then resolve its domains and branches before further experiments. No new experiment is recommended or started here.

## 10 Evidence and GPT review questions

[ALGEBRA_CERTIFICATES.json](../../evidence/PRIOR_ALGEBRA_CERTIFICATES.json) records 20 successful finite arithmetic checks of examples and matrix identities: branch counterexamples, compressor signs, negative H, R/D commutators, finite-core factorization/norm and generator signs. These are not 20 dynamical experiments or substitutes for proofs.

STATIC_SEARCH_LEDGER.json (historical local identifier `STATIC_SEARCH_LEDGER.json`; not an active link in this reading copy) covers all 19 PDF texts, all 35 OLD_MATERIAL Python files and selected later source files. Relevant equations and operative code were read directly; VISUAL_VERIFICATION.json (historical local identifier `VISUAL_VERIFICATION.json`; not an active link in this reading copy) lists visually checked equation pages. This is a bounded local-corpus investigation, not a claim that no private or missing source exists elsewhere.

GPT review should focus on:

1. Whether the scalar typing qualification and full branch set F13 faithfully expose P03 §§3.1–3.4 without repairing it.
2. Which historical update family should be formalized, and which missing definitions can come from further primary sources.
3. Whether “mirror” should be reserved separately for quadrature, shift, reflection and sector exchange.
4. Whether the conditional memory/geometry results support a reconstruction manuscript once disproved contraction and representation claims are qualified.

All output remains under FOUNDATIONS_01_ORIGINAL_RECURSION. INTEGRITY_RECEIPT.json (historical local identifier `INTEGRITY_RECEIPT.json`; not an active link in this reading copy) records preservation of OLD_MATERIAL, R0–R3 and REVIEW_DECISIONS plus source-copy verification. The review ZIP is a source package, not an executable plan for another experiment.
