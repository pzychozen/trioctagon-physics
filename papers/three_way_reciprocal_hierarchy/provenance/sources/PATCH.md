# Six candidate apertures, the Z harmonic and a rotated toroidal motif

**Codex research report · RESEARCH_GATE_TORUS_v0.1 · 24 September 2026**
Baseline: `d0aa8d1cb19421ff441eacda0f83ec89fc3160b3`. New findings await GPT research review.

1. **Objects analyzed.** The actual Paper-C three-face welded shell, from unchanged `geometry.folded_module()`, supplies six triangular **candidate aperture patches**: three upper chamfer notches and their lower mirrors. Each has two actual boundary edges and a measurement-only base. The shell still has **two connected nine-edge rims**, not six boundary components. These patches are not physical gate definitions recovered from a source.
2. **Correspondence.** Threefold/mirror symmetry agrees. Uniform similarity fails for the tips, centroids and base midpoints separately. It **does permit exact simultaneous membership in the six finite triangles**, in a one-parameter rotation/scale family. Thus the finite-patch claim is conditionally feasible, while a unique coordinate attachment, gate axis and SRG-channel assignment remain **underdetermined**.
3. **Clock.** Six frozen continuous extrema form **three vertical upper/lower pairs**, visited `U0,L2,U1,L0,U2,L1`. Negative scalar radius reverses horizontal direction. The unchanged twelve-sector clock at lock 0.244 instead samples `(c,s,-c,-s)` three times, misses every continuous extremum, and has six displayed azimuths. Those are different sets.
4. **Spring.** No angular restoring equation is implemented. The earlier potential has negative curvature on odd branches. A newly assumed branch potential `-eta*(-1)^k*f` would have curvature `9*eta*A` for `eta,A>0`. This is conditional stiffness, without an adopted force, inertia, damping or energy calibration.
5. **Rotated motif.** The declared example—radius 3, twelve copies, scale 1/4, quarter turn about local first axis—is well defined, closes its moving frame and has positive separation bounds. The original shell axis becomes the negative circle tangent. The exact minimum tube radius containing the small filled shells is approximately **0.1447091669**. This is a geometric placement and envelope, not a material tube or interaction.
6. **EM.** A hypothetical common orthonormal E/B frame gives the standard local Gram/energy/flux algebra. It does not establish Maxwell evolution or a photon. The prescribed initially null fixture becomes `((3+i)/5,(1+3i)/5,(1+i)/5)`, with bilinear square **14i/25**, disproving null-subset preservation by this recurrence.

The two fixed 96-update experiments completed: **388 observer rows**, no precision/domain failures, bitwise agreement with controls without observers. The new research suite passed **20/20**; the single final unchanged package suite passed **207/207**, including all 30 local-only methods. No kernel, manuscript, existing evidence, index or remote content was changed.

## 1. Authority, source scope and assumptions

**SOURCE_FACT.** The authoritative checkout is `C:\TORMENT\TRIOCTAGON_new\trioctagon-physics`. Its main HEAD, sole parent and tree match the order; a read-only `git ls-remote origin refs/heads/main` returned the same baseline. The tracked/index diffs were empty. The new output directory was absent at preflight. No fetch, synchronization, alternate checkout or package installation was performed.

The source hashes, pinned Git blobs, exact source line spans, interpreter and imported module paths are in `RESULTS.json`. The local-source ledger is:

| Input | Consulted locator and purpose |
|---|---|
| `kernel_physics/geometry.py` | Full module: exact accepted vertices, faces, incidence, C3 and horizontal reflection |
| Paper C v0.3.1 | §§4–5, lines 98–190; §§8–9, 241–303; Appendix B, 377–381: vertex IDs, topology, measurement regions, symmetry |
| Paper D v0.1.1 | Abstract/provenance, 7–37; §12, 327–368: reference concept and exact welded-member distinction |
| Paper E v0.1.1 | §§3–9, 52–360; §§17–20, 604–731: readout, sampling, signed pairing, Gram identity, potential, EMA and open attachment |
| `z_manifold.py` | Full module: pure observers, literal defaults, explicit clock and memory updates |
| `dynamics.py` | Full module, particularly 87–104: unchanged complex recurrence |
| `readouts.py` | Full module: raw channel chirality |
| `z_diagnostics.py` | Lines 1–220: passive norm/Q, Gram and alignment accounting |
| `face_state.py` | Full module: channel-to-face tangent vectors, not shared ambient field coordinates |
| `K1_K2_K3_PARITY_CLOSEOUT.md` | Lines 125–180: accepted limits and local-only test obligations |

The three manuscripts are `papers/PAPER_C/PAPER_C_EXACT_TRIOCTAGON_GEOMETRY_DRAFT_v0.3.1.md`, `papers/PAPER_D/v0.1.1/PAPER_D_REFERENCE_SCAFFOLD_v0.1.1.md` and `papers/PAPER_E/v0.1.1/PAPER_E_Z_MANIFOLD_v0.1.1.md`, relative to the checkout. No historical snapshot or additional corpus paper was needed. The only external reference consulted was the primary Riemann–Silberstein review, §8 below. Existing reconstruction results were not relabelled as new archaeological discoveries.

| Evidence class | Statement or choice |
|---|---|
| SOURCE_FACT / author input | The order records Hilmir Frímann Halldórsson's conceptual torus, upper/lower openings and proposed spring/pair interpretation. The image is not calibrated data and was not needed. |
| SOURCE_FACT | Paper C defines the notch measurements; Paper D defines a separate reference family; the accepted source leaves spatial Z attachment open. |
| DERIVED | Exact patch geometry, representative mismatches, finite-patch registration family, frame/clearance/tube results and fixed counterexamples below. |
| NEW_ASSUMPTION | Treat the measurement triangles as candidate gate regions; choose the outward normal convention and representative labels. |
| NEW_ASSUMPTION | Use the restricted dictionary `O+lambda*Rz(delta0)*M`; no source has supplied this spatial meaning. |
| NEW_ASSUMPTION | For display only, choose the median hit at frozen reference amplitude 1 before examining trajectories. |
| NEW_ASSUMPTION | Branch potential, toroidal placement and same-frame E/B dictionary are independent hypotheses. |
| NUMERICAL_WITNESS | Two fixed trajectories and checked floating residuals; no asymptotic or physical conclusion follows. |
| COUNTEREXAMPLE | Representative metric mismatch, extended-plane miss, odd-branch potential maximum and loss of EM nullness. |
| UNRESOLVED | Which object/point/axis represents a physical gate, which readout is attached, the fixed coordinate dictionary, channel labels and an interaction law. |

The accepted face view assigns the real and imaginary part of each channel to that face's own tangent and vertical vectors. Its channel-indexed area triple is not automatically an ambient axial vector. No equation here identifies those different frames merely by matching three coordinates.

## 2. Exact six-patch geometry

Put
\[
s=\sqrt2-1,\quad d=s/\sqrt2=1-\sqrt2/2,\quad
O=(0,\sqrt3/6,0),\quad h_0=s/2,\quad r_0=1/\sqrt3.
\]
Paper C's upper seed is `A=V7, B=V6, C=V16`. All coordinates below are read from the mesh API, with zero-based source IDs:

| Source ID | Exact global coordinate (x,y,z) |
|---:|---|
| 0 | `(0, sqrt(3)/2, 1/2 - sqrt(2)/2)` |
| 1 | `(-1/2 + sqrt(2)/4, sqrt(6)/4, -1/2)` |
| 2 | `(-sqrt(2)/4, -sqrt(6)/4 + sqrt(3)/2, -1/2)` |
| 3 | `(-1/2, 0, 1/2 - sqrt(2)/2)` |
| 4 | `(-1/2, 0, -1/2 + sqrt(2)/2)` |
| 5 | `(-sqrt(2)/4, -sqrt(6)/4 + sqrt(3)/2, 1/2)` |
| 6 | `(-1/2 + sqrt(2)/4, sqrt(6)/4, 1/2)` |
| 7 | `(0, sqrt(3)/2, -1/2 + sqrt(2)/2)` |
| 8 | `(1/2 - sqrt(2)/2, 0, -1/2)` |
| 9 | `(-1/2 + sqrt(2)/2, 0, -1/2)` |
| 10 | `(1/2, 0, 1/2 - sqrt(2)/2)` |
| 11 | `(1/2, 0, -1/2 + sqrt(2)/2)` |
| 12 | `(-1/2 + sqrt(2)/2, 0, 1/2)` |
| 13 | `(1/2 - sqrt(2)/2, 0, 1/2)` |
| 14 | `(sqrt(2)/4, -sqrt(6)/4 + sqrt(3)/2, -1/2)` |
| 15 | `(1/2 - sqrt(2)/4, sqrt(6)/4, -1/2)` |
| 16 | `(1/2 - sqrt(2)/4, sqrt(6)/4, 1/2)` |
| 17 | `(sqrt(2)/4, -sqrt(6)/4 + sqrt(3)/2, 1/2)` |

Use
\[
u_j=R_z(2\pi j/3)(0,1,0),\quad
v_j=R_z(2\pi j/3)(-1,0,0),\quad j=0,1,2.
\]
Thus the pair azimuths are \(\pi/2,7\pi/6,11\pi/6\), not measured about the global origin. For sign \(\sigma=+1\) upper or \(-1\) lower, define the finite patch exactly by
\[
X=O+r(t)u_j+w v_j+\sigma h(t)e_z,\quad
r(t)=r_0-\frac{\sqrt3d}{2}t,\quad h(t)=h_0+dt,\quad
0\le t\le1,\quad |w|\le dt/2. \tag{1}
\]
These inequalities are the whole triangular region, not its infinitely extended plane. The outgoing cycles are:

| Patch | Outgoing (tip,base,base) source IDs | Pair azimuth | Exact unit normal |
|---|---|---|---|
| U0 | (7, 6, 16) | pi/2 | `(0, 2*(-2*sqrt(14) + 3*sqrt(7))/(7*sqrt(17 - 12*sqrt(2))), (-2*sqrt(42) + 3*sqrt(21))/(7*sqrt(17 - 12*sqrt(2))))` |
| L0 | (0, 15, 1) | pi/2 | `(0, 2*(-2*sqrt(14) + 3*sqrt(7))/(7*sqrt(17 - 12*sqrt(2))), (-3*sqrt(21) + 2*sqrt(42))/(7*sqrt(17 - 12*sqrt(2))))` |
| U1 | (4, 13, 5) | 7pi/6 | `((-3*sqrt(21) + 2*sqrt(42))/(7*sqrt(17 - 12*sqrt(2))), sqrt(7)*(-3 + 2*sqrt(2))/(7*sqrt(17 - 12*sqrt(2))), (-2*sqrt(42) + 3*sqrt(21))/(7*sqrt(17 - 12*sqrt(2))))` |
| L1 | (3, 2, 8) | 7pi/6 | `((-3*sqrt(21) + 2*sqrt(42))/(7*sqrt(17 - 12*sqrt(2))), sqrt(7)*(-3 + 2*sqrt(2))/(7*sqrt(17 - 12*sqrt(2))), (-3*sqrt(21) + 2*sqrt(42))/(7*sqrt(17 - 12*sqrt(2))))` |
| U2 | (11, 17, 12) | 11pi/6 | `((-2*sqrt(42) + 3*sqrt(21))/(7*sqrt(17 - 12*sqrt(2))), sqrt(7)*(-3 + 2*sqrt(2))/(7*sqrt(17 - 12*sqrt(2))), (-2*sqrt(42) + 3*sqrt(21))/(7*sqrt(17 - 12*sqrt(2))))` |
| L2 | (10, 9, 14) | 11pi/6 | `((-2*sqrt(42) + 3*sqrt(21))/(7*sqrt(17 - 12*sqrt(2))), sqrt(7)*(-3 + 2*sqrt(2))/(7*sqrt(17 - 12*sqrt(2))), (-3*sqrt(21) + 2*sqrt(42))/(7*sqrt(17 - 12*sqrt(2))))` |

Here “outgoing” selects positive radial normal component and the matching upper/lower vertical sign. Reflecting an oriented triangle reverses its cross product; the lower cycles therefore swap the two base vertices after reflection. The opposite normal is an orientation convention, not different geometry. The pair normals and planes are
\[
n_j^\sigma=\frac{2u_j+\sigma\sqrt3 e_z}{\sqrt7},\qquad
u_j\cdot(X-O)+\sigma\frac{\sqrt3}{2}X_z=K,\qquad
K=\frac{\sqrt3}{12}+\frac{\sqrt6}{4}. \tag{2}
\]
Equivalently \(n_j^\sigma\cdot(X-O)=2K/\sqrt7\). Their constant is positive.

For the seed, \(B-A=d(-1/2,-\sqrt3/2,1)\) and
\(C-A=d(1/2,-\sqrt3/2,1)\). Their cross product is
\(d^2(0,1,\sqrt3/2)\); rotation/reflection gives the other five.
Consequently every spatial area is \(\sqrt7\,s^2/8>0\), and every axial projected area is \(\sqrt3\,s^2/8>0\). The projected triangles are equilateral with side \(d\); the spatial triangles instead have sides \(s,s,d\) and tip angle \(\arccos(3/4)\).

The three representative choices are distinct. The table supplies all six representatives through \(P_j^\sigma=O+r\,u_j+\sigma h\,e_z\):

| Choice | Radius \(r\) | Positive height \(h\) | Exact \(r/h\) | Numerical ratio |
|---|---|---|---|---:|
| Tip, \(t=0,w=0\) | \(\sqrt3/3\) | \((\sqrt2-1)/2\) | \(2(\sqrt3+\sqrt6)/3\) | 2.7876937002 |
| Centroid, \(t=2/3,w=0\) | \(\sqrt6/6\) | \((1+\sqrt2)/6\) | \(2\sqrt3-\sqrt6\) | 1.0146118724 |
| Base midpoint, \(t=1,w=0\) | \(\sqrt6/4-\sqrt3/6\) | \(1/2\) | \(\sqrt6/2-\sqrt3/3\) | 0.6473946022 |

All have azimuth \(\arg u_j\), height sign \(\sigma\), and the same mirror partner index. The exact global/relative coordinates and opposite normal signs are also listed separately for every patch in the JSON. The source names the tip and notch; selecting one representative as a gate anchor would be an additional definition.

**SOURCE_FACT.** The top measurement hexagon has cycle `(5,6,16,17,12,13)` and alternating side lengths \(s,d\). Since \(d/s=1/\sqrt2\ne1\), it is not regular. It is not the nine-edge rim, a cap, or Paper D's separately selected regular member. Figure 01 shows measurement patches without adding them to the mesh.

![Actual accepted shell and candidate measurement apertures](01_shell_apertures.png)

**Figure 01.** Left: actual three-face shell and six labelled triangular measurements. Right: upper/lower patches share three axial footprints around the nonregular top measurement hexagon. Filled measurement regions in this diagram are not additional material faces. Projection hides the distinction between the spatial notch angle and its 60-degree projected angle.

## 3. Symmetry and exact metric registration

### 3.1 Correct the signed radius before assigning labels

For frozen \(A>0\),
\[
f(\theta)=A\cos3(\theta-\ell),\quad
M=f(\theta)(\cos\theta,\sin\theta,1),\quad
\theta_k=\ell+k\pi/3 .
\]
Even \(k=2j\) gives \(U_j=A(\cos a_j,\sin a_j,1)\), \(a_j=\ell+2\pi j/3\).
Odd \(k=2j+1\) has negative scalar; adding \(\pi\) to its horizontal direction gives \(L_{j+2}\), with indices modulo three. Hence
\[
U_0\to L_2\to U_1\to L_0\to U_2\to L_1. \tag{3}
\]
There are three horizontal directions and two heights on each. A six-ray interpretation of these continuous extrema is false.

At the pair level, the actual C3 sends \(j\mapsto j+1\); horizontal reflection swaps U/L at fixed \(j\). A vertical reflection reverses pair orientation. The possible label maps can be written \(j\mapsto \epsilon j+m\), \(\epsilon=\pm1\), \(m=0,1,2\), with an optional global U/L swap. The JSON enumerates all twelve resulting orders. Within the stated positive-scale axial-rotation family only \(\epsilon=+1\) and no U/L swap are used; the other cases require explicitly adding global reflections. A map of pair labels alone chooses neither a patch point nor an SRG element.

### 3.2 Three exact representative counterexamples

**NEW_ASSUMPTION.** Restrict the coordinate dictionary to
\[
P(M)=O+\lambda R_z(\delta_0)M,\qquad\lambda>0. \tag{4}
\]
Its frozen extrema have horizontal radius equal to absolute height, both \(a=\lambda A\). Rotation, positive uniform scale and the separately considered global horizontal/vertical reflections cannot change that ratio. All three ratios in §2 differ exactly from one. Thus the complete tip, centroid and base-midpoint correspondences each fail in this family. A centroid ratio close to one is still not exact equality.

An anisotropic map would need a separately selected radial/vertical scale ratio \(r/h\) from the table for each chosen representative convention. That extra freedom is not part of (4) and is not adopted. The patch normal has radial/vertical ratio \(2/\sqrt3\), also different from the macro cone ray's ratio one. At the median hit the angle between the outward normal and the outgoing cone ray has cosine \((2+\sqrt3)/\sqrt{14}\), which is not one. Anchor rays, normals and physical gate axes cannot silently be identified.

### 3.3 Finite triangles admit an exact family

**DERIVED, conditional on (4).** Let \(\delta\) be the upper ray's azimuth relative to \(u_0\), measured towards \(v_0\). Its relative coordinates in the \((v_0,u_0,e_z)\) frame are
\[
(w,r,h)=a(\sin\delta,\cos\delta,1).
\]
Substitution into the supporting plane gives the unique candidate
\[
a(\delta)=\frac{K}{\cos\delta+\sqrt3/2},\quad
t=\frac{a-h_0}{d},\quad
(\alpha,\beta,\gamma)
 =\left(1-t,\frac t2+\frac{a\sin\delta}{d},
                    \frac t2-\frac{a\sin\delta}{d}\right). \tag{5}
\]
These are the seed \((A,B,C)\) barycentrics. A hit requires \(a>0\), all three nonnegative, and their sum one. In particular, plane equality by itself is insufficient.

A complete characterization follows without scanning angles. At fixed \(t\) in (1), the cone condition \(w^2+r(t)^2-h(t)^2=0\) requires
\[
q_{\rm mid}(t)=r(t)^2-h(t)^2\le0,\qquad
q_{\rm edge}(t)=r(t)^2+(dt/2)^2-h(t)^2\ge0 .
\]
The first is strictly decreasing on \([0,1]\), starts positive and has a unique root \(t_0=(a_0-h_0)/d\). The second simplifies to
\[
q_{\rm edge}(t)=(1-\sqrt2)t-\frac5{12}+\frac{\sqrt2}{2},
\quad t_e=\frac{7+\sqrt2}{12}.
\]
Its root is also in \((0,1)\), with \(t_0<t_e\). Therefore precisely \(t\in[t_0,t_e]\) is allowed, with \(w=\pm\sqrt{h(t)^2-r(t)^2}\). Since \(h/r\) strictly increases here, the absolute ray azimuth increases from zero to the edge value. Explicitly,
\[
\begin{aligned}
a_0&=\frac{K}{1+\sqrt3/2}=0.4055196684131613\ldots,\\
a_e&=\frac{7\sqrt2}{24}=0.4124789556921527\ldots,\\
w_e&=\frac14-\frac{5\sqrt2}{48},\qquad
r_e=\frac{\sqrt3}{12}+\frac{5\sqrt6}{48},\\
\delta_e&=\arctan(w_e/r_e)=0.25159459771206244\ldots .
\end{aligned} \tag{6}
\]
The full admissible set, modulo three label offsets, is
\[
|\delta|\le\delta_e,\quad
\delta_0=\pi/2-\ell+\delta+2\pi m/3,\quad
\lambda A=a(\delta),\quad m=0,1,2. \tag{7}
\]
Rotation and scale are **linked** in (7); the interval \([a_0,a_e]\) is not free to pair with every angle. Strict inequalities give six simultaneous interior hits. Each endpoint lands on a chamfer boundary edge, never the tip or base. C3 and horizontal reflection carry the same seed solution to all six patches; no per-patch fitting is used.

At \(\delta=0\), \(t_0=0.6774239705\ldots\) and barycentrics are \((1-t_0,t_0/2,t_0/2)\), all positive. This is close to, but distinct from, the centroid's \(t=2/3\).

**COUNTEREXAMPLE.** At \(\delta=\pi/6\), the plane intersection has
\[
a=K/\sqrt3=1/12+\sqrt2/4,\quad
(\alpha,\beta,\gamma)=((4-\sqrt2)/12,(2+\sqrt2)/3,-\sqrt2/4).
\]
The negative third coordinate proves **MISS**, although the point lies on the plane. At \(\delta=5\pi/6\) or \(7\pi/6\) the denominator vanishes; the ray is parallel to the plane and cannot lie in it because \(K>0\). A nonpositive candidate \(a\) is not an outgoing positive-scale hit. \(A=0\) (or the excluded \(\lambda=0\)) collapses the image to O, outside all six patches. Positive-length triangles themselves are nondegenerate at the accepted width.

Only the product \(\lambda A\) is identifiable from one static extremum shape. Aligning a rotation to \(\ell\) does not establish that \(\ell\) originated in the geometry. No remaining symmetry fixes a preferred representative, scale normalization, normal-based interpretation or channel assignment.

### 3.4 The actual clock is a different finite set

For \(N=12\), \(\theta_q=\pi q/6\) gives
\[
z_q/A=\cos(\pi q/2-3\ell)
 =(c,s,-c,-s,c,s,-c,-s,c,s,-c,-s),
\]
where \(c=\cos(3\ell)=0.7438391736\ldots\), \(s=\sin(3\ell)=0.6683586491\ldots\).
An extremum requires \(\pi q/2-3\ell\in\pi\mathbb Z\), equivalently
\(\ell\in(\pi/6)\mathbb Z\). The literal nonzero rational 0.244, as well as its binary64 rational representation, cannot meet that condition. No phase lock or clock setting was tuned.

The default frozen samples have displayed azimuths
\(0,30,120,150,240,270\) degrees before external rotation, with vertical pairs between \(q\) and \(q+6\). These are **six sampled directions, not the three extremum directions**. Evolving amplitudes break equal-height pairing; EMA offsets can also remove opposite signs. External rigid display rotation changes none of the scalar sampling facts.

![Continuous harmonic, source clock samples and conditional finite-patch placement](02_macro_registration.png)

**Figure 02.** Left distinguishes scalar angle, continuous extrema and twelve unchanged clock samples for the unit-amplitude analytic fixture. Right uses (4) with \(\delta=0,\lambda=a_0,A_{\rm ref}=1\). Labels U/L identify the mathematical pair convention, not recovered gates. The orange curve is continuous analytic geometry; samples are isolated markers, not measured crossings or an adopted interpolation.

## 4. Fixed bounded trajectories

**NEW_ASSUMPTION, declared before execution.** Select (4) with \(O\) from the shell,
\(\lambda=a_0\), \(\delta_0=\pi/2-0.244=1.3267963267948966\) radians and unit frozen reference amplitude. This normalizes a static figure, not the model's state. The selection record was saved before calling the trajectory routine. The same map is retained in every CSV row across both runs and both observers. No per-row normalization, percentile scale, retuned lock, nearest-label assignment or geometry feedback was used. This display choice does not eliminate family (7).

**SOURCE_FACT / execution inputs.**
\[
\Omega_0=(0.2+0.3i,-0.4+0.1i,0.1-0.2i),\quad
\epsilon=.05,\ g=.2,\ k=(1,1,1).
\]
Run phase strengths are exactly 0 and .001. Both start at `Clock(q=0,N=12,t=0,q_step=1)` with `dt=.1`. Each performs 96 unchanged `step3` updates. Each same-Omega history is observed with public staged and EMA APIs, their literal defaults, and `EMAState(m=0)`.

Row zero is explicitly recomputed and consumes **no** EMA innovation. Subsequent rows use one state update, one clock advance and one memory advance from the new Omega, then both observations. The full initial-plus-post-update convention yields 97 rows per observer per run, total 388. The two observer histories share each run's Omega by construction; a separate step3-only control has the same stored complex128 bytes. Input Omega bytes and the old clock/memory values were checked around pure calls.

| Phase strength | Observer | Final I | Final z | Final EMA m |
|---:|---|---:|---:|---:|
| 0.0 | staged | 2.966341816282475 | 0.001142870453854933 | not applicable |
| 0.0 | ema | 2.966341816282475 | 0.4538355559204664 | 0.1630043531454321 |
| 0.001 | staged | 2.96626861396742 | 0.001142865273737776 | not applicable |
| 0.001 | ema | 2.96626861396742 | 0.4537511510740386 | 0.1629212665058914 |

All four final C values are below K3's \(10^{-12}\) direction-resolution threshold; 33 of each history's rows resolve C. A floating zero or very small C is not an exact zero theorem, and unresolved alignment numbers are accompanied by resolution flags. **Z_chiral has no imposed decay envelope; it need not decay.** The decrease of C in these particular histories does not alter that source statement.

`TRAJECTORIES.csv` retains Omega components, q/t/theta, scalar z, raw M/C/T, I, harmonic amplitude, EMA memory, fixed display M, norm/Q/Gram residuals and all historical alignment flags. `RESULTS.json` retains the full passive accounting records and bitwise history hashes. Every gate-assignment field is blank. No gate flux, causal interaction, residence time or passage theorem is inferred from these rows.

The maximum absolute residuals were:

| Residual | Maximum absolute value |
|---|---:|
| norm_residual | 5.5511151231257827e-17 |
| q_residual | 2.0400383799441322e-17 |
| macro_relation_residual | 5.5511151231257827e-17 |
| q_macro | 5.5511151231257827e-17 |
| gram_residual | 6.6613381477509392e-16 |
| slack_residual | 8.8817841970012523e-16 |

For each row the allowance is
\(128\,\epsilon_{\rm binary64}\max(1,\|T\|^2,|\text{norm prediction}|,\|M\|^2,\|C\|^2,I^2)\).
The checks use the recorded scale and do not clip values. The largest absolute residual is approximately \(8.89\times10^{-16}\), well within its allowance. There were no precision/domain failures, shortened runs or changed parameters.

## 5. What the spring hypothesis does and does not supply

**DERIVED.** Independent differentiation gives
\[
f'=-3A\sin3(\theta-\ell),\qquad f''=-9A\cos3(\theta-\ell).
\]
At \(\theta_k=\ell+k\pi/3\), \(f=A\sigma_k\) and \(f''=-9A\sigma_k\), \(\sigma_k=(-1)^k\). These classify the scalar's frozen angular extrema; a readout maximum is not itself a potential minimum.

**COUNTEREXAMPLE.** For the earlier expression
\[
U_{\rm bad}(\delta)=-\sigma_k A\cos3\delta,\qquad
U_{\rm bad}''(0)=9\sigma_k A,
\]
odd \(k\) has negative curvature when \(A>0\). It is a local maximum.

**NEW_ASSUMPTION.** If instead a sign-indexed interaction is expressly defined as
\[
U_k(\theta)=-\eta\sigma_k f(\theta),\qquad\eta>0,
\]
then
\[
U_k(\theta_k+\delta)=-\eta A\cos3\delta
=-\eta A+\frac92\eta A\delta^2+O(\delta^4),\qquad
U_k''(\theta_k)=9\eta A . \tag{8}
\]
With a fixed positive displacement scale \(R_s\), \(x=R_s\delta\) would give curvature \(9\eta A/R_s^2\). \(R_s\) is not automatically the torus radius, gate height or source normalization. No value of \(\eta\), units or force update is selected.

For \(A=0\) everything is flat/collapsed and there are no six isolated extrema. For \(A<0\) scalar maximum/minimum labels reverse and the whole macro curve changes sign. With the same branch labels in (8), curvature is then negative; replacing branch signs by \({\rm sign}(A)\sigma_k\) would instead be an explicitly relabelled ansatz with \(9\eta|A|\). It is not an unmentioned rescue of the original formula.

These six local branches are not an already implemented single six-well global potential. Switching the branch sign is an additional gate/state-selection rule. A different sixfold potential would be another new law.

**SOURCE_FACT.** `dynamics.step3` has no geometry, angular displacement, clock or gate-force input. `advance_clock` advances the prescribed q_step and explicit stored time; it has no inertia or damping equation. K2 scalar observers are passive. The real potential of Paper E §18 is a different scalar on six real Omega coordinates, not an angular gate potential; even its negative-gradient increment does not guarantee finite-step descent. Along an evolving trajectory, amplitude and memory change, so frozen angular derivatives alone do not classify temporal extrema. Positive conditional curvature proves neither oscillation nor attraction, confinement, feedback or energy transfer.

**Disposition:** current source supplies readout curvature. A spring interpretation requires a newly defined interaction and response dynamics. Exact finite-patch feasibility neither supplies that law nor rules it out.

## 6. The declared quarter-turn motif

For the actual centered shell \(G=S_{\rm shell}-O\), define
\[
c(\phi)=R(\cos\phi,\sin\phi,0),\quad
e_r=(\cos\phi,\sin\phi,0),\quad e_\phi=(-\sin\phi,\cos\phi,0),
\quad F(\phi)=[e_r,e_\phi,e_z].
\]
The proposed placement is
\[
X_j(p)=c(\phi_j)+\lambda_jF(\phi_j)Q_x(\pi/2)G(p),\qquad
Q_x(\pi/2)=\begin{pmatrix}1&0&0\\0&0&-1\\0&1&0\end{pmatrix}. \tag{9}
\]
Here x means the **local first basis axis before F**, hence the quarter turn is about \(e_r\) in the placed frame. Multiplication order is part of the definition. Direct calculation gives \(F^TF=I,\det F=1\), \(F(2\pi)=F(0)\), and
\[
F(\phi)Q_x(\pi/2)e_z=-e_\phi.
\]
Rotating the shell axis to a tangent direction is distinct from rotating a tangent-frame convention while leaving the axis fixed.

**NEW_ASSUMPTION / single example.** Take \(R=3,\phi_j=2\pi j/12,\lambda_j=1/4\). The central comparison copy is the same shell, centered at the origin, unscaled and unrotated. These are the order's illustrative values, not adopted author physics or a tuned fit.

Every centered source vertex has
\[
B^2=13/12-\sqrt2/2.
\]
The ball of radius B contains each full polygonal face by convexity. Adjacent circle centers are at least \(6\sin(\pi/12)\) apart; therefore small-copy surface separation is bounded below by
\[
6\sin(\pi/12)-B/2>0.
\]
The central/small-copy clearance bound is \(3-5B/4>0\). These bounds suffice without a collision engine.

### 6.1 Minimum tube radius for the filled shells

The minimum here refers to distance from the **circle centerline**, not from a cell center. Rotational invariance reduces all copies to \(\phi=0\). For a centered source point \((x,y,z)\), (9) gives \((3+x/4,-z/4,y/4)\), so its squared distance to the circle is
\[
D^2(x,y,z)=
\left(\sqrt{(3+x/4)^2+(z/4)^2}-3\right)^2+y^2/16. \tag{10}
\]
A vertex-only maximum is not automatically the answer for full faces. The following reduction checks their interiors and boundaries.

On a vertical source face, fix its horizontal local coordinate. The allowed z interval is symmetric and includes zero. As a function of \(v=z^2\), (10) is convex (its second derivative is positive). Its maximum is therefore at \(z=0\) or either allowed extreme \(z=\pm z_{\max}\). This reduces the problem to the z=0 horizontal face segments and the upper/lower piecewise linear rim edges.

For a nonvertical rim edge parametrized by horizontal arc length u, \(x'^2+y'^2=1\); either \(z'=0\) (horizontal edge) or \(|z'|=1\) (chamfer). Write \(\rho=\sqrt{(3+x/4)^2+(z/4)^2}\). Throughout the mesh,
\[
\rho\ge23/8,\quad 3/\rho\le24/23,\quad |z/4|/\rho\le1/23 .
\]
Along the straight edge, differentiating (10) twice yields
\[
\frac{(D^2)''}{2(1/4)^2}
=x'^2+y'^2+z'^2
-\frac3{\rho^3}\big((3+x/4)z'-(z/4)x'\big)^2 .
\]
For a chamfer this is bounded below by
\(2-(24/23)(1+1/23)^2>0\); for a horizontal edge it is bounded below by
\(1-(24/23)(1/23)^2>0\).
Thus each rim edge has its maximum at an endpoint. The \(z=0\) sections have
\(D^2=(x^2+y^2)/16\), whose maximum is \(1/48\) at the three seam footprints. Convexity in \(z^2\) also covers the vertical seams. Comparing the exact 18 vertex values and \(1/48\) therefore covers the entire filled shell.

The largest exact value occurs at vertices 10 and 11:
\[
\tau_{\min}^2=
\frac{(\sqrt{625+s^2}-24)^2}{64}+\frac1{192},\qquad
\tau_{\min}=0.14470916688184346\ldots . \tag{11}
\]
It exceeds \(1/\sqrt{48}\) and is less than the conservative sphere envelope \(B/4\). Both attaining points belong to the shell, so a smaller uniform tube fails. The JSON records all exact comparisons and the positive rational convexity margins. This is a finite geometric result for the declared axis, placement and scales.

### 6.2 Periodic placement is not scale recursion

Equal-size repeated cells give a periodic spatial pattern. At one fixed base, defining \(\lambda_n=\lambda_0s_{\rm scale}^n\) adds a separate hierarchy index and scale choice; for \(0<s_{\rm scale}<1\) sizes shrink, for \(s_{\rm scale}>1\) they grow. Neither defines an interaction.

If a closed ring of M identical steps instead identifies the scale after a full circuit,
\(\lambda_M=\lambda_0s_{\rm scale}^M=\lambda_0\), with \(\lambda_0,s_{\rm scale}>0\), then \(s_{\rm scale}^M=1\). A positive number above one has a power above one; a positive number below one has a power below one. Hence \(s_{\rm scale}=1\). Nontrivial scale recursion needs a separate n or another explicit closure rule. A further twist angle around a chosen local axis is independent of the quarter turn; its own seam condition must be defined. No spectrum or coupling is supplied by (9).

![One geometric placement of rotated shell copies](03_rotated_motif.png)

**Figure 03.** Exactly one declared ring, plus the unscaled central comparison shell. Orange is the circle centerline. Pale lines mark the tube envelope at (11), not a material surface. Cell labels indicate spatial placement indices, not recursive generations, channels or photons.

## 7. Source-limited interpretation of the geometry

**DERIVED.** Threefold symmetry and finite triangle membership can coexist with the metric failure of every proposed representative anchor. This is more precise than either “the six gaps match” or “the triangles cannot match.” It identifies a conditional geometric feasibility result and its remaining definition.

**UNRESOLVED.** The smallest next scientific question is: *which specified readout is assigned to which finite patch point or axis, under which one fixed source-to-shell coordinate dictionary and channel labelling?* A response/spring law remains a further independent question even after that selection. Neither a pair permutation nor the feasible family provides these missing meanings.

No gap ontology, six-gap observer registration, physical field calibration, E8/QCD identification, restored RSB/portal machinery or new kernel mechanism has been adopted.

## 8. Bounded electromagnetic comparison

The primary reference is I. Bialynicki-Birula and Z. Bialynicka-Birula, [*Electromagnetism made simpler: The Riemann–Silberstein vector*, arXiv:1211.2655v1, §§1–2](https://arxiv.org/html/1211.2655v1). It combines electric and magnetic fields in one complex vector and gives the vacuum curl/divergence equations, duality transformation and energy/momentum expressions. Its RS abbreviation is unrelated to this project's SRG and RSB names. Only those sections were consulted.

The following calculation is **DERIVED under a NEW_ASSUMPTION**, not a recovered model dictionary. Write \(\Omega=x+iy\) and suppose
\[
E=E_0x,\quad B=(E_0/c)y
\]
in the same orthonormal spatial frame, with real fixed \(E_0\), \(c>0,\epsilon_0>0\). Direct substitution into vacuum \(u=(\epsilon_0/2)(|E|^2+c^2|B|^2)\) and \(S=\epsilon_0c^2E\times B\) gives
\[
I=|x|^2+|y|^2,\quad C=x\times y,\qquad
u=\frac{\epsilon_0E_0^2}{2}I,\quad S=\epsilon_0cE_0^2C .
\]
The accepted Gram identity implies
\[
I^2-4|C|^2=(|x|^2-|y|^2)^2+4(x\cdot y)^2\ge0.
\]
For \(I>0\) **and \(E_0\ne0\)** this yields \(|S|/(cu)=2|C|/I\le1\). The extra nonzero calibration condition matters: when \(E_0=0\), \(u=S=0\) and the ratio is undefined, even if \(I>0\). Equality requires equal real/imaginary norms and orthogonality. This is the instantaneous null-field condition in the proposed dictionary; the Gram identity itself is standard and already accepted.

General vacuum fields need not satisfy that equality pointwise. It holds for a simple traveling plane wave but does not define all solutions. A common complex phase \(i\) maps \((x,y)\mapsto(-y,x)\), preserving C. A real proper spatial rotation Q instead maps \((x,y)\mapsto(Qx,Qy)\) and \(C\mapsto QC\). For \(\Omega=(1,i,0)\), the former keeps \(C=e_z\); a local x quarter turn sends C to \(-e_y\). Neither operation is an assertion that independently chosen E and B are perpendicular. The separate EMA cubic has \(J(1,1,1)=0\), \(J(i,i,i)=1\), so it is not common-phase invariant.

**COUNTEREXAMPLE from the unchanged recurrence.** At \(\Omega=(1,i,0)\),
\(\epsilon=1/20,g=1/5,k=(1,1,1)\), phase strength zero, the on-site term vanishes componentwise. Hence
\[
\Omega'=\Omega+\frac15L_3\Omega
=\left(\frac{3+i}{5},\frac{1+3i}{5},\frac{1+i}{5}\right),\qquad
\Omega\cdot\Omega=0,\quad
\Omega'\cdot\Omega'=\frac{14i}{25}\ne0. \tag{12}
\]
The dot product here is bilinear, not Hermitian. A separate call to unchanged `step3` agrees with this exact result within the recorded binary64 allowance; no state was repaired to preserve nullness.

The reference vacuum equations \(i\partial_tF=c\,\mathrm{curl}\,F\) and \(\mathrm{div}\,F=0\) require a spatial field and boundary conditions. A three-node graph Laplacian is not that spatial curl merely because each can be represented by matrices. The present dictionary supplies no Maxwell solution, photon helicity, toroidal confinement or energy calibration. There is no derived interaction sum or spectrum supporting an Apéry/zeta connection.

## 9. Execution, verification and preservation

All operations used the existing work-order Python interpreter with `-B` and Windows CMD, importing the authoritative package paths. SymPy supplied exact algebra and fixed symbolic fixtures; NumPy and accepted APIs supplied the bounded binary64 runs. Matplotlib was unavailable. The existing Pillow 12.3.0 renderer produced headless scientific data plots from actual coordinates, with no installation, GUI, browser automation or generated imagery. All three final PNGs were visually inspected; view scales were reduced to remove first-pass label overlaps without changing scientific coordinates or the CSV.

The research tests use independent Paper-C ID/metric fixtures, incidence checks, a matrix inverse for barycentrics, exact cone-edge polynomials, signed unit-circle values, direct scalar finite samples and a separate exact recurrence oracle. Tests are verification procedures, not a theorem count. The complete executed 20 IDs and output are in the JSON.

Exactly one final unchanged package regression suite ran. All 207 discovered IDs matched the entry inventory and all succeeded, including the separately recorded 30 methods in the four local-only test files. Those files remain unchanged and unpublished. No isolated export was required for this research-only task.

One initial development execution stopped with a TypeError because the research script called the source `boundary_loops` property as a method. This was corrected solely in the research script before any trajectories were run; the failed output is retained. Twenty research tests then passed. One successful compute run generated the trajectories. A later figure-only pass changed layout and corrected a timestamp **label** from start to completed; it preserved the timestamp value, fixed map and CSV bytes. Final whitespace checks also found a Markdown two-space line break and a terminal blank test-file line; only those formatting details were removed. The JSON retains these development dispositions. No scientific parameter was altered in response to an outcome.

The evidence contains one complete entry Git index/status record and a final reconciliation. All **43** protected raw identities match: 36 tracked package files, four local-only predecessor test files and three consulted manuscripts. All pre-existing 2,130 untracked status entries outside this output directory remain the same. Final HEAD/tree/index and tracked diffs remain at baseline. The eight new files listed below are the complete persistent write scope. No staged paths, commit or push were created.

| Returned file | Purpose |
|---|---|
| `REPORT.md` | This complete disposition and derivations |
| `investigate.py` | Actual research analysis, bounded runner and figure source |
| `test_investigate.py` | Twenty independent research verification methods |
| `RESULTS.json` | Full new execution evidence, inputs, outputs, source/protection identities and final reconciliation |
| `TRAJECTORIES.csv` | 388 actual rows, 97 per run/observer combination |
| `01_shell_apertures.png` | Accepted shell, finite patches and axial projection |
| `02_macro_registration.png` | Frozen extrema, actual clock samples and conditional dictionary |
| `03_rotated_motif.png` | Single explicit quarter-turn ring example |

To inspect the research tests from the checkout, run the specified interpreter with `-B -X utf8 research\GATE_TORUS_INVESTIGATION_v0.1\test_investigate.py`. The analysis CLI is `investigate.py --compute --scratch EXISTING_TASK_TEMP` and writes only its CSV/three figures plus a computation record in that task-owned temporary directory. It is not an installation or kernel entry point. The evidence records actual execution commands; no rerun is required to review this packet.

Task-owned scratch was removed only after retaining its relevant evidence in `RESULTS.json`; previous temporary evidence was not touched. The JSON binds the seven companion files and has no recursive self-hash. Its own final size and SHA-256 are supplied separately in the delivery.

```
ACCEPTED_KERNEL_MODIFIED = NO
COMPLETED_ARCHAEOLOGY_REOPENED = NO
UNRELATED_RTM_OR_JSX_IMPORTED = NO
GATE_CORRESPONDENCE = MEASURED_AND_CLASSIFIED_NOT_ASSUMED
SPRING_LAW = DERIVED_IF_SUPPORTED_OTHERWISE_CONDITIONAL
TOROIDAL_REPETITION = EXPLICIT_GEOMETRIC_HYPOTHESIS
ELECTROMAGNETISM = BOUNDED_ALGEBRAIC_COMPARISON_NOT_IDENTIFICATION
STAGING_COMMIT_PUSH = NO
NEXT_BOUNDARY = GPT_RESEARCH_REVIEW
```
