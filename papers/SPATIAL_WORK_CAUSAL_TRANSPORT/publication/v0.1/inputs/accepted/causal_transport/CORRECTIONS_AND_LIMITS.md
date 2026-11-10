# Corrections and retained limits

Codex independent review, 10 November 2026.

**T01-T07 in the analytical start are verified as stated at their assumptions.** No candidate force, boundary law, state metric, parameter, preparation or theorem has been replaced. The review is returned for GPT/author assessment; their acceptance or physical-model adoption is not claimed.

## D01: inactivity is not equivalent to empty added states

**Target:** Work order, T06: “Zero new activity also requires empty new states.”

**Correction:** At κ=0, the old RX system decouples for arbitrary added-state preparation. The added subsystem may still evolve from its own stock. Empty added states are sufficient for inactivity, but they are not necessary.

**Counterexample:** Let n be a unit normal to the planar selected carrier, choose nonzero h in L2(G), and prepare ζ0(X)=(0,h(X)n), with both line profiles zero and κ=0. Every carrier tangent is perpendicular to n, so C*ζ0=0 and CC*ζ0=0. All four boundary signals and both traveling fields remain zero, while ζ(t)=ζ0 is constant with positive receiving stock. There is no added exchange or evolution despite nonempty receiving preparation. The old RX preparation can be arbitrary because it is decoupled.

**Impact:** Analytical-start section 8 already gives the correct sufficient statement, “If its states start empty, they remain empty.” The input claim ledger also correctly distinguishes decoupling from possible activity of prepared states. T06 is verified as stated in those controlling mathematical claims. D01 corrects only the work-order necessity wording; no alternate candidate is introduced. The proof is in R6.2, with the kernel calculation in R1/E01.

## Required limits of the verified claims

1. **Fixed geometry and metrics.** The actual broken G arcs, common width, full reflected hand and positive finite delay bounds remain fixed. G is not filled into an aperture. The product arclength measure and the new quadratic metrics are explicit proposals, not inherited physical area or material energy density. Ball radius and cylindrical radius remain distinct.
2. **Spatial adjoint, not temporal feedback.** J is an isometric duplication; C is bounded but need not be contractive or invertible. The vector Gram block has null directions. The far coupling uses same-time C*, not W's advanced finite-window temporal adjoint.
3. **Legitimate transport traces.** Arbitrary L2 initial line profiles yield locally L2 time traces by characteristics/Fubini. They need not have fixed-time boundary values or satisfy classical corner compatibility. No derivative of a static delay or geometric aperture flow is supplied by the channel calculation.
4. **Forward mild theorem.** Global forward existence, uniqueness, energy-space continuity, x/z C1 regularity, ζ local absolute continuity and finite-horizon continuous dependence are proved for fixed parameters and positive minimum delay. The proof establishes local component work before using total conservation. It does not prove global H1 regularity, a backward flow, a zero-delay limit or bounds uniform over unbounded parameter families.
5. **Correct C6 history domains.** Arbitrary forward-profile preparation contributes the positive startup term +sqrt(2) C c_init. Zero extension in the algebraic decomposition does not infer a physical past. The complete-history formula additionally requires the negative-time near boundary law and a compatible initial forward profile. Histories supplied for an identity are not automatically past solutions of the full model.
6. **Loaded response and storage.** C6 is exactly the direct term, with coefficient 2κ in the ζ equation. The complete drive also has delayed return, loading and possibly startup terms. Positive line energy is not W's signed prehistory pairing relabeled as a stock. Old H_R and new H_G are separate stores; old H_R is not counted twice. H_G can decrease by sending energy back into the channels.
7. **Native updates.** The original tuple, zero convention and F-first/exchange-second order are retained. Only x jumps; post-jump endpoints count t_a<t_j<=t_b. Every finite iterate exists, but no uniform infinite-step bound or continuity at singular native prestages is inferred. For κ>0 the trajectories change, so old receiving, credit, capacity and convergence results need their hypotheses checked before reuse.
8. **Scoped activity witness.** Empty added states give zero receiving through θ-minus and zero incoming b before 2θ-minus. Launching through -κ²Q starts immediately. The strict activity witness starts with constant positive carrier preload, x0=z0=0 and empty added states. It is carrier-funded; x stays zero. It proves neither native empty-launch supply/recovery nor a capacity fraction or all-six simultaneous receiving.
9. **Incoming return is a distinct statement.** Nonzero b on the specified interval follows from the positive-measure delay sublevel set and the explicit ε bound. This does not establish nonzero projection J*b, positive net carrier work or native credit. General boundary statements are a.e. in time; no exact-onset point trace is required.
10. **Physical correspondence remains open.** The delay coordinate is time/age on an abstract channel, not the intended toroidal route. A physical detour at the same speed changes travel time relative to endpoint distance. Any embedding must justify route lengths, overlap/multiplicity, material interfaces, state densities, units and speed. No material G receiver, aperture normal, tube thickness, diversion fraction or calibrated clock has been adopted.

Accepted W01-W05, central-route Q01, six-opening separation and cadence/receiving qualifications are retained as inputs. No earlier investigation or publication was reopened. The current mathematical assessment closes without an author geometry decision. The intended W-plus-candidate paper and any physical attachment remain later work.
