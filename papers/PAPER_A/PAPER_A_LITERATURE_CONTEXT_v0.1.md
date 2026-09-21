# Paper A — Literature Context v0.1
### Standard machinery vs model-specific contribution
Focused literature-context review of `PAPER_A_CYCLE_COVERING_DYNAMICS_DRAFT_v0.3.md` (mathematics frozen). **No proof was modified, no simulation rerun, no model redesigned, no new mathematics introduced, no manuscript edited.** Purpose: locate each component within established theory and classify it conservatively.

**Classification vocabulary (as instructed):** `STANDARD` · `STANDARD_SPECIALIZATION` · `CLOSE_PRECEDENT` · `MODEL_SPECIFIC` · `NO_CLOSE_PRECEDENT_LOCATED` · `NOVELTY_UNRESOLVED`. The word `NOVEL` is **never** used on the basis of a search finding nothing. References by tag are in `PAPER_A_REFERENCE_LEDGER_v0.1.md`.

**Search scope.** Targeted web search (Sep 2026) across the families named in the work order: coupled-cell synchrony, graph fibrations/coverings, equitable partitions & quotient Laplacian, discrete-time network synchrony, cluster synchronization & master stability, symmetry/representation (IRR) decomposition, covering-graph spectra, higher-harmonic phase coupling, transverse/blowout bifurcation, coupled map lattices, feedback-preserving synchrony. This is not an exhaustive survey.

---

## 1. Headline finding

**Essentially all of Paper A's mathematical *machinery* is standard theory or a direct specialization of it.** The cycle-Laplacian pull-back, the $C_{12}\to C_3$ quotient, the invariant sector $V_3$, the Fourier/deck spectral decomposition, the nonlinear reduction $F_M\circ P=P\circ F_3$, the deck-character block-diagonalization of the transverse Jacobian, and the transverse-Floquet stability method are all recognizable, named constructions in the coupled-cell-network / graph-fibration / equitable-partition / cluster-synchronization / master-stability literatures.

**The model-specific content is the *instance*, not the *machinery*:** (i) the particular map — a complex Mexican-hat amplitude nonlinearity plus cycle-Laplacian coupling plus a separate harmonic-3 phase-synchronization step; (ii) the explicit, deck-resolved **transverse-stability atlas** of that specific map (its stable/unstable fixed and periodic regimes, the crossing $g_\ast=0.4220744\ldots$, the specific Floquet values); and (iii) the RSB shared-sector observation. For these, **no close precedent was located** — but that is expected for any specific model and is recorded as `NOVELTY_UNRESOLVED`, never as a novelty claim.

**Recommended positioning: CONSERVATIVE** (§4). Treat the covering/quotient/synchrony reduction as established background; foreground the specific model and its worked deck-resolved transverse atlas as the contribution.

## 2. Terminology crosswalk for $C_{12}\to C_3$

In the special setting of a **regular cover of an (undirected) cycle**, four literatures describe the same object; they coincide here and Paper A may cite any, but should acknowledge the equivalence:

| Description | Literature | Statement for $C_{12}\to C_3$ |
|---|---|---|
| **Graph covering** (4-sheeted, regular; deck group $\mathbb Z_4$) | topological/algebraic graph theory; [GR01] | Paper A's primary term. Correct. |
| **Graph fibration** (surjective; bijective on in-/out-neighbourhoods) | [BV02], [DL15], [NRS16], [GFBC24] | For an undirected cycle in$=$out, so covering $=$ fibration here. The residue map is a fibration. |
| **Balanced coloring / synchrony-subspace quotient** | [SGP03], [GST05], [GS06] | The fibre partition $\{r,r{+}3,r{+}6,r{+}9\}$ is a **balanced equivalence relation**; $C_3$ is its quotient network; $V_3$ is the synchrony subspace. |
| **Equitable partition / quotient (divisor) matrix** | [GR01], [OYSB13], [Schaub16] | The residue partition is **equitable**; the quotient matrix is $\Delta_3=L_3$; $Q^\ast\Delta_{12}Q=\Delta_3$ is the quotient-matrix identity. |

**Recommendation:** state once that these are the same object here (covering $\equiv$ surjective fibration $\equiv$ balanced-coloring quotient $\equiv$ equitable-partition quotient for regular cycle covers), and cite [GFBC24] (which synthesizes groupoids/fibrations/balanced colorings) plus [GR01] (equitable partition). This *strengthens* the paper by placing it correctly, at no cost to the frozen mathematics.

## 3. Component-by-component classification (§14 table)

| Paper A component | Closest literature concept | Best references | Classification | What remains specific here |
|---|---|---|---|---|
| $\Delta_M P=P\Delta_d$ ($d\mid M$); $Q^\ast\Delta_M Q=\Delta_d$ | equitable-partition / quotient-(divisor)-matrix identity; covering-graph pullback | [GR01], [OYSB13] | **STANDARD** (at most `STANDARD_SPECIALIZATION` to cycles) | only the explicit cycle-graph form and the exact integer identity $P^\ast\Delta_MP=q\Delta_d$ |
| quotient/covering $C_M\to C_3$ (deck $\mathbb Z_4$) | graph covering ≡ fibration ≡ balanced quotient | [BV02],[DL15],[GS06],[GFBC24] | **STANDARD** | the specific 4-sheeted cycle cover; nothing conceptually new |
| $V_3$ synchrony/pull-back sector | polydiagonal / synchrony subspace; balanced-coloring invariance | [SGP03],[GST05] | **STANDARD** | that this particular balanced partition of $C_{12}$ yields $L_3$ |
| Fourier/deck decomposition; $e_0,e_4,e_8$; inherited spectrum | covering-graph / lift spectra decomposing over deck-group characters | [GR01], lift-spectra lit. | **STANDARD** | the explicit $\{0,-3,-3\}$ / radical complement for $C_{12}$ |
| nonlinear $F_M\circ P=P\circ F_3$ | fibration ⇒ conjugacy of network dynamics; synchrony-subspace restriction of admissible maps | [DL15] ("dynamics are conjugate"), [SGP03], [Field04] | **STANDARD_SPECIALIZATION** (subsumed by the general fibration/balanced-quotient semiconjugacy) | verifying the harmonic-3 neighbour coupling is admissible & that $\{n{-}1,n{+}1\}\!\mapsto\!\mathbb Z_3\setminus\{n\}$ — routine, model-specific |
| all-$3\mid M$ extension | every $C_{3q}\to C_3$ is a (fibration) covering; tower of covers | [BV02],[GR01] | **STANDARD_SPECIALIZATION** | writing it out explicitly for this coupling; `NO_CLOSE_PRECEDENT_LOCATED` for this exact map's all-$3q$ statement |
| deck blocks $U_0\oplus U_2\oplus U_{13}$ (transverse) | symmetry-adapted / IRR block-diagonalization of the cluster-sync variational equation | [Pecora14],[Sorrentino16],[PC98] | **STANDARD** (abelian $\mathbb Z_4$ ⇒ characters) | the explicit real-character pairing $U_{13}$ for this ring |
| Floquet transverse-stability *method* | master-stability / cluster-sync transverse Floquet multipliers | [PC98],[Pecora14],[Sorrentino16],[ABS96] | **STANDARD** (method) | — |
| the transverse-stability **atlas** (regimes, $g_\ast$, Floquet values) | (specific-model computation) | — | **MODEL_SPECIFIC** / `NO_CLOSE_PRECEDENT_LOCATED` | the entire atlas of *this* map; `NOVELTY_UNRESOLVED` |
| direct perturbation confirmation | numerical transverse-perturbation verification of synchrony stability | [ABS96],[Schaub16] | **STANDARD** (method) | the specific measured rates for this map |
| RSB shared $L_3$ sector | two $\Delta_{12}$-based operators sharing the equitable-partition sector | [GR01] (same argument) | **STANDARD** (underlying fact) + **MODEL_SPECIFIC** (this pair) | the observation that these two specific operators coincide on $V_3$ |
| feedback compatibility (Corollary 3, $k$-only) | coupling respecting the balanced partition preserves the synchrony subspace; adaptive/state-dependent cluster sync | [Schaub16],[Sorrentino16] | **CLOSE_PRECEDENT** / `STANDARD_SPECIALIZATION` | the explicit $k$-only sufficient pull-back condition |
| $g_\ast$ crossing terminology | transverse multiplier crossing $-1$ (period-doubling-type transverse instability); blowout/bubbling family | [ABS96],[ABS94],[OS94] | **STANDARD** terminology available | whether to *call* it a transverse $-1$ crossing (yes) vs blowout (only if chaotic base) |

## 4. Answers to the work order's specific questions

**§2 — how does $V_3=\{x_n=x_{n+3}\}$ fit synchrony/polydiagonal theory?** Exactly: it is the **polydiagonal (synchrony subspace)** of the **balanced/equitable partition** of $C_{12}$ into residues mod 3. Its invariance under all admissible dynamics is the balanced-coloring theorem [SGP03]. `ESTABLISHED`.

**§3 — is $C_M\to C_3$ a covering, fibration, balanced quotient, or equitable-partition quotient?** All four, equivalently, in this regular-cycle setting (§2 crosswalk). The most general framing is *graph fibration* [BV02]/[DL15]; the most computational is *equitable partition / quotient matrix* [GR01]; the most dynamics-native is *balanced coloring / synchrony subspace* [SGP03]. `GRAPH_FIBRATION_CONNECTION = ESTABLISHED`.

**§4 — how standard is $\Delta_M P=P\Delta_d$?** It is the equitable-partition **quotient-matrix identity** (textbook, [GR01]) and simultaneously the covering-graph pullback. **Theorem 1 should not be presented as original**; it is a direct standard specialization. (Paper A already labels §§3–5 "elementary and self-contained," which is consistent; the addition is naming the standard results.)

**§5 — is the exact restriction of a nonlinear *map* under a fibration already covered by a general theorem?** Yes. The balanced/fibration framework is stated for admissible **maps** as well as flows: a balanced partition's polydiagonal is invariant under *all* admissible maps, and a fibration induces a **semiconjugacy** of the network dynamics ([DL15]: "the original network and its quotients are related by graph fibrations and hence their dynamics are conjugate"; [Field04] for the explicitly discrete-time combinatorial-dynamics setting). Paper A's $F_M\circ P=P\circ F_3$ is a concrete instance. Where the continuous-time statements dominate a source, the balanced-invariance argument transfers verbatim to maps (no derivative or flow is used). `NONLINEAR_REDUCTION_SUBSUMED_BY_GENERAL_THEORY = YES`.

**§6 — is Proposition 2 a direct instance, a specialization needing the harmonic-3 form, or model-specific?** A **specialization**: the reduction is subsumed by the general fibration/balanced-quotient semiconjugacy; the model-specific ingredient is only the verification that the harmonic-3 neighbour term is admissible and that the ring's residue map is a fibration (the $\{n{-}1,n{+}1\}\mapsto\mathbb Z_3\setminus\{n\bmod3\}$ property is exactly the local-bijectivity/balance condition). That property is elementary and not itself a new theorem.

**§7 — is the transverse decomposition / Floquet analysis standard?** Yes on all three sub-questions: tangential+transverse invariant splitting is standard (master stability [PC98]); using representation/deck characters to block-diagonalize the normal dynamics is the **IRR method** of [Pecora14]/[Sorrentino16] (Paper A's abelian $\mathbb Z_4$ characters are its simplest case); periodic-orbit transverse **Floquet** multipliers for cluster states are standard [Sorrentino16],[ABS96]. `TRANSVERSE_DECOMPOSITION_STANDARD = YES`, `FLOQUET_CLUSTER_STABILITY_PRECEDENT = YES`. Model-specific: the numeric atlas.

**§8 — symmetry/representation decomposition.** The $U_0,U_2,U_{13}$ isotypic split is standard symmetry-adapted decomposition [Pecora14],[Sorrentino16]; do **not** oversell it.

**§9 — covering-graph spectral facts $e_0,e_4,e_8$.** Standard lift/quotient spectra ([GR01]; lift-spectra literature). `STANDARD`.

**§10 — closest dynamical neighbour of the full map.** The genre is a **complex coupled map lattice with cluster states**; the nearest cited genre is Kaneko's coupled map lattices [Kaneko90] (discrete-time cluster states) and Stuart–Landau/Ginzburg–Landau ring models, but with real logistic maps or continuous-time amplitude equations rather than Paper A's discrete complex Mexican-hat *plus a separate* harmonic-3 phase step. **No near-identical model was located.** `CLOSE_PRECEDENT_FOR_FULL_MODEL_FOUND = NO`; `NOVELTY_UNRESOLVED`.

**§11 — harmonic-3 phase coupling.** Higher-harmonic phase coupling $\sin(m\Delta\phi)$ supporting $m$-cluster states is established ([HMM93] second harmonic; general higher-harmonic Kuramoto literature). $m=3$ naturally supports three-cluster states. Paper A's $\sin 3(\phi_i-\phi_j)$ is **not novel** as a coupling. `HARMONIC_3_COUPLING_STANDARD = YES`. Describe it as standard higher-harmonic phase coupling.

**§12 — transverse-bifurcation terminology for $g_\ast$.** Best described plainly as a **transverse multiplier crossing $-1$** (a transverse period-doubling-type instability of the synchrony sector). "Blowout bifurcation" [OS94] and "bubbling/riddling" [ABS94] are specific to a **chaotic** base state losing transverse stability, which Paper A does not claim; do **not** relabel $g_\ast$ as a blowout. The available standard term ("loss of transverse stability" / "transverse $-1$ crossing") already fits; no manuscript change is required, and the existing wording ("transverse $-1$ eigenvalue crossing") is correct.

**§13 — feedback-preserving synchrony.** Corollary 3's $k$-only sufficient condition is a **specialization** of the principle that coupling respecting the balanced partition preserves the synchrony subspace (implicit in [SGP03],[Schaub16]); adaptive/state-dependent cluster synchronization is an active area. It is essentially a routine compatibility statement; **no stronger general theorem is needed to make it correct**, and none more specific than the balanced-invariance principle was located. `CLOSE_PRECEDENT`.

## 5. What is genuinely model-specific (the contribution surface)

1. **The specific map** — discrete complex state $\Omega\in\mathbb C^M$, Mexican-hat amplitude $\varepsilon\Omega(k-|\Omega|^2)$, cycle-Laplacian coupling $g\Delta_M\Omega$, and a *separate* harmonic-3 phase-synchronization operator with three-periodic $k$. The *combination* was not located as a studied model. `MODEL_SPECIFIC`, `NOVELTY_UNRESOLVED`.
2. **The explicit deck-resolved transverse-stability atlas** — the specific stable/unstable fixed and periodic regimes, the crossing $g_\ast=0.4220744431784353$, the specific normal Floquet values, and the direct-perturbation confirmation. These are computations *of this map*; `NO_CLOSE_PRECEDENT_LOCATED`.
3. **The all-$3\mid M$ explicit reduction for this coupling** and the **RSB shared-$L_3$-sector** observation — routine given the general theory, but written out for these operators; `MODEL_SPECIFIC`.

None of these justifies a novelty claim: they are what a specific worked example naturally contributes.

## 6. Verdict

```
PAPER_A_LITERATURE_CONTEXT = COMPLETE   (focused pass; not an exhaustive survey)

COVERING_PULLBACK_STANDARD = YES
EQUITABLE_PARTITION_CONNECTION = ESTABLISHED
COUPLED_CELL_SYNCHRONY_CONNECTION = ESTABLISHED
GRAPH_FIBRATION_CONNECTION = ESTABLISHED

NONLINEAR_REDUCTION_SUBSUMED_BY_GENERAL_THEORY = YES
HARMONIC_3_COUPLING_STANDARD = YES
TRANSVERSE_DECOMPOSITION_STANDARD = YES
FLOQUET_CLUSTER_STABILITY_PRECEDENT = YES

CLOSE_PRECEDENT_FOR_FULL_MODEL_FOUND = NO
CLOSE_PRECEDENT_FOR_ALL_3Q_REDUCTION_FOUND = NO
CLOSE_PRECEDENT_FOR_THIS_STABILITY_ATLAS_FOUND = NO

MODEL_SPECIFIC_CONTRIBUTION_IDENTIFIED = YES
NOVELTY_CLAIM_JUSTIFIED = NO
NOVELTY_REMAINS_UNRESOLVED = YES

RECOMMENDED_POSITIONING = CONSERVATIVE

MATHEMATICS_CHANGED = NO
MANUSCRIPT_CHANGED = NO

READY_FOR_REFERENCED_MANUSCRIPT_v0_4 = YES
```

The three `CLOSE_PRECEDENT_… = NO` entries mean *no near-identical precedent for this specific model/atlas was located in a focused search* — they are **not** novelty claims (`NOVELTY_CLAIM_JUSTIFIED = NO`, `NOVELTY_REMAINS_UNRESOLVED = YES`). The machinery is standard; the instance is specific. A referenced v0.4 can proceed by adding the citations above as background and framing the contribution conservatively (see `PAPER_A_POSITIONING_NOTE_v0.1.md`).
