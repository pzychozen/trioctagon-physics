# Bridge IV-A — corrected accepted-results digest v0.2

Date: 2026-09-22. Documentary synthesis, not a new proof campaign or repository freeze.
Science: accepted individual results with the scopes below. Review: based on the completed Codex adversarial review; this digest awaits bounded continuity review. Record: local only. Implementation: no kernel admission.

Sources: [Codex v0.1 review](../physics_kernel/BRIDGE_IV_A_CODEX_ADVERSARIAL_REVIEW_v0.1.md), [unchanged Claude reconstruction](../../pdfs_new/BRIDGE_IV_A_DMQPF_VESICA_SRG_RECONSTRUCTION.md), and [prior v0.1 digest](C:/Users/Notandi/Downloads/BRIDGE_IV_A_ACCEPTED_RESULTS_v0.1.md). The review's 68+61=129 recorded predicates include counterexamples and integrity checks. They are not 129 theorems or a reproduction of Claude's 128 predicates; no verifier was rerun here.

## 1. Intended model and version control

DMQPF/Vesica boundary → first SRG recursion → Tri-Octagon/toroidal realization is retained as the intended architecture. E6 at the top and E8 inside is MODEL_DESIGN_INTENT. Neither standard subgroup branching nor a Coxeter-plane projection substitutes for this placement. The full physical chain remains unresolved.

The fixed SRG, field-composite REFU/TGMO/RPCO and glyph variants are distinct source objects within that program. Preserve their equations and implementation order; names do not prove equality. See review evidence table, A4–A6 and A10.

## 2. Upstream results and the Three-Way scope correction

Sources: [A1–A5](../physics_kernel/BRIDGE_IV_A_CODEX_ADVERSARIAL_REVIEW_v0.1.md#a1-vesica-geometry-and-documentary-transfer).

- Lens: for \(r>0,\ 0\le d\le2r,\ \theta=\arccos(d/(2r))\in[0,\pi/2]\), \(d=2r\cos\theta,\ P=4r\theta,\ A_{\rm lens}=2r^2\theta-r^2\sin2\theta\). Full-angle and half-angle conventions must be translated.
- VPQW and January TGMO share \(a^{-2}\partial_\theta^2+b^{-2}\partial_\varphi^2+\partial_r^2\) as a documented differential expression. This is the flat product expression, not the induced embedded-torus Laplace–Beltrami operator. A cover date does not establish the date or copying direction of every appended section.
- DMQPF explicitly names a de Broglie wavelength. \(\sin(\lambda/r)\) and \(\sin(2\pi r/\lambda)\) have different zero sets and phase gradients; a conventional cosine also occurs in the source. No wave equation is thereby derived.
- DMQPF calls \(M\) filament mass density. Its density type and reference scales are unresolved. Under dimensionless \(\eta\), \(\sqrt{\hbar/(Mv)}\) has length for linear density; replacing it with \(\hbar/(Mv)\) is not an established repair. Density divided by Planck mass requires an additional scale. No mass-based astronomical estimate is accepted here.
- The inspected default \(H(t)\) is a time-only, functionally active schedule. Its six-state autonomous realization does not turn it into endogenous feedback memory. Dynamic REFU in the [R1 digest §4](RECURSIVE_STATE_I_ACCEPTED_RESULTS.md#4-dynamic-refu-exact-elimination-initial-memory-retained) is a different object.

**Three-Way requires two dated records.** A3 verifies the February 10, 2025 *ThreeWayRefined* p.3 Eq. (4),
\(f(x)=-\lambda(x^2-1)e^{-\alpha(1-|x|)}\).
For \(\lambda>0\), \(+1\) attracts and \(-1\) repels; finite-time escape for \(x<-1\) additionally requires \(\alpha\ge0\). The added-\(x\) odd field and quartic-wall/tanh connection are NEW_CONSTRUCTION_NOT_LINEAGE, with a separate spatial gradient energy and coordinate identification.

The May 1, 2025 final draft is a different source: §3.4, PDF p.5 uses a tanh coupling law; Appendix C, PDF pp.13–14 explicitly supplies reciprocal rational maps. For example, p.13 prints
\[
f_1(x)=\frac{9x^4-9x^2+1}{x^4-9x^2+9},\qquad 1/f_1(x).
\]
This is a transcription establishing source presence, not a new theorem about its poles, intersections or attractors. It refutes the blanket source claim in Claude §5.6 that reciprocal structure is absent from Three-Way. The February result cannot classify the May map. Nor does \(f=1/f\), hence \(f=\pm1\) where both sides are defined, by itself define temporal attraction.

Evidence: [existing extraction, PDF page markers 5 and 13–14](../../verification/host_geometry_phase2_codex/paper_text/Downloads__three_way_final_draft-1.pdf.txt), [source manifest](../../verification/host_geometry_phase2_codex/paper_manifest.json), [hash-matching PDF alias](../../pdfs_old/three_way_final_draft.pdf). SHA-256: e6543e658a293693e8d66a78d1715d04941fb9cb1be714567a7fb62c797c39ad. The manifest's historical Downloads draft-1 name need not still exist; the project PDF and current Downloads draft have that same hash. Later reciprocal-map work is not adjudicated here.

## 3. Fixed SRG and the shared subspace

Source: [A6](../physics_kernel/BRIDGE_IV_A_CODEX_ADVERSARIAL_REVIEW_v0.1.md#a6-fixed-srg-exact-factorization-and-shared-channel-algebra), fixed-SRG source dated 2025-11-24.

Use helicity-major \(\mathbb C^2\otimes\mathbb C^3\), \(s=(1,1,1)^T/\sqrt3\), \(p=ss^\dagger\), \(q=e^{-\eta}\), \(r=e^\gamma\), \(c=1-\lambda_c\), \(\omega=e^{2\pi i/3}\):
\[
R=qI+(r-q)p,\quad C=cI+(1-c)p,\quad
Z=\operatorname{diag}(1,\omega^{-1},\omega^{-2}),
\]
\[
B=e^{-i\alpha\sigma_z}e^{-i\beta\sigma_x},\quad A=RZC,\quad U=B\otimes A.
\]
These preserve the source factor order. \(Z\) here is a corridor clock matrix, not \(Z_{\rm chiral}\).
For \(Xe_k=e_{k+1}\), \(XAX^{-1}=\omega A\): covariance, not commutation. In \(F=(s,Zs,Z^2s)\),
\[
F^\dagger AF=\begin{pmatrix}0&0&rc\\q&0&0\\0&qc&0\end{pmatrix},
\qquad A^3=dI,\quad d=\det A=rq^2c^2.
\]
For \(0\le\lambda_c<1\), \(d>0\), \(a=d^{1/3}\), the corridor eigenvalues are \(a,a\omega,a\omega^2\). All six eigenvalue moduli of \(U\) equal \(a\); its singular values are \(q,qc,rc\), each twice.

The exact shared-channel identity is
\[
L_3=-3(I-p),\quad \Pi_{\rm core}=I_2\otimes p,\quad
\operatorname{im}\Pi_{\rm core}
=\mathbb C^2\otimes\ker L_3
=\ker(I_2\otimes L_3).
\]
It identifies a subspace, not a projector with a kernel. The full product does not preserve the balanced line: \(As=qZs\). A face/corridor label identification gives an exact representation match; it does not supply an evolution-compatible map into Paper A.

## 4. Raw and normalized dynamics

Source: [A7](../physics_kernel/BRIDGE_IV_A_CODEX_ADVERSARIAL_REVIEW_v0.1.md#a7-raw-and-normalized-dynamics).

At \(\alpha=2\pi(.244),\beta=\pi(.244),\lambda_c=.618,\gamma=.577,\eta=.423\), recorded \(a=0.48131992098\) and \(\|U\|_2=0.68022294764<1\). The raw map has zero as a global attractor. These contraction numbers do not apply to every allowed gain/loss parameter.

For \(c>0\), normalized unit vectors obey \(N(v)=Uv/\|Uv\|\) and \(N^3(v)=(B^3\otimes I_3)v\). The induced \(\mathbb{CP}^5\) map has fixed eigenrays, projective period-dividing-three subfamilies in one helicity eigenspace, and generic one-frequency recurrence with closure at most three circles. Similarity to a unitary projective action excludes open-basin attracting rays/cycles in this invertible equal-modulus family. Generic irrational recurrence is established for the exact printed decimal, not for an unspecified rounded physical constant. An attractor is not a prerequisite for recursion or a boundary-state handoff.

## 5. Non-Hermitian, PT, endpoint and phase results

Sources: [A8–A9](../physics_kernel/BRIDGE_IV_A_CODEX_ADVERSARIAL_REVIEW_v0.1.md#a8-non-hermitian-generator-pt-and-exceptional-points).

Under \(U=e^{-iH}\), \(H_{\rm mem}=i[\gamma\Pi-\eta(I-\Pi)]\); the opposite historical sign is rejected. \(R\) and \(Z\) generally do not commute.

At the printed point, principal \(H_{\rm eff}=i\operatorname{Log}U\) has nonzero common imaginary eigenvalue part \(\log a\), excluding a commuting antiunitary. Removing uniform decay gives \(H_0=H_{\rm eff}-i\log(a)I\); the frozen non-real eigenray Bargmann product still obstructs an isometric antiunitary. This is not a family-wide PT prohibition: the allowed interior family \(c=e^{-(\gamma+\eta)/2}\) admits the review's shifted algebraic PT construction. Its parity is not identified with a physical shell mirror.

At \(\lambda_c=1\), the discrete map is nonzero, square-zero and defective: corridor \(J_2(0)\oplus J_1(0)\), full map two such copies. This allowed boundary exceptional point has no finite matrix logarithm; normalized evolution fails after annihilation. It is not a finite-generator exceptional point.

With ordinary source Hilbert metric and eigenray order \((a,a\omega,a\omega^2)\), the recorded Bargmann product is \(0.01910142260+0.03964523780i\), argument \(+1.12180733627\) radians. Independent ray phases cancel; reversing order or conjugating reverses its argument. General nonunitary similarity does not preserve it. Paper C contains no such Bargmann invariant. A constructed parameter-dependent Berry loop is a separate comparison, not recovered lineage.

## 6. Connections retained without stronger identifications

Sources: [B5–B19](../physics_kernel/BRIDGE_IV_A_CODEX_ADVERSARIAL_REVIEW_v0.1.md#b5-srg-corridor-triplet--su3).

| Retained result | Boundary |
|---|---|
| Gell-Mann expansion of \(p,L_3\); Pauli \(B\in SU(2)\); carrier \((V,W)\mapsto V\otimes W\) | Exact algebra/representation. Neither full dynamical gauge invariance nor color/flavor/weak-isospin assignment follows. |
| \(3\otimes\bar3=1\oplus8\), \(3^{\otimes3}=10\oplus8\oplus8\oplus1\) | The fundamental balanced vector is not an SU(3) singlet. Color and flavor assignments are different. |
| \(M=M_0+\alpha Y+\beta[I(I+1)-Y^2/4]\) gives \(2M_N+2M_\Xi-3M_\Lambda-M_\Sigma=0\) | Conditional GMO relation; an unrestricted mass operator need not obey it. |
| Untilted orthonormal TM2 columns in B16 | Exact unitary family given the mass/flavor basis identification; \(J_{\rm CP}=-\sin2\varphi\sin\delta/(6\sqrt3)\) in the printed ordering. No fixed CP phase or octant selected; the separate tilted construction fails unitarity. |
| Standard E8 branching \(248=(8,1)\oplus(1,78)\oplus(3,27)\oplus(\bar3,\overline{27})\) | Lie-algebra statement; group image involves a common \(\mathbb Z_3\) quotient. The printed root/Coxeter appendix, claimed single 24-point order-three orbit and unsigned height lift fail B14's specific checks. No universal no-map theorem follows. |
| Periodic toroidal operators and conditional field/dispersion comparisons | Structural connections; no physical finite-\(m\), universal \(m=12\), confinement or calibrated plasma law derived. Pure-diffusion/Nyquist conclusions apply to the specified scheme. |
| \(Z_{\rm chiral}\) and \(J_{\rm eff}\) transformation laws | Accepted coefficient-space mathematics; neither physical CP nor magnetic helicity is identified. |

The later IVB E8 map class/proof is PENDING because its actual note was not found. No conclusion about all equivariant E8 maps, or about ten radial copies / \(3\times8\times10\) labels, is admitted. No omitted IVB result is declared lost or refuted.

## 7. Change log from v0.1 and open items

1. Separate scientific acceptance, digest review, local save, commit/remote receipt and implementation.
2. Restrict the February Three-Way rejection to its actual ODE and restore the May reciprocal source.
3. Supply parameter domains, exact shared-subspace typing, factor order and the full product's failure to preserve the core.
4. Restore raw zero attraction, fixed projective rays, periodic exceptions and at-most-three-circle generic closure.
5. Correct generator sign; state frozen versus family PT scope and the discrete endpoint limitation.
6. Remove Paper-C Bargmann attribution; fix metric, eigenray order and Berry-loop provenance.
7. Preserve GMO/TM2/representation results while qualifying their assumptions; restrict E8 failures to inspected constructions.
8. Replace v0.1's simultaneous three-target reopening with Q0–Q5: Paper B drafting, then one saved Target B verification packet. IVB A/C remain parked.

PENDING: physical density/scales, the actual IVB proof package, a precise evolution/reduction/boundary handoff, physical assignments and the independent continuity review. No new theorem, scientific rerun, source edit, commit, upload or kernel change occurred.
