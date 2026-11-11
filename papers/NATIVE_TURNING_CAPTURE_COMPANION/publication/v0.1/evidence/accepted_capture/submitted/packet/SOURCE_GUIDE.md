# Source guide

## Reading checkpoint and use

Repository: `pzychozen/trioctagon-physics`  
Latest supplied publication checkpoint: `564810272703403af413e60ee2d44b32effbd79a`.

This is a **reading reference**, not an instruction to reset a checkout. It is not a claim that current remote HEAD has been freshly checked. No publication re-audit is commissioned. The original collective paper was published at `7cc1fa03af589818bcdcfaaac51838cc36c84253`.

Full primary-paper bytes are not bundled. They are located below; use the existing accessible local corpus or immutable source retrieval, without asking the author to find old parameters. Dated Library handoffs were inspected as text during preparation but had no authorized raw-byte export; they are identified, not misrepresented as included originals.

## Primary sources

### A. Collective Turning and Coherent Relaxation

Directory: `papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/`.

- `main.tex`: controlling scientific text. At the reading checkpoint, Git blob `de060bd217261af9bc87a52f0a79fe6fa4f6495d`.
- `CLAIM_SOURCE_MAP.md`: inherited versus completed claims.
- `evidence/turning_witness_20261028.json` and its `.py`: original two-step certificate and method; read without replaying the whole old investigation.
- `evidence/moving_mean_domain_constants_20261028.json` and its `.py`: domain constants, not a capture trajectory.
- `references.tex`: resolves referenced original source reports.

Read the abstract and `sec:overview` (explicit missing single-trajectory connection); `eq:parameters`, `eq:entrance`, `eq:certturn`, `eq:ratio`; `sec:domain`, `lem:phase`, `eq:apos`, `eq:lower`, `eq:upper`; `thm:convergence`, `eq:phasebound`, `eq:fullbound`, `eq:limits`, `eq:Cdecay`; `sec:prior` (scope distinctions from NRG/Paper G/D1).

Immutable main source:
https://github.com/pzychozen/trioctagon-physics/blob/564810272703403af413e60ee2d44b32effbd79a/papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/main.tex

### B. Native implementation

`kernel_physics/dynamics.py`, especially `arg0`, `phase_sync`, `_advance`, `step3`.

A byte-identical reference with Git blob `4283c9929fa8b0df18234a23ea9adf4ebce98510` is included at `inputs/reference/dynamics.py`. It was extracted from the supplied central-route review archive and matched by Git-blob identity to the current reading-checkpoint fetch. Its implementation uses complex128; its docstring explicitly distinguishes numerical arithmetic from the exact formula.

### C. Most likely later overlap

Use the following directories and their actual README/source ledgers to resolve canonical files. Do not assume all publication layouts use the same manuscript filename.

- `papers/COHERENCE_RETURNS_AND_PHASE_REMAINDER_BOUNDS/publication/v0.1/`
- `papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/`
- `papers/PHASE_RECONSTRUCTION_AND_STATIONARY_SUPPORT_AXES/publication/v0.1/`
- Natural Core Motion correspondence/return evidence and `docs/methods/Z_MOTION/` where relevant.

### D. Earlier native response and other capture mechanisms

- `papers/NATIVE_RESPONSE_GEOMETRY/`, including `provenance/THEOREM_LEDGER.md`, response/spectral/closure sources and GR0–GR2/CM0/SA0 source crosswalks.
- `papers/PAPER_G/`, M1–M3; identify actual entrance, parameters and certificate rather than assuming equivalence from the word capture.
- `papers/MEASUREMENT_AND_CHIRAL_DRIFT/v0.1/`, D0/D1 and source labels.
- `research/mathematical_atlas/README.md` and the repository research index for further relevant native results.

The primary collective paper's `sec:prior` directly discusses why local positive-branch stability, twisted chiral drift and Paper G's cycle are different statements. That discussion is a starting map, not a substitute for checking later coverage.

## Historical context retained and superseded status

The selected November 9 handoff and completion list are copied unchanged from the supplied packet. Their “next” directions are historical. Subsequent central-route/six-opening work and W/T/D01 have completed; the latest supplied receipt records publication of W/T/D01 at `564810...`. The author's newer direction is native discovery with a prior-work gate, not automatic further transport construction.

## Source limitations

No claim-by-claim audit of the entire project was completed to prepare this order. The targeted primary source and status evidence support a specific candidate gap. Codex must finish the bounded overlap check before treating a finite-entry result as new. An unavailable controlling source is a source limitation, not permission to assume the answer.
