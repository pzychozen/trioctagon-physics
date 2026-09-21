# Unresolved assumptions at the first geometry-to-state interface

Scope: the exact local Paper-C shell and the existing abstract Paper-A map only. This is a companion to `TOP_TO_RECURSIVE_BRIDGE_DERIVATION.md`, not an instruction to implement a model. Later complex doubling and recursion are deferred.

## What has been established

**EXACT.** The three faces carry a real permutation representation with a balanced line and a transverse plane. The actual unweighted face-sharing Laplacian is the current kernel's \(L_3=-3P_\perp\). This fixes neither a physical coupling strength nor a time scale.

**EXACT.** With an orientation, the transverse plane is one complex line. It leaves the balanced real line unpaired. It cannot turn the original real three-channel space into three complex dimensions.

**EXACT.** The direct sum of the three oriented face-center tangent planes is isometric to \(\mathbb C^3\). The construction uses outward-normal cross products, and the cyclic rotation permutes its coefficients. Spatial mirrors act conjugate-linearly. This is a geometric vector space, not yet a selected dynamical state.

## Missing premises

All entries in the following table are **UNRESOLVED**. The listed alternatives are **CANDIDATE_INTERPRETATION**, not equivalent models or selected implementations.

| Interface question | Why it matters | Specific missing input |
|---|---|---|
| What is measured on each face? | A face label supplies a channel, not a value or physical observable. | A tangent vector, a specified field integral, an oscillator coordinate, or another explicitly defined observable. |
| Where is its second real quadrature? | Three real coefficients cannot have a global complex structure. | A second observable, oriented tangent-vector component, or demonstrated two-dimensional mode eigenspace. |
| Why is the tangent-plane candidate physically relevant? | Euclidean planes do provide a kinematic complex structure. Their rotation need not be a temporal phase. | A field or transformation whose real state is these vectors, with units and an extraction map. |
| What generates phase? | Finite C3 rotations are not continuous time evolution. | A specified reversible real-linear orthogonal phase action, or a sufficiently justified dynamical generator. |
| What fixes the sign and scale of phase? | Geometry supplies no period or time unit; reflections reverse oriented-plane complex structure. | Orientation convention and, when relating unequal physical units, a frequency or scale. |
| How do seams couple fields? | Welded geometry alone does not choose scalar continuity, vector transport, or an interface law. | State type and trace/transport conditions derived for that type. |
| Which three modes are retained? | Three labels do not prove there are exactly three relevant physical modes. | An operator and a justified finite-dimensional restriction, without inventing host or rim conditions. |
| Which symmetry action should the state obey? | Scalar face permutations and spatial tangent vectors differ under mirrors. | The observable's transformation law; whether parameters such as k are also transformed. |
| What relates this state to the frozen nonlinear rule? | An isomorphism with C³ does not derive the amplitude nonlinearity or harmonic three. | An independently justified interface to the already defined map, retaining its stated domain and zero convention. |

## Two constraints an independent derivation should try to break

**DERIVED_FROM_STATED_ASSUMPTION — perimeter test.** Give each perimeter one scalar Fourier harmonic of the same order and require equality along the entire welded seam. The odd cycle of opposite-edge matches leaves exactly one real coefficient, not three phase planes. To evade this result, an alternative must identify the changed premise explicitly: field type, harmonic content, continuity law, or mode space. No such change is made here.

**CONTRADICTED — weak phase-plane inference.** Invariant phase planes spanning a space do not imply that every vector belongs to an invariant phase plane of the same generator. \(K=\operatorname{diag}(J_2,2J_2)\) is a counterexample. To use the strong version of the secondary source's §13 argument, prove its universal-vector hypothesis, or explicitly use a different construction such as polar normalization of an already supplied invertible skew generator.

## Concrete mathematical handoff for independent review

The results below are respectively **EXACT**, **DERIVED_FROM_STATED_ASSUMPTION**, and **UNRESOLVED**, as indicated; no novelty claim is made.

1. **EXACT:** Verify the three-face representation and \(L_3=-3P_\perp\), and distinguish its single transverse phase plane from three independent complex channels.
2. **EXACT:** Verify \(J_i=n_i\times\) on each face-center tangent plane, including the conjugate-linear mirror actions. Decide whether the claimed geometry-to-complex-space construction uses any hidden orientation or observable choice beyond those stated.
3. **DERIVED_FROM_STATED_ASSUMPTION:** Independently derive the opposite-edge Fourier trace constraints and the one-dimensional matching subspace. Test the scope, not merely the rank calculation.
4. **DERIVED_FROM_STATED_ASSUMPTION:** Check the sufficient phase-generator theorem using every vector's membership in a nontrivial invariant two-plane. Separate the supplied generator from a structure allegedly selected by geometry.
5. **UNRESOLVED:** Identify a real observable and independent phase transformation before calling any of these geometric spaces the kernel's dynamical state. No requirement to recover C³ should be used as evidence that the chosen observable exists.

This work stops at the conditional first bridge. It supplies no upper/lower complex doubling, no global domain, no physical boundary conditions at the rims, no recursive handoff object, and no SRG dependency map. Those questions remain deferred by the revised work order.
