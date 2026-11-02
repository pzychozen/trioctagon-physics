# Claim/source ledger — NATIVE_SPATIAL_CORRESPONDENCE_01

2 November 2026. This ledger separates accepted definitions and results from the deductions proved in `NATIVE_SPATIAL_CORRESPONDENCE_01_PROOF_REVIEW.md` (abbreviated **Note**). It records the exact local sources read. A source hash identifies bytes; it does not certify every result in that source or a live Git HEAD.

## Claim dependencies and applicable domains

| Claim | Status | Source or new proof | Applicable domain and limitation |
| --- | --- | --- | --- |
| C01. Exact ordered map, fixed tuple, invariant coherent domain and regularity | Accepted input | PS §2 `sec:setting`, `eq:pre`, `eq:full`; PC §5 `thm:autonomy`, `eq:semiconjugacy`, `eq:iterates`; PH §2; W §3 | Exact triad tuple; amplitudes [0.9,1.1], ordinary phase width ≤π/12, arbitrary common angle. No global zero-stratum extension. |
| C02. Positive-root representative, joint-span image, third pair and common-phase fibres | Accepted input | PC §5 `thm:reconstruction`, `eq:roots`, `eq:thirdpair`, `eq:representative`, `eq:radicands`, `prop:image`, `eq:span` | Entire closed image, including zero individual areas, coincident phases and equal amplitudes. Independent area bounds are insufficient. |
| C03. Unit factor, all-step state reconstruction and canonical ordinary lifts | Accepted input; acceptance recorded in current W §1 | PH §§3.1–3.3, equations (7)–(13); §3.4 aligned relaxation | Same fixed domain; requires original initial unit phase for a particular full-state history. No helper rerun or reopened convergence proof. |
| C04. Overlap correction and representative dependence | Accepted input | PH §§5–6, equations (21)–(25), (28)–(33) | Canonical overlap is not the anchor increment; changed representative and unit factor must change together. No arbitrary global argument assumption. |
| C05. Exact centers, normals, tangents, origin, labels and implementation conventions | Accepted definitions; transcription reconciled here | NA `app:notation`, exact frame table at lines 19–26; FS lines 22–24 and `face_frames`, `decode_to_faces`, `encode_from_faces`, `transport` | The adopted fixed folded-host frame; 1/A/P1 corresponds to Python index 0, then 2/B/P2/1 and 3/C/P3/2. FS only read, not imported or executed. |
| C06. Centered fixed-gap origin, support directions and stationarity/attachment distinction | Accepted definitions and conditional geometry result | FG §1 and §3; FGR §§1–3, 6 | Reference directions g_k with the source's orientation and translation by O. A stationary line is not automatically a material rod or attachment. |
| C07. Positioned lines agree: n_i=-g_(i-1), c_i-O=r n_i, ell_i=L_(i-1); directed angle reverses | New source-comparison deduction | Note §2.2, equations (6)–(9), using C05–C06; exact helper groups 1, 2, 5 | Exact specified fixed frames; equality of positioned unoriented lines, no fit, reflection or permutation. Not a new material identification. |
| C08. Lossless decoder, tangent-plane inverse, projector on ambient arrays and existing face update | Accepted construction, algebra checked here | NO `sec:attachment`, `eq:decoder`, `eq:faceupdate`; FS named functions; Note §§3.1–3.2 | D/E are inverse on the direct sum of tangent planes, not unrestricted ambient arrays. Transport is rank two ambiently. |
| C09. Pure complex rephasing is the signed local normal-axis rotation; based endpoint rotates about that support | New explicit composition of existing definitions | Note §3.1, equations (11)–(13), using C07–C08; exact helper groups 3–5 | Algebraically all complex channel values, including zero, and all real phase angles. This broader algebraic domain does not extend the native reconstruction theorem. |
| C10. Reconstructed face history and commuting relation | New deduction from accepted reconstruction and decoder conjugacy | Note §3.2, equations (15)–(16), using C03 and C08 | All mathematical iterates of the fixed invariant domain. No numerical trajectory or second recurrence. |
| C11. Channel angular increment and length change; gauge-independent decoded vectors | New composition and subtraction using accepted lifts | Note §3.3, equations (17)–(20); PH §§3.3–3.4, 6 | Same domain, consistent ordinary lift. Zero aligned phase increment can accompany changing lengths. Actual rephasing differs from a representative change. |
| C12. Universal fixed-label ambient proper rotation exists iff chi=0 mod 2π | New quantified result | Note §4, equations (21)–(23); exact helper groups 6–7 | Q independent of state, acting on the three free vectors, every state in D. No moved centers, channel permutation or individual-registration classification. Both witnesses have modulus one and width zero. |
| C13. I and raw channel C factor through y; raw C is not ambient axial W | Accepted definitions plus retained composition | PC `eq:thirdpair`; NO `eq:chiral` and adjacent raw/ambient distinction; Z §3 C07/C09; Note §5 equation (24); helper group 8 | Entire Y. Uses raw (a23,-a13,a12), not a substituted ambient projection. |
| C14. Staged Z, placement and fixed-geometry measurements factor through y plus external data; equal retained starts and schedules give equal staged histories | Immediate composition of accepted closure and observation formulas | Z §§3, 8 C07–C10/C22; PC `thm:autonomy`; Note §5 equation (25) and dependency table | Current exact native domain for the all-step statement. No autonomous closure on Z alone or assumed observer schedule. Frozen settings leave dependence on native retained state. |
| C15. Reconstructed phase determines cubic innovation; EMA history also needs memory and ordering | Accepted observer definition plus elementary phase covariance | Z §8 C24; Note §5 equation (26) and dependency table | The cubic formula applies to reconstructed states; no recovery of unknown initial memory, update-order choice or EMA advance. |
| C16. Historical Z tuples are different and not covered by the new history statement | Source reconciliation | Z §2 coefficient table; Note §5 final paragraph | No Z01/Z02/Z03 replay, coefficient replacement or transfer of the present invariant-domain theorem. |
| C17. No material feature, spatial pose, clock/time/geometry-parameter identification follows; stationary support and author alternatives remain fixed | Accepted author/review boundary, maintained here | W §§1, 6–7; NO `sec:attachment` following `eq:decoder`/`eq:faceupdate`; FG recommendation; FGR §§3, 6; Note §6 | No new body motion, attachment, aperture, force, flow, emission, observer or interpretation choice. One conditional feature-identification question remains for discussion, not for completing the proof. |
| C18. Execution and source-preservation statements | Actual task records | `exact_algebra_results.json`, `SOURCE_IDENTITIES.json`, `PREPARATION_REPORT.md`, `REVIEW_PACKAGE_MANIFEST.json` | Static symbolic and focused file checks only; no claim of native numerical validation or reconstruction of historical audits. |

## Actual source identities

The retained publication worktree was used directly. Commit `634ff13b666604d5caed11cc3731dcb5a863ff6c` is the order's reading reference; no Git query established or changed a checkout HEAD. NRG files without an in-file edition number are identified by their actual copy and hash rather than an invented version.

The available fixed-gap report is byte-identical to the accepted raw report identity `bc43cadd16d4235cda17fc42f082e5fa6fe579158ac3ed9ad779687fb4ec9da8`. Its accepted archive identity is supplied by W and FGR, but that archive was unnecessary and was not re-audited. The separate phase-review acceptance is supplied by W §1; a separate GPT phase-review file is not used or claimed to have been read.

**W** — [C:/Users/Notandi/Downloads/NATIVE_SPATIAL_CORRESPONDENCE_01_CODEX_WORK_ORDER.md](<C:/Users/Notandi/Downloads/NATIVE_SPATIAL_CORRESPONDENCE_01_CODEX_WORK_ORDER.md>)  
Version/copy: Current order, 2 November 2026; records phase-review acceptance.  
Locator: Sections 1-7: authorized scope, candidates and review endpoint.  
SHA-256: `d119719c16bdecde1f99da559952fc959c28e096bf210ba1c6d392be6120c71a`; 19396 bytes.

**PH** — [C:/TORMENT/TRIOCTAGON_new/research/NATIVE_PHASE_RECONSTRUCTION_01/NATIVE_PHASE_RECONSTRUCTION_01_PROOF_REVIEW.md](<C:/TORMENT/TRIOCTAGON_new/research/NATIVE_PHASE_RECONSTRUCTION_01/NATIVE_PHASE_RECONSTRUCTION_01_PROOF_REVIEW.md>)  
Version/copy: Local phase proof review, 2 November 2026; accepted disposition supplied by W section 1.  
Locator: Sections 2-3, 5-7; equations (7)-(13), (21)-(25), (28)-(33): reconstruction, ordinary lift, correction and section change.  
SHA-256: `0ce3d59e249ee7794c3386047e2bf79f9d7a83b76ec563c8541de4b66c35f2c6`; 40656 bytes.

**PS** — [C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/setting.tex](<C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/setting.tex>)  
Version/copy: Published research edition v0.1 in the retained publication worktree.  
Locator: Section 2 sec:setting; eq:pre, eq:full; native order, zero convention and regular equivariance.  
SHA-256: `f0b3113ce197085b6175e7a8b738d37c9f6f8785f67b0376341353757940edfe`; 4790 bytes.

**PC** — [C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/coordinates.tex](<C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_POTENTIAL_AND_CLOSED_COHERENCE/publication/v0.1/manuscript/coordinates.tex>)  
Version/copy: Published research edition v0.1 in the retained publication worktree.  
Locator: Section 5 thm:reconstruction, prop:image, thm:autonomy; eq:roots, eq:thirdpair, eq:representative, eq:span, eq:semiconjugacy, eq:iterates.  
SHA-256: `f244a48b9203c5a4d703097635d6b745ed7b0f2e072602e86bce0f13784e0137`; 7792 bytes.

**NO** — [C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_RESPONSE_GEOMETRY/manuscript/observables_closure.tex](<C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_RESPONSE_GEOMETRY/manuscript/observables_closure.tex>)  
Version/copy: NRG manuscript copy in the retained publication worktree; exact bytes identified below.  
Locator: sec:observables eq:chiral; sec:attachment eq:decoder and eq:faceupdate; adopted tangent-state definitions and conjugacy.  
SHA-256: `fd3316c3845657e00cf3e0d103b9b13b605436a35b458c34f61dcceb41ef4aa4`; 16125 bytes.

**NA** — [C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_RESPONSE_GEOMETRY/manuscript/appendices.tex](<C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/papers/NATIVE_RESPONSE_GEOMETRY/manuscript/appendices.tex>)  
Version/copy: NRG manuscript copy in the retained publication worktree; exact bytes identified below.  
Locator: app:notation, exact shell-frame table immediately after the notation table, lines 19-26.  
SHA-256: `83c1c5e87dba36537f94b2644430363502af8c9824ec56986ff10303e0424e7d`; 11158 bytes.

**FS** — [C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/kernel_physics/face_state.py](<C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/kernel_physics/face_state.py>)  
Version/copy: FRAME_ID=face_center_tangent_ez_v1; TRANSPORT_ID=c3_matched_zero_phase_v1.  
Locator: FACE_ORDER; face_frames, decode_to_faces, encode_from_faces, transport; read only, never imported.  
SHA-256: `be9d1e25a6f368e644ecfa9b1af70ba9382599e8b4d43d529d1783004d86ded7`; 8721 bytes.

**Z** — [C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/docs/methods/Z_MOTION/v0.1/manuscript/NOTE.md](<C:/TORMENT/TRIOCTAGON_new/research/NATIVE_POTENTIAL_INFORMATION_PUBLISH_01/publication_worktree/docs/methods/Z_MOTION/v0.1/manuscript/NOTE.md>)  
Version/copy: Explanatory methods note, draft v0.1, 1 November 2026.  
Locator: Sections 2, 3 and 8, especially C07-C10 and C22-C24: staged data, placement, common-phase invariance and separate EMA.  
SHA-256: `0e1c3fd6ff4e0ec742d6856305b3ba10b565b9beb93e29b28d8df4985eb8c0c1`; 32801 bytes.

**FG** — [C:/TORMENT/TRIOCTAGON_new/research/NATURAL_CORE_MOTION_Z_FIXED_REFERENCE_01/packet/REFERENCES/NCM_FIXED_GAP_01_REPORT.md](<C:/TORMENT/TRIOCTAGON_new/research/NATURAL_CORE_MOTION_Z_FIXED_REFERENCE_01/packet/REFERENCES/NCM_FIXED_GAP_01_REPORT.md>)  
Version/copy: NCM-FIXED-GAP-01 v0.1, 31 October 2026; raw report hash prescribed in W.  
Locator: Sections 1 and 3: centered frame, O, g_k and stationary support lines; recommendation: attachment boundary.  
SHA-256: `bc43cadd16d4235cda17fc42f082e5fa6fe579158ac3ed9ad779687fb4ec9da8`; 27375 bytes.

**FGR** — [C:/TORMENT/TRIOCTAGON_new/research/NATURAL_CORE_MOTION_Z_FIXED_REFERENCE_01/packet/REFERENCES/NCM_FIXED_GAP_01_GPT_REVIEW.md](<C:/TORMENT/TRIOCTAGON_new/research/NATURAL_CORE_MOTION_Z_FIXED_REFERENCE_01/packet/REFERENCES/NCM_FIXED_GAP_01_GPT_REVIEW.md>)  
Version/copy: GPT review, 31 October 2026; ACCEPTED bounded conditional geometry.  
Locator: Sections 1-3 and 6: accepted identities, stationarity, distinction between lines and a material attachment.  
SHA-256: `bb1ba09b703cf63ebd482638f22635c1ae69c4db989a38a251342ba0f0ab8d64`; 10642 bytes.

## Unverified provenance or mathematical dependency

None is blocking or unresolved for the commissioned source/frame comparison. Exact decoder constants came from the accepted NRG table, support constants and origin from the hash-matched fixed-gap report, and labels/formulas from read-only implementation text. No import-time shell construction or floating-point implementation certification is claimed. Source identities do not establish a material interpretation, and the ledger does not claim independent re-verification of inherited convergence, descent or historical geometry certificates.
