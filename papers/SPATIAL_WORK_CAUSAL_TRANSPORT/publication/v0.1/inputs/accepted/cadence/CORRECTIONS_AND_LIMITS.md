# Corrections, clarifications and remaining gaps

Codex review, 9 November 2026. Original inputs are unchanged.

## Mathematical disposition

No formula, rational coefficient, sign threshold, source-bound constant or asymptotic limit in the GPT analytical start required correction. F01–F12 are verified with the hypotheses and limits stated in the proof review. This is Codex's independent disposition, not an already-issued GPT/author acceptance of this new investigation.

## Documentary corrections

1. In inputs/analysis/NATIVE_MAP_AND_FIRST_JUMP.md, section 1, the reference to sources/SOURCE_IDENTITIES.json is a stale locator. The actual supplied inventory is inputs/SOURCE_IDENTITIES.json, at the packet root. Its 144 entries identify all source copies.
2. In inputs/analysis/CADENCE_LIMITS_AND_POSTF_LOCAL_GEOMETRY.md, “Exact sources” gives an earlier staging prefix, publish_order/packet/publication_payload/papers/NATIVE_CAPACITY_RECEIVING_RECOVERY/publication/v0.1/. That staging prefix is not a delivered packet directory. The corresponding source files are under inputs/sources/receiving_recovery/publication/v0.1/. SOURCE_LOCATORS.json resolves every required label at the actual preserved path.

These are path corrections in this review, not scientific source contradictions. No input file is edited.

## Notation and qualification clarifications

- The analytical start uses f_+ for the complete post-jump vector, while + is also a raw-port label. The proof uses f^{post} for the vector and f_{raw,±} for individual port components. The raw registration signs are unchanged.
- “Uniform source lower bound” means a uniform positive coefficient multiplying sin²(phi), not a positive absolute bound as phi approaches zero. It supplies no uniform remainder in time on its own.
- The invariant floor L is constant within an exchange interval. The instantaneous capacity C=H_N−L generally is not; C+E is constant there. At jumps both the invariant level and floor can change.
- Pre-jump sampled accounts include b_0 through b_{N−1}; a post-jump window from 0+ to (Nh)+ instead includes b_1 through b_N. The proof spells out both conventions.
- The post-F capacity expansion is local, with fixed nonzero native detuning. Its O(phi⁴) remainder follows from analyticity, parity and a strictly selected branch; exact arithmetic alone does not establish that remainder.
- The real-state dark-iterate argument concerns exact mathematics. Floating evaluation of sine at integer multiples of pi need not give exact machine zeros.

These retain or make explicit the analytical start's intended qualifications rather than changing its mathematics.

## Remaining gaps

The original capacity-sized receiving and quantified return theorem has not been extended to the actual F-first post-jump state or to repeated preloaded hybrid intervals. No phase-uniform small-time remainder, explicit neighbourhood for the local capacity branch, selected physical cadence, uniform infinite-step bound or N≈T/h limit is proved. None is silently inferred from an exact account, nonzero initial source, asymptotic ceiling ratio or fixed-N convergence.

Failure to inherit the prior theorem is not a proof that the hybrid cannot receive and return storage. An additional argument would be needed to establish that behavior. No new modeling premise or author decision is needed to finish this first bounded assessment; a later physical-clock choice would require one.
