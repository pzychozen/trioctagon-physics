# GPT review — causal transport and storage

**Task:** `NATIVE_CAUSAL_TRANSPORT_STORAGE_01`  
**Review date:** 10 November 2026, Atlantic/Reykjavik  
**Disposition:** **T01–T07 accepted as stated at their specified assumptions, with documentary clarification D01 adopted. No candidate equation or mathematical theorem requires correction.**

This accepts the mathematical assessment of one explicitly declared causal extension. It does not adopt a physical route, material receiving mechanism, aperture flux or calibrated clock. Manuscript preparation can proceed on the accepted mathematical scope; manuscript acceptance and publication are later stages.

## 1. Controlling submission and evidence

The controlling submission is `NATIVE_CAUSAL_TRANSPORT_STORAGE_01_REVIEW.zip`, 2,899,213 bytes, SHA-256:

`7dedee300067374e95866286a6c45878de3083421e692d8e1bcf322d309ab8df`

Its proof review has SHA-256:

`1d88714a424c6e559a8087ac22de2ee80e492aac7a8ed9227712a5885a80cd6a`

The [submitted proof](submitted/NATIVE_CAUSAL_TRANSPORT_STORAGE_01_PROOF_REVIEW.md), [claim ledger](submitted/CLAIM_LEDGER.json), and [corrections and limits](submitted/CORRECTIONS_AND_LIMITS.md) are preserved unchanged. The original submitted archive and checksum are under `submitted_archive/`. The original GPT analytical start and work order retain their historical proposed status and wording inside the preserved inputs; the present disposition and D01 control their onward use.

GPT read the proof and relevant original equations, inspected the exact-check code and execution records, and commissioned complementary functional-analysis, activity/accounting and manuscript-scope subreviews. Those notes are retained under `verification/`. They are project-internal mathematical scrutiny, not external peer review or separate Windows test executions.

| Current-submission check | Result |
| --- | --- |
| Uploaded archive versus supplied checksum | Exact match; CRC check passed. |
| Archive contents | All 90 members reopened; all 89 self-excluded manifest entries matched lengths and SHA-256. |
| Standalone proof and result summary | Exact matches to the archive members. |
| Returned original GPT packet | Exact match to the issued 1,419,744-byte packet, SHA-256 `2ec94a53c4624d6bc429ff4c64807f4ea559dcd95e4563b8b939bf6efd1af515`. |
| Preserved original packet | All 63 members match their returned `inputs/` copies; all 62 original manifest entries match. |
| Registered source identities | All 46 match; all 28 recorded Git-blob identities also match. |
| Source and proof crosswalk | All 61 source locators match hashes and recorded lines; all seven claim proof hashes match. |
| Accepted W archive binding | Checksum matches the retained acceptance archive. |
| Submitted execution evidence | Five exact-algebra groups E01–E05 pass; validator and check subprocesses exited zero with empty stderr. |

The measured Windows record reports Command Prompt, conda `torment`, Python 3.11.15 and SymPy 1.14.0. GPT inspected those scientific scripts and logs; it did **not** rerun them. The new GPT execution verifies bytes, locators and evidence links. Infinite-dimensional evolution and positive-measure activity are justified by written proofs, not inferred from the five symbolic groups. Prior publications were not re-audited. See [integrity and scope checks](verification/GPT_INTEGRITY_AND_SCOPE_CHECKS.json).

## 2. T01 — exact bounded spatial factorization

**Accepted as stated.** The declared product arclength spaces give `J*J=I` with the stated `1/sqrt(M)` normalization. Cauchy–Schwarz and Fubini justify C and its same-time spatial adjoint. The `sqrt(M)` factors cancel exactly in `C D_theta J`, recovering C6. Time translation is taken at each channel label and then integrated, so arbitrary L2 histories are not evaluated through an unsupported single-time trace. [Submitted proof R1]

The Gram operator is bounded and nonnegative. Its scalar block has a positive lower bound for the fixed geometry; its vector block has the carrier-plane normal in its kernel. No inverse and no contraction condition on C is needed. The energy matching later uses C paired with C*, rather than assuming that C alone is a normalized scattering map.

## 3. T02 — causal transport, time traces and nonnegative stock

**Accepted as stated.** Both characteristic orientations match the forward and backward transport equations. The initial-profile terms and delayed boundary terms occupy disjoint time ranges per channel. Translation and Fubini provide legitimate locally L2 time traces, with no extra factor two and no prescribed instantaneous trace for a general L2 profile. [R2.1]

Zero extension, translation and restriction prove strong continuity of the evolving transport state; fixed fiber reflection handles the backward field. Direct integration of squared characteristic profiles gives the exact integrated balance

\[
E_{\rm tr}(T)-E_{\rm tr}(0)=\int_0^T(P_N-P_G)\,dt.
\]

This is valid with arbitrary finite-energy preparation and incompatible classical boundary corners. It uses no unsupported integration by parts and no derivative of the static delay field. The stock is nonnegative in the declared mathematical metric. Its channel coordinate is time/age, not a constructed ambient arclength. [R2.2–R2.3]

## 4. T03 — closed coupling and exact augmented work

**Accepted as stated.** The original native feedback factor one-half is retained, so the degree-two identity `J_f x=2f` supplies the original native power. The existing carrier/old-receiver cancellation is unchanged except for the explicitly added carrier force. [R3.1]

The near and far boundary laws give

\[
\dot H_{\rm RX}=-P_N,\qquad \dot H_G=P_G,
\qquad H_{\rm total}=H_{\rm RX}+E_{\rm tr}+H_G.
\]

Together with the transport balance, this makes `H_total` constant during exchange. Old receiver z is counted once in `H_RX`; the new receiving field ζ has its own stock. The damping-looking terms have explicit traveling-state counterparts. `H_G` need not increase monotonically and can release its prepared energy into the return channel. The proposed abstract dimensions are consistent, without selecting physical calibration. R4 supplies the regularity and integrated work justification for these identities. [R3.2–R3.3]

## 5. T04 — global forward mild evolution

**Accepted as stated.** A positive minimum delay makes both incoming traces known from the initial profiles or previous time slabs. The original polynomial subsystem with bounded damping and known locally L2 forcing has a local mild solution; the new receiving field solves a bounded-generator Hilbert-space ODE. [R4.1–R4.2]

The proof does not assume total conservation to obtain global existence. The inverse free-carrier group makes the carrier interaction variable absolutely continuous, allowing a legitimate norm chain rule for L2 preparation. Original reciprocal cancellation gives the local RX inequality

\[
H_{\rm RX}(t)-H_{\rm RX}(r)
\le\tfrac12\int_r^t\|b(v)\|_V^2\,dv.
\]

That known finite input bound controls all RX coordinates on the slab. The bounded nonlinear term and integrable forcing give a limit at any hypothetical finite maximal endpoint, allowing restart. Only after this continuation are the outgoing laws, transport work and receiving work combined into total conservation. Induction completes every finite forward horizon. [R4.3]

Uniqueness and finite-horizon continuous dependence follow from the same slab construction and characteristic estimates for differences. The accepted solution is continuous in the energy space; x and old z are C1 during exchange; ζ is locally absolutely continuous, indeed H1 in time on finite exchange windows; boundary signals are generally locally L2 in time. This is a fixed-geometry, fixed-parameter forward theorem with positive minimum delay. It asserts no global H1 regularity, backward flow, uniform zero-delay limit or uniform unbounded-parameter estimate. [R4.4]

## 6. T05 — C6 as the direct component, including preparation and return

**Accepted as stated.** The exact initial-value identity is

\[
\beta_G\dot\zeta
=2\kappa\mathcal K_{G,0}Q-\sqrt2 C D_\theta^+b
+\sqrt2 Cc_{\rm init}-CC^*\zeta.
\]

The direct coefficient is `2κ`; the startup contribution has a plus sign. Zero extension in this decomposition does not assert a physical zero past. Independent forward profiles carry the preparation represented by `c_init`. [R5.1]

The complete-history version follows only with the stated negative-time near law and compatible initial forward profile. A supplied Q history by itself is insufficient; no backward evolution theorem is being used. After the maximum delay, the startup term disappears and the delayed arguments are nonnegative. [R5.2]

The new same-time C* is distinct from W's advanced finite-window temporal adjoint `K_G*`. The causal extension does not contradict or make that temporal adjoint causal. Bare C6 is not generally the entire loaded drive or the receiving field. Likewise, nonnegative `E_tr(0)` is a quadratic new-state preparation, not W's signed bilinear prehistory pairing under a new name.

## 7. T06 and D01 — native steps, decoupling and stationary preparation

**T06 accepted as stated. D01 adopted.** The original native tuple, simultaneous prestage, zero convention and F-first/exchange-second order are retained. Only x jumps. With post-jump endpoints, the correct finite-window account is

\[
H_{\rm total}(t_b)-H_{\rm total}(t_a)
=\sum_{t_a<t_j\le t_b}\frac{\alpha_N}{2}
\bigl[I(F_{\rm native}\Omega(t_j^-))-I(\Omega(t_j^-))\bigr]
=B_N.
\]

Every finite iterate exists; no uniform infinite-step bound or continuity through singular native prestages follows. The baseline increment is not automatically external physical energy. [R6.1]

At κ=0, the old subsystem is exactly RX for **every** preparation of the new states. The separated added subsystem can still evolve from its own stock. My previous work-order sentence, “Zero new activity also requires empty new states,” incorrectly suggested necessity. The controlling correction is:

> At zero coupling, empty added states are sufficient, not necessary, for inactivity. Nonempty added states may evolve, or may remain stationary.

The counterexample is explicit: take empty traveling fields and a nonzero `ζ_0(X)=(0,h(X)n)`, where n is normal to the carrier plane. Then `C*ζ_0=0`; all boundary waves vanish and ζ stays constant with positive stock. The analytical start already states the correct sufficient condition, so no candidate equation or theorem changes. Preserve the historical work order and carry D01 as a separate clarification. [R1, R6.2]

At positive coupling the carrier force changes the coupled trajectory. The unchanged form of the native and old-z equations therefore does not automatically transfer earlier capacity, recovery, credit or convergence theorems.

## 8. T07 — positive latency and a carrier-funded activity witness

**Accepted as stated.** With empty added states, receiving stock vanishes through the minimum delay, and incoming b vanishes a.e. before twice that delay. Immediate launch through `-κ²Q` remains present; only the incoming return is delayed. [R7.1]

For the declared constant preload `Q_0=(P,0)`, `P>0`, with native x and old z initially zero, x remains zero while z obeys its retained dynamics. Before return, finite H1 profiles and constant H1 carrier preparation give temporary H1 continuity. This supplies the strictly positive short-time scalar carrier bound needed for receiving. The scalar integrating-factor argument and positive-measure strict delay sublevels establish `H_G(t)>0` on the stated nonempty early interval, including when a minimizing G point is an endpoint or elbow. [R7.2–R7.3]

The return estimate is also correctly normalized. The far-effort/direct lower-bound ratio is

\[
\frac{8a_o^2ML\,\varepsilon}{\beta_G\delta_w^2}<\frac12
\quad\text{when}\quad
\varepsilon<\frac{\beta_G\delta_w^2}{16a_o^2ML}.
\]

This yields a strictly nonzero incoming b on a positive-measure channel set, a.e. in the specified later interval. Nonzero b alone establishes neither nonzero projected `J*b`, positive net carrier work, native credit nor recovery. [R7.4]

The witness is funded by declared carrier preload, not native empty-launch supply. It gives no capacity fraction, equal/simultaneous six-way allocation or physical aperture flux. Temporary H1 regularity in this witness does not strengthen the general energy-space theorem.

## 9. Assessment closed; manuscript next

All seven claims may now be carried forward as accepted mathematical results under their specified hypotheses, with D01 controlling inactivity wording. The supplied limits are part of the accepted scope, not unresolved mathematical corrections.

The constructive gap addressed here is explicit: one causal state extension now supplies nonnegative transport and receiving stocks, exact coupled work, global forward mild evolution and a delayed receiving/incoming-return witness. C6 remains exactly identifiable as the direct component. [R1–R7]

Physical attachment remains open. Endpoint distance divided by the inherited observation speed is delay data; a curved detour at the same speed generally changes travel time. The product channel measure does not itself supply material density or remove overlap multiplicity. G remains the actual labeled broken arcs. No physical aperture, toroidal return path, receiving location, irreversible load or clock is adopted. The author's stationary supports, central meeting region, opposed directions, outward spread, curved return and possible elsewhere transfer remain the intended correspondence questions. [R8; retained geometry/model boundary]

**Next:** commission one complete manuscript combining accepted W01–W05 and T01–T07, then review the actual paper with the author. No additional mathematical investigation or author geometry decision is needed before that scoped manuscript. The previously published central-route/six-opening edition remains closed. The standing gravity–magnetism, outer-geometry, SRG and later receiving/recovery directions retain their existing place.
