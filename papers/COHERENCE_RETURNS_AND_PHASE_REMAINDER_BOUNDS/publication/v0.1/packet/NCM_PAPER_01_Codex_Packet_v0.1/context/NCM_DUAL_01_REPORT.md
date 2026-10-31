# NCM-DUAL-01 v0.1 — Dual Cone-Pair Quarter-Turn Sequence

**31 October 2026 · bounded research review · prescribed kinematics**

| Supplied station | Green opposed pair | Orange opposed pair |
|---|---|---|
| 0 | Left–right, x | Top–bottom, y |
| 1 | Top–bottom, y | Near–far, z |
| 2 | Near–far, z | Left–right, x |

**The sequence is internally realizable.** Both unresolved inward-label branches admit continuous, center-preserving motions through these stations. Under the independent equal-progress quarter-turn trial, the pairs temporarily stop being perpendicular: their smaller axis angle falls from 90° to **60°** and rises to 90°. The two persistently tracked outward rays instead reach **120°** at the midpoint.

The same signed endpoints also admit a common rigid interpolation that remains perpendicular. Its whole-frame rotation is **120° per leg**, although each tracked axis changes direction by 90° between endpoints. These are two different paths through the author's endpoint stations; the rigid comparator does not replace the independent quarter-turn proposal.

Under an explicitly tested repeating extension, pair-axis placements return after three legs in both branches. Persistent cone labels return after six legs for s=+1 and three for s=−1. A deliberately marked cone generator distinguishes a further roll return: the independent s=−1 transport returns fully after twelve legs, whereas the rigid comparator returns after three. An unmarked circular cone does not reveal that roll, so twelve legs is **not an inferred material period**.

The bounded source inspection finds no equation binding these two cone-pair orientations or their progression to native channels, Z, or a golden-ratio controller. This missing connection does not prevent a faithful kinematic representation. The earlier average-arrow P study addresses a different question and supplies no rejection of this proposal.

Open [preview.html](preview.html) locally for a controllable, initially paused view. It needs no server or network. The mathematical checks and preview logic passed; actual browser rendering could not be verified because the browser tool rejected local file URLs. The four PNG figures were inspected directly.

## Author account, received sketch, and unresolved choices

The controlling account is the current work order and the sketch reattached by the author during this task. Green denotes the main Tri-Octagon arrangement and its intended golden-ratio field-controller role; orange denotes the second arrangement. They share a fixed center. The surrounding circle supplies an enclosing reference. The blue strokes are rough structure, not metric data. The toroid is intentionally excluded.

The work order preserves these statements:

> "Imagine each triangle 2x green and 2x orange are 3D cones viewed in this 2D image"
>
> "green has moved 90° clockwise, while orange has moved 90° inward"
>
> "move 90° as if they were chasing the last position known by the orange triangles"
>
> "Given that -z is closer to us and +z is further as viewed from our perspective on this image."

The author additionally fixes orange's depth-to-horizontal map: +z → +x and −z → −x. The phrases “0° z axis” and “−0° z axis” refer to axis directions here; they introduce neither signed-zero data nor another rotation convention.

**Input identity qualification.** The work order describes a 5,722-byte PNG with SHA-256 `8a3d4f9f190f71fbfebed1cc60815584ff77561e50a60185d8a0640c442e6a1b`. That exact byte stream was not found. The author supplied a clipboard PNG during the task: 5,615 bytes, SHA-256 `2d7c31897464687b82f0c4e98fdade1c80c27a3d1eec1d4e5e33b7b08fc5848a`. It is preserved unchanged as [the received private discussion sketch](inputs/RECEIVED_AUTHOR_DISCUSSION_SKETCH.png). This is the author-supplied replacement reference, not a claimed hash match to the original. No dimensions or ratios were extracted from pixels; no image-generation model was used.

| Status | Content |
|---|---|
| Author intent | Three stations; first green clockwise map; orange depth-to-horizontal map; inward-facing cone tips; fixed shared center; green controller interpretation. |
| Unresolved label alternative | Which original orange cone first goes far: s=+1 or s=−1. Both are retained. |
| Trial assumption | Green uses the same inward quarter-turn map that orange used on the preceding leg. Endpoint occupancy alone would not select that path. |
| Trial assumption | Both pairs progress simultaneously with angle θ=(π/2)u, 0≤u≤1, on each independent leg. |
| Comparator assumption | A common shortest proper rotation connects the completed signed endpoint frames. |
| Tested extension | Repeat green's A,B_s,C routing and orange's B_s,C,A routing beyond station 2. The author did not prescribe a full return law. |
| Display convention | Circular cone proxies, nonzero tip clearance, opacity, base radius, camera, and optional marked generators. |
| Still absent | Physical timing, full-mesh attachment, orientation-to-native/Z binding, a controller law, and an observation rule equating simultaneous presence with alternation. |

No additional author answer is required to complete this bounded study.

## Coordinate construction and persistent identities

Use the explanation chart +x right, +y up, +z far. With these screen conventions the chart is **left-handed**. The computational right-handed coordinates are

\[
(X,Y,Z)=(x,y,-z),\qquad H=\operatorname{diag}(1,1,-1).
\]

Vectors convert by v_comp=Hv_chart and rotation matrices by R_comp=H R_chart H. H changes the coordinate description; it is not a physical mirror operation performed on the cones. The computational frame is a convenient right-handed frame, not an identification of native channel indices with spatial axes or of cone axes with accepted mesh features.

Let g point outward toward the base of **G_right0** and o toward **O_upper0**. The partners **G_left0** and **O_lower0** are −g and −o. Inward directions of the representatives are −g and −o; outward location and inward pointing must not be interchanged. Figure abbreviations G_R, G_L, O_U and O_D always retain these initial identities.

| Station | g for s=+1 | o for s=+1 | g for s=−1 | o for s=−1 |
|---|---|---|---|---|
| 0 | +x | +y | +x | +y |
| 1 | −y | +z | −y | −z |
| 2 | −z | +x | +z | −x |

The physical pair-axis placements agree between branches. Only persistent label tracking differs at these stations.

![Three stations, both branches](figures/01_three_stations.png)

*Figure 1. The supplied three stations, both inward branches, with identical orthographic camera and scale. The broad bases face outward; finite clearances keep tips away from exact coincidence. Near/far labels and an oblique camera preserve depth. Labels follow cones rather than screen positions. The proxies are not an inferred Tri-Octagon mesh.*

## Independent quarter-turn trial

For c=cos θ and b=sin θ, the complete chart matrices are

\[
A(\theta)=\begin{pmatrix}c&b&0\\-b&c&0\\0&0&1\end{pmatrix},\quad
B_s(\theta)=\begin{pmatrix}1&0&0\\0&c&-sb\\0&sb&c\end{pmatrix},\quad
C(\theta)=\begin{pmatrix}c&0&b\\0&1&0\\-b&0&c\end{pmatrix}.
\]

Each obeys RᵀR=I and det R=+1. At θ=π/2, A maps +x→−y and −x→+y; B_s maps +y→s z and −y→−s z; C maps +z→+x and −z→−x. The signed **computational right-hand rotation axes**, with positive angle θ, are respectively −Z, −sX and −Y. Stating these axes avoids interpreting “clockwise” from an unspecified viewpoint.

| Leg | Green rotation | Orange rotation | Status |
|---|---|---|---|
| 0→1 | A, chart xy plane | B_s, chart yz plane | Trial path between supplied endpoints |
| 1→2 | B_s, chart yz plane | C, chart zx plane | Trial path between supplied endpoints |
| 2→3 | C, chart zx plane | A, chart xy plane | First leg of the tested return extension |

Applying these matrices to each station's existing orientation gives, on the first three legs:

\[
\begin{array}{c|c|c}
\text{leg}&g(\theta)&o(\theta)\\\hline
0&(c,-b,0)&(0,c,sb)\\
1&(0,-c,-sb)&(sb,0,sc)\\
2&(-sb,0,-sc)&(sc,-sb,0)
\end{array}
\]

These are unit vectors, and applying the same matrices to the opposite cones preserves opposition exactly. Their dot product on every leg, for both branches, is

\[
g\cdot o=-\sin\theta\cos\theta=-\tfrac12\sin2\theta.
\]

For 0≤θ≤π/2 this is between −1/2 and 0, with the minimum at θ=π/4. Thus the directed angle acos(g·o) ranges from 90° to 120°, while the smaller angle between the **unoriented pair axes**, acos(|g·o|), ranges from 90° to 60°. GPT's 60° midpoint statement is correct for the latter object. The 120° directed angle refers to the persistent G_right0 and O_upper0 rays, not to their nearest opposed partners.

If relative progress differs, the same calculation gives

\[
g\cdot o=-\sin\theta_G\cos\theta_O.
\]

For example θ_G=π/2 and θ_O=0 gives opposite directed rays and coincident unoriented axes: 180° and 0°, respectively. This algebraic example shows why the 60° minimum belongs to the equal-progress trial. No additional timing family or sweep was performed.

Progress u is dimensionless. It is not seconds, a native step, a Z sector or geometric τ. The piecewise paths are continuous, but their angular-velocity axes change at leg boundaries; neither acceleration smoothing nor a torque law has been supplied. The angle result establishes no compression, energy transfer or physical speed.

## Rigid comparison with the same signed stations

At station j complete a right-handed frame in computational coordinates:

\[
F_j=[Hg_j\quad Ho_j\quad(Hg_j)\times(Ho_j)],\qquad
Q_j=F_{j+1}F_j^T.
\]

Every endpoint frame is orthonormal with determinant +1. Q_j is therefore a proper rotation. Its trace is zero, giving

\[
\alpha=\arccos\frac{\operatorname{tr}Q_j-1}{2}=2\pi/3=120^\circ.
\]

The first three positive-angle axes in computational coordinates are

\[
a_0=(-s,s,-1)/\sqrt3,\quad
a_1=(-s,-1,s)/\sqrt3,\quad
a_2=(1,-1,-1)/\sqrt3.
\]

Use Rodrigues rotation R(a_j,120°u)F_j on each leg. Because a single orthogonal matrix moves both axes, g·o=0 throughout. The quarter-turn trial's midpoint and this rigid midpoint therefore differ despite agreeing at signed station endpoints. For s=−1 all three rigid axes coincide; this comparator completes one 360° turn after three legs. This is a comparator deduction, not a renaming of the author's independent quarter-turn moves.

![Midpoint comparison](figures/02_midpoint_comparison.png)

*Figure 2. First-leg midpoints for s=+1, and the exact angle formulas plotted over one dimensionless leg. The curves apply to both branches. Arrows show the two tracked outward directions. Spatial camera and scale match; the plotted angle curves are illustrations of the symbolic identities.*

## Tested periodic extension: what returns

Write A=A(π/2), B=B_s(π/2), C=C(π/2). With matrices acting on column vectors, the earliest operation is on the **right**. Green uses A then B then C; orange uses B then C then A. Their three-leg products are

\[
T_G=CBA=\begin{pmatrix}-s&0&0\\0&0&-s\\0&-1&0\end{pmatrix},\qquad
T_O=ACB=\begin{pmatrix}0&0&-s\\0&-s&0\\-1&0&0\end{pmatrix}.
\]

Both initial representative axes acquire the factor −s after three legs. This proves the distinct label returns without relying on visual similarity.

| First return in legs | Independent s=+1 | Independent s=−1 | Rigid s=+1 | Rigid s=−1 |
|---|---:|---:|---:|---:|
| Uncolored set of two pair axes | 3 | 3 | 3 | 3 |
| Green/orange pair-axis occupancy | 3 | 3 | 3 | 3 |
| All four persistent cone identities | 6 | 3 | 6 | 3 |
| Full transported frames / diagnostic generators | 6 | 12 | 6 | 3 |

For s=+1, T_G and T_O have order two. At three legs each opposed pair has exchanged its two persistent identities; at six the full individual transports return.

For s=−1, the labels already return after three legs, but T_G and T_O each have order four. In computational coordinates they retain +90° roll about the original green +X axis and −90° roll about the original orange +Y axis. The independent transported frames return after twelve legs. This becomes observable only after adding a diagnostic marker or an actual nonsymmetric attached feature. Circular unmarked cones are unchanged by rotation about their own axes; no twelve-leg material cycle is inferred.

For the rigid comparator the total transport at an endpoint is fixed by F_jF_0ᵀ. At three legs it is diag(−s,−s,1) in computational coordinates. Thus s=+1 has a 180° remainder and s=−1 has identity; its frame returns occur at six and three legs. Exact products and all signed stations through twelve legs are recorded in results.json. Return counts concern this routing extension; the original three stations alone do not determine them.

![Return categories and deliberately marked generators](figures/03_return_and_roll.png)

*Figure 3. For s=−1 the unmarked pair arrangement repeats every three legs while added black generators change orientation. The generators return at twelve legs. They are explicit diagnostic constructions, not author features. The table compares all return categories and both interpolations.*

### Order reversal is different from reversing the motion

Applying the same quarter turns in reversed chronological order gives

\[
\widetilde T_G=ABC=\begin{pmatrix}s&0&0\\0&0&-1\\0&s&0\end{pmatrix},\qquad
\widetilde T_O=BCA=\begin{pmatrix}0&0&1\\0&s&0\\-s&0&0\end{pmatrix}.
\]

For s=+1 these reverse-order products have order four, whereas the forward products have order two; for s=−1 the orders exchange. They are not the same transformations. A direct witness is AB e_x=−e_y but BA e_x=−s e_z. Actual retracing requires inverse turns in reverse order, e.g. (CBA)⁻¹=A⁻¹B⁻¹C⁻¹. These are ordinary specified rotations; no quantum-spin or particle interpretation follows.

## Sphere, schematic cones, and two meanings of “dual”

The enclosing reference has the original width-dependent radius

\[
\rho=w\sqrt{13/12-\sqrt2/2}\simeq0.6133730937584284\,w.
\]

This value is supplied by the order and independently recovered from the maximum centered radius of the printed width-one host vertices in geometry.py. No extended-edge sphere was used. The chart origin is the shared center; the accepted host's center O=(0,√3/6,0) is inherited registration data. Adding a center offset does not select a cone-to-full-mesh attachment.

The one schematic proxy choice uses w=1; apex radius 0.10ρ; broad-base center radius 0.78ρ; base radius 0.34ρ; and opacity 0.52. Each cone has length 0.68ρ and a 48-segment visual base ring. The full solid proxy lies in the ball: its apex has radius 0.10ρ and every base-rim point has radius √(181/250)ρ≈0.8508818954ρ. Ball convexity contains the cone between them. Proper center rotations preserve this bound for every progress value. This is containment, not collision avoidance or a physical wall.

No lengths, apertures, clearances or field intensities were measured from the sketch. No φ value was assigned as a cone size or spin speed. Opacity and overlapping projections do not represent an additive field or an impossible material collision. The actual Tri-Octagon mesh was not rotated, contact-constrained or collision-tested.

**A — simultaneous arrangements:** both pairs are present at the same progress value. The independent trial then has a meaningful instantaneous relative angle.

**B — one arrangement visiting poses:** at a given instant only one arrangement is present. The green and orange pictures can label candidate orientations, but a relative angle between two simultaneously existing bodies is no longer a literal instantaneous measurement. Connecting the poses into a rapid alternation would require its own timing/selection rule. The preview's B choices show one pair at either candidate pose; they do not invent an alternation schedule.

A measurement could blur that distinction only after its response and averaging rule are declared. No exposure duration, duty cycle, detector nonlinearity, additive energy rule or continuous quantum superposition is specified. A translucent overlay or trail by itself proves no observational equivalence.

![Simultaneous arrangements and single-pair alternatives](figures/04_simultaneous_or_alternating.png)

*Figure 4. A shows both arrangements at one independent-trial midpoint. The two B panels show alternative instantaneous single-pair poses at the same geometric scale. Their colors identify the candidate poses, not two identities simultaneously assigned to one object. No duty cycle or transition timing is asserted.*

## Compact crosswalk to the existing model

The source route label `7cc1fa03af589818bcdcfaaac51838cc36c84253` is a locator, not a checked-out revision claim. No Git command was run. File bytes and selected ranges actually read are recorded in SOURCE_MANIFEST.json and source_reads.json.

| Proposed or existing quantity | Accepted source definition | Correspondence status |
|---|---|---|
| Cone-pair orientation g,o | Work order supplies endpoint axes. Native/observer definitions below contain no these-axis output or transport variable. | New author hypothesis plus the two explicit trial interpolations; no documented native binding found. |
| Relative cone-pair orientation | g·o follows from this investigation's axes. | Exact kinematic deduction; no inherited torque or coupling. |
| Shared center / original sphere | [geometry.py, lines 16–49](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/geometry.py:16), plus the order's original radius. | Center and host scale inherited; cone proxy sizes and full-mesh attachment are additional/absent respectively. |
| Native channels Ω | [dynamics.py, lines 27–104](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/dynamics.py:27): amplitude/coupling stage followed by simultaneous phase synchronization. | Inherited state evolution. The functions do not take cone orientations as inputs or return cone-body rotations. No native update was executed. |
| Decoded face vectors | [face_state.py, lines 22–80](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/face_state.py:22); [observables chapter, lines 78–104](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/NATIVE_RESPONSE_GEOMETRY/manuscript/observables_closure.tex:78): D_i(Ω_i)=Re Ω_i t_i+Im Ω_i e_z. | Inherited invertible state representation on fixed face planes. A possible comparison object, not a two-cone-body attachment. |
| Z and its schedule | [z_manifold.py, lines 46–199](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/z_manifold.py:46), [central paper, equations readouts/placement](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/CENTRAL_GEOMETRY_Z_CHIRAL_RESPONSE/publication/v0.3/manuscript.tex:459), [NCM definitions](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/NATURAL_CORE_MOTION_CORRESPONDENCE/v0.1/main.tex:198): Z=αM+βC, with C=Re Ω×Im Ω and M a scheduled harmonic readout; X=O+μRψZ. | Existing readout and declared point placement. Twelve clock sectors give 30° observer increments, not a body rotation. Three increments do not establish the present 90° choreography. |
| Common native phase | [NCM phase-invariance proposition](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/papers/NATURAL_CORE_MOTION_CORRESPONDENCE/v0.1/main.tex:401). | At fixed observer settings Z is invariant under common phase, while decoded face arrows can change. Common phase alone supplies no shared 3-D material rotation. |
| Fixed central surface | [NCM guide, lines 9–13 and 71–90](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/apps/scientific_ui/NATURAL_CORE_MOTION_v0.1.md:71). | Existing reference remains fixed. Its motion is not obtained by attaching this new cone proxy implicitly. |
| Green's intended golden-ratio controller | Author intent; [historical presets, lines 18–37](C:/TORMENT/TRIOCTAGON_new/trioctagon-physics/kernel_physics/_presets.py:18) and staged config literals in z_manifold.py. | The bounded sources record λ_vp=0.618; they do not bind it to green-cone orientation or this choreography. No explicit referenced controller-to-cone definition was found in these definitions. |

The exact inverse golden ratio is (√5−1)/2≈0.6180339887498948. The historical decimal 0.618 equals 309/500 as a decimal mathematical value, and differs by about 0.0000339887498948482; its stored binary64 value also has ordinary representation rounding. Neither was silently substituted for the other. The name or numerical resemblance of a parameter does not establish that it controls this motion.

The [prior P report](C:/TORMENT/TRIOCTAGON_new/research/NATURAL_CORE_MOTION_GAP_ALIGNMENT_02/REPORT.md:5) restricts one average-arrow common-phase family to its own fixed plane. This proposal involves two orientations moving through multiple coordinate planes. Its successful construction here is consistent with that earlier limited result. The old checker was not rerun and P was not used as a replacement mechanism.

## Answers and smallest missing relation

1. **Realizable?** Yes, as prescribed kinematics, for both signed branches. This is independent of a material-feasibility claim.
2. **Intermediate behavior?** Independent equal-progress quarter turns give a 60° pair-axis minimum / 120° tracked-ray maximum. The rigid comparator stays at 90°. Endpoint data alone do not select between these behaviors.
3. **Return?** Under the stated extension, axes and color occupancy return in three legs; labels in six or three; independent full transports in six or twelve; rigid full transport in six or three, for s=+1 or s=−1 respectively. Markers reveal roll only by deliberate addition.
4. **Simultaneous versus alternating?** Two present pairs have an instantaneous relative configuration. One alternating pair has a single instantaneous pose. An observation/averaging rule is missing before the two can be called equivalent.
5. **Existing equation binding?** No such binding is documented in the bounded native, observer and geometric definitions read here. Z already exists as a readout; that alone does not turn it into two transported cone arrangements.
6. **Smallest missing relation?** Before calling this native-model motion, specify how the existing state/readouts determine the cone-pair orientation or orientations and their progression. For discussing the picture alone, the present axes are already sufficient; no corner/face selection is needed. Path and timing remain explicit alternatives rather than silently chosen physics.

This is a completed investigation of the stated picture, with positive kinematic findings and a missing equation-level connection. It neither accepts nor rejects the author's wider physical interpretation. No force, energy, normalization, feedback, relaxation, snapping or new recurrence was added.

## Reproduction, verification and limits

From Command Prompt in the fresh external directory:

```bat
conda activate torment
cd /d C:\TORMENT\TRIOCTAGON_new\research\NATURAL_CORE_MOTION_DUALITY_01
set PYTHONDONTWRITEBYTECODE=1
python -X utf8 -I -B run_research.py check_duality.py make_visuals.py
```

Python 3.11.15 was used from the existing torment environment, with NumPy 2.4.4, SymPy 1.14.0, Matplotlib 3.10.9, mpmath 1.3.0 and Pillow 12.2.0 already available. Nothing was installed or upgraded. Standalone scripts load only their sibling research module, not the checkout. Scratch/cache paths are inside this new directory.

**18 tests passed, zero failed/errored/skipped.** They check signed author stations, both branches, clockwise and depth maps, chart handedness, proper rotations, opposition, all-leg dot products, midpoint angle types, unequal-progress algebra, endpoint continuity, rigid frames and perpendicularity, distinct first returns, exact products/roll, order reversal, original sphere radius, cone containment, numeric-renderer agreement with exact special angles, preserved sources and absent prohibited imports. Symbolic identities—not numerical sampling—support the claims about continuous paths. Numeric illustrations are not interval certificates.

**60 offline JavaScript logic cases passed** in an isolated VM with stub DOM/canvas: initial pause, branch/interpolation switches, midpoint values, station buttons, visibility qualification, generator toggle, all endpoint poses through twelve legs, and reset. These are logic checks, not browser or canvas-rendering verification. The browser tool rejected the file protocol; no server, alternate browser, account login or other workaround was used. PREVIEW_QA.json records the limitation. Actual final viewing in the user's browser remains a review step.

The mathematical tests include the twelve-file bounded before/after source guard, and packaging repeats the comparison. This is not a whole-repository audit. The first intake guard correctly rejected the mismatch with the original sketch hash; the author-supplied received bytes and the mismatch remain visible in the package. The missing original byte stream is a provenance limitation, not an invitation to reconstruct or alter it.

The read-only source guard depends on the original paths when rerun. An extracted review on another machine can inspect the self-contained calculations and preview; the preservation test cannot certify unavailable originals. The preview itself is fully self-contained. Included papers and installed environments are not required or packaged.

See CLOSEOUT.txt, SOURCE_MANIFEST.json, OUTPUT_HASHES.json and the external archive receipt for actual commands, artifact identities and archive verification. No application/kernel changes, native step/run/resume, clock/EMA advancement, old scientific checker replay, Git commands or publication occurred. Work stops at this review package.
