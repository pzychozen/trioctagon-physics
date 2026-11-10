# Functional review of the submitted causal transport candidate

**Task:** NATIVE_CAUSAL_TRANSPORT_STORAGE_01  
**Date:** 10 November 2026, Atlantic/Reykjavik  
**Review scope:** T01, T02, T04 and T05, with the component energy calculation needed for T04.  
**Disposition:** Accept the four claim groups as stated at their submitted assumptions. No equation or mathematical theorem correction is required in this scope.

## Material examined

- Submitted `upload/NATIVE_CAUSAL_TRANSPORT_STORAGE_01_PROOF_REVIEW.md`, in particular R0–R5 and the stated T06 distinction between the spatial and temporal adjoints.
- Original `deliverables/NATIVE_CAUSAL_TRANSPORT_STORAGE_01/NATIVE_CAUSAL_TRANSPORT_STORAGE_01_GPT_ANALYTICAL_START.md`, sections 1–7 and equations N1–N17.
- Retained RX `candidate.tex`, `power.tex` and `wellposed.tex` under that deliverable's `sources/RX/` directory: spaces, bounded finite-width ports, polynomial native feedback, original reciprocal energy cancellation and periodic carrier group.

This was a direct mathematical review. It neither reran Codex's Windows checks nor treated finite-dimensional symbolic checks as proof of infinite-dimensional assertions.

## Findings

### T01 — exact bounded spatial factorization

The duplication normalization gives `J*J=I` exactly in the declared arclength product spaces. Cauchy–Schwarz in carrier arclength supplies the stated bound for C, while Fubini proves its adjoint. The factors of `sqrt(M)` cancel in `C D_theta J`, retaining C6's coefficient. The time shift depends on the fixed channel label, so its whole-time L2 isometry follows from translation in time at each label and Fubini; it does not require evaluating arbitrary L2 histories at one prescribed instant.

The pointwise Gram formula is correct. Its scalar block is bounded below by a positive constant at the fixed finite geometry. Its vector block can have the carrier-plane normal in its kernel. The proof neither requires invertibility nor silently assumes C is a contraction. No transfer of a power normalization through C alone is asserted.

### T02 — variable-length transport in the energy space

Both characteristic orientations and startup outflows agree with the stated PDEs and boundary orientations. Startup and delayed portions have disjoint supports in time for each label. Therefore the trace inequalities need no extra factor two. Substitution on each fiber, followed by Fubini, makes the time traces representative-independent and locally L2.

The strong-continuity argument is sound: zero extension, translation on the full label-by-real-coordinate L2 space and restriction produce the forward state continuously; the backward state follows by the fixed, measure-preserving fiber reflection. This remains true when boundary corners do not match. The direct squared-profile formula supplies the integrated energy balance for every endpoint time without unsupported spatial boundary traces or integration by parts for rough states. No derivative of the static delay field is used.

### T04 — noncircular global forward mild construction

Choosing slabs no longer than the strictly positive minimum delay makes both incoming signals depend only on initial profiles and previously constructed outgoing histories, apart from irrelevant endpoint values. The known incoming signals are locally L2. On each slab, the RX variables satisfy a semilinear integral equation with locally Lipschitz polynomial feedback, bounded damping and additive L1 forcing; the receiving field separately satisfies a bounded-generator Hilbert-space ODE.

The interaction variable formed with the inverse unitary carrier group is absolutely continuous. Its Hilbert-space chain rule gives the carrier norm derivative for L2 carrier preparation. Native and old-receiver chain rules are ordinary finite-dimensional ones because their bounded-port right-hand sides are continuous. This establishes the RX energy inequality before the total conservation law is used. Its coercive bound controls all RX coordinates; the integrable interaction-variable derivative gives a finite limit at any putative finite maximal endpoint, allowing continuation. Thus the argument is not circular.

Once the slab solutions exist, the outgoing boundary laws, transport identity and receiving chain rule give augmented conservation. Induction produces every finite forward horizon. Uniqueness follows by the same slab induction. The stated dependence estimates also close: initial-profile differences and previous outgoing histories bound incoming differences; local integral estimates bound subsystem differences; characteristic energy estimates bound the evolving transport difference. For a fixed finite horizon there are finitely many slabs. Local Lipschitz dependence on bounded initial-energy sets is justified with constants depending on that bound, the fixed parameters and the horizon.

### T05 — exact C6 term with honest history data

Direct substitution of the near boundary law into the forward characteristic yields the displayed zero-extended formula. The direct coefficient is `2*kappa`; the startup contribution has a plus sign. The independent forward profile is not incorrectly identified with a zero or a past RX history.

The complete-history formula follows under the two stated conditions: the initial forward profile equals the launched negative-time boundary history, and the near boundary relation also holds at those negative times. A supplied Q history alone would not be enough, and the proof correctly says so. After the maximum delay, the startup term vanishes and all displayed delay arguments are nonnegative.

C* is a same-time spatial adjoint. It is not the advanced finite-window temporal adjoint from W03. The loaded receiving equation includes delayed return and, for arbitrary preparation, startup contributions. The nonnegative quadratic transport preparation is not W05's signed bilinear prehistory term.

## Required manuscript scope

1. State fixed static geometry and fixed finite parameters, including positive lower delay, before the theorem. No moving-geometry or zero-delay limit theorem has been proved.
2. State the solution class explicitly: continuous energy-space state; native x and old receiver z are C1; the new receiver is locally absolutely continuous (indeed H1 in time on finite exchange windows); boundary signals are generally only locally L2 in time.
3. Retain the integrated energy argument. Do not replace it with formal integration by parts for arbitrary L2 preparation.
4. Do not claim global H1 regularity, unrestricted fixed-time boundary traces, backward existence, or uniform parameter-limit estimates.
5. Keep arbitrary initial profiles and compatible complete histories as distinct cases. Retain the startup term, its plus sign and the direct coefficient `2*kappa`.
6. State C6 as the exact direct observation component of the loaded response. Do not identify the entire new receiving field or drive with bare C6.
7. Keep the declared mathematical product measure and delay coordinate distinct from an embedded curved physical route, material density or physical aperture flux.

These are existing qualifications to preserve, not additional obstacles to acceptance or manuscript drafting.
