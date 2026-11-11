# Source and claim guide

All paths in this guide are relative to the packet. Inside `inputs/accepted_capture/submitted/`, the original relative paths and ledger references are unchanged.

## Read these first

| Purpose | File or locator |
|---|---|
| Accepted disposition and exact qualifications | `inputs/accepted_capture/NATIVE_TURNING_CAPTURE_01_GPT_REVIEW.md`, sections 1–4 and 6 |
| Machine-readable acceptance | `inputs/accepted_capture/GPT_ACCEPTANCE.json` |
| Current underlying proof | `inputs/accepted_capture/submitted/NATIVE_TURNING_CAPTURE_01_PROOF_REVIEW.md`, R2, R4–R7 |
| Distinct-gap comparison | `inputs/accepted_capture/submitted/PRIOR_WORK_COMPARISON.md` |
| Original 16-record claim ledger | `inputs/accepted_capture/submitted/CLAIM_LEDGER.json` |
| Exact trajectory certificate | `inputs/accepted_capture/submitted/data/CERTIFICATE.json` |
| Terminal values and recorded independent checks | `inputs/accepted_capture/submitted/data/CERTIFICATE_CHECK.json` |
| Recorded damaged-input controls | `inputs/accepted_capture/submitted/data/CHECKER_NEGATIVE_CONTROLS.json` |
| Presentation-only numerical history | `inputs/accepted_capture/submitted/data/EXPLORATION.json` |
| Unchanged generator and independent checker | `inputs/accepted_capture/submitted/scripts/generate_certificate.py`, `check_certificate.py` |
| Original execution evidence | `inputs/accepted_capture/submitted/logs/` |
| GPT corroborating replay and environment-only adapter | `inputs/accepted_capture/reviewer/` |
| Original submission and final-delivery audit | `inputs/accepted_capture/received/` |

## The inherited paper

`inputs/accepted_capture/submitted/sources/collective/main.tex`

Use labels rather than stale page numbers while drafting:

- `eq:pre`, `eq:kicks`, `eq:post`: ordered native recurrence.
- `eq:parameters`, `eq:entrance`: unchanged coefficients and original seed.
- `eq:turn`, `eq:certturn`: inherited early turning and strict enclosure.
- `sec:domain`, `thm:convergence`: invariant domain and inherited convergence theorem.
- `eq:fixed`, `eq:beta`, `eq:forcing`, `eq:radialbound`, `eq:fullbound`: fixed profile and accepted quantitative estimates.
- `eq:limits`, `eq:Cdecay`, `eq:area`, `eq:attach`: inherited observable definitions and limits.
- `sec:overview`, `sec:prior`: the earlier missing connection and distinct alternative regimes.

The bibliography and `CLAIM_SOURCE_MAP.md` alongside it give edition and source provenance. The primary manuscript SHA-256 is `40b6ca84ca136453b045386e2dead012fc8fcd7984b845d159ae6d6c8a6c2292`; computed Git blob identity `de060bd217261af9bc87a52f0a79fe6fa4f6495d`.

Repository-relative reading path: `papers/COLLECTIVE_TURNING_AND_COHERENT_RELAXATION/v0.1/main.tex`.

Recorded publication checkpoint: `7cc1fa03af589818bcdcfaaac51838cc36c84253`.

Recorded later reading context: `564810272703403af413e60ee2d44b32effbd79a`.

No current remote check is claimed by this packet.

## Original ledger IDs and manuscript treatment

These are the IDs in `submitted/CLAIM_LEDGER.json`, not the investigation's N01–N05 work-package numbering in proof R1.

| Ledger record | Treatment in the companion manuscript |
|---|---|
| I01 | Inherited model/coefficients/seed; state exactly and cite. |
| I02 | Inherited strict early turning; cite, not a new turning theorem. |
| I03 | Inherited invariant-domain/convergence theorem; state hypotheses and reuse. |
| I04 | Inherited estimates, unequal spread and area limits; apply with index shift. |
| I05 | Inherited mean accounting; mention only as needed for the no-sole-cause qualification. |
| N01 | Bounded prior-work assessment. Not a mathematical theorem or worldwide novelty result; preserve this interpretation even though the historical ledger groups it under a broader status label. |
| E01 | Numerical exploration only: apparent first hit 41 and target selection 50. Optional brief methodological sentence; never proof of earliest entry. |
| N02 | Connected exact certificate and positive prestages: principal finite proof mechanism. |
| N03 | Strict inclusion at index 50: central result. |
| N04 | Same-trajectory convergence: new application of the inherited theorem. |
| N05 | Qualitative same-coefficient open neighborhood: short corollary and proof. |
| U01 | Earliest entry unassessed; explicitly retain. |
| U02 | No explicit neighborhood radius; explicitly retain. |
| X01 | No global basin, new parameter regime, replacement seed or scan. |
| X02 | No inference of finitely many remaining direction changes. |
| X03 | No physical force/position/gravity/magnetism/clock/transport/receiver identification. |

A manuscript-specific ledger should map all 16 records to actual manuscript locations or a justified omission of a nonessential inherited/numerical item. This is coverage, not a count of 16 new theorems.

## Exact controlling identities

| Item | SHA-256 |
|---|---|
| Complete GPT acceptance archive | `411ae5eeeec97a62245d2dd5fb37bc86e7f64ce23cfe507d9c05c31dc2f9ca11` |
| Original research review ZIP | `c9fd8d7bb366dd882a9f7457e943345f06fba7b0e335a161aa7e66435af1ca6e` |
| Codex proof | `7f57b3e87272a6be822ed8e1f211e62de56d6556224a136193347b1108da8f72` |
| Exact certificate | `1244cafe2e8aa6b646aa25b4784102f4ce085c90464e5087b3cf01bde43782a1` |
| Submitted independent checker | `f7b01f38bd897399812c1adb748dd88de6d90a08da7d77136267350d49c6b32e` |
| GPT scientific review | `cb2abf9432938c96a9bdb302b0b6d96f19ee243e7f1854b6702467ab3f70be14` |

The originals, their source identities, logs and qualifications remain unchanged. Read them; do not re-execute prior instructions simply because they are packaged here.
