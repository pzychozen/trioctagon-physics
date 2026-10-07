# TL0 — Top-layer / “top circle” recovery
<!-- Public locator-only derivative; original raw SHA-256 and exact edits in provenance/public_export_map.json. Historical status wording is retained. -->

Read-only mathematical archaeology · 6 October 2026

**Result: no uniquely identified historical “top circle” has been recovered.** The inspected sources contain several different boundaries, angular constructions, displays and recursion proposals. Their formulas do not define a single common object. The strongest *upstream provenance* is the recorded DMQPF/Vesica host intent; the strongest *implemented circular displays* are the later torus frame and RSB halo. Neither attribution establishes what Hilmir meant by the phrase.

```text
TOP_CIRCLE_DISTINCT_OBJECT = OPEN / NOT_FORMALIZED
THREE_WAY_RESEARCH = PARKED
GR0–GR2 / CM0 / SA0 = CLOSED BASELINES, CONSULTED ONLY
PAPER_G = CLOSED
TL0 = EXTERNAL RESEARCH ONLY
```

## 1. Authority, scope and counting convention

**SOURCE FACT.** The authoritative checkout is `project-source/trioctagon-physics`, on `main`, initially at **82cab10cbe550f58c43163fb8b05fabdad1b05ae**. This is the published-paper checkpoint, not the earlier `da461294…` checkpoint. Existing dirty/untracked work was recorded before inspection; it includes scientific-UI changes, local research, tests, the publication supplement ZIP and publication `tmp/`. None was adopted as permission to change anything. The complete initial status and index fingerprint are retained in [the crosswalk/results file][results].

The census below separates **24 historical candidate records: 16 explicitly specified mathematical objects/maps and 8 incomplete geometric proposals or schematics**. This is a source-and-type census, **not a theorem that there are 24 inequivalent circles**, nor a claim that every object was actually called “top circle.” For example, a parent circle, its lens boundary and its perimeter functional are different typed objects, despite exact relationships between them. Duplicate implementations of the same formula are recorded together with their differences. Current rims, the reference scaffold and a later conditional placement are additional *comparators*, not extra historical candidates.

The search covered the named historical UI files and their geometry/readout/RSB call sites; the 46-document P0 text collection; the earlier top-to-recursive source extracts; relevant DMQPF, Vesica, VPQW, D24, E8, Recursive Engines, Forward–Backward, Meta-Shell and v3.4 texts; prior host-recovery records; and the current comparison modules and published Native Response Geometry sections. Literal absence is limited to these inspected sources. Missing original scripts and unindexed images prevent an exhaustive claim about everything ever drawn or discussed. No web novelty search, parameter scan, archived simulation execution or new physics derivation was performed.

Evidence labels have their literal meanings: **SOURCE FACT** reports surviving bytes; **EXACT THEOREM / DERIVED IDENTITY** gives a mathematical consequence with an argument; **NUMERICAL EVIDENCE** means bounded implementation checks; **STRUCTURAL ANALOGY** does not supply a map; **HISTORICAL INTERPRETATION** records an intended architecture; **PHYSICAL INTERPRETATION** is neither established nor adopted here; **OPEN QUESTION** identifies missing data. Definitions adopted by historical or current authors are explicitly called *adoptions*.

## 2. Census: upstream geometry and historical scaffolds

Here “evolves” means a supplied evolution rule, not that a parameter could be varied by hand. Coordinates are mathematical coordinates without a recovered physical calibration.

| ID / object | Exact surviving construction, domain and dimension | Status, evolution and current relationship |
|---|---|---|
| **H01 DMQPF profile** — specified | [DMQPF][dmqpf], PDF pp.1–2, Eqs.(1)–(5): scalar `P(θ)=4r\|θ\|`; corrected scalar given below. Inputs include radius, angle and historical phenomenological parameters. Output is one real scalar where the chosen expression is defined. | Upstream perimeter/profile functional, **not a parametrized curve or surface**. No native update for these inputs. Current boundary response is not this formula. |
| **H02 Vesica parent circles** — specified | [Vesica Delay][vesica], pp.1,9: two equal circles, radius `r>0`, centre separation `0≤d≤2r`, `d=2r cos θ`, `0≤θ≤π/2`. In a chosen rigid planar frame, centres `(±d/2,0)`. Each boundary is 1D in `R²`; each filled disk is 2D. The source adopts `r=1/2`, circumference `π`. | Fixed once parameters are chosen. Neither parent is an enclosing third circle. The current initializer accepts this **lens chart**, without attaching its circles to the shell. |
| **H03 Vesica overlap/aperture** — specified | Same source, Eqs.(2)–(3): intersection of the two disks; boundary of two circular arcs for `0<d<2r`; perimeter `4rθ`, area `r²(2θ−sin2θ)`. At `d=0` the disks coincide; at `d=2r` the lens degenerates to a point. | 2D region and its 1D boundary, distinct from H02. Exact geometric relation to H01's uncorrected scalar on this angle domain. Current `lens_area_norm_v1` uses its area fraction by explicit adoption. Nested lens scale choices are variants of this geometry, not evidence for a third circle. |
| **H04 VPQW toroidal extension** — incomplete | [VPQW][vpqw], §13, Eq.(15): the displayed operator is `a⁻²∂²_θ + b⁻²∂²_φ + ∂²_r`, acting on a proposed wavefunction, with angular variables and a radial variable. No embedding from the preceding lens to these coordinates is supplied. | Historical higher-dimensional/toroidal proposal, upstream of later TGMO language. The displayed differential expression alone does **not** specify an embedded standard torus, its induced metric, a top circle or a current-kernel operator. |
| **H05 Three-octagon centre ring** — specified planar construction; incomplete fold | [Recursive Engines][engines], §1.1–1.3, Eqs.(1)–(3): `C_i=L(cos(2πi/3),sin(2πi/3))`, `L>R`; vertices `C_i+R(cos(θ₀+kπ/4),sin(θ₀+kπ/4))`. A 1D centre circle organizes three 2D octagons. A later inward tilt `α` is proposed. | Fixed reference geometry. This is a circle of **octagon centres**, not a lid. The source's claim of 24 equally distributed boundary vertices does not follow from these translated, equally oriented octagons. The cited `tri.py`/`center3.py` were not recovered in the searched tree. The accepted shell is not obtained by silently choosing `L,R,α`. |
| **H06 Projected E8 ring / upper-lower lift** — incomplete as claimed ring | [E8 source][e8], §§3–4: specified three octets of roots; `π(v)=(⟨v,a⟩,⟨v,b⟩)` for a Coxeter-plane frame. The source claims one projected radial shell and a lift with upper/lower structure. These are finite point configurations in `R²`, then proposed `R³` geometry. | Static projection/lift claim, not state evolution. A same-radius circle and the upper-layer attachment are not accepted merely from prose. In particular a single 24-element orbit under `C¹⁰` cannot follow when `C³⁰=I`: its orbit length divides 3. This elementary inconsistency is sufficient to withhold that claimed identification; TL0 does not reopen an E8 audit. |
| **H07 24-position D24 orientation frame** — specified | [D24–CP][d24], PDF p.3: rotation increment `π/12`, `r²⁴=f²=1`, `frf=r⁻¹`. Angular labels in `Z₂₄` act in the transverse flavour plane. Finite set; not a filled disk or embedded shell rim. | Static orientation scaffold. That presentation has 24 rotations and 48 dihedral elements. The actual historical clock has 12 positions by default, and no automatic equality with these labels. |
| **H08 Twelve-phase curvature rosette** — incomplete drawn curve | [TriOcta violations][violations], PDF p.5, Fig.2: `φ_k=kπ/6`, `k=0,…,11`; modulation `cos12φ`; proposed `κ̇=Aκ^(12/π)(1+η cos12φ)`. Figure shows a scalloped closed display around a small central circle. | Historical abstract phase/curvature picture. No radial equation for the drawn rosette or its small central circle is provided there. The same page/caption also calls the spacing `π/12`; twelve such steps are only a half-turn. Keep this discrepancy. It is not the current `cos3(θ−θ_lock)` Z readout. |
| **H09 Möbius collapse-ladder band** — incomplete surface claim | Same document, PDF pp.7–8, Fig.3: `(s,φ,κ)↦(S(s),φ+π/12,κ exp[λ₀+λ₁ cos12φ])`, with an unspecified successor `S` on nine identity labels. The figure calls outer/inner bands identity/phase space. | Partially specified abstract recurrence. No strip identification, embedding or metric is supplied to establish a Möbius surface or top rim. The native threshold-based stage/identity bookkeeping is not this recurrence. |

**SOURCE FACT / HISTORICAL INTERPRETATION.** H01's displayed corrected profile is

\[
P_{QG}=4r|\theta|\,(1-e^{-M/M_{Pl}})(1+M/M_c)^{-k}
 (1+\sin(\lambda/r))(1+\tanh(T/r)).
\]

The source labels `λ` a de Broglie wavelength and `T` a thickness. Its further GUP, coherence and uncertainty expressions are separate extensions, not instructions to multiply everything together. Those physical claims are not validated by TL0. Crucially, neither a scalar perimeter nor its correction determines a unique curve, centre, radius, attachment or recursive boundary condition.

**DERIVED IDENTITY.** For H02–H03, subtracting the two circle equations gives intersection coordinate `x=0`; then `z²=r²−d²/4` (here `z` is just the second planar coordinate). Each inward arc subtends `2θ`; two arcs have length `4rθ`. Subtract the two isosceles triangles from the two sectors to obtain `r²(2θ−sin2θ)`. Thus the lens-perimeter relation is exact. At coincident centres the limiting boundary is the **existing coincident parent circle**, not a new enclosing object.

The wording “total enclosing geometry” in Vesica Delay p.9 occurs in its derivation `C=2πr=π ⇒ r=1/2`. It supplies no third centre, third radius or enclosing-circle equation. **OPEN QUESTION:** no independently defined third/top circle was located in that passage or the other inspected upstream sources.

## 3. Census: actual historical code and displays

Let `q` be the historical integer `phi_index`, `κ=||Ω||₂`, and `ρ=κ/(1+κ)`. Repeated use of `φ`, `r`, `Z`, or “toroidal” does not make the following maps equal.

| ID / object | Formula, input/output, parameters | Evolution/type; current survival |
|---|---|---|
| **H10 Runtime phase clock** — specified | [model_core][core], lines164–166,183: `q⁺=(q+h) mod N`, `θ=2πq/N`, default `(N,h)=(12,1)`. `Z_N` plus a separately advanced real time. | Evolves independently of `Ω`; finite clock/observer coordinate, not material rotation. Current [Clock][zman] preserves this explicit observer construction. |
| **H11 Scalar/macro/chiral Z readouts** — specified | [model_core][core], lines169–230: `z=Λρ cos[3(θ−θ₀)]e^(−γt)`, `M=z(cosθ,sinθ,1)`, `C=(Im Ω̄₂Ω₃,Im Ω̄₃Ω₁,Im Ω̄₁Ω₂)`, `Z=αM+βC`. Defaults `.618,.244,.577,1,.5`. State plus clock → scalar/`R³`. | Passive state/clock readouts. Not a surface. H11 is algebraically retained by current staged Z and raw chirality APIs, with explicit domains and numerical contracts. Historical UI `Z` trajectories are plots of these vectors; scaling a plot is not attachment to a shell. |
| **H12 Cylindrical history curve** — specified | [geometry_3d][geo3d], lines4–23: history arrays → `(κ cosφ,κ sinφ,z)`, `φ=2πq/12`. [geometry_embeddings][geoemb], lines12–17 repeats it. | Sampled curve in `R³`, varying radius/height; passive history representation. No independent recurrence or native current-shell placement. |
| **H13 History torus chart A** — specified | [geometry_3d][geo3d], lines25–57: `r=r_max ρ`, `χ=(π/2)z/(max_history\|z\|+10⁻⁹)`; standard torus coordinate formula below with `φ=2πq/12`; defaults `R=2,r_max=1`. | History → sampled `R³` points; **whole-history** normalization, so not an instantaneous state map. Radius varies and `\|χ\|<π/2` for finite data. Does not sweep a fixed full torus. The alternate [TorusConfig][geoemb] exposes `N` instead of hardcoding 12; identical formula at `N=12`. No current native dynamics use this embedding. |
| **H14 Three-anchor state torus chart B** — specified | [toy_3d_triocta][ui3d], lines283–325: `φ_j=2πj/3`, `χ_j=argΩ_j`, `r_j=r₀[1+m log(1+\|Ω_j\|)]`; torus formula nodewise, defaults `R=2,r₀=.6,m=.4`. Complex `T×3` history → three `3×T` coordinate arrays. | State-dependent display, three fixed major-angle anchors; individual phases are minor angles. Radius is unbounded as amplitude grows, so “on a fixed torus” is generally false. NumPy `arg0=0` is a display convention, not a continuous phase at zero. Not H13 and not current shell dynamics. |
| **H15 Fixed torus wireframe** — specified | [toy_3d_triocta][ui3d], lines573–590: `R=2,r=.6`; full major/minor angles sampled at 80/40 points. Standard 2D torus surface in `R³`. | Fixed display scaffold, independent of state. It really is an embedded torus at these radii. Its uppermost parallel is mathematically a circle, but the source does not promote that subset to a named “top-circle” variable or recursive boundary. |
| **H16 RSB spectral halo** — specified | Same file, lines520–571: band `m` has `χ_m=2π(m+1/2)/M`; full-circle angle `φ`; `R_h=1.01R`, `r_h=1.05r`; `(X,Y,Z)=((R_h+r_h cosχ_m)cosφ,(R_h+r_h cosχ_m)sinφ,r_h sinχ_m)`. | Finite family of 1D parallel circles. Final RSB energies set colour after clipped logarithmic normalization; effective `α` sets opacity. For fixed band count the circles' coordinates do **not** depend on energies. Later RSB display, not upstream SRG boundary; no corresponding current native object. |
| **H17 Polar corridor occupancy wheel** — specified | [toy_lab][lab], lines155,186–209,294–330: 12 angular bins; bar height `count_j/max(count)`, with strong-event colour. Analogous polar panel in [toy_3d_triocta][ui3d], line503 onward. History → planar histogram. | Observer chart, not a material circle. Uses stored `phi_index` in the actual paths. The helper `compute_phi_index` instead bins `arg(meanΩ)`; its toy_lab docstring says node 0, contrary to its body. These choices must not be conflated. |
| **H18 “Torus tangent” planar curve** — specified | [tangent_corridor_analysis][corridor], lines11–50: `(X,Y)=(R+ρ cosφ)(cosφ,sinφ)`, `φ=2πq/12`, default `R=2`; normalized **finite differences** are compared with two selected `uxy` coordinate differences. | At frozen `ρ` this is a planar limaçon; for changing `ρ`, a sampled varying-radius path. The code uses `φ` for both trigonometric roles, not H13's `χ(z)`. Historical analysis predicate, not a 2D torus or current connection. No native shell boundary map. |
| **H19 Angular gap window** — specified | [seed_emission][gate], lines19–82: `θ_j=wrap(2π(q mod N_g)/N_g+argΩ_j)`; test `\|wrap(θ_j−θ_c)\|≤w`, optionally with `\|mean e^(3i argΩ_j)\|` coherence. Defaults `N_g=24`, centre 0°, tolerance 5°. | Angular observer/event predicate. With the default core clock, only twelve scaffold offsets 0°…165° occur; channel phases add further angles. It is not a 24-step core clock, geometric shell hole or top circle. No current boundary/SRG identification. |
| **H20 Early “toroidal attractor” TGMO field** — specified | [archived TGMO/REFU script][tgmo], lines12–35: with `R=sqrt(X²+Y²)`, `θ=atan2(Y,X)`, field `H(t)(−Y/(R+.1)+.5cos(θ+2πt), X/(R+.1)+.5sin(θ+2πt))`. Exact `H` below. | Prescribed time-dependent 2D quiver field on a fixed grid, not an embedded torus or state-feedback memory. A different historical operator era. Script was read, not executed; not the current scientific kernel. |

The common display formula used in H13–H16 is

\[
\mathcal T(R,r,\phi,\chi)
=((R+r\cos\chi)\cos\phi,(R+r\cos\chi)\sin\phi,r\sin\chi).
\]

**DERIVED IDENTITY.** At fixed `R>r>0` with both angles free, `sqrt(X²+Y²)=R+r cosχ`, so `(sqrt(X²+Y²)−R)²+Z²=r²`. This proves the fixed frame's torus geometry. It does not convert data-dependent radii, discrete angles or a history curve into that whole surface. H15's upper parallel is obtained by `χ=π/2`, giving radius `R` and height `r`. This is a subset calculation, explicitly **not** a recovered separate top-circle definition. H16 samples minor angles at band midpoints; a band need not coincide with that upper parallel.

H20 uses exactly

\[
H(t)=2e^{-.5t}\cos t+e^{-.3t}\sin t+1.5e^{-.7t}+e^{-.4t}.
\]

The script updates arrows by evaluating this prescribed function. It does not integrate particle paths or feed a measured circle back into `H`. The label “toroidal attractor” therefore cannot establish a 3D torus, closed orbit or attractor theorem. Other archived SRG/glyph examples belong to their own recursions; none is silently substituted for the fixed November SRG.

**SOURCE FACT.** The named UI entry points do not implement one shared geometry. `toy_ui_live.py` displays `J_eff(t)` and `(κ,z)`, plus downstream RSB plots. `toy_ui.py` additionally offers Z-vector and diagnostic plots. `toy_lab.py` adds the polar histogram. `toy_3d_triocta.py` draws the wireframe, node embeddings, scaled Z trace and halo. Its Z display uses a history-dependent 99th-percentile norm to scale coordinates by `.85 r_frame/denominator` (lines649–663). This is a further presentation scaling of H11, not a new geometric carrier. No UI was launched.

## 4. Census: recursion-layer and host proposals

| ID / object | Surviving construction and source | Mathematical status and current relation |
|---|---|---|
| **H21 Tilted outer long-return ring** — incomplete geometry | [Forward–Backward recursion][forward], PDF p.8, Fig.2: an oval-looking outer loop around stacked internal shells, with outgoing and long-return arrows. §4.3 defines a three-state shell basis and shift `T\|S_n⟩=\|S_(n+1)⟩`, `S₄=S₁`; short return is written `D_int(Σ T^k)M`. | Diagrammatic 1D loop in a pseudo-3D picture; no radius, embedding, travel metric, geometric `M`, or map to the current shell is supplied. Later finite matrices model labelled return channels, not a derivation of the drawn loop. No identity with current GR circulation or SRG transfer follows. |
| **H22 Z meta-shell / shadow corridors** — incomplete | [Meta-Shell][meta], PDF pp.2–3: primary 12-sector `T_Ω`, secondary `T_Z`, `B:C_j^(Ω)↦(C_k^(Z),w_jk)`, `Z_mem(t)=∫Φ(J_eff,ΔZ)dτ`; proposed loop `T_Ω→T_Z→bias on T_Ω`. | An interpretive/history layer with unspecified `Φ`, weights, threshold and transition law, not a defined surface. Historical intent for feedback exists. Current opt-in EMA diagnostics do not supply this missing shell-to-transition interface. |
| **H23 Unified seed-manifold union** — incomplete | [Chirality-stabilized geometry][seedunion], §§2–3: `Γ=Γ_VPQW∪Γ_toroid∪Γ_RSB`; lens wavefunction, toroidal phase corridors and spectral bands appear together. The text uses 24 corridor angles `2πk/24`. | Nominal union of different spaces; no gluing, common coordinates or boundary attachment. State-dependent descriptive intent, not a constructed host. The v3.4 guardrail [memo][memo] explicitly says visual geometry does not feed back. |
| **H24 Larger circular/Vesica host of a local module** — incomplete | [earlier host specifications][host], H-H, records Hilmir's intent that the canonical folded module is local within a larger circular/Vesica construction. The [bridge reconciliation][bridge] records DMQPF as the upstream “dark-profile / top-layer” description. | Best provenance for the upstream meaning of “top layer,” but **no surviving exact host equation or module insertion map** in these records. Dimension, radius, central axis, evolution and recursion interface remain unspecified. This is retained intent, not a recovered extra circle. |

These eight incomplete entries (H04, H06, H08, H09, H21–H24) are not promoted to established geometric objects. The words “circle,” “shell,” “toroidal,” “Möbius” and “recursive” have different mathematical content in each.

## 5. Architecture and actual arrows

**HISTORICAL INTERPRETATION, supported but not a single exact pipeline:**

```text
DMQPF / perimeter-profile intent
    → Vesica overlap / delay / VPQW geometry
    → several SRG / RPCO / TGMO / REFU formulations
    → Tri-Octagon geometry and the later complex-triad recurrence

Tri-Octagon readouts → later RSB spectral extension → display halo
```

The source support is specific: DMQPF supplies a perimeter expression; Vesica Delay supplies the same uncorrected overlap expression and a delay interpretation; VPQW explicitly proposes toroidal continuation; [Symbolic Recursion and SRG Fusion][fusion], §2.1, calls overlap of two glyph fields “Vesica compression”; Recursive Engines applies named recursion operators to a folded chamber; v3.4 says RSB is run **after** the TriOcta run and rendered as a halo. These establish documentary lineage. They do not show that DMQPF's corrected scalar generates a particular circle, that a lens induces the SRG matrices, or that those matrices derive the nonlinear triad recurrence. Chronology also includes later retrospective synthesis; it is not a single monotonically developed set of equations.

The pre-existing bridge audit separates fixed finite-dimensional SRG, glyph/ensemble SRG and other historical uses of the acronym. The fixed-operator core projection and the triad's synchronized subspace provide a limited algebraic correspondence; the audit explicitly leaves the historical dynamical handoff underived. TL0 preserves that distinction.

### The exact implemented historical downstream bridge

**SOURCE FACT / DERIVED IDENTITY.** In [toy_3d_triocta][ui3d], lines102–135 and220–280 (and a related helper in `toy_ui_live.py`), define

\[
J_{\rm norm}=\operatorname{clip}_{[0,1]}
\frac{\operatorname{mean}|J|}{\max |J|},\qquad
\sigma=\operatorname{sign}(\operatorname{mean}J_{\rm tail}),
\]

where a zero maximum uses denominator 1, and the tail is the last 20 samples when there are more than 20, otherwise all samples. Then

\[
\alpha_{\rm eff}=\alpha_0(.3+.7J_{\rm norm}),\quad
\mu_{\rm eff}=.6+.2\sigma,\quad
\gamma_{\rm eff}=.2(.5+.5J_{\rm norm}).
\]

The absent/empty-input fallback is `(α₀,.6,.2)`. The 3D runner uses `α₀=.6`, RSB couplings `.02,.30`, and `η=.005`; it computes an RSB history, takes final band energies, and sends these to H16. This is an exact **readout → RSB parameter preparation → RSB output → graphic** chain. The ring coordinates themselves are not inputs to the RSB run or to the preceding TriOcta evolution. The v3.4 PDF p.3 expressly states that no explicit SRG calculations are implemented there.

H22 proposes a genuinely different return arrow, but does not define it sufficiently to reconstruct. H20 has explicit time dependence, not state-to-memory feedback. H21 defines a cyclic operator on named shells, not a geometry-to-SRG coupling. None supplies the requested historical `state → top object → recursive continuation` map.

### The exact current initialization interface

**SOURCE FACT / ADOPTED DEFINITION.** [boundary_response.py][boundary] and [srg.py][srg], together with the published [preparation discussion][attachment], supply

\[
\theta=\arccos(d/2r),\quad
G(\theta)=\sqrt{(2\theta-\sin2\theta)/\pi},\quad
\psi_0=G(\theta)(\xi\otimes f_0),\quad
\Omega_0=(\chi^\dagger\otimes I_3)U^n\psi_0,
\]

with `r>0`, `0≤d≤2r`, `ξ∈C²`, `f₀=(1,1,1)/√3`, helicity-major order, named eigenbra `χ`, and fixed `U=B_s⊗A_s`. Here `n` counts preparation transfers, not later kernel steps. More explicitly, for `n=3m+j`,

\[
\Omega_0=G(\theta)(\chi^\dagger\xi)b_\chi^n
 (r_s q_s^2c_s^2)^m(1,q_s,q_s^2c_s)_j f_j,
\]

where `q_s=e^(-.423)`, `r_s=e^.577`, `c_s=1−.618`; these symbols are SRG coefficients, not geometric radii. The native recurrence then evolves `Ω` with its own parameters. Floating APIs further restrict representability; the algebra does not override those contracts.

This is a surviving exact *adopted initialization* map. It neither recovers physical DMQPF nor attaches `ξ` to two rim traces, the lens to a material aperture, or any circle to the shell. `lens_area_norm_v1` is explicitly selected by name. The current recurrence contains no return path into lens geometry or preparation parameters.

## 6. Current-kernel comparison: what does and does not match

**SOURCE FACT / retained exact geometry.** [geometry.py][geometry] specifies three width-one regular octagonal panels, fold angle `π/3`, side `s=√2−1`, and exact vertex welding. There are 18 distinct vertices, three shared seams and two nine-edge boundary cycles. The material surface is an annulus with polygonal, nonplanar rims; it has no filled top or bottom cap. Twenty-four face-vertex incidences are not twenty-four distinct shell points.

**DERIVED IDENTITY, bounded recheck.** The upper rim contains six vertices at `z=1/2` and three at `z=s/2`. Three of the high vertices are noncollinear. Any plane through all those high vertices is `z=1/2`, which excludes the low vertices because `s≠1`. Hence the upper rim is not planar; reflection gives the same conclusion below. It cannot be a Euclidean circle. Its topology `S¹` supplies only a topological resemblance to a ring, not a preferred metric or parametrization identifying it with H02, H07 or H15.

The panel maps are the exact affine formulas in `geometry.panel_point` (lines34–49). Face centres `c_i`, outward normals `n_i`, tangents `t_i=e_z×n_i` and `e_z` are fixed, derived in [face_state.py][face]. The accepted decoder and matched connection are

\[
D_i(q_i+ip_i)=q_it_i+p_ie_z,\qquad
T_{ij}=t_it_j^T+e_ze_z^T.
\]

These relate **state coefficients to tangent vectors**, not to points on any historical circle. `c_i+D_iΩ_i` is generally outside the finite face. Closed matched transport is the tangent identity (ambiently a projector); it defines no ring circulation in physical space.

| Current comparator | Exact content retained | Consequence for the census |
|---|---|---|
| Fixed shell and two rims | Paper-C mesh, affine frames, actual boundary cycles | No historical top-circle identity recovered. H05 supplies an ancestral motif only; H06/H07 cardinalities do not identify mesh vertices. |
| Z/chirality observers | H10/H11 formulas survive in current staged Z and raw chirality modules | Exact formula-level continuity, with explicit clock/configuration and distinct numerical contracts. No embedding into a shell is implied. |
| CM0 equivariants | Published [spatial-observable census][attachment], lines19–55: multiple independent polar/axial maps, not a unique position. Raw `C=ReΩ×ImΩ` is a channel triple; its ambient polar/axial projections use the accepted frame representation. | A displayed `R³` triple in H11 is not automatically a polar spatial vector or a physical axis. This rules out silently identifying viewer coordinates with face coordinates. |
| SA0 finite attachments | Published attachment section, lines78–151: adopted face decoder; finite vertex/edge/seam/rim assignments require specified carriers and labels; no material motion or boundary feedback | A valid finite assignment is not a continuous rim field or a recovered host surface. |
| Reference scaffold | [reference_scaffold.py][scaffold], lines171–277: `p=(s+2g_gap)/(2√3)`, `L=p+(1+√2)s/2`; six selected endpoints `p u_i±(s/2)t_i` form an alternating hexagon, circumradius² `(s²+sg_gap+g_gap²)/3`. Fixed two-parameter geometry. | There are well-defined centre/circumradius data here, but no privileged top circle. The hexagon boundary is not its circumcircle. `g_gap` is not recurrence coupling `g`. |
| Exact scaffold-to-shell special member | Same file, lines339–352: `p=a/√3`, `a=(1+√2)s/2`, rigid map `R_z(π/6)v+(0,a/√3,0)`; frame order maps to P3,P1,P2. Width one recovers Paper C. | A real exact geometric comparison exists, but only for the stated member and embeddings. It does not retrospectively complete H05's arbitrary tilt or H24's missing host. |
| Graph covering | [covering.py][covering] and Atlas 02: reduction of cyclic labels and pullback of admissible cycle states | Shared cyclic algebra is real; circle embeddings, radii and geometric feedback are additional data. |
| Lens/SRG preparation | H02–H03 → named response → fixed SRG transfer → `Ω₀` → optional decoder | Exact adopted typed interface, distinct from DMQPF, torus plotting and rim boundary conditions. |

**Separate later research comparator.** The existing untracked [Gate/Torus report][gatereport], dated 24 September 2026, §6, explicitly *assumes* a placement of shell copies:

\[
X_j(p)=c(\phi_j)+\lambda_j F(\phi_j)Q_x(\pi/2)(p-o),\quad
c(\phi)=R(\cos\phi,\sin\phi,0),\quad F=[e_r,e_\phi,e_z].
\]

Its declared example uses `R=3`, twelve sites and `λ_j=1/4`; the local quarter-turn sends the original shell axis to `−e_φ`. This is an actual conditional geometric placement with a tube-envelope calculation. It was **not** newly derived, rerun, adopted or altered by TL0. Its centreline, placed copies and envelope are distinct from H13–H16 and from the unchanged native shell. The report itself leaves the readout/gate/SRG dictionary open. Thus “there is no geometric placement anywhere in the research” would be false; “there is no recovered canonical native top-circle attachment” remains supported.

## 7. GR1/GR2 circulation versus historical rings

**Retained exact result, not reopened.** The published [response section][response], lines121 onward, distinguishes the positive-branch pre-synchronization matrix

\[
P=R_r^{-1}H_rR_r,\quad R_r=\operatorname{diag}(r_i),\quad
R_r^2P=P^TR_r^2,
\qquad J_\phi=S_\phi P.
\]

GR1's triad obstruction is the difference of oriented **products of matrix entries**

\[
\mathcal C=J_{12}J_{23}J_{31}-J_{13}J_{32}J_{21}.
\]

GR2 analyzes the complete response spectrum and finite-ring Bloch blocks. Neither construction defines a spatial path, torus winding number, holonomy of the matched face connection, or boundary flux. All published hypotheses and distinctions between diagonal balance and general SPD self-adjointness remain in force.

The exact relationships are limited:

- **Shared cyclic representation:** the triad/cycle adjacency, the historical three-state shell shift, phase-sector labels and abstract covering reductions all use cyclic sets/actions. Identifying their *state meanings* or geometric embeddings requires an extra map. The 12-clock, 24-orientation frame and N-site perturbation graph are not one variable.
- **No recovered algebraic correspondence:** no inspected source identifies `𝒞`, Bloch phase or a GR spectral invariant with H13/H14 torus angles, H16 energy colours, H18 chord alignment or H21's long-return operator. Their input/output types already differ.
- **Decisive non-implication:** the unequal branch used by GR is a fixed native state. Its response cycle obstruction can be nonzero under the published hypotheses while a state-only embedding such as H14 remains constant. Conversely H10 can advance with a fixed/equal state and H11 can change through its explicit clock. Thus visible angular progression is neither necessary nor sufficient for the GR obstruction.
- **STRUCTURAL ANALOGY only:** directed cyclic response and an oriented ring drawing can both suggest “circulation.” This language supplies no physical flow or curvature, and no missing interface.

There is no contradiction with the flat matched connection: it transports state-frame coefficients, whereas GR differentiates an ordered nonlinear update on a background. TL0 infers no universal no-go theorem for future emergent geometry.

## 8. Verification and preservation

[verify_tl0_sources.py][script] performs bounded source checks and direct algebra/numerical consistency checks. It does not launch UIs, archive simulations, recurrent trajectories or test suites from parked projects. Historical geometry functions are isolated from their ASTs; only the pure current geometry constructor is loaded, with bytecode writing disabled.

The checks cover: lens formulas and area normalization; exact two-rim/nonplanarity data; standard torus identity; parity between the two H13 implementations at `N=12`; H13's whole-history dependence and angular range; H14's anchors and distinction from H13; halo circles and energy-independent coordinates; clock/gate stride distinction; the literal H18 limaçon expression; and the readout-to-RSB call sequence. Source checks support bounded dataflow statements, not a universal proof of absence across unknown files.

**Final verification: 63/63 PASS** — 9 algebra/geometry identity checks, 8 bounded numerical checks and 46 source/existence/integrity checks. The detailed outcomes and source hashes are in [tl0_object_crosswalk.json][results]. They are **TL0 checks only**; no earlier paper-local or checkpoint counts are rerun or recombined. These counts are not a count of proved research theorems. Three relevant primary pages were visually inspected: Vesica Delay p.1, TriOcta violations p.5, and Forward–Backward recursion p.8. They respectively show the overlap formulas, a rosette with an unparameterized central circle, and the labelled outer-return schematic. Text extraction was not used as a substitute for these figure checks.

**Preservation PASS.** Complete path/content inventories outside `.git`, plus Git HEAD, working-tree status and index entries, match the pre-inspection snapshot. The four protected roots contain 8,571 files (authoritative checkout), 401 (historical `kernel_TO`), 15 (`kernel_torment`) and 4,162 (non-authoritative sibling `kernel_physics`). All four inventory hashes match. Thus the protected papers, kernels, UI, history, fixtures and pre-existing tmp/untracked files retain their bytes and paths. Only this external report, its crosswalk/results and its bounded verification script are deliverables. No staging, commit, push, tag, release, cleanup of existing work or new implementation occurred.

## 9. Final answers and stop

1. **How many?** Twenty-four distinct source/type candidate records were separated: sixteen specified constructions and eight incomplete proposals/schematics. This count includes non-circular readouts and recursion diagrams because they are plausible sources of the phrase. It is not twenty-four recovered “top circles,” and the wider uninspected history may contain more.
2. **Strongest attribution?** No unique object. The strongest *upstream attribution* is H24's retained larger circular/Vesica-host intent, together with the DMQPF/Vesica profile H01–H03. The strongest exact *late display* alternatives are H15 and H16. A specific original labelled drawing or description is still needed to choose between these meanings.
3. **Which layer?** The upstream candidate is boundary/profile/Vesica intent. The concrete late circles are display geometry and downstream RSB visualization. The rosette is phase-space imagery; the long-return ring is recursion imagery. None has been proved to be the shell's top rim.
4. **Exact current mappings?** Yes: staged Z/readout formula continuity; abstract cycle pullbacks; the special reference-scaffold/Paper-C rigid correspondence; and the explicitly adopted lens-area → SRG → initial-triad → face-decoder chain. No one of these identifies a canonical historical top circle.
5. **GR connection?** Shared cyclic language/representations only where specified. No algebraic identification with historical torus/circle geometry was recovered. GR response circulation can exist at a fixed background with a constant state-only display.
6. **What survives exactly?** The two-circle/lens equations, typed scalar profile, discrete clocks/gates, Z formulas, distinct cylindrical/toroidal/limaçon display maps, fixed halo parallels, explicit downstream RSB parameter map and adopted current initializer. The report preserves their different domains and roles.
7. **What is missing?** First, an attributable choice of the intended object. Then its ambient space, dimensions/scale, orientation/attachment to the fixed shell, and a typed geometry-to-recursion rule. Neither a topological circle, common constant, nominal set union nor a ring picture supplies these.
8. **ONE justified next calculation:** a bounded **identifiability calculation for the existing adopted lens→SRG initializer**: at fixed nonzero incident state, named helicity branch and transfer count, characterize its fibres in `(r,d)` and the zero-overlap exceptions. This asks exactly which lens data can survive into `Ω₀`, without choosing a new top circle or changing any law. It would constrain a possible interface; it would not settle historical attribution. No such follow-up is started here.

**TL0 stops with `TOP_CIRCLE_DISTINCT_OBJECT = OPEN / NOT_FORMALIZED`. No physical interpretation is established.**

[results]: project-source/research/TL0_top_layer_recovery_20261006/tl0_object_crosswalk.json
[script]: project-source/research/TL0_top_layer_recovery_20261006/verify_tl0_sources.py
[dmqpf]: project-source/reconstruction/physics_kernel/bridge_IV_A_codex_support/DMQPF.txt
[vesica]: <project-source/trioctagon-physics/research_files/sources/Downloads/Vesica Delay Method-1.pdf>
[vpqw]: project-source/reconstruction/physics_kernel/bridge_IV_A_codex_support/VPQW.txt
[engines]: project-source/trioctagon-physics/research_files/verification/phase3_host_feedback/paper_text_pdfs_old/Recursive_Engines_Across_Scales__From_Vesica_Thermodynamics_to_QGS.txt
[e8]: project-source/reconstruction/physics_kernel/bridge_IV_A_codex_support/E8_SU3.txt
[d24]: project-source/reconstruction/physics_kernel/bridge_IV_A_codex_support/D24_CP.txt
[violations]: project-source/pdfs_old/TriOcta_violations.pdf
[core]: project-source/kernel_TO/model_core.py
[geo3d]: project-source/kernel_TO/geometry_3d.py
[geoemb]: project-source/kernel_TO/geometry_embeddings.py
[ui3d]: project-source/kernel_TO/toy_3d_triocta.py
[lab]: project-source/kernel_TO/toy_lab.py
[corridor]: project-source/kernel_TO/tangent_corridor_analysis.py
[gate]: project-source/kernel_TO/seed_emission.py
[tgmo]: <project-source/trioctagon-physics/research_files/archive_members/Zenodo_research/17253999/Reading material.zip/Simulations_Trash/Early_simulations/TGMO_REFU_toroidal_attractor_lock_in.py>
[forward]: project-source/pdfs_old/FB_recursion/Forward_Backward_recursion.pdf
[meta]: project-source/trioctagon-physics/research_files/verification/phase3_host_feedback/paper_text_pdfs_old/The_Meta_Shell_int.txt
[seedunion]: project-source/trioctagon-physics/research_files/verification/phase3_host_feedback/paper_text_pdfs_old/chirality_stabilized_geometry.txt
[memo]: project-source/reconstruction/physics_kernel/P0_source_map/extracted_text/P37.txt
[host]: project-source/reconstruction/HOST_GEOMETRY_CANDIDATE_SPECIFICATIONS_v0.1.md
[bridge]: project-source/reconstruction/bridge_IV_A/BRIDGE_IV_A_DMQPF_VESICA_SRG_RECONSTRUCTION.md
[fusion]: <project-source/trioctagon-physics/research_files/supporting_research_snapshot/top_to_recursive_bridge/source_text/S04_1.Symbolic Recursion and SRG Fusion.txt>
[zman]: project-source/trioctagon-physics/kernel_physics/z_manifold.py
[boundary]: project-source/trioctagon-physics/kernel_physics/boundary_response.py
[srg]: project-source/trioctagon-physics/kernel_physics/srg.py
[geometry]: project-source/trioctagon-physics/kernel_physics/geometry.py
[face]: project-source/trioctagon-physics/kernel_physics/face_state.py
[scaffold]: project-source/trioctagon-physics/kernel_physics/reference_scaffold.py
[covering]: project-source/trioctagon-physics/kernel_physics/covering.py
[attachment]: project-source/trioctagon-physics/papers/NATIVE_RESPONSE_GEOMETRY/manuscript/observables_closure.tex
[response]: project-source/trioctagon-physics/papers/NATIVE_RESPONSE_GEOMETRY/manuscript/response.tex
[gatereport]: project-source/trioctagon-physics/research/GATE_TORUS_INVESTIGATION_v0.1/REPORT.md
